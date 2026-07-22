#!/usr/bin/env python3
"""
ballenas_observer.py — observador continuo del timing de entrada de las
wallets GANADORAS, desagregado por activo x marco temporal (5m/15m/60m/
240m/weekly), TODAS las combinaciones — no solo las 3 que hoy lo consumen.

Origen (15-Jul, petición explícita Javi): las 3 estrategias
s_gbm_late_15min_py_confirmado / s_gbm_late_60min_py_confirmado /
s_gbm_late_5min (shadow_predict.py) nacieron el 14-Jul de un análisis
MANUAL puntual (ver memoria idea_timing_wallets_smart_vs_sistema_14jul):
banda de precio [0.70,0.90) + ventana de minutos restantes calibradas una
vez y hardcodeadas. Este script las convierte en "gasolina" continua:
recalcula con datos frescos cada ciclo en vez de congelar un análisis de
un día concreto.

Metodología (idéntica a la validada a mano el 14-Jul, automatizada):
1. Muestrea mercados YA RESUELTOS de data/markets/*.csv — TODOS los
   activos x marcos, no solo los que ya tienen estrategia. Cada marco
   tiene su propia ventana de lookback: los lentos (240min, weekly)
   necesitan mirar más atrás para acumular n que 5min, donde hay
   mercados de sobra cada hora.
2. Para mercados no vistos todavía (cache de condition_id ya procesados
   — un mercado resuelto no cambia, nunca hace falta reprocesarlo), pide
   sus trades reales (data-api /trades, reutiliza
   smart_money_tracker.trades_de_mercado) y la resolución oficial
   (gamma-api, reutiliza shadow_resolve.fetch_mercados_paralelo /
   parse_outcome_prices) — igual que analisis_timing_wallets_por_activo.py,
   pero muestreando TODAS las wallets que operan cada mercado (vía
   /trades) en vez de una lista de wallets "smart" precocinada (lección
   del 14-Jul: la lista precocinada sesga qué patrones se ven).
3. Cada trade se guarda con: activo, marco, precio pagado (el precio del
   lado comprado, no siempre "precio_yes" — comprar el favorito caro es
   la señal, sea YES o NO), wallet, minutos restantes hasta el cierre
   (sirve tal cual para comparar entre marcos: un 5min y un weekly viven
   en escalas de tiempo distintas y no hace falta forzarlos a la misma
   unidad, cada combo se lee con su propia escala) y si acertó.
4. El histórico se acumula en un CSV rolling que se poda cada ciclo a la
   ventana de retención propia de cada marco — el patrón medido es
   siempre reciente, no arrastra para siempre datos de hace meses.
5. Por (activo, marco), se barren bandas de precio fijas y se busca la de
   mejor z-test (H0: mercado eficiente, gana con prob=precio pagado) que
   además esté REPARTIDA entre wallets (top1 < TOP1_MAX del PnL positivo
   agregado) y tenga n >= N_MIN — los 2 mismos filtros que cazaron los
   falsos positivos manuales del 14-Jul (SOL#5min banda barata = 1
   wallet con 95% de acierto, ETH#60min z altísimo pero top1=58%).
   Solo si pasa las 3 barras se marca "significativo"; si no, el combo
   se deja tal cual (no se inventa una banda con datos insuficientes) y
   el consumidor (shadow_predict.py) cae a su valor por defecto.
6. Persiste data/shadow/ballenas_timing_state.json — leído en vivo por
   shadow_predict.py con fallback a las constantes de la primera pasada
   manual si el combo no es significativo todavía.

Puramente shadow/observacional: no toca live_trade.py, config_live.json
ni pares_permitidos_live — ninguna de las 3 estrategias que consume esto
está en whitelist live. Cron propio (hourly), no comparte cadencia con
smart_money_tracker.py (P16, propósito distinto: consenso direccional
poblacional, no timing de entrada por banda de precio).
"""
import csv
import json
import math
import random
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

from smart_money_tracker import TAG_A_DURACION, NOMBRE_A_TICKER, trades_de_mercado
from shadow_resolve import fetch_mercados_paralelo, parse_outcome_prices

DIR = Path(__file__).parent
DIR_MARKETS = DIR / "data/markets"
DIR_SHADOW = DIR / "data/shadow"
HISTORY_CSV = DIR_SHADOW / "ballenas_timing_history.csv"
STATE_JSON = DIR_SHADOW / "ballenas_timing_state.json"
CACHE_PROCESADOS = DIR_SHADOW / "ballenas_timing_procesados.json"

# Cuánto mirar hacia atrás (horas) para MUESTREAR mercados nuevos, y hasta
# dónde se retiene el histórico rolling antes de podarlo — mismo valor
# para ambos usos: lo que ya no cabe en la ventana de lookback tampoco
# debería seguir pesando en las estadísticas.
VENTANA_LOOKBACK_HORAS = {"5m": 24 * 3, "15m": 24 * 5, "60m": 24 * 10,
                           "240m": 24 * 21, "weekly": 24 * 60}
# Tope de mercados NUEVOS a procesar por ciclo, repartido por marco para
# que los lentos (poco volumen) no se queden sin cupo frente a 5min/15min
# (mucho volumen) — igual que MAX_MERCADOS_MUESTRA en smart_money_tracker,
# pero con reparto explícito en vez de un tope único.
CUOTA_POR_MARCO = {"5m": 40, "15m": 40, "60m": 20, "240m": 15, "weekly": 5}
MARGEN_RESOLUCION_MIN = 5  # solo procesar mercados cuyo end_date pasó hace >=5min

# Duración nominal (min) de cada marco de duración fija — weekly queda
# fuera a propósito (no tiene ventana fija conocida desde este CSV).
# Sirve para descartar trades con restante_min fuera de lo físicamente
# posible (visto en datos reales: ~0.1-0.4% de las filas con
# restante_min de horas/días en mercados de 5-240min — condition_id o
# end_date mal etiquetado en algún snapshot, no señal real). Buffer de
# 5min por posible desfase de reloj/snapshot.
MARCO_DURACION_MIN = {"5m": 5, "15m": 15, "60m": 60, "240m": 240}
BUFFER_DURACION_MIN = 5

BANDAS_PRECIO = [(0.0, 0.05), (0.05, 0.30), (0.30, 0.50),
                  (0.50, 0.70), (0.70, 0.90), (0.90, 1.00)]
Z_MIN = 2.0
TOP1_MAX = 0.40
N_MIN = 40
N_MIN_INFORMATIVO = 15  # umbral más bajo solo para reportar la banda en el detalle, no para activarla

HISTORY_COLS = ["condition_id", "activo", "marco", "ts_trade", "wallet",
                 "precio", "restante_min", "acierto", "compro_yes", "size_usd"]
# size_usd (22-Jul, petición Javi: "necesitamos tamaño de apuesta y ROI de
# la misma" tras encontrar que este CSV -- la única fuente con cobertura
# COMPLETA del nicho Up/Down corto, 389k filas -- nunca capturó tamaño,
# solo precio/timing/acierto. smart_money_tracker.py::trades_de_mercado ya
# usa el mismo endpoint /trades y confirma que trae 'size' (en SHARES, no
# USD -- verificado en vivo: size=2, price=0.51 en un trade BTC 5min real).
# size_usd = size*precio, el importe real arriesgado en esa compra. Filas
# viejas (antes de este cambio) no tienen esta columna -- mismo patrón ya
# usado para compro_yes (16-Jul), DictReader/DictWriter lo manejan sin
# fallar (restval='').
# compro_yes (16-Jul, petición Javi tras corrección de
# idea_vigia_ballenas_tiempo_real_no_viable_16jul): antes solo se guardaba
# si el trade acertó, no de qué LADO apostó — sin el lado no se puede medir
# si la CONCENTRACIÓN del flujo de ballenas en un mercado concreto (no solo
# el agregado histórico banda+ventana que ya usa PYCONFIRMADO) predice el
# resultado. Filas viejas (antes de este cambio) no tienen esta columna;
# _cargar_historia_podada las relee sin fallar (DictWriter usa restval=''
# para la clave que falta) — quedan con compro_yes='' y se filtran aparte
# en cualquier análisis de dosis-respuesta futuro.


def _cargar_json(path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _parse_dt(s):
    if not s:
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def _universo_mercados_resueltos(ahora):
    """Todos los mercados Up-or-Down (5/15/60/240min) + WEEKLY_PRICE ya
    resueltos (end_date pasado, con margen) vistos en TODO
    data/markets/*.csv disponible. A diferencia de
    smart_money_tracker.mercados_recientes() (ventana fija 30h, pensada
    para su propio propósito de consenso reciente), aquí cada marco tiene
    su propia ventana — weekly tarda semanas en acumular n."""
    margen = timedelta(minutes=MARGEN_RESOLUCION_MIN)
    por_marco = defaultdict(dict)  # marco -> {condition_id: info}
    for archivo in sorted(DIR_MARKETS.glob("*.csv")):
        try:
            with open(archivo, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    cid = row.get("condition_id", "")
                    mid = row.get("market_id", "")
                    if not cid or not mid:
                        continue
                    end_dt = _parse_dt(row.get("end_date", ""))
                    if end_dt is None or end_dt > ahora - margen:
                        continue
                    tags = (row.get("event_tags") or "").split("|")
                    question = row.get("question") or ""
                    duracion = next((TAG_A_DURACION[t] for t in tags if t in TAG_A_DURACION), None)
                    if duracion is not None and "Up or Down" not in question:
                        continue
                    elif duracion is None and "Up or Down" not in question and (
                        "weekly" in [t.lower() for t in tags] or "week" in question.lower()
                    ):
                        duracion = "weekly"
                    # Detección de activo por NOMBRE COMPLETO en la pregunta
                    # (bitcoin/ethereum/solana/xrp), NUNCA por ticker/tag —
                    # Polymarket etiqueta estos mercados con el nombre
                    # completo ("Bitcoin", no "BTC"), y "btc" no es substring
                    # de "bitcoin". Bug real encontrado en producción: la
                    # primera versión de este filtro (copiada de
                    # smart_money_tracker.mercados_recientes(), que tiene el
                    # mismo bug) solo detectaba ETH/SOL (ticker=substring
                    # casual del nombre) y XRP (ticker=nombre) — BTC quedaba
                    # silenciosamente fuera de TODO el universo, 0 filas en
                    # 30k+ trades acumulados hasta que Javi lo notó. Mismo
                    # mapeo NOMBRE_A_TICKER que ya usa la rama weekly (que
                    # sí detectaba BTC bien) — unificado para las dos ramas.
                    activo = next((tk for nombre, tk in NOMBRE_A_TICKER.items()
                                   if nombre in question.lower()), None)
                    if duracion is None or not activo:
                        continue
                    por_marco[duracion][cid] = {
                        "condition_id": cid, "market_id": mid,
                        "activo": activo, "marco": duracion,
                        "end_date": end_dt.isoformat(),
                    }
        except Exception as e:
            print(f"  [warn] leyendo {archivo}: {e}")
    return {marco: list(d.values()) for marco, d in por_marco.items()}


def _seleccionar_nuevos(universo, procesados, ahora):
    seleccion = []
    for marco, mercados in universo.items():
        corte = ahora - timedelta(hours=VENTANA_LOOKBACK_HORAS.get(marco, 24 * 30))
        candidatos = [m for m in mercados if m["condition_id"] not in procesados
                      and _parse_dt(m["end_date"]) >= corte]
        random.shuffle(candidatos)
        cuota = CUOTA_POR_MARCO.get(marco, 10)
        seleccion.extend(candidatos[:cuota])
    return seleccion


def _procesar_mercados(seleccion):
    """Descarga resolución oficial + trades reales de los mercados
    seleccionados. Devuelve (filas nuevas para el histórico, resultado
    por condition_id 'ok'/'sin_resolucion' — solo 'ok' se marca procesado,
    lo demás se reintenta el ciclo siguiente)."""
    if not seleccion:
        return [], {}
    market_ids = [m["market_id"] for m in seleccion]
    print(f"  Resolviendo {len(market_ids)} mercados nuevos (gamma-api)...")
    resueltos = fetch_mercados_paralelo(market_ids, workers=3)

    filas = []
    resultado_por_cid = {}
    for m in seleccion:
        cid = m["condition_id"]
        resultado_por_cid[cid] = "sin_resolucion"
        mercado = resueltos.get(m["market_id"])
        if not mercado:
            continue
        precios = parse_outcome_prices(mercado.get("outcomePrices"))
        if not precios or len(precios) < 2:
            continue
        try:
            py, pn = float(precios[0]), float(precios[1])
        except (ValueError, TypeError):
            continue
        if abs(py - 1.0) < 0.01:
            outcome_real = "YES"
        elif abs(pn - 1.0) < 0.01:
            outcome_real = "NO"
        else:
            continue  # aún no liquidado limpio, se reintenta el ciclo siguiente
        end_dt = _parse_dt(mercado.get("endDate") or m["end_date"])
        if end_dt is None:
            continue
        for t in trades_de_mercado(cid):
            # SOLO compras: /trades devuelve BUY y SELL mezclados. Una venta
            # ("Up" SELL a 0.99) no es una apuesta direccional a ese precio —
            # es cerrar/reducir una posición ya abierta (toma de beneficio,
            # corte de pérdida, etc.), economía distinta de una compra fresca.
            # El análisis manual original (14-Jul, vía /activity) ya filtraba
            # side=="BUY" explícitamente; se perdió al cambiar a /trades para
            # muestrear TODAS las wallets en vez de una lista precocinada —
            # sin este filtro, mezclar compras y ventas contamina el z-test
            # y el hit-rate con una población que no está apostando nada.
            if (t.get("side") or "").strip().upper() != "BUY":
                continue
            w = t.get("proxyWallet")
            ts = t.get("timestamp")
            precio = t.get("price")
            outcome = (t.get("outcome") or "").strip().lower()
            if not w or ts is None or precio is None or outcome not in ("up", "down", "yes", "no"):
                continue
            try:
                t_dt = datetime.fromtimestamp(float(ts), tz=timezone.utc)
                precio = float(precio)
            except (ValueError, TypeError, OSError):
                continue
            # size_usd: tamaño real arriesgado (size en SHARES * precio). Si
            # falta o es inválido, la fila se conserva igual (precio/timing/
            # acierto siguen siendo válidos) pero size_usd queda vacío -- no
            # descartar el trade entero por un campo opcional nuevo.
            try:
                size_usd = round(float(t.get("size")) * precio, 2)
            except (TypeError, ValueError):
                size_usd = ""
            restante_min = (end_dt - t_dt).total_seconds() / 60.0
            if restante_min < -2:  # trade posterior al cierre — dato corrupto
                continue
            dur_nominal = MARCO_DURACION_MIN.get(m["marco"])
            if dur_nominal is not None and restante_min > dur_nominal + BUFFER_DURACION_MIN:
                continue  # fuera de lo físicamente posible para este marco — etiquetado corrupto
            compro_yes = outcome in ("up", "yes")
            acierto = (compro_yes and outcome_real == "YES") or (not compro_yes and outcome_real == "NO")
            filas.append({
                "condition_id": cid, "activo": m["activo"], "marco": m["marco"],
                "ts_trade": t_dt.isoformat(), "wallet": w, "precio": round(precio, 4),
                "restante_min": round(restante_min, 2), "acierto": int(acierto),
                "compro_yes": int(compro_yes), "size_usd": size_usd,
            })
        resultado_por_cid[cid] = "ok"
    return filas, resultado_por_cid


def _append_history(filas):
    nuevo = not HISTORY_CSV.exists()
    if not nuevo:
        # Auto-heal de cabecera obsoleta (22-Jul, al añadir size_usd): si el
        # fichero ya existe con una cabecera de un esquema anterior (menos
        # columnas), un append directo desalinearía csv.DictReader para las
        # filas NUEVAS de este ciclo hasta que _cargar_historia_podada
        # corrigiera la cabecera más tarde en el mismo main() -- se cura
        # aquí primero, reusando esa misma rutina de poda+reescritura ya
        # probada (mismo patrón que la migración de compro_yes, 16-Jul).
        # Tras la primera corrida post-deploy la cabecera ya coincide y
        # este chequeo es un no-op barato en cada ciclo siguiente.
        with open(HISTORY_CSV, encoding="utf-8") as f:
            cabecera_actual = f.readline().strip().split(",")
        if cabecera_actual != HISTORY_COLS:
            _cargar_historia_podada(datetime.now(timezone.utc))
    with open(HISTORY_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HISTORY_COLS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)


def _cargar_historia_podada(ahora):
    """Carga el histórico y lo poda a la ventana de retención propia de
    cada marco, para que el patrón medido sea siempre reciente. Reescribe
    el CSV ya podado para que no crezca sin límite."""
    if not HISTORY_CSV.exists():
        return []
    filas = []
    with open(HISTORY_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ts = _parse_dt(row.get("ts_trade", ""))
            marco = row.get("marco", "")
            if ts is None:
                continue
            corte = ahora - timedelta(hours=VENTANA_LOOKBACK_HORAS.get(marco, 24 * 30))
            if ts < corte:
                continue
            try:
                row["precio"] = float(row["precio"])
                row["restante_min"] = float(row["restante_min"])
                row["acierto"] = bool(int(row["acierto"]))
            except (ValueError, KeyError, TypeError):
                continue
            # compro_yes puede faltar en filas anteriores a este campo (16-Jul)
            # — se deja como None (desconocido), no se descarta la fila entera
            # solo por eso (acierto/precio/restante_min siguen siendo válidos).
            cy = row.get("compro_yes", "")
            row["compro_yes"] = bool(int(cy)) if cy not in (None, "") else None
            filas.append(row)
    with open(HISTORY_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HISTORY_COLS)
        w.writeheader()
        for row in filas:
            cy = row["compro_yes"]
            w.writerow({**row, "acierto": int(row["acierto"]),
                        "compro_yes": "" if cy is None else int(cy)})
    return filas


def _stats_banda(filas):
    n = len(filas)
    if n == 0:
        return None
    hit = sum(1 for r in filas if r["acierto"]) / n
    precio_medio = sum(r["precio"] for r in filas) / n
    if not (0 < precio_medio < 1):
        return None
    se = math.sqrt(precio_medio * (1 - precio_medio) / n)
    z = (hit - precio_medio) / se if se > 0 else 0.0
    pnl_por_wallet = defaultdict(float)
    pnl_total = 0.0
    for r in filas:
        pnl = (1 - r["precio"]) if r["acierto"] else -r["precio"]
        pnl_por_wallet[r["wallet"]] += pnl
        pnl_total += pnl
    top1 = max(pnl_por_wallet.values()) if pnl_por_wallet else 0.0
    # Sin PnL positivo agregado no hay "cuota del edge" que medir — se
    # trata como concentrado (1.0), no pasa TOP1_MAX de todos modos porque
    # tampoco pasaría Z_MIN con un patrón perdedor.
    top1_share = (top1 / pnl_total) if pnl_total > 0 else 1.0
    return {"n": n, "hit": round(hit, 4), "precio_medio": round(precio_medio, 4),
            "z": round(z, 3), "n_wallets": len(pnl_por_wallet), "top1_share": round(top1_share, 3)}


def _timing_ganadoras(filas):
    restantes = sorted(r["restante_min"] for r in filas if r["acierto"])
    n = len(restantes)
    if n < 5:
        return None
    return {
        "rest_p25": round(restantes[n // 4], 2),
        "rest_mediana": round(restantes[n // 2], 2),
        "rest_p75": round(restantes[3 * n // 4], 2),
        "n_ganadoras": n,
    }


def _calcular_estado(filas_historia, ahora):
    por_combo = defaultdict(lambda: defaultdict(list))  # (activo,marco) -> {(lo,hi): filas}
    for r in filas_historia:
        clave = (r["activo"], r["marco"])
        for lo, hi in BANDAS_PRECIO:
            if lo <= r["precio"] < hi or (hi == 1.00 and r["precio"] == 1.00):
                por_combo[clave][(lo, hi)].append(r)
                break

    estado = {}
    for (activo, marco), bandas in por_combo.items():
        tabla = []
        mejor = None
        for (lo, hi), filas in bandas.items():
            s = _stats_banda(filas)
            if s is None or s["n"] < N_MIN_INFORMATIVO:
                continue
            pasa = (s["n"] >= N_MIN and s["z"] >= Z_MIN and s["top1_share"] < TOP1_MAX)
            tabla.append({"banda_lo": lo, "banda_hi": hi, "pasa_gates": pasa, **s})
            # La banda [0.90,1.00) queda FUERA de la selección aunque pase las
            # 3 barras: es la zona de "confirmación total", con el libro más
            # fino cerca del cierre (mismo motivo por el que el análisis
            # manual del 14-Jul acotó la banda a [0.70,0.90) y no a [0.70,1.00)
            # — un edge de 2-4 céntimos ahí no sobrevive fee real del CLOB,
            # ~3.8% mediana, ver nota nested_arb en config_live.json). Se
            # sigue reportando en la tabla (informativo), nunca se activa.
            if pasa and hi < 1.00 and (mejor is None or s["z"] > mejor["z"]):
                mejor = {"lo": lo, "hi": hi, **s, "filas": filas}
        tabla.sort(key=lambda e: -e["z"])
        clave = f"{activo}#{marco}"
        significativo = mejor is not None
        entrada = {
            "significativo": significativo,
            "bandas": [{k: v for k, v in e.items() if k != "filas"} for e in tabla],
            "actualizado": ahora.isoformat(timespec="seconds"),
        }
        if significativo:
            timing = _timing_ganadoras(mejor["filas"])
            entrada.update({
                "banda_lo": mejor["lo"], "banda_hi": mejor["hi"],
                "z": mejor["z"], "n": mejor["n"], "n_wallets": mejor["n_wallets"],
                "top1_share": mejor["top1_share"],
            })
            if timing:
                entrada.update({
                    "rest_lo_min": timing["rest_p25"],
                    "rest_hi_min": timing["rest_p75"],
                    "rest_mediana_min": timing["rest_mediana"],
                    "n_ganadoras": timing["n_ganadoras"],
                })
            else:
                entrada["significativo"] = False  # sin timing fiable, no usable como filtro vivo
        estado[clave] = entrada
    estado["_actualizado"] = ahora.isoformat(timespec="seconds")
    return estado


def main():
    ahora = datetime.now(timezone.utc)
    print(f"[ballenas_observer] {ahora.isoformat(timespec='seconds')}")

    universo = _universo_mercados_resueltos(ahora)
    print("  Universo de mercados resueltos disponibles: " +
          ", ".join(f"{k}={len(v)}" for k, v in sorted(universo.items())))

    procesados = _cargar_json(CACHE_PROCESADOS, {})
    seleccion = _seleccionar_nuevos(universo, procesados, ahora)
    reparto = {m: sum(1 for s in seleccion if s["marco"] == m) for m in CUOTA_POR_MARCO}
    print(f"  Mercados nuevos a procesar este ciclo: {len(seleccion)} {reparto}")

    filas_nuevas, resultado_por_cid = _procesar_mercados(seleccion)
    print(f"  Trades nuevos recolectados: {len(filas_nuevas)}")
    if filas_nuevas:
        _append_history(filas_nuevas)

    for m in seleccion:
        if resultado_por_cid.get(m["condition_id"]) == "ok":
            procesados[m["condition_id"]] = {"marco": m["marco"], "end_date": m["end_date"],
                                              "procesado": ahora.isoformat(timespec="seconds")}
        # "sin_resolucion" no se marca procesado -> se reintenta el ciclo siguiente

    # Poda de la cache de procesados para que no crezca sin límite.
    max_retencion = max(VENTANA_LOOKBACK_HORAS.values())
    corte_cache = ahora - timedelta(hours=max_retencion + 24)
    procesados = {cid: info for cid, info in procesados.items()
                  if (_parse_dt(info.get("end_date", "")) or ahora) >= corte_cache}
    CACHE_PROCESADOS.write_text(json.dumps(procesados, indent=2), encoding="utf-8")

    historia = _cargar_historia_podada(ahora)
    print(f"  Histórico rolling tras poda: {len(historia)} trades")

    estado = _calcular_estado(historia, ahora)
    STATE_JSON.write_text(json.dumps(estado, indent=2, ensure_ascii=False), encoding="utf-8")

    sig = sorted(k for k, v in estado.items() if isinstance(v, dict) and v.get("significativo"))
    print(f"  Combos significativos ({len(sig)}): {sig}")


if __name__ == "__main__":
    sys.exit(main() or 0)
