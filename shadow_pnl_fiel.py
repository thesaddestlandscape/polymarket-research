"""
shadow_pnl_fiel.py — PnL "fiel" nocional, por estrategia, para TODAS las
tuplas strategy#subtype#direction del shadow (no solo las 8 en
pares_permitidos_live).

Petición explícita de Javi (21-Jul noche, ver memoria nativa
project_shadow_fiel_a_live_pendiente_22jul): "el shadow tiene que ser como
el live pero para las estrategias, hipótesis y tuplas que no operan en
live". El "PnL fiel" que ya existe en dashboard_server.py::_pnl_realista()
usa stake fijo $1 + slippage constante — sigue siendo una cota superior.
Este script reconstruye, señal a señal y en orden cronológico, qué le
habría pasado a un bankroll nocional INDEPENDIENTE por tupla si operase con
las mismas reglas que live: fill-ability real (libro_snapshots.csv), stake
real (misma cascada Kelly que live_stake.calcular_stake), y los mismos
circuit breakers/frenos (freno diario, racha, freno ventana, suelo).

NO toca shadow_predict.py / shadow_resolve.py / live_trade.py / live_stake.py
— es una capa de post-proceso de solo lectura sobre datos ya existentes.

Decisiones de diseño acordadas con Javi (22-Jul):
  - Señal sin snapshot de libro capturado → EXCLUIDA del PnL fiel (nunca se
    rellena con una estimación poblacional por arquetipo).
  - El bankroll nocional por estrategia SÍ simula los circuit breakers
    (freno diario/ventana, racha, suelo), no solo fill-ability+stake+fees.

Limitaciones documentadas (no ocultas):
  - El IC usado para el stake Kelly es el ACTUAL de strategy_params.json,
    no un snapshot histórico punto-en-el-tiempo (no existe ese historial).
  - Los overrides puntuales con fecha de circuit_breaker (freno_diario_pct_
    override, bankroll_minimo_eur_override, etc. — casi todos ya expirados)
    se ignoran a propósito: aplicar "hoy" el override real de una fecha
    pasada concreta sería sesgar la simulación histórica con una excepción
    de un solo día pensada para otro contexto. Se usa siempre el valor base.
  - No se replica la penalización por inventario direccional (posiciones
    abiertas simultáneas en la misma dirección) — el bankroll nocional de
    cada tupla es independiente y no compite por inventario con nadie.
  - mejor_ask del libro puede desviarse mucho de precio_plan en algunas
    filas capturadas (dato real observado, no un bug de este script) — se
    usa tal cual (es lo que live habría pagado) pero se cuenta aparte
    (n_precio_sospechoso) para que la desviación sea visible, no silenciosa.
  - No se replican los vetos de ejecución de live_trade.py: veto CLV
    (clv_medio<0 en ventana 7d), veto de discrepancia entre tuplas
    whitelisted (otra tupla predice la dirección opuesta hoy),
    streak_cooldown_factor (reduce IC tras 2 derrotas seguidas 2h) ni
    abort_requote/fok_kill en el momento exacto de ejecutar. Validado 22-Jul
    contra las 8 tuplas ya-live acotando por fecha real de promoción +
    excluyendo el corte real de switch OFF (17→21-Jul): el AGREGADO de las
    8 sale del mismo signo y orden de magnitud que trades.csv real
    (nocional -0.80€ n=112 vs real -1.28€ n=71), pero el desglose POR TUPLA
    individual puede tener signo distinto al real cuando n es bajo (2/8
    cambiaron de signo: FAVORITO_CONFIRMADO#ETH#15min#BUY_YES y
    GBM_LATE_15M#ETH#15min#BUY_YES) — los vetos no modelados de arriba son
    la explicación más probable. Tratar el número por tupla individual como
    orientativo, no concluyente, hasta que se añadan esos vetos.
"""

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Misma constante que live_trade.py:43 (FEE_RATE_TAKER_CRYPTO). Duplicada a
# propósito en vez de importada: live_trade.py importa live_guard/live_stake/
# shadow_digest/live_balance/smart_money_tracker (credenciales, Telegram,
# requests) solo para definir esta constante — demasiado acoplamiento para
# un script de solo lectura. Si live_trade.py cambia este valor, sincronizar
# a mano (verificado 22-Jul: 0.07, validado contra fees on-chain reales).
FEE_RATE_TAKER_CRYPTO = 0.07

PRECIO_SOSPECHOSO_DELTA = 0.15  # |mejor_ask - precio_plan| por encima de esto se marca, no se excluye


def parse_ts(s: str):
    if not s:
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def madrid_dt(ts_utc: datetime, config: dict) -> datetime:
    offset_h = config.get("utc_offset_verano", 2)
    return ts_utc + timedelta(hours=offset_h)


def ventana_en(ts_utc: datetime, config: dict):
    """Nombre de la ventana operativa para un timestamp UTC HISTÓRICO dado
    (no usa datetime.now() como live_guard.en_ventana_horaria). Misma lógica
    exacta: día de semana + rango HH:MM contra ventanas_lunes_viernes /
    ventanas_fin_de_semana del config_live.json real."""
    md = madrid_dt(ts_utc, config)
    dow = md.weekday()
    hora = md.time()

    if dow >= 5:
        modo_fds = config.get("fines_de_semana", "solo_manual")
        if modo_fds == "off":
            return None
        if modo_fds == "solo_manual":
            return "fin_de_semana_manual"
        ventanas = config.get("ventanas_fin_de_semana", [])
    else:
        ventanas = config.get("ventanas_lunes_viernes", [])

    for v in ventanas:
        try:
            h_ini = datetime.strptime(v["inicio"], "%H:%M").time()
            h_fin = datetime.strptime(v["fin"], "%H:%M").time()
            if h_ini <= hora <= h_fin:
                return v.get("nombre", "ventana")
        except Exception:
            continue
    return None


def cargar_config(root: Path) -> dict:
    p = root / "data" / "live" / "config_live.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def cargar_params(root: Path) -> dict:
    p = root / "data" / "shadow" / "strategy_params.json"
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def ic_para(strategy: str, subtype: str, decision: str, params: dict):
    """IC actual (no histórico punto-en-el-tiempo, ver limitación en el
    docstring del módulo) para strategy#subtype#decision. Cascada: entrada
    específica strategy#subtype primero, agregado strategy si no existe;
    dentro de cada una, IC direccional (ic_BUY_YES/ic_BUY_NO) si está
    presente, si no ic_bayes agregado."""
    est = params.get("estrategias", {})
    campo_dir = f"ic_{decision}"
    for key in (f"{strategy}#{subtype}", strategy):
        entry = est.get(key)
        if not entry:
            continue
        if entry.get(campo_dir) is not None:
            return entry[campo_dir]
        if entry.get("ic_bayes") is not None:
            return entry["ic_bayes"]
    return None


def construir_indice_libro(root: Path) -> dict:
    """(market_id, direction) -> fila de libro_snapshots.csv, prefiriendo
    motivo='ejecutada' (fill real) > 'candidato_evaluacion' > 'fuera_ventana'."""
    prioridad = {"ejecutada": 0, "candidato_evaluacion": 1, "fuera_ventana": 2}
    indice: dict[tuple, tuple] = {}  # key -> (prioridad_actual, row)
    p = root / "data" / "live" / "libro_snapshots.csv"
    with open(p, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            motivo = row.get("motivo", "")
            if motivo not in prioridad:
                continue
            key = (row.get("market_id"), row.get("direction"))
            pr = prioridad[motivo]
            actual = indice.get(key)
            if actual is None or pr < actual[0]:
                indice[key] = (pr, row)
    return {k: v[1] for k, v in indice.items()}


def cargar_resultados_por_tupla(root: Path) -> dict:
    p = root / "data" / "shadow" / "results.csv"
    por_tupla = defaultdict(list)
    with open(p, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            strategy = row.get("strategy", "")
            subtype = row.get("subtype", "")
            decision = row.get("decision", "")
            if decision not in ("BUY_YES", "BUY_NO"):
                continue
            ts = parse_ts(row.get("prediction_timestamp", ""))
            if ts is None:
                continue
            row["_ts"] = ts
            tupla = f"{strategy}#{subtype}#{decision}"
            por_tupla[tupla].append(row)
    for tupla in por_tupla:
        por_tupla[tupla].sort(key=lambda r: r["_ts"])
    return por_tupla


def simular_tupla(rows: list, config: dict, params: dict, indice_libro: dict,
                   bankroll_inicial: float, desde_ts: datetime | None = None,
                   periodos_off: list | None = None) -> dict:
    riesgo = config.get("riesgo", {})
    cb = riesgo.get("circuit_breaker", {})
    half_kelly = riesgo.get("half_kelly", True)
    max_pct = riesgo.get("max_pct_bankroll_por_trade", 0.10)
    min_stake = riesgo.get("min_stake_eur", 0.25)
    max_stake = riesgo.get("max_stake_eur", 2.00)
    min_ratio_libro = riesgo.get("min_profundidad_ratio_libro", 5.0)
    freno_diario_pct = cb.get("freno_diario_pct", 0.15)
    freno_ventana_pct = cb.get("freno_ventana_pct", 0.20)
    bankroll_minimo = cb.get("bankroll_minimo_eur", 1.00)
    max_racha = cb.get("max_perdidas_consecutivas", 4)

    strategy, subtype, decision = rows[0]["strategy"], rows[0]["subtype"], rows[0]["decision"]
    ic = ic_para(strategy, subtype, decision, params)

    bankroll = bankroll_inicial
    suelo_disparado = False
    dia_actual = None
    bankroll_inicio_dia = bankroll_inicial
    racha_hoy: list[bool] = []
    freno_diario_activo_hoy = False
    ventana_actual = None
    bankroll_inicio_ventana = bankroll_inicial
    pnl_ventana = 0.0
    latches_ventana: set = set()  # (fecha, nombre_ventana)

    stats = dict(n_total=0, n_fuera_rango_validacion=0, n_fuera_ventana=0,
                 n_bloqueado_freno=0, n_sin_dato_libro=0, n_vetado_profundidad=0,
                 n_sin_ic=0, n_no_viable_stake=0, n_precio_invalido=0,
                 n_precio_sospechoso=0, n_ejecutado=0)
    equity = []
    periodos_off = periodos_off or []

    for row in rows:
        ts = row["_ts"]
        stats["n_total"] += 1

        if desde_ts is not None and ts < desde_ts:
            stats["n_fuera_rango_validacion"] += 1
            continue
        if any(ini <= ts <= fin for ini, fin in periodos_off):
            stats["n_fuera_rango_validacion"] += 1
            continue

        fecha_md = madrid_dt(ts, config).date()

        if dia_actual != fecha_md:
            dia_actual = fecha_md
            bankroll_inicio_dia = bankroll
            racha_hoy = []
            freno_diario_activo_hoy = False

        nombre_v = ventana_en(ts, config)
        if nombre_v is None:
            stats["n_fuera_ventana"] += 1
            continue

        if ventana_actual != (fecha_md, nombre_v):
            ventana_actual = (fecha_md, nombre_v)
            bankroll_inicio_ventana = bankroll
            pnl_ventana = 0.0

        if (suelo_disparado or freno_diario_activo_hoy
                or ventana_actual in latches_ventana
                or (len(racha_hoy) >= max_racha and not any(racha_hoy[-max_racha:]))):
            stats["n_bloqueado_freno"] += 1
            continue

        libro_row = indice_libro.get((row["market_id"], decision))
        if libro_row is None:
            stats["n_sin_dato_libro"] += 1
            continue

        try:
            ratio = float(libro_row["ratio_vs_stake"]) if libro_row.get("ratio_vs_stake") not in (None, "") else None
        except ValueError:
            ratio = None
        if ratio is None or ratio < min_ratio_libro:
            stats["n_vetado_profundidad"] += 1
            continue

        if ic is None:
            stats["n_sin_ic"] += 1
            continue

        techo_kelly = bankroll * abs(ic) * (0.5 if half_kelly else 1.0)
        techo_pct = bankroll * max_pct
        stake = min(techo_kelly, techo_pct, max_stake)
        stake = max(stake, min_stake) if bankroll >= min_stake else 0.0
        if stake <= 0:
            stats["n_no_viable_stake"] += 1
            continue

        try:
            precio_fill = float(libro_row["mejor_ask"])
        except (ValueError, TypeError):
            stats["n_precio_invalido"] += 1
            continue
        if not (0.01 < precio_fill < 0.99):
            stats["n_precio_invalido"] += 1
            continue

        try:
            precio_plan = float(libro_row.get("precio_plan") or 0)
            if abs(precio_fill - precio_plan) > PRECIO_SOSPECHOSO_DELTA:
                stats["n_precio_sospechoso"] += 1
        except (ValueError, TypeError):
            pass

        fee = FEE_RATE_TAKER_CRYPTO * precio_fill * (1 - precio_fill)
        acierto = row.get("acierto") == "1"
        pnl = stake * (1.0 / precio_fill - 1.0) - fee if acierto else -stake

        bankroll += pnl
        stats["n_ejecutado"] += 1
        racha_hoy.append(acierto)
        pnl_ventana += pnl
        equity.append({"ts": row["resolution_timestamp"], "bankroll": round(bankroll, 4), "pnl": round(pnl, 4)})

        if bankroll <= bankroll_minimo:
            suelo_disparado = True
        if bankroll_inicio_dia > 0 and (bankroll_inicio_dia - bankroll) / bankroll_inicio_dia >= freno_diario_pct:
            freno_diario_activo_hoy = True
        if pnl_ventana < 0 and bankroll_inicio_ventana > 0 and abs(pnl_ventana) / bankroll_inicio_ventana >= freno_ventana_pct:
            latches_ventana.add(ventana_actual)

    denom_fill = stats["n_ejecutado"] + stats["n_vetado_profundidad"]
    fill_rate = round(stats["n_ejecutado"] / denom_fill, 4) if denom_fill else None

    return {
        "strategy": strategy, "subtype": subtype, "decision": decision,
        "ic_usado": ic,
        **stats,
        "fill_rate": fill_rate,
        "bankroll_inicial": bankroll_inicial,
        "bankroll_nocional_final": round(bankroll, 4),
        "pnl_fiel_eur": round(bankroll - bankroll_inicial, 4),
        "suelo_disparado_final": suelo_disparado,
        "equity_curve": equity,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=".", help="raíz del repo (contiene data/)")
    ap.add_argument("--out", default=None, help="ruta de salida JSON")
    ap.add_argument("--bankroll-inicial", type=float, default=25.44)
    ap.add_argument("--min-n", type=int, default=1, help="omitir tuplas con menos de n señales totales")
    ap.add_argument("--promocion-json", default=None,
                     help="JSON {tupla: fecha_iso} — solo para validación: cuenta señales de esa "
                          "tupla desde su fecha real de promoción a live, no desde el inicio del shadow")
    ap.add_argument("--periodos-off", default=None,
                     help="lista separada por ';' de 'inicio_iso,fin_iso' — ventanas globales "
                          "(ej. circuit breaker real) en las que NINGUNA tupla cuenta señales, "
                          "para que la simulación no opere donde el switch real estuvo apagado")
    args = ap.parse_args()

    root = Path(args.root)
    out_path = Path(args.out) if args.out else root / "data" / "shadow" / "pnl_fiel_por_estrategia.json"

    config = cargar_config(root)
    params = cargar_params(root)
    indice_libro = construir_indice_libro(root)
    por_tupla = cargar_resultados_por_tupla(root)

    promocion = {}
    if args.promocion_json:
        with open(args.promocion_json, encoding="utf-8") as f:
            promocion = {k: parse_ts(v) for k, v in json.load(f).items()}

    periodos_off = []
    if args.periodos_off:
        for tramo in args.periodos_off.split(";"):
            ini_s, fin_s = tramo.split(",")
            periodos_off.append((parse_ts(ini_s), parse_ts(fin_s)))

    resultado = {}
    for tupla, rows in sorted(por_tupla.items()):
        if len(rows) < args.min_n:
            continue
        r = simular_tupla(rows, config, params, indice_libro, args.bankroll_inicial,
                           desde_ts=promocion.get(tupla), periodos_off=periodos_off)
        r["equity_curve"] = r["equity_curve"][-500:]  # cap tamaño de salida
        resultado[tupla] = r

    salida = {
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "bankroll_inicial_por_tupla": args.bankroll_inicial,
        "n_snapshots_libro_indexados": len(indice_libro),
        "limitaciones": [
            "IC usado para Kelly es el ACTUAL de strategy_params.json, no histórico punto-en-el-tiempo",
            "Overrides puntuales con fecha de circuit_breaker se ignoran (se usa siempre el valor base)",
            "Sin penalización por inventario direccional (bankroll nocional aislado por tupla)",
            "Señal sin snapshot de libro capturado ese ciclo → excluida, nunca estimada",
            "No replica veto CLV / veto discrepancia entre tuplas / streak_cooldown / abort_requote — "
            "validado 22-Jul: el AGREGADO de las 8 tuplas ya-live cuadra en signo y orden de magnitud "
            "con trades.csv real, pero el desglose POR TUPLA individual puede tener signo distinto "
            "con n bajo (2/8 cambiaron de signo en la validación) — orientativo, no concluyente",
        ],
        "estrategias": resultado,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(salida, f, indent=2, ensure_ascii=False)

    print(f"[shadow_pnl_fiel] {len(resultado)} tuplas simuladas, libro_index={len(indice_libro)} filas → {out_path}")
    total_pnl = sum(r["pnl_fiel_eur"] for r in resultado.values())
    total_ejecutado = sum(r["n_ejecutado"] for r in resultado.values())
    total_señales = sum(r["n_total"] for r in resultado.values())
    print(f"[shadow_pnl_fiel] pnl_fiel_total={total_pnl:+.2f}€  n_ejecutado_total={total_ejecutado}  n_señales_total={total_señales}")


if __name__ == "__main__":
    main()
