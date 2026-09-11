#!/usr/bin/env python3
"""analisis_manipulacion_twap_flash_move_10ago.py -- Prioridad nueva
10-Ago (petición explícita Javi, tras hilo externo verificado con datos
propios): mide, con nuestros propios datos de precio Chainlink y nuestros
propios resultados, cuántos mercados BTC/ETH#5min/15min post-TWAP (07-Ago
en adelante) muestran la firma de "flash move" descrita en el hilo --
movimiento de precio anómalo en los últimos ~30-45s antes del cierre,
justo antes/al empezar la ventana de promedio TWAP -- y si esas ventanas
tienen un hit-rate/pnl distinto en nuestras propias operaciones reales.

Verificado ANTES de escribir este script: el ejemplo concreto del hilo
(BTC 07-Ago 22:54:23-22:54:31 UTC, caída de $64887 a $64847) replica
CASI EXACTO en data/prices/chainlink_2026-08-07.csv, fuente independiente
nuestra -- no es una afirmación sin verificar de terceros.

Metodología (primera pasada, deliberadamente simple -- afinar si el
hallazgo inicial lo justifica):
  1. Para cada asset/día, cargar la serie de precio Chainlink completa.
  2. Para cada mercado resuelto BTC/ETH#5min/15min desde el 07-Ago
     (results.csv, filas únicas por market_id), calcular:
     - pre  = precio en (close - VENTANA_PRE_S)
     - post = precio en (close - MARGEN_FINAL_S) (justo antes del cierre)
     - movimiento = (post - pre) / pre, en pb (puntos básicos)
  3. Baseline de movimiento "normal" para ese asset/día: mismo cálculo
     sobre TODAS las ventanas de VENTANA_PRE_S segundos que empiezan cada
     minuto ese día (no solo los cierres de mercado) -- percentil 95 del
     valor absoluto = umbral de "anómalo".
  4. Cruzar market_id con results.csv: hit-rate/pnl_neto de NUESTRAS
     operaciones reales en mercados marcados vs no marcados.

Solo lectura, no toca dinero ni ninguna decisión -- medición pura, tal
y como pidió Javi antes de decidir si construir un detector activo."""
import bisect
import csv
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data/shadow/results.csv"
CORTE_TWAP = datetime(2026, 8, 7, tzinfo=timezone.utc)

VENTANA_PRE_S = 40   # segundos antes del cierre para el precio "pre"
MARGEN_FINAL_S = 3   # segundos antes del cierre para el precio "post"
# 10-Ago, ampliado a petición de Javi ("ponlo para todos, no cuesta mucho
# y estamos cubiertos al máximo"): las 6 monedas con captura Chainlink
# propia (fetch_chainlink_prices.py) y los 4 marcos con TWAP real
# (5min/15min/60min/240min -- 60min usa TWAP de 60s igual que 15min per
# el anuncio oficial; "atexpiry"/"daily"/"reach"/"sniper" son mecanismos
# de resolución distintos, sin TWAP, fuera de alcance de este análisis).
ACTIVOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
MARCOS = {"5min", "15min", "60min", "240min"}


def _cargar_precios_dia(asset: str, fecha: str) -> tuple[list[float], list[float]]:
    """(timestamps epoch UTC ordenados, precios) -- separado en 2 listas
    paralelas para que bisect trabaje directo sobre floats, sin overhead
    de comparar datetimes en cada búsqueda."""
    path = REPO / f"data/prices/chainlink_{fecha}.csv"
    if not path.exists():
        return [], []
    pares = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("asset") != asset:
                continue
            try:
                ts = datetime.fromisoformat(row["timestamp_utc"])
                p = float(row["price_usd"])
            except (KeyError, ValueError):
                continue
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            pares.append((ts.timestamp(), p))
    pares.sort()
    if not pares:
        return [], []
    ts_lista, precios = zip(*pares)
    return list(ts_lista), list(precios)


def _precio_en(ts_lista: list[float], precios: list[float], t_epoch: float) -> float | None:
    """Búsqueda binaria (bisect) sobre la serie ordenada -- O(log n) por
    consulta, independiente del orden en que se pida t. La versión previa
    con "idx_hint" nunca pasaba el índice devuelto a la siguiente llamada
    (bug real: cada consulta volvía a arrancar desde 0), O(n) por llamada
    -- con ~1440 muestras/día de baseline + miles de mercados, eso hacía
    que _baseline_movimientos tardara minutos por asset-día y el script
    entero superara el timeout de 300s. Bisect es correcto sin importar
    el orden de las llamadas."""
    i = bisect.bisect_right(ts_lista, t_epoch)
    if i == 0:
        return None
    return precios[i - 1]


def _baseline_movimientos(ts_lista: list[float], precios: list[float]) -> list[float]:
    """Movimiento (pb) de VENTANA_PRE_S-MARGEN_FINAL_S segundos, muestreado
    cada 60s a lo largo del día -- distribución de referencia de "cuánto
    se mueve el precio normalmente" en una ventana de esa duración."""
    if not ts_lista:
        return []
    movs = []
    t0 = ts_lista[0] - (ts_lista[0] % 60)
    t_fin = ts_lista[-1]
    t = t0
    delta = VENTANA_PRE_S - MARGEN_FINAL_S
    while t < t_fin:
        p_pre = _precio_en(ts_lista, precios, t)
        p_post = _precio_en(ts_lista, precios, t + delta)
        if p_pre and p_post and p_pre > 0:
            movs.append(abs((p_post - p_pre) / p_pre) * 10000)
        t += 60
    return movs


def cargar_mercados_objetivo() -> dict:
    """market_id -> {activo, marco, close, filas:[results.csv rows]}."""
    mercados = {}
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            subtype = row.get("subtype", "")
            if "#" not in subtype:
                continue
            activo, marco = subtype.split("#", 1)
            if activo not in ACTIVOS or marco not in MARCOS:
                continue
            if row.get("acierto") not in ("0", "1"):
                continue
            try:
                ts_pred = datetime.fromisoformat(row["prediction_timestamp"].replace("Z", "+00:00"))
            except (KeyError, ValueError):
                continue
            if ts_pred < CORTE_TWAP:
                continue
            end_date = row.get("end_date", "")
            if not end_date:
                continue
            try:
                close = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
            except ValueError:
                continue
            if close.tzinfo is None:
                close = close.replace(tzinfo=timezone.utc)
            mid = row["market_id"]
            m = mercados.setdefault(mid, {"activo": activo, "marco": marco, "close": close, "filas": []})
            m["filas"].append(row)
    return mercados


def main():
    mercados = cargar_mercados_objetivo()
    print(f"[cargar_mercados_objetivo] {len(mercados)} mercados únicos BTC/ETH#5min/15min post-TWAP con resultado propio")

    por_activo_dia_serie = {}
    por_activo_dia_baseline = {}

    resultados_por_mercado = {}
    for mid, m in mercados.items():
        activo, close = m["activo"], m["close"]
        close_epoch = close.timestamp()
        fecha = close.date().isoformat()
        clave = (activo, fecha)
        if clave not in por_activo_dia_serie:
            por_activo_dia_serie[clave] = _cargar_precios_dia(activo, fecha)
            ts_lista, precios = por_activo_dia_serie[clave]
            por_activo_dia_baseline[clave] = _baseline_movimientos(ts_lista, precios)
        ts_lista, precios = por_activo_dia_serie[clave]
        if not ts_lista:
            continue
        p_pre = _precio_en(ts_lista, precios, close_epoch - VENTANA_PRE_S)
        p_post = _precio_en(ts_lista, precios, close_epoch - MARGEN_FINAL_S)
        if not p_pre or not p_post or p_pre <= 0:
            continue
        mov_pb = (p_post - p_pre) / p_pre * 10000
        baseline = por_activo_dia_baseline[clave]
        if not baseline:
            continue
        p95 = sorted(baseline)[int(0.95 * len(baseline))]
        anomalo = abs(mov_pb) > p95 and p95 > 0
        resultados_por_mercado[mid] = {
            "activo": activo, "marco": m["marco"], "close": close,
            "mov_pb": mov_pb, "p95_baseline_pb": p95, "anomalo": anomalo,
            "filas": m["filas"],
        }

    print(f"[medido] {len(resultados_por_mercado)} mercados con precio Chainlink disponible en la ventana pre-cierre\n")

    for activo in sorted(ACTIVOS):
        for marco in sorted(MARCOS):
            subset = [v for v in resultados_por_mercado.values() if v["activo"] == activo and v["marco"] == marco]
            if not subset:
                continue
            n_anomalos = sum(1 for v in subset if v["anomalo"])
            print(f"=== {activo}#{marco}: {len(subset)} mercados medidos, {n_anomalos} anómalos "
                  f"({100 * n_anomalos / len(subset):.1f}%) ===")

            for etiqueta, filtro in [("ANÓMALOS", lambda v: v["anomalo"]), ("normales", lambda v: not v["anomalo"])]:
                filas = [r for v in subset if filtro(v) for r in v["filas"]]
                if not filas:
                    print(f"  {etiqueta}: sin filas propias")
                    continue
                n = len(filas)
                hit = 100 * sum(1 for r in filas if r["acierto"] == "1") / n
                pnl = sum(float(r["pnl_neto"]) for r in filas) / n
                print(f"  {etiqueta}: n_filas_propias={n} hit={hit:.1f}% pnl_medio={pnl:+.4f}€ "
                      f"(mercados={sum(1 for v in subset if filtro(v))})")
            print()

    anomalos_top = sorted(resultados_por_mercado.items(), key=lambda kv: -abs(kv[1]["mov_pb"]))[:5]
    print("=== Top 5 movimientos más extremos detectados (verificación manual) ===")
    for mid, v in anomalos_top:
        print(f"  {v['activo']}#{v['marco']} market_id={mid} close={v['close'].isoformat()} "
              f"mov={v['mov_pb']:+.1f}pb (umbral p95={v['p95_baseline_pb']:.1f}pb) anomalo={v['anomalo']}")


if __name__ == "__main__":
    main()
