#!/usr/bin/env python3
"""analisis_arbitraje_anidado_dryrun.py -- valora el dry-run del arbitraje anidado de 2 patas (05-Oct, Javi: "dry-run
del arbitraje anidado de 2 patas"). Lee los CSV de arbitraje_anidado_dryrun_fase0.py (datalogs) y, por latencia simulada:
  unidad = oportunidad única (par, moneda, cierre, pata A) -> su PRIMERA detección (las repeticiones del mismo
  segundo/cierre no son apuestas independientes);
  ambas  -> PnL = pago_A + pago_B - ask_A - ask_B - fee_A - fee_B (garantía >= 1; 2 si el cierre cae entre referencias)
  solo_X -> PnL de la pata suelta con desenlace OFICIAL (legging sin cobertura posterior: cota pesimista)
  ninguna -> 0
fee(p) = 0,07·p·(1−p) por share. Desenlace oficial por id de gamma (closed=true, caché de analisis_maker_cancelacion_binance).
Se informa la cobertura de desenlaces, el reparto por día / moneda / par y el PnL sin el mejor día.
Uso: python3 analisis_arbitraje_anidado_dryrun.py [--desde YYYY-MM-DD]
"""
import argparse
import collections
import csv
import glob
import gzip
from datetime import datetime, timezone

from analisis_maker_cancelacion_binance import desenlaces

DATALOGS = "/root/polymarket-research-datalogs"
LATS = ["150", "200", "250", "300", "400", "600", "1000"]   # 200-300 desde el 05-Oct 17Z


def fee(p):
    return 0.07 * p * (1 - p)


def pago(pata, row, des):
    lado, cual = pata.split("_")                     # Up_largo / Down_corto ...
    res = des.get(row["market_" + cual])
    if res is None:
        return None
    return 1.0 if (res == "YES") == (lado == "Up") else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2000-01-01")
    a = ap.parse_args()
    filas = []
    for f in sorted(glob.glob(f"{DATALOGS}/arbitraje_anidado_dryrun_*.csv*")):
        op = gzip.open if f.endswith(".gz") else open
        with op(f, "rt") as fh:
            filas += list(csv.DictReader(fh))
    prim = {}
    for r in sorted(filas, key=lambda r: int(r["ts_ms"])):
        prim.setdefault((r["par"], r["activo"], r["fin"], r["pata_A"]), r)
    ops = [r for r in prim.values()
           if datetime.fromtimestamp(int(r["ts_ms"]) / 1000, timezone.utc).strftime("%Y-%m-%d") >= a.desde]
    des = desenlaces([r["market_largo"] for r in ops] + [r["market_corto"] for r in ops])
    print(f"filas {len(filas)}  oportunidades únicas {len(ops)}")
    for lat in LATS:
        tot, n_val, n_sin, cnt = 0.0, 0, 0, collections.Counter()
        por = collections.defaultdict(lambda: collections.defaultdict(float))
        rotas = 0
        for r in ops:
            fill = r.get(f"fill_{lat}")
            if not fill:                             # latencia que el observador aún no medía en esa fila
                continue
            cnt[fill] += 1
            sh, aA, aB = float(r["shares"]), float(r["ask_A"]), float(r["ask_B"])
            pA, pB = pago(r["pata_A"], r, des), pago(r["pata_B"], r, des)
            if fill == "ambas":
                if pA is None or pB is None:
                    n_sin += 1
                    continue
                if pA + pB < 1:
                    rotas += 1
                pnl = sh * (pA + pB - aA - aB - fee(aA) - fee(aB))
            elif fill == "solo_A":
                if pA is None:
                    n_sin += 1
                    continue
                pnl = sh * (pA - aA - fee(aA))
            elif fill == "solo_B":
                if pB is None:
                    n_sin += 1
                    continue
                pnl = sh * (pB - aB - fee(aB))
            else:
                pnl = 0.0
            n_val += 1
            tot += pnl
            dia = datetime.fromtimestamp(int(r["ts_ms"]) / 1000, timezone.utc).strftime("%Y-%m-%d")
            for dim, k in (("dia", dia), ("moneda", r["activo"]), ("par", r["par"]), ("relleno", fill)):
                por[dim][k] += pnl
        dias = por["dia"]
        sin_mejor = tot - max(dias.values()) if dias else 0.0
        print(f"\n== latencia {lat} ms: {dict(cnt)}  valoradas {n_val}  sin desenlace {n_sin}  garantía rota {rotas}")
        print(f"   PnL total {tot:+.2f} $  por oportunidad {tot / max(n_val, 1):+.3f} $  sin el mejor día {sin_mejor:+.2f} $")
        for dim in ("dia", "moneda", "par", "relleno"):
            print(f"   {dim}: " + "  ".join(f"{k} {v:+.2f}" for k, v in sorted(por[dim].items())))


if __name__ == "__main__":
    main()
