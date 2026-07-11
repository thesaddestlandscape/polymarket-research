#!/usr/bin/env python3
"""Read-only: barrido de vecinos para constantes clave ya "optimizadas" en
shadow_predict.py — ¿el valor actual está en una MESETA (vecinos rinden
parecido → robusto) o es un PICO aislado (vecinos caen fuerte → probable
sobreajuste al backtest concreto que lo fijó)?

Idea del artículo de breakout trading (09-Jul, ver conversación): un ATR-
multiplier de 1.8 solo se acepta si 1.7/1.9 rinden similar. Aplicado aquí a
5 constantes fijadas por un único backtest en shadow_predict.py.

Métrica: misma que scan_blacklist_hours.py (hit% + edge_real = |edge_neto|
con signo del acierto). Disciplina del proyecto: n<15 no concluye nada.
NO toca producción — solo lee results.csv. Correr desde la raíz del repo:
    python3 barrido_vecinos.py
"""
import csv
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "data", "shadow", "results.csv")
ROWS = list(csv.DictReader(open(RES)))
N_MIN = 15


def _features(r):
    try:
        return json.loads(r["features"]) if r["features"] else {}
    except Exception:
        return {}


def sedge(r):
    try:
        e = abs(float(r["edge_neto"]))
        return e if r["acierto"] == "1" else -e
    except Exception:
        return None


def agg(rows):
    n = len(rows)
    if not n:
        return (0, 0.0, 0.0)
    hit = sum(1 for r in rows if r["acierto"] == "1") / n
    ses = [x for x in (sedge(r) for r in rows) if x is not None]
    return (n, hit, sum(ses) / len(ses) if ses else 0.0)


def base_rows(strategy, subtype_suffix=None, decision=None):
    out = []
    for r in ROWS:
        if r["strategy"] != strategy:
            continue
        if subtype_suffix and not r.get("subtype", "").endswith(subtype_suffix):
            continue
        if decision and r.get("decision") != decision:
            continue
        out.append(r)
    return out


def sweep(label, rows, feature, current, steps, bound_type, extra=None, transform=abs):
    """bound_type: 'min' (feature transform >= umbral pasa) o 'max' (feature
    transform < umbral pasa). extra: filtro adicional fijo (lambda val -> bool)
    aplicado siempre, independiente del barrido."""
    print(f"\n### {label}  (constante actual = {current})")
    pre = []
    for r in rows:
        f = _features(r)
        v = f.get(feature)
        if v is None:
            continue
        if extra and not extra(f):
            continue
        pre.append((r, v))
    if len(pre) < N_MIN:
        print(f"  n total con feature disponible = {len(pre)} (insuficiente, skip)")
        return

    resultados = []
    sel_por_umbral = {}
    for umbral in sorted(set(steps + [current])):
        sel = []
        for r, v in pre:
            tv = transform(v)
            if bound_type == "min":
                ok = tv >= umbral
            else:  # max
                ok = tv < umbral
            if ok:
                sel.append(r)
        sel_por_umbral[umbral] = set(id(r) for r in sel)
        n, hit, edge = agg(sel)
        resultados.append((umbral, n, hit, edge, sel))

    for i, (umbral, n, hit, edge, sel) in enumerate(resultados):
        marca = "  <- ACTUAL" if abs(umbral - current) < 1e-9 else ""
        if n < N_MIN:
            print(f"  umbral={umbral:<7} n={n:<5} (insuficiente){marca}")
        else:
            print(f"  umbral={umbral:<7} n={n:<5} hit={hit*100:5.1f}%  edge_real={edge:+.4f}{marca}")
        # Propuesta #5 backlog quant-desk (Part V reducción de varianza):
        # umbral y vecino son conjuntos ANIDADOS (comparten casi todas las
        # filas), así que comparar sus edges agregados diluye la señal real
        # con ruido compartido. La franja MARGINAL (solo las filas que un
        # umbral tiene y el anterior no) aísla justo lo que el barrido
        # pregunta: ¿las filas que se ganan/pierden al mover el umbral son
        # buenas o malas? Mucho más sensible para detectar pico vs meseta.
        if i > 0:
            umbral_prev = resultados[i - 1][0]
            ids_prev, ids_cur = sel_por_umbral[umbral_prev], sel_por_umbral[umbral]
            marginal_ids = ids_cur ^ ids_prev  # diferencia simétrica
            if marginal_ids:
                marginal_rows = [r for r, _ in pre if id(r) in marginal_ids]
                n_m, hit_m, edge_m = agg(marginal_rows)
                if n_m >= N_MIN:
                    print(f"           franja marginal vs {umbral_prev}: n={n_m:<4} "
                          f"hit={hit_m*100:5.1f}%  edge_real={edge_m:+.4f}")

    # Veredicto simple: comparar el edge del actual con la media de sus dos vecinos
    # inmediatos (si tienen n suficiente).
    idx_actual = next((i for i, x in enumerate(resultados) if abs(x[0] - current) < 1e-9), None)
    if idx_actual is not None:
        vecinos = []
        if idx_actual > 0 and resultados[idx_actual - 1][1] >= N_MIN:
            vecinos.append(resultados[idx_actual - 1][3])
        if idx_actual < len(resultados) - 1 and resultados[idx_actual + 1][1] >= N_MIN:
            vecinos.append(resultados[idx_actual + 1][3])
        actual_n = resultados[idx_actual][1]
        if vecinos and actual_n >= N_MIN:
            actual_edge = resultados[idx_actual][3]
            media_vecinos = sum(vecinos) / len(vecinos)
            gap = actual_edge - media_vecinos
            if abs(gap) < 0.02:
                print(f"  => MESETA: vecinos a {gap:+.4f} de distancia, valor robusto")
            elif gap > 0:
                print(f"  => POSIBLE PICO: actual supera vecinos por {gap:+.4f} (sospechar sobreajuste)")
            else:
                print(f"  => actual PEOR que vecinos por {gap:+.4f} (revisar si el umbral sigue vigente)")
        else:
            print("  => vecinos sin n suficiente para veredicto")


def main():
    print("=" * 78)
    print("BARRIDO DE VECINOS — constantes optimizadas de shadow_predict.py")
    print("=" * 78)

    # 1. ORDER_FLOW_5M: DELTA_MIN=0.38 (banda mínima, BUY_NO)
    of_rows = base_rows("ORDER_FLOW_5M", decision="BUY_NO")
    sweep(
        "ORDER_FLOW_5M#BUY_NO — DELTA_MIN (banda mínima |delta_ratio|)",
        of_rows, "delta_ratio", 0.38,
        steps=[0.30, 0.34, 0.38, 0.42, 0.46],
        bound_type="min",
        extra=lambda f: f.get("delta_ratio", 0) < 0 and abs(f.get("delta_ratio", 0)) <= 0.46,
    )

    # 2. ORDER_FLOW_5M: DELTA_MAX=0.46 (banda máxima, BUY_NO)
    sweep(
        "ORDER_FLOW_5M#BUY_NO — DELTA_MAX (banda máxima |delta_ratio|)",
        of_rows, "delta_ratio", 0.46,
        steps=[0.38, 0.42, 0.46, 0.50, 0.54],
        bound_type="max",
        extra=lambda f: f.get("delta_ratio", 0) < 0 and abs(f.get("delta_ratio", 0)) >= 0.38,
    )

    # 3. UPDOWN_GBM#15min BUY_YES: BUY_YES_15M_TH_MAX=0.2 (T_h máximo, solo tardío)
    gbm15_yes = base_rows("UPDOWN_GBM", subtype_suffix="15min", decision="BUY_YES")
    sweep(
        "UPDOWN_GBM#15min#BUY_YES — BUY_YES_15M_TH_MAX (T_h máximo)",
        gbm15_yes, "T_h", 0.2,
        steps=[0.10, 0.15, 0.20, 0.25, 0.30],
        bound_type="max",
        transform=lambda v: v,
    )

    # 4. UPDOWN_GBM#15min BUY_YES: DRIFT_60_BUY_YES_15M_HI=0.25 (LO=0.0 fijo)
    sweep(
        "UPDOWN_GBM#15min#BUY_YES — DRIFT_60_HI (banda drift_60min, LO=0.0 fijo)",
        gbm15_yes, "drift_60min", 0.25,
        steps=[0.15, 0.20, 0.25, 0.30, 0.35, 0.50],
        bound_type="max",
        transform=lambda v: v,
        extra=lambda f: f.get("drift_60min") is not None and f.get("drift_60min") >= 0.0,
    )

    # 5. GBM_LATE_15M: GBM_LATE_15M_REST_MIN_HI=12.0 (minutos restantes máximos)
    gbm_late = base_rows("GBM_LATE_15M")
    sweep(
        "GBM_LATE_15M — REST_MIN_HI (minutos restantes máximos, todos los pares/direcciones)",
        gbm_late, "restante_min", 12.0,
        steps=[8.0, 9.0, 10.0, 10.5, 11.0, 12.0, 13.0, 14.0],
        bound_type="max",
        transform=lambda v: v,
        extra=lambda f: f.get("restante_min") is not None and f.get("restante_min") >= 3.0,
    )

    # 6. GBM_LATE (familia): GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 (distancia mínima drift ventana)
    sweep(
        "GBM_LATE_15M — GBM_LATE_DRIFT_VENT_MIN_PCT (distancia mínima |drift_ventana_pct|)",
        gbm_late, "drift_ventana_pct", 0.02,
        steps=[0.00, 0.01, 0.02, 0.03, 0.05, 0.08],
        bound_type="min",
    )

    print("\n" + "=" * 78)
    print("Fin. Disciplina: n<15 no concluye nada; 'PICO' = sospechar sobreajuste,")
    print("no cambiar el umbral solo por esto — confirmar con más ventanas/tiempo.")


if __name__ == "__main__":
    main()
