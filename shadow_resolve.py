"""
shadow_resolve.py — resolución de predicciones contra resultados reales.

Recorre todas las predicciones registradas que tengan decision != SKIP
y aún no se hayan resuelto. Para cada una:
  - Consulta el estado actual del mercado en Polymarket.
  - Si el mercado se ha cerrado/resuelto, determina el outcome ganador.
  - Calcula si la predicción acertó, el P&L bruto y el P&L con slippage.

Salidas:
  - data/shadow/results.csv         — historial acumulativo de resoluciones
  - data/shadow/strategy_accuracy.csv — IC y stats por estrategia (para auto-calibración)

Ejecutado tras shadow_predict.py en el mismo workflow.
"""

import csv
import fcntl
import glob
import json
import math
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# Credenciales antes de leer POLY_DEPOSIT_WALLET en _fees_reales_recientes.
# Fix 08-Jul (code-review): sin esto os.getenv devuelve None en producción
# (run_fast.sh no exporta .env al proceso) y toda la confirmación de fee real
# queda inerte en silencio -- el mismo bug que ledger_fiscal.py/reconciliar.py
# ya evitan haciendo esto mismo al principio del fichero.
from dotenv import load_dotenv
load_dotenv(Path("data/live/.env"))


def _infer_subtype(pred: dict) -> str:
    """Infiere subtype de la columna razon cuando no está disponible en el CSV."""
    s = pred.get("subtype", "")
    if s:
        return s
    razon = pred.get("razon", "") or ""
    # "updown_gbm BTC 15min ..."  →  BTC#15min
    m = re.search(r'updown_gbm\s+(\w+)\s+(\w+)', razon)
    if m:
        return f"{m.group(1)}#{m.group(2)}"
    # "price_target_gbm BTC atexpiry ..."  →  BTC#atexpiry
    m = re.search(r'price_target_gbm\s+(\w+)\s+(\w+)', razon)
    if m:
        return f"{m.group(1)}#{m.group(2)}"
    # "weekly_between BTC ..." / "weekly_price BTC ..."  →  BTC
    m = re.search(r'weekly_(?:between|price)\s+(\w+)', razon)
    if m:
        return m.group(1)
    # "price_momentum ..." / "smart_flow_1h ..."  → asset si aparece
    m = re.search(r'(?:price_momentum|smart_flow_1h)\s+.*?(BTC|ETH|SOL|XRP|DOGE|BNB)', razon)
    if m:
        return m.group(1)
    return ""

TIMEOUT = 30
SLIPPAGE = 0.02
APUESTA_SIMULADA = 0.90  # consistente con el bot anterior (3% de 30€)

DIR_SHADOW = Path("data/shadow")
DIR_SHADOW.mkdir(parents=True, exist_ok=True)
RESULTS_PATH = DIR_SHADOW / "results.csv"
ACCURACY_PATH = DIR_SHADOW / "strategy_accuracy.csv"
CONFIRM_STATE_PATH = DIR_SHADOW / "resolucion_confirmacion_state.json"
# 21-Jul (code-review pendiente desde 15-Jul, idea_shadow_resolve_cierre_prematuro):
# margen mínimo que un outcome cerca de 1.0/0.0 debe verse ESTABLE antes de
# aceptarse como definitivo. Cubre el caso real de un mercado resuelto 1min
# después de su end_date con asentamiento aún inestable.
# code-review 21-Jul: este margen es un heurístico de tiempo, sin medición
# propia de cuánto dura un asentamiento inestable real — la fuente de
# resolución OFICIAL (Chainlink, vía fetch_chainlink_prices.py) sería más
# precisa que este margen fijo, pero a 21-Jul solo lleva ~1-2 días
# acumulando y aún no está conectada a ninguna decisión en todo el proyecto
# (ver memoria idea_nested_arb_garantia_causa_chainlink_20jul) — conectarla
# aquí hoy sería una integración nueva sin datos suficientes para validarla,
# no una mejora de este fix. Queda anotado como mejora futura, no construido.
MARGEN_CONFIRMACION_SEGUNDOS = 90
# Entradas de confirmación más viejas que esto se podan por seguridad (nunca
# deberían sobrevivir tanto — candidatas() ya descarta end_date >2h en el
# futuro; esto es solo defensa contra crecimiento sin límite del fichero).
CONFIRM_STATE_MAX_AGE_SEGUNDOS = 6 * 3600
# code-review 21-Jul (2ª pasada): cuánto se espera a que la resolución normal
# (evaluar(), con su margen de estabilidad propio) cierre un trade antes de
# que Smart Exit retome la protección por su cuenta. Acota el hueco "ninguna
# de las dos protege" a un máximo conocido (antes no tenía cota: si
# evaluar() reseteaba su margen de 90s una y otra vez por fallos de fetch,
# Smart Exit ya había dejado de proteger para siempre en cuanto pasó
# end_date). 5min = ~3x el margen normal de 90s, margen generoso para
# reintentos transitorios sin dejar la ventana sin cota.
GRACIA_RESOLUCION_NORMAL_SEGUNDOS = 300


def _clave_confirmacion(strategy: str, market_id: str) -> str:
    """Única fuente de verdad para la clave de resolucion_confirmacion_state.json
    — evaluar() y main() deben llamar a esta función en vez de construir el
    f-string cada uno por su cuenta (code-review 21-Jul: dos construcciones
    independientes podían divergir en silencio)."""
    return f"{strategy}|{market_id}"


def _parsear_end_date(end_str: str) -> "datetime | None":
    """Parsea un end_date de la API/predicción a datetime tz-aware, o None si
    está vacío o es inválido. Única fuente de verdad para este parseo —
    code-review 21-Jul (2ª pasada): estaba duplicado verbatim en evaluar() y
    en _check_salidas_tempranas_bajo_lock, con el riesgo de que un fix futuro
    solo tocara una de las dos copias."""
    if not end_str:
        return None
    try:
        end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
        return end_dt
    except Exception:
        return None


def _cargar_estado_confirmacion() -> dict:
    if not CONFIRM_STATE_PATH.exists():
        return {}
    try:
        estado = json.loads(CONFIRM_STATE_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        # Fail-closed: un estado ilegible se trata como "nada visto todavía",
        # nunca como "ya confirmado" — en el peor caso se repite el margen de
        # espera una vez más, nunca se acepta una resolución de golpe.
        print(f"  ⚠️ estado de confirmación de resolución ilegible "
              f"({type(e).__name__}: {e}) — se trata como vacío, cualquier "
              f"outcome pendiente reinicia su margen de confirmación")
        return {}
    if not isinstance(estado, dict):
        return {}
    # Fail-closed también por entrada individual (code-review 21-Jul): una
    # entrada parcial/corrupta (p.ej. truncada a mitad de escritura) NO debe
    # tumbar evaluar() con un KeyError — se descarta esa entrada sola, como
    # si nunca se hubiera visto, en vez de perder el ciclo entero.
    # code-review 21-Jul (2ª pasada): bool es subclase de int en Python
    # (isinstance(True, int) → True) y json.loads acepta NaN/Infinity por
    # defecto — ambos colaban como "primera_vista_ts" válido y hacían que
    # `elapsed < MARGEN` diera False, saltándose la espera y aceptando de
    # golpe. Se excluye bool explícitamente y se exige un valor finito.
    limpio = {}
    huerfanas = False
    for k, v in estado.items():
        ts = v.get("primera_vista_ts") if isinstance(v, dict) else None
        ts_valido = (isinstance(ts, (int, float)) and not isinstance(ts, bool)
                     and math.isfinite(ts))
        if (isinstance(v, dict) and v.get("outcome") in ("YES", "NO") and ts_valido):
            limpio[k] = v
        else:
            huerfanas = True
            print(f"  ⚠️ entrada de confirmación ilegible para {k!r} — "
                  f"descartada, se trata como no vista todavía")
    if huerfanas:
        # code-review 21-Jul (2ª pasada): si no se persiste ya aquí, y este
        # ciclo no cambia nada más, la comparación "solo escribir si cambió"
        # de main() nunca detecta la limpieza (compara contra ESTE mismo
        # dict ya limpio) y la entrada corrupta queda en disco para siempre,
        # re-avisando cada ciclo. Autocurar de inmediato en cuanto se detecta.
        _guardar_estado_confirmacion(limpio)
    return limpio


def _guardar_estado_confirmacion(estado: dict) -> None:
    try:
        tmp = CONFIRM_STATE_PATH.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(estado, separators=(",", ":")), encoding="utf-8")
        tmp.replace(CONFIRM_STATE_PATH)
    except Exception as e:
        print(f"  ⚠️ fallo al escribir estado de confirmación de resolución "
              f"({type(e).__name__}: {e}) — la próxima resolución candidata "
              f"reiniciará su margen de confirmación")


def _normalizar_pred(row: dict) -> dict:
    """
    El header del CSV puede tener solo 13 columnas (formato antiguo).
    En ese caso subtype, apuesta y features van al key None como lista.
    Los extraemos para que el resto del código los encuentre con sus nombres.
    """
    extra = row.pop(None, None)
    if isinstance(extra, list):
        campos = ["subtype", "apuesta", "features"]
        for i, campo in enumerate(campos):
            if i < len(extra) and extra[i] and not row.get(campo):
                row[campo] = extra[i]
    return row


def cargar_predicciones_pendientes() -> list:
    """Carga todas las predicciones que tengan decision != SKIP."""
    archivos = sorted(glob.glob(str(DIR_SHADOW / "predictions_*.csv")))
    pendientes = []
    for arch in archivos:
        with open(arch, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("decision", "SKIP") in ("BUY_YES", "BUY_NO"):
                    pendientes.append(_normalizar_pred(row))
    return pendientes


def cargar_ya_resueltas() -> set:
    """
    Devuelve set de (strategy, market_id) ya resueltos.
    Sin timestamp: cada (strategy, market_id) se resuelve UNA sola vez aunque
    se haya predicho en varios días distintos (evita duplicar el IC).
    """
    if not RESULTS_PATH.exists():
        return set()
    ya = set()
    with open(RESULTS_PATH, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ya.add((row.get("strategy", ""),
                    row.get("market_id", "")))
    return ya


def estado_mercado(market_id: str) -> dict | None:
    """
    Consulta el estado actual del mercado en Polymarket. Reintenta en 429.

    Usa el endpoint por path (/markets/{id}), NO por query param (?id=X):
    verificado 2026-07-01 que ?id=X aplica un filtro implícito closed=false
    y por tanto NUNCA devuelve un mercado ya cerrado — exactamente el caso
    que evaluar() necesita para confirmar la resolución final. Esto dejaba
    predicciones sin resolver indefinidamente en cuanto el mercado cerraba
    de verdad (875 pares strategy/market_id >6h pasado su end_date sin
    resolver en el momento de detectarlo), con riesgo directo de dejar
    trades live en status=OPEN para siempre.
    """
    url = f"https://gamma-api.polymarket.com/markets/{market_id}"
    for intento in range(3):
        try:
            r = requests.get(url, timeout=TIMEOUT)
            if r.status_code == 429:
                time.sleep(2 ** intento)  # backoff: 1s, 2s, 4s
                continue
            if r.status_code == 404:
                return None
            r.raise_for_status()
            data = r.json()
            if isinstance(data, list) and data:
                return data[0]
            if isinstance(data, dict):
                return data
            return None
        except Exception as e:
            if intento == 2:
                print(f"  Error consultando {market_id}: {type(e).__name__}: {e}")
    return None


def fetch_mercados_paralelo(market_ids: list, workers: int = 3) -> dict:
    """
    Descarga el estado de múltiples mercados en paralelo con throttle.
    Máximo 3 workers simultáneos para no saturar la API de Polymarket.
    """
    import threading
    from concurrent.futures import ThreadPoolExecutor, as_completed
    _sem = threading.Semaphore(workers)

    def _fetch_con_sem(mid):
        with _sem:
            time.sleep(0.1)  # 100ms entre requests → ~30 req/s máximo
            return estado_mercado(mid)

    resultados = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futuros = {executor.submit(_fetch_con_sem, mid): mid for mid in market_ids}
        for futuro in as_completed(futuros):
            mid = futuros[futuro]
            try:
                resultados[mid] = futuro.result()
            except Exception:
                resultados[mid] = None
    return resultados


def parse_outcome_prices(raw):
    if raw is None or raw == "":
        return None
    if isinstance(raw, list):
        return raw
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return None
    return None


def evaluar(pred: dict, mercado: dict, ahora: datetime | None = None,
            estado_confirmacion: dict | None = None) -> dict | None:
    """
    Señal primaria: outcomePrices — si alguno llega a 1.0 el mercado está
    resuelto, independientemente de los flags closed/archived/resolved.
    Esto evita falsos negativos cuando la API actualiza los precios antes
    de cambiar el campo closed (comportamiento habitual en Polymarket).

    Salvaguarda 1 (21-Jul, antes solo exigía closed O end_date): el flag
    closed/archived/resolved NO basta por sí solo — verificado 15-Jul que
    Polymarket puede marcar closed=True hasta 44min ANTES del end_date real
    (precio tocó ~100% del lado incorrecto por volatilidad intraciclo, el
    mercado revirtió después). Ahora SIEMPRE se exige que el end_date real
    haya pasado, tenga o no el mercado ya el flag closed puesto.

    Salvaguarda 2 (21-Jul): pasar el end_date tampoco basta en el instante
    exacto — un caso real resolvió mal 1min DESPUÉS de end_date, con el
    asentamiento aún inestable ("photo finish" sin terminar de asentar). Se
    exige ver el MISMO outcome de forma estable durante
    MARGEN_CONFIRMACION_SEGUNDOS antes de aceptarlo como definitivo.
    estado_confirmacion debe persistir entre ciclos (main() lo carga/guarda
    en CONFIRM_STATE_PATH) para que el margen se cumpla de verdad; si se
    pasa None o un dict nuevo en cada llamada, el fail-closed por diseño es
    que NUNCA se confirme (cada llamada ve la primera vez) — nunca al revés.

    Nota (code-review 21-Jul): "estable" se exige de forma CONTINUA — un
    ciclo intermedio que no repita el mismo outcome (precio no liquidado,
    fetch fallido o end_date aún no pasado) BORRA el progreso de
    confirmación en curso para este mercado, no solo lo deja congelado. Si
    no fuera así, un asentamiento que parpadea (terminal→no-terminal→
    terminal) podría acumular los 90s con huecos de inestabilidad en medio,
    exactamente el escenario que este margen existe para descartar.
    """
    ahora_dt = ahora or datetime.now(timezone.utc)
    estado = estado_confirmacion if estado_confirmacion is not None else {}
    clave_conf = _clave_confirmacion(pred.get("strategy", ""), pred.get("market_id", ""))

    if not mercado:
        estado.pop(clave_conf, None)
        return None

    # --- Señal primaria: outcomePrices ---
    precios = parse_outcome_prices(mercado.get("outcomePrices"))
    if not precios or len(precios) < 2:
        estado.pop(clave_conf, None)
        return None
    try:
        py_final = float(precios[0])
        pn_final = float(precios[1])
    except (ValueError, TypeError):
        estado.pop(clave_conf, None)
        return None

    if abs(py_final - 1.0) < 0.01:
        outcome_real = "YES"
    elif abs(pn_final - 1.0) < 0.01:
        outcome_real = "NO"
    else:
        estado.pop(clave_conf, None)
        return None  # precios no liquidados — reintentar en el siguiente ciclo

    # Confirmar que el mercado realmente cerró antes de aceptar el precio como
    # definitivo. 21-Jul: el flag closed/archived/resolved/active YA NO se usa
    # para saltarse esta comprobación — se verificó que Polymarket puede
    # marcar closed=True hasta 44min ANTES del end_date real (ver docstring).
    # Prioriza el endDate fresco del mercado (recién descargado en esta misma
    # función) sobre el cacheado en la predicción — si la predicción se hizo
    # sin endDate (mercado aún sin ese campo poblado en su momento), el
    # cacheado queda vacío para siempre y la resolución por precio nunca se
    # acepta (trade live queda OPEN indefinidamente).
    end_str = mercado.get("endDate") or pred.get("end_date", "")
    end_dt = _parsear_end_date(end_str)
    end_pasado = end_dt is not None and ahora_dt >= end_dt
    if end_dt is None:
        # Sin end_date en NINGÚN sitio (ni la respuesta fresca de la API ni
        # la predicción cacheada) — code-review 21-Jul: esto puede dejar la
        # predicción sin resolver para siempre si además closed/resolved ya
        # es True (el bypass que aceptaba esto de inmediato se quitó a
        # propósito, ver Salvaguarda 1). No se reintroduce ningún bypass —
        # se prefiere fail-closed (nunca resolver mal) a fail-open (resolver
        # mal) — pero se deja constancia en el log para que sea detectable
        # en vez de un None silencioso indistinguible de "aún no ha cerrado".
        if mercado.get("closed") or mercado.get("resolved") or mercado.get("archived"):
            print(f"  ⚠️ market {pred.get('market_id','')}: closed/resolved=True "
                  f"pero SIN end_date en ningún sitio (ni API ni predicción) — "
                  f"no se resuelve por precio hasta tener un end_date real; "
                  f"si esto persiste, revisar manualmente (reconciliar_posiciones.py "
                  f"avisa aparte para trades live >60min OPEN tras su end_date)")
    if not end_pasado:
        estado.pop(clave_conf, None)
        return None  # precio cerca de certeza pero el reloj real aún no ha llegado a end_date — reintentar

    # Margen de reconfirmación: no aceptar en el primer ciclo que se ve el
    # outcome como definitivo — exige verlo estable un rato antes de cerrarlo.
    previa = estado.get(clave_conf)
    if previa is None or previa.get("outcome") != outcome_real:
        # Primera vez que vemos este outcome (o cambió respecto al anterior
        # visto para este mismo mercado) — fail-closed: reinicia el reloj de
        # confirmación y reintenta, nunca acepta a la primera.
        estado[clave_conf] = {"outcome": outcome_real, "primera_vista_ts": ahora_dt.timestamp()}
        return None
    if ahora_dt.timestamp() - previa["primera_vista_ts"] < MARGEN_CONFIRMACION_SEGUNDOS:
        return None  # visto pero aún no ha pasado el margen mínimo de estabilidad
    # Confirmado: mismo outcome estable >= MARGEN_CONFIRMACION_SEGUNDOS.
    # El llamador (main()) debe borrar clave_conf de estado_confirmacion una
    # vez aceptado aquí, para no crecer sin límite.

    decision = pred.get("decision", "")
    acierto = (decision == "BUY_YES" and outcome_real == "YES") or \
              (decision == "BUY_NO" and outcome_real == "NO")

    # P&L simulado.
    try:
        precio_entrada = float(pred.get("precio_yes_mercado", 0.5))
    except (ValueError, TypeError):
        precio_entrada = 0.5
    # Piso Y techo: precio_yes_mercado es una probabilidad, [0,1]. Un valor
    # corrupto por encima de 1 (dato upstream dañado) haría que un WIN real
    # se contabilizara como pérdida más abajo (payout = apuesta/precio_entrada
    # sale por debajo de la apuesta) — mismo patrón que ya se corrigió para
    # el caso "hacia 0", pero por el lado no cubierto.
    precio_entrada = min(0.99, max(0.01, precio_entrada))
    if decision == "BUY_NO":
        precio_entrada = 1 - precio_entrada

    # Apuesta: usa la registrada en la predicción (Kelly dinámico), o la base si no existe
    try:
        apuesta = float(pred.get("apuesta") or APUESTA_SIMULADA)
        if apuesta <= 0:
            apuesta = APUESTA_SIMULADA
    except (ValueError, TypeError):
        apuesta = APUESTA_SIMULADA

    if acierto:
        payout    = apuesta / max(0.01, precio_entrada)
        pnl_bruto = payout - apuesta
        pnl_neto  = pnl_bruto - SLIPPAGE * apuesta
    else:
        pnl_bruto = -apuesta
        pnl_neto  = -apuesta - SLIPPAGE * apuesta

    return {
        "outcome_real": outcome_real,
        "acierto": 1 if acierto else 0,
        "precio_entrada": precio_entrada,
        "pnl_bruto": pnl_bruto,
        "pnl_neto": pnl_neto,
    }


def actualizar_strategy_accuracy(nuevos: list, ts: str):
    """
    Actualiza data/shadow/strategy_accuracy.csv con las nuevas resoluciones.

    Por cada estrategia calcula métricas acumuladas:
    - n_total: predicciones resueltas
    - n_aciertos: cuántas acertaron
    - hit_rate: tasa de acierto real
    - edge_medio: edge_direccional medio al entrar
    - pnl_total: P&L neto acumulado
    - IC (Information Coefficient): correlación entre señal y outcome
      IC = hit_rate - 0.5  (simplificado para mercados binarios 50/50)
      Cuando tengamos suficientes datos usaremos correlación de Pearson
      entre prob_yes_modelo y outcome_real (YES=1, NO=0).
    - IC_pearson: correlación Pearson entre prob_yes_modelo y outcome_real
      (más preciso que hit_rate-0.5, requiere prob_yes_modelo poblado)
    """
    # Cargar stats existentes
    stats = {}
    if ACCURACY_PATH.exists():
        with open(ACCURACY_PATH, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                s = row["strategy"]
                stats[s] = {
                    "n_total": int(row.get("n_total", 0)),
                    "n_aciertos": int(row.get("n_aciertos", 0)),
                    "pnl_total": float(row.get("pnl_total", 0)),
                    "sum_edge": float(row.get("sum_edge", 0)),
                    # Para IC de Pearson: acumulamos suma de productos
                    "sum_prob": float(row.get("sum_prob", 0)),
                    "sum_outcome": float(row.get("sum_outcome", 0)),
                    "sum_prob2": float(row.get("sum_prob2", 0)),
                    "sum_outcome2": float(row.get("sum_outcome2", 0)),
                    "sum_prob_outcome": float(row.get("sum_prob_outcome", 0)),
                }

    # Incorporar nuevas resoluciones
    for r in nuevos:
        s = r["strategy"]
        if s not in stats:
            stats[s] = {
                "n_total": 0, "n_aciertos": 0, "pnl_total": 0.0,
                "sum_edge": 0.0, "sum_prob": 0.0, "sum_outcome": 0.0,
                "sum_prob2": 0.0, "sum_outcome2": 0.0, "sum_prob_outcome": 0.0,
            }
        d = stats[s]
        d["n_total"] += 1
        d["n_aciertos"] += int(r["acierto"])
        d["pnl_total"] += float(r["pnl_neto"])
        try:
            d["sum_edge"] += float(r.get("edge_direccional", 0) or 0)
        except (ValueError, TypeError):
            pass
        # Para IC Pearson: prob_yes_modelo vs outcome (YES=1, NO=0)
        try:
            prob = float(r.get("prob_yes_modelo", "") or "")
            outcome = 1.0 if r["outcome_real"] == "YES" else 0.0
            d["sum_prob"] += prob
            d["sum_outcome"] += outcome
            d["sum_prob2"] += prob * prob
            d["sum_outcome2"] += outcome * outcome
            d["sum_prob_outcome"] += prob * outcome
        except (ValueError, TypeError):
            pass

    # Calcular métricas derivadas y guardar
    columnas = [
        "timestamp_utc", "strategy",
        "n_total", "n_aciertos", "hit_rate",
        "edge_medio", "pnl_total", "pnl_medio",
        "IC_simple", "IC_pearson",
        # acumuladores internos (para poder añadir filas futuras)
        "sum_edge", "sum_prob", "sum_outcome",
        "sum_prob2", "sum_outcome2", "sum_prob_outcome",
    ]
    filas = []
    for s, d in sorted(stats.items()):
        n = d["n_total"]
        hit_rate = d["n_aciertos"] / n if n else 0.0
        ic_simple = round(hit_rate - 0.5, 4)  # IC simplificado binario
        # IC Pearson si tenemos datos de prob_yes_modelo
        ic_pearson = 0.0
        try:
            sp = d["sum_prob"]
            so = d["sum_outcome"]
            sp2 = d["sum_prob2"]
            so2 = d["sum_outcome2"]
            spo = d["sum_prob_outcome"]
            num = n * spo - sp * so
            den = math.sqrt(max(0, (n * sp2 - sp**2) * (n * so2 - so**2)))
            ic_pearson = round(num / den, 4) if den > 1e-10 else 0.0
        except (ZeroDivisionError, ValueError):
            pass

        filas.append({
            "timestamp_utc": ts,
            "strategy": s,
            "n_total": n,
            "n_aciertos": d["n_aciertos"],
            "hit_rate": round(hit_rate, 4),
            "edge_medio": round(d["sum_edge"] / n, 4) if n else 0.0,
            "pnl_total": round(d["pnl_total"], 4),
            "pnl_medio": round(d["pnl_total"] / n, 4) if n else 0.0,
            "IC_simple": ic_simple,
            "IC_pearson": ic_pearson,
            "sum_edge": round(d["sum_edge"], 6),
            "sum_prob": round(d["sum_prob"], 6),
            "sum_outcome": round(d["sum_outcome"], 6),
            "sum_prob2": round(d["sum_prob2"], 6),
            "sum_outcome2": round(d["sum_outcome2"], 6),
            "sum_prob_outcome": round(d["sum_prob_outcome"], 6),
        })

    with open(ACCURACY_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        w.writeheader()
        for fila in filas:
            w.writerow(fila)

    print(f"  IC por estrategia (IC_simple = hit_rate - 0.5):")
    for fila in filas:
        if fila["n_total"] > 0:
            bar = "+" * max(0, int(fila["IC_simple"] * 20))
            print(f"    {fila['strategy']:30s}  n={fila['n_total']:>4}  "
                  f"hit={fila['hit_rate']:.3f}  IC={fila['IC_simple']:+.3f}  "
                  f"pnl={fila['pnl_total']:+.2f}  {bar}")


def _brier(pred: dict, res: dict) -> str:
    """Brier score = (prob_modelo - outcome)². Proper scoring rule: se minimiza con la prob real."""
    try:
        p = float(pred.get("prob_yes_modelo", 0.5) or 0.5)
        o = float(res["acierto"])  # 1 si acertó YES, 0 si no
        # Para BUY_NO: el acierto es cuando outcome=NO (acierto=1 pero outcome_real=NO)
        # prob_yes_modelo < 0.5 para BUY_NO, outcome_real puede ser YES o NO
        outcome_yes = 1.0 if res["outcome_real"] == "YES" else 0.0
        return f"{(p - outcome_yes) ** 2:.4f}"
    except Exception:
        return ""


def _log_loss(pred: dict, res: dict) -> str:
    """Log loss = -[o*ln(p) + (1-o)*ln(1-p)]. Complementa Brier: penaliza mucho
    más fuerte estar MUY seguro y equivocado (una p=0.95 que falla cuesta
    ln(20)≈3.0 en log loss vs solo 0.9 en Brier) — el fallo que más costó esta
    sesión (FAVORITO_CONFIRMADO con 60% hit pero pnl negativo en ejecución
    real: alta confianza mal calibrada). Clip a [1e-9,1-1e-9] para evitar -inf
    en p=0 o p=1 exactos. Artículo 12-Jul sobre probabilidad bayesiana bien
    calibrada — parte 6 (calibración), ver memoria idea_bayes_calibracion_bot."""
    try:
        p = float(pred.get("prob_yes_modelo", 0.5) or 0.5)
        p = min(max(p, 1e-9), 1 - 1e-9)
        outcome_yes = 1.0 if res["outcome_real"] == "YES" else 0.0
        import math
        ll = -(outcome_yes * math.log(p) + (1 - outcome_yes) * math.log(1 - p))
        return f"{ll:.4f}"
    except Exception:
        return ""


def _clv(pred: dict, res: dict) -> str:
    """
    Closing Line Value: mide si nuestra predicción tenía edge respecto al mercado.
    CLV = outcome_real - precio_entrada (para BUY_YES)
        = precio_entrada - outcome_real  (para BUY_NO)
    Positivo = compramos barato (el mercado estaba equivocado a nuestro favor).
    Promedio de CLV > 0 con n suficiente = edge real, no suerte.
    """
    try:
        precio = float(pred.get("precio_yes_mercado", 0.5) or 0.5)
        outcome_yes = 1.0 if res["outcome_real"] == "YES" else 0.0
        dec = pred.get("decision", "")
        if dec == "BUY_YES":
            return f"{outcome_yes - precio:.4f}"
        elif dec == "BUY_NO":
            return f"{precio - outcome_yes:.4f}"
        return ""
    except Exception:
        return ""


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Shadow resolve ===")

    # Smart Exit stop-loss (16-Jul): independiente de si hay resoluciones
    # nuevas este ciclo — revisa las posiciones OPEN antes de que su mercado
    # resuelva. No-op mientras riesgo.smart_exit_stop_loss.activo sea false.
    try:
        _check_salidas_tempranas(ts)
    except Exception as e:
        print(f"  ⚠️  _check_salidas_tempranas: {e} — posiciones OPEN sin tocar, resolución normal sigue")

    pendientes = cargar_predicciones_pendientes()
    ya_resueltas = cargar_ya_resueltas()
    estado_confirmacion = _cargar_estado_confirmacion()
    # Copia para comparar al final y no escribir el fichero si no cambió nada
    # este ciclo (code-review 21-Jul: evitar I/O sin motivo cada ~20s).
    # code-review 21-Jul (2ª pasada): basta una copia superficial -- ninguna
    # mutación de estado_confirmacion edita un dict interno in-place, siempre
    # reemplaza la clave entera o la borra, así que dict(...) es suficiente
    # para la comparación posterior y evita el round-trip JSON completo.
    estado_confirmacion_snapshot = dict(estado_confirmacion)

    nuevos_resultados = []
    debug_no_resueltos = 0
    ahora = datetime.now(timezone.utc)

    # Filtrar predicciones que vale la pena consultar
    candidatas = []
    for pred in pendientes:
        if pred.get("decision", "") == "SKIP":
            continue  # SKIP no necesitan resolución
        clave = (pred.get("strategy", ""), pred.get("market_id", ""))
        if clave in ya_resueltas:
            continue
        end_str = pred.get("end_date", "")
        if end_str:
            try:
                end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
                if end_dt.tzinfo is None:
                    end_dt = end_dt.replace(tzinfo=timezone.utc)
                if (end_dt - ahora).total_seconds() > 7200:
                    continue
            except Exception:
                pass
        candidatas.append(pred)

    # Obtener IDs únicos y descargar en paralelo (throttled)
    mids_unicos = list({p.get("market_id", "") for p in candidatas if p.get("market_id")})
    print(f"  Descargando {len(mids_unicos)} mercados en paralelo (workers=3, throttled)...")
    cache_mercados = fetch_mercados_paralelo(mids_unicos, workers=3)
    consultados_ids = set(mids_unicos)

    for pred in candidatas:
        clave = (pred.get("strategy", ""), pred.get("market_id", ""))
        if clave in ya_resueltas:
            continue
        mid = pred.get("market_id", "")
        mercado = cache_mercados.get(mid)
        res = evaluar(pred, mercado, ahora=ahora, estado_confirmacion=estado_confirmacion)
        if res is None:
            if mercado and debug_no_resueltos < 3:
                precios = mercado.get("outcomePrices", "?")
                print(f"  [debug] market {mid}: closed={mercado.get('closed')} "
                      f"archived={mercado.get('archived')} "
                      f"resolved={mercado.get('resolved')} "
                      f"active={mercado.get('active')} "
                      f"outcomePrices={str(precios)[:40]}")
                debug_no_resueltos += 1
            continue

        # Marcar como resuelta en memoria para evitar duplicados dentro del mismo run
        ya_resueltas.add(clave)
        # Ya confirmada de forma definitiva — no hace falta seguir rastreando
        # su margen de confirmación.
        estado_confirmacion.pop(_clave_confirmacion(clave[0], clave[1]), None)

        nuevos_resultados.append({
            "resolution_timestamp": ts,
            "prediction_timestamp": pred.get("timestamp_utc", ""),
            "strategy": pred.get("strategy", ""),
            "subtype": _infer_subtype(pred),
            "market_id": mid,
            "question": pred.get("question", ""),
            "end_date": pred.get("end_date", ""),
            "decision": pred.get("decision", ""),
            "precio_yes_mercado": pred.get("precio_yes_mercado", ""),
            "prob_yes_modelo": pred.get("prob_yes_modelo", ""),
            "edge_neto": pred.get("edge_neto", ""),
            "edge_direccional": pred.get("edge_direccional", ""),
            "outcome_real": res["outcome_real"],
            "acierto": res["acierto"],
            "pnl_bruto": f"{res['pnl_bruto']:.4f}",
            "pnl_neto": f"{res['pnl_neto']:.4f}",
            "features": pred.get("features", ""),
            "brier_score": _brier(pred, res),
            "clv": _clv(pred, res),
            "log_loss": _log_loss(pred, res),
        })

        # Simulación maker (observacional, best-effort — jamás afecta a la
        # resolución real ni al cierre de trades live; ver maker_sim.py)
        try:
            import maker_sim
            maker_sim.simular(pred, mercado, res, ts)
        except Exception:
            pass

    # Podar entradas de confirmación demasiado viejas (defensa contra
    # crecimiento sin límite; ver CONFIRM_STATE_MAX_AGE_SEGUNDOS). El margen
    # de confirmación se cumple entre ciclos, así que esto debe evaluarse
    # SIEMPRE, haya o no resoluciones nuevas — pero solo se escribe a disco
    # si algo cambió de verdad respecto a lo cargado al inicio (code-review
    # 21-Jul: escribir el fichero cada ~20s sin cambios era I/O sin motivo,
    # y este proyecto solo escribe sus otros ficheros de estado on-change).
    ahora_ts = ahora.timestamp()
    for k in [k for k, v in estado_confirmacion.items()
              if ahora_ts - v.get("primera_vista_ts", ahora_ts) > CONFIRM_STATE_MAX_AGE_SEGUNDOS]:
        estado_confirmacion.pop(k, None)
    if estado_confirmacion != estado_confirmacion_snapshot:
        _guardar_estado_confirmacion(estado_confirmacion)

    print(f"  Predicciones pendientes consultadas: {len(consultados_ids)} mercados")
    print(f"  Resoluciones nuevas: {len(nuevos_resultados)}")
    try:
        import maker_sim
        _rs = maker_sim.resumen()
        if _rs:
            print(f"  {_rs}")
    except Exception:
        pass

    if not nuevos_resultados:
        print(f"[{ts}] === Fin shadow resolve (nada nuevo) ===")
        return

    nuevo_archivo = not RESULTS_PATH.exists()
    columnas = list(nuevos_resultados[0].keys())
    with open(RESULTS_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        if nuevo_archivo:
            w.writeheader()
        for r in nuevos_resultados:
            w.writerow(r)

    # Resumen rápido por estrategia
    resumen = {}
    for r in nuevos_resultados:
        s = r["strategy"]
        resumen.setdefault(s, {"n": 0, "aciertos": 0, "pnl": 0.0})
        resumen[s]["n"] += 1
        resumen[s]["aciertos"] += r["acierto"]
        resumen[s]["pnl"] += float(r["pnl_neto"])
    print("  Resumen de nuevas resoluciones por estrategia:")
    for s, d in resumen.items():
        tasa = d["aciertos"] / d["n"] * 100 if d["n"] else 0
        print(f"    {s:30s}  n={d['n']:>4}  acierto={tasa:5.1f}%  "
              f"pnl_neto={d['pnl']:+.2f}€")

    # Cerrar trades live que hayan resuelto
    _cerrar_trades_live(nuevos_resultados, ts)


def _check_salidas_tempranas(ts: str):
    """Smart Exit — stop-loss (16-Jul, petición Javi de espejar el take-profit
    original para el lado perdedor). Revisa cada trade live OPEN y, solo si
    la config lo activa, vende anticipadamente cuando la pérdida no
    realizada (con haircut de spread+fee real) cruza el umbral configurado.
    Calibración y contexto completo en idea_smart_exit.md; gate en
    config_live.json::riesgo.smart_exit_stop_loss. Mientras 'activo' sea
    false (default), esto es un no-op completo — ni siquiera consulta
    mercados. Fail-closed en cada paso (ver live_trade._ejecutar_venta_temprana):
    cualquier duda deja la posición OPEN, el camino normal de resolución
    sigue intacto — nunca puede empeorar el resultado. Código de seguridad
    live — no minimizar."""
    LIVE_CSV = Path("data/live/trades.csv")
    if not LIVE_CSV.exists():
        return
    try:
        cfg = json.loads(Path("data/live/config_live.json").read_text(encoding="utf-8"))
    except Exception:
        return
    sl_cfg = cfg.get("riesgo", {}).get("smart_exit_stop_loss", {})
    # 18-Jul (hallazgo /code-review): comprobación de tipo estricta -- un
    # "false" string (típico error de edición manual de JSON) es truthy en
    # Python y habría activado el mecanismo sin querer. Solo True booleano
    # activa; cualquier otra cosa (incluida ausencia de la clave) es inerte.
    if sl_cfg.get("activo") is not True:
        return

    try:
        umbral  = float(sl_cfg.get("umbral_perdida_eur", 0.30))
        haircut = float(sl_cfg.get("fee_rate_taker_estimado", 0.07))
    except (TypeError, ValueError):
        return

    import live_trade
    # flock (17-Jul, code-review del ejecutor ballenas_fast: 3 ángulos
    # independientes encontraron que esta reescritura completa del CSV no
    # estaba protegida por el mismo lock que _registrar_trade() -- un
    # append de otro proceso (ballenas_executor_btc15m.py, persistente,
    # fuera del orden secuencial de run_fast.sh) cayendo entre la lectura
    # y la reescritura de aquí se perdía en silencio. Se toma UNA vez para
    # toda la lectura+bucle+escritura(s), no por-write, porque el bucle
    # puede reescribir varias veces sobre el mismo `trades` en memoria
    # (una vez por posición cerrada) y todas comparten la misma foto de
    # lectura inicial.
    lock_f = open(live_trade.TRADES_LOCK_PATH, "w")
    fcntl.flock(lock_f, fcntl.LOCK_EX)
    try:
        _check_salidas_tempranas_bajo_lock(LIVE_CSV, ts, umbral, haircut)
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()


def _check_salidas_tempranas_bajo_lock(LIVE_CSV: Path, ts: str, umbral: float, haircut: float):
    """Cuerpo real de _check_salidas_tempranas, ejecutado con el lock de
    trades.csv ya adquirido (ver ahí el motivo). Separado en función propia
    para no anidar el bucle entero dentro de un try/finally."""
    import live_trade
    trades = list(csv.DictReader(open(LIVE_CSV, encoding="utf-8")))
    abiertas = [t for t in trades if t.get("status") == "OPEN" and t.get("market_id")]
    if not abiertas:
        return

    # 18-Jul (hallazgo /code-review): estado_mercado(mid) secuencial, una
    # llamada HTTP por posición OPEN -- ya existe fetch_mercados_paralelo en
    # este mismo fichero (throttle 3 workers/100ms) para exactamente esto.
    mercados = fetch_mercados_paralelo([t.get("market_id", "") for t in abiertas])

    cols = list(trades[0].keys())
    fees_recientes = None  # lazy: solo se pide a data-api si de verdad hay una venta que cerrar
    ahora_local = datetime.now(timezone.utc)  # una sola vez, no por posición
    for t in abiertas:
        mid = t.get("market_id", "")
        direction = t.get("direction", "")
        try:
            entry_p = float(t.get("entry_price") or 0)
            stake   = float(t.get("stake_eur") or 0)
        except ValueError:
            continue
        if entry_p <= 0 or stake <= 0:
            continue

        mercado = mercados.get(mid)
        if not mercado:
            continue  # fail-closed: sin dato de mercado, no se evalúa esta posición
        # code-review 21-Jul: closed/resolved/archived YA NO se usa como señal
        # de "la resolución normal está al caer" — evaluar() (este mismo
        # fichero) verificó que Polymarket puede marcar closed=True hasta
        # 44min ANTES del end_date real. Se exige el mismo criterio que
        # evaluar(): end_date genuinamente pasado.
        #
        # code-review 21-Jul (2ª pasada): end_pasado solo no basta — evaluar()
        # además exige un margen de estabilidad (MARGEN_CONFIRMACION_SEGUNDOS)
        # que puede reiniciarse sin cota ante fallos de fetch/parpadeos. Si
        # aquí se dejara de proteger para siempre en cuanto pasa end_date (sin
        # más), y evaluar() nunca llega a confirmar, la posición queda sin
        # NINGUNA protección por tiempo indefinido. Se da un margen de gracia
        # acotado (GRACIA_RESOLUCION_NORMAL_SEGUNDOS) a la resolución normal;
        # si se agota y el trade sigue OPEN, Smart Exit retoma la protección.
        end_str = mercado.get("endDate") or t.get("end_date", "")
        end_dt = _parsear_end_date(end_str)
        if end_dt is not None:
            segundos_desde_cierre = (ahora_local - end_dt).total_seconds()
            if 0 <= segundos_desde_cierre < GRACIA_RESOLUCION_NORMAL_SEGUNDOS:
                continue  # end_date pasó hace poco -- se le da margen a la resolución normal
            # si no: end_date aún no ha pasado (sigue vivo, se protege como
            # siempre) o ya pasó de sobra y sigue OPEN (algo se atascó -- se
            # retoma la protección en vez de dejarlo indefinidamente expuesto)
        else:
            # Sin end_date determinable -- no hay forma de saber si la
            # resolución normal lo va a manejar pronto. Se prefiere seguir
            # protegiendo (fail-closed hacia MÁS protección) en vez de
            # saltarlo a ciegas como hacía el flag closed/resolved antiguo.
            if mercado.get("closed") or mercado.get("resolved") or mercado.get("archived"):
                print(f"  ⚠️ Smart Exit: market {mid} closed/resolved=True pero "
                      f"sin end_date en ningún sitio -- se sigue protegiendo "
                      f"(fail-closed) en vez de asumir que la resolución "
                      f"normal lo maneja")

        op = parse_outcome_prices(mercado.get("outcomePrices"))
        if not op or len(op) < 2:
            continue
        try:
            pyes, pno = float(op[0]), float(op[1])
        except (TypeError, ValueError):
            continue
        p_lado = pyes if direction == "BUY_YES" else pno

        shares = stake / entry_p
        valor_ajustado = shares * p_lado * (1.0 - haircut)
        pnl_ajustado = valor_ajustado - stake
        if pnl_ajustado > -umbral:
            continue  # todavía no cruza el umbral

        resultado = live_trade._ejecutar_venta_temprana(
            mid, direction, entry_p, stake,
            contexto={"strategy": t.get("strategy", ""), "subtype": t.get("subtype", "")})
        if not resultado.get("ok"):
            continue  # fail-closed: sigue OPEN, la resolución normal seguirá su curso

        # 18-Jul (hallazgo /code-review, el más importante de los 9):
        # resultado["pnl_neto_eur"] solo descuenta el fee de LA VENTA -- el
        # fee de la COMPRA original (fee_eur al abrir casi siempre 0, nunca
        # se confirmó contra data-api en esta ruta) faltaba por completo,
        # sobreestimando el PnL real ~2.9-6.7% del stake (mismo rango que
        # ya corrige _fee_real_para_trade en el cierre normal). Reusa
        # exactamente esa función -- el fee de apertura es el mismo evento
        # real independientemente de cómo cierre la posición después.
        if fees_recientes is None:
            fees_recientes = _fees_reales_recientes()
        fee_apertura = _fee_real_para_trade(t, fees_recientes)
        # Capturar la confirmación ANTES del fallback (18-Jul, 2º hallazgo
        # /code-review sobre este mismo fix): reasignar fee_apertura más
        # abajo si es None hacía que la nota "confirmado=1/0" ya no pudiera
        # ver el None nunca -- mismo bug que ya se evitó en
        # _cerrar_trades_live_bajo_lock (línea ~997) capturando fee_real
        # aparte de fee. Aquí replica ese patrón correcto.
        fee_confirmado = fee_apertura is not None
        if fee_apertura is None:
            try:
                fee_apertura = float(t.get("fee_eur") or 0)
            except ValueError:
                fee_apertura = 0.0
            print(f"  ⚠️  fee de apertura no confirmado para market={mid} (smart-exit) -- usando fallback")
        fee_venta   = resultado["fee_eur"]
        fee_total   = round(fee_apertura + fee_venta, 4)
        pnl_bruto   = resultado["valor_venta_eur"] - stake
        # 18-Jul (hallazgo /code-review): el comentario anterior afirmaba
        # que resultado['pnl_neto_eur'] "ya resta fee_venta" pero pnl_bruto
        # se deriva de valor_venta_eur (bruto), no de ese campo -- fee_venta
        # nunca se restaba de verdad. Restar fee_total (apertura+venta), no
        # solo fee_apertura.
        pnl_neto    = round(pnl_bruto - fee_total, 4)

        t["status"]          = "CLOSED"
        t["close_timestamp"] = ts
        t["exit_price"]      = f"{resultado['exit_price']:.4f}"
        t["outcome_real"]    = "STOP_LOSS_TEMPRANO"
        t["fee_eur"]         = f"{fee_total:.4f}"
        t["pnl_bruto_eur"]   = f"{pnl_bruto:.4f}"
        t["pnl_neto_eur"]    = f"{pnl_neto:.4f}"
        nota_fee = "fee_apertura_confirmado=1" if fee_confirmado else "fee_apertura_confirmado=0"
        t["notas"] = f"{t.get('notas','')} smart_exit_stop_loss {nota_fee}".strip()

        # Persistir INMEDIATAMENTE tras esta venta real, antes de seguir
        # evaluando el resto de posiciones OPEN (16-Jul, code-review: 4
        # ángulos independientes marcaron el batch al final del bucle como
        # riesgo de idempotencia — si el proceso muere entre la venta #1 y
        # el fin del loop, esa venta ya ejecutada on-chain nunca se
        # persistía y la fila quedaba status=OPEN para siempre). Reescribe
        # el CSV completo (mismo patrón no atómico que _cerrar_trades_live),
        # pero ahora una vez POR TRADE cerrado, no una vez por ciclo.
        with open(LIVE_CSV, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(trades)
        try:
            from live_balance import actualizar_balance_real
            actualizar_balance_real()
        except Exception:
            pass
        try:
            # 18-Jul (hallazgo /code-review): acierto_dir hardcodeado a False
            # ocultaba visualmente cualquier caso donde el corte terminara en
            # PnL positivo (poco frecuente por diseño, pero posible si el
            # haircut estimado fue más pesimista que el fill real) y habría
            # escondido silenciosamente una futura corrección a medias del
            # cálculo de PnL. Se deriva del signo real.
            _notificar_cierre_live(t, pnl_neto, acierto_dir=(pnl_neto > 0))
        except Exception:
            pass
        print(f"  🔴 Smart-exit stop-loss: {t['strategy']}#{t['subtype']} {direction} "
              f"market={mid} PNL={pnl_neto:+.4f}€ (fee_apertura={fee_apertura:.4f}€, "
              f"corte anticipado, no resolución)")


def _notificar_cierre_live(trade: dict, pnl_neto: float, acierto_dir: bool):
    """Envía notificación Telegram cuando un trade live se resuelve."""
    import os
    tok = os.environ.get("TELEGRAM_TOKEN", "")
    cid = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not tok or not cid:
        return

    # Bankroll operativo (real on-chain si está fresco, si no ledger) y P&L del día
    try:
        from live_stake import bankroll_actual, pnl_live_hoy, CAPITAL_OPERATIVO_INICIAL
        bkr   = bankroll_actual()
        pnl_d = pnl_live_hoy()
        bkr_ini = CAPITAL_OPERATIVO_INICIAL
        pnl_total = bkr - bkr_ini
    except Exception:
        bkr = pnl_d = pnl_total = 0.0
        bkr_ini = 25.44

    # Balance REAL on-chain (verdad de suelo) — coordinado con el dashboard.
    # Antes este mensaje llamaba "Bankroll real" al bankroll de PLAN (engañoso).
    try:
        from live_balance import cargar_balance_real
        _snap = cargar_balance_real(max_edad_s=1800)
    except Exception:
        _snap = None

    signo   = "✅ WIN" if acierto_dir else "❌ LOSS"
    pnl_str = f"{pnl_neto:+.2f}$"
    q       = trade.get("question", "")[:55]
    entry_p = float(trade.get("entry_price") or 0)
    dir_    = trade.get("direction", "")
    sub     = trade.get("subtype", "")

    # Desglose de coste real (fix 08-Jul): stake + fee = coste total; el fee de
    # Polymarket (cobrado solo al comprar) no se veía en ningún sitio antes.
    stake_t   = float(trade.get("stake_eur") or 0)
    fee_t     = float(trade.get("fee_eur") or 0)
    pnl_bruto_t = float(trade.get("pnl_bruto_eur") or 0)
    coste_total = stake_t + fee_t
    fee_confirmado = "fee_confirmado=1" in (trade.get("notas") or "")
    linea_coste = (f"Coste: {stake_t:.2f}$ stake + {fee_t:.4f}$ fee{'' if fee_confirmado else ' (sin confirmar⚠)'} "
                   f"= {coste_total:.2f}$\n"
                   f"Bruto: {pnl_bruto_t:+.2f}$  →  Neto: *{pnl_str}*")

    # Racha: contar wins/losses en trades.csv para el día
    try:
        trades_hoy = []
        LIVE_CSV = Path("data/live/trades.csv")
        hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        for row in csv.DictReader(open(LIVE_CSV, encoding="utf-8")):
            if row.get("status") == "CLOSED" and row.get("close_timestamp", "").startswith(hoy):
                trades_hoy.append(row)
        n_hoy  = len(trades_hoy)
        w_hoy  = sum(1 for r in trades_hoy if float(r.get("pnl_neto_eur", 0) or 0) > 0)
        racha  = f"{w_hoy}W/{n_hoy-w_hoy}L hoy"
    except Exception:
        racha = ""

    if _snap and not _snap.get("_rancio"):
        bkr_color = "📈" if _snap["pnl_real"] >= 0 else "📉"
        linea_bkr = (f"{bkr_color} Balance real: *{_snap['total']:.2f}$*  "
                     f"({_snap['pnl_real']:+.2f} total · operativo {bkr:.2f}$)")
    else:
        bkr_color = "📈" if bkr >= bkr_ini else "📉"
        linea_bkr = f"{bkr_color} Bankroll operativo: *{bkr:.2f}$* ({pnl_total:+.2f}$ · real n/d)"
    msg = (
        f"{'🏆' if acierto_dir else '💸'} *TRADE LIVE — {signo}*\n"
        f"\n"
        f"Mercado: _{q}_\n"
        f"Dir: {dir_}  |  Entrada: {entry_p:.3f}  |  Sub: {sub}\n"
        f"{linea_coste}\n"
        f"\n"
        f"{linea_bkr}\n"
        f"Hoy (operativo): {pnl_d:+.2f}$  |  {racha}"
    )
    try:
        requests.post(
            f"https://api.telegram.org/bot{tok}/sendMessage",
            json={"chat_id": cid, "text": msg, "parse_mode": "Markdown"},
            timeout=10,
        )
        print(f"  [telegram] Resultado live enviado.")
    except Exception as e:
        print(f"  [telegram] Error notificando cierre live: {e}")


DATA_API_ACTIVITY = "https://data-api.polymarket.com/activity"
FEE_MAX_FRACCION_STAKE = 0.15  # observado 2.9%-6.7%; techo generoso, no cero


def _fees_reales_recientes(limit_paginas: int = 3, pagina: int = 500) -> dict:
    """{timestamp_unix: [(usdc_pagado, shares, precio), ...]} de los TRADE BUY
    reales más recientes de la wallet, vía data-api (público, sin clave).
    Lista por timestamp (no un solo valor) porque dos fills pueden caer en el
    mismo segundo -- un dict de valor único los pisaría en silencio.

    Fix 08-Jul: el fee real de Polymarket (cobrado SOLO al comprar, nunca al
    canjear) no aparece en `resp.get("feeRateBps")` -- ese campo nunca vino
    poblado en 104/104 trades históricos, así que fee_eur quedó en 0.0 siempre
    y pnl_neto_eur sobreestimaba la ganancia real ~3.78% del stake de media
    (verificado cruzando data-api/activity: usdcSize pagado > shares*price).
    En vez de reproducir la fórmula interna del fee (curva price*(1-price)^exp,
    con AL MENOS dos orígenes de tasa distintos en la librería del CLOB, unidades
    ambiguas) se lee el gasto real ya asentado on-chain -- ground truth, no
    estimación, y sobrevive a cualquier cambio futuro del esquema de fees.

    Paginado (no un solo limit=300): un día con mucha actividad podía dejar
    fuera del corte un BUY temprano y reportarlo como "no confirmado" por una
    razón evitable, no por falta de dato real.
    """
    wallet = os.getenv("POLY_DEPOSIT_WALLET")
    if not wallet:
        print("  [WARN] _fees_reales_recientes: POLY_DEPOSIT_WALLET no disponible "
              "(revisar que data/live/.env se cargó) -- fee_eur quedará sin confirmar esta vuelta")
        return {}
    eventos = []
    for i in range(limit_paginas):
        try:
            r = requests.get(DATA_API_ACTIVITY,
                             params={"user": wallet, "limit": pagina, "offset": i * pagina},
                             timeout=15)
            r.raise_for_status()
            chunk = r.json() or []
        except Exception as e:
            print(f"  [WARN] _fees_reales_recientes: {type(e).__name__}: {e} "
                  "-- fee_eur quedará sin confirmar esta vuelta")
            break
        if not chunk:
            break
        eventos.extend(chunk)
        if len(chunk) < pagina:
            break
    out: dict = {}
    for a in eventos:
        if a.get("type") != "TRADE" or a.get("side") != "BUY":
            continue
        try:
            registro = (float(a["usdcSize"]), float(a["size"]), float(a["price"]))
        except (KeyError, ValueError, TypeError):
            continue
        out.setdefault(int(a["timestamp"]), []).append(registro)
    return out


def _fee_real_para_trade(t: dict, fees_recientes: dict, tolerancia_s: int = 90) -> float | None:
    """Busca el TRADE real más cercano en el tiempo al timestamp_utc del trade,
    desambiguando por nº de shares esperado (stake/entry_price) para no cruzar
    el fee de OTRO trade cuando hay 2 posiciones abiertas simultáneas (el
    sistema lo permite, config_live.json::max_posiciones_abiertas_misma_direccion).
    None si no hay match dentro de tolerancia+shares -- fail-loud, no se inventa
    un fee ni se disfraza de "fuera de tolerancia" una causa distinta (credencial
    ausente, API caída: eso ya se avisa aparte en _fees_reales_recientes)."""
    try:
        ts_trade = datetime.fromisoformat(t["timestamp_utc"].replace("Z", "+00:00"))
        if ts_trade.tzinfo is None:
            ts_trade = ts_trade.replace(tzinfo=timezone.utc)
        ts_unix = ts_trade.timestamp()
        stake = float(t.get("stake_eur") or 0)
        entry_p = float(t.get("entry_price") or 0)
    except (KeyError, ValueError, TypeError, AttributeError):
        return None
    if stake <= 0 or entry_p <= 0:
        return None
    shares_esperadas = stake / entry_p

    candidatos = []
    for ts_ev, registros in fees_recientes.items():
        delta = abs(ts_ev - ts_unix)
        if delta > tolerancia_s:
            continue
        for usdc, shares, precio in registros:
            # desambiguación: el nº de shares real debe parecerse al esperado
            # (stake/entry_price) -- filtra el caso de 2 trades cerrando en el
            # mismo ciclo con matches cercanos en el tiempo pero de mercados
            # distintos (montos/precios distintos -> shares distintas).
            if abs(shares - shares_esperadas) / shares_esperadas > 0.15:
                continue
            candidatos.append((delta, usdc, shares, precio))
    if not candidatos:
        return None
    _, usdc_pagado, shares, precio = min(candidatos, key=lambda c: c[0])
    fee = usdc_pagado - shares * precio
    # clamp de seguridad (mismo espíritu que el techo/piso de entry_p arriba):
    # un match erróneo residual no debe poder corromper pnl_neto_eur real con
    # un fee absurdo. Rango observado 2.9%-6.7% del stake; techo generoso.
    return round(max(0.0, min(fee, stake * FEE_MAX_FRACCION_STAKE)), 4)


def _cerrar_trades_live(nuevos_resultados: list, ts: str):
    """Actualiza data/live/trades.csv: cierra trades OPEN cuyo mercado ya resolvió."""
    LIVE_CSV = Path("data/live/trades.csv")
    if not LIVE_CSV.exists():
        return

    # Índice de outcomes por market_id
    outcomes = {}
    for r in nuevos_resultados:
        outcomes[str(r["market_id"])] = {
            "outcome_real": r["outcome_real"],
            "acierto":      int(r["acierto"]),
        }

    import live_trade
    # flock (17-Jul, mismo motivo que _check_salidas_tempranas arriba):
    # protege esta reescritura completa del CSV frente a un append
    # concurrente de _registrar_trade() desde otro proceso.
    lock_f = open(live_trade.TRADES_LOCK_PATH, "w")
    fcntl.flock(lock_f, fcntl.LOCK_EX)
    try:
        _cerrar_trades_live_bajo_lock(LIVE_CSV, outcomes, ts)
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()

    # Fuera del lock a propósito: no tocan trades.csv, no hace falta
    # retener el lock más de lo necesario.
    actualizar_strategy_accuracy(nuevos_resultados, ts)
    print(f"[{ts}] === Fin shadow resolve ===")


def _cerrar_trades_live_bajo_lock(LIVE_CSV: Path, outcomes: dict, ts: str):
    """Cuerpo real de _cerrar_trades_live, ejecutado con el lock de
    trades.csv ya adquirido (ver ahí el motivo)."""
    trades = list(csv.DictReader(open(LIVE_CSV, encoding="utf-8")))
    modificado = False
    cierres = []
    fees_recientes = None  # lazy: solo se pide a data-api si de verdad hay algo que cerrar

    for t in trades:
        if t.get("status") != "OPEN":
            continue
        mid = str(t.get("market_id", ""))
        if mid not in outcomes:
            continue

        if fees_recientes is None:
            fees_recientes = _fees_reales_recientes()

        outcome = outcomes[mid]["outcome_real"]
        acierto = outcomes[mid]["acierto"]
        direction = t.get("direction", "")
        acierto_dir = (direction == "BUY_YES" and outcome == "YES") or \
                      (direction == "BUY_NO"  and outcome == "NO")

        try:
            stake      = float(t.get("stake_eur") or 0)
            # Techo además de piso: mismo motivo que en evaluar() — un
            # entry_price corrupto >1 convertiría un WIN real en pérdida
            # via pnl_bruto = stake*(1/entry_p - 1) negativo.
            entry_p    = min(0.99, max(0.01, float(t.get("entry_price") or 0.5)))
        except ValueError:
            continue

        fee_real = _fee_real_para_trade(t, fees_recientes)
        if fee_real is not None:
            fee = fee_real
        else:
            # fail-loud: no se encontró/confirmó el TRADE real (credencial
            # ausente, API caída, o genuinamente fuera de tolerancia -- la
            # causa concreta ya se avisó aparte en _fees_reales_recientes si
            # aplica; aquí NO se afirma cuál fue para no disfrazar de "detalle
            # normal" lo que puede ser un fallo sistemático). Se cierra igual
            # (no bloquear el resolver por una métrica secundaria) con el
            # fallback anterior, protegido: fee_eur corrupto en el CSV no debe
            # tumbar el cierre de TODOS los trades de este ciclo.
            try:
                fee = float(t.get("fee_eur") or 0)
            except ValueError:
                fee = 0.0
            print(f"  ⚠️  fee real no confirmado para market={mid} -- fee_eur queda sin confirmar")

        if acierto_dir and entry_p > 0:
            pnl_bruto = stake * (1.0 / entry_p - 1.0)
        else:
            pnl_bruto = -stake
        pnl_neto = pnl_bruto - fee

        t["status"]          = "CLOSED"
        t["close_timestamp"] = ts
        t["exit_price"]      = "1.0" if acierto_dir else "0.0"
        t["outcome_real"]    = outcome
        t["fee_eur"]         = f"{fee:.4f}"
        t["pnl_bruto_eur"]   = f"{pnl_bruto:.4f}"
        t["pnl_neto_eur"]    = f"{pnl_neto:.4f}"
        nota_fee = "fee_confirmado=1" if fee_real is not None else "fee_confirmado=0"
        t["notas"] = f"{t.get('notas','')} {nota_fee}".strip()
        modificado = True
        cierres.append((t, pnl_neto, acierto_dir))
        signo = "✅" if acierto_dir else "❌"
        print(f"  {signo} Trade live cerrado: {t['strategy']}#{t['subtype']} "
              f"{direction} market={mid} PNL={pnl_neto:+.4f}€")

    if modificado:
        cols = list(trades[0].keys())
        with open(LIVE_CSV, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(trades)
        # Refresca el balance REAL on-chain tras redimir → dashboard y notificación
        # reflejan el wallet al instante (no esperan al cron 15min). Guardado.
        try:
            from live_balance import actualizar_balance_real
            actualizar_balance_real()
        except Exception:
            pass
        # Notificar cada cierre por Telegram
        for t, pnl_neto, acierto_dir in cierres:
            _notificar_cierre_live(t, pnl_neto, acierto_dir)


if __name__ == "__main__":
    main()
