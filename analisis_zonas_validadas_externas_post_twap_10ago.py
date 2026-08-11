#!/usr/bin/env python3
"""analisis_zonas_validadas_externas_post_twap_10ago.py — regenera
data/shadow/zonas_validadas_externas.json, la semilla externa de
gate_bucket_propio.py::_ZONAS_VALIDADAS_EXTERNAMENTE, usando SOLO datos
post-TWAP (07-Ago en adelante) de ballenas_timing_history.csv.

Origen (10-Ago, petición explícita Javi tras el diagnóstico de por qué
BALLENAS_TARDIAS#ETH#5min y FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC
#15min llevaban desde el 09-Ago con el override de emergencia puesto):
la semilla externa original (05-Ago) se retiró el 09-Ago porque se basaba
en `ballenas_timing_history.csv` PRE-TWAP -- pero el fichero sigue
creciendo cada día con datos NUEVOS, post-TWAP, y ya acumula miles de
observaciones por zona (n=2500-14700 según zona) -- mucho más rápido que
esperar a que las 2 tuplas acumulen su propio n en results.csv (que
habría tardado meses en el caso más ajustado, ver
project_stage0_redefinido_diagnostico_completo_10ago).

Rigor por zona (bucket 0.05, mismo step que gate_bucket_propio.py):
  1. n >= N_MIN (15, mínimo CLAUDE.md -- en la práctica todas las zonas
     activas tienen n en miles, muy por encima)
  2. Wilson90 lower bound del hit-rate > breakeven implícito por el
     precio medio real de la zona + fee 7% real (gross_win=(1-p)/p,
     NUNCA (1-p) -- fórmula exacta del proyecto)
  3. Concentración: ningún mercado (condition_id) puede superar el 30%
     de las observaciones de la zona (mismo umbral que analisis_franja_
     milimetrica_ballenas.py usa para huecos de cobertura) -- evita que
     un solo evento amplificado por muchas wallets infle el n
  4. Split-half cronológico: el signo de (wilson90lo - breakeven) debe
     repetirse en ambas mitades temporales del periodo post-TWAP

SOLO promueve a "bueno_confirmado" -- nunca "malo_confirmado" (la
semilla externa, por diseño de gate_bucket_propio.py, únicamente
PROMUEVE mientras el dato propio siga sin_concluir, nunca sustituye un
veredicto propio ya confirmado ni añade vetos nuevos).

Solo lectura de ballenas_timing_history.csv -- solo ESCRIBE
data/shadow/zonas_validadas_externas.json. No toca gate_bucket_propio.py
ni ningún override -- la conexión final (leer este JSON en vez del
diccionario hardcodeado) y la retirada del override son decisiones
separadas, explícitas, después de revisar este resultado.
"""
import csv
import json
import math
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
BALLENAS_HIST = REPO / "data/shadow/ballenas_timing_history.csv"
OUT = REPO / "data/shadow/zonas_validadas_externas.json"
HISTORIAL = REPO / "data/shadow/zonas_validadas_externas_historial.json"

FECHA_CAMBIO_TWAP = datetime(2026, 8, 7, tzinfo=timezone.utc)
STEP = 0.05
N_MIN = 15
FEE = 0.07
Z_90 = 1.645
TOP1_MAX_PCT = 30.0
# 10-Ago (petición explícita Javi, tras ver zonas cambiar por completo en
# horas -- SOL#5min pasó de [0.60,0.65) a [0.85,0.90), rango distinto, no
# expansión, solo por acumular más horas de datos): "pasa" el gate
# estadístico no basta, hace falta que se SOSTENGA en el tiempo antes de
# confiar en una zona con dinero real. ESTABILIDAD_MIN_HORAS exige que
# haya al menos una regeneración de hace >= ese margen que YA diera
# "pasa" para esa zona exacta, Y que NINGUNA regeneración desde entonces
# haya fallado -- un solo fallo intermedio reinicia el contador (fail-
# closed, no basta con "pasó alguna vez hace tiempo").
# 10-Ago, decisión explícita de Javi: arrancar bajo (cubierto por el
# historial real ya disponible desde que se construyó este mecanismo hoy,
# ~16:21 UTC) para no dejar sin zona confirmada a las 2 tuplas YA LIVE
# mientras se acumula historial de verdad -- subir gradualmente (6h, 12h,
# 18h) en las próximas sesiones conforme crezca el historial real. Ver
# project_extension_buyno_zonas_externas_10ago (memoria) para el porqué.
ESTABILIDAD_MIN_HORAS = 4
# 10-Ago (/code-review, hallazgo real): el corte FECHA_CAMBIO_TWAP se
# aplicaba sin condición a TODOS los marcos, incluido 60m -- pero el
# cambio de resolución (snapshot->TWAP Chainlink) solo afectó a 5min/
# 15min/240min (mismo criterio ya usado en live_trade.py::CLV_MARCOS_
# TWAP_AFECTADOS/gate_bucket_propio.py -- 60min queda fuera). Aplicar el
# corte a 60m descartaba datos pre-07-Ago perfectamente válidos sin
# ninguna razón (menos n, split-half más débil, sin motivo real).
MARCOS_TWAP_AFECTADOS = {"5m", "15m", "240m"}

# 11-Ago (petición explícita Javi, "vamos con la extensión del twap a
# más candidatos_evaluacion_live"): en vez de mantener una lista estática
# de tuplas objetivo, se generan TODAS las de config_live.json
# (pares_permitidos_live + candidatos_evaluacion_live, ~335) agrupadas
# por (activo, marco ballenas, dirección) -- la validación externa NUNCA
# depende de qué estrategia nuestra generó la señal (cargar() filtra por
# activo/marco/compro_yes, nunca por strategy, hallazgo ya confirmado
# hoy: BALLENAS_TARDIAS#BTC#15min y FAVORITO_CONFIRMADO_15MIN_
# ALTACONVICCION#BTC#15min comparten EXACTAMENTE el mismo detalle_por_
# bucket). Agrupar evita recalcular el mismo (activo,marco,dirección)
# decenas de veces (GBM_LATE_15M/_TARDIO/_ESPACIO_ATR/_PYCONFIRMADO/
# _MULTIHORIZONTE#BTC#15min#BUY_YES son 5 tuplas, 1 solo grupo real) y
# hace que el historial de estabilidad sea compartido entre todas las
# estrategias del mismo grupo en vez de fragmentado por tupla (lo que
# ya venía pasando de facto en los 10-Ago, solo que duplicado). Marcos
# fuera de MARCO_BALLENAS_MAP (daily/atexpiry/reach/sniper/weekly) no
# tienen ballenas_timing_history.csv en esa convención -- se excluyen,
# no hay dato con que validarlos por esta vía.
# 11-Ago (/code-review): copia local, NO import de live_trade.py -- ese
# módulo trae credenciales/cliente CLOB al importarlo (ya lo hacen los
# ejecutores, que sí lo necesitan; este script es análisis puro, acoplarlo
# a live_trade.py solo por este dict es peor que la duplicación). Debe
# coincidir SIEMPRE con live_trade.py::_MARCO_BALLENAS_MAP (fuente
# canónica, incluye 240min) -- shadow_predict.py tiene una 3ª copia con
# "weekly" añadido, no aplica aquí (esta fuente no cubre weekly).
MARCO_BALLENAS_MAP = {"5min": "5m", "15min": "15m", "60min": "60m", "240min": "240m"}
CONFIG_LIVE = REPO / "data/live/config_live.json"


def _grupos_desde_config() -> dict:
    """{(activo, marco_ballenas, direccion): [tupla_str, ...]} a partir de
    pares_permitidos_live + candidatos_evaluacion_live. Tuplas con formato
    inesperado (no STRATEGY#ACTIVO#MARCO#DIRECCION) o marco/dirección no
    reconocidos se ignoran silenciosamente (p.ej. SMART_FLOW_1H#BTC#BUY_YES,
    3 partes, o WEEKLY_PRICE#BTC#BUY_NO, sin marco -- no hay ballenas_
    timing_history en esa convención para validarlas por esta vía)."""
    cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
    # 11-Ago (/code-review, hallazgo real): dict.fromkeys en vez de
    # list()+concat -- una tupla presente en AMBAS listas (ya pasó con
    # FAVORITO_CONFIRMADO#BTC#60min#BUY_NO y FAVORITO_CONFIRMADO_15MIN_
    # ALTACONVICCION#BTC#15min#BUY_YES, promocionadas a pares_permitidos_
    # live sin retirarlas de candidatos_evaluacion_live) se colaba 2 veces
    # en tuplas_grupo, corrompiendo cualquier conteo de tuplas por grupo.
    todas = dict.fromkeys(cfg.get("pares_permitidos_live", []) + cfg.get("candidatos_evaluacion_live", []))
    grupos: dict = {}
    for tupla_str in todas:
        partes = tupla_str.split("#")
        if len(partes) != 4:
            continue
        _strategy, activo, marco, direccion = partes
        marco_b = MARCO_BALLENAS_MAP.get(marco)
        if marco_b is None or direccion not in ("BUY_YES", "BUY_NO"):
            continue
        grupos.setdefault((activo, marco_b, direccion), []).append(tupla_str)
    return grupos


# Lista estática histórica (10-Ago) -- ya no se usa en main(), se deja
# solo como referencia de las tuplas live/prioritarias originales.
OBJETIVO = [
    ("BALLENAS_TARDIAS#BNB#5min#BUY_YES", "BNB", "5m"),
    ("BALLENAS_TARDIAS#BTC#15min#BUY_YES", "BTC", "15m"),
    ("BALLENAS_TARDIAS#DOGE#5min#BUY_YES", "DOGE", "5m"),
    ("BALLENAS_TARDIAS#ETH#5min#BUY_YES", "ETH", "5m"),
    ("BALLENAS_TARDIAS#SOL#5min#BUY_YES", "SOL", "5m"),
    ("BALLENAS_TARDIAS#XRP#5min#BUY_YES", "XRP", "5m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min#BUY_YES", "BNB", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min#BUY_YES", "BTC", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min#BUY_YES", "DOGE", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min#BUY_YES", "ETH", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min#BUY_YES", "SOL", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min#BUY_YES", "XRP", "15m"),
    # 10-Ago: primera tupla BUY_NO -- LIVE, dinero real, prioridad #1 del
    # criterio de orden (gate_bucket_propio propio: 0/7 buckets
    # confirmados hoy pese a n=250 en un bucket, ver idea_criterio_orden_
    # extension_twap_10ago). Requiere el fix de conversión de precio en
    # cargar()/breakeven() de arriba -- verificado ANTES de añadir esta
    # línea, no se puede simplemente copiar el patrón BUY_YES.
    ("FAVORITO_CONFIRMADO#BTC#60min#BUY_NO", "BTC", "60m"),
    # 11-Ago: la validación externa depende SOLO de (activo,marco,lado
    # comprado) -- ballenas_timing_history.csv no sabe ni le importa qué
    # estrategia nuestra generó la señal (cargar() filtra por activo/
    # marco/compro_yes, nunca por strategy). Las zonas de SOL/ETH#15min
    # BUY_YES ya confirmadas arriba bajo el label ALTACONVICCION aplican
    # IGUAL a cualquier otra estrategia que compre YES ahí -- lo que
    # faltaba comprobar de verdad eran los combos NUNCA evaluados por
    # NINGÚN label: 60min#BUY_YES (petición explícita Javi, "lo tienes
    # todo ya para sacar las zonas buenas post twap, hay millones de
    # datos" -- tenía razón, solo faltaba correr el mismo mecanismo aquí).
    ("FAVORITO_CONFIRMADO#BTC#60min#BUY_YES", "BTC", "60m"),
    ("FAVORITO_CONFIRMADO#SOL#60min#BUY_YES", "SOL", "60m"),
]


def bucket(p):
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def wilson_lower(hits, n, z=Z_90):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def breakeven(py_medio, decision="BUY_YES"):
    """py_medio SIEMPRE en convención "precio YES crudo" -- misma que usa
    gate_bucket_propio.evaluar()/shadow_predict.py en runtime para tuplas
    BUY_NO (bucket_bp = _gate_bucket_propio(tupla_str, py) con py =
    market["_precio_yes"] SIN convertir, ver s_favorito_confirmado y
    s_weekly_price -- confirmado leyendo el código real, no asumido).

    10-Ago: `decision` nuevo -- para BUY_NO, el lado que de verdad
    mantenemos es NO al precio (1-py_medio), así que el breakeven real
    hay que calcularlo sobre ESE precio, no sobre py_medio directo (que
    daría el breakeven de la posición YES equivocada).

    10-Ago (/code-review): valida `decision` explícitamente -- antes
    cualquier valor que no fuera exactamente "BUY_NO" caía silenciosamente
    en la rama BUY_YES (typo, mayúscula distinta, dirección nueva sin
    actualizar aquí), produciendo una zona confirmada equivocada sin que
    nada avisara. Mejor fallar fuerte que servir un breakeven erróneo
    para dinero real."""
    if decision not in ("BUY_YES", "BUY_NO"):
        raise ValueError(f"decision desconocida: {decision!r} (solo BUY_YES/BUY_NO)")
    p_held = (1 - py_medio) if decision == "BUY_NO" else py_medio
    gross_win = (1 - p_held) / p_held
    return 1 / (1 + gross_win * (1 - FEE))


def cargar(activo, marco, compro_yes="1", hasta: datetime | None = None):
    """marco en convención ballenas ("5m"/"15m"/"60m"/"240m"). compro_yes
    filtra el LADO comprado -- 10-Ago, fix real cazado por
    /code-review: `precio` en ballenas_timing_history.csv es el precio SIN
    CONVERTIR del lado que compró esa wallet (ballenas_observer.py::precio
    = t["price"] crudo de la API). Un compro_yes=0 a precio=0.55 significa
    "pagó 0.55 por NO" (probabilidad YES implícita ~0.45), NO es el mismo
    bucket de precio que un compro_yes=1 a precio=0.55.

    10-Ago (extensión a BUY_NO, FAVORITO_CONFIRMADO#BTC#60min): cuando
    compro_yes="0" se CONVIERTE aquí mismo a precio YES equivalente
    (p = 1 - precio_NO) antes de bucketear -- así el bucket queda en la
    MISMA convención que usa gate_bucket_propio.evaluar() en runtime
    (py crudo, sin convertir, incluso para tuplas BUY_NO -- ver
    breakeven() arriba). Sin esta conversión, una tupla BUY_NO quedaría
    bucketeada por precio NO mientras el ejecutor real consulta por
    precio YES -- las zonas no emparejarían nunca, bug silencioso.

    11-Ago: `hasta` (opcional) filtra `ts_trade <= hasta` -- permite
    reconstruir qué habría visto una regeneración en un instante pasado,
    usando SOLO datos que ya existían entonces (backfill del historial
    de estabilidad con datos reales, no fabricados -- ver
    backfill_historial_zonas_externas_11ago.py). None = sin corte,
    comportamiento idéntico al de antes de este parámetro."""
    por_bucket = defaultdict(list)
    with open(BALLENAS_HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("activo") != activo or row.get("marco") != marco:
                continue
            if row.get("compro_yes") != compro_yes:
                continue
            try:
                p = float(row["precio"])
                ac = int(row["acierto"])
            except (TypeError, ValueError):
                continue
            if compro_yes == "0":
                p = 1 - p
            try:
                ts = datetime.fromisoformat(row["ts_trade"])
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
            except Exception:
                continue
            if marco in MARCOS_TWAP_AFECTADOS and ts < FECHA_CAMBIO_TWAP:
                continue
            if hasta is not None and ts > hasta:
                continue
            b = bucket(p)
            por_bucket[b].append((ts, p, ac, row.get("condition_id", "")))
    return por_bucket


def evaluar_zona(filas, decision="BUY_YES"):
    n = len(filas)
    if n < N_MIN:
        return None
    py_medio = sum(p for _, p, _, _ in filas) / n
    hits = sum(ac for _, _, ac, _ in filas)
    hit = hits / n
    wlo = wilson_lower(hits, n)
    be = breakeven(py_medio, decision)

    from collections import Counter
    c_mkt = Counter(cid for _, _, _, cid in filas)
    top1_pct = (c_mkt.most_common(1)[0][1] / n * 100) if c_mkt else 100.0

    filas_ordenadas = sorted(filas, key=lambda x: x[0])
    mid = n // 2
    m1, m2 = filas_ordenadas[:mid], filas_ordenadas[mid:]
    if len(m1) < 5 or len(m2) < 5:
        split_ok = False
        wlo1 = wlo2 = None
    else:
        hits1 = sum(ac for _, _, ac, _ in m1)
        hits2 = sum(ac for _, _, ac, _ in m2)
        py1 = sum(p for _, p, _, _ in m1) / len(m1)
        py2 = sum(p for _, p, _, _ in m2) / len(m2)
        wlo1 = wilson_lower(hits1, len(m1))
        wlo2 = wilson_lower(hits2, len(m2))
        be1, be2 = breakeven(py1, decision), breakeven(py2, decision)
        split_ok = (wlo1 > be1) and (wlo2 > be2)

    return {
        "n": n, "py_medio": round(py_medio, 4), "hit": round(hit, 4),
        "wilson90lo": round(wlo, 4), "breakeven": round(be, 4),
        "margen_pp": round((wlo - be) * 100, 2),
        "n_mercados": len(c_mkt), "top1_pct": round(top1_pct, 1),
        "split_half_ok": split_ok,
        "pasa": bool(wlo > be and top1_pct <= TOP1_MAX_PCT and split_ok),
    }


def _cargar_historial() -> dict:
    try:
        return json.loads(HISTORIAL.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _actualizar_historial(historial: dict, tupla_str: str, bucket_key: str, pasa: bool, ahora: datetime,
                           max_entradas: int = 60) -> list:
    """Añade la observación de HOY al historial de esa (tupla,bucket) y
    devuelve la lista actualizada (recortada a max_entradas, ~2 meses a
    cadencia diaria -- de sobra para juzgar estabilidad sin crecer sin
    límite)."""
    clave = f"{tupla_str}#{bucket_key}"
    entradas = historial.get(clave, [])
    entradas.append({"ts": ahora.isoformat(timespec="seconds"), "pasa": pasa})
    entradas = entradas[-max_entradas:]
    historial[clave] = entradas
    return entradas


def _es_estable(entradas: list, ahora: datetime) -> bool:
    """True solo si HOY pasa Y hay al menos una observación de hace
    >=ESTABILIDAD_MIN_HORAS que TAMBIÉN pasó, sin ningún fallo intermedio
    entre esa observación antigua y ahora -- un solo fallo reinicia el
    contador (fail-closed). Con una sola observación (primera vez que se
    corre para esa zona) nunca es estable, por diseño: hace falta ver la
    zona sobrevivir al menos una regeneración futura antes de confiar en
    ella con dinero real."""
    if not entradas or not entradas[-1]["pasa"]:
        return False
    corte = ahora - timedelta(hours=ESTABILIDAD_MIN_HORAS)
    anteriores_validas = [i for i, e in enumerate(entradas)
                           if datetime.fromisoformat(e["ts"]) <= corte]
    if not anteriores_validas:
        return False
    idx = anteriores_validas[-1]
    ventana = entradas[idx:]
    return all(e["pasa"] for e in ventana)


def main():
    ahora = datetime.now(timezone.utc)
    historial = _cargar_historial()
    resultado = {}
    grupos = _grupos_desde_config()
    print(f"{len(grupos)} grupos (activo,marco,dirección) únicos, cubriendo "
          f"{sum(len(v) for v in grupos.values())} tuplas de config_live.json")

    n_grupos_con_zona = 0
    for (activo, marco, direccion), tuplas_del_grupo in sorted(grupos.items()):
        grupo_key = f"{activo}|{marco}|{direccion}"
        compro_yes = "1" if direccion == "BUY_YES" else "0"
        por_bucket = cargar(activo, marco, compro_yes=compro_yes)
        zonas_confirmadas = []
        detalle = {}
        for b in sorted(por_bucket):
            info = evaluar_zona(por_bucket[b], decision=direccion)
            if info is None:
                continue
            b_key = f"{b:.2f}"
            entradas = _actualizar_historial(historial, grupo_key, b_key, info["pasa"], ahora)
            estable = _es_estable(entradas, ahora)
            info["estable"] = estable
            info["n_observaciones_historial"] = len(entradas)
            detalle[b_key] = info
            if estable:
                zonas_confirmadas.append([b, round(b + STEP, 2)])
        salida_grupo = {
            "zonas_bueno_confirmado": zonas_confirmadas,
            "detalle_por_bucket": detalle,
            "fuente": "ballenas_timing_history.csv post-07-Ago (TWAP-safe)",
            "regenerado_utc": ahora.isoformat(timespec="seconds"),
            "tuplas_grupo": sorted(tuplas_del_grupo),
        }
        for tupla_str in tuplas_del_grupo:
            resultado[tupla_str] = salida_grupo
        print(f"\n=== {activo}#{marco}#{direccion} ({len(tuplas_del_grupo)} tuplas) ===")
        if zonas_confirmadas:
            n_grupos_con_zona += 1
            for b, hi in zonas_confirmadas:
                info = detalle[f"{b:.2f}"]
                print(f"  🟢 [{b:.2f},{hi:.2f}) n={info['n']} hit={info['hit']*100:.1f}% "
                      f"wilson90lo={info['wilson90lo']*100:.1f}% breakeven={info['breakeven']*100:.1f}% "
                      f"margen={info['margen_pp']:+.1f}pp mercados={info['n_mercados']} top1={info['top1_pct']:.1f}% "
                      f"estable=True (n_hist={info['n_observaciones_historial']})")
        # 11-Ago (/code-review, hallazgo real): el print por grupo se
        # había quedado silencioso cuando no había zona confirmada -- un
        # operador leyendo logs/vigia_zonas_validadas_externas.log ya no
        # podía distinguir "grupo evaluado, sin zona todavía" de "grupo
        # sin datos suficientes" ni ver qué buckets pasan el gate crudo
        # pero siguen esperando la ventana de estabilidad (visibilidad
        # que sí tenía la versión por-tupla original).
        pasa_pero_no_estable = [b for b, i in detalle.items() if i["pasa"] and not i["estable"]]
        if pasa_pero_no_estable:
            print(f"  ⏳ pasa el gate pero AÚN no estable (esperando >= {ESTABILIDAD_MIN_HORAS}h sin fallar): "
                  f"{sorted(pasa_pero_no_estable)}")
        if not zonas_confirmadas and not pasa_pero_no_estable:
            print("  (ninguna zona con margen positivo hoy)" if detalle else "  (sin datos -- n<15 en todos los buckets)")

    print(f"\n{n_grupos_con_zona}/{len(grupos)} grupos con al menos una zona estable confirmada")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    HISTORIAL.write_text(json.dumps(historial, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT}")
    print(f"Historial actualizado en {HISTORIAL}")


if __name__ == "__main__":
    main()
