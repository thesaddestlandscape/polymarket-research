#!/usr/bin/env python3
"""analisis_5m_barato_maker_sim.py -- misión «5m barato» (12-Oct), experimento H6: MAKER ANTICIPATORIO de valor relativo.
SOLO LECTURA (archivo del registro ms en el volumen). Hipótesis NUEVA: los días que se simulan aquí son DESCUBRIMIENTO /
VALIDACIÓN; si sale algo, se congela y se mide forward (nunca se presenta este resultado como OOS).

Motivo (autopsia 12-Oct): las señales v4 que DESAPARECEN en <215 ms valían +1,67 €/€ (83 % acierto) y las que quedan
−0,37. Un tomador no llega antes (taker delay 150 ms + POST). Un MAKER ya colocado sí: si alguien pone un ask del 5m por
debajo de nuestro bid, cruza contra NOSOTROS (prioridad precio-tiempo) sin esperar a nadie.

Política (por cierre C de un 15m y moneda; 5m que cierra en C):
  lado s = Up si ref15 > ref5 (TWAP60 oficial en C-900 y C-300, |gap| >= 1 bps), si no Down (misma lógica que v4).
  Ventana [C-300+1,5 s, C-10 s] (hora de RECEPCIÓN). Objetivo = mayor tick p con bid15(s) - p - fee(p) >= M, post-only
  (p <= ask5(s) - 0,01). Libro 15m cruzado o sin bid -> sin orden. Cada cambio de bid15/ask5 recoloca la orden; el
  precio nuevo rige en el exchange a +L_REP ms (cancelar 60 + alta 68 medidos el 07-Oct -> 130).
  Tamaño objetivo 5 acciones; una posición por mercado (al llenarse 5, se acaba).
Relleno (CONSERVADOR): para un evento recibido en r se usa el precio vigente en r - 360 ms (p90 del retraso del feed):
  cuenta de MÁS los rellenos con bid rancio (adversos) y de MENOS los favorables.
  (a) fila q del 5m(s) con ask <= p: ese vendedor cruzaría contra nuestro bid -> min(ask_size, resto) a p.
  (b) operación tomadora SELL del 5m(s) a precio < p (atraviesa el nivel) -> llena; a precio == p solo si la cola de
      delante (tamaño del mejor bid al ponernos, si estábamos igualados; infinita si por debajo) ya se consumió.
  (c) operación tomadora BUY del 5m contrario a precio > 1-p (acuñación) -> llena; == con la misma cola.
PnL = acciones x (pago oficial - p); maker sin comisión; reembolso estimado aparte (20 % de 0,07·p·(1-p)).
BASE "pasivo": misma maquinaria con p = mejor bid del 5m(s) (unirse al bid), sin referencia al 15m.
Unidad = cierre (IC por cierre). Uso: --dias 2026-10-06,... [--margenes 0.05,0.08,0.10] [--lrep 130,300]
"""
import argparse
import bisect
from array import array
import collections
import glob
import gzip
import json
import math
import random
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import vigia_5m_barato_forward as V  # noqa: E402  (fee, twap_refs)

ARCH = Path("/mnt/HC_Volume_106538179/registro_5m_barato")
LAG_FEED_MS = 360
ACC_OBJ = 5.0
TICK = 0.01


def p_objetivo(bid15, M):
    p = math.floor((bid15 - M) / TICK) * TICK
    while p > 0 and bid15 - p - V.fee(p) < M - 1e-12:
        p -= TICK
    return round(p, 2) if p >= TICK else None


class _Serie:
    """Columnas array (la versión con tuplas reventaba la memoria, como el vigía v3)."""
    __slots__ = ("cols",)

    def __init__(self, n):
        self.cols = [array("d") for _ in range(n)]

    def add(self, *v):
        for c, x in zip(self.cols, v):
            c.append(x)

    def ordenar(self):
        orden = sorted(range(len(self.cols[0])), key=self.cols[0].__getitem__)
        self.cols = [array("d", (c[i] for i in orden)) for c in self.cols]


NAN = float("nan")


def cargar_dia(dia):
    d = date.fromisoformat(dia)
    t_lo = int(datetime(d.year, d.month, d.day, tzinfo=timezone.utc).timestamp())
    fich = sorted((f for f in glob.glob(str(ARCH / "maker_ms_*.csv.gz"))
                   if Path(f).name[9:19] in (dia, (d + timedelta(days=1)).isoformat())), key=lambda f: Path(f).stat().st_mtime)
    meta, idx = {}, collections.defaultdict(dict)
    q, tr = collections.defaultdict(lambda: _Serie(5)), collections.defaultdict(lambda: _Serie(4))
    for f in fich:
        try:
            for ln in gzip.open(f, "rt"):
                c = ln.rstrip("\n").split(",")
                if c[0] == "k" and len(c) > 7 and c[4] in ("5min", "15min"):
                    cie = int(datetime.fromisoformat(c[6]).timestamp())
                    meta[c[2]] = (c[3], c[4], c[5], cie, c[7])
                    idx[(c[3], cie)][(c[4], c[7])] = c[2]
                elif c[0] in ("q", "t"):
                    m = meta.get(c[2])
                    if not m or not (t_lo <= m[3] < t_lo + 86400) or m[3] % 900:
                        continue
                    try:
                        if c[0] == "q":
                            r = int(c[7]) if len(c) > 7 and c[7] else int(c[1])
                            if not ((m[3] - 305) * 1000 <= r <= m[3] * 1000):
                                continue
                            g = lambda x: NAN if x in ("", "None") else float(x)  # noqa: E731
                            b, a, bs, as_ = g(c[3]), g(c[4]), g(c[5]), g(c[6])
                            q[c[2]].add(r, b, a, 0.0 if bs != bs else bs, 0.0 if as_ != as_ else as_)
                        else:
                            r = int(c[6]) if len(c) > 6 and c[6] else int(c[1])
                            if not ((m[3] - 305) * 1000 <= r <= m[3] * 1000):
                                continue
                            tr[c[2]].add(r, float(c[3]), 1.0 if c[4] == "SELL" else 0.0, float(c[5]))
                    except (ValueError, IndexError):
                        continue
        except (EOFError, OSError):
            continue
    for v in list(q.values()) + list(tr.values()):
        v.ordenar()
    return t_lo, meta, idx, q, tr


def _ultimo(serie, t):
    """(r, bid, ask, bid_sz, ask_sz) con r <= t, None si no hay; NaN -> None."""
    if serie is None:
        return None
    i = bisect.bisect_right(serie.cols[0], t) - 1
    if i < 0:
        return None
    v = [c[i] for c in serie.cols]
    return tuple(None if (k in (1, 2) and x != x) else x for k, x in enumerate(v))


def simular(C, coin, s, t15s, t5s, t5c, q, tr, M, L_REP, modo, lag=LAG_FEED_MS):
    T0, T1 = (C - 300) * 1000 + 1500, (C - 10) * 1000
    q15, q5 = q.get(t15s), q.get(t5s)
    rr = lambda S: [x for x in (S.cols[0] if S else []) if T0 - 5000 <= x <= T1]  # noqa: E731
    # 1) cronología de PRECIOS de nuestra orden en el exchange: (t_efectivo, p, cola_delante)
    cambios = sorted(set(rr(q15)) | set(rr(q5)) | {T0})
    orden, ult = [], ("init",)
    for t in cambios:
        if t < T0:
            continue
        a, b = _ultimo(q15, t), _ultimo(q5, t)
        p, cola = None, math.inf
        if b and b[2] is not None:
            if modo == "pasivo":
                p = b[1]
            elif a and a[1] is not None and (a[2] is None or a[1] < a[2]):
                p = p_objetivo(a[1], M)
            if p is not None:
                p = min(p, round(b[2] - TICK, 2))
                if p < TICK:
                    p = None
            if p is not None:
                bb = b[1] if b[1] is not None else 0.0
                cola = 0.0 if p > bb + 1e-9 else (b[3] if abs(p - bb) < 1e-9 else math.inf)
        if (p,) != ult[:1]:
            orden.append((t + L_REP, p, cola))
            ult = (p,)
    if not orden:
        return None
    t_ef = [o[0] for o in orden]

    def vigente(t):
        i = bisect.bisect_right(t_ef, t) - 1
        return orden[i] if i >= 0 else (None, None, math.inf)

    # 2) eventos de relleno en orden de recepción
    def filas(S):
        return zip(*S.cols) if S else []
    evs = [(r, "q", ask, asz) for (r, _b, ask, _bs, asz) in filas(q5) if T0 <= r <= T1 and ask == ask]
    evs += [(r, "tS", px, sz) for (r, px, side, sz) in filas(tr.get(t5s)) if T0 <= r <= T1 and side == 1.0]
    evs += [(r, "tC", px, sz) for (r, px, side, sz) in filas(tr.get(t5c)) if T0 <= r <= T1 and side == 0.0]
    evs.sort()
    lleno, coste, vol_nivel, ultimo_p, via = 0.0, 0.0, 0.0, None, collections.Counter()
    for r, tipo, px, sz in evs:
        t_ord, p, cola = vigente(r - lag)
        if p is None:
            continue
        if p != ultimo_p:
            vol_nivel, ultimo_p = 0.0, p
        resto = ACC_OBJ - lleno
        if resto <= 1e-9:
            break
        n = 0.0
        if tipo == "q" and px <= p + 1e-9:
            n = min(resto, sz)
        elif tipo == "tS":
            if px < p - 1e-9:
                n = min(resto, sz)
            elif abs(px - p) < 1e-9:
                vol_nivel += sz
                n = min(resto, max(0.0, vol_nivel - cola))
        elif tipo == "tC":
            if px > 1 - p + 1e-9:
                n = min(resto, sz)
            elif abs(px - (1 - p)) < 1e-9:
                vol_nivel += sz
                n = min(resto, max(0.0, vol_nivel - cola))
        if n > 0:
            lleno += n
            coste += n * p
            via[tipo] += n
    if lleno <= 0:
        return {"lleno": 0.0}
    return {"lleno": round(lleno, 4), "precio": round(coste / lleno, 4), "via": dict(via)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", required=True)
    ap.add_argument("--margenes", default="0.05,0.08,0.10")
    ap.add_argument("--lrep", default="130,300")
    ap.add_argument("--lags", default=str(LAG_FEED_MS), help="retraso del feed supuesto (ms), p.ej. 0,100,360")
    a = ap.parse_args()
    from analisis_maker_cancelacion_binance import desenlaces
    dias = a.dias.split(",")
    tw = V.twap_refs(sorted({(date.fromisoformat(d) - timedelta(days=1)).isoformat() for d in dias} | set(dias)))
    lags = [int(x) for x in a.lags.split(",")]
    politicas = [("rv", float(M), int(L), g) for M in a.margenes.split(",") for L in a.lrep.split(",") for g in lags] + \
                [("pasivo", 0.0, 130, g) for g in lags]
    filas = []
    for dia in dias:
        t_lo, meta, idx, q, tr = cargar_dia(dia)
        n_c = 0
        for (coin, C), toks in idx.items():
            if not (t_lo <= C < t_lo + 86400) or C % 900:
                continue
            r15, r5 = tw.get(coin, {}).get(C - 900), tw.get(coin, {}).get(C - 300)
            if r15 is None or r5 is None or abs(r15 - r5) / r5 * 1e4 < 1.0:
                continue
            s = "Up" if r15 > r5 else "Down"
            ls, lc = ("YES", "NO") if s == "Up" else ("NO", "YES")
            t15s, t5s, t5c = toks.get(("15min", ls)), toks.get(("5min", ls)), toks.get(("5min", lc))
            if not (t15s and t5s and t5c):
                continue
            n_c += 1
            mid5 = meta[t5s][2]
            for modo, M, L, g in politicas:
                r = simular(C, coin, s, t15s, t5s, t5c, q, tr, M, L, modo, g)
                if r and r["lleno"] > 0:
                    filas.append({"dia": dia, "cierre": C, "moneda": coin, "lado": s, "market": mid5,
                                  "politica": (f"{modo}_M{M:.2f}_L{L}" if modo == "rv" else "pasivo_bid5") + f"_lag{g}", **r})
        print(f"{dia}: {n_c} pares (cierre, moneda) simulados", flush=True)
        del meta, idx, q, tr
    des = desenlaces({f["market"] for f in filas}) if filas else {}
    print(f"\ndesenlace oficial: {sum(1 for f in filas if f['market'] in des)}/{len(filas)} rellenos con desenlace")
    print(f"\n{'política':18} {'merc':>5} {'cierres':>7} {'acierto':>7} {'p medio':>7} {'PnL $':>8} {'EV $/$':>7} {'IC90 cierre':>17} "
          f"{'sin mejor':>9} {'sin BTC':>8} {'reemb $':>7} {'vías q/tS/tC':>14}")
    res = {}
    for pol in sorted({f["politica"] for f in filas}):
        F = [f for f in filas if f["politica"] == pol and f["market"] in des]
        if not F:
            continue
        for f in F:
            f["gana"] = (des[f["market"]] == "YES") == (f["lado"] == "Up")
            f["pnl"] = f["lleno"] * ((1.0 if f["gana"] else 0.0) - f["precio"])
            f["riesgo"] = f["lleno"] * f["precio"]
        porc = collections.defaultdict(list)
        for f in F:
            porc[f["cierre"]].append(f["pnl"] / f["riesgo"])
        g, rng, med = list(porc.values()), random.Random(3), []
        for _ in range(3000):
            sm = [x for _ in g for x in rng.choice(g)]
            med.append(sum(sm) / len(sm))
        med.sort()
        pnl, rie = sum(f["pnl"] for f in F), sum(f["riesgo"] for f in F)
        top = max(F, key=lambda f: f["pnl"])
        nb = [f for f in F if f["moneda"] != "BTC"]
        via = collections.Counter()
        for f in F:
            via.update(f["via"])
        d = {"mercados": len(F), "cierres": len(porc), "acierto": round(sum(f["gana"] for f in F) / len(F), 3),
             "precio_medio": round(sum(f["precio"] for f in F) / len(F), 3), "pnl": round(pnl, 2), "ev": round(pnl / rie, 3),
             "ic90_cierre": [round(med[150], 3), round(med[2849], 3)],
             "ev_sin_mejor": round((pnl - top["pnl"]) / (rie - top["riesgo"]), 3) if rie > top["riesgo"] else None,
             "ev_sin_btc": round(sum(f["pnl"] for f in nb) / sum(f["riesgo"] for f in nb), 3) if nb else None,
             "reembolso": round(sum(0.2 * 0.07 * f["precio"] * (1 - f["precio"]) * f["lleno"] for f in F), 2),
             "por_dia": {dd: round(sum(f["pnl"] for f in F if f["dia"] == dd), 2) for dd in dias}}
        res[pol] = d
        print(f"{pol:18} {d['mercados']:5d} {d['cierres']:7d} {d['acierto']:7.0%} {d['precio_medio']:7.2f} {d['pnl']:+8.2f} {d['ev']:+7.3f} "
              f"{str(d['ic90_cierre']):>17} {str(d['ev_sin_mejor']):>9} {str(d['ev_sin_btc']):>8} {d['reembolso']:7.2f} "
              f"{int(via['q'])}/{int(via['tS'])}/{int(via['tC']):>3}")
    out = REPO / "informes" / f"m5barato_maker_sim_{dias[0]}_{dias[-1]}.json"
    out.write_text(json.dumps({"dias": dias, "lag_feed_ms": LAG_FEED_MS, "acc_obj": ACC_OBJ, "resultados": res}, indent=1), encoding="utf-8")
    print(f"\nJSON: {out}")


if __name__ == "__main__":
    main()
