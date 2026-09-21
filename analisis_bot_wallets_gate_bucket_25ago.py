#!/usr/bin/env python3
"""analisis_bot_wallets_gate_bucket_25ago.py — gate riguroso por micro-
bucket de precio real para bot_wallets_gate_bucket_fase0.py (P-GALLINA
FASE0), mismo mecanismo que analisis_wallet_mirror_gate_bucket_10ago.py
(P24) pero para las bot wallets en vez de Wallet Mirror.

Origen (25-Ago, petición explícita Javi: "soluciona 2" -- el hueco de
instrumentación identificado en la revisión de pendientes): `bot_wallets_
gate_bucket_fase0.py` medía fill-ability real (profundidad de libro en
el instante de detección) pero nunca PnL real, porque no había ningún
join contra el resultado oficial del mercado. Cerrado el mismo día
añadiendo `resolver_pendientes()` (reusa `outcome_por_slug()` de
wallet_mirror_tracker.py) al propio observador -- este script consume
ese resultado ya resuelto.

A diferencia de Wallet Mirror (2 ficheros a joinear por clave compuesta),
aquí todo vive en un único CSV (`bot_wallets_gate_bucket_fase0.csv`):
`lado_wallet` (lo que compró la wallet), `outcome_real` (ganador oficial),
`mejor_ask_deteccion` (ask REAL en el instante de detección -- nunca
`precio_wallet`, ya refutado como aproximación optimista el 10-Ago,
project_p24_wallet_mirror_refutado_ask_real_10ago).

Rigor idéntico al resto del proyecto: n>=15, shuffle test (bucket vs
resto del mismo grupo), split-half cronológico, BH-FDR por (arquetipo,
activo,marco). pnl_neto con la fórmula exacta (gross_win=(1-ask)/ask,
fee 7%) -- mismo criterio que gate_bucket_propio.py/wallet_mirror_gate_
bucket.py, nunca duplicar con una fórmula distinta.

Solo lectura, solo ESCRIBE data/shadow/bot_wallets_gate_bucket.json --
no toca ningún gate real, estas tuplas no están en pares_permitidos_live
(FASE 0, solo observación).

31-Ago (/code-review sesión, pendiente #3 checkpoint 31-Ago): exigir
ratio_vs_stake_deteccion>=RATIO_MIN además de mejor_ask_deteccion --
antes solo se comprobaba que hubiera UN ask capturado, sin verificar que
el libro tuviera profundidad real en ese instante (mismo hueco ya
corregido para Wallet Mirror el 10-Ago, project_p24_wallet_mirror_
refutado_ask_real_10ago, y que Sports Wallet Mirror ya evitó desde el
día 1 -- analisis_sports_wallet_mirror_gate_bucket_fino.py::RATIO_MIN).
Verificado con datos reales antes de aplicar el fix: de los 9 buckets
`bueno_confirmado` de hoy, 8/9 sobreviven con n_fillable>=15 (incluso
mejoran en varios), pero DISPERSO#SOL#15min[0.50,0.55) SE INVIERTE
(n_fillable=345, pnl_medio=-0.061€ -- selección adversa real, no ruido:
n de sobra) -- exactamente el patrón que este fix existe para cazar.
"""
import csv
import json
import math
import sys
import zlib
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

from gate_dias_independientes import robustez_dias, ENFORCE as DIAS_ENFORCE, K_MEJORES_DIAS, PISO_EUR as PISO_DIAS_EUR

from gate_confirmacion_historial import cargar_historial_previo, veredicto_con_tolerancia

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_gate_bucket_propio_28jul import (  # noqa: E402
    UMBRAL_ABSOLUTO_EUR, bootstrap_absoluto, rescatar_via_absoluta,
)
import shadow_postmortem as sp  # noqa: E402 -- reusa es_pre_twap
import ballenas_cross_check as bcc  # noqa: E402 -- refuerzo informativo, ver docstring del módulo

IN = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"
OUT = REPO / "data/shadow/bot_wallets_gate_bucket.json"
TRADES_REAL = REPO / "data/live/trades.csv"

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
ITERS = 2000
FEE = 0.07
RATIO_MIN = 5.0
F_KELLY = 0.10  # 14-Sep: mismo default que analisis_log_growth.py/gate_bucket_propio.py/
# analisis_wallet_mirror_gate_bucket_10ago.py (P28/CLAUDE.md pt.14)
# 07-Sep (vigia_bot_wallets_gate_bucket seguía colgándose con timeout=600s
# tras el fix de la sesión anterior -- root cause real: shuffle_test()
# construye una matriz (ITERS, na+nb) y hace argsort de cada fila; con
# grupos que ya llegan a n=45.927 filas (DISPERSO#BTC#5min, fase0.csv
# creciendo, mismo patrón que ya rompió calcular_params() en
# shadow_postmortem.py) eso es ~2000 x 46k = 92M elementos por bucket,
# repetido ~20 buckets x grupo -- minutos por grupo grande, sin cambiar de
# orden de magnitud el resultado (un test de permutación no necesita la
# población completa para estimar el p-valor con precisión suficiente
# para el gate BH-FDR de q=0.05). Subsample determinista (mismo rng
# seedeado por seed_key, reproducible) a MAX_N por lado antes de permutar.
MAX_N_SHUFFLE = 3000


def bucket(p):
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def pnl_neto(ask, acierto):
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE) if acierto else -1.0


def cargar_filas():
    """clave de grupo: (arquetipo, activo, marco) -> [(ts, ask, pnl, wallet), ...].
    Solo filas resueltas (outcome_real presente), con ask real capturado
    (mejor_ask_deteccion no vacío -- si _fillability_mirror falló, no hay
    ask real que usar, la fila no aporta a PnL, solo a fill-ability) Y con
    ratio_vs_stake_deteccion>=RATIO_MIN (31-Ago -- ver docstring del
    módulo: un ask capturado no implica libro con profundidad real, mismo
    hueco ya corregido para Wallet Mirror el 10-Ago)."""
    grupos = defaultdict(list)
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real"):
                continue
            ask_raw = r.get("mejor_ask_deteccion", "")
            if not ask_raw:
                continue
            try:
                ask = float(ask_raw)
            except (TypeError, ValueError):
                continue
            if not (0.0 < ask < 1.0):
                continue
            ratio_raw = r.get("ratio_vs_stake_deteccion", "")
            try:
                ratio = float(ratio_raw) if ratio_raw else None
            except (TypeError, ValueError):
                ratio = None
            if ratio is None or ratio < RATIO_MIN:
                continue
            marco = r.get("marco", "?")
            if sp.es_pre_twap(marco, r.get("timestamp_utc", "")):
                continue
            acierto = 1 if r.get("outcome_real") == r.get("lado_wallet") else 0
            pnl = pnl_neto(ask, acierto)
            clave = (r.get("arquetipo", "?"), r.get("activo", "?"), marco)
            grupos[clave].append((r["timestamp_utc"], ask, pnl, r.get("wallet", "")))
    return grupos


def shuffle_test(a, b, seed_key, iters=ITERS):
    """Mismo generador seedeado por hash estable de seed_key, mismo fix
    de no-determinismo del 20-Ago (analisis_wallet_mirror_gate_bucket_
    10ago.py) -- nunca un RNG module-level compartido entre llamadas."""
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    diff_real = a.mean() - b.mean()  # sobre la población completa, no el subsample
    if len(a) > MAX_N_SHUFFLE:
        a = rng.choice(a, size=MAX_N_SHUFFLE, replace=False)
    if len(b) > MAX_N_SHUFFLE:
        b = rng.choice(b, size=MAX_N_SHUFFLE, replace=False)
    na, nb = len(a), len(b)
    todos = np.concatenate([a, b])
    n = na + nb
    idx = rng.random((iters, n)).argsort(axis=1)
    permutado = todos[idx]
    media_a = permutado[:, :na].mean(axis=1)
    media_b = permutado[:, na:].mean(axis=1)
    diffs = media_a - media_b
    p_valor = float(np.mean(np.abs(diffs) >= abs(diff_real)))
    return float(diff_real), p_valor


def bh_fdr_signif(p_valores, q=0.05):
    n = len(p_valores)
    if n == 0:
        return set()
    orden = sorted(range(n), key=lambda i: p_valores[i])
    corte = -1
    for rank, i in enumerate(orden, start=1):
        if p_valores[i] <= (rank / n) * q:
            corte = rank
    if corte == -1:
        return set()
    return set(orden[:corte])


ESTRATEGIAS_BOT_WALLETS = ("SNIPER", "DISPERSO", "WEEKLY_TEMPRANO", "WEEKLY_TARDIO")


def _cargar_pnl_real_crudo(estrategias: tuple = ESTRATEGIAS_BOT_WALLETS) -> dict:
    """{clave_str: [(ask, pnl_neto_eur), ...]} de trades.csv REALES, SIN
    bucketizar a grid 0.05 -- para el consumidor fino (analisis_bot_
    wallets_gate_bucket_fino.py), cuyas ventanas ganadoras caen en cortes
    libres de 0.01, no en el grid fijo (14-Sep, /code-review: la versión
    bucketizada de abajo, _cargar_pnl_real_por_bucket(), solo coincide con
    ~21% de las posiciones posibles de ventana fina -- lookup exacto por
    clave '0.27' nunca encuentra nada si el bucket real es '0.25'). Filtro
    de rango [lo,hi) se aplica en el consumidor, no aquí.

    `estrategias` parametrizable (14-Sep, /code-review: analisis_
    candidata9_10_gate_bucket_26ago.py reusa esta función en vez de
    duplicarla con su propio filtro de strategy -- "nunca duplicar la
    fórmula", mismo criterio que el resto del proyecto)."""
    out = defaultdict(list)
    try:
        with open(TRADES_REAL, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                strategy = r.get("strategy") or ""
                if strategy not in estrategias:
                    continue
                if r.get("status") != "CLOSED":
                    continue
                subtype = r.get("subtype") or ""
                if "#" not in subtype:
                    continue
                try:
                    ask = float(r.get("entry_price") or "")
                    pnl = float(r.get("pnl_neto_eur") or "")
                except (TypeError, ValueError):
                    continue
                if not (0.0 < ask < 1.0):
                    continue
                out[f"{strategy}#{subtype}"].append((ask, pnl))
    except (OSError, csv.Error):
        return {}
    return dict(out)


def _cargar_pnl_real_por_bucket() -> dict:
    """{clave_str: {bucket_str: [pnl_neto_eur, ...]}} de trades.csv REALES
    (arquetipo==strategy, CLOSED) -- verdad de suelo, mismo mecanismo que
    analisis_wallet_mirror_gate_bucket_10ago.py::_cargar_pnl_real_por_bucket
    (14-Sep, petición explícita Javi: "protegida... no podemos perder
    dinero", construido junto al veto de payout asimétrico que sigue).
    A diferencia de Wallet Mirror, aquí `strategy` en trades.csv YA es el
    arquetipo (SNIPER/DISPERSO/WEEKLY_TEMPRANO/WEEKLY_TARDIO), no hace
    falta parsear `notas` para extraer tipo/grande.

    Fail-safe: fichero ausente/corrupto -> {} (ningún bucket se degrada)."""
    out = defaultdict(lambda: defaultdict(list))
    try:
        with open(TRADES_REAL, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                strategy = r.get("strategy") or ""
                if strategy not in ("SNIPER", "DISPERSO", "WEEKLY_TEMPRANO", "WEEKLY_TARDIO"):
                    continue
                if r.get("status") != "CLOSED":
                    continue
                subtype = r.get("subtype") or ""
                if "#" not in subtype:
                    continue
                try:
                    ask = float(r.get("entry_price") or "")
                    pnl = float(r.get("pnl_neto_eur") or "")
                except (TypeError, ValueError):
                    continue
                if not (0.0 < ask < 1.0):
                    continue
                clave_str = f"{strategy}#{subtype}"
                out[clave_str][f"{bucket(ask):.2f}"].append(pnl)
    except (OSError, csv.Error):
        return {}
    return {k: dict(v) for k, v in out.items()}


UMBRAL_CONCENTRACION_MAX = 0.40  # 16-Sep (subido de 0.30, decisión explícita
# Javi): el 0,30 original no venía de un consenso del proyecto (verificado
# 16-Sep -- es el ÚNICO gate con degradación automática por concentración,
# los demás como analisis_sports_wallet_mirror_concentracion.py solo
# reportan, no degradan). Cuantificado ANTES de subir: exactamente 4
# buckets con estadística limpia (g_kelly>0, shuffle_p<=0,007) liberados
# hoy -- DISPERSO#ETH#240min[0.25) n=15, DISPERSO#BTC#60min[0.10) n=34,
# SNIPER#SOL#15min[0.15) n=16, DISPERSO#DOGE#15min[0.15) n=49. Los casos
# de dominancia real de una wallet (SNIPER#XRP#5min[0.20) 65,5%,
# SNIPER#SOL#5min[0.05) 71,3%) siguen bloqueados igual a 40% -- el umbral
# sigue protegiendo justo lo que debe. Hallazgo original que motivó el
# 0,30 (15-Sep): SNIPER#XRP#5min[0.20,0.25) con 75,1% de concentración en
# una sola wallet, encontrado a mano y no por ningún mecanismo automático
# -- ese caso sigue vetado con el nuevo umbral, sin cambio.

EXECUTOR_BOT_WALLETS = REPO / "data/shadow/dispersed_bot_executor_dryrun.csv"
N_MIN_FILL = 15            # mismo mínimo que el resto del proyecto para concluir algo
UMBRAL_FILLABLE_MIN = 0.30  # mismo umbral que el precedente manual de rechazo
# (ETH#5min[0.55,0.60) descartado a mano el 13-Sep con fill-ability real
# 28,2%, ver candidata9_gate_bucket.py -- nunca inventado, es el único
# precedente cuantitativo que existía para "esto es demasiado bajo").


def _cargar_fillability_por_bucket(path, col_activo="activo", col_marco="marco",
                                    col_bucket="bucket_precio", col_fill="sigue_fillable",
                                    col_arquetipo="arquetipo", arquetipo_fijo=None):
    """{clave_str: {bucket_str: (fillable_n, fillable_ok)}} desde el propio
    EJECUTOR dry-run (decisión REAL, segunda consulta al libro tras Kelly/
    circuit-breakers -- no el observador de detección que alimenta
    cargar_filas()/eventos_candidata9()). 16-Sep, petición explícita Javi
    tras el /code-review que encontró que quitar BUCKETS_APROBADOS_REAL de
    bot_wallets_gate_bucket.py/candidata9_gate_bucket.py perdía la
    comprobación de fill-ability real que antes exigía aprobación manual
    por bucket -- este loader generaliza AUTOMÁTICAMENTE lo que gate_
    bucket_propio.py ya hace solo desde el 28-Ago (_veto_fillable()) y lo
    que Wallet Mirror ya hace solo desde el día 1 (cargar_filas() en
    analisis_wallet_mirror_gate_bucket_10ago.py solo cuenta filas con
    sigue_fillable_en_decision=='1'): aquí el pnl/g_kelly del propio gate
    viene del observador de DETECCIÓN (mucho más volumen, pero sin
    resolver fill-ability real en el instante de decisión), así que la
    fill-ability se mide aparte, sobre el ejecutor, y degrada/frena la
    promoción en _degradar() más abajo -- nunca se mezclan las dos fuentes
    en un solo cálculo de pnl.

    Fail-safe: fichero ausente/corrupto -> {} (ningún bucket tiene
    evidencia -> _degradar() lo trata como fillable_n=0, nunca como
    "aprobado por defecto")."""
    out = defaultdict(lambda: defaultdict(lambda: [0, 0]))  # [n, ok]
    try:
        with open(path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                activo = r.get(col_activo) or ""
                marco = r.get(col_marco) or ""
                b_raw = r.get(col_bucket) or ""
                fill = r.get(col_fill)
                arquetipo = arquetipo_fijo if arquetipo_fijo is not None else (r.get(col_arquetipo) or "")
                if not (arquetipo and activo and marco and b_raw) or fill not in ("0", "1"):
                    continue
                try:
                    b = bucket(float(b_raw))
                except (TypeError, ValueError):
                    continue
                clave_str = f"{arquetipo}#{activo}#{marco}"
                cont = out[clave_str][f"{b:.2f}"]
                cont[0] += 1
                cont[1] += int(fill)
    except (OSError, csv.Error):
        return {}
    return {k: {bb: tuple(v) for bb, v in vv.items()} for k, vv in out.items()}


def _degradar(veredicto_crudo, entrada, clave_str, b, pnl_real_por_bucket, fillability_por_bucket=None):
    """14-Sep: vetos de payout asimétrico (Kelly g(f=10%)<=0) y verdad-de-
    suelo (trades REALES ya negativos en este bucket exacto, n_real>=2) --
    mismo criterio EXACTO que analisis_wallet_mirror_gate_bucket_10ago.py,
    portado tal cual para que bot_wallets (SNIPER/DISPERSO/WEEKLY_*) deje
    de ser la única familia de gate sin este veto (hueco señalado en
    project_checkpoint_sesion_12sep_piso_absoluto_microbuckets). Solo
    puede DEGRADAR, nunca promover.

    15-Sep, añadido veto de concentración de wallet: si una sola wallet
    genera más del UMBRAL_CONCENTRACION_MAX de las señales del bucket, el
    "edge" puede ser el comportamiento de una wallet concreta (que puede
    dejar de operar, cambiar de patrón, o ser ruido de una sola fuente),
    no una ineficiencia sistémica del mercado -- mismo espíritu que
    analisis_sports_wallet_mirror_concentracion.py, pero aquí degrada el
    veredicto en línea en vez de solo reportarlo aparte.

    16-Sep, añadido veto de TENDENCIA RECIENTE (petición explícita Javi,
    "todo lo que nos sirva para evitar pérdidas... siempre y cuando
    cumpla con todos los criterios y el rigor"): el bootstrap CI90%
    absoluto ya exigido para "bueno_confirmado" (ver los 2 callers de
    este módulo) remuestrea sobre TODA la muestra y no detecta una
    tendencia monótona dentro de ella si la media global sigue siendo
    sólida -- caso real que lo motivó, CANDIDATA9_BOT_CONSENSO#BNB#5min
    [0.25,0.30): n=56, ci90_bootstrap_absoluto=[+0.127,+0.890] (pasaba
    limpio), pero desagregado por terciles cronológicos daba
    -0,03€/+0,55€/-0,13€ -- el último tercio (última semana) ya
    negativo, invisible al bootstrap porque los 2 tercios anteriores
    (sobre todo el primero, +1,20€) lo diluían. `entrada` trae
    "tercio3_pnl_medio"/"tercio3_n" (calculados por el caller, que tiene
    el `dentro` ordenado por tiempo -- este módulo no conoce la forma
    exacta de esas tuplas por familia, 2/3/4 elementos según el archivo)
    -- si el último tercio (n>=5) ya está por debajo de UMBRAL_ABSOLUTO_
    EUR (mismo piso que el resto del proyecto, no un umbral nuevo),
    degrada. Ausente/None (caller no lo calculó, o n<5) -> el check se
    salta sin tocar el veredicto, fail-neutral, nunca fail-open.

    16-Sep tarde, añadido veto de FILL-ABILITY REAL (petición explícita
    Javi, tras /code-review sobre la retirada de BUCKETS_APROBADOS_REAL
    de bot_wallets_gate_bucket.py/candidata9_gate_bucket.py: "esto tiene
    que ser así en todas las tuplas live... si un micro-bucket pasa a
    sin_concluir o malo_confirmado, automáticamente no se opera ahí hasta
    que revierta la situación y se vuelva a abrir automáticamente"):
    generaliza a estas 2 familias el mismo automatismo que gate_bucket_
    propio.py (_veto_fillable, 28-Ago) y Wallet Mirror (cargar_filas()
    filtrando por sigue_fillable_en_decision) ya tienen desde antes, sin
    depender de que Javi mida fill-ability a mano por bucket antes de
    aprobar. `fillability_por_bucket` viene de _cargar_fillability_por_
    bucket() sobre el propio ejecutor dry-run (decisión REAL, no el
    observador de detección) -- (a) fillable_n<N_MIN_FILL: el bucket NUNCA
    se promueve a bueno_confirmado por primera vez sin evidencia real de
    que el libro sigue operable en el instante de decisión (degrada a
    sin_concluir, no a malo_confirmado -- fail-neutral mientras se
    acumula evidencia, nunca fail-open); (b) fillable_n>=N_MIN_FILL y
    fillable_pct<UMBRAL_FILLABLE_MIN: degrada a malo_confirmado, mismo
    precedente cuantitativo que motivó el rechazo manual de ETH#5min
    [0.55,0.60) (28,2% fill-ability, ver candidata9_gate_bucket.py).
    fillability_por_bucket=None (caller no lo pasó) -> el check se salta
    sin tocar el veredicto, mismo fail-neutral que el resto de esta
    función -- nunca usado en producción sin pasarlo explícito."""
    nota_payout = ""
    g_kelly = entrada.get("g_kelly_f10")
    if veredicto_crudo == "bueno_confirmado" and g_kelly is not None and g_kelly <= 0:
        veredicto_crudo = "malo_confirmado"
        nota_payout = f" [degradado: payout asimétrico g_kelly(f=10%)={g_kelly:+.5f}<=0]"
    nota_real = ""
    pnls_reales = pnl_real_por_bucket.get(clave_str, {}).get(b)
    if veredicto_crudo == "bueno_confirmado" and pnls_reales and len(pnls_reales) >= 2:
        media_real = sum(pnls_reales) / len(pnls_reales)
        if media_real < 0:
            veredicto_crudo = "malo_confirmado"
            nota_real = f" [degradado: {len(pnls_reales)} trades REALES pnl_medio={media_real:+.3f}€<0]"
    nota_concentracion = ""
    concentracion = entrada.get("concentracion_top1_wallet")
    if veredicto_crudo == "bueno_confirmado" and concentracion is not None and concentracion > UMBRAL_CONCENTRACION_MAX:
        veredicto_crudo = "malo_confirmado"
        nota_concentracion = f" [degradado: concentración top1_wallet={concentracion:.1%}>{UMBRAL_CONCENTRACION_MAX:.0%}]"
    nota_tendencia = ""
    tercio3_n = entrada.get("tercio3_n") or 0
    tercio3_pnl = entrada.get("tercio3_pnl_medio")
    # 16-Sep tarde (petición explícita Javi, tras encontrar el umbral n>=5
    # muy por debajo del estándar del proyecto): ninguna conclusión con
    # n<15 (regla #2 del manual operativo, CLAUDE.md) -- n>=5 permitía
    # degradar un bucket con años de historial bueno por una racha de solo
    # 5 trades recientes. Subido a n>=15, mismo mínimo que shuffle/split-
    # half ya exigen en el resto del proyecto.
    if (veredicto_crudo == "bueno_confirmado" and tercio3_n >= 15
            and tercio3_pnl is not None and tercio3_pnl < UMBRAL_ABSOLUTO_EUR):
        veredicto_crudo = "malo_confirmado"
        nota_tendencia = (f" [degradado: tendencia reciente último_tercio "
                           f"n={tercio3_n} pnl_medio={tercio3_pnl:+.3f}€<{UMBRAL_ABSOLUTO_EUR}]")
    if (DIAS_ENFORCE and veredicto_crudo == "bueno_confirmado"
            and entrada.get("robusto_dias") is not True):
        veredicto_crudo = "sin_concluir"
        nota_tendencia += (f" [sin_concluir: no robusto por dias -- sin los {K_MEJORES_DIAS} mejores dias "
                           f"pnl_medio={entrada.get('pnl_sin_mejores_dias')} (<{PISO_DIAS_EUR}) "
                           f"n_dias={entrada.get('n_dias')}]")
    nota_fill = ""
    if fillability_por_bucket is not None:
        fill_n, fill_ok = fillability_por_bucket.get(clave_str, {}).get(b, (0, 0))
        entrada["fillable_n"] = fill_n
        entrada["fillable_pct"] = round(fill_ok / fill_n, 4) if fill_n else None
        if veredicto_crudo == "bueno_confirmado":
            if fill_n < N_MIN_FILL:
                veredicto_crudo = "sin_concluir"
                nota_fill = (f" [sin_concluir: fill-ability real del ejecutor n={fill_n}"
                             f"<{N_MIN_FILL}, esperando más decisiones]")
            elif fill_ok / fill_n < UMBRAL_FILLABLE_MIN:
                veredicto_crudo = "malo_confirmado"
                nota_fill = (f" [degradado: fill-ability real ejecutor {fill_ok/fill_n:.1%} "
                             f"n={fill_n}<{UMBRAL_FILLABLE_MIN:.0%}]")
    return veredicto_crudo, nota_payout, nota_real, nota_concentracion, nota_tendencia, nota_fill, g_kelly


def _cargar_historial_abs_previo(out_path):
    """12-Sep (/code-review, mismo hueco que analisis_wallet_mirror_gate_
    bucket_10ago.py): namespace INDEPENDIENTE de historial para la vía
    absoluta -- reusar historial_crudo de la vía relativa contaminaba su
    ventana de tolerancia (un malo_confirmado relativo podía "reconfirmarse"
    bueno con solo 2 días de rescate absoluto)."""
    try:
        with open(out_path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return {}
    hist = {}
    for clave_str, tabla in data.items():
        if not isinstance(tabla, dict):
            continue
        hist[clave_str] = {b: v.get("historial_crudo_abs", [])
                            for b, v in tabla.items() if isinstance(v, dict)}
    return hist


def main():
    grupos = cargar_filas()
    print(f"Grupos (arquetipo,activo,marco): {len(grupos)}")
    # 10-Sep, petición explícita Javi (SNIPER#BTC#5min[0.25,0.30] -- la
    # ÚNICA tupla de esta familia aprobada para dinero real, BUCKETS_
    # APROBADOS_REAL en bot_wallets_gate_bucket.py -- volvió a sin_concluir
    # el 09-Sep pese a +10,38€ reales en 13 trades los 2 días anteriores):
    # este generador nunca se conectó a gate_confirmacion_historial.py, a
    # diferencia de sus 6 hermanos (gate_bucket_propio, gate_bucket_fino,
    # wallet_mirror x2, sports_wallet_mirror x2) -- sin la tolerancia "2 de
    # los últimos 3 días" que rige el resto del proyecto desde el 01-Sep,
    # un solo día flojo de BH-FDR apagaba el gate en caliente aunque la
    # racha real siguiera ganando. Cron ya es diario (vigia_bot_wallets_
    # gate_bucket.py, 06:59 UTC) -- no hace falta el wrapper "_diario" que
    # sí necesitó Wallet Mirror (ese corre horario).
    historial_previo = cargar_historial_previo(OUT, anidado_por_bucket=True)
    historial_abs_previo = _cargar_historial_abs_previo(OUT)
    pnl_real_por_bucket = _cargar_pnl_real_por_bucket()
    # /code-review 16-Sep (mismo hallazgo real corregido en
    # analisis_candidata9_10_gate_bucket_26ago.py, mismo día): cargar_filas()
    # de arriba bucketiza por "mejor_ask_deteccion" (ask de NUESTRO libro en
    # el instante de detección, lo mismo que bot_wallets_gate_bucket_fase0.py
    # captura vía fill.get("mejor_ask")) -- el default de esta función
    # ("bucket_precio", columna del propio ejecutor) bucketiza en cambio por
    # el PRECIO DE TRADE de la wallet copiada, una magnitud distinta.
    # dispersed_bot_executor_dryrun.csv trae su propia columna
    # "mejor_ask_deteccion" (misma fuente conceptual, fill.get("mejor_ask")
    # de su propia consulta al libro) -- usarla alinea los dos lados.
    fillability_por_bucket = _cargar_fillability_por_bucket(
        EXECUTOR_BOT_WALLETS, col_bucket="mejor_ask_deteccion")

    resultado = {}
    pendientes = []
    candidatos_abs = []  # vía absoluta (12-Sep), ver UMBRAL_ABSOLUTO_EUR
    for clave, filas in grupos.items():
        arquetipo, activo, marco = clave
        clave_str = f"{arquetipo}#{activo}#{marco}"
        if len(filas) < N_MIN:
            # Mismo patrón que analisis_wallet_mirror_gate_bucket_10ago.py
            # (/code-review 01-Sep): no perder el historial_crudo de los
            # buckets de esta clave si hoy cae por debajo de N_MIN a nivel
            # clave -- un día flojo no es un día MALO a nivel bucket.
            historial_clave = historial_previo.get(clave_str, {})
            resultado[clave_str] = {
                b: {"veredicto": "sin_concluir", "historial_crudo": hist}
                for b, hist in historial_clave.items() if hist
            }
            continue
        por_bucket = defaultdict(list)
        for ts, ask, pnl, wallet in filas:
            por_bucket[bucket(ask)].append((ts, pnl, wallet))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b for ts, pnl, _w in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, pnl, _w in dentro]
            media_d = sum(pnl_d) / n_d
            # 15-Sep (petición explícita Javi, tras encontrar a mano
            # SNIPER#XRP#5min[0.20,0.25) con 75,1% de concentración en una
            # sola wallet -- "nadie lo habría visto sin que yo lo pidiera
            # explícitamente"): concentración automática, mismo espíritu
            # que analisis_sports_wallet_mirror_concentracion.py pero
            # calculado en línea aquí (no un script aparte) para que
            # DEGRADE el veredicto directamente, no solo lo reporte.
            _conteo_wallets = Counter(w for _, _, w in dentro if w)
            concentracion_top1 = (max(_conteo_wallets.values()) / n_d) if (_conteo_wallets and n_d) else None
            # Semilla de historial_crudo -- si este bucket no sobrevive más
            # abajo (BH-FDR/piso), esta entrada por defecto es la que queda
            # escrita, y sin la semilla perdía el historial acumulado sin
            # que hubiera pasado un día MALO (mismo motivo que la rama de
            # arriba, a nivel bucket en vez de a nivel clave).
            historial_semilla = historial_previo.get(clave_str, {}).get(f"{b:.2f}", [])
            g_kelly = sum(math.log(1 + F_KELLY * x) for x in pnl_d) / n_d if n_d > 0 else None
            # 15-Sep (petición explícita Javi, "masterizar" pt.4, "me
            # parece bien como refuerzo, pero no como veto"): cruce con
            # ballenas PURAMENTE INFORMATIVO -- `ask` aquí ya está en la
            # perspectiva de la DECISIÓN (precio del lado que la wallet
            # realmente compró, ver cargar_filas()), así que se consulta
            # como "BUY_YES" (misma convención que candidata9/wallet_
            # mirror: "apostamos a que el lado a este precio gana").
            # NUNCA afecta a veredicto/degradación.
            ballenas = bcc.consultar(activo, marco, b, "BUY_YES")
            entrada = {"n": n_d, "pnl_medio": round(media_d, 4),
                       "g_kelly_f10": round(g_kelly, 5) if g_kelly is not None else None,
                       "concentracion_top1_wallet": round(concentracion_top1, 4) if concentracion_top1 is not None else None,
                       "tercio3_n": 0, "tercio3_pnl_medio": None,
                       "ballenas_hit_rate_yes": ballenas["hit_rate_yes"], "ballenas_n": ballenas["n"],
                       "ballenas_coincide": ballenas["coincide"],
                       "shuffle_p": None, "split_half": None, "veredicto": "sin_concluir",
                       "historial_crudo": historial_semilla}
            tabla[f"{b:.2f}"] = entrada
            if n_d >= N_MIN:
                # 12-Sep (decisión explícita Javi, ver UMBRAL_ABSOLUTO_EUR
                # en analisis_gate_bucket_propio_28jul.py): vía absoluta,
                # independiente de "fuera".
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                # 21-Sep (aprobado por Javi): robustez por DIAS INDEPENDIENTES, ver
                # gate_dias_independientes.py -- solo alimenta _degradar().
                _rob = robustez_dias([(_ts, _p) for _ts, _p, _w in dentro_sorted])
                entrada["n_dias"] = _rob["n_dias"]
                entrada["pnl_sin_mejores_dias"] = _rob["pnl_sin_mejores"]
                entrada["robusto_dias"] = _rob["robusto"]
                # 16-Sep (ver docstring de _degradar() -- criterio de
                # tendencia reciente), reusa el mismo dentro_sorted de
                # arriba en vez de ordenar dos veces (16-Sep, /code-review:
                # la primera versión ordenaba SIEMPRE, incluso para buckets
                # por debajo de N_MIN que nunca pueden confirmar -- con
                # buckets de miles de filas eso duplicaba trabajo real,
                # llevó el runtime de wallet_mirror de varios minutos a
                # 28min, cerca del timeout de 2400s). n>=15 (subido de 5
                # el 16-Sep tarde, ver _degradar()) para no juzgar una
                # racha corta -- mismo mínimo que el resto del proyecto
                # exige para concluir cualquier cosa.
                _k_tend = n_d // 3
                # /code-review 16-Sep (hallazgo real): dentro_sorted[2*_k_tend:]
                # dejaba caer el resto de la división en el tercio3, ensanchando
                # la ventana "reciente" más allá de 1/3 para n no múltiplo de 3
                # (ej. n=17 -> 7 filas, 41% en vez de ~33%). Toma exactamente los
                # últimos _k_tend elementos -- el resto queda fuera de los 3
                # tercios, definición estable que no crece con el resto.
                _tercio3 = dentro_sorted[n_d - _k_tend:] if _k_tend > 0 else []
                tercio3_n = len(_tercio3)
                if tercio3_n >= 15:
                    entrada["tercio3_n"] = tercio3_n
                    entrada["tercio3_pnl_medio"] = round(sum(pnl for _, pnl, _w in _tercio3) / tercio3_n, 4)
                _, _, p_valor_abs = bootstrap_absoluto(pnl_d, seed_key=f"abs#{clave_str}#{b:.2f}")
                entrada["p_valor_abs"] = round(p_valor_abs, 4)
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                split_half_abs = None
                if len(m1) >= 5 and len(m2) >= 5:
                    m1_abs = sum(pnl for _, pnl, _w in m1) / len(m1)
                    m2_abs = sum(pnl for _, pnl, _w in m2) / len(m2)
                    split_half_abs = [round(m1_abs, 4), round(m2_abs, 4)]
                    entrada["split_half_absoluto"] = split_half_abs
                candidatos_abs.append({"clave_str": clave_str, "bucket": f"{b:.2f}",
                                        "entrada": entrada, "p_valor_abs": p_valor_abs,
                                        "split_half_abs": split_half_abs})
            if n_d >= N_MIN and fuera:
                pnl_f = [pnl for _, pnl in fuera]
                diff, p_valor = shuffle_test(pnl_d, pnl_f, seed_key=f"{clave_str}#{b:.2f}")
                entrada["shuffle_p"] = round(p_valor, 4)
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    media_fuera = sum(pnl_f) / len(pnl_f)
                    d1 = sum(pnl for _, pnl, _w in m1) / len(m1) - media_fuera
                    d2 = sum(pnl for _, pnl, _w in m2) / len(m2) - media_fuera
                    entrada["split_half"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"clave_str": clave_str, "bucket": f"{b:.2f}",
                                            "entrada": entrada, "p": p_valor, "diff": diff})
        resultado[clave_str] = tabla

    # BH-FDR por (activo,marco) -- mismo nivel de agrupación que
    # analisis_wallet_mirror_gate_bucket_10ago.py usa por (activo,marco,grande).
    por_grupo = defaultdict(list)
    for idx, p in enumerate(pendientes):
        _, activo, marco = p["clave_str"].split("#")
        por_grupo[(activo, marco)].append(idx)

    sobreviven = set()
    for grupo, indices in por_grupo.items():
        p_valores = [pendientes[i]["p"] for i in indices]
        sobreviven |= {indices[j] for j in bh_fdr_signif(p_valores, q=P_MAX)}

    veredictos_nuevos = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        if p["diff"] < 0:
            veredicto_crudo = "malo_confirmado"
        elif p["entrada"]["pnl_medio"] >= 0:
            veredicto_crudo = "bueno_confirmado"
        else:
            continue
        veredicto_crudo, nota_payout, nota_real, nota_concentracion, nota_tendencia, nota_fill, g_kelly = _degradar(
            veredicto_crudo, p["entrada"], p["clave_str"], p["bucket"], pnl_real_por_bucket,
            fillability_por_bucket)
        p["entrada"]["veredicto_crudo_hoy"] = veredicto_crudo
        # 10-Sep: 2 de los últimos 3 días (incluido hoy), asimétrico --
        # "malo_confirmado" sigue inmediato. Mismo mecanismo que el resto
        # del proyecto desde el 01-Sep, ver comentario junto a
        # historial_previo arriba.
        historial_bucket = historial_previo.get(p["clave_str"], {}).get(p["bucket"])
        veredicto, p["entrada"]["historial_crudo"] = veredicto_con_tolerancia(
            veredicto_crudo, historial_bucket)
        p["entrada"]["veredicto"] = veredicto
        if veredicto == "sin_concluir":
            continue
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        veredictos_nuevos.append(
            f"{marca} {p['clave_str']} [{p['bucket']},{float(p['bucket'])+STEP:.2f}) "
            f"n={p['entrada']['n']} pnl_medio={p['entrada']['pnl_medio']:+.3f} "
            f"g_kelly={g_kelly:+.5f} p={p['p']:.4f} {veredicto}{nota_payout}{nota_real}{nota_concentracion}{nota_tendencia}{nota_fill}"
        )

    # 12-Sep, vía absoluta (decisión explícita Javi, ver UMBRAL_ABSOLUTO_EUR
    # en analisis_gate_bucket_propio_28jul.py): rescata buckets rentables de
    # sobra que la vía relativa dejó en malo_confirmado/sin_concluir solo
    # por ser peores que un vecino de la misma tupla.
    rescatados = rescatar_via_absoluta(
        candidatos_abs, agrupador_fn=lambda clave_str: tuple(clave_str.split("#")[1:]))
    for c in rescatados:
        b = c["bucket"]
        veredicto_crudo_abs, nota_payout, nota_real, nota_concentracion, nota_tendencia, nota_fill, g_kelly = _degradar(
            "bueno_confirmado", c["entrada"], c["clave_str"], b, pnl_real_por_bucket,
            fillability_por_bucket)
        historial_bucket = historial_abs_previo.get(c["clave_str"], {}).get(b)
        veredicto, c["entrada"]["historial_crudo_abs"] = veredicto_con_tolerancia(
            veredicto_crudo_abs, historial_bucket)
        c["entrada"]["veredicto_crudo_hoy_abs"] = veredicto_crudo_abs
        if veredicto == "sin_concluir":
            # NUNCA pisa el veredicto ya decidido por la vía relativa --
            # ver comentario en _cargar_historial_abs_previo. /code-review
            # 15-Sep (aplicado primero en analisis_candidata9_10_gate_
            # bucket_26ago.py): "via" NO se marca aquí -- c["entrada"] es el
            # MISMO objeto que resultado[clave_str][b], así que fijar "via"
            # antes de este continue lo dejaba corrupto ("absoluta") incluso
            # cuando el veredicto vigente lo puso la vía relativa.
            continue
        c["entrada"]["veredicto"] = veredicto
        c["entrada"]["via"] = "absoluta"
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        veredictos_nuevos.append(
            f"{marca} [vía absoluta] {c['clave_str']} [{b},{float(b)+STEP:.2f}) "
            f"n={c['entrada']['n']} pnl_medio={c['entrada']['pnl_medio']:+.3f} "
            f"g_kelly={g_kelly:+.5f} p_abs={c['p_valor_abs']:.4f} {veredicto}{nota_payout}{nota_real}{nota_concentracion}{nota_tendencia}{nota_fill}"
        )

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
