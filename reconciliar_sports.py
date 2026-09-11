"""
reconciliar_sports.py — Guardia diaria de reconciliación wallet real ↔
ledger de sports (data/sports/trades.csv), mismo mecanismo que
reconciliar.py (cripto, 08-Jul) pero adaptado a que sports NO tiene su
propia wallet on-chain -- comparte una con cripto.

27-Ago noche (petición explícita Javi: "algo que le pueda faltar para
ser 100% óptimo" -> reconciliación priorizada): sin esto, un drift en el
ledger de sports (un fill no capturado, una resolución mal calculada) no
solo corrompe los números de sports -- corrompe TAMBIÉN el bankroll de
cripto, porque live_stake.py resta el bankroll de sports (calculado por
su propio ledger) del saldo real de la wallet compartida para obtener el
bankroll operativo de cripto. Si el ledger de sports miente, cripto
también sizea mal sin saberlo.

Mecánica (por diferencia, único camino posible sin wallet propia de
sports): total_bruto (wallet completa, sin restar sports -- ver
live_balance.py::fetch_balance_real(), 27-Ago) menos lo que el ledger de
CRIPTO dice que debería haber (reusa modelo_trades() de reconciliar.py,
misma fuente de verdad) = lo que la wallet real "cree" que tiene sports.
Comparado contra lo que el propio ledger de sports dice que tiene
(sports_live_stake.bankroll_actual()) -- la diferencia es el tracking
error de sports.

Cron: después de reconciliar.py (cripto) y de live_balance.py, mismo
bloque 05:5x UTC.

⚠️ Nota real de la primera corrida (27-Ago): TE baseline = +2,55€, NO es
un problema de sports -- es el TE propio y ya conocido de CRIPTO (7 filas
`status=ERROR` en trades.csv de cripto, nunca contadas en su modelo, ver
`reconciliar.py` cripto que muestra el MISMO +2,55€ para su propio TE).
Como este script deriva "lo que le queda a sports" restando el modelo de
CRIPTO del total bruto, cualquier drift ya existente del lado cripto se
cuela como ruido en la lectura absoluta de sports. Por diseño (no se
puede evitar sin una wallet propia de sports) -- lo que SÍ importa es el
`delta_dia`, no el TE absoluto: un salto día a día es la señal real de
un problema NUEVO específico de sports, la baseline heredada de cripto
es constante y no dispara alertas por sí sola."""
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DIR_LIVE = REPO / "data" / "live"
DIR_SPORTS = REPO / "data" / "sports"
HIST_PATH = DIR_SPORTS / "reconciliacion.csv"

UMBRAL_DELTA_DIA = 0.75  # € de deriva del TE en un día que dispara alerta
MAX_EDAD_SNAPSHOT_S = 3600

from dotenv import load_dotenv
load_dotenv(DIR_LIVE / ".env")

from shadow_digest import enviar_telegram  # noqa: E402
from reconciliar import modelo_trades as _modelo_trades_cripto  # noqa: E402


def _cargar_historial() -> list[dict]:
    if not HIST_PATH.exists():
        return []
    with open(HIST_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _guardar_historial(filas: list[dict]) -> None:
    campos = ["date", "ts", "sports_implicado_wallet", "sports_modelo",
              "tracking_error", "delta_dia", "alerta"]
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
    if not snap or snap.get("_rancio") or "total_bruto" not in snap:
        msg = ("🔎 *RECONCILIACIÓN wallet↔sports*\n"
               "⚠️ Sin snapshot on-chain fresco o sin `total_bruto` (cache viejo, "
               "se refresca solo en el próximo ciclo de live_balance.py) -- "
               "no puedo medir el tracking error de sports hoy.")
        print(f"[reconciliar_sports] {hoy} SIN SNAPSHOT ÚTIL")
        enviar_telegram(msg, bot="sports")
        return 1

    import sports_live_stake as _sls
    sports_modelo = _sls.bankroll_actual()

    pnl_cripto, _n_error_cripto = _modelo_trades_cripto()
    try:
        cfg_cripto = __import__("json").loads((DIR_LIVE / "config_live.json").read_text(encoding="utf-8"))
        depositos_cripto = cfg_cripto.get("depositos", [])
        deposito_cripto = sum(float(d["eur"]) for d in depositos_cripto) if depositos_cripto else 0.0
    except Exception:
        deposito_cripto = 0.0
    modelo_cripto = deposito_cripto + pnl_cripto

    sports_implicado_wallet = snap["total_bruto"] - modelo_cripto
    te = sports_implicado_wallet - sports_modelo

    filas = [f for f in _cargar_historial() if f["date"] != hoy]
    prev = filas[-1] if filas else None
    delta = te - float(prev["tracking_error"]) if prev else None

    alerta = delta is not None and abs(delta) > UMBRAL_DELTA_DIA
    filas.append({
        "date": hoy,
        "ts": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sports_implicado_wallet": f"{sports_implicado_wallet:.4f}",
        "sports_modelo": f"{sports_modelo:.4f}",
        "tracking_error": f"{te:.4f}",
        "delta_dia": f"{delta:.4f}" if delta is not None else "",
        "alerta": "1" if alerta else "0",
    })
    _guardar_historial(filas)

    delta_str = f"{delta:+.2f}€" if delta is not None else "baseline"
    print(f"[reconciliar_sports] {hoy} implicado_wallet={sports_implicado_wallet:.2f}€ "
          f"modelo={sports_modelo:.2f}€ TE={te:+.2f}€ delta_dia={delta_str}"
          f"{' ⚠️ ALERTA' if alerta else ''}")

    if alerta:
        sentido = ("el ledger de sports cree tener MENOS de lo que la wallet real implica "
                   "(trade real no registrado, o resolución con PnL mal calculado)" if delta < 0 else
                   "el ledger de sports cree tener MÁS de lo que la wallet real implica "
                   "(posible doble conteo o trade fantasma)")
        enviar_telegram(
            "🔎 *RECONCILIACIÓN wallet↔sports*\n"
            f"⚠️ El tracking error de sports se movió *{delta:+.2f}€* en un día "
            f"(umbral {UMBRAL_DELTA_DIA:.2f}€).\n"
            f"TE: {float(prev['tracking_error']):+.2f}€ → {te:+.2f}€\n"
            f"Implícito en wallet: {sports_implicado_wallet:.2f}€ vs modelo ledger: {sports_modelo:.2f}€\n\n"
            f"Lectura: {sentido}.\n"
            "⚠️ Esto también puede significar que el bankroll de CRIPTO está mal "
            "calculado (descuenta el bankroll de sports del saldo compartido) -- revisar.",
            bot="sports",
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
