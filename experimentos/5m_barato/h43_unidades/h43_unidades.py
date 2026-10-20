#!/usr/bin/env python3
"""h43_unidades.py -- definicion UNICA de la unidad de H43 R5K (mision 5m barato, A1 de Javi 19-Oct).

Solo lectura: no escribe en produccion, no usa red (desenlaces desde cache), no envia ordenes. stdlib.

DEFINICION (la de h43_auditoria_datos/informe.md, causas C1-C4):
  * Universo: filas «relleno de maker en banda» (0,10; 0,30] de BTC 5m (band_D.csv.gz de pass1.py), unidad = (mercado, lado s).
  * cum(s): acciones acumuladas de TODAS las filas de la banda (cualquier T) hasta cruzar OFFSET=5000 (el relleno que cruza
    aporta solo la parte por encima de 5000).
  * K COSECHABLE: tras cruzar, las K=50 PRIMERAS acciones de fills con T en (60, 270] (los fills fuera de esa ventana NO
    consumen cupo: es lo que difiere de la ventana POSICIONAL del vigia congelado, C1).
  * COMPLETA = reunio las 50 acciones. Las incompletas se reportan aparte y NO cuentan en las cifras (C3).
  * DIA = dia UTC de CIERRE del mercado (fin = round((ts+T)/300)*300), no el del fichero (C2).
  * EV = Σpnl / Σcoste (ponderado por USDC) + IC90 por CIERRE y por DIA (bootstrap de clusters), sin 2 mejores dias, sin top-20.
  * A4 de Javi: el dia NUNCA es gate ni veredicto; solo descripcion.
Desenlace oficial desde cache (des[mkt] = 'YES'/'NO'); mercado sin desenlace = EXCLUIDO y CONTADO (missing != 0).

Variantes de frontera de fichero (documentadas, no mezcladas):
  concat=False (por defecto, compatible con a7 y con el vigia): cada fichero band_D se procesa solo. Un mercado que cierra
        justo tras las 00:00 UTC tiene fills en dos ficheros y su cum se reinicia (puede partirlo en dos unidades).
  concat=True: traslada al fichero siguiente las filas de mercados que cierran tras la medianoche (cum continuo por mercado-lado).
Uso: python3 -I h43_unidades.py --dias 2026-10-06 2026-10-07 ... [--concat] [--out cifras.json]
"""
import argparse
import csv
import datetime
import gzip
import json
import os
import random
import sys
from collections import defaultdict

OFFSET, K, T_MIN, T_MAX = 5000.0, 50.0, 60.0, 270.0   # congelados en REGISTRO_HIPOTESIS (H43 R5K)
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
DES_CACHES = ("/root/polymarket-research/experimentos/5m_barato/h43_auditoria_datos/des_cache_descubrimiento.json",
              "/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")
IN_SAMPLE = ("2026-10-06", "2026-10-16")
FORWARD = ("2026-10-17", "2026-10-31")


def ruta_banda(dia):
    for f in (f"{DISC}/band_{dia}.csv.gz", f"{VIGC}/{dia}/out/band_{dia}.csv.gz"):
        if os.path.exists(f):
            return f
    return None


def leer_banda(path, act="BTC"):
    """Filas (ts, li, mkt, lado, acc, coste, T, pc, maker) de la banda; lado = lado ADQUIRIDO por el maker."""
    rows = []
    with gzip.open(path, "rt") as fh:
        rd = csv.reader(fh)
        h = next(rd)
        ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            if c[ix["act"]] != act:
                continue
            rows.append((float(c[ix["ts"]]), int(float(c[ix["li"]])), c[ix["mkt"]], c[ix["lado_c"]], float(c[ix["acc"]]),
                         float(c[ix["coste"]]), float(c[ix["T"]]), float(c[ix["pc"]]), c[ix["maker"]]))
    return rows


def cargar_desenlaces(caches=DES_CACHES):
    des = {}
    for f in caches:
        if os.path.exists(f):
            with open(f) as fh:
                des.update(json.load(fh))
    return des


def dia_cierre(u):
    return datetime.datetime.fromtimestamp(u["fin"], datetime.timezone.utc).strftime("%Y-%m-%d")


def unidades_cosechables(rows, des):
    """-> (unidades {(mkt,lado): {...}}, sin_desenlace {(mkt,lado)}). Cada unidad: fin, c (USDC), p (pnl USDC), acc, completa."""
    seq = defaultdict(list)
    for r in sorted(rows, key=lambda r: (r[2], r[3], r[0], r[1])):
        seq[(r[2], r[3])].append(r)
    U, sin_des = {}, set()
    for k, lst in seq.items():
        mkt, lado = k
        g = des.get(mkt)
        if g is None:
            g = des.get(str(mkt))
        cum, crossed, need, take = 0.0, False, K, []
        for ts, li, _, _, acc, coste, T, pc, _ in lst:
            if acc <= 0:
                continue
            if not crossed:
                new = cum + acc
                if new >= OFFSET:
                    crossed = True
                    cand = min(new - OFFSET, acc)
                else:
                    cum = new
                    continue
            else:
                cand = acc
            if not (T_MIN < T <= T_MAX):
                continue
            th = min(cand, need)
            if th <= 0:
                continue
            take.append((pc, th))
            need -= th
            if need <= 1e-9:
                break
        if not take:
            continue
        if g is None:
            sin_des.add(k)
            continue
        c = sum(t * p for p, t in take)
        pnl = sum(t * ((1.0 if g == lado else 0.0) - p) for p, t in take)
        U[k] = {"fin": round((lst[0][0] + lst[0][6]) / 300) * 300, "c": c, "p": pnl, "acc": K - need, "completa": need <= 1e-9}
    return U, sin_des


def unidades_posicionales(rows, des):
    """Definicion POSICIONAL del vigia congelado (solo para la tabla de discrepancias): ventana [5000,5050) de posicion."""
    cum, U = defaultdict(float), {}
    for ts, li, mkt, lado, acc, coste, T, pc, mk in sorted(rows, key=lambda r: (r[2], r[3], r[0], r[1])):
        k = (mkt, lado)
        c0 = cum[k]
        cum[k] = c0 + acc
        if acc <= 0 or not (T_MIN < T <= T_MAX):
            continue
        lo, hi = max(c0 - OFFSET, 0.0), max(c0 + acc - OFFSET, 0.0)
        tk = max(min(K, hi) - min(K, lo), 0.0)
        g = des.get(mkt, des.get(str(mkt)))
        if tk <= 0 or g is None:
            continue
        f = tk / acc
        u = U.setdefault(k, {"fin": round((ts + T) / 300) * 300, "c": 0.0, "p": 0.0, "acc": 0.0})
        u["c"] += coste * f
        u["p"] += (acc * (g == lado) - coste) * f
        u["acc"] += tk
    return U


def _fin_fila(r):
    return round((r[0] + r[6]) / 300) * 300


def _medianoche_siguiente(dia):
    d = datetime.datetime.strptime(dia, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc) + datetime.timedelta(days=1)
    return d.timestamp()


def construir(dias, des=None, concat=False, posicional=False):
    """-> (lista de unidades con 'fichero', sin_desenlace_total, cobertura). Las incompletas se devuelven marcadas.
    concat=True: las filas de mercados que cierran DESPUES de la medianoche del fichero (fin > 00:00 del dia siguiente: los
    5m que cierran a las 00:05 tienen fills en dos ficheros) se trasladan al fichero siguiente para que su cum sea continuo."""
    des = cargar_desenlaces() if des is None else des
    out, sd_tot, cob = [], 0, {}
    f = unidades_posicionales if posicional else unidades_cosechables
    carry, carry_mk = [], 0
    dias_ok = [d for d in dias if ruta_banda(d)]
    for i, d in enumerate(dias_ok):
        rows = carry + leer_banda(ruta_banda(d))
        carry = []
        if concat and i + 1 < len(dias_ok) and _dia_siguiente(d) == dias_ok[i + 1]:
            lim = _medianoche_siguiente(d)
            carry = [r for r in rows if _fin_fila(r) > lim]
            rows = [r for r in rows if _fin_fila(r) <= lim]
            carry_mk += len({r[2] for r in carry})
        if posicional:
            U, sd = f(rows, des), set()
        else:
            U, sd = f(rows, des)
        for k, u in U.items():
            out.append(dict(u, mkt=k[0], lado=k[1], fichero=d, completa=u.get("completa", True)))
        sd_tot += len(sd)
        cob[d] = {"filas": len(rows), "unidades": len(U), "sin_desenlace": len(sd)}
    faltan = [d for d in dias if not ruta_banda(d)]
    return out, sd_tot, dict(cob, _dias_sin_banda=faltan, _mercados_trasladados_de_fichero=carry_mk, _carry_final_sin_procesar=len(carry))


def _dia_siguiente(d):
    return (datetime.datetime.strptime(d, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")


def _ic90(grupos, B=4000, seed=11):
    g = list(grupos.values())
    if len(g) < 3:
        return None
    r = random.Random(seed)
    bs = []
    for _ in range(B):
        m = [r.choice(g) for _ in g]
        c = sum(x[0] for x in m)
        bs.append(sum(x[1] for x in m) / c if c else 0.0)
    bs.sort()
    return [round(bs[int(B * .05)], 3), round(bs[int(B * .95) - 1], 3)]


def cifras(us, clave_dia=dia_cierre):
    """Cifras de una lista de unidades (se asume ya filtrada a COMPLETAS y al periodo)."""
    us = list(us)
    if not us:
        return None
    c, p = sum(u["c"] for u in us), sum(u["p"] for u in us)
    dia, cie = defaultdict(lambda: [0.0, 0.0]), defaultdict(lambda: [0.0, 0.0])
    for u in us:
        d = clave_dia(u)
        dia[d][0] += u["c"]
        dia[d][1] += u["p"]
        cie[u["fin"]][0] += u["c"]
        cie[u["fin"]][1] += u["p"]
    mej = sorted(dia, key=lambda d: dia[d][1], reverse=True)[:2]
    rest = [v for d, v in dia.items() if d not in mej]
    top = sorted(us, key=lambda u: u["p"], reverse=True)[20:]
    tc = sum(u["c"] for u in top)
    cr = sum(v[0] for v in rest)
    return {"n": len(us), "dias": len(dia), "cierres": len(cie), "coste_usdc": round(c, 2), "pnl_usdc": round(p, 2),
            "EV_ponderado": round(p / c, 4), "EV_media_unidad": round(sum(u["p"] / u["c"] for u in us) / len(us), 4),
            "IC90_cierre": _ic90(cie), "IC90_dias": _ic90(dia),
            "EV_sin_2_mejores_dias": round(sum(v[1] for v in rest) / cr, 4) if rest and cr else None,
            "EV_sin_top20_unidades": round(sum(u["p"] for u in top) / tc, 4) if tc else None,
            "dias_positivos": sum(1 for v in dia.values() if v[1] > 0),
            "por_dia": {d: round(v[1] / v[0], 3) for d, v in sorted(dia.items())}}


def periodo(us, lo, hi, clave=dia_cierre):
    return [u for u in us if lo <= clave(u) <= hi]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", nargs="+", required=True)
    ap.add_argument("--concat", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    us, sd, cob = construir(a.dias, concat=a.concat)
    comp = [u for u in us if u["completa"]]
    res = {"definicion": "cosechable T in (60,270], 50 acc, completas, dia de cierre", "concat": a.concat,
           "dias": a.dias, "unidades_totales": len(us), "incompletas": len(us) - len(comp), "sin_desenlace": sd,
           "cobertura": cob,
           "in_sample_06_16": cifras(periodo(comp, *IN_SAMPLE)), "forward_17_en_adelante": cifras(periodo(comp, *FORWARD))}
    print(json.dumps(res, indent=1, ensure_ascii=False))
    if a.out:
        tmp = a.out + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(res, fh, indent=1, ensure_ascii=False)
        os.replace(tmp, a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
