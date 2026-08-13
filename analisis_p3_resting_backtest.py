"""
P3 -- backtest de FACTIBILIDAD para ordenes resting anticipatorias (GBM_LATE family).
Solo lectura, no toca dinero ni coloca ninguna orden. Ver memoria
project_profundidad_libro_p1_p2_construidos_13ago para el contexto (P1/P2 ya
construidos, P3 pendiente).

Pregunta que responde (condicion NECESARIA, no suficiente -- ver caveats al final):
dado un mercado donde GBM_LATE ya disparo senal en direccion X con precio de
senal P_signal, ¿el libro de ESE MISMO lado paso por niveles mas baratos
(P_signal - offset) ANTES de que la senal disparase? Si nunca pasa por ahi
(salta directo), colocar una orden resting mas barata es inutil incluso con
retrospectiva perfecta -- mata la idea sin gastar mas tiempo. Si SI pasa,
cuantifica cuanto antes (tiempo de exposicion) y que PnL hipotetico (maker,
fee=0) habria dado frente al PnL real de entrar de taker al precio de senal.

Fuente libro continuo: /root/polymarket-research-datalogs/libro_ambos_lados_YYYY-MM-DD.csv
(fuera del repo, no versionado, cron `libroambos` desde 28-Jul).
"""
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

RESULTS_CSV = Path("data/shadow/results.csv")
DATALOGS_DIR = Path("/root/polymarket-research-datalogs")

FAMILIA_GBM_LATE = {
    "GBM_LATE_15M", "GBM_LATE_5M", "GBM_LATE_15M_TARDIO",
    "GBM_LATE_15M_ESPACIO_ATR", "GBM_LATE_15M_MULTIHORIZONTE",
    "GBM_LATE_15M_PYCONFIRMADO",
}

DESDE = "2026-08-08"  # datalogs sin comprimir disponibles 08-13 Ago
OFFSETS = [0.05, 0.10, 0.15, 0.20]
FEE_TAKER = 0.07  # ya establecido en el proyecto


def parse_ts(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def cargar_predicciones():
    preds = []
    with open(RESULTS_CSV, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] not in FAMILIA_GBM_LATE:
                continue
            if not r["prediction_timestamp"] or r["prediction_timestamp"] < DESDE:
                continue
            if r["outcome_real"] not in ("YES", "NO"):
                continue
            try:
                precio = float(r["precio_yes_mercado"])
            except (ValueError, TypeError):
                continue
            preds.append(r)
    return preds


def cargar_libro_dia(fecha: str):
    """market_id -> lista de (timestamp, ask_yes, ask_no) ordenada."""
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
    preds = cargar_predicciones()
    print(f"predicciones GBM_LATE family desde {DESDE}: {len(preds)}")

    # agrupar por dia de prediction_timestamp para cargar el libro solo una vez por dia
    por_dia = defaultdict(list)
    for r in preds:
        fecha = r["prediction_timestamp"][:10]
        por_dia[fecha].append(r)

    resultados = []  # cada uno: dict con activo, marco, offset, filled, lead_s, pnl_maker, pnl_taker_real
    dias_cargados = {}
    for fecha, filas in sorted(por_dia.items()):
        # el mercado puede haber abierto el dia anterior (15/60min normalmente no cruza medianoche,
        # pero cargamos tambien el dia anterior por si acaso)
        fecha_prev = (datetime.fromisoformat(fecha) - timedelta(days=1)).strftime("%Y-%m-%d")
        libro_hoy = dias_cargados.get(fecha) or cargar_libro_dia(fecha)
        libro_prev = dias_cargados.get(fecha_prev) or cargar_libro_dia(fecha_prev)
        dias_cargados[fecha] = libro_hoy
        dias_cargados[fecha_prev] = libro_prev

        for r in filas:
            mid = r["market_id"]
            serie = libro_prev.get(mid, []) + libro_hoy.get(mid, [])
            if not serie:
                continue
            ts_signal = parse_ts(r["prediction_timestamp"])
            decision = r["decision"]
            precio_signal = float(r["precio_yes_mercado"])
            outcome = r["outcome_real"]
            acierto = (decision == "BUY_YES" and outcome == "YES") or (decision == "BUY_NO" and outcome == "NO")

            # serie de nuestro lado, solo puntos ANTES de la senal
            antes = [(ts, ay if decision == "BUY_YES" else an) for ts, ay, an in serie if ts < ts_signal]
            antes = [(ts, p) for ts, p in antes if p is not None]
            if not antes:
                continue

            try:
                activo, marco = r["subtype"].split("#")
            except ValueError:
                activo, marco = r["subtype"], "?"

            # PnL real de taker al precio de senal (ya conocido/documentado, se recalcula aqui
            # para comparar en la misma muestra exacta)
            stake = 1.05
            shares_taker = stake / precio_signal
            pnl_taker = shares_taker * (1 - FEE_TAKER) - stake if acierto else -stake

            for off in OFFSETS:
                nivel = precio_signal - off
                if nivel <= 0.01:
                    continue
                cruce = next(((ts, p) for ts, p in antes if p <= nivel), None)
                filled = cruce is not None
                lead_s = (ts_signal - cruce[0]).total_seconds() if filled else None
                if filled:
                    shares_maker = stake / nivel
                    pnl_maker = shares_maker - stake if acierto else -stake  # maker fee=0
                else:
                    pnl_maker = None
                resultados.append({
                    "activo": activo, "marco": marco, "strategy": r["strategy"],
                    "offset": off, "filled": filled, "lead_s": lead_s,
                    "pnl_maker": pnl_maker, "pnl_taker": pnl_taker, "acierto": acierto,
                    "market_id": mid,
                })

    print(f"filas evaluadas (pred x offset con libro disponible): {len(resultados)}")

    # resumen agregado por offset
    print("\n=== RESUMEN POR OFFSET (todas las familias/activos) ===")
    for off in OFFSETS:
        sub = [x for x in resultados if x["offset"] == off]
        if not sub:
            continue
        n = len(sub)
        n_fill = sum(1 for x in sub if x["filled"])
        pct_fill = 100 * n_fill / n
        leads = [x["lead_s"] for x in sub if x["filled"]]
        lead_med = sorted(leads)[len(leads) // 2] if leads else None
        maker_pnls = [x["pnl_maker"] for x in sub if x["filled"]]
        pnl_maker_medio = sum(maker_pnls) / len(maker_pnls) if maker_pnls else None
        taker_pnls_mismos = [x["pnl_taker"] for x in sub if x["filled"]]
        pnl_taker_medio = sum(taker_pnls_mismos) / len(taker_pnls_mismos) if taker_pnls_mismos else None
        print(f"offset={off:.2f}  n={n}  fill_rate={pct_fill:.1f}%  lead_mediana={lead_med}s  "
              f"pnl_maker/tr={pnl_maker_medio}  pnl_taker/tr(mismos)={pnl_taker_medio}")

    # desagregado por activo x marco, offset=0.10 (el mas representativo)
    print("\n=== DESAGREGADO offset=0.10 por activo#marco ===")
    grp = defaultdict(list)
    for x in resultados:
        if x["offset"] == 0.10:
            grp[(x["activo"], x["marco"])].append(x)
    for (activo, marco), sub in sorted(grp.items()):
        n = len(sub)
        n_fill = sum(1 for x in sub if x["filled"])
        if n_fill == 0:
            print(f"{activo}#{marco}: n={n} fill=0")
            continue
        maker_pnls = [x["pnl_maker"] for x in sub if x["filled"]]
        pnl_medio = sum(maker_pnls) / len(maker_pnls)
        print(f"{activo}#{marco}: n={n} fill_rate={100*n_fill/n:.1f}% pnl_maker/tr={pnl_medio:+.3f}")

    with open("data/shadow/p3_resting_backtest.json", "w", encoding="utf-8") as f:
        json.dump({
            "generado_utc": datetime.now(timezone.utc).isoformat(),
            "n_predicciones": len(preds),
            "n_filas_evaluadas": len(resultados),
            "resumen_por_offset": [
                {
                    "offset": off,
                    "n": len([x for x in resultados if x["offset"] == off]),
                    "fill_rate": (
                        100 * sum(1 for x in resultados if x["offset"] == off and x["filled"])
                        / max(1, len([x for x in resultados if x["offset"] == off]))
                    ),
                }
                for off in OFFSETS
            ],
        }, f, indent=2)
    print("\nGuardado data/shadow/p3_resting_backtest.json")


if __name__ == "__main__":
    main()
