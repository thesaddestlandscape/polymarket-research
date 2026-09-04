#!/usr/bin/env python3
"""
sports_wallet_mirror_frescura.py — gate de frescura de wallet para
Sports Wallet Mirror, mismo patrón EXACTO que wallet_mirror_tracker.py
(cripto) — ver ese fichero para la justificación completa del mecanismo
(wallets_operativas_recientes/wallets_operativas_recientes_por_bucket).

Petición explícita Javi, 04-Sep, textual: "esto tienes que hacerlo con
wallet mirror cripto y extenderlo a sports... no podemos dejar nada sin
cubrir". Sports NO tenía NINGÚN gate de frescura de wallet hasta hoy
(solo `cargar_wallets_validadas()` en sports_wallet_mirror_sniper.py,
histórico estático, sin exigir rendimiento reciente) — hueco real más
grande que en cripto, donde al menos existía la capa agregada.

Separación estricta (CLAUDE.md): solo lee data/sports/, nunca
data/shadow/data/live de cripto. Fichero propio, no se reutiliza código
de wallet_mirror_tracker.py (categorías distintas -- sports no tiene eje
de marco temporal, solo `categoria`).

Fuente única: data/sports/wallet_mirror_sniper_dry_run.csv (a diferencia
de cripto, sports NO tiene un `ballenas_timing_history.csv` equivalente
con histórico de mercado completo -- solo lo que el propio sniper ha
detectado y resuelto desde el 18-Ago). Con menos volumen que cripto
(48k filas vs 400k+), los umbrales de N por defecto dejarán MENOS
combinaciones (wallet,categoria[,bucket]) operativas al principio --
es el comportamiento fail-closed correcto, no un bug: sports lleva menos
tiempo vivo, hay menos evidencia reciente que exigir.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

from sports_wallet_mirror_gate_bucket import bucket as _bucket_precio
from analisis_gate_riguroso import wilson_ci

REPO = Path(__file__).resolve().parent
DIR_SPORTS = REPO / "data" / "sports"
EDGE_JSON = DIR_SPORTS / "wallet_edge_score_por_categoria.json"
DRY_RUN_VIVO = DIR_SPORTS / "wallet_mirror_sniper_dry_run.csv"

_cache_dry_run_vivo = {"mtime": None, "filas": None}


def _leer_dry_run_vivo_filas() -> list:
    """Lee wallet_mirror_sniper_dry_run.csv UNA vez, cacheado por mtime --
    mismo motivo/patrón que wallet_mirror_tracker.py (cripto, /code-review
    04-Sep): _historial_reciente() y _historial_reciente_por_bucket() lo
    leían cada una por separado en el mismo refresco."""
    try:
        mtime = DRY_RUN_VIVO.stat().st_mtime
    except OSError:
        return []
    if _cache_dry_run_vivo["mtime"] != mtime:
        with open(DRY_RUN_VIVO, encoding="utf-8") as f:
            _cache_dry_run_vivo["filas"] = list(csv.DictReader(f))
        _cache_dry_run_vivo["mtime"] = mtime
    return _cache_dry_run_vivo["filas"]

N_RECIENTE_OPERAR = 15             # mismo valor de partida que cripto (wallet_mirror_tracker.py)
MARGEN_DEGRADACION_PP_OPERAR = 15  # mismo criterio que cripto
N_RECIENTE_BUCKET_OPERAR = 8       # mismo valor de partida que cripto
MARGEN_DEGRADACION_PP_BUCKET = 15  # mismo criterio que MARGEN_DEGRADACION_PP_OPERAR
MIN_ANTIGUOS_DEGRADACION_BUCKET = 5  # mínimo de trades ANTERIORES a la ventana reciente
# para que el histórico DEL PROPIO BUCKET sea informativo.


def cargar_wallets_validadas() -> dict:
    """(wallet_lower, categoria) -> {"tipo","edge_pp","n","hit"}. Histórico
    completo, SIN filtrar por frescura -- mismo rol que la función gemela
    en sports_wallet_mirror_sniper.py, pero aquí también expone "hit" (la
    línea base contra la que se compara la degradación reciente)."""
    if not EDGE_JSON.exists():
        return {}
    d = json.loads(EDGE_JSON.read_text(encoding="utf-8"))
    out = {}
    for w in d.get("wallets_validadas", []):
        tipo = "SEGUIR" if w["edge_pp"] > 0 else "FADE"
        out[(w["wallet"].lower(), w["categoria"])] = {
            "tipo": tipo, "edge_pp": w["edge_pp"], "n": w["n"], "hit": w.get("hit"),
        }
    return out


def _historial_reciente(wallets_objetivo: set | None = None) -> dict:
    """(wallet, categoria, tipo) -> [(trade_timestamp, acierto_wallet), ...]
    ordenado. "acierto" en semántica NATIVA de la wallet (¿acertó ELLA?,
    no nuestra posición) -- el CSV guarda acierto de NUESTRA posición
    (mirror_outcome_index), así que se invierte para FADE, mismo criterio
    exacto que wallet_mirror_tracker.py::_historial_reciente_wallet_mirror
    (bug real cazado ahí el 24-Ago: mezclar las dos semánticas bajo la
    misma clave corrompe el gate)."""
    hist = defaultdict(dict)  # clave -> {(wallet,condition_id): (ts, acierto)} para dedup
    for row in _leer_dry_run_vivo_filas():
        if row.get("acierto") not in ("0", "1"):
            continue
        w = (row.get("wallet") or "").lower()
        if wallets_objetivo is not None and w not in wallets_objetivo:
            continue
        tipo = row.get("tipo", "")
        acierto = int(row["acierto"])
        if tipo == "FADE":
            acierto = 1 - acierto
        clave = (w, row.get("categoria", ""), tipo)
        cid = row.get("condition_id", "")
        hist[clave][(w, cid)] = (row.get("trade_timestamp", ""), acierto)
    out = {}
    for clave, por_cid in hist.items():
        out[clave] = sorted(por_cid.values(), key=lambda x: x[0])
    return out


def wallets_operativas_recientes() -> dict:
    """(wallet, categoria) -> info si tiene evidencia reciente suficiente
    (N_RECIENTE_OPERAR trades resueltos propios), no degradada frente a su
    histórico, y con borde estadístico propio sobre 50% -- MISMO criterio
    exacto que wallet_mirror_tracker.py (cripto). Fail-closed: candidata
    sin suficiente historial reciente propio se EXCLUYE."""
    candidatas = cargar_wallets_validadas()
    if not candidatas:
        return candidatas
    wallets_objetivo = {w for w, _ in candidatas}
    hist = _historial_reciente(wallets_objetivo)
    out = {}
    for clave, info in candidatas.items():
        w, categoria = clave
        aciertos = hist.get((w, categoria, info["tipo"]), [])
        if len(aciertos) < N_RECIENTE_OPERAR:
            continue
        if info.get("hit") is None:
            continue
        recientes = [a for _, a in aciertos[-N_RECIENTE_OPERAR:]]
        k, n = sum(recientes), len(recientes)
        ci_lo, ci_hi = wilson_ci(k, n)
        hit_hist = info["hit"] * 100
        if ci_hi * 100 < (hit_hist - MARGEN_DEGRADACION_PP_OPERAR):
            continue  # degradada frente a SU histórico
        k_posicion = k if info["tipo"] == "SEGUIR" else (n - k)
        ci_lo_posicion, _ = wilson_ci(k_posicion, n)
        if ci_lo_posicion <= 0.50:
            continue  # sin edge reciente confirmado por sí mismo
        out[clave] = info
    return out


def _historial_reciente_por_bucket(wallets_objetivo: set | None = None) -> dict:
    """(wallet, categoria, tipo, bucket_precio) -> [(ts, acierto), ...].
    Mismo motivo de función separada (no tocar _historial_reciente) que
    la versión de cripto -- `mejor_ask_mirror` (NUESTRO ask real en el
    lado que mirroreamos) como ancla del bucket, el MISMO campo exacto
    que sports_wallet_mirror_gate_bucket.py/analisis_sports_wallet_
    mirror_gate_bucket_26ago.py usan para construir sus propios buckets
    desde este mismo CSV.

    /code-review 04-Sep, hallazgo real (misma clase de bug que se corrigió
    el mismo día en wallet_mirror_tracker.py, cripto): la primera versión
    usaba `precio_wallet` (el precio al que operó LA WALLET), NO
    `mejor_ask_mirror` (nuestro ask real) -- difieren materialmente
    (mediana |diff|=0,03, media=0,13 en muestra real de 2000 filas),
    a menudo cruzando de bucket. Con la clave equivocada, el lookup en el
    ejecutor (que consulta por el ask REAL) habría fallado sistemáticamente
    contra el bucket equivocado -- el gate habría bloqueado wallets con
    edge real o aprobado wallets con edge medido en una zona de precio
    distinta, justo lo que este mecanismo existe para evitar."""
    hist = defaultdict(dict)
    for row in _leer_dry_run_vivo_filas():
        if row.get("acierto") not in ("0", "1"):
            continue
        w = (row.get("wallet") or "").lower()
        if wallets_objetivo is not None and w not in wallets_objetivo:
            continue
        tipo = row.get("tipo", "")
        acierto = int(row["acierto"])
        if tipo == "FADE":
            acierto = 1 - acierto
        try:
            precio = float(row.get("mejor_ask_mirror"))
        except (TypeError, ValueError):
            continue
        b = _bucket_precio(precio)
        clave = (w, row.get("categoria", ""), tipo, b)
        cid = row.get("condition_id", "")
        hist[clave][(w, cid)] = (row.get("trade_timestamp", ""), acierto)
    out = {}
    for clave, por_cid in hist.items():
        out[clave] = sorted(por_cid.values(), key=lambda x: x[0])
    return out


def wallets_operativas_recientes_por_bucket(wallets_admitidas: dict | None = None) -> dict:
    """(wallet, categoria, tipo, bucket_precio) -> info si la wallet tiene
    evidencia reciente CON EDGE dentro de ESE micro-bucket concreto --
    capa ADICIONAL sobre wallets_operativas_recientes(), no sustituto.
    wallets_admitidas: dict de wallets_operativas_recientes(), recomendado
    para no evaluar el bucket de wallets ya excluidas en agregado."""
    candidatas = cargar_wallets_validadas()
    if not candidatas:
        return {}
    if wallets_admitidas is not None:
        candidatas = {k: v for k, v in candidatas.items() if k in wallets_admitidas}
    wallets_objetivo = {w for w, _ in candidatas}
    hist = _historial_reciente_por_bucket(wallets_objetivo)
    out = {}
    for (w, categoria, tipo, b), aciertos in hist.items():
        info = candidatas.get((w, categoria))
        if info is None or info["tipo"] != tipo:
            continue
        if len(aciertos) < N_RECIENTE_BUCKET_OPERAR:
            continue
        recientes_tup = aciertos[-N_RECIENTE_BUCKET_OPERAR:]
        recientes = [a for _, a in recientes_tup]
        k, n = sum(recientes), len(recientes)
        # Mismo fix 04-Sep que wallet_mirror_tracker.py (cripto,
        # /code-review): comparar contra el histórico DE ESTE BUCKET
        # concreto, calculado con la parte de `aciertos` anterior a la
        # ventana reciente -- sin precomputado (a diferencia de
        # info["hit"] agregado). Si no hay suficiente historia previa,
        # se deja pasar solo por el borde >50% de abajo.
        antiguos_tup = aciertos[:-N_RECIENTE_BUCKET_OPERAR]
        if len(antiguos_tup) >= MIN_ANTIGUOS_DEGRADACION_BUCKET:
            k_hist = sum(a for _, a in antiguos_tup)
            hit_hist_bucket = k_hist / len(antiguos_tup) * 100
            _, ci_hi = wilson_ci(k, n)
            if ci_hi * 100 < (hit_hist_bucket - MARGEN_DEGRADACION_PP_BUCKET):
                continue  # degradada frente a SU histórico EN ESTE BUCKET
        k_posicion = k if tipo == "SEGUIR" else (n - k)
        ci_lo_posicion, _ = wilson_ci(k_posicion, n)
        if ci_lo_posicion <= 0.50:
            continue
        out[(w, categoria, tipo, b)] = {"n": n, "hit_reciente": round(k / n, 4)}
    return out


def wallet_aprueba_bucket(wallet: str, categoria: str, tipo: str, ask: float, cache: dict) -> bool:
    """Lookup de conveniencia para el ejecutor. `cache` = resultado ya
    calculado de wallets_operativas_recientes_por_bucket()."""
    b = _bucket_precio(ask)
    return (wallet.lower(), categoria, tipo, b) in cache
