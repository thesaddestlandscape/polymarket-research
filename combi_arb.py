"""
combi_arb.py — Arbitraje Combinatorio en Polymarket (SOLO OBSERVACIÓN).

Detecta dos tipos de dependencias lógicas entre mercados:

  FAST PATH — Cadenas de monotonicidad (sin LLM, instantáneo):
    "Will Bitcoin reach $65k" vs "reach $70k" — mismo evento, umbral distinto.
    P(reach $65k) ≥ P(reach $70k) SIEMPRE. Violación → arb garantizado.

  LLM PATH — Dependencias arbitrarias (Claude API, ~100 pares/día):
    Pares mismo-fecha, mismo-topic → Claude detecta implicaciones lógicas.
    "Token X lanza antes de Sep30" → "Token X lanza antes de Dic31" (implicación).

Basado en: arXiv 2508.03474 "Combinatorial Arbitrage in Prediction Markets"

NO ejecuta trades. Requiere ANTHROPIC_API_KEY para LLM path.
Output: data/shadow/combi_arb_YYYY-MM-DD.csv
"""
import csv
import json
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------
DIR_SHADOW   = Path("data/shadow")
DIR_MARKETS  = Path("data/markets")
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

MIN_LIQ      = 5_000   # liquidez mínima USD por mercado
PRICE_LO     = 0.04    # filtrar mercados ya casi resueltos
PRICE_HI     = 0.96
MIN_PROFIT   = 0.005   # 0.5% mínimo para reportar (neto de fees)
POLY_FEE     = 0.02    # fee Polymarket 2%
MAX_LLM_PARES = 60     # máx pares a enviar al LLM por run (costo API)

# Regex para extraer umbrales monetarios del título.
# El sufijo [BMK] requiere lookahead negativo para no capturar "B" de "by", etc.
# re.I para aceptar "$150k"/"$1b" en minúscula (_parse_umbral ya hace .upper()
# antes de mirar _SUFIJO, verificado 2026-07-01 — sin el flag, "150k"/"1b" se
# interpretaban como umbral sin multiplicador, ej. $150 en vez de $150,000).
_RE_UMBRAL = re.compile(
    r'\$([\d,]+(?:\.\d+)?)\s*([BMK](?=[^a-zA-Z]|$))?', re.I
)
# Sufijos a multiplicadores (mayúsculas; la "b" de "by" no pasa el lookahead)
_SUFIJO = {"B": 1e9, "M": 1e6, "K": 1e3, "": 1.0}

# Palabras clave por topic para clustering sin embeddings
_TOPICS = {
    "crypto":    ["bitcoin", "btc", "ethereum", "eth", "solana", "sol", "bnb",
                  "xrp", "crypto", "defi", "nft", "token", "fdv", "airdrop",
                  "blockchain", "layer", "chain", "stablecoin", "usdc", "usdt"],
    "politics":  ["president", "election", "senate", "congress", "vote", "trump",
                  "biden", "democrat", "republican", "government", "policy", "law",
                  "fed", "powell", "nato", "war", "ukraine", "russia", "china"],
    "sports":    ["win", "champion", "nba", "nfl", "soccer", "football", "baseball",
                  "tennis", "ufc", "fight", "league", "playoff", "tournament",
                  "goal", "score", "team", "match", "game"],
    "economics": ["gdp", "inflation", "recession", "interest", "rate", "fed", "cpi",
                  "unemployment", "market", "stock", "s&p", "nasdaq", "dow", "ipo",
                  "merger", "acquire", "company", "revenue", "profit"],
    "science":   ["ai", "chatgpt", "openai", "anthropic", "model", "launch",
                  "nasa", "space", "rocket", "tech", "software", "release", "update"],
    "other":     [],
}


# ---------------------------------------------------------------------------
# Carga y deduplicación de mercados
# ---------------------------------------------------------------------------

def cargar_mercados() -> list[dict]:
    import glob as _glob
    archivos = sorted(_glob.glob(str(DIR_MARKETS / "*.csv")))
    if not archivos:
        return []

    # Deduplicar por market_id → quedarse con el snapshot más reciente
    last: dict[str, dict] = {}
    with open(archivos[-1], encoding="utf-8") as f:
        for row in csv.DictReader(f):
            mid = row.get("market_id", "")
            if not mid:
                continue
            try:
                py  = float(row.get("price_yes") or 0)
                liq = float(row.get("liquidity") or 0)
            except (ValueError, TypeError):
                continue
            if liq < MIN_LIQ or py < PRICE_LO or py > PRICE_HI:
                continue
            ts = row.get("timestamp_utc", "")
            if mid not in last or ts > last[mid]["timestamp_utc"]:
                last[mid] = row

    return list(last.values())


# ---------------------------------------------------------------------------
# Topic clustering (keyword-based, sin LLM)
# ---------------------------------------------------------------------------

def asignar_topic(question: str) -> str:
    q_l = question.lower()
    scores = {t: 0 for t in _TOPICS}
    for topic, keywords in _TOPICS.items():
        for kw in keywords:
            if kw in q_l:
                scores[topic] += 1
    scores.pop("other")
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "other"


# ---------------------------------------------------------------------------
# Extracción de umbral y tipo de cadena
# ---------------------------------------------------------------------------

def _parse_umbral(texto: str) -> float | None:
    """Extrae el valor monetario del umbral (convertido a unidades base)."""
    m = _RE_UMBRAL.search(texto)
    if not m:
        return None
    try:
        val = float(m.group(1).replace(",", ""))
        suf = (m.group(2) or "").upper()
        mul = _SUFIJO.get(suf, 1.0)
        return val * mul
    except (ValueError, KeyError):
        return None


def _strip_umbral(texto: str) -> str:
    """Quita el umbral del texto para obtener la 'template' del mercado."""
    return _RE_UMBRAL.sub("$___", texto, count=1).strip()


def _tipo_cadena(texto: str) -> str | None:
    """
    Determina el tipo de relación monotónica:
      "above_up"   → P debe DISMINUIR al subir el umbral (reach, above, hit)
      "below_down" → P debe DISMINUIR al bajar el umbral (dip to, below)
    """
    t = texto.lower()
    if any(w in t for w in ["reach", "above", "hit", "exceed", "over", "top",
                             "high", "ath", "fdv above", "mcap above"]):
        return "above_up"
    if any(w in t for w in ["dip", "drop", "fall", "below", "under", "crash",
                             "low", "bottom"]):
        return "below_down"
    return None


# ---------------------------------------------------------------------------
# FAST PATH: Cadenas de monotonicidad
# ---------------------------------------------------------------------------

def detectar_cadenas(mercados: list[dict]) -> list[dict]:
    """
    Agrupa mercados en cadenas por (template, end_date, topic).
    Para cada par adyacente viola la monotonicidad → oportunidad de arb.
    """
    # Construir cadenas
    grupos: dict[tuple, list[dict]] = defaultdict(list)
    for m in mercados:
        q       = m.get("question", "")
        umbral  = _parse_umbral(q)
        tipo    = _tipo_cadena(q)
        if umbral is None or tipo is None:
            continue
        template = _strip_umbral(q)
        fecha    = m.get("end_date", "")[:10]
        topic    = asignar_topic(q)
        key      = (template, fecha, tipo, topic)
        grupos[key].append({**m, "_umbral": umbral, "_tipo": tipo})

    # Filtrar grupos con ≥2 mercados
    oportunidades = []
    for (template, fecha, tipo, topic), ms in grupos.items():
        if len(ms) < 2:
            continue

        # Ordenar por umbral
        if tipo == "above_up":
            # P debe bajar al subir el umbral → ordenar ascendente
            ms.sort(key=lambda x: x["_umbral"])
        else:
            # P debe bajar al bajar el umbral → ordenar descendente
            ms.sort(key=lambda x: x["_umbral"], reverse=True)

        # Verificar monotonicidad par a par
        for i in range(len(ms) - 1):
            a = ms[i]
            b = ms[i + 1]
            pa = float(a["price_yes"])
            pb = float(b["price_yes"])
            # Coste real de comprar YES en "a" es el ask, no el mid (ver mismo
            # fix aplicado 2026-07-01 en arb_scanner.py — ask medio ~0.025 por
            # encima del mid, suficiente para tragarse el margen de arb).
            ask_a = float(a.get("best_ask") or 0) or pa

            # Corrección: monotonicidad exige pa ≥ pb (a es "más fácil" de cumplir)
            if pa >= pb:
                continue  # sin violación

            # VIOLACIÓN: pa < pb → a debería tener mayor P pero no la tiene
            # Arb: comprar YES en "a" (barato) + NO en "b" (pagar (1-pb))
            # NOTA: el coste de la pata NO en "b" sigue siendo (1-price_yes_b),
            # una aproximación al mid — Polymarket no expone un ask propio del
            # token NO en nuestro esquema de datos (solo best_bid/best_ask del
            # YES), así que profit_bruto/profit_neto pueden seguir estando
            # ligeramente sobreestimados por esa pata. SOLO OBSERVACIÓN, no se
            # ejecuta ningún trade desde aquí.
            coste = ask_a + (1.0 - pb)
            profit_bruto = 1.0 - coste
            profit_neto  = profit_bruto - POLY_FEE

            # Registrar SIEMPRE (observation) — accionable solo si profit_neto > 0
            liq_min = min(float(a["liquidity"]), float(b["liquidity"]))
            oportunidades.append({
                "tipo_arb":       "MONOTONICITY",
                "topic":          topic,
                "mercado_a_id":   a["market_id"],
                "mercado_b_id":   b["market_id"],
                "pregunta_a":     a["question"][:80],
                "pregunta_b":     b["question"][:80],
                "umbral_a":       a["_umbral"],
                "umbral_b":       b["_umbral"],
                "price_yes_a":    round(pa, 4),
                "price_yes_b":    round(pb, 4),
                "tipo_cadena":    tipo,
                "relacion":       "a_implica_b",
                "coste_arb":      round(coste, 4),
                "profit_bruto":   round(profit_bruto * 100, 2),
                "profit_neto":    round(profit_neto * 100, 2),
                "accionable":     profit_neto > 0,
                "liq_min":        round(liq_min, 0),
                "fecha":          fecha,
                "dependencia":    f"Si '{a['question'][:50]}' → entonces '{b['question'][:50]}'",
                "posicion":       f"BUY_YES mercado_a ({pa:.3f}) + BUY_NO mercado_b ({1-pb:.3f})",
                "payoff":         "min {:.1f}%  max {:.1f}%".format(
                                  profit_neto * 100,
                                  (2.0 - coste - POLY_FEE) * 100
                                 ),
                "similitud":      1.0,
                "llm_flag":       False,
                "llm_razon":      "Monotonicidad matemática",
                "AVISO":          "SOLO OBSERVACION — verificar criterios de resolución",
            })

    return sorted(oportunidades, key=lambda x: -x["profit_neto"])


# ---------------------------------------------------------------------------
# REGLAS PATH: Detección de dependencias por reglas (sin LLM, sin API key)
# ---------------------------------------------------------------------------

# Meses abreviados para parsing de fechas
_MESES_ES = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
    "january": 1, "february": 2, "march": 3, "april": 4,
    "june": 6, "july": 7, "august": 8, "september": 9,
    "october": 10, "november": 11, "december": 12,
}
_RE_FECHA_TXT = re.compile(
    r'\b(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|'
    r'jul(?:y)?|aug(?:ust)?|sep(?:tember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)'
    r'\s+(\d{1,2})(?:st|nd|rd|th)?,?\s*(\d{4})',
    re.I
)
_RE_YEAR = re.compile(r'\b(202[4-9]|203\d)\b')
_RE_BY   = re.compile(r'\bby\b', re.I)


def _extraer_fecha_fin(texto: str) -> str | None:
    """Extrae fecha límite del texto ('by September 30, 2026' → '2026-09-30')."""
    m = _RE_FECHA_TXT.search(texto)
    if m:
        mon = _MESES_ES.get(m.group(1).lower(), 0)
        day = int(m.group(2))
        yr  = int(m.group(3))
        if mon:
            return f"{yr:04d}-{mon:02d}-{day:02d}"
    # Fallback: solo año
    m2 = _RE_YEAR.search(texto)
    if m2 and _RE_BY.search(texto):
        return f"{m2.group(1)}-12-31"
    return None


def _strip_fechas_y_umbrales(texto: str) -> str:
    """Template limpio: quita fechas Y umbrales (para monotonicity grouping)."""
    t = _RE_FECHA_TXT.sub("___DATE___", texto)
    t = _RE_UMBRAL.sub("$___", t)
    t = re.sub(r'\bby\s+\d{4}\b', 'by ___YEAR___', t, flags=re.I)
    return t.strip()


def _strip_solo_fechas(texto: str) -> str:
    """Template limpio: quita SOLO fechas, MANTIENE umbrales.
    Para R1 temporal: 'X by Sep30' y 'X by Dec31' → mismo template."""
    t = _RE_FECHA_TXT.sub("___DATE___", texto)
    t = re.sub(r'\bby\s+\d{4}\b', 'by ___YEAR___', t, flags=re.I)
    return t.strip()


def _entidad_token(texto: str) -> str | None:
    """Extrae nombre de token/proyecto de una pregunta tipo 'Will X launch...'"""
    q = texto.lower()
    # Patterns: "Will X launch", "Will X airdrop", "X FDV above", "X token"
    for pat in [
        r'^will\s+(\w[\w\s]*?)\s+(?:launch|release|airdrop|deploy|announce)',
        r'^(\w[\w\s]*?)\s+(?:fdv|mcap|market cap|token)\s+(?:above|below|reach)',
        r'^will\s+(\w[\w\s]*?)\s+(?:do|perform|complete)\s+an?\s+(?:airdrop|token)',
    ]:
        m = re.match(pat, q)
        if m:
            nombre = m.group(1).strip()
            if len(nombre) >= 2 and nombre not in ("the", "a", "an"):
                return nombre
    return None


def _registro_regla(a: dict, b: dict, tipo_dep: str, razon: str,
                    coste: float, profit_bruto: float, desc: str) -> dict:
    profit_neto = profit_bruto - POLY_FEE
    liq_min     = min(float(a.get("liquidity", 0)), float(b.get("liquidity", 0)))
    pa = float(a["price_yes"])
    pb = float(b["price_yes"])
    return {
        "tipo_arb":    "RULE_DEPENDENCY",
        "topic":       asignar_topic(a.get("question", "")),
        "mercado_a_id": a["market_id"],
        "mercado_b_id": b["market_id"],
        "pregunta_a":  a["question"][:80],
        "pregunta_b":  b["question"][:80],
        "umbral_a":    _parse_umbral(a.get("question", "")) or "",
        "umbral_b":    _parse_umbral(b.get("question", "")) or "",
        "price_yes_a": round(pa, 4),
        "price_yes_b": round(pb, 4),
        "tipo_cadena": tipo_dep,
        "relacion":    tipo_dep,
        "coste_arb":   round(coste, 4),
        "profit_bruto": round(profit_bruto * 100, 2),
        "profit_neto":  round(profit_neto * 100, 2),
        "accionable":   profit_neto > 0,
        "liq_min":      round(liq_min, 0),
        "fecha":        a.get("end_date", "")[:10],
        "dependencia":  razon,
        "posicion":     desc,
        "payoff":       f"profit_neto={profit_neto*100:.1f}%",
        "similitud":    0.9,
        "llm_flag":     False,
        "llm_razon":    razon,
        "AVISO":        "SOLO OBSERVACION — verificar resolución y liquidez",
    }


def _r1_temporal(mercados: list[dict]) -> list[dict]:
    """
    R1: Implicación temporal.
    'X by Sep30' implica 'X by Dec31' → P(Sep30) ≤ P(Dec31).
    Si P(Sep30) > P(Dec31), violación.
    """
    ops = []
    # Agrupar por template (sin fechas, CON umbrales) + topic
    # Así "launch by Sep30" y "launch by Dec31" → mismo grupo
    # Pero "reach $70k by Dec31" y "reach $85k by Dec31" → grupos distintos
    grupos: dict[str, list[dict]] = defaultdict(list)
    for m in mercados:
        q = m.get("question", "")
        if not _RE_BY.search(q):
            continue
        fecha_limite = _extraer_fecha_fin(q)
        if not fecha_limite:
            continue
        tmpl  = _strip_solo_fechas(q)   # mantiene umbrales → no confunde monotonicidad
        topic = asignar_topic(q)
        grupos[f"{tmpl}|{topic}"].append({**m, "_deadline": fecha_limite})

    for ms in grupos.values():
        if len(ms) < 2:
            continue
        ms.sort(key=lambda x: x["_deadline"])   # más temprano primero
        for i in range(len(ms) - 1):
            a = ms[i]    # deadline más temprano → CONDICIÓN MÁS RESTRICTIVA
            b = ms[i+1]  # deadline más tardío   → CONDICIÓN MÁS LAXA
            # Ignorar pares con misma fecha — esos son monotonicidad, no temporal
            if a["_deadline"] == b["_deadline"]:
                continue
            pa = float(a["price_yes"])
            pb = float(b["price_yes"])
            # Coste real de comprar YES en "b" es el ask, no el mid (mismo fix
            # que arb_scanner.py). La pata NO en "a" sigue siendo aproximada
            # con (1-price_yes_a) — no hay ask propio del token NO en el
            # esquema de datos actual. SOLO OBSERVACIÓN, sin ejecución.
            ask_b = float(b.get("best_ask") or 0) or pb
            # Debe cumplirse: P(antes) ≤ P(después)
            if pa <= pb:
                continue  # sin violación
            # VIOLACIÓN: P(antes) > P(después) — imposible lógicamente
            # Arb: comprar YES en B (más barato que debería) + NO en A
            coste        = ask_b + (1.0 - pa)
            profit_bruto = 1.0 - coste
            desc = f"BUY_YES_B({pb:.3f}) + BUY_NO_A({1-pa:.3f}) — deadline B más tardío"
            razon = (f"'{b['question'][:50]}' (deadline {b['_deadline']}) "
                     f"abarca '{a['question'][:50]}' (deadline {a['_deadline']}) "
                     f"→ P_B ≥ P_A debe cumplirse")
            ops.append(_registro_regla(a, b, "A_implica_B", razon, coste, profit_bruto, desc))
    return ops


def _r2_exclusividad(mercados: list[dict]) -> list[dict]:
    """
    R2: Exclusividad mutua.
    En un mercado con un único ganador, la suma de P(winner_i) ≤ 1.
    Detecta preguntas tipo 'Will [X] win [tournament/election]?'
    """
    ops  = []
    _RE_WIN = re.compile(
        r'^(?:will\s+)?(.+?)\s+(?:win|become|take)\s+(?:the\s+)?(.+?)(?:\?|$)', re.I
    )
    # Agrupar por "event" (lo que se gana)
    grupos: dict[str, list[dict]] = defaultdict(list)
    for m in mercados:
        q = m.get("question", "")
        mt = _RE_WIN.match(q)
        if not mt:
            continue
        quien  = mt.group(1).strip()
        evento = mt.group(2).strip().lower()
        # Normalizar evento
        evento = re.sub(r'\s+', ' ', evento)
        fecha  = m.get("end_date", "")[:10]
        grupos[f"{evento}|{fecha}"].append({**m, "_quien": quien})

    for ms in grupos.values():
        if len(ms) < 2:
            continue
        # Verificar todos los pares
        for i in range(len(ms)):
            for j in range(i+1, len(ms)):
                a = ms[i]; b = ms[j]
                pa = float(a["price_yes"])
                pb = float(b["price_yes"])
                suma = pa + pb
                if suma <= 1.02:   # tolerancia 2% por fee
                    continue
                # VIOLACIÓN: suma > 1 → comprar NO en ambos
                # Pagar (1-pa) + (1-pb), cobrar ≥1 cuando uno resuelve NO
                # NOTA: ambas patas son NO — no hay ask propio del token NO en
                # el esquema de datos actual (solo best_bid/best_ask del YES),
                # así que (1-price_yes) es una aproximación al mid en las DOS
                # patas, no solo una. profit_bruto/profit_neto aquí son los
                # menos fiables de las 3 reglas. SOLO OBSERVACIÓN.
                coste        = (1.0 - pa) + (1.0 - pb)
                profit_bruto = suma - 1.0    # exceso garantizado
                desc = (f"BUY_NO_A({1-pa:.3f}) + BUY_NO_B({1-pb:.3f}) "
                        f"— sum YES = {suma:.3f} > 1")
                razon = (f"'{a['_quien']}' y '{b['_quien']}' no pueden ganar ambos "
                         f"el mismo evento → suma YES {suma:.3f} > 1")
                ops.append(_registro_regla(
                    a, b, "mutuamente_excluyentes", razon, coste, profit_bruto, desc
                ))
    return ops


def _r3_launch_fdv(mercados: list[dict]) -> list[dict]:
    """
    R3: Implicación lanzamiento → FDV.
    'Token X FDV above $Y' implica 'Token X lanza' → P(lanza) ≥ P(FDV > Y).
    Si P(lanza) < P(FDV > Y), violación.
    """
    ops = []
    # Separar: mercados de lanzamiento vs mercados de FDV/MCap
    _RE_FDV = re.compile(r'\b(?:fdv|mcap|market cap)\b', re.I)
    _RE_LAU = re.compile(r'\b(?:launch|token|airdrop|release)\b', re.I)

    launch_ms: list[dict] = []
    fdv_ms:    list[dict] = []
    for m in mercados:
        q = m.get("question", "")
        entidad = _entidad_token(q)
        if not entidad:
            continue
        m2 = {**m, "_entidad": entidad}
        if _RE_FDV.search(q):
            fdv_ms.append(m2)
        elif _RE_LAU.search(q) and not _RE_FDV.search(q):
            launch_ms.append(m2)

    # Emparejar por entidad (nombre similar)
    for fdv in fdv_ms:
        pa = float(fdv["price_yes"])  # P(FDV > X)
        for launch in launch_ms:
            pb = float(launch["price_yes"])  # P(lanza)
            # Coste real de comprar YES(lanza) es el ask, no el mid (mismo fix
            # que arb_scanner.py). La pata NO(FDV) sigue aproximada con
            # (1-price_yes) — sin ask propio del token NO en el esquema actual.
            ask_pb = float(launch.get("best_ask") or 0) or pb
            # Misma entidad?
            e1 = fdv["_entidad"].lower()
            e2 = launch["_entidad"].lower()
            if e1 not in e2 and e2 not in e1:
                continue
            # Mismo año de resolución?
            if fdv.get("end_date","")[:4] != launch.get("end_date","")[:4]:
                continue
            # Debe cumplirse: P(lanza) ≥ P(FDV > X)
            if pb >= pa:
                continue  # sin violación
            # VIOLACIÓN: P(FDV > X) > P(lanza) — imposible
            # Posición correcta: BUY_NO_FDV + BUY_YES_LAUNCH (coste=(1-pa)+pb).
            # La combinación contraria (BUY_YES_FDV + BUY_NO_LAUNCH, pa+(1-pb))
            # tiene un estado real donde ambas patas pierden (FDV<=X y lanza) —
            # no es un hedge válido, y su profit_bruto=pb-pa sale negativo en
            # toda violación real, así que nunca se marcaba accionable (bug
            # confirmado 2026-07-01: coste usaba las patas cambiadas respecto
            # a la posición descrita más abajo en `desc`).
            coste        = (1.0 - pa) + ask_pb
            profit_bruto = 1.0 - coste
            desc = (f"BUY_NO_FDV({1-pa:.3f}) + BUY_YES_LAUNCH({pb:.3f}) "
                    f"— FDV implica lanzamiento")
            razon = (f"'{fdv['question'][:50]}' implica lanzamiento de {e1} "
                     f"→ P(lanza)={pb:.3f} ≥ P(FDV>X)={pa:.3f} debe cumplirse")
            ops.append(_registro_regla(
                fdv, launch, "A_implica_B", razon, coste, profit_bruto, desc
            ))
    return ops


def detectar_reglas(mercados: list[dict]) -> list[dict]:
    """
    Detector de dependencias por reglas (sin LLM, sin API key).
    R1: Implicación temporal (mismo evento, distinto deadline)
    R2: Exclusividad mutua (mismo evento, distintos ganadores)
    R3: Implicación lanzamiento→FDV
    """
    ops  = []
    ops += _r1_temporal(mercados)
    ops += _r2_exclusividad(mercados)
    ops += _r3_launch_fdv(mercados)
    return sorted(ops, key=lambda x: -x["profit_neto"])


# ---------------------------------------------------------------------------
# Output CSV
# ---------------------------------------------------------------------------

COLS = [
    "timestamp_utc", "tipo_arb", "topic", "mercado_a_id", "mercado_b_id",
    "pregunta_a", "pregunta_b", "umbral_a", "umbral_b",
    "price_yes_a", "price_yes_b", "tipo_cadena", "relacion",
    "coste_arb", "profit_bruto", "profit_neto", "accionable", "liq_min", "fecha",
    "dependencia", "posicion", "payoff", "similitud",
    "llm_flag", "llm_razon", "AVISO",
]


def guardar_csv(oportunidades: list[dict], fecha: str) -> Path:
    path = DIR_SHADOW / f"combi_arb_{fecha}.csv"
    ts   = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        for op in oportunidades:
            w.writerow({**op, "timestamp_utc": ts})
    return path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ts    = datetime.now(timezone.utc).isoformat(timespec="seconds")
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"[{ts}] === Combi Arb Scanner ===")

    print(f"  Cargando mercados (liq>${MIN_LIQ/1000:.0f}k)...")
    t0      = time.time()
    mercados = cargar_mercados()
    print(f"    {len(mercados)} mercados únicos ({time.time()-t0:.1f}s)")

    # ── FAST PATH ────────────────────────────────────────────────────────────
    print("  [FAST] Detectando violaciones de monotonicidad...")
    fast_ops = detectar_cadenas(mercados)
    print(f"    {len(fast_ops)} violaciones encontradas")

    # ── RULES PATH ───────────────────────────────────────────────────────────
    print("  [RULES] Detectando dependencias (temporal, exclusividad, FDV→launch)...")
    llm_ops = detectar_reglas(mercados)
    print(f"    {len(llm_ops)} dependencias detectadas")

    # ── Combinar y mostrar ────────────────────────────────────────────────────
    todas = sorted(fast_ops + llm_ops, key=lambda x: -x["profit_neto"])

    accionables = [op for op in todas if op.get("accionable")]
    print(f"\n  {'='*60}")
    print(f"  TOTAL violaciones: {len(todas)}  (FAST: {len(fast_ops)}, LLM: {len(llm_ops)})")
    print(f"  Accionables (profit_neto>0): {len(accionables)}")
    print(f"  Observación sub-fee:         {len(todas) - len(accionables)}")

    # Mostrar primero accionables, luego sub-fee
    mostrar = accionables[:5] + [op for op in todas if not op.get("accionable")][:5]
    if mostrar:
        print(f"\n  TOP OBSERVACIONES:")
        for op in mostrar[:8]:
            tag = "OK" if op.get("accionable") else "obs"
            print(f"\n  [{tag}] [{op['tipo_arb']}] {op['topic'].upper()} "
                  f"| profit_neto={op['profit_neto']:+.2f}% | liq=${op['liq_min']:.0f}")
            print(f"    A: {op['pregunta_a'][:70]}  YES={op['price_yes_a']}")
            print(f"    B: {op['pregunta_b'][:70]}  YES={op['price_yes_b']}")
            print(f"    {op['dependencia'][:80]}")
            print(f"    {op['posicion'][:80]}")
    else:
        print("\n  Sin violaciones detectadas hoy.")

    if todas:
        path = guardar_csv(todas, fecha)
        print(f"\n  Guardado: {path} ({len(todas)} filas)")

    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin Combi Arb ===")


if __name__ == "__main__":
    main()
