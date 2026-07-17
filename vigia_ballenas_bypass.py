#!/usr/bin/env python3
"""Vigía ballenas-bypass: acumula el resultado REAL de cada señal que
`veto_ballenas` bloqueó, para poder responder con n creciente (no caso a
caso) si un bypass por conviction/edge propio ("si nuestra señal es muy
buena, dejar entrar aunque las ballenas no confirmen") merecería la pena.

Origen (17-Jul, petición Javi): la señal FAVORITO_CONFIRMADO#ETH#60min#BUY_NO
del 16-Jul 23:09 fue bloqueada 12 veces por veto_ballenas (concentración
12.5-22% << umbral 60%) y el mercado resolvió a su favor (+0.70€ hipotético
con stake real 1.05€) — un solo caso no prueba nada (regla del proyecto:
n<15 no concluye), pero apunta a la pregunta correcta. Este vigía no decide
nada ni cambia comportamiento live: solo registra.

Método: cruza `data/live/veto_ballenas_eventos.jsonl` (veta=True) con la
predicción real que originó la señal bloqueada (`data/shadow/predictions_*.csv`,
misma subtype+decision, timestamp más reciente ANTES del bloqueo) y con su
resolución ya calculada por shadow_resolve.py (`data/shadow/results.csv` —
resuelve TODAS las predicciones, no solo las que se ejecutan en real). Con
eso calcula qué pnl_neto habría dado ENTRANDO IGUAL con el stake real
pineado (mismo fee_est que usa el propio veto en live_trade.py:2219), sin
slippage (optimista, igual que idea_smart_exit.md).

Ledger acumulativo en data/shadow/ballenas_veto_bypass.csv (una fila por
market_id bloqueado, se completa cuando el mercado resuelve). Read-only
respecto a todo lo demás — no toca trades.csv, config_live.json ni
strategy_params.json. Cron sugerido: cada 15-20min (ver crontab).
"""
import csv
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

EVENTOS_PATH = REPO / "data/live/veto_ballenas_eventos.jsonl"
PREDICTIONS_DIR = REPO / "data/shadow"
RESULTS_CSV = REPO / "data/shadow/results.csv"
CONFIG_PATH = REPO / "data/live/config_live.json"
LEDGER_CSV = REPO / "data/shadow/ballenas_veto_bypass.csv"
LATCH_PATH = REPO / "data/live/vigia_ballenas_bypass_latch.json"

FEE_RATE_TAKER_CRYPTO = 0.07  # mismo valor que live_trade.py:41, duplicado
                               # a propósito (script standalone, sin pagar
                               # el import pesado de live_trade/py_clob_client)
STAKE_ASUMIDO_DEFAULT = 1.05

_MARCO_INV = {"5m": "5min", "15m": "15min", "60m": "60min", "240m": "240min"}

N_ALERTA = 15  # mismo umbral n≥15 del resto del proyecto para "hay algo que mirar"


def _parse_dt(s):
    try:
        dt = datetime.fromisoformat((s or "").replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def _stake_asumido() -> float:
    try:
        c = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        return float(c.get("riesgo", {}).get("min_stake_eur", STAKE_ASUMIDO_DEFAULT))
    except Exception:
        return STAKE_ASUMIDO_DEFAULT


def _cargar_bloqueos() -> dict:
    """market_id -> primer evento veta=True (ts más antiguo) + n_intentos."""
    bloqueos = {}
    if not EVENTOS_PATH.exists():
        return bloqueos
    with open(EVENTOS_PATH, encoding="utf-8") as f:
        for linea in f:
            try:
                ev = json.loads(linea)
            except Exception:
                continue
            if not ev.get("veta"):
                continue
            mid = str(ev.get("market_id"))
            ts = _parse_dt(ev.get("ts"))
            if ts is None:
                continue
            d = bloqueos.setdefault(mid, {"primer_evento": ev, "primer_ts": ts, "n_intentos": 0})
            d["n_intentos"] += 1
            if ts < d["primer_ts"]:
                d["primer_ts"] = ts
                d["primer_evento"] = ev
    return bloqueos


def _predicciones_de_fechas(fechas: set) -> list:
    filas = []
    for fecha in fechas:
        p = PREDICTIONS_DIR / f"predictions_{fecha}.csv"
        if not p.exists():
            continue
        with open(p, encoding="utf-8") as f:
            filas.extend(csv.DictReader(f))
    return filas


def _match_prediccion(market_id: str, combo: str, ts_bloqueo: datetime, filas_pred: list) -> dict | None:
    marco = _MARCO_INV.get((combo or "").split("#")[-1])
    activo = (combo or "").split("#")[0]
    if not marco or not activo:
        return None
    subtype_esperado = f"{activo}#{marco}"
    candidatas = []
    for row in filas_pred:
        if str(row.get("market_id")) != str(market_id):
            continue
        if (row.get("subtype") or "") != subtype_esperado:
            continue
        if (row.get("decision") or "SKIP") == "SKIP":
            continue
        ts_pred = _parse_dt(row.get("timestamp_utc"))
        if ts_pred is None or ts_pred > ts_bloqueo + timedelta(seconds=2):
            continue
        candidatas.append((ts_pred, row))
    if not candidatas:
        return None
    candidatas.sort(key=lambda t: t[0])
    return candidatas[-1][1]  # la más reciente antes del bloqueo


def _buscar_resultado(strategy: str, subtype: str, decision: str, ts_pred: str) -> dict | None:
    if not RESULTS_CSV.exists():
        return None
    with open(RESULTS_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("strategy") == strategy and row.get("subtype") == subtype
                    and row.get("decision") == decision
                    and row.get("prediction_timestamp") == ts_pred):
                return row
    return None


def _ic_hist(strategy: str, subtype: str, decision: str) -> tuple[float | None, int | None]:
    try:
        params = json.loads((REPO / "data/shadow/strategy_params.json").read_text(encoding="utf-8"))
    except Exception:
        return None, None
    tupla = params.get("estrategias", {}).get(f"{strategy}#{subtype}")
    if not isinstance(tupla, dict):
        return None, None
    suf = "BUY_YES" if decision == "BUY_YES" else "BUY_NO"
    ic = tupla.get(f"ic_{suf}")
    n = tupla.get(f"n_{suf}")
    try:
        return (float(ic) if ic is not None else None), (int(n) if n is not None else None)
    except (TypeError, ValueError):
        return None, None


def _pnl_hipotetico(py: float, decision: str, outcome_real: str, stake: float) -> tuple[float, float, bool]:
    py = min(0.99, max(0.01, py))
    entry_p = py if decision == "BUY_YES" else round(1.0 - py, 6)
    entry_p = min(0.99, max(0.01, entry_p))
    acierto_dir = (decision == "BUY_YES" and outcome_real == "YES") or \
                  (decision == "BUY_NO" and outcome_real == "NO")
    fee_est = FEE_RATE_TAKER_CRYPTO * py * (1 - py) * stake
    pnl_bruto = stake * (1.0 / entry_p - 1.0) if acierto_dir else -stake
    pnl_neto = pnl_bruto - fee_est
    return round(pnl_neto, 4), round(fee_est, 4), acierto_dir


LEDGER_COLS = [
    "market_id", "ts_bloqueo", "combo", "pct_ballenas", "n_ballenas", "umbral",
    "n_intentos", "strategy", "subtype", "decision", "precio_yes_mercado",
    "edge_neto", "ic_hist", "n_hist", "resuelto", "outcome_real", "acierto_dir",
    "pnl_neto_hipotetico_eur", "fee_est_eur", "motivo_sin_match",
]


def _cargar_ledger() -> dict:
    if not LEDGER_CSV.exists():
        return {}
    with open(LEDGER_CSV, encoding="utf-8") as f:
        return {row["market_id"]: row for row in csv.DictReader(f)}


def _guardar_ledger(ledger: dict):
    LEDGER_CSV.parent.mkdir(parents=True, exist_ok=True)
    filas = sorted(ledger.values(), key=lambda r: r.get("ts_bloqueo", ""))
    with open(LEDGER_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=LEDGER_COLS)
        w.writeheader()
        for row in filas:
            w.writerow({k: row.get(k, "") for k in LEDGER_COLS})


def main() -> int:
    bloqueos = _cargar_bloqueos()
    ledger = _cargar_ledger()
    stake = _stake_asumido()

    pendientes = {mid: d for mid, d in bloqueos.items()
                  if mid not in ledger or ledger[mid].get("resuelto") != "1"}

    if not pendientes:
        print(f"[vigia_ballenas_bypass] sin bloqueos nuevos/pendientes (ledger n={len(ledger)})")
    else:
        fechas = set()
        for d in pendientes.values():
            ts = d["primer_ts"]
            fechas.add(ts.strftime("%Y-%m-%d"))
            fechas.add((ts - timedelta(days=1)).strftime("%Y-%m-%d"))
        filas_pred = _predicciones_de_fechas(fechas)

        actualizados = 0
        for mid, d in pendientes.items():
            ev = d["primer_evento"]
            fila = ledger.get(mid, {k: "" for k in LEDGER_COLS})
            fila.update({
                "market_id": mid,
                "ts_bloqueo": d["primer_ts"].isoformat(timespec="seconds"),
                "combo": ev.get("combo", ""),
                "pct_ballenas": ev.get("pct", ""),
                "n_ballenas": ev.get("n", ""),
                "umbral": ev.get("umbral", ""),
                "n_intentos": d["n_intentos"],
            })

            pred = _match_prediccion(mid, ev.get("combo", ""), d["primer_ts"], filas_pred)
            if pred is None:
                fila["resuelto"] = "0"
                fila["motivo_sin_match"] = "sin_prediccion_encontrada"
                ledger[mid] = fila
                continue

            strategy, subtype, decision = pred["strategy"], pred["subtype"], pred["decision"]
            precio_yes = pred.get("precio_yes_mercado", "")
            fila.update({
                "strategy": strategy, "subtype": subtype, "decision": decision,
                "precio_yes_mercado": precio_yes, "edge_neto": pred.get("edge_neto", ""),
                "motivo_sin_match": "",
            })
            ic, n_ic = _ic_hist(strategy, subtype, decision)
            fila["ic_hist"] = ic if ic is not None else ""
            fila["n_hist"] = n_ic if n_ic is not None else ""

            res = _buscar_resultado(strategy, subtype, decision, pred["timestamp_utc"])
            if res is None:
                fila["resuelto"] = "0"
                ledger[mid] = fila
                continue

            outcome_real = res.get("outcome_real", "")
            try:
                py = float(precio_yes)
            except (TypeError, ValueError):
                fila["resuelto"] = "0"
                fila["motivo_sin_match"] = "precio_invalido"
                ledger[mid] = fila
                continue

            pnl_neto, fee_est, acierto_dir = _pnl_hipotetico(py, decision, outcome_real, stake)
            fila.update({
                "resuelto": "1",
                "outcome_real": outcome_real,
                "acierto_dir": "1" if acierto_dir else "0",
                "pnl_neto_hipotetico_eur": pnl_neto,
                "fee_est_eur": fee_est,
            })
            ledger[mid] = fila
            actualizados += 1

        _guardar_ledger(ledger)
        print(f"[vigia_ballenas_bypass] pendientes={len(pendientes)} resueltos_este_ciclo={actualizados} "
              f"ledger_total={len(ledger)}")

    resueltos = [r for r in ledger.values() if r.get("resuelto") == "1"]
    n = len(resueltos)
    if n == 0:
        return 0
    aciertos = sum(1 for r in resueltos if r.get("acierto_dir") == "1")
    pnl_total = sum(float(r.get("pnl_neto_hipotetico_eur") or 0) for r in resueltos)
    print(f"[vigia_ballenas_bypass] n_resuelto={n} hit={aciertos}/{n} ({100*aciertos/n:.1f}%) "
          f"pnl_hipotetico_total={pnl_total:+.2f}€")

    if n < N_ALERTA:
        return 0
    try:
        latch = json.loads(LATCH_PATH.read_text()) if LATCH_PATH.exists() else {}
    except Exception:
        latch = {}
    if latch.get("n_en_ultimo_aviso") == n:
        return 0  # ya avisado para este n exacto, no repetir cada ciclo

    try:
        from shadow_digest import enviar_telegram
        msg = (f"🐋 vigia_ballenas_bypass: n={n} señales bloqueadas por veto_ballenas ya "
               f"resueltas (umbral n≥{N_ALERTA} alcanzado)\n"
               f"hit={aciertos}/{n} ({100*aciertos/n:.1f}%)  pnl_hipotético_total={pnl_total:+.2f}€\n"
               f"Suficiente para empezar a mirar si un bypass por conviction/edge propio "
               f"tendría sentido — ver data/shadow/ballenas_veto_bypass.csv")
        ok = enviar_telegram(msg)
        print(f"[vigia_ballenas_bypass] aviso n>={N_ALERTA} enviado (telegram={ok})")
    except Exception as e:
        print(f"[vigia_ballenas_bypass] no se pudo avisar: {type(e).__name__}: {e}")
    latch["n_en_ultimo_aviso"] = n
    LATCH_PATH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_ballenas_bypass] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
