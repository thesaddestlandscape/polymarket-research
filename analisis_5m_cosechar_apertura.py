#!/usr/bin/env python3
"""5m: COSECHAR PARES AL ABRIR (Javi 14-Oct prioritaria; 15-Oct: "si funciona en 5m, tiene que haber una manera de que
funcione 100 % real en 5m barato"). SOLO LECTURA / simulación con NUESTRA cola (mismo modelo de rellenos que
analisis_5m_pares_maker_cola.py, clase Pata importada: venta tomadora del token a p <= b o compra tomadora del contrario a
p' >= 1−b; precio < b atraviesa y llena; == b llena lo que supere la cola de delante; t_ex en [post+68 ms, cancel+60 ms]).

Inspiración: cosechadores on-chain 0x21f4/0xaa1a/0x41e2 (entran al abrir, ~10 acc, par 0,974-0,985, +0,7/+1,3 %/vol);
0x21f4 persistente fuera de muestra (analisis_5m_wallets_baratas.py, 15-Oct).
POLÍTICAS FIJADAS ANTES DE MIRAR (15-Oct), BTC 5m, SH = 5 acciones por lado:
  - Entrada: en los primeros ENTRADA_S = 15 s de la ventana se cotiza en AMBOS tokens a b = PAR/2 (PAR ∈ {0,96, 0,98}) si
    b < ask. Cola: si b > mejor bid -> somos el nuevo top (cola 0); si b == mejor bid -> cola = tamaño del bid (FINAL) o 0
    (CABEZA, cota optimista no elegible); si b < mejor bid -> solo rellena lo que ATRAVIESA.
  - Tras rellenarse una pata, la otra queda cotizando a su b hasta T = 10 s (sin perseguir el precio): par <= PAR.
  - Defensa (solo mientras NINGUNA pata tiene rellenos): se cancelan las dos y se recolocan 2 s después de la última señal
      A0   sin defensa (todos los 5m)
      A_BN Binance BTCUSDT se mueve >= 2 bps en 1 s (recepción)
      B_15 solo 5m que cierran con un 15m; el bid del 15m del MISMO lado cambia >= 0,02 en 500 ms
    A0_15 = A0 restringida al mismo subconjunto que B_15 (comparación justa del valor incremental del 15m).
  - Fin: se cancela todo a T = 10 s; lo que quede sin pareja se valora al desenlace OFICIAL. Reembolso maker estimado
    aparte (20 % de 0,07·p·(1−p) por acción rellenada).
Partición: DESC 05-09 (elección de PAR y defensa entre las A, FINAL); OOS 10-14 juicio único. B_15 vs A0_15 en los mismos
mercados y días.
Salida: datalogs/m5_cosechar_apertura/mercados_D.csv.gz (caché) + informe.txt
Uso: nice -n 19 ionice -c3 python3 analisis_5m_cosechar_apertura.py [--dias ...]
"""
import argparse
import bisect
import collections
import csv
import gzip
import hashlib
import json
import os
import sys
import time
from array import array
from datetime import datetime
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_5m_pares_maker_cola as PM  # noqa: E402  (Pata, SH, latencias: mismo modelo de cola)
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5_cosechar_apertura")
DIAS = [f"2026-10-{d:02d}" for d in range(5, 15)]
DESC, OOS = DIAS[:5], DIAS[5:]
ENTRADA_S, T_FIN_S = 15, 10
REARME_MS = 2000
INF = float("inf")
POLS = [(f"{d}_P{int(p * 100)}_{c}", d, p, c) for d in ("A0", "A_BN", "B_15") for p in (0.96, 0.98)
        for c in ("FINAL", "CABEZA")]

TRUNCADOS = set()                                   # días cuyo m5_registro de origen estaba truncado (no se cachean)


def escribir_atomico(ruta, texto):
    """Escritura atómica (tmp + fsync + os.replace): un kill nunca deja el fichero final a medias."""
    ruta = Path(ruta)
    tmp = ruta.with_name(ruta.name + ".tmp")
    with open(tmp, "w") as fh:
        fh.write(texto)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, ruta)


def leer_cache(cache):
    """Filas de la caché o None. Se descomprime ENTERA (el CRC del gz detecta truncados); si falla o no tiene filas se
    borra y se recalcula (una caché vacía no cuenta como válida)."""
    if not cache.exists():
        return None
    try:
        with gzip.open(cache, "rt") as fh:
            filas = list(csv.DictReader(fh))
    except (EOFError, OSError, UnicodeDecodeError, csv.Error) as e:
        print(f"  {cache.name}: caché corrupta ({type(e).__name__}) -> se borra y se recalcula", file=sys.stderr, flush=True)
        cache.unlink()
        return None
    if not filas:
        print(f"  {cache.name}: caché sin filas -> se borra y se recalcula", file=sys.stderr, flush=True)
        cache.unlink()
        return None
    return filas


def escribir_cache(cache, filas):
    """Caché atómica (gz a <cache>.tmp + os.replace). Un día sin filas NO se cachea."""
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = cache.with_name(cache.name + ".tmp")
    with gzip.open(tmp, "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    with open(tmp, "rb") as fh:
        os.fsync(fh.fileno())
    os.replace(tmp, cache)


def serie_15m(d):
    """(cierre_ms, lado) -> (array horas recepción, array bid) del 15m BTC."""
    meta, ser = {}, {}
    f = VOL / "m15_registro" / f"m15_registro_{d}.csv.gz"
    if not f.exists():
        return {}
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                tp = ln[:2]
                if tp == "k,":
                    c = ln.rstrip("\n").split(",")
                    if len(c) >= 8 and c[3] == "BTC" and c[4] == "15min":
                        meta[c[2]] = (int(datetime.fromisoformat(c[6]).timestamp() * 1000), c[7])
                    continue
                if tp != "q,":
                    continue
                c = ln.rstrip("\n").split(",")
                m = meta.get(c[2])
                if not m or c[3] in ("", "None"):
                    continue
                try:
                    t_, b_ = ser.setdefault(m, (array("q"), array("d")))
                    t_.append(int(c[7]))
                    b_.append(float(c[3]))
                except (ValueError, IndexError):
                    continue
        except (EOFError, OSError):
            pass
    out = {}
    for k, (t_, b_) in ser.items():
        o = sorted(range(len(t_)), key=t_.__getitem__)
        out[k] = (array("q", (t_[i] for i in o)), array("d", (b_[i] for i in o)))
    return out


def simular_dia(d):
    cache = OUT / f"mercados_{d}.csv.gz"
    c_ = leer_cache(cache)
    if c_ is not None:
        return c_
    f = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    if not f.exists():
        return None
    s15 = serie_15m(d)
    meta, par, por_mkt, top = {}, {}, {}, {}
    est = {}                                        # (pol, token) -> Pata
    bloqueo = collections.defaultdict(lambda: -INF)  # (pol, mkt) -> hora hasta la que la defensa bloquea
    bn = collections.deque()                        # (t_rx, precio) Binance último segundo
    fins, mkts_ord = [], []                         # cierres ordenados -> mercados con ventana viva en O(log n)

    def con15(tk):
        fin = meta[tk][2]
        return fin % 900_000 == 0

    def señal15(tk, t_rx):
        k = (meta[tk][2], meta[tk][3])
        if k not in s15:
            return False
        t_, b_ = s15[k]
        i = bisect.bisect_right(t_, t_rx) - 1
        j = bisect.bisect_right(t_, t_rx - 500) - 1
        return i >= 0 and j >= 0 and abs(b_[i] - b_[j]) >= 0.02 - 1e-9

    def con_rellenos(nom, mkt):
        return any(est.get((nom, t)) is not None and est[(nom, t)].lleno > 1e-9 for t in por_mkt[mkt].values())

    def evaluar(pol, tk, t_rx):
        nom, defensa, PAR, colam = pol
        act, mkt, fin, lado = meta[tk]
        if defensa == "B_15" and not con15(tk):
            return
        T = (fin - t_rx) / 1000.0
        tp = top.get(tk)
        if tp is None:
            return
        o = est.get((nom, tk))
        if o is not None and o.lleno >= PM.SH - 1e-9:
            return
        hay = con_rellenos(nom, mkt)
        b = round(PAR / 2, 2)
        bid, ask, bsz = tp
        en_entrada = 300 - ENTRADA_S < T <= 300        # primeros 15 s DE LA VENTANA (no antes de abrir)
        # sin rellenos: solo se cotiza en la ventana de entrada (o al rearmarse tras la defensa, dentro de esa ventana)
        ok = T > T_FIN_S and b < ask - 1e-9 and (hay or en_entrada) and t_rx >= bloqueo[(nom, mkt)]
        if b > bid + 1e-9:
            cola = 0.0
        elif abs(b - bid) < 1e-9:
            cola = 0.0 if colam == "CABEZA" else bsz
        else:
            cola = INF
        if o is not None and o.viva(t_rx):
            if ok:
                return                               # sigue en su sitio (no perseguimos)
            o.cancelar(t_rx)
            return
        if ok and (o is None or not o.segs or o.lleno <= 1e-9 or hay):
            if o is None:
                o = est[(nom, tk)] = PM.Pata(fin - T_FIN_S * 1000)
            o.cotizar(b, cola, t_rx, fin - T_FIN_S * 1000)

    def defender(t_rx, tk_evento=None):
        """Aplica la defensa: cancela las patas SIN rellenos de los mercados afectados y bloquea REARME_MS."""
        i0 = bisect.bisect_right(fins, t_rx)          # solo ventanas vivas: cierre en (t_rx, t_rx + 300 s]
        i1 = bisect.bisect_right(fins, t_rx + 300_000)
        vivos = mkts_ord[i0:i1]
        for pol in POLS:
            nom, defensa = pol[0], pol[1]
            if defensa == "A0":
                continue
            for mkt in vivos:
                tks = por_mkt[mkt]
                if len(tks) != 2 or con_rellenos(nom, mkt):
                    continue
                tk0 = next(iter(tks.values()))
                if defensa == "A_BN" and tk_evento is None:
                    pass
                elif defensa == "B_15" and tk_evento is not None and con15(tk0) and \
                        any(señal15(t, t_rx) for t in tks.values()):
                    pass
                else:
                    continue
                bloqueo[(nom, mkt)] = t_rx + REARME_MS
                for t in tks.values():
                    o = est.get((nom, t))
                    if o is not None:
                        o.cancelar(t_rx)

    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                tp_ = ln[:2]
                if tp_ not in ("k,", "q,", "t,", "x,"):
                    continue
                c = ln.rstrip("\n").split(",")
                if tp_ == "x,":
                    if c[2] != "BTCUSDT":
                        continue
                    try:
                        t_rx, px = int(c[7]), float(c[3])
                    except (ValueError, IndexError):
                        continue
                    bn.append((t_rx, px))
                    while bn and bn[0][0] < t_rx - 1000:
                        bn.popleft()
                    if abs(px / bn[0][1] - 1) * 1e4 >= 2.0:
                        defender(t_rx)
                    continue
                if tp_ == "k,":
                    if len(c) >= 8 and c[4] == "5min" and c[3] == "BTC" and c[2] not in meta:
                        fin = int(datetime.fromisoformat(c[6]).timestamp() * 1000)
                        meta[c[2]] = (c[3], c[5], fin, c[7])
                        if c[5] not in por_mkt:
                            k_ = bisect.bisect_right(fins, fin)
                            fins.insert(k_, fin)
                            mkts_ord.insert(k_, c[5])
                        d_ = por_mkt.setdefault(c[5], {})
                        d_[c[7]] = c[2]
                        if len(d_) == 2:
                            a, b_ = d_.get("YES"), d_.get("NO")
                            if a and b_:
                                par[a], par[b_] = b_, a
                    continue
                tk = c[2]
                if tk not in meta or tk not in par:
                    continue
                if tp_ == "q,":
                    try:
                        top[tk] = (float(c[3]), float(c[4]), float(c[5]))
                        t_rx = int(c[7])
                    except (ValueError, IndexError):
                        continue
                    if señal15(tk, t_rx):
                        defender(t_rx, tk)
                    for pol in POLS:
                        evaluar(pol, tk, t_rx)
                else:
                    try:
                        p, side, sz, t_ex = float(c[3]), c[4], float(c[5]), int(c[1])
                    except (ValueError, IndexError):
                        continue
                    if side == "SELL":
                        obj, pe = tk, (p, sz)
                    elif side == "BUY":
                        obj, pe = par[tk], (round(1.0 - p, 4), sz)
                    else:
                        continue
                    for pol in POLS:
                        o = est.get((pol[0], obj))
                        if o is not None:
                            o.consumir(t_ex, pe)
        except (EOFError, OSError) as e:
            print(f"  {d}: fichero truncado ({type(e).__name__})", file=sys.stderr)
            TRUNCADOS.add(d)
    mkts = {meta[tk][1] for (_, tk) in est}
    des = desenlaces(mkts)
    print(f"  {d}: desenlace oficial {sum(1 for m in mkts if m in des)}/{len(mkts)}", flush=True)
    filas = []
    for pol in POLS:
        nom = pol[0]
        for mkt, tks in por_mkt.items():
            if len(tks) != 2 or mkt not in des:
                continue
            q, cst, reb = {}, {}, 0.0
            for lado in ("YES", "NO"):
                o = est.get((nom, tks.get(lado)))
                q[lado] = o.lleno if o else 0.0
                cst[lado] = o.coste if o else 0.0
                if o:
                    reb += sum(g[5] * 0.2 * 0.07 * g[0] * (1 - g[0]) for g in o.segs)
            if q["YES"] + q["NO"] <= 1e-9:
                continue
            r = des[mkt]
            pares = min(q["YES"], q["NO"])
            coste = cst["YES"] + cst["NO"]
            fin = meta[tks["YES"]][2]
            filas.append({"dia": d, "pol": nom, "mkt": mkt, "con15": int(fin % 900_000 == 0), "qY": round(q["YES"], 4),
                          "qN": round(q["NO"], 4), "coste": round(coste, 6), "pnl": round(q[r] - coste, 6),
                          "completo": int(pares >= PM.SH - 1e-9), "rebate": round(reb, 6)})
    if not filas:
        print(f"  {d}: dia_sin_filas (registro presente, 0 mercados con rellenos): no se cachea", flush=True)
    elif d in TRUNCADOS:
        print(f"  {d}: origen truncado: resultado parcial, no se cachea", flush=True)
    else:
        escribir_cache(cache, filas)
    return filas


def resumen(filas, pol, dias, solo15=False):
    x = [r for r in filas if r["pol"] == pol and r["dia"] in dias and (not solo15 or int(r["con15"]) == 1)]
    if not x:
        return "n=0"
    pnl = np.array([float(r["pnl"]) for r in x])
    coste = np.array([float(r["coste"]) for r in x])
    reb = sum(float(r["rebate"]) for r in x)
    comp = np.mean([int(r["completo"]) for r in x])
    pd_ = collections.defaultdict(lambda: [0.0, 0.0])
    for r in x:
        pd_[r["dia"]][0] += float(r["pnl"])
        pd_[r["dia"]][1] += float(r["coste"])
    ev_d = np.array([a / b for a, b in pd_.values() if b > 0])
    ic = None
    if len(ev_d) >= 3:
        bt = np.random.default_rng(7).choice(ev_d, size=(5000, len(ev_d))).mean(axis=1)
        ic = (round(float(np.percentile(bt, 5)), 4), round(float(np.percentile(bt, 95)), 4))
    return (f"merc {len(x):5d} | EV/€ {pnl.sum() / coste.sum():+.4f} IC90 días {ic} {int((ev_d > 0).sum())}/{len(ev_d)} días+"
            f" | PnL {pnl.sum():+8.2f} $ (+reemb {reb:.2f}) | pares completos {comp:.0%}")


def main():
    global OUT
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default=",".join(DIAS))
    ap.add_argument("--out", default=str(OUT), help="directorio de cachés/informe/manifiesto (por defecto el real)")
    a = ap.parse_args()
    OUT = Path(a.out)
    OUT.mkdir(parents=True, exist_ok=True)
    pedidos = a.dias.split(",")
    man = {"job": "analisis_5m_cosechar_apertura", "script": Path(__file__).name,
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "args": vars(a), "dias_pedidos": pedidos, "dias_ok": [], "dias_ausentes": [], "dias_sin_filas": [],
           "dias_truncados": [], "dias_fallidos": {}, "inicio_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "fin_utc": None,
           "estado": "RUNNING"}
    escribir_atomico(OUT / "manifiesto.json", json.dumps(man, indent=1))
    filas = []
    for d in pedidos:
        try:
            r = simular_dia(d)
        except Exception as e:                       # un día roto no tumba el resto ni deja el manifiesto en RUNNING
            man["dias_fallidos"][d] = f"{type(e).__name__}: {e}"
            print(f"  {d}: FALLIDO {man['dias_fallidos'][d]}", file=sys.stderr, flush=True)
            escribir_atomico(OUT / "manifiesto.json", json.dumps(man, indent=1))
            continue
        if r is None:
            man["dias_ausentes"].append(d)
            print(f"  {d}: AUSENTE (sin m5_registro)", flush=True)
        else:
            filas += r
            (man["dias_ok"] if r else man["dias_sin_filas"]).append(d)
            if d in TRUNCADOS:
                man["dias_truncados"].append(d)
            print(f"  {d}: {len(r)} filas (mercados {len({x['mkt'] for x in r})})", flush=True)
        escribir_atomico(OUT / "manifiesto.json", json.dumps(man, indent=1))   # resumen parcial tras cada día
    completo = len(man["dias_ok"]) == len(pedidos) and not man["dias_truncados"] and not man["dias_fallidos"]
    cobertura = (f"COBERTURA: {len(man['dias_ok'])}/{len(pedidos)} días con filas | ausentes (sin registro): "
                 f"{man['dias_ausentes'] or 'ninguno'} | sin filas: {man['dias_sin_filas'] or 'ninguno'} | origen truncado: "
                 f"{man['dias_truncados'] or 'ninguno'} | fallidos: {list(man['dias_fallidos']) or 'ninguno'} | VEREDICTO {'COMPLETE' if completo else 'PARTIAL'}")
    lines = [cobertura, f"COSECHAR PARES AL ABRIR — BTC 5m, DESC {DESC[0]}..{DESC[-1]}, OOS {OOS[0]}..{OOS[-1]}"]
    for etiqueta, dias in (("DESC", DESC), ("OOS", OOS)):
        lines.append(f"\n== {etiqueta}")
        for pol in [p[0] for p in POLS]:
            lines.append(f"  {pol:18s} todos  {resumen(filas, pol, dias)}")
            lines.append(f"  {pol:18s} con15  {resumen(filas, pol, dias, solo15=True)}")
    elegibles = [p[0] for p in POLS if p[3] == "FINAL" and p[1] != "B_15"]

    def ev(pol, dias):
        x = [r for r in filas if r["pol"] == pol and r["dia"] in dias]
        c_ = sum(float(r["coste"]) for r in x)
        return sum(float(r["pnl"]) for r in x) / c_ if c_ > 0 else -9

    elegida = max(elegibles, key=lambda p: ev(p, DESC))
    lines.append(f"\nELEGIDA en DESC (solo A, cola FINAL): {elegida}")
    lines.append(f"OOS juicio elegida: {resumen(filas, elegida, OOS)}")
    par_ = elegida.split("_P")[1].split("_")[0]
    lines.append(f"5m barato vs normal, OOS, mismos mercados (con15): B_15_P{par_}_FINAL "
                 f"{resumen(filas, f'B_15_P{par_}_FINAL', OOS, True)}  ||  A0_P{par_}_FINAL "
                 f"{resumen(filas, f'A0_P{par_}_FINAL', OOS, True)}")
    txt = "\n".join(lines)
    print(txt)
    escribir_atomico(OUT / "informe.txt", txt + "\n")
    man["estado"] = "COMPLETE" if completo else "PARTIAL"
    man["fin_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    escribir_atomico(OUT / "manifiesto.json", json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
