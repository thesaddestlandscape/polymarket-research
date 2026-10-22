#!/usr/bin/env python3
"""h23_cobertura_diaria.py -- MANIFIESTO DE COBERTURA DIARIA de los datos de H23 (22-Oct-2026). SOLO LECTURA de datos; escribe sus salidas atomicas en
/root/polymarket-research-datalogs/h23_cobertura/ (fuera de git; JSON ~20 KB + CSV por cierre ~15 KB por dia).
Por (dia, moneda) y por cada FUENTE: esperados (96 cierres: D 00:15..D+1 00:00), recibidos (con datos), procesados, con hueco, incompletos y FALTANTES (missing != 0):
  registro  maker_ms vía replay v3 (v3_cobertura_<COIN>_D.json) + libro de huecos (h23_huecos_ws): limpio / caida / reinicio por cierre
  shadow_v1 h23shadow (h23_shadow/), shadow_v3 (h23_shadow_v3/), shadow_v3r (h23_shadow_v3r/): pares con mercado_fin, completos (0 caidas), caidas, hueco_ms, frames, lag
  pares     registro propio de h23_shadow_v3r (h23_pares/): pares con alta P, con caida g en ventana, filas q/t, bytes
  replay    existencia y validez de v3_<COIN>_D.csv (cabecera, claves unicas) y de la variante `pares` (h23_v3_pares/)
y la UTILIDAD por cierre: utilizable = alguna fuente sin hueco en la ventana de cotizacion [C-305 s, C-10 s]. Rellenos de la celda PRIMARIA del PREREGISTRO (BTC/alt, cola base, alta 79,
cancel 60, tamano real, un relleno cierra, r150) por brazo, para ver cuantos caen en cierres con hueco. Exit 0 siempre que escriba; el estado `COMPLETE|PARTIAL` va en el JSON.
Uso: python3 -I h23_cobertura_diaria.py --dia 2026-10-21 [--monedas BTC,...] [--shadow-v3r DIR] [--pares DIR]
"""
import argparse
import csv
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import h23_huecos_ws as H  # noqa: E402
import h23_pares_lector as P  # noqa: E402
import h23_shadow_v3 as V3  # noqa: E402

DL = "/root/polymarket-research-datalogs/"
SALIDA = DL + "h23_cobertura/"
V3DIR = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/"
V3PARES = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3_pares/"
SHADOWS = {"shadow_v1": DL + "h23_shadow/h23_shadow_", "shadow_v3": DL + "h23_shadow_v3/h23_shadow_v3_", "shadow_v3r": DL + "h23_shadow_v3r/h23_shadow_v3_"}
MONEDAS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
COLS = ['coin', 'dia', 'cierre', 'lado', 'm5', 'brazo', 'sizing', 'modo', 'rep', 'cola', 'lat_post', 'lat_cancel', 'n_cotiz', 'need', 'lleno', 'coste', 'n_fill',
        't_rel', 'p_rel', 'gana', 'rebate']


def cierres(dia):
    d0 = int(datetime.strptime(dia, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())
    return [d0 + 900 * k for k in range(1, 97)]


def leer_shadow(prefijo, dia):
    """-> {(coin, cierre): dict(completo, caidas, hueco_ms, frames, lag, arranque_tarde)} de un directorio shadow. v1/v3 sin `coin` => BTC. Un par cruza el dia por su cierre."""
    out = {}
    d0 = datetime.strptime(dia, "%Y-%m-%d").date()
    for dd in (d0, d0 + timedelta(days=1)):
        f = f"{prefijo}{dd.isoformat()}.jsonl.gz"
        if not os.path.exists(f):
            continue
        gap, ws, fin = defaultdict(int), {}, {}
        for r in V3.leer_gz_tolerante(f):
            t = r.get("tipo")
            if t == "gap":
                gap[r["mkt"]] += 1
            elif t == "ws_pair":
                ws[r["mkt"]] = r
            elif t == "mercado_fin":
                fin[r["mkt"]] = r
        for mkt, r in fin.items():
            coin = r.get("coin", "BTC")
            C = r["cierre"]
            w = ws.get(mkt, {})
            out[(coin, C)] = dict(completo=bool(r["completo"]), caidas=gap.get(mkt, r.get("reconex", 0)), hueco_ms=w.get("hueco_ms"), frames=w.get("n_frames"),
                                  lag_max=w.get("lag_max_ms"), arranque_tarde=r.get("arranque_tarde"), abortado=r.get("abortado"))
    return out


def fills_primarios(f):
    """{(cierre, brazo): lleno>0} de la celda primaria."""
    out = {}
    if not os.path.exists(f):
        return out
    with open(f, newline="") as fh:
        for r in csv.DictReader(fh):
            if r["sizing"] == "real" and r["modo"] == "primer" and r["rep"] == "150" and r["cola"] == "base" and r["lat_post"] == "79" and r["lat_cancel"] == "60":
                out[(int(r["cierre"]), r["brazo"])] = float(r["lleno"]) > 0
    return out


def valida_csv(f):
    if not os.path.exists(f):
        return "falta"
    seen = set()
    with open(f, newline="") as fh:
        rd = csv.DictReader(fh)
        if rd.fieldnames != COLS:
            return "cabecera"
        for r in rd:
            k = (r["cierre"], r["brazo"], r["sizing"], r["modo"], r["rep"], r["cola"], r["lat_post"], r["lat_cancel"])
            if k in seen:
                return "duplicados"
            seen.add(k)
    return "ok"


def manifiesto(dia, monedas, dir_v3r=None, dir_pares=None):
    led = H.cargar()
    CS = cierres(dia)
    shadows = dict(SHADOWS)
    if dir_v3r:
        shadows["shadow_v3r"] = os.path.join(dir_v3r, "h23_shadow_v3_")
    sh = {k: leer_shadow(p, dia) for k, p in shadows.items()}
    res = dict(dia=dia, generado=datetime.now(timezone.utc).strftime("%FT%TZ"), esperados_por_moneda=len(CS), monedas={})
    filas = []
    for coin in monedas:
        cl = H.clasificar(coin, dia, led) if led else {}
        pares = P.cargar(coin, dia, dir_pares or P.REGISTRO_DEFECTO) if os.path.isdir(dir_pares or P.REGISTRO_DEFECTO) else {}
        cobf = V3DIR + f"v3_cobertura_{coin}_{dia}.json"
        cob = json.load(open(cobf)) if os.path.exists(cobf) else None
        csvf = V3DIR + f"v3_{coin}_{dia}.csv"
        fl = fills_primarios(csvf)
        fp = fills_primarios(V3PARES + f"v3_{coin}_{dia}.csv")
        cobp = V3PARES + f"v3_cobertura_{coin}_{dia}.json"
        m = dict(registro=dict(replay=valida_csv(csvf), cierres_con_libro=cob["con_libro"] if cob else None, con_lado=cob["con_lado"] if cob else None,
                               errores=cob["errores"] if cob else None, sin_desenlace=cob["sin_desenlace"] if cob else None,
                               limpios=sum(v == "limpio" for v in cl.values()) if cl else None, con_caida=sum("caida" in v for v in cl.values()) if cl else None,
                               con_reinicio=sum("reinicio" in v for v in cl.values()) if cl else None),
                 pares=dict(pares_alta=len(pares), con_caida_en_ventana=sum(1 for C, p in pares.items() if P.huecos_en_ventana(p, C)),
                            filas_q=sum(len(p["q"]) for p in pares.values()), filas_t=sum(len(p["t"]) for p in pares.values()),
                            replay=valida_csv(V3PARES + f"v3_{coin}_{dia}.csv") if os.path.exists(cobp) else "no_calculado"))
        for k in sh:
            d = {C: v for (c, C), v in sh[k].items() if c == coin and C in set(CS)}
            m[k] = dict(pares_recibidos=len(d), completos=sum(v["completo"] for v in d.values()), incompletos=sum(not v["completo"] for v in d.values()),
                        faltantes=len(CS) - len(d), caidas=sum(v["caidas"] or 0 for v in d.values()), arranque_tarde=sum(bool(v["arranque_tarde"]) for v in d.values()))
        util = 0
        for C in CS:
            reg = cl.get(C, "sin_ledger")
            p = pares.get(C)
            pe = ("sin_par" if p is None else "caida" if P.huecos_en_ventana(p, C) else "limpio")
            fila = dict(coin=coin, dia=dia, cierre=C, registro=reg, pares=pe,
                        **{k: ("falta" if (coin, C) not in sh[k] else "completo" if sh[k][(coin, C)]["completo"] else "incompleto") for k in sh})
            u = reg == "limpio" or pe == "limpio" or fila["shadow_v1"] == "completo" or fila["shadow_v3"] == "completo" or fila["shadow_v3r"] == "completo"
            fila["utilizable"] = int(u)
            util += int(u)
            for b in "AB":
                fila[f"fill_{b}_replay"] = (int(fl[(C, b)]) if (C, b) in fl else "")
                fila[f"fill_{b}_pares"] = (int(fp[(C, b)]) if (C, b) in fp else "")
            filas.append(fila)
        m["utilizables"] = util
        m["fills_primarios_replay"] = {b: sum(v for (C, bb), v in fl.items() if bb == b) for b in "AB"}
        m["fills_en_cierres_con_hueco_registro"] = {b: sum(v for (C, bb), v in fl.items() if bb == b and cl.get(C, "limpio") != "limpio") for b in "AB"}
        res["monedas"][coin] = m
    res["estado"] = "COMPLETE" if all(m["registro"]["replay"] == "ok" or m["pares"]["replay"] == "ok" for m in res["monedas"].values()) else "PARTIAL"
    return res, filas


def escribir(dia, res, filas, salida=SALIDA):
    os.makedirs(salida, exist_ok=True)
    f = salida + f"cobertura_{dia}.json"
    with open(f + ".tmp", "w") as fh:
        json.dump(res, fh, indent=1)
    os.replace(f + ".tmp", f)
    g = salida + f"cobertura_cierres_{dia}.csv"
    with open(g + ".tmp", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    os.replace(g + ".tmp", g)
    return f, g


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dia", required=True)
    ap.add_argument("--monedas", default=",".join(MONEDAS))
    ap.add_argument("--shadow-v3r", default=None)
    ap.add_argument("--pares", default=None)
    a = ap.parse_args()
    res, filas = manifiesto(a.dia, a.monedas.split(","), a.shadow_v3r, a.pares)
    f, g = escribir(a.dia, res, filas)
    print(f, g, res["estado"])
    for c, m in res["monedas"].items():
        print(c, "utilizables", m["utilizables"], "/", res["esperados_por_moneda"], "| registro limpios", m["registro"]["limpios"], "| shadow_v1", {k: m["shadow_v1"][k] for k in ("completos", "incompletos", "faltantes")},
              "| fills replay", m["fills_primarios_replay"], "en hueco", m["fills_en_cierres_con_hueco_registro"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
