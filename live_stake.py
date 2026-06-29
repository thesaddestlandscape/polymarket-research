"""
live_stake.py — Calculadora de stake con capital distribuido por ventana.

Lógica de capital:
  - Bankroll total = 20€ inicial + PNL acumulado de trades cerrados
  - Cada día se divide el bankroll entre las ventanas del día
  - Las ganancias/pérdidas resueltas se redistribuyen en tiempo real:
      capital_disponible = bankroll_actual
      ventanas_restantes = ventanas que quedan hoy (incluida la actual)
      budget_esta_ventana = capital_disponible / ventanas_restantes

  Ejemplo con bankroll=20€ y 6 ventanas:
    Ventana 1: 20/6 = 3.33€ — gana 1€ → bankroll=21€
    Ventana 2: 21/5 = 4.20€ — pierde 2€ → bankroll=19€
    Ventana 3: 19/4 = 4.75€
    ...

  Si en una ventana el bot GASTA todo su presupuesto → freno hasta la siguiente.
  No espera a que los trades se resuelvan — el freno es por capital DESPLEGADO.

Freno adicional (diario):
  Si el bankroll cae por debajo del umbral mínimo → desactiva el switch.
"""

import csv
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

DIR_LIVE              = Path("data/live")
CONFIG_PATH           = DIR_LIVE / "config_live.json"
TRADES_CSV            = DIR_LIVE / "trades.csv"
SWITCH_PATH           = DIR_LIVE / "LIVE_MODE_ON"

CAPITAL_OPERATIVO_INICIAL = 25.44  # depósito real 2026-06-29


def _cargar_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def _hoy_madrid(config: dict) -> str:
    offset = config.get("utc_offset_verano", 2)
    return (datetime.now(timezone.utc) + timedelta(hours=offset)).strftime("%Y-%m-%d")


def _ahora_madrid(config: dict) -> datetime:
    offset = config.get("utc_offset_verano", 2)
    return datetime.now(timezone.utc) + timedelta(hours=offset)


# ── Bankroll ──────────────────────────────────────────────────────────────────

def bankroll_actual() -> float:
    """Capital total = inicial + PNL de todos los trades cerrados."""
    if not TRADES_CSV.exists():
        return CAPITAL_OPERATIVO_INICIAL
    pnl = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") == "CLOSED":
                try:
                    pnl += float(row.get("pnl_neto_eur", 0) or 0)
                except ValueError:
                    pass
    return CAPITAL_OPERATIVO_INICIAL + pnl


# ── Ventanas ──────────────────────────────────────────────────────────────────

def _ventanas_hoy(config: dict) -> list:
    ahora = _ahora_madrid(config)
    dia   = ahora.weekday()  # 0=lunes…6=domingo
    if dia < 5:
        return config.get("ventanas_lunes_viernes", [])
    return []  # fin de semana: sin ventanas automáticas


def _ventana_actual(config: dict) -> dict | None:
    """Devuelve la ventana en la que estamos ahora, o None."""
    ahora = _ahora_madrid(config).time()
    for v in _ventanas_hoy(config):
        try:
            h_ini = datetime.strptime(v["inicio"], "%H:%M").time()
            h_fin = datetime.strptime(v["fin"],    "%H:%M").time()
            if h_ini <= ahora <= h_fin:
                return v
        except Exception:
            continue
    return None


def ventanas_restantes_hoy(config: dict) -> int:
    """Número de ventanas que quedan hoy (incluida la actual si estamos en una)."""
    ahora = _ahora_madrid(config).time()
    restantes = 0
    for v in _ventanas_hoy(config):
        try:
            h_fin = datetime.strptime(v["fin"], "%H:%M").time()
            if h_fin >= ahora:
                restantes += 1
        except Exception:
            continue
    return max(restantes, 1)  # nunca 0 para evitar división por cero


# ── Stakes por ventana ────────────────────────────────────────────────────────

def _ts_inicio_ventana_utc(v: dict, config: dict) -> datetime:
    """Timestamp UTC del inicio de la ventana de hoy."""
    offset  = config.get("utc_offset_verano", 2)
    ahora_m = _ahora_madrid(config)
    h_ini   = datetime.strptime(v["inicio"], "%H:%M").time()
    inicio_madrid = ahora_m.replace(hour=h_ini.hour, minute=h_ini.minute,
                                    second=0, microsecond=0)
    return inicio_madrid - timedelta(hours=offset)


def stakes_desplegados_ventana_actual() -> float:
    """
    Suma de stakes colocados en la ventana horaria actual (trades OPEN o STUB).
    Este es el 'capital en juego' de la ventana — el freno se basa en esto.
    """
    if not TRADES_CSV.exists():
        return 0.0
    config = _cargar_config()
    v      = _ventana_actual(config)
    if v is None:
        return 0.0

    ts_ini = _ts_inicio_ventana_utc(v, config)
    total  = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") not in ("OPEN", "STUB"):
                continue
            ts_str = row.get("timestamp_utc") or ""
            try:
                ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
                if ts >= ts_ini:
                    total += float(row.get("stake_eur", 0) or 0)
            except Exception:
                pass
    return total


def pnl_live_hoy() -> float:
    """PNL neto de trades cerrados hoy."""
    if not TRADES_CSV.exists():
        return 0.0
    config    = _cargar_config()
    hoy       = _hoy_madrid(config)
    pnl       = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            fecha = (row.get("close_timestamp") or row.get("timestamp_utc") or "")[:10]
            if fecha == hoy:
                try:
                    pnl += float(row.get("pnl_neto_eur", 0) or 0)
                except ValueError:
                    pass
    return pnl


# ── Circuit breaker ───────────────────────────────────────────────────────────

def bankroll_inicio_dia() -> float:
    """Bankroll al inicio del día de hoy (antes de cualquier trade de hoy)."""
    bkr_ahora = bankroll_actual()
    pnl_hoy   = pnl_live_hoy()
    return bkr_ahora - pnl_hoy


def pnl_live_ventana_actual() -> float:
    """PNL neto de trades cerrados en la ventana horaria actual."""
    if not TRADES_CSV.exists():
        return 0.0
    config = _cargar_config()
    v = _ventana_actual(config)
    if v is None:
        return 0.0
    ts_ini = _ts_inicio_ventana_utc(v, config)
    pnl = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            ts_str = row.get("close_timestamp") or row.get("timestamp_utc") or ""
            try:
                ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
                if ts >= ts_ini:
                    pnl += float(row.get("pnl_neto_eur", 0) or 0)
            except Exception:
                pass
    return pnl


def verificar_circuit_breaker() -> tuple[bool, str]:
    """
    Tres niveles de freno (de mayor a menor prioridad):

      1. Bankroll mínimo absoluto (5€): apaga el switch, avisa al usuario.
      2. Freno diario (-15%): si el bankroll cayó 15% desde inicio del día → para hoy.
      3. Freno por ventana (-20%): si en esta ventana se ha perdido 20% del bankroll
         del inicio de la ventana → para esta ventana.

    Devuelve (disparado, motivo).
    """
    config  = _cargar_config()
    cb      = config.get("riesgo", {}).get("circuit_breaker", {})
    bkr     = bankroll_actual()
    bkr_min = cb.get("bankroll_minimo_eur", 5.0)

    # Freno 1 — bankroll mínimo absoluto
    if bkr <= bkr_min:
        if SWITCH_PATH.exists():
            SWITCH_PATH.unlink()
        return True, f"🛑 bankroll {bkr:.2f}€ ≤ mínimo {bkr_min:.2f}€ — switch desactivado"

    # Freno 2 — caída diaria
    freno_dia_pct = cb.get("freno_diario_pct", 0.15)
    bkr_ini_dia   = bankroll_inicio_dia()
    if bkr_ini_dia > 0:
        caida_dia = (bkr_ini_dia - bkr) / bkr_ini_dia
        if caida_dia >= freno_dia_pct:
            return True, (f"🛑 caída diaria {caida_dia*100:.1f}% "
                          f"({bkr_ini_dia:.2f}€ → {bkr:.2f}€) ≥ freno {freno_dia_pct*100:.0f}%")

    # Freno 3 — caída en ventana actual
    freno_v_pct = cb.get("freno_ventana_pct", 0.20)
    v = _ventana_actual(config)
    if v:
        pnl_v       = pnl_live_ventana_actual()
        desp        = stakes_desplegados_ventana_actual()
        bkr_ini_v   = bkr - pnl_v           # bankroll al inicio de esta ventana
        if bkr_ini_v > 0 and pnl_v < 0:
            caida_v = abs(pnl_v) / bkr_ini_v
            if caida_v >= freno_v_pct:
                return True, (f"🛑 caída en ventana '{v.get('nombre','')}' "
                               f"{caida_v*100:.1f}% ({pnl_v:.2f}€) ≥ freno {freno_v_pct*100:.0f}%")

    return False, f"✅ OK  (bkr={bkr:.2f}€  pnl_día={pnl_live_hoy():+.2f}€)"


# ── Calcular stake ────────────────────────────────────────────────────────────

def calcular_stake(ic: float, strategy: str = "", subtype: str = "") -> dict:
    """
    Stake para una señal con IC dado.
    Opera con el bankroll completo en cada ventana (compounding natural).

    Techos en cascada:
      1. Kelly half: IC × bankroll × 0.5
      2. Máx 10% del bankroll por trade (nunca más de 2€ con bankroll=20€)
      3. Máximo absoluto del config (2€)
    """
    config     = _cargar_config()
    riesgo     = config.get("riesgo", {})
    bkr        = bankroll_actual()
    half_kelly = riesgo.get("half_kelly", True)
    max_pct    = riesgo.get("max_pct_bankroll_por_trade", 0.10)
    min_stake  = riesgo.get("min_stake_eur", 0.25)
    max_stake  = riesgo.get("max_stake_eur", 2.00)

    techo_kelly  = bkr * abs(ic) * (0.5 if half_kelly else 1.0)
    techo_pct    = bkr * max_pct
    techo_config = max_stake

    stake = min(techo_kelly, techo_pct, techo_config)
    stake = max(stake, min_stake) if bkr >= min_stake else 0.0

    motivo = (
        f"bankroll={bkr:.2f}€ | "
        f"Kelly={techo_kelly:.2f}€  max10%={techo_pct:.2f}€  máx={techo_config:.2f}€ "
        f"→ stake={stake:.2f}€"
    )

    return {
        "stake_eur":  round(stake, 2),
        "bankroll":   round(bkr, 2),
        "motivo":     motivo,
        "viable":     stake >= min_stake,
    }


# ── CLI de diagnóstico ────────────────────────────────────────────────────────

if __name__ == "__main__":
    config = _cargar_config()
    bkr    = bankroll_actual()
    n_rest = ventanas_restantes_hoy(config)
    desp   = stakes_desplegados_ventana_actual()
    pnl_h  = pnl_live_hoy()
    v      = _ventana_actual(config)
    cb, motivo_cb = verificar_circuit_breaker()

    print(f"Bankroll actual:       {bkr:.2f}€")
    print(f"PNL hoy:               {pnl_h:+.2f}€")
    print(f"Ventana actual:        {v['nombre'] if v else 'fuera de ventana'}")
    print(f"Ventanas restantes:    {n_rest}")
    print(f"Budget esta ventana:   {bkr/n_rest:.2f}€")
    print(f"Ya desplegado:         {desp:.2f}€")
    print(f"Restante ventana:      {max(0, bkr/n_rest - desp):.2f}€")
    print(f"Circuit breaker:       {'🛑 DISPARADO — ' + motivo_cb if cb else '✅ OK'}")
    print()
    print("Simulación de stakes:")
    for ic in [0.08, 0.10, 0.15, 0.22]:
        r = calcular_stake(ic)
        print(f"  IC={ic:+.2f} → {r['stake_eur']:.2f}€  |  {r['motivo']}")
