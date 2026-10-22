#!/usr/bin/env python3
"""h23_sim_v3_monedas.py -- replay H23 v3 para MONEDAS (ETH/SOL/XRP/DOGE/BNB) y/o FUENTE alternativa (22-Oct-2026). NO modifica h23_sim_v3.py: lo importa y solo cambia de donde salen
las filas (extractos por moneda del registro, o el registro propio de pares de h23_shadow_v3r) y el nombre de las claves. La logica (segmentos, llenar, celdas) es la de h23_sim_v3.py: mismo
resultado para BTC desde el registro (test de equivalencia: test_h23_sim_v3_monedas.py).
Uso:  nice -n 19 ionice -c3 python3 -I h23_sim_v3_monedas.py registro COIN D        # extractos h23_v2/alts (ETH,SOL,XRP,DOGE,BNB) o v4_comprar_lo_bueno (BTC)
      nice -n 19 ionice -c3 python3 -I h23_sim_v3_monedas.py pares    COIN D        # registro propio de pares (h23_shadow_v3r --registro-dir)
(ulimit -v 3000000.) Env: H23V3_OUT (def. .../h23_v3/ para `registro`; .../h23_v3_pares/ para `pares`), H23_PARES_DIR. Idempotente: si existe la salida, no recalcula.
Lados: controles_D.csv del vigia v4 (04:35 del dia siguiente); si no existe y fuente=pares, derivados de las referencias TWAP60 oficiales (R.lado_de_refs), anotado en la cobertura.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ALTS = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/alts/"
BTC_IN = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/"
OUT_REG = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/"
OUT_PARES = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3_pares/"
PRICES = "/root/polymarket-research/data/prices/"
sys.path.insert(0, HERE)


def preparar(fuente, coin):
    if fuente == "registro":
        os.environ["H23V3_IN"] = BTC_IN if coin == "BTC" else ALTS
        os.environ.setdefault("H23V3_OUT", OUT_REG)
    else:
        os.environ.setdefault("H23V3_IN", BTC_IN)
        os.environ.setdefault("H23V3_OUT", OUT_PARES)


def lados_desde_refs(coin, D, pares, R):
    """{C: (lado, mkt5)} con TWAP60 oficial (source=chainlink) de PolyBolt: ref15 = twap60(C-900), ref5 = twap60(C-300). Solo para fuente=pares sin controles del vigia."""
    import gzip
    v = {}
    from datetime import datetime, timedelta
    d0 = datetime.strptime(D, "%Y-%m-%d").date()
    for dd in (d0 - timedelta(days=1), d0, d0 + timedelta(days=1)):
        for f in (PRICES + f"polybolt_{dd.isoformat()}.csv", PRICES + f"polybolt_{dd.isoformat()}.csv.gz"):
            if os.path.exists(f):
                op = gzip.open if f.endswith(".gz") else open
                with op(f, "rt") as fh:
                    for ln in fh:
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 7 and c[2] == "twap60" and c[6] == "chainlink" and c[1] == coin:
                            try:
                                e = int(c[4]) // 1000
                                if e % 300 == 0:
                                    v.setdefault(e, float(c[3]))
                            except ValueError:
                                pass
                break
    out = {}
    for C, p in pares.items():
        r15, r5 = v.get(C - 900), v.get(C - 300)
        if r15 and r5:
            s = R.lado_de_refs(r15, r5)
            if s is not None:
                out[C] = (s, p["mkt5"])
    return out


def correr(fuente, coin, D):
    preparar(fuente, coin)
    import h23_sim_v3 as S
    import h23_regla_v3 as R
    extra = {}
    if fuente == "registro":
        k0, g0 = S.kmap, S.grupos
        if coin != "BTC":
            S.kmap = lambda key, c: k0(f"{coin}_{key}", c)
            S.grupos = lambda key: g0(f"{coin}_{key}")
    else:
        import h23_pares_lector as P
        dirn = os.environ.get("H23_PARES_DIR", P.REGISTRO_DEFECTO)
        pares = P.cargar(coin, D, dirn)
        S.kmap = lambda key, c: P.kmap(pares)
        S.grupos = lambda key: P.grupos(pares, S.simlib)
        ctrl = S.DL + f"vigia_5m_barato/controles_{D}.csv"
        if not os.path.exists(ctrl):
            ls = lados_desde_refs(coin, D, pares, R)
            S.lados = lambda dd, c: ls
            extra["lados_fuente"] = "refs_twap60"
        else:
            extra["lados_fuente"] = "controles_vigia"
        extra["pares_en_registro"] = len(pares)
        extra["pares_con_caida"] = sum(1 for p in pares.values() if p["huecos"])
        extra["caidas_total"] = sum(len(p["huecos"]) for p in pares.values())
        extra["pares_con_caida_en_ventana"] = sum(1 for C, p in pares.items() if P.huecos_en_ventana(p, C))
        extra["dir_registro"] = dirn
    S.main(D, coin)
    fc = S.OUT + f"v3_cobertura_{coin}_{D}.json"
    if os.path.exists(fc):
        cob = json.load(open(fc))
        cob.update(fuente=fuente, **extra)
        if fuente == "registro" and coin != "BTC":
            cob["rows_fuente"] = ALTS + f"rows_{coin}_{D}.csv.gz"
        tmp = fc + ".tmp"
        json.dump(cob, open(tmp, "w"))
        os.replace(tmp, fc)


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("registro", "pares"):
        sys.exit(__doc__)
    correr(sys.argv[1], sys.argv[2], sys.argv[3])
