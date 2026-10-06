#!/usr/bin/env python3
"""analisis_arbitraje_anidado_ms_scanner.py -- reconstruye TODOS los episodios de arbitraje anidado 5m>15m a partir
del registro ms (06-Oct, Javi: "auditar B1 hasta el último milisegundo"). Independiente del observador
arbitraje_anidado_dryrun_fase0 (que sondea cada 50 ms y valora la llegada con un histórico muestreado a 100 ms).

Garantía (misma que el observador): el 5m que cierra en C y el 15m que cierra en C resuelven con el MISMO TWAP60 de
cierre; solo cambia la referencia de apertura. ref_largo = twap60 oficial en C-900, ref_corto = twap60 en C-300
(canal twap60 de polybolt_*.csv = media RTDS [e-62, e-3], la que resuelve). Si ref_largo < ref_corto:
Up_largo (YES 15m) + Down_corto (NO 5m) paga >= 1; si ref_largo > ref_corto: Down_largo + Up_corto. |gap| >= 1 bps.

Episodio: desde el primer cambio de top (hora de RECEPCIÓN) con neto = 1 - askA - askB - fee(askA) - fee(askB) >=
NETO_MIN hasta el primer cambio con neto < NETO_MIN. Para cada episodio:
  t0 recepción y exchange; vida (ms, por hora del exchange y de recepción); neto en t0 y máximo; shares = min(tamaños top,
  200) en t0 (>=5); pata que cambió en t0 (A = la que acaba de cambiar) y edad de la otra; Binance (mid bookTicker) en
  los 1.000 ms previos; estado de cada pata a t0+L (L en LATS): "llena" si ask(t0+L) < precio o == precio con tamaño >=
  shares (semántica FOK en la llegada, como el observador) y "viva_continua" si nunca dejó de servir en [t0, t0+L];
  causa de la primera muerte de cada pata: consumida (operación a ese precio) o cancelada (sin operación).
Salida: CSV de episodios (--out) + resumen. Uso: --desde 2026-10-05T16:06 [--out fichero]
"""
import argparse
import bisect
import collections
import csv
import glob
import gzip
import sys
from datetime import datetime, timezone
from pathlib import Path

DL = "/root/polymarket-research-datalogs"
PRICES = Path(__file__).resolve().parent / "data" / "prices"
NETO_MIN = 0.0005
GAP_MIN_BPS = 1.0
MAX_SH, MIN_SH = 200.0, 5.0
LATS = [25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 1000]
SEGUIMIENTO_MS = 2000
REF_CONOCIBLE_MS = 1500
SIM = {"BTC": "BTCUSDT", "ETH": "ETHUSDT", "SOL": "SOLUSDT", "XRP": "XRPUSDT", "DOGE": "DOGEUSDT", "BNB": "BNBUSDT"}


def fee(p):
    return 0.07 * p * (1 - p)


def cargar_twap60(dias):
    tw = collections.defaultdict(dict)
    for d in dias:
        f = PRICES / f"polybolt_{d}.csv"
        if not f.exists():
            continue
        with open(f, encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if r["canal"] == "twap60" and r["source"] == "chainlink":
                    try:
                        tw[r["asset"]][int(r["event_ts_ms"]) // 1000] = float(r["value"])
                    except (ValueError, KeyError):
                        pass
    return tw


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-05T16:06")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    t_desde = int(datetime.fromisoformat(a.desde).replace(tzinfo=timezone.utc).timestamp() * 1000)
    fich = sorted(glob.glob(f"{DL}/maker_ms_*.csv.gz"), key=lambda f: Path(f).stat().st_mtime)
    dias = sorted({Path(f).name[9:19] for f in fich} | {datetime.fromtimestamp(t_desde / 1000, timezone.utc).date().isoformat()})
    tw = cargar_twap60(dias)
    meta = {}                       # token -> (moneda, marco, mid, cierre_s, lado)
    idx = collections.defaultdict(dict)   # (moneda, cierre_s) -> {(marco, lado): token}
    pares = {}                      # (moneda, cierre_s) -> dict con tokens y lados de la garantía
    top = {}                        # token -> (ask, asz, t_exch, t_recv)
    abiertos = {}                   # clave par -> episodio abierto
    seguimiento = []                # episodios cerrados o abiertos aún en seguimiento de 2 s
    terminados = []
    bin_hist = collections.defaultdict(lambda: collections.deque(maxlen=4000))
    stats = collections.Counter()

    def par_de(tok):
        m = meta.get(tok)
        if not m:
            return None
        return pares.get((m[0], m[3]))

    def preparar_par(moneda, cierre):
        k = (moneda, cierre)
        if k in pares:
            return
        toks = idx.get(k, {})
        if not all(x in toks for x in (("5min", "YES"), ("5min", "NO"), ("15min", "YES"), ("15min", "NO"))):
            return
        rl, rc = tw.get(moneda, {}).get(cierre - 900), tw.get(moneda, {}).get(cierre - 300)
        if rl is None or rc is None:
            stats["par_sin_ref"] += 1
            pares[k] = None
            return
        gap = (rc / rl - 1) * 1e4
        if abs(gap) < GAP_MIN_BPS:
            stats["par_gap<min"] += 1
            pares[k] = None
            return
        if rl < rc:
            A, B = toks[("15min", "YES")], toks[("5min", "NO")]
            pa, pb = "Up_largo", "Down_corto"
        else:
            A, B = toks[("15min", "NO")], toks[("5min", "YES")]
            pa, pb = "Down_largo", "Up_corto"
        pares[k] = {"k": k, "A": A, "B": B, "pata_A": pa, "pata_B": pb, "gap": gap,
                    "mid_l": meta[A][2], "mid_c": meta[B][2]}
        stats["pares_validos"] += 1

    for f in fich:
        try:
            fh = gzip.open(f, "rt")
            for ln in fh:
                c = ln.rstrip("\n").split(",")
                tp = c[0]
                if tp == "k":
                    if c[4] in ("5min", "15min"):
                        cierre = int(datetime.fromisoformat(c[6]).timestamp())
                        meta[c[2]] = (c[3], c[4], c[5], cierre, c[7])
                        idx[(c[3], cierre)][(c[4], c[7])] = c[2]
                        preparar_par(c[3], cierre)
                    continue
                if tp == "x":
                    if len(c) > 6 and c[6]:
                        bin_hist[c[2]].append((int(c[6]), float(c[3])))
                    continue
                if tp == "t":
                    tok = c[2]
                    if tok in top:
                        tr = int(c[6]) if len(c) > 6 and c[6] else int(c[1])
                        for e in seguimiento:
                            if tok in (e["A"], e["B"]) and tr <= e["t0r"] + SEGUIMIENTO_MS:
                                e["trades"].append((tok, tr, float(c[3])))
                    continue
                if tp != "q":
                    continue
                tok = c[2]
                m = meta.get(tok)
                if not m:
                    continue
                p = par_de(tok)
                if not p:
                    continue
                trv = int(c[7]) if len(c) > 7 and c[7] else int(c[1])
                tex = int(c[1])
                ask = None if c[4] in ("", "None") else float(c[4])
                asz = 0.0 if c[6] in ("", "None") else float(c[6])
                top[tok] = (ask, asz, tex, trv)
                for e in seguimiento:
                    if tok in (e["A"], e["B"]) and trv <= e["t0r"] + SEGUIMIENTO_MS:
                        e["upd"].append((tok, trv, ask, asz))
                if trv < t_desde:
                    continue
                k = p["k"]
                ta, tb = top.get(p["A"]), top.get(p["B"])
                neto = None
                if ta and tb and ta[0] and tb[0]:
                    neto = 1 - ta[0] - tb[0] - fee(ta[0]) - fee(tb[0])
                ep = abiertos.get(k)
                if ep is not None and trv / 1000 >= k[1]:      # el mercado ya cerró: fin del episodio
                    ep["fin_r"], ep["fin_x"] = trv, tex
                    del abiertos[k]
                    continue
                if trv / 1000 >= k[1]:
                    continue
                # SIN LOOK-AHEAD (06-Oct): ref_corto = twap60 del segundo de inicio del 5m (media [ini-62, ini-3]),
                # publicado ~1,4 s después de ini-3 por RTDS. Antes de ini+1,5 s el par garantizado NO es conocible
                # (el 5m ya cotiza antes de su ventana: 2.116 episodios falsos con la ref futura en la 1ª versión).
                if trv < (k[1] - 300) * 1000 + REF_CONOCIBLE_MS:
                    if ep is not None:
                        del abiertos[k]
                    continue
                if neto is not None and neto >= NETO_MIN:
                    if ep is None:
                        sh = min(ta[1], tb[1], MAX_SH)
                        cambia = "A" if tok == p["A"] else "B"
                        otra = tb if cambia == "A" else ta
                        bh = bin_hist.get(SIM[k[0]], ())
                        def bret(ms):
                            if not bh:
                                return None
                            ts_ = [x[0] for x in bh]
                            i1 = bisect.bisect_right(ts_, trv) - 1
                            i0 = bisect.bisect_right(ts_, trv - ms) - 1
                            if i1 < 0 or i0 < 0:
                                return None
                            return (bh[i1][1] / bh[i0][1] - 1) * 1e4
                        ep = {"A": p["A"], "B": p["B"], "k": k, "pata_A": p["pata_A"], "pata_B": p["pata_B"],
                              "gap": p["gap"], "mid_l": p["mid_l"], "mid_c": p["mid_c"],
                              "t0r": trv, "t0x": tex, "askA": ta[0], "askB": tb[0], "szA": ta[1], "szB": tb[1],
                              "shares": sh, "neto0": neto, "neto_max": neto, "cambia": cambia,
                              "edad_otra_ms": trv - otra[3], "resto_s": k[1] - trv / 1000,
                              "bin_100": bret(100), "bin_250": bret(250), "bin_500": bret(500), "bin_1000": bret(1000),
                              "fin_r": None, "fin_x": None, "upd": [], "trades": []}
                        abiertos[k] = ep
                        seguimiento.append(ep)
                    else:
                        ep["neto_max"] = max(ep["neto_max"], neto)
                elif ep is not None:
                    ep["fin_r"], ep["fin_x"] = trv, tex
                    del abiertos[k]
                # cerrar seguimientos vencidos
                if seguimiento and (len(seguimiento) > 50 or stats["q"] % 2000 == 0):
                    vivos = []
                    for e in seguimiento:
                        (terminados if trv > e["t0r"] + SEGUIMIENTO_MS and e["fin_r"] is not None else vivos).append(e)
                    seguimiento = vivos
                stats["q"] += 1
            fh.close()
        except (EOFError, OSError) as ex:
            print(f"  aviso: {Path(f).name} truncado ({type(ex).__name__})", file=sys.stderr)
    terminados += [e for e in seguimiento if e["fin_r"] is not None]
    filas = []
    for e in terminados:
        if e["shares"] < MIN_SH:
            stats["ep_shares<5"] += 1
            continue
        fila = {k_: e[k_] for k_ in ("t0r", "t0x", "askA", "askB", "szA", "szB", "shares", "neto0", "neto_max", "cambia",
                                       "edad_otra_ms", "resto_s", "gap", "bin_100", "bin_250", "bin_500", "bin_1000",
                                       "pata_A", "pata_B", "mid_l", "mid_c")}
        fila["moneda"], fila["cierre"] = e["k"]
        fila["vida_recv_ms"] = e["fin_r"] - e["t0r"]
        fila["vida_exch_ms"] = e["fin_x"] - e["t0x"]
        fila["garantizado_usd"] = e["shares"] * e["neto0"]
        for pata, tok, precio in (("A", e["A"], e["askA"]), ("B", e["B"], e["askB"])):
            ups = sorted((u for u in e["upd"] if u[0] == tok), key=lambda u: u[1])
            muerte, causa = None, "sobrevive_2s"
            for u in ups:
                if u[1] <= e["t0r"]:
                    continue
                if u[2] is None or u[2] > precio + 1e-9 or (abs(u[2] - precio) < 1e-9 and u[3] < e["shares"]):
                    muerte = u[1] - e["t0r"]
                    tr = [x for x in e["trades"] if x[0] == tok and e["t0r"] - 50 <= x[1] <= u[1] + 50 and x[2] >= precio - 1e-9]
                    causa = "consumida" if tr else "cancelada"
                    break
            fila[f"muerte_{pata}_ms"], fila[f"causa_{pata}"] = muerte, causa
            for L in LATS:
                est = None
                for u in ups:
                    if u[1] <= e["t0r"] + L:
                        est = u
                    else:
                        break
                if est is None or est[1] <= e["t0r"]:
                    ok = True       # sin cambios entre t0 y t0+L: sigue el top de t0
                else:
                    ok = est[2] is not None and (est[2] < precio - 1e-9 or (abs(est[2] - precio) < 1e-9 and est[3] >= e["shares"]))
                fila[f"llena_{pata}_{L}"] = int(ok)
                fila[f"viva_{pata}_{L}"] = int(muerte is None or muerte > L)
        filas.append(fila)
    print(f"stats: {dict(stats)} | episodios con shares>=5: {len(filas)}")
    if a.out and filas:
        with open(a.out, "w", newline="", encoding="utf-8") as fo:
            w = csv.DictWriter(fo, fieldnames=list(filas[0]))
            w.writeheader()
            w.writerows(filas)
        print(f"-> {a.out}")


if __name__ == "__main__":
    main()
