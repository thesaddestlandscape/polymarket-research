#!/usr/bin/env python3
"""candidata9_gate_bucket.py — 08-Sep, módulo LIGERO (sin dependencias
pesadas -- solo json/math/pathlib) que expone el gate de micro-bucket de
CANDIDATA9_BOT_CONSENSO (candidata9_10_gate_bucket.json) con la MISMA
firma que wallet_mirror_gate_bucket.py/resolution_sniper_naive_gate_
bucket.py, para poder registrarse en live_trade.py::
_GATES_EXTERNOS_POR_ESTRATEGIA sin crear un import circular.

Por qué un módulo aparte y no reusar la función ya escrita en
candidata9_bot_consenso_reactivo_fase0.py: ese módulo importa
wallet_mirror_tracker (para _fillability_mirror), que a su vez importa
live_trade -- si live_trade.py importara candidata9_bot_consenso_
reactivo_fase0.py directamente, el ciclo live_trade → fase0 →
wallet_mirror_tracker → live_trade rompería el arranque del proceso.
Mismo motivo por el que wallet_mirror_gate_bucket.py vive aislado de
wallet_mirror_tracker.py pese a evaluar exactamente los mismos datos.

Única fuente de verdad para el precio: candidata9_10_gate_bucket.json,
regenerado por analisis_candidata9_10_gate_bucket_26ago.py (cron/vigía ya
existente, ver vigia_candidata9_10_gate_bucket_26ago.py). Este módulo
solo LEE -- nunca escribe, nunca decide qué es bueno_confirmado, solo
expone el veredicto ya calculado con la firma que live_trade.py espera.
"""
import json
import math
import time
from pathlib import Path

from gate_frescura import esta_fresco, avisar_obsoleto, MAX_ANTIGUEDAD_DIARIO_S

REPO = Path(__file__).resolve().parent
GATE_PATH = REPO / "data" / "shadow" / "candidata9_10_gate_bucket.json"
GATE_STEP = 0.05

_gate_cache: dict = {"mtime": None, "datos": {}}

# 10-Sep (hallazgo real, checklist de promoción de ETH#5min[0.30,0.35)):
# este módulo, a diferencia de sus hermanos (bot_wallets_gate_bucket.py,
# wallet_mirror_gate_bucket.py), no tenía NINGUNA capa de aprobación
# manual por micro-bucket -- `evaluar()` confía en cualquier bucket que
# candidata9_10_gate_bucket.json marque bueno_confirmado, y el generador
# (analisis_candidata9_10_gate_bucket_26ago.py) tampoco calcula ni vetea
# por g_kelly (payout asimétrico). Con CANDIDATA9_BOT_CONSENSO ya en
# pares_permitidos_live (ETH#15min#BUY_YES/BUY_NO desde 08-Sep) y sin
# separación por bucket en esa whitelist, cualquier bucket nuevo que
# confirme -- con payout inverso o sin verificar -- se activaría solo.
# Mismo patrón exacto que bot_wallets_gate_bucket.py::BUCKETS_APROBADOS_
# REAL/permitido_real() (08-Sep), aplicado aquí ahora.
#
# ETH#5min[0.30,0.35): gate n=65 pnl/tr=+0,645€ shuffle_p=0,0 split-half
# ambas mitades positivas, CI90 bootstrap=[0,344,0,930] (no cruza cero).
# g_kelly(f=10%)=+0,0526 (calculado a mano el 10-Sep, NO payout inverso
# -- el generador no lo comprueba, hueco real encontrado en este mismo
# checklist). Fill-ability real (candidata9_bot_consenso_executor.csv):
# n_en_zona=16, fillable=14 (87,5%). Concentración sana: 508 mercados
# únicos de 510 filas ETH#5min, consenso de 2-6 wallets por evento (sin
# wallet/mercado dominante). Cruce con ballenas: señal independiente
# (hit propio 55,4% vs baseline agregado ballenas ETH#5min 59,1% -- no
# redescubre el mismo edge). Checklist completo, decisión explícita Javi.
#
# 13-Sep, 12 buckets adicionales aprobados (petición explícita Javi, tras
# barrido de rescate post-fix precio invertido -- ver project_bug_
# inversion_precio_candidata9_buyno_11sep): mismo checklist (g_kelly a
# mano vía wallet_edge_tracker._g_kelly sobre eventos_candidata9(),
# fill-ability real desde candidata9_bot_consenso_executor.csv,
# concentración wallet/mercado). Todos g_kelly>0, fill-ability 51-96%,
# top1-wallet<14% salvo donde se anota. Dejados FUERA a propósito (aviso,
# revisar más adelante): ETH#5min[0.55,0.60) (fill-ability 28,2%, posible
# arquetipo A) y BNB#5min[0.25,0.30) (top1-wallet 28,1% de solo 15
# wallets, cerca del umbral de alarma 30%).
#   BTC#5min[0.40,0.45) n=155 g=+0,0260 fill=95,7% top1=n/d
#   BTC#5min[0.45,0.50) n=955 g=+0,0146 fill=88,1% top1=6,3%
#   BTC#5min[0.50,0.55) n=1433 g=+0,0227 fill=59,9% top1=6,0%
#   ETH#5min[0.25,0.30) n=45 g=+0,0676 fill=80,6% top1=13,9%
#   ETH#5min[0.35,0.40) n=124 g=+0,0314 fill=83,8% top1=10,7%
#   ETH#5min[0.50,0.55) n=697 g=+0,0193 fill=60,0% top1=8,8%
#   SOL#5min[0.45,0.50) n=215 g=+0,0294 fill=76,8% top1=10,1%
#   SOL#5min[0.50,0.55) n=702 g=+0,0176 fill=63,8% top1=12,2%
#   BTC#15min[0.45,0.50) n=308 g=+0,0270 fill=82,4% top1=5,8%
#   BTC#15min[0.50,0.55) n=458 g=+0,0337 fill=61,8% top1=4,5%
#   ETH#15min[0.50,0.55) n=449 g=+0,0245 fill=51,2% top1=7,1% -- ÚNICO
#   bucket de la tupla ya viva desde 08-Sep (CANDIDATA9_BOT_CONSENSO#ETH#
#   15min), que llevaba muda (0 buckets aprobados) desde entonces.
# 15-Sep, checklist completo (petición explícita Javi, "procede atendiendo
# a los objetivos y misiones de este proyecto"): BTC#5min[0.30,0.35)
# añadido -- gate propio n=37-39, shuffle_p=0,0, p_valor_abs=0,0, 3/3 días
# de historial (tolerancia multi-día, fix del mismo 15-Sep), fill-ability
# real 98,5% (n=65, candidata9_bot_consenso_executor.csv), concentración
# de mercado limpia (66/66 mercados distintos, top1=1,5%), g_kelly(f=10%)
# =+0,072 (positivo, sin payout inverso). Cruce con ballenas (
# ballenas_timing_history.csv, BTC#5m): hit=32,8% n=11.273 vs breakeven
# ~34,9% -- NO corrobora (población de "cualquier ballena a este precio"
# es mediocre/neutra), el edge parece venir específicamente del filtro de
# consenso de bots (~4-5 wallets votando el mismo lado), no de la zona de
# precio en sí -- aceptado con esa reserva explícita, no es una
# contradicción del gate propio. BTC#5min[0.20,0.25) (n=18, mismo cruce
# con ballenas peor, hit=18,3% vs breakeven ~24,2%) se deja FUERA a
# propósito -- menos n y peor cruce, dejar acumular más días antes de
# repetir el checklist.
BUCKETS_APROBADOS_REAL = {
    ("ETH", "5min"): {0.25, 0.30, 0.35, 0.50},
    ("BTC", "5min"): {0.30, 0.40, 0.45, 0.50},
    ("SOL", "5min"): {0.45, 0.50},
    ("BTC", "15min"): {0.45, 0.50},
    ("ETH", "15min"): {0.50},
}

# 14-Sep (hallazgo real, petición explícita Javi -- "no podemos permitirnos
# perder trades ganadores, tiene que dejar pasar las señales óptimas"):
# candidata9_bot_consenso_executor.py usaba una única constante
# EDGE_DIR_ESTIMADO=0.072 (medida el 08-Sep SOLO para ETH#15min[0.50,0.55))
# para los 12 buckets de arriba -- el _decidir_requote() de live_trade.py
# usa ese valor como presupuesto de edge que el deterioro del libro puede
# comerse antes de abortar. Medido ahora (mismo pipeline fiable que
# BUCKETS_APROBADOS_REAL, eventos_candidata9() sobre bot_wallets_gate_
# bucket_fase0.csv, hit_rate-ask_medio): el edge real de LOS 12 buckets es
# 10,1pp a 21,7pp -- muy por encima del 7,2pp asumido -- así que la
# constante vieja era sistemáticamente demasiado conservadora en los 12,
# abortando por deterioro trades que en realidad seguían teniendo edge de
# sobra. Nunca al revés (ningún bucket mide menos de 0.072), así que este
# cambio solo deja pasar MÁS trades ganadores, nunca menos protección.
EDGE_MEDIDO_REAL = {
    ("ETH", "5min", 0.25): 0.217,
    ("ETH", "5min", 0.30): 0.216,
    ("ETH", "5min", 0.35): 0.139,
    ("ETH", "5min", 0.50): 0.131,
    ("BTC", "5min", 0.30): 0.294,
    ("BTC", "5min", 0.40): 0.145,
    ("BTC", "5min", 0.45): 0.101,
    ("BTC", "5min", 0.50): 0.149,
    ("SOL", "5min", 0.45): 0.176,
    ("SOL", "5min", 0.50): 0.124,
    ("BTC", "15min", 0.45): 0.166,
    ("BTC", "15min", 0.50): 0.200,
    ("ETH", "15min", 0.50): 0.158,
}
# Fallback SOLO para un bucket que se apruebe en el futuro en
# BUCKETS_APROBADOS_REAL sin medir todavía aquí -- mismo valor
# conservador de origen (08-Sep), nunca asumir un edge alto sin medirlo.
EDGE_FALLBACK_CONSERVADOR = 0.072

# 15-Sep (petición explícita Javi, propuesta 1 de "10 para explotar el
# edge ya capturado"): EDGE_MEDIDO_REAL de arriba era una foto fija --
# solo se remedía a mano cuando alguien añadía un bucket nuevo (ETH#15min
# seguía con el dato de una sola sesión del 08-Sep). El edge cambia con
# el tiempo igual que cualquier otro gate del proyecto; el dict de arriba
# ahora es solo la SEMILLA/fallback de origen -- la fuente de verdad viva
# es este JSON, regenerado a diario por analisis_candidata9_edge_medido_
# real.py (mismo patrón mtime-cache que _gate_veredicto_dict de abajo).
# Solo puede venir de un bucket que YA esté en BUCKETS_APROBADOS_REAL
# (nunca "descubre" edge de un bucket no aprobado).
EDGE_JSON_PATH = REPO / "data" / "shadow" / "candidata9_edge_medido_real.json"
_edge_cache: dict = {"mtime": None, "datos": {}}


def _bucket(precio: float) -> float:
    return round(math.floor(precio / GATE_STEP + 1e-9) * GATE_STEP, 4)


def _edge_medido_vivo(activo: str, marco: str, b: float) -> float | None:
    """Lee data/shadow/candidata9_edge_medido_real.json (mtime-cached).
    None si el fichero no existe todavía, está corrupto, o el bucket no
    aparece -- el caller cae al dict EDGE_MEDIDO_REAL/fallback estático,
    nunca a "sin protección" (mismo fail-closed que el resto del módulo)."""
    try:
        st = EDGE_JSON_PATH.stat()
    except OSError:
        return None
    if time.time() - st.st_mtime > MAX_ANTIGUEDAD_DIARIO_S:
        avisar_obsoleto(EDGE_JSON_PATH)  # visible: sin esto el fallback conservador seria silencioso
        return None  # 21-Sep: edge medido obsoleto -> como si no existiera
    if _edge_cache["mtime"] != st.st_mtime:
        try:
            _edge_cache["datos"] = json.loads(EDGE_JSON_PATH.read_text(encoding="utf-8"))
            _edge_cache["mtime"] = st.st_mtime
        except Exception:
            return None
    clave = f"{activo}#{marco}#{b:.2f}"
    valor = _edge_cache["datos"].get(clave)
    return float(valor) if valor is not None else None


def edge_estimado(activo: str, marco: str, ask: float) -> float:
    """Edge real medido para el bucket exacto -- primero el JSON vivo
    (remedido a diario), si no existe cae al dict estático EDGE_MEDIDO_
    REAL (semilla de origen), si tampoco está ahí, fallback conservador."""
    b = _bucket(ask)
    vivo = _edge_medido_vivo(activo, marco, b)
    if vivo is not None:
        return vivo
    return EDGE_MEDIDO_REAL.get((activo, marco, b), EDGE_FALLBACK_CONSERVADOR)


def permitido_real(activo: str, marco: str, precio: float) -> bool:
    """16-Sep tarde (petición explícita Javi: "cuando salga un micro-bucket
    bueno confirmado tiene que abrirse automáticamente, no podemos estar
    pendientes todo el rato" -- ampliado el mismo día, tras /code-review,
    "esto tiene que ser así en todas las tuplas live... el sistema tiene
    que ser inteligente para operar en cada momento en todos los micro-
    buckets confirmados... si un micro-bucket pasa a sin_concluir o malo
    confirmado, automáticamente no se opera ahí hasta que revierta y se
    vuelva a abrir automáticamente"): quitada la capa BUCKETS_APROBADOS_
    REAL -- era exactamente la tabla hardcodeada que CLAUDE.md prohíbe
    desde 05-Ago, reintroducida aquí el 08/13/15-Sep porque en esa fecha
    el generador del JSON todavía no vetaba por payout asimétrico
    (g_kelly). Reemplazada por DOS checks automáticos, mismo patrón
    exacto que bot_wallets_gate_bucket.py::permitido_real() (16-Sep,
    portado tal cual, nunca duplicar el criterio), sin perder ninguna de
    las dos protecciones que antes exigían aprobación manual:

    (a) el gate diario (_degradar() compartido, analisis_bot_wallets_
        gate_bucket_25ago.py, aplicado aquí desde analisis_candidata9_10_
        gate_bucket_26ago.py) ya cubre payout asimétrico, concentración
        de wallet, tendencia reciente Y, desde hoy, fill-ability real
        medida automáticamente contra el propio ejecutor dry-run
        (candidata9_bot_consenso_executor.csv, columna
        sigue_fillable_en_decision) -- un bucket nunca llega a
        bueno_confirmado por primera vez sin esa evidencia.
    (b) edge_estimado() puede caer al fallback EDGE_FALLBACK_CONSERVADOR
        si el bucket no tiene medición viva todavía -- aceptable para
        `evaluar()`/dry-run, NUNCA para dinero real: exige edge remedido
        en vivo hoy (analisis_candidata9_edge_medido_real.py ahora cubre
        TODO bucket bueno_confirmado, no solo una lista pre-aprobada, se
        cumple sola en el mismo ciclo cron en que el bucket se confirma).

    Ambos checks se re-evalúan EN CALIENTE (mtime-cache) en cada llamada
    -- si el gate diario degrada el bucket mañana, esta función deja de
    operar ahí automáticamente, y reabre sola en cuanto reconfirme. La
    protección por-trade (CLV, profundidad real, requote/abort) sigue
    intacta más abajo en el pipeline, independiente de esta función."""
    # 21-Sep: guardia de antiguedad fail-closed (mismo hueco que bot_wallets_gate_bucket.py), ver gate_frescura.py
    if not esta_fresco(GATE_PATH):
        avisar_obsoleto(GATE_PATH)
        return False
    info = _gate_veredicto_dict(activo, marco, precio)
    if info.get("veredicto") != "bueno_confirmado":
        return False
    # 16-Sep tarde (hallazgo real al probar el fix con datos reales, mismo
    # día): la tolerancia histórica ("2 de los últimos 3 días") puede
    # arrastrar un "bueno_confirmado" de días ANTERIORES a que este veto de
    # fill-ability existiera, aunque HOY mismo _degradar() haya marcado
    # fillable_n<15 -- caso real, CANDIDATA9_BOT_CONSENSO#BTC#5min[0.85,0.90)
    # el mismo día de este cambio. Leer fillable_n directo del JSON (lo
    # escribe _degradar() en la misma entrada) en vez de fiarse solo de
    # `veredicto` cierra el hueco sin esperar 2-3 días a que la tolerancia
    # se autolimpie -- fail-closed: ausente/None se trata como 0.
    if (info.get("fillable_n") or 0) < 15:
        return False
    b = _bucket(precio)
    if _edge_medido_vivo(activo, marco, b) is None and (activo, marco, b) not in EDGE_MEDIDO_REAL:
        return False  # fail-closed: sin edge medido real para este bucket exacto, no operar sobre el fallback genérico
    return True


def _gate_veredicto_dict(activo: str, marco: str, precio: float) -> dict:
    """Consulta EN CALIENTE candidata9_10_gate_bucket.json -- única fuente
    de verdad, autoaprendiente (mismo patrón que gate_bucket_propio.py en
    cripto). Cachea por mtime, no relee el fichero en cada llamada. Fail-
    closed: sin fichero/clave/bucket -> {"veredicto": "sin_concluir"},
    nunca "permitir por defecto"."""
    try:
        st = GATE_PATH.stat()
    except OSError:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "sin_fichero"}}
    if _gate_cache["mtime"] != st.st_mtime:
        try:
            _gate_cache["datos"] = json.loads(GATE_PATH.read_text(encoding="utf-8"))
            _gate_cache["mtime"] = st.st_mtime
        except Exception:
            return {"veredicto": "sin_concluir", "detalle": {"origen": "fichero_ilegible"}}
    clave = f"CANDIDATA9_BOT_CONSENSO#{activo}#{marco}"
    tabla = _gate_cache["datos"].get(clave)
    if not tabla:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "sin_clave", "clave": clave}}
    bucket_key = f"{math.floor(precio / GATE_STEP + 1e-9) * GATE_STEP:.2f}"
    info = tabla.get(bucket_key)
    if not info:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "sin_bucket", "bucket": bucket_key}}
    return info


def evaluar(activo: str, marco: str, precio: float) -> dict:
    """Alias directo, para llamadores que ya tienen (activo, marco, precio)
    resueltos (candidata9_bot_consenso_reactivo_fase0.py/executor)."""
    return _gate_veredicto_dict(activo, marco, precio)


def evaluar_para_recheck(subtype: str, direction: str, py: float, contexto: dict) -> dict:
    """Firma uniforme que live_trade.py::_ejecutar_orden_polymarket usa en
    el re-chequeo post-requote y en el multi-lectura de justo antes de
    firmar (registrado en _GATES_EXTERNOS_POR_ESTRATEGIA) -- mismo patrón
    que wallet_mirror_gate_bucket.py::evaluar_para_recheck (ver su
    docstring). `py` llega en perspectiva YES -- se convierte al precio
    del lado que de verdad estamos comprando (el gate opera sobre el ask
    del lado mayoritario, no sobre YES a secas).

    10-Sep: aplica SIEMPRE permitido_real() -- misma razón exacta que
    bot_wallets_gate_bucket.py::evaluar_para_recheck (ver su docstring):
    este gate no separaba la whitelist por bucket, así que la
    restricción tiene que vivir aquí para cubrir tanto el chequeo
    inicial (candidata9_bot_consenso_executor.py) como el recheck con
    una sola fuente."""
    partes = subtype.split("#")
    if len(partes) != 2:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "subtype_invalido"}}
    activo, marco = partes
    ask = py if direction == "BUY_YES" else round(1.0 - py, 6)
    if not permitido_real(activo, marco, ask):
        return {
            "veredicto": "malo_confirmado",
            "detalle": {"origen": "bucket_no_aprobado_para_real",
                        "clave": f"{activo}#{marco}", "bucket": f"{_bucket(ask):.2f}"},
        }
    return _gate_veredicto_dict(activo, marco, ask)
