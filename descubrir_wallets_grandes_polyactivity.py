#!/usr/bin/env python3
"""
descubrir_wallets_grandes_polyactivity.py — segunda conexión de
`polyactivity` (petición explícita Javi 29-Jul, ver
idea_conectar_polyactivity_a_todo_29jul en memoria: "hay que conectarlo a
todo aquello que nos pueda dar ventaja").

Detecta wallets con actividad grande (`categoria_whale=1`, umbral ya
fijado en `fetch_polymarket_activity_ws.py::WHALE_USD_MIN=1000` por
trade) en el firehose de HOY, y las cruza contra las bases ya conocidas
(`wallet_edge_score_por_activo_marco.json`, `smart_money_consensus.json`,
`wallet_especialistas_state.json`) para separar "ya la conocíamos" de
"wallet nueva con volumen real, nunca vista antes en nuestras fuentes
habituales" — mismo patrón que `wallet_especialistas_observer.py`
(marca NUEVAS desde la última corrida, sin perder el historial).

Ventaja sobre el descubrimiento actual (`descubrir_wallets_sospechosas.py`,
cron semanal vía `data-api.polymarket.com/activity`): `polyactivity` es
CASI EN TIEMPO REAL (websocket, no un cron semanal) y cubre volumen
agregado del DÍA, no una muestra puntual.

Solo lectura, no toca dinero ni ninguna decisión — genera
`data/shadow/wallets_grandes_polyactivity_state.json` con el estado
acumulado, para revisar en el barrido de "solo observacional"
(CLAUDE.md punto 16).

Cron sugerido: diario (mismo bloque 06:xx UTC que el resto de análisis).
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"

WALLET_SCORES = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
ESPECIALISTAS_STATE = DIR_SHADOW / "wallet_especialistas_state.json"
STATE_OUT = DIR_SHADOW / "wallets_grandes_polyactivity_state.json"

N_MIN_TRADES = 3       # ruido de un solo trade grande puntual no basta
USD_TOTAL_MIN = 2000.0  # volumen acumulado del día


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _wallets_conocidas() -> set:
    """Unión de todas las bases de wallets ya conocidas. smart_money_
    consensus.json NO tiene direcciones (solo agregados por activo,
    verificado 29-Jul) -- no se cruza contra esa fuente, solo contra las
    2 que sí listan wallets concretas."""
    conocidas = set()
    try:
        d = json.loads(WALLET_SCORES.read_text(encoding="utf-8"))
        conocidas |= {v["wallet"].lower() for v in d.values() if v.get("wallet")}
    except Exception:
        pass
    try:
        d = json.loads(ESPECIALISTAS_STATE.read_text(encoding="utf-8"))
        wallets_dict = d.get("wallets", {}) if isinstance(d, dict) else {}
        # Claves compuestas "wallet#activo#marco" -- quedarse con la wallet.
        conocidas |= {k.split("#", 1)[0].lower() for k in wallets_dict.keys()}
    except Exception:
        pass
    return conocidas


def _archivos_activity(dias: int = 1) -> list[Path]:
    hoy = datetime.now(timezone.utc)
    out = []
    for d in range(dias):
        fecha = (hoy - timedelta(days=d)).strftime("%Y-%m-%d")
        p = DIR_SHADOW / f"polymarket_activity_{fecha}.csv"
        if p.exists():
            out.append(p)
    return out


def agregar_grandes() -> dict:
    """wallet_lower -> {"n": int, "usd_total": float, "activos": set}"""
    agg = defaultdict(lambda: {"n": 0, "usd_total": 0.0, "activos": set()})
    for path in _archivos_activity():
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("categoria_whale") != "1":
                    continue
                w = (row.get("wallet") or "").lower()
                if not w:
                    continue
                try:
                    usd = float(row.get("usd_value") or 0)
                except (TypeError, ValueError):
                    continue
                a = agg[w]
                a["n"] += 1
                a["usd_total"] += usd
                if row.get("activo"):
                    a["activos"].add(row["activo"])
    return agg


def main() -> int:
    conocidas = _wallets_conocidas()
    _log(f"wallets ya conocidas en nuestras fuentes: {len(conocidas)}")

    agg = agregar_grandes()
    candidatas = {w: v for w, v in agg.items()
                  if v["n"] >= N_MIN_TRADES and v["usd_total"] >= USD_TOTAL_MIN}
    _log(f"wallets con actividad whale hoy (n>={N_MIN_TRADES}, "
         f"usd>={USD_TOTAL_MIN:.0f}): {len(candidatas)}")

    nuevas = {w: v for w, v in candidatas.items() if w not in conocidas}
    _log(f"de esas, NUEVAS (no en wallet_edge_score/smart_money/especialistas): {len(nuevas)}")

    try:
        estado_previo = json.loads(STATE_OUT.read_text(encoding="utf-8")) if STATE_OUT.exists() else {}
    except Exception:
        estado_previo = {}
    ya_vistas_antes = set(estado_previo.get("nuevas_detectadas", {}).keys())

    nuevas_hoy = {w: v for w, v in nuevas.items() if w not in ya_vistas_antes}
    _log(f"NUEVAS que no se habían visto en corridas anteriores: {len(nuevas_hoy)}")

    for w, v in sorted(nuevas_hoy.items(), key=lambda kv: -kv[1]["usd_total"])[:15]:
        _log(f"  {w}: n={v['n']} usd_total={v['usd_total']:.0f} activos={sorted(v['activos'])}")

    todas_nuevas = dict(estado_previo.get("nuevas_detectadas", {}))
    for w, v in nuevas.items():
        todas_nuevas[w] = {"n": v["n"], "usd_total": round(v["usd_total"], 2),
                            "activos": sorted(v["activos"]),
                            "primera_vez": todas_nuevas.get(w, {}).get("primera_vez",
                                            datetime.now(timezone.utc).isoformat(timespec="seconds"))}

    STATE_OUT.write_text(json.dumps({
        "actualizado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "n_candidatas_hoy": len(candidatas),
        "nuevas_detectadas": todas_nuevas,
    }, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
