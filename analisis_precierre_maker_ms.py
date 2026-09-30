#!/usr/bin/env python3
"""analisis_precierre_maker_ms.py -- simulación "maker con cancelación en ms" en el PRECIERRE (ronda 1 #4).
Entrada: /root/polymarket-research-datalogs/precierre_libro_ms_YYYY-MM-DD.csv.gz (película del libro del YES a
100 ms + trades, últimos ~70 s de cada up/down 5m/15m de BTC/ETH/SOL/XRP; retención 5 días) y el desenlace
oficial (gamma, closed=true).

Regla simulada (sin fee: es maker). En T-`inicio` s, si el libro da un favorito claro (mid >= 0,55):
  - orden pasiva de COMPRA del favorito un tick por dentro del spread si cabe; si no, igualando el mejor precio;
  - RELLENO conservador: solo si después se imprime un trade AGRESOR contra mi lado a mi precio o mejor para él
    (igualando precio: solo si lo atraviesa, porque estaría al final de la cola);
  - CANCELACIÓN: si el mid del favorito cae `c` céntimos respecto al de la colocación se manda cancelar y tarda
    LAT_MS en hacerse efectiva (los rellenos dentro de esa latencia cuentan); sin relleno a T-2 s se retira.
El libro grabado es el del YES: comprar NO a q equivale a vender YES a 1-q (libro espejo), y el agresor es el
trade BUY del YES.

Qué mirar: % de rellenos, acierto de lo rellenado frente a lo NO rellenado (selección adversa) y EV por € del
relleno, por marco y por precio. Con menos de 3 días es EXPLORATORIO; cualquier celda buena se congela y se mide
en forward, no se opera. Solo lectura.  Uso: analisis_precierre_maker_ms.py
"""
import collections
import csv
import glob
import gzip
import json
import random
import sys

import requests

DATALOGS = "/root/polymarket-research-datalogs"
LAT_MS = 300
TICK = 0.01


def _desenlaces(ids) -> dict:
    out, ses, ids = {}, requests.Session(), sorted(ids)
    for k in range(0, len(ids), 40):
        try:
            r = ses.get("https://gamma-api.polymarket.com/markets", timeout=20,
                        params=[("id", i) for i in ids[k:k + 40]] + [("closed", "true"), ("limit", "40")])
            for m in r.json() or []:
                pr = m.get("outcomePrices")
                pr = json.loads(pr) if isinstance(pr, str) else pr
                if pr and float(pr[0]) >= 0.999:
                    out[str(m["id"])] = "YES"
                elif pr and float(pr[1]) >= 0.999:
                    out[str(m["id"])] = "NO"
        except Exception as e:
            print(f"lote {k // 40} de desenlaces falló: {type(e).__name__}", file=sys.stderr)
    return out


def _cargar():
    mk = {}
    for f in sorted(glob.glob(f"{DATALOGS}/precierre_libro_ms_*.csv.gz")):
        dia = f[-17:-7]
        with gzip.open(f, "rt", encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if r["token"] != "YES":
                    continue
                m = mk.setdefault(r["market_id"], {"activo": r["activo"], "marco": r["marco"], "dia": dia, "book": [], "tr": []})
                rel = int(float(r["rel_fin_ms"]))
                try:
                    if r["tipo"] == "book":
                        if r["best_bid"] and r["best_ask"]:
                            m["book"].append((rel, float(r["best_bid"]), float(r["best_ask"])))
                    elif r["precio"]:
                        m["tr"].append((rel, float(r["precio"]), r["side"]))
                except ValueError:
                    continue
    for m in mk.values():
        m["book"].sort()
        m["tr"].sort()
    return mk


def _simular(m, inicio_s: int, c_cent):
    """-> None (no se coloca) | dict(lado, precio, relleno, mid0)"""
    t0 = -inicio_s * 1000
    prev = [b for b in m["book"] if b[0] <= t0]
    if not prev or t0 - prev[-1][0] > 30000:         # sin foto reciente del libro en el instante de colocar
        return None
    _, bid, ask = prev[-1]
    mid = (bid + ask) / 2
    if 0.45 < mid < 0.55 or ask - bid <= 0 or ask - bid > 0.10:
        return None
    fav_yes = mid >= 0.55
    # precio de mi orden EN TÉRMINOS DEL YES: compro YES a `p` (favorito YES) o vendo YES a `p` (favorito NO)
    dentro = ask - bid >= 2 * TICK - 1e-9
    p = (bid + TICK if dentro else bid) if fav_yes else (ask - TICK if dentro else ask)
    mid_fav0 = mid if fav_yes else 1 - mid
    t_cancel = -2000
    if c_cent is not None:
        for rel, b, a in m["book"]:
            if rel <= t0:
                continue
            mf = (b + a) / 2 if fav_yes else 1 - (b + a) / 2
            if mf <= mid_fav0 - c_cent / 100 + 1e-9:
                t_cancel = min(t_cancel, rel + LAT_MS)
                break
    relleno = False
    for rel, precio, side in m["tr"]:
        if rel <= t0 or rel > t_cancel:
            continue
        if fav_yes and side == "SELL" and (precio < p - 1e-9 or (dentro and precio <= p + 1e-9)):
            relleno = True
            break
        if not fav_yes and side == "BUY" and (precio > p + 1e-9 or (dentro and precio >= p - 1e-9)):
            relleno = True
            break
    return {"fav": "YES" if fav_yes else "NO", "precio": p if fav_yes else 1 - p, "relleno": relleno, "mid0": mid_fav0}


def _ic(por_dia_mk: dict):
    ks, bs = list(por_dia_mk), []
    for _ in range(600):
        v = [por_dia_mk[k] for k in random.choices(ks, k=len(ks))]
        bs.append(sum(v) / len(v))
    bs.sort()
    return bs[30], bs[569]


def main() -> int:
    random.seed(17)
    mk = _cargar()
    gan = _desenlaces(mk.keys())
    dias = sorted({m["dia"] for m in mk.values()})
    print(f"{len(mk)} mercados con película, {sum(1 for k in mk if k in gan)} con desenlace, días: {dias} "
          f"({'EXPLORATORIO: <3 días' if len(dias) < 3 else 'ok'})")
    print("\nmarco  inicio cancel  banda_fav     colocadas  relleno%  acierto_relleno  acierto_NO_relleno  precio  EV/€_relleno  IC90 (por mercado)  EV/€ por colocada  días+")
    for marco in ("5min", "15min"):
        for inicio in (60, 30):
            for c in (None, 4, 2, 1):
                for lo, hi in ((0.55, 0.80), (0.80, 0.95), (0.95, 1.0)):
                    sims = []
                    for k, m in mk.items():
                        if m["marco"] != marco or k not in gan:
                            continue
                        s = _simular(m, inicio, c)
                        if s and lo <= s["mid0"] < hi:
                            s["ok"] = gan[k] == s["fav"]
                            s["k"], s["dia"] = k, m["dia"]
                            sims.append(s)
                    rell = [s for s in sims if s["relleno"]]
                    if len(sims) < 30 or len(rell) < 15:
                        continue
                    ev = {s["k"]: ((1 - s["precio"]) / s["precio"] if s["ok"] else -1.0) for s in rell}
                    no = [s for s in sims if not s["relleno"]]
                    lo_ic, hi_ic = _ic(ev)
                    pd = collections.defaultdict(list)
                    for s in rell:
                        pd[s["dia"]].append(ev[s["k"]])
                    print(f"{marco:5s}  T-{inicio:2d}  {('-' if c is None else str(c) + 'c'):>5s}  [{lo:.2f},{hi:.2f})  {len(sims):8d}  "
                          f"{len(rell) / len(sims):7.1%}  {sum(s['ok'] for s in rell) / len(rell):14.1%}  "
                          f"{(sum(s['ok'] for s in no) / len(no) if no else 0):17.1%}  {sum(s['precio'] for s in rell) / len(rell):6.3f}  "
                          f"{sum(ev.values()) / len(ev):+11.3f}  ({lo_ic:+.3f},{hi_ic:+.3f})  {sum(ev.values()) / len(sims):+15.4f}  "
                          f"{sum(1 for v in pd.values() if sum(v) > 0)}/{len(pd)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
