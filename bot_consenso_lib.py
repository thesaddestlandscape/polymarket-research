#!/usr/bin/env python3
"""bot_consenso_lib.py — Extracción de `_bots_consenso()`/`_cargar_bot_wallets()`/
`_cargar_bot_wallets_por_activo()` desde `shadow_predict.py` (líneas 5043-5187
originales, lógica IDÉNTICA, copiada sin cambios) a un módulo pequeño e
independiente, para poder reusarla desde ejecutores de baja latencia que
NO deben importar el módulo `shadow_predict.py` completo (7400+ líneas,
estado global de muchas otras estrategias, imports pesados).

Motivo (09-Sep, petición explícita Javi: "Tenemos que intentar sacar todo
el rendimiento posible a todas las estrategias, quizá hasta funcione en
gbm, Momentum..."): verificado que `BALLENAS_TARDIAS` (ballenas_executor_
btc15m.py / ballenas_executor_5min.py) y `FAVORITO_CONFIRMADO` baja
latencia (favorito5min_bajalatencia_fase0.py) corren en ejecutores propios
FUERA del bucle de `shadow_predict.py` -- 0/4.793 señales recientes de
BALLENAS_TARDIAS tenían el dato de bot_consenso, y `favorito5min_
bajalatencia_fase0.csv` ni siquiera tenía la columna. Hueco de
instrumentación real, no una zona ya explorada.

`shadow_predict.py` pasa a IMPORTAR de aquí (mismos nombres `_bots_consenso`
/`_cargar_bot_wallets`/`_cargar_bot_wallets_por_activo`, delegando --
ningún call site de los ~15 existentes en shadow_predict.py necesita
cambiar), única fuente de verdad para ambos usos -- mismo criterio que
`gate_bucket_propio.py`/`gbm_confluencia.py` (módulos pequeños y
compartidos en vez de duplicar lógica).

Solo lectura de disco (JSON cacheado por mtime) + `ballenas_firehose_cache.
leer_snapshot_reciente()` (cero llamadas de red, mismo mecanismo ya usado
en producción por `_gate_volumen_ballenas()`). NUNCA toca `prob_yes`,
stake ni ninguna decisión de envío de orden -- feature puramente aditiva
de logueo, igual que en su ubicación original."""
import json
from pathlib import Path

import ballenas_firehose_cache as _fc

DIR_SHADOW = Path(__file__).resolve().parent / "data" / "shadow"

_BOT_WALLETS_PATH = DIR_SHADOW / "bot_wallets_universo_25ago.json"
_bot_wallets_cache = {"mtime": None, "set": frozenset()}
_WEDGE_PATH = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
_bot_wallets_por_activo_cache = {"mtime": None, "por_activo": {}}


def _cargar_bot_wallets() -> frozenset:
    """Carga perezosa + cacheada por mtime de las 84 bot wallets con edge
    confirmado. Fail-open a frozenset() si el fichero no existe/corrupto."""
    global _bot_wallets_cache
    try:
        mtime = _BOT_WALLETS_PATH.stat().st_mtime
    except OSError:
        return frozenset()
    if _bot_wallets_cache["mtime"] != mtime:
        try:
            data = json.loads(_BOT_WALLETS_PATH.read_text(encoding="utf-8"))
            _bot_wallets_cache = {"mtime": mtime, "set": frozenset(w.lower() for w in data.keys())}
        except Exception:
            return _bot_wallets_cache["set"]
    return _bot_wallets_cache["set"]


def _cargar_bot_wallets_por_activo(activo: str) -> frozenset:
    """Subconjunto de bot wallets cuyo edge está confirmado (sig_bhfdr +
    g_kelly>0 + edge_pp>0) específicamente para ESTE activo -- evita que
    una wallet confirmada solo en BTC#5min diluya el consenso de un
    mercado de DOGE con el mismo peso que una wallet confirmada ahí."""
    global _bot_wallets_por_activo_cache
    try:
        mtime = _WEDGE_PATH.stat().st_mtime
    except OSError:
        return frozenset()
    if _bot_wallets_por_activo_cache["mtime"] != mtime:
        try:
            wedge = json.loads(_WEDGE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return _bot_wallets_por_activo_cache["por_activo"].get(activo, frozenset())
        por_activo: dict = {}
        for v in wedge.values():
            if not (v.get("sig_bhfdr") and v.get("g_kelly", 0) > 0 and v.get("edge_pp", 0) > 0):
                continue
            a = v.get("activo")
            w = (v.get("wallet") or "").lower()
            if not a or not w:
                continue
            por_activo.setdefault(a, set()).add(w)
        por_activo = {a: frozenset(ws) for a, ws in por_activo.items()}
        _bot_wallets_por_activo_cache = {"mtime": mtime, "por_activo": por_activo}
    return _bot_wallets_por_activo_cache["por_activo"].get(activo, frozenset())


def _bots_consenso(market: dict, activo: str | None = None) -> dict:
    """Consenso mayoritario de las bot wallets con edge confirmado sobre
    el MISMO mercado (`market["condition_id"]`) que se está prediciendo/
    ejecutando. Devuelve `bot_consenso_n/lado/pct` (universo plano de 84)
    y, si se pasa `activo`, además `bot_consenso_activo_n/lado/pct`
    (restringido a wallets confirmadas para ESE activo). Fail-open: en
    cualquier fallo (fichero ausente, snapshot no disponible) devuelve el
    dict vacío (`None`/`0`) -- NUNCA lanza excepción, NUNCA bloquea al
    caller (mismo criterio que el resto de features de solo-logueo)."""
    condition_id = market.get("condition_id")
    base_vacio = {"bot_consenso_n": 0, "bot_consenso_lado": None, "bot_consenso_pct": None,
                  "bot_consenso_activo_n": 0, "bot_consenso_activo_lado": None, "bot_consenso_activo_pct": None}
    if not condition_id:
        return base_vacio
    bots = _cargar_bot_wallets()
    bots_activo = _cargar_bot_wallets_por_activo(activo) if activo else frozenset()
    if not bots and not bots_activo:
        return base_vacio
    try:
        trades = _fc.leer_snapshot_reciente(condition_id)
    except Exception:
        return base_vacio
    votos: dict = {}
    votos_activo: dict = {}
    for t in trades:
        if (t.get("side") or "").strip().upper() != "BUY":
            continue
        w = (t.get("proxyWallet") or "").lower()
        lado = t.get("outcome", "")
        if not lado:
            continue
        if w in bots:
            votos[lado] = votos.get(lado, 0) + 1
        if w in bots_activo:
            votos_activo[lado] = votos_activo.get(lado, 0) + 1
    n_total = sum(votos.values())
    n_total_activo = sum(votos_activo.values())
    resultado = dict(base_vacio)
    if n_total > 0:
        lado_mayoria = max(votos, key=votos.get)
        resultado.update({
            "bot_consenso_n": n_total,
            "bot_consenso_lado": lado_mayoria,
            "bot_consenso_pct": round(votos[lado_mayoria] / n_total, 4),
        })
    if n_total_activo > 0:
        lado_mayoria_activo = max(votos_activo, key=votos_activo.get)
        resultado.update({
            "bot_consenso_activo_n": n_total_activo,
            "bot_consenso_activo_lado": lado_mayoria_activo,
            "bot_consenso_activo_pct": round(votos_activo[lado_mayoria_activo] / n_total_activo, 4),
        })
    return resultado
