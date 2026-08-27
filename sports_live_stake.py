"""sports_live_stake.py — Calculadora de stake y circuit breakers para
LIVE en sports. Mismo diseño núcleo que live_stake.py (cripto) y
weather_live_stake.py (weather, ya adaptado una vez) — 3 niveles de
circuit breaker, Kelly half con techos en cascada.

Simplificado a propósito (mínimo viable, CLAUDE.md decisión ladder):
sin ventanas horarias, sin overrides puntuales fecha-acotados (no hay
historial de incidentes todavía en sports), sin HRP/kelly_precio_gate
(requieren datos propios que sports aún no tiene con este mecanismo).
Se amplía más adelante con el mismo patrón ya probado si hace falta.

Circuit breaker, 3 niveles (mayor a menor prioridad):
  1. Bankroll mínimo absoluto -> apaga el switch.
  2. Freno diario: caída >=X% del bankroll desde el inicio del día UTC.
  3. Racha de pérdidas consecutivas -> para el día (firma de fallo
     sistemático, no varianza).

calcular_stake(): Kelly half sobre el edge de la señal, techos en
cascada (% bankroll, máximo absoluto de config), penalización de
inventario direccional (partidos/rondas pueden tardar minutos-horas en
resolver, así que acumular en la misma dirección SÍ concentra riesgo
correlacionado mientras están abiertas, igual que en weather).

Ledger PROPIO (data/sports/trades.csv) — nunca el de cripto.
"""

import csv
from datetime import datetime, timezone
from pathlib import Path

from sports_live_guard import CONFIG_PATH, SWITCH_PATH, _cargar_config

DIR_SPORTS_LIVE = Path("data/sports")
TRADES_CSV = DIR_SPORTS_LIVE / "trades.csv"

# Sin depósito todavía -- Javi decide el importe real antes de financiar la
# porción de sports. Placeholder explícito, NUNCA usar sin que
# config_live_sports.json::depositos tenga al menos un depósito real.
CAPITAL_OPERATIVO_INICIAL = 0.0


def _parse_ts(ts_str: str) -> datetime | None:
    if not ts_str:
        return None
    try:
        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return ts
    except Exception:
        return None


def _capital_total_depositado(config: dict | None = None) -> float:
    if config is None:
        config = _cargar_config()
    try:
        deps = config.get("depositos", [])
        if deps:
            return sum(float(d.get("eur", 0)) for d in deps)
    except Exception:
        pass
    return CAPITAL_OPERATIVO_INICIAL


def bankroll_actual(config: dict | None = None) -> float:
    """Capital de plan: total depositado + PnL de trades cerrados (ledger
    propio, no saldo on-chain -- misma limitación reconocida que weather:
    ampliar con un live_balance.py propio si el drift ledger-vs-real
    llega a importar aquí como importó en cripto)."""
    capital = _capital_total_depositado(config)
    if not TRADES_CSV.exists():
        return capital
    pnl = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") == "CLOSED":
                try:
                    pnl += float(row.get("pnl_neto_eur", 0) or 0)
                except ValueError:
                    pass
    return capital + pnl


def _ts_inicio_dia_utc() -> datetime:
    ahora = datetime.now(timezone.utc)
    return ahora.replace(hour=0, minute=0, second=0, microsecond=0)


def pnl_hoy() -> float:
    if not TRADES_CSV.exists():
        return 0.0
    ts_ini = _ts_inicio_dia_utc()
    pnl = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            ts = _parse_ts(row.get("close_timestamp") or row.get("timestamp_utc") or "")
            if ts is not None and ts >= ts_ini:
                try:
                    pnl += float(row.get("pnl_neto_eur", 0) or 0)
                except ValueError:
                    pass
    return pnl


def stakes_abiertos_total() -> float:
    if not TRADES_CSV.exists():
        return 0.0
    total = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "OPEN":
                continue
            try:
                total += float(row.get("stake_eur", 0) or 0)
            except ValueError:
                pass
    return total


def bankroll_inicio_dia() -> float:
    return bankroll_actual() - pnl_hoy()


def racha_perdidas_consecutivas() -> int:
    if not TRADES_CSV.exists():
        return 0
    ts_ini = _ts_inicio_dia_utc()
    cierres = []
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            ts = _parse_ts(row.get("close_timestamp") or "")
            if ts is None or ts < ts_ini:
                continue
            try:
                cierres.append((ts, float(row.get("pnl_neto_eur", 0) or 0)))
            except ValueError:
                pass
    racha = 0
    for _, pnl in sorted(cierres, reverse=True):
        if pnl < 0:
            racha += 1
        else:
            break
    return racha


def inventario_direccional_hoy() -> dict:
    """Posiciones OPEN de hoy por índice de outcome comprado (`direction`
    en trades.csv = mirror_idx, "0"/"1" -- ver sports_wallet_mirror_
    sniper.py, NUNCA "YES"/"NO" literal: sports no siempre es binario
    Yes/No, muchos mercados son "Equipo A vs Equipo B" y solo el índice
    generaliza). Concentración en el mismo índice es un proxy de riesgo
    correlacionado más débil que en cripto/weather (ahí Yes/No sí tiene
    un significado consistente cruzando mercados distintos; aquí el
    índice 0 en un partido no tiene por qué correlacionar con el índice
    0 de otro) -- pero sigue protegiendo el caso real más probable:
    varias posiciones abiertas en el MISMO índice dentro de mercados de
    la misma categoría/torneo en curso a la vez.

    27-Ago noche (/code-review, hallazgo real tras 'revisa que todo esté
    perfecto'): esta función comparaba contra "YES"/"NO" literal desde
    que se escribió, pero registrar_trade() nunca guarda esos strings --
    la penalización llevaba siendo un no-op silencioso desde el diseño
    original, nunca se había activado con datos reales (n=0 hasta hoy)."""
    if not TRADES_CSV.exists():
        return {"IDX0": 0, "IDX1": 0, "q_net": 0}
    n_0 = n_1 = 0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "OPEN":
                continue
            if row.get("direction") == "0":
                n_0 += 1
            elif row.get("direction") == "1":
                n_1 += 1
    return {"IDX0": n_0, "IDX1": n_1, "q_net": n_0 - n_1}


def _inventory_penalty(direction: str, inv: dict) -> float:
    q_net = inv.get("q_net", 0)
    if direction == "0" and q_net > 0:
        exceso = q_net
    elif direction == "1" and q_net < 0:
        exceso = abs(q_net)
    else:
        return 1.0
    return max(0.50, 1.0 - exceso * 0.20)


def freno_diario_pct_efectivo(bkr: float, riesgo: dict) -> float:
    """27-Ago (petición explícita Javi, tras verificar con bankroll real
    de 5€ que el freno diario fijo bloqueaba TODOS los trades desde el
    día 1): con un bankroll pequeño, un freno_diario_pct fijo (ej. 15%,
    pensado para los bankrolls de cripto) puede dar un margen diario en
    euros MENOR que el suelo del CLOB (1,05€) -- ninguna orden cabría
    nunca, en silencio (stake=0€ sin error visible).

    Se AUTO-AJUSTA: el % efectivo es el mayor entre el configurado y el
    que garantiza que el margen diario cubra al menos
    `margen_diario_minimo_trades` operaciones al suelo del CLOB. Con
    bankroll pequeño, el % sube (más laxo en términos relativos, pero
    el € de riesgo real sigue siendo pequeño en términos absolutos). En
    cuanto el bankroll crece con el PnL, el suelo en € se vuelve
    irrelevante frente al %, y se auto-estrecha de vuelta al valor base
    -- no hace falta acordarse de subir/bajar nada a mano."""
    cb = riesgo.get("circuit_breaker", {})
    freno_base = cb.get("freno_diario_pct", 0.15)
    min_stake = riesgo.get("min_stake_eur", 1.05)
    n_trades_min = cb.get("margen_diario_minimo_trades", 2)
    if bkr <= 0:
        return freno_base
    pct_minimo_por_suelo = (n_trades_min * min_stake) / bkr
    return max(freno_base, pct_minimo_por_suelo)


def verificar_circuit_breaker() -> tuple[bool, str]:
    """Tres niveles de freno. Devuelve (disparado, motivo)."""
    config = _cargar_config()
    riesgo = config.get("riesgo", {})
    cb = riesgo.get("circuit_breaker", {})
    bkr = bankroll_actual(config)
    bkr_min = cb.get("bankroll_minimo_eur", 1.0)

    if bkr <= bkr_min:
        if SWITCH_PATH.exists():
            SWITCH_PATH.unlink()
        return True, f"🛑 bankroll {bkr:.2f}€ <= mínimo {bkr_min:.2f}€ -- switch desactivado"

    freno_dia_pct = freno_diario_pct_efectivo(bkr, riesgo)
    bkr_ini_dia = bankroll_inicio_dia()
    if bkr_ini_dia > 0:
        caida_dia = (bkr_ini_dia - bkr) / bkr_ini_dia
        if caida_dia >= freno_dia_pct:
            return True, (f"🛑 caída diaria {caida_dia*100:.1f}% "
                          f"({bkr_ini_dia:.2f}€ -> {bkr:.2f}€) >= freno {freno_dia_pct*100:.0f}%")

    max_racha = cb.get("max_perdidas_consecutivas", 3)
    if max_racha:
        racha = racha_perdidas_consecutivas()
        if racha >= max_racha:
            return True, (f"🛑 {racha} pérdidas live consecutivas >= {max_racha} "
                          f"-- racha sistemática, para el día")

    return False, f"✅ OK  (bkr={bkr:.2f}€  pnl_día={pnl_hoy():+.2f}€)"


def bloquear_por_circuit_breaker(log_fn) -> bool:
    disparado, motivo = verificar_circuit_breaker()
    if disparado:
        log_fn(motivo)
    return disparado


def calcular_stake(edge: float, categoria: str = "", tipo: str = "",
                    direction: str = "") -> dict:
    """Stake para una señal con edge dado (fracción, ej. 0.05 = 5pp sobre
    breakeven). Kelly half + techos en cascada + penalización de
    inventario direccional. Suelo CLOB 1.05€ (igual que cripto/weather,
    mismo exchange -- min size 1$)."""
    config = _cargar_config()
    riesgo = config.get("riesgo", {})
    bkr = bankroll_actual(config)
    half_kelly = riesgo.get("half_kelly", True)
    max_pct = riesgo.get("max_pct_bankroll_por_trade", 0.10)
    min_stake = riesgo.get("min_stake_eur", 1.05)
    max_stake = riesgo.get("max_stake_eur", 2.00)

    techo_kelly = bkr * abs(edge) * (0.5 if half_kelly else 1.0)
    techo_pct = bkr * max_pct

    stake = min(techo_kelly, techo_pct, max_stake)
    stake = max(stake, min_stake) if bkr >= min_stake else 0.0

    inv_str = ""
    if direction:
        inv = inventario_direccional_hoy()
        inv_factor = _inventory_penalty(direction, inv)
        if inv_factor < 1.0:
            stake = max(min_stake, stake * inv_factor)
            inv_str = (f" | inv_penalty×{inv_factor:.2f} "
                       f"(q_net={inv['q_net']:+d} YES={inv['YES']} NO={inv['NO']})")

    freno_str = ""
    freno_dia_pct = freno_diario_pct_efectivo(bkr, riesgo)
    bkr_min = riesgo.get("circuit_breaker", {}).get("bankroll_minimo_eur", 1.0)
    bkr_ini_dia = bankroll_inicio_dia()
    abiertos = stakes_abiertos_total()
    if bkr_ini_dia > 0:
        margen_freno = bkr_ini_dia * freno_dia_pct + pnl_hoy() - abiertos
        margen_suelo = bkr - bkr_min - abiertos
        margen_dia = min(margen_freno, margen_suelo)
        if stake > margen_dia:
            stake = max(0.0, margen_dia)
            if stake < min_stake:
                stake = 0.0
            freno_str = (f" | techo_freno_diario={margen_dia:.2f}€ "
                        f"(freno={freno_dia_pct*100:.0f}% de {bkr_ini_dia:.2f}€, "
                        f"abiertos={abiertos:.2f}€)")

    motivo = (f"bankroll={bkr:.2f}€ | Kelly={techo_kelly:.2f}€ max{max_pct*100:.0f}%={techo_pct:.2f}€ "
              f"máx={max_stake:.2f}€{inv_str}{freno_str} -> stake={stake:.2f}€")

    return {
        "stake_eur": round(stake, 2),
        "bankroll": round(bkr, 2),
        "motivo": motivo,
        "viable": stake >= min_stake,
    }


if __name__ == "__main__":
    config = _cargar_config()
    bkr = bankroll_actual(config)
    pnl_h = pnl_hoy()
    cb, motivo_cb = verificar_circuit_breaker()

    print(f"Bankroll actual sports: {bkr:.2f}€")
    print(f"PNL hoy:                {pnl_h:+.2f}€")
    print(f"Circuit breaker:        {'🛑 DISPARADO -- ' + motivo_cb if cb else '✅ OK'}")
    print()
    print("Simulación de stakes:")
    for edge in [0.05, 0.10, 0.15]:
        r = calcular_stake(edge)
        print(f"  edge={edge:+.2f} -> {r['stake_eur']:.2f}€  |  {r['motivo']}")
