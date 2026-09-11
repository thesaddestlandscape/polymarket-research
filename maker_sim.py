"""
maker_sim.py — Simulación OBSERVACIONAL de entrada maker (2026-07-02).

Pregunta a responder: si en vez de entrar taker (FOK contra el ask) hubiéramos
puesto una limit pasiva 2 céntimos mejor en los primeros minutos de la ventana,
¿qué % de nuestras señales se habría llenado y cuánto mejora el EV?

Contexto: el estudio de ballenas verificadas (2026-07-02) muestra que el flujo
informado llega en la fase TARDÍA de la ventana — cotizar pasivo en la fase
temprana (flujo retail) y cancelar antes de la fase sniper es la conversión
taker→maker segura. Sobre precio ~0.5, 2-3 céntimos de mejora de entrada son
~8-10% más de payoff por trade con la misma señal.

Metodología de fill (conservadora-aproximada): la limit se considera LLENADA
si algún trade real del mercado (data-api /trades) imprimió en nuestro token
a precio <= limit dentro de [ts_predicción, fin_ventana - CANCEL_MIN]. No
modela prioridad de cola FIFO; un print estrictamente por debajo del límite
implica que el nivel se atravesó. Con limit 500 trades por mercado puede
infraestimar fills en mercados muy activos (aceptable: sesgo conservador).

Se invoca desde shadow_resolve al resolver predicciones UPDOWN_GBM/GBM_LATE_15M
de 15min. NUNCA lanza excepciones hacia arriba (resolve cierra trades live).
Salida: data/shadow/maker_sim.csv
"""
import csv
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

DIR_SHADOW = Path(__file__).parent / "data" / "shadow"
CSV_PATH = DIR_SHADOW / "maker_sim.csv"
DATA_API = "https://data-api.polymarket.com"
H = {"User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)"}

MEJORA = 0.02             # limit 2 céntimos mejor que el precio taker
CANCEL_MIN = 4            # cancelar la limit N min antes del cierre (fase sniper)
ESTRATEGIAS_SIM = {"UPDOWN_GBM", "GBM_LATE_15M"}

_CAMPOS = ["resolution_ts", "strategy", "subtype", "market_id", "decision",
           "taker_price", "limit_price", "filled", "n_trades_vistos",
           "acierto", "pnl1_taker", "pnl1_maker"]


def _parse_ts(s):
    try:
        dt = datetime.fromisoformat((s or "").replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def simular(pred: dict, mercado: dict, res: dict, resolution_ts: str) -> None:
    """Simula la entrada maker para una predicción recién resuelta. Nunca lanza."""
    try:
        strategy = pred.get("strategy", "")
        subtype = pred.get("subtype") or ""
        decision = pred.get("decision", "")
        if strategy not in ESTRATEGIAS_SIM or "15min" not in subtype:
            return
        if decision not in ("BUY_YES", "BUY_NO"):
            return

        py = float(pred.get("precio_yes_mercado") or 0)
        if not (0.02 < py < 0.98):
            return
        taker = py if decision == "BUY_YES" else round(1 - py, 4)
        limit = round(taker - MEJORA, 4)
        if limit <= 0.01:
            return

        t0 = _parse_ts(pred.get("timestamp_utc"))
        end = _parse_ts(pred.get("end_date"))
        if not t0 or not end:
            return
        t1 = end - timedelta(minutes=CANCEL_MIN)
        if t1 <= t0:
            return  # señal demasiado tardía para la variante maker

        cond_id = (mercado or {}).get("conditionId") or ""
        if not cond_id:
            return
        r = requests.get(f"{DATA_API}/trades",
                         params={"market": cond_id, "limit": 500},
                         headers=H, timeout=10)
        trades = r.json() or []
        time.sleep(0.15)

        lado = "Up" if decision == "BUY_YES" else "Down"
        filled = 0
        for t in trades:
            if t.get("outcome") != lado:
                continue
            try:
                p = float(t.get("price") or 0)
                tt = datetime.fromtimestamp(int(t["timestamp"]), tz=timezone.utc)
            except Exception:
                continue
            if p <= limit and t0 <= tt <= t1:
                filled = 1
                break

        acierto = int(res.get("acierto") or 0)
        # PNL por 1€ de stake (sin fees, comparabilidad pura de entrada)
        pnl1_taker = round(1 / taker - 1, 4) if acierto else -1.0
        pnl1_maker = (round(1 / limit - 1, 4) if acierto else -1.0) if filled else 0.0

        nuevo = not CSV_PATH.exists()
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=_CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerow({
                "resolution_ts": resolution_ts,
                "strategy": strategy,
                "subtype": subtype,
                "market_id": pred.get("market_id", ""),
                "decision": decision,
                "taker_price": taker,
                "limit_price": limit,
                "filled": filled,
                "n_trades_vistos": len(trades),
                "acierto": acierto,
                "pnl1_taker": pnl1_taker,
                "pnl1_maker": pnl1_maker,
            })
    except Exception as e:
        # Best-effort: la simulación jamás debe afectar a la resolución real
        print(f"  [maker_sim] warn: {type(e).__name__}: {e}")


def resumen() -> str | None:
    """Resumen acumulado fill-rate + EV. None si no hay datos suficientes."""
    try:
        if not CSV_PATH.exists():
            return None
        rows = list(csv.DictReader(open(CSV_PATH, encoding="utf-8")))
        n = len(rows)
        if n < 5:
            return None
        fills = sum(1 for r in rows if r["filled"] == "1")
        ev_taker = sum(float(r["pnl1_taker"]) for r in rows) / n
        # EV maker por señal (las no llenadas cuentan 0 — coste de oportunidad implícito)
        ev_maker = sum(float(r["pnl1_maker"]) for r in rows) / n
        return (f"maker_sim: n={n} fill_rate={fills/n:.0%} "
                f"EV/señal taker={ev_taker:+.4f}€ maker={ev_maker:+.4f}€ (por 1€ stake)")
    except Exception:
        return None
