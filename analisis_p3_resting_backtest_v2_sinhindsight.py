"""
P3 v2 -- backtest SIN hindsight de la regla de disparo anticipatorio (GBM_LATE_15M).

Diferencia frente a analisis_p3_resting_backtest.py (v1, commit e7d060a5f1):
  v1 usaba el precio de la senal YA CONFIRMADA como referencia del offset, y
  solo miraba mercados donde GBM_LATE_15M SI disparo -- dos sesgos reales
  (hindsight + seleccion de poblacion) que el propio v1 dejo como pendiente.

v2 corrige ambos:
  1. Sin hindsight: el disparador es una version MAS BLANDA del mismo gate
     que usa la produccion (edge = p_up - py, |edge|>=0.03 dispara BUY_YES/
     BUY_NO en _s_gbm_late). Aqui se usa un umbral MENOR (UMBRAL_BLANDO),
     calculado con datos que ya existian en ese instante -- nada del futuro.
  2. Sin sesgo de poblacion: se recorre CADA mercado GBM_LATE_15M evaluado
     (incluidos los SKIP, que en v1 no aparecian) y se sigue el libro desde
     el primer cruce del umbral blando, sin condicionar a que la senal dura
     llegue a confirmar nunca.

Fuente de "verdad" de resolucion: como no hay tabla de resolucion oficial
universal a mano, se usa el ULTIMO ask_yes observado en libro_ambos_lados
cerca de end_date como proxy (mercados binarios convergen a ~0/~1). Se
descartan mercados donde ese proxy no es concluyente (entre 0.03 y 0.97).

Solo lectura. No coloca ninguna orden.
"""
import csv
import math
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

PRED_DIR = Path("data/shadow")
DATALOGS_DIR = Path("/root/polymarket-research-datalogs")

DIAS = [f"2026-08-{d:02d}" for d in range(8, 13)]  # 08..12 -- 13 esta a medias, se excluye
ESTRATEGIA = "GBM_LATE_15M"
UMBRAL_BLANDO = 0.03   # mitad del umbral duro de produccion (0.03)
UMBRAL_DURO = 0.03      # el que usa _s_gbm_late para disparar de verdad
MIN_RESTANTE_MIN = 3.0  # exige tiempo real de exposicion
OFFSETS = [0.05, 0.10, 0.15]
RESOLUCION_YES = 0.97
RESOLUCION_NO = 0.03


def norm_cdf(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def parse_ts(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def cargar_predicciones_dia(fecha: str):
    path = PRED_DIR / f"predictions_{fecha}.csv"
    if not path.exists():
        return []
    out = []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] != ESTRATEGIA:
                continue
            try:
                import json
                feats = json.loads(r["features"]) if r.get("features") else {}
                d_gbm = feats.get("d_gbm")
                restante_min = feats.get("restante_min")
                py = feats.get("py_entrada")
                if d_gbm is None or restante_min is None or py is None:
                    continue
                d_gbm = float(d_gbm)
                restante_min = float(restante_min)
                py = float(py)
            except Exception:
                continue
            out.append({
                "ts": parse_ts(r["timestamp_utc"]),
                "market_id": r["market_id"],
                "subtype": r["subtype"],
                "end_date": r["end_date"],
                "d_gbm": d_gbm, "restante_min": restante_min, "py": py,
            })
    return out


def cargar_libro_dia(fecha: str):
    path = DATALOGS_DIR / f"libro_ambos_lados_{fecha}.csv"
    out = defaultdict(list)
    if not path.exists():
        return out
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                ts = parse_ts(r["timestamp_utc"])
                ay = float(r["ask_yes"]) if r["ask_yes"] else None
                an = float(r["ask_no"]) if r["ask_no"] else None
            except (ValueError, TypeError):
                continue
            out[r["market_id"]].append((ts, ay, an))
    for mid in out:
        out[mid].sort(key=lambda x: x[0])
    return out


def main():
    # 1) cargar predicciones de todos los dias y agrupar por market_id
    todas = []
    for fecha in DIAS:
        todas.extend(cargar_predicciones_dia(fecha))
    print(f"filas predictions GBM_LATE_15M ({DIAS[0]}..{DIAS[-1]}): {len(todas)}")

    por_mercado = defaultdict(list)
    for r in todas:
        por_mercado[r["market_id"]].append(r)
    for mid in por_mercado:
        por_mercado[mid].sort(key=lambda x: x["ts"])
    print(f"mercados distintos evaluados: {len(por_mercado)}")

    # 2) detectar pre-senal por mercado: primer cruce del umbral blando
    pre_senales = []
    n_confirma_duro = 0
    for mid, filas in por_mercado.items():
        pre = None
        confirma_duro = False
        for r in filas:
            p_up = norm_cdf(r["d_gbm"])
            edge = p_up - r["py"]
            if not confirma_duro and abs(edge) >= UMBRAL_DURO:
                confirma_duro = True
            if pre is None and abs(edge) >= UMBRAL_BLANDO and r["restante_min"] >= MIN_RESTANTE_MIN:
                pre = dict(r)
                pre["edge"] = edge
                pre["direccion"] = "YES" if edge > 0 else "NO"
        if pre is not None:
            pre["confirma_duro_alguna_vez"] = confirma_duro
            pre_senales.append(pre)
            if confirma_duro:
                n_confirma_duro += 1

    print(f"pre-senales blandas detectadas: {len(pre_senales)}")
    print(f"  de las cuales SI llegan a confirmar el umbral duro en algun momento: {n_confirma_duro} "
          f"({100*n_confirma_duro/max(1,len(pre_senales)):.1f}%)")

    # 3) cargar libro por dia bajo demanda (cache)
    libro_cache = {}

    def libro_de(fecha):
        if fecha not in libro_cache:
            libro_cache[fecha] = cargar_libro_dia(fecha)
        return libro_cache[fecha]

    resultados = []
    n_sin_libro = 0
    n_resolucion_ambigua = 0
    for pre in pre_senales:
        mid = pre["market_id"]
        fecha_pre = pre["ts"].strftime("%Y-%m-%d")
        try:
            fecha_end = parse_ts(pre["end_date"]).strftime("%Y-%m-%d")
        except Exception:
            fecha_end = fecha_pre

        serie = list(libro_de(fecha_pre).get(mid, []))
        if fecha_end != fecha_pre:
            serie += libro_de(fecha_end).get(mid, [])
        serie.sort(key=lambda x: x[0])
        if not serie:
            n_sin_libro += 1
            continue

        # resolucion proxy: ultimo ask_yes observado
        ultimos_ay = [ay for _, ay, _ in serie if ay is not None]
        if not ultimos_ay:
            n_sin_libro += 1
            continue
        ay_final = ultimos_ay[-1]
        if ay_final >= RESOLUCION_YES:
            outcome = "YES"
        elif ay_final <= RESOLUCION_NO:
            outcome = "NO"
        else:
            n_resolucion_ambigua += 1
            continue

        direccion = pre["direccion"]
        py_pre = pre["py"]
        acierto = (direccion == outcome)

        # serie de nuestro lado, DESDE la pre-senal en adelante
        propia = [(ts, ay if direccion == "YES" else an) for ts, ay, an in serie if ts >= pre["ts"]]
        propia = [(ts, p) for ts, p in propia if p is not None]
        if not propia:
            continue

        try:
            activo, marco = pre["subtype"].split("#")
        except ValueError:
            activo, marco = pre["subtype"], "?"

        for off in OFFSETS:
            nivel = py_pre - off
            if nivel <= 0.01:
                continue
            cruce = next(((ts, p) for ts, p in propia if p <= nivel), None)
            filled = cruce is not None
            lead_s = (cruce[0] - pre["ts"]).total_seconds() if filled else None
            if filled:
                stake = 1.05
                shares = stake / nivel
                pnl_maker = shares - stake if acierto else -stake  # maker fee=0
            else:
                pnl_maker = None
            resultados.append({
                "activo": activo, "marco": marco, "offset": off,
                "filled": filled, "lead_s": lead_s, "pnl_maker": pnl_maker,
                "confirma_duro": pre["confirma_duro_alguna_vez"],
                "market_id": mid,
            })

    print(f"mercados sin libro disponible: {n_sin_libro}")
    print(f"mercados con resolucion ambigua (ask_yes final entre 0.03-0.97): {n_resolucion_ambigua}")
    print(f"filas evaluadas (pre-senal x offset): {len(resultados)}")

    print("\n=== RESUMEN POR OFFSET (poblacion COMPLETA de pre-senales, sin condicionar a confirmacion dura) ===")
    for off in OFFSETS:
        sub = [x for x in resultados if x["offset"] == off]
        if not sub:
            continue
        n = len(sub)
        n_fill = sum(1 for x in sub if x["filled"])
        maker_pnls = [x["pnl_maker"] for x in sub if x["filled"]]
        pnl_medio = sum(maker_pnls) / len(maker_pnls) if maker_pnls else None
        print(f"offset={off:.2f}  n_presenales={n}  fill_rate={100*n_fill/n:.1f}%  "
              f"pnl_maker/tr={pnl_medio}")

    print("\n=== MISMO offset=0.10, separado por si la senal dura confirmo despues o no ===")
    for confirma in (True, False):
        sub = [x for x in resultados if x["offset"] == 0.10 and x["confirma_duro"] == confirma]
        if not sub:
            continue
        n = len(sub)
        n_fill = sum(1 for x in sub if x["filled"])
        maker_pnls = [x["pnl_maker"] for x in sub if x["filled"]]
        pnl_medio = sum(maker_pnls) / len(maker_pnls) if maker_pnls else None
        print(f"confirma_duro={confirma}  n={n}  fill_rate={100*n_fill/n:.1f}%  pnl_maker/tr={pnl_medio}")

    print("\n=== DESAGREGADO offset=0.10 por activo (poblacion completa) ===")
    grp = defaultdict(list)
    for x in resultados:
        if x["offset"] == 0.10:
            grp[x["activo"]].append(x)
    for activo, sub in sorted(grp.items()):
        n = len(sub)
        n_fill = sum(1 for x in sub if x["filled"])
        if n_fill == 0:
            print(f"{activo}: n={n} fill=0")
            continue
        maker_pnls = [x["pnl_maker"] for x in sub if x["filled"]]
        pnl_medio = sum(maker_pnls) / len(maker_pnls)
        print(f"{activo}: n={n} fill_rate={100*n_fill/n:.1f}% pnl_maker/tr={pnl_medio:+.3f}")


if __name__ == "__main__":
    main()
