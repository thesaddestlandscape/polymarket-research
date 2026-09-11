#!/usr/bin/env python3
"""bot_wallets_gate_bucket.py — 08-Sep, módulo LIGERO (sin dependencias
pesadas -- solo json/math/pathlib) que expone el gate de micro-bucket de
la familia P-GALLINA (DISPERSO/SNIPER/WEEKLY_TEMPRANO/WEEKLY_TARDIO,
bot_wallets_gate_bucket.json) con la MISMA firma que wallet_mirror_gate_
bucket.py/candidata9_gate_bucket.py, para poder registrarse en
live_trade.py::_GATES_EXTERNOS_POR_ESTRATEGIA sin crear un import
circular.

Por qué un módulo aparte y no seguir con la copia local que tenía
dispersed_bot_executor_dryrun.py (`_gate_veredicto()`): esa copia nunca
se consultaba en el RE-CHEQUEO post-requote de live_trade.py (solo en el
chequeo inicial, antes de la ida-y-vuelta de red a Gamma para resolver
market_id) -- mismo bug real ya encontrado y corregido para WALLET_MIRROR
(25-Ago) y CANDIDATA9_BOT_CONSENSO (08-Sep): sin esta pieza, el recheck
caía en gate_bucket_propio.py::_zonas_validadas_externamente() (zonas de
ballenas, sin ninguna relación con este gate de wallets), quedando de
hecho SIN re-verificación real justo en la ventana donde el precio puede
haberse movido.

Única fuente de verdad para el precio: bot_wallets_gate_bucket.json,
regenerado por analisis_bot_wallets_gate_bucket_25ago.py (cron/vigía ya
existente, vigia_bot_wallets_gate_bucket.py). Este módulo solo LEE --
nunca escribe, nunca decide qué es bueno_confirmado estadísticamente,
solo expone el veredicto ya calculado con la firma que live_trade.py
espera.

`evaluar()` es la fuente ÚNICA y SIN restringir (dry-run/observacional
sigue trackeando TODO el universo, decisión explícita de Javi 26-Ago:
"así tenemos datos de todo ya" -- no filtrar aquí).

`permitido_real()` es una capa DISTINTA y ADICIONAL: la lista explícita
de (arquetipo,activo,marco,bucket) que Javi ha aprobado para DINERO
REAL -- el gate estadístico puede confirmar un bucket (ej. SNIPER#BTC#
5min[0.05,0.10), n=124, pnl+0.547€) que aun así NO se manda a producción
porque su Kelly de crecimiento logarítmico es negativo (g(f=10%)=-0.00426,
"payout inverso", mismo patrón ya documentado en FAVORITO_CONFIRMADO#
BUY_NO) -- aprobar por tupla+dirección sin filtrar por bucket habría
activado ese bucket también, sin que nadie lo decidiera explícitamente.
Cada entrada nueva aquí exige aprobación explícita de Javi, con motivo y
fecha -- igual que pares_permitidos_live, pero a nivel de micro-bucket
porque este gate no separa por bucket en la whitelist genérica.
"""
import json
import math
from pathlib import Path

REPO = Path(__file__).resolve().parent
GATE_PATH = REPO / "data" / "shadow" / "bot_wallets_gate_bucket.json"
GATE_STEP = 0.05

_gate_cache: dict = {"mtime": None, "datos": {}}

# 08-Sep, aprobación explícita Javi (sesión de cierre de Stage 0): SOLO
# este bucket exacto -- gate n=344, pnl/tr=+0.197€, p_shuffle=0.0005,
# g_kelly(f=10%)=+0.00704, fill-ability 58.2%, checklist de 6 categorías
# completado 07-Sep, estable 2/2 lecturas diarias sin revertir (07 y
# 08-Sep). NO incluye SNIPER#BTC#5min[0.05,0.10) pese a estar también
# bueno_confirmado -- ese bucket tiene g_kelly NEGATIVO (-0.00426,
# payout inverso), no aprobado.
# ⚠️ 09-Sep: este bucket volvió a `sin_concluir` en caliente (n=389,
# BH-FDR de un solo día flojo) pese a +10,38€ reales en 13 trades los 2
# días previos -- permitido_real() bloqueó correctamente (fail-closed),
# pero motivó el fix de tolerancia diaria (10-Sep, commit c53354b402):
# este generador no tenía la protección "2 de los últimos 3 días" que sí
# tienen sus 6 hermanos desde el 01-Sep. Activo de nuevo desde ese fix.
#
# 10-Sep, aprobación explícita Javi (checklist completo sobre las 3
# candidatas que ya pasaban el gate estadístico n>=40): DISPERSO#BTC#
# 15min[0.75,0.80) -- gate n=551, pnl/tr=+0.067€, p=0.007, g_kelly(f=10%)
# =+0.00546, fill-ability real 62.5% (dry-run n=3115, dispararía=1948),
# concentración SANA (29 wallets, top1=12.9%; 502 mercados, top1=0.8%),
# 3 de los últimos 4 días reales `bueno_confirmado` con n creciendo de
# verdad (47->551, no estancado). La candidata más limpia de la ronda.
# Descartadas la misma sesión: SNIPER#BTC#15min[0.10,0.15) (concentración
# 36.7% en solo 15 wallets, por encima del umbral de alarma 30% -- se
# deja observando) y SNIPER#XRP#5min[0.20,0.25) (concentración 73.4% en
# 4 wallets, la dominante fichada en smart_money_wallets.json con
# win_rate=0.0 y pnl_total=-15.214€ -- lo contrario de una wallet
# informada, n congelado 3 días seguidos porque esa wallet dejó de
# operar ahí -- ver idea_sniper_xrp5min_concentracion_wallet_perdedora_10sep).
BUCKETS_APROBADOS_REAL = {
    ("SNIPER", "BTC", "5min"): {0.25},
    ("DISPERSO", "BTC", "15min"): {0.75},
}


def _bucket(precio: float) -> float:
    return round(math.floor(precio / GATE_STEP + 1e-9) * GATE_STEP, 4)


def _gate_veredicto_dict(arquetipo: str, activo: str, marco: str, precio: float) -> dict:
    """Consulta EN CALIENTE bot_wallets_gate_bucket.json -- única fuente
    de verdad, autoaprendiente (mismo patrón que gate_bucket_propio.py en
    cripto). Cachea por mtime, no relee el fichero en cada llamada.
    Fail-closed: sin fichero/clave/bucket -> {"veredicto": "sin_concluir"},
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
    clave = f"{arquetipo}#{activo}#{marco}"
    tabla = _gate_cache["datos"].get(clave)
    if not tabla:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "sin_clave", "clave": clave}}
    bucket_key = f"{_bucket(precio):.2f}"
    info = tabla.get(bucket_key)
    if not info:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "sin_bucket", "bucket": bucket_key}}
    return info


def evaluar(arquetipo: str, activo: str, marco: str, precio: float) -> dict:
    """Alias directo SIN restringir por aprobación real -- para
    dispersed_bot_executor_dryrun.py (accumulación/tracking del universo
    completo, decisión Javi 26-Ago) y para el propio vigía diario."""
    return _gate_veredicto_dict(arquetipo, activo, marco, precio)


def permitido_real(arquetipo: str, activo: str, marco: str, precio: float) -> bool:
    """Capa adicional de aprobación explícita por micro-bucket para
    DINERO REAL -- exige (a) el bucket exacto en BUCKETS_APROBADOS_REAL
    Y (b) el gate estadístico siga bueno_confirmado en caliente (el
    autoaprendizaje puede retirar la confirmación con más datos, en cuyo
    caso deja de operar aunque siga en la lista de aprobados)."""
    clave = (arquetipo, activo, marco)
    aprobados = BUCKETS_APROBADOS_REAL.get(clave)
    if not aprobados or _bucket(precio) not in aprobados:
        return False
    return _gate_veredicto_dict(arquetipo, activo, marco, precio).get("veredicto") == "bueno_confirmado"


def evaluar_para_recheck(subtype: str, direction: str, py: float, contexto: dict) -> dict:
    """Firma uniforme que live_trade.py::_ejecutar_orden_polymarket usa en
    el re-chequeo post-requote y en el multi-lectura de justo antes de
    firmar (registrado en _GATES_EXTERNOS_POR_ESTRATEGIA) -- mismo patrón
    que wallet_mirror_gate_bucket.py::evaluar_para_recheck. `arquetipo`
    llega en contexto["strategy"] (dispersed_bot_executor_dryrun.py lo
    pasa así). `py` llega en perspectiva YES -- se convierte al precio
    del lado que de verdad estamos comprando. Aplica SIEMPRE la capa de
    aprobación explícita por micro-bucket (permitido_real) -- este gate,
    a diferencia de wallet_mirror_gate_bucket.py, no separa la whitelist
    por bucket, así que la restricción tiene que vivir aquí para cubrir
    tanto el chequeo inicial como el recheck con una sola fuente."""
    arquetipo = contexto.get("strategy", "")
    partes = subtype.split("#")
    if not arquetipo or len(partes) != 2:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "contexto_invalido"}}
    activo, marco = partes
    ask = py if direction == "BUY_YES" else round(1.0 - py, 6)
    if not permitido_real(arquetipo, activo, marco, ask):
        return {
            "veredicto": "malo_confirmado",
            "detalle": {"origen": "bucket_no_aprobado_para_real",
                        "clave": f"{arquetipo}#{activo}#{marco}",
                        "bucket": f"{_bucket(ask):.2f}"},
        }
    return _gate_veredicto_dict(arquetipo, activo, marco, ask)
