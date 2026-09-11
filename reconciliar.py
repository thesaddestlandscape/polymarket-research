"""
reconciliar.py — Guardia diaria de reconciliación wallet real ↔ modelo (trades.csv).

Mejora #1 del plan de loops (aprobada por Javi 07-Jul, implementada 08-Jul).

El tracking error (TE) = balance real on-chain − balance según trades.csv no es
un dato contable: es MÉTRICA DE TRADING. Si su deriva diaria acelera, los fills
están empeorando (selección adversa creciendo) y hay que recortar stake antes
de que el PnL lo haga evidente.

Determinista y read-only sobre el sistema: no toca órdenes, config ni frenos.
Escribe solo su historial (data/live/reconciliacion.csv) y avisa por Telegram si:
  - |Δ TE| entre días supera UMBRAL_DELTA_DIA, o
  - no hay snapshot on-chain fresco (fail-loud: guardia que no puede medir, avisa).

Cron: 50 5 * * * (tras el ciclo de live_balance.py de las 05:45 UTC).
Idempotente: re-ejecutar el mismo día reescribe la fila del día, no duplica.
"""
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent
DIR_LIVE = BASE / "data" / "live"
TRADES_PATH = DIR_LIVE / "trades.csv"
HIST_PATH = DIR_LIVE / "reconciliacion.csv"

UMBRAL_DELTA_DIA = 0.75  # $ de deriva del TE en un día que dispara alerta
MAX_EDAD_SNAPSHOT_S = 3600

# Credenciales antes de importar shadow_digest (lee TELEGRAM_* al importarse).
from dotenv import load_dotenv
load_dotenv(DIR_LIVE / ".env")

from shadow_digest import enviar_telegram  # noqa: E402


def modelo_trades() -> tuple[float, int]:
    """PnL neto de trades CLOSED según trades.csv y nº de filas ERROR.

    Posiciones OPEN se valoran a coste (el stake salió del wallet pero la
    posición vale ~stake): no entran en el modelo y meten solo ruido
    transitorio mark-to-market en el TE mientras están abiertas.
    """
    if not TRADES_PATH.exists():
        return 0.0, 0
    pnl = 0.0
    errores = 0
    with open(TRADES_PATH, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            st = r.get("status", "")
            if st == "CLOSED":
                pnl += float(r.get("pnl_neto_eur") or 0)
            elif st == "ERROR":
                errores += 1
    return pnl, errores


def cargar_historial() -> list[dict]:
    if not HIST_PATH.exists():
        return []
    with open(HIST_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def guardar_historial(filas: list[dict]):
    campos = ["date", "ts", "total_real", "modelo", "tracking_error",
              "delta_dia", "alerta"]
    tmp = HIST_PATH.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)
    tmp.replace(HIST_PATH)


def main() -> int:
    ahora = datetime.now(timezone.utc)
    hoy = ahora.strftime("%Y-%m-%d")

    from live_balance import cargar_balance_real
    snap = cargar_balance_real(max_edad_s=MAX_EDAD_SNAPSHOT_S)
    if not snap or snap.get("_rancio"):
        msg = ("🔎 *RECONCILIACIÓN wallet↔modelo*\n"
               "⚠️ Sin snapshot on-chain fresco (live_balance.py, cron 15min) — "
               "no puedo medir el tracking error hoy. Revisar logs/balance.log.")
        print(f"[reconciliar] {hoy} SIN SNAPSHOT FRESCO — alerta enviada")
        enviar_telegram(msg)
        return 1

    pnl_modelo, n_error = modelo_trades()
    modelo = snap["deposito_inicial"] + pnl_modelo
    te = snap["total"] - modelo

    filas = [f for f in cargar_historial() if f["date"] != hoy]  # idempotencia
    prev = filas[-1] if filas else None
    delta = te - float(prev["tracking_error"]) if prev else None

    alerta = delta is not None and abs(delta) > UMBRAL_DELTA_DIA
    filas.append({
        "date": hoy,
        "ts": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_real": f"{snap['total']:.4f}",
        "modelo": f"{modelo:.4f}",
        "tracking_error": f"{te:.4f}",
        "delta_dia": f"{delta:.4f}" if delta is not None else "",
        "alerta": "1" if alerta else "0",
    })
    guardar_historial(filas)

    delta_str = f"{delta:+.2f}$" if delta is not None else "baseline"
    print(f"[reconciliar] {hoy} real={snap['total']:.2f}$ modelo={modelo:.2f}$ "
          f"TE={te:+.2f}$ delta_dia={delta_str} errores_trades={n_error}"
          f"{' ⚠️ ALERTA' if alerta else ''}")

    if alerta:
        sentido = ("los fills están dejando MENOS dinero del que el modelo cree "
                   "(selección adversa/slippage creciendo)" if delta < 0 else
                   "aparece dinero que el modelo no explica (posible trade sin "
                   "registrar o error de contabilidad)")
        enviar_telegram(
            "🔎 *RECONCILIACIÓN wallet↔modelo*\n"
            f"⚠️ El tracking error se movió *{delta:+.2f}$* en un día "
            f"(umbral {UMBRAL_DELTA_DIA:.2f}$).\n"
            f"TE: {float(prev['tracking_error']):+.2f}$ → {te:+.2f}$\n"
            f"Real {snap['total']:.2f}$ vs modelo {modelo:.2f}$\n\n"
            f"Lectura: {sentido}.\n"
            "Antes de subir stake: revisar libro\\_snapshots.csv y slip\\_real."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
