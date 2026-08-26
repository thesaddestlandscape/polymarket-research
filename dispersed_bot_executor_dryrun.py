#!/usr/bin/env python3
"""
dispersed_bot_executor_dryrun.py -- P-GALLINA FASE 1 (25-Ago noche,
petición explícita Javi: "busca alfa, dinero... cerrar el stage 0").
ACTUALIZADO 26-Ago (petición explícita Javi, tras ver 6/8 veredictos
nuevos del aviso de Telegram revertir a sin_concluir en el mismo día --
"actualízalo y déjalo acumulando para que trackee absolutamente todo el
universo, así tenemos datos de todo ya"): se elimina el filtro fijo a 3
combos hardcodeados. La inestabilidad del propio gate (buckets que pasan
y dejan de pasar en horas con solo un poco más de n) es la prueba de que
fijar el ejecutor a un snapshot puntual queda obsoleto casi de inmediato
-- mejor trackear TODO lo que detecta el firehose (4 arquetipos x 6
activos x 5 marcos x buckets de precio) y dejar que `_gate_veredicto()`
decida en vivo, en cada fila, si ese combo/bucket exacto está confirmado
HOY. Así se acumula histórico completo de decisión simulada (stake real,
circuit breakers) para el universo entero, sin tener que re-desplegar
cada vez que el gate cambia de veredicto.

Extensión de bot_wallets_gate_bucket_fase0.py (FASE 0, solo lectura) a
FASE 1 DRY_RUN. Fill-ability real (ratio_vs_stake>=5x) ya verificada
sólida en varios combos (SOL 58%, BTC 85%, XRP 60%, ver histórico) --
señales genuinamente ejecutables cuando el gate las confirma, no solo
teóricas.

Mismo patrón EXACTO de detección que bot_wallets_gate_bucket_fase0.py
(firehose vía _archivos_activity(), fill-ability vía _fillability_mirror()
de wallet_mirror_tracker.py) -- ahora SIN restringir a combos concretos.
Añade la capa que bot_wallets_gate_bucket_fase0.py no tiene: simulación
de decisión de trade real (calcular_stake real, circuit breakers) --
mismo criterio que wallet_mirror_executor_dryrun.py/momentum_ibs_
ballena_executor.py.

⚠️ DRY_RUN=True SIEMPRE. Activar DRY_RUN=False (dinero real) requiere
aprobación explícita de Javi en una sesión futura, con el checklist de
6 categorías (project_checklist_conexion_promocion_live_31jul) revisado
a fondo para el combo concreto -- pendiente: cruce contra ballenas/franja
fina NO hecho todavía (arquetipo de bot wallets no es una estrategia de
shadow_predict.py, zonas_validadas_externas.json no lo cubre), y exigir
ESTABILIDAD del veredicto durante varios días seguidos antes de proponer
nada, dada la fragilidad observada 26-Ago.

NO coloca, cancela ni modifica ninguna orden real mientras DRY_RUN=True.
"""
import csv
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from wallet_mirror_tracker import _archivos_activity, _fillability_mirror  # noqa: E402
from live_stake import calcular_stake, bloquear_por_circuit_breaker  # noqa: E402

DRY_RUN = True  # NUNCA cambiar sin aprobación explícita de Javi

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "dispersed_bot_executor_dryrun.csv"
VISTOS_PATH = DIR_SHADOW / "dispersed_bot_executor_dryrun_vistos.json"
BOTS_PATH = DIR_SHADOW / "bot_wallets_universo_25ago.json"
GATE_PATH = DIR_SHADOW / "bot_wallets_gate_bucket.json"
HIST = DIR_SHADOW / "ballenas_timing_history.csv"

POLL_S = 5
STEP_BUCKET = 0.05
UMBRAL_SNIPER_MIN = 5.0

COLUMNS = [
    "timestamp_utc", "trade_timestamp", "wallet", "arquetipo", "activo", "marco",
    "bucket_precio", "market_slug", "lado_wallet", "mejor_ask_deteccion",
    "profundidad_eur_deteccion", "ratio_vs_stake_deteccion", "sigue_fillable",
    "gate_veredicto", "stake_sim_eur", "circuit_breaker_bloquea", "decision_dry_run",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _bucket(p: float) -> float:
    return round(math.floor(p / STEP_BUCKET + 1e-9) * STEP_BUCKET, 4)


def clasificar_arquetipos(wallets: set) -> dict:
    """MISMA lógica que bot_wallets_gate_bucket_fase0.py::clasificar_arquetipos()."""
    from collections import defaultdict
    por_wallet = defaultdict(lambda: defaultdict(list))
    with open(HIST, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            w = r.get("wallet", "").lower()
            if w not in wallets:
                continue
            try:
                rm = float(r["restante_min"])
            except (TypeError, ValueError):
                continue
            por_wallet[w][r.get("marco", "?")].append(rm)
    out = {}
    for w, marcos in por_wallet.items():
        marco_dom = max(marcos, key=lambda m: len(marcos[m]))
        mediana = sorted(marcos[marco_dom])[len(marcos[marco_dom]) // 2]
        if marco_dom == "weekly":
            out[w] = "WEEKLY_TEMPRANO" if mediana > 500 else "WEEKLY_TARDIO"
        else:
            out[w] = "SNIPER" if mediana <= UMBRAL_SNIPER_MIN else "DISPERSO"
    return out


def _gate_veredicto(arquetipo: str, activo: str, marco: str, bucket: float) -> str:
    try:
        d = json.loads(GATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return "sin_datos"
    tabla = d.get(f"{arquetipo}#{activo}#{marco}", {})
    entrada = tabla.get(f"{bucket:.2f}")
    return entrada.get("veredicto", "sin_concluir") if entrada else "sin_concluir"


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-20000:]), encoding="utf-8")


def _guardar(filas: list) -> None:
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        for fila in filas:
            w.writerow([fila.get(c, "") for c in COLUMNS])


def _seed_vistos_sin_consultar(wallets: set) -> set:
    vistos = _vistos_cargar()
    nuevos = 0
    for path in _archivos_activity():
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if (row.get("side") or "").strip().upper() != "BUY":
                    continue
                w = (row.get("wallet") or "").lower()
                if w not in wallets:
                    continue
                dedup_key = f"{w}|{row.get('market_slug','')}"
                if dedup_key not in vistos:
                    vistos.add(dedup_key)
                    nuevos += 1
    _log(f"backlog existente marcado como visto sin consultar profundidad: {nuevos} matches")
    return vistos


def _procesar_fila(row: dict, wallets: set, arquetipos: dict, vistos: set) -> dict | None:
    if (row.get("side") or "").strip().upper() != "BUY":
        return None
    w = (row.get("wallet") or "").lower()
    if w not in wallets:
        return None
    arquetipo = arquetipos.get(w, "?")
    activo = row.get("activo", "")
    marco = row.get("marco", "")
    dedup_key = f"{w}|{row.get('market_slug','')}"
    if dedup_key in vistos:
        return None
    vistos.add(dedup_key)
    try:
        precio = float(row.get("price") or 0)
    except (TypeError, ValueError):
        return None
    if not (0.0 < precio < 1.0):
        return None
    b = _bucket(precio)
    # 26-Ago: sin filtro de combo -- se procesa TODO el universo (4
    # arquetipos x 6 activos x 5 marcos x bucket), el gate decide en vivo
    # por fila si ese combo/bucket exacto está confirmado hoy.

    lado = row.get("outcome", "")
    fill = _fillability_mirror(row.get("market_slug", ""), lado, row.get("price", ""))
    ratio = fill.get("ratio_vs_stake") if fill.get("ok") else None
    sigue_fillable = bool(ratio is not None and ratio >= 5.0)

    veredicto = _gate_veredicto(arquetipo, activo, marco, b)

    # Simulación de stake real (mismo camino que un ejecutor live real,
    # pero DRY_RUN -- nunca se envía). ic_proxy conservador: usamos el
    # hit-rate confirmado del bucket como proxy de IC (mismo patrón que
    # wallet_mirror_executor_dryrun.py/momentum_ibs_ballena_executor.py).
    ic_proxy = 0.15  # conservador -- no hay IC real para señales de wallet
    stake_sim = 0.0
    try:
        r_stake = calcular_stake(ic_proxy, strategy="DISPERSED_BOT", subtype=f"{activo}#{marco}",
                                  direction="BUY_YES" if lado == "Up" else "BUY_NO",
                                  precio_entrada=precio)
        stake_sim = r_stake.get("stake_eur", 0.0)
    except Exception as e:
        _log(f"WARN calcular_stake falló: {e}")

    cb_bloquea = False
    try:
        cb_bloquea = bool(bloquear_por_circuit_breaker(lambda motivo: _log(f"circuit breaker: {motivo}")))
    except Exception:
        pass

    decision = "DISPARARIA" if (veredicto == "bueno_confirmado" and sigue_fillable and not cb_bloquea) else "NO_dispara"

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "trade_timestamp": row.get("timestamp_utc", ""),
        "wallet": w, "arquetipo": arquetipo, "activo": activo, "marco": marco,
        "bucket_precio": f"{b:.2f}", "market_slug": row.get("market_slug", ""),
        "lado_wallet": lado, "mejor_ask_deteccion": fill.get("mejor_ask", "") if fill.get("ok") else "",
        "profundidad_eur_deteccion": fill.get("profundidad_eur", "") if fill.get("ok") else "",
        "ratio_vs_stake_deteccion": ratio if ratio is not None else "",
        "sigue_fillable": int(sigue_fillable), "gate_veredicto": veredicto,
        "stake_sim_eur": stake_sim, "circuit_breaker_bloquea": int(cb_bloquea),
        "decision_dry_run": decision,
    }


def main() -> None:
    bots = json.loads(BOTS_PATH.read_text(encoding="utf-8"))
    wallets = set(bots.keys())
    arquetipos = clasificar_arquetipos(wallets)
    _log(f"dispersed_bot_executor_dryrun arrancado (DRY_RUN={DRY_RUN}) -- "
         f"{len(wallets)} bot wallets, universo completo (sin filtro de combo)")

    vistos = _seed_vistos_sin_consultar(wallets)
    _vistos_guardar(vistos)

    posiciones: dict[Path, int] = {}
    cabeceras: dict[Path, list[str]] = {}
    while True:
        try:
            filas = []
            for path in _archivos_activity():
                if path not in posiciones:
                    with open(path, encoding="utf-8") as f:
                        cabeceras[path] = next(csv.reader([f.readline()]))
                        posiciones[path] = f.tell()
                with open(path, encoding="utf-8") as f:
                    f.seek(posiciones[path])
                    nuevas = f.readlines()
                    posiciones[path] = f.tell()
                if not nuevas:
                    continue
                header = cabeceras[path]
                for linea in csv.reader(nuevas):
                    if len(linea) != len(header):
                        continue
                    row = dict(zip(header, linea))
                    fila = _procesar_fila(row, wallets, arquetipos, vistos)
                    if fila is not None:
                        filas.append(fila)
                        _log(f"[{fila['arquetipo']}] {fila['activo']}#{fila['marco']}"
                             f"[{fila['bucket_precio']}) wallet={fila['wallet'][:10]}.. "
                             f"veredicto={fila['gate_veredicto']} fillable={fila['sigue_fillable']} "
                             f"stake_sim={fila['stake_sim_eur']} -> {fila['decision_dry_run']}")
            if filas:
                _guardar(filas)
                _vistos_guardar(vistos)
        except Exception as e:
            _log(f"🚨 error en ciclo: {type(e).__name__}: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
