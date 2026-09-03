"""Latencia REAL del POST /order recorriendo el pipeline COMPLETO
(validacion + matching + taker delay) contra un mercado ABIERTO.

⚠️ HERRAMIENTA MANUAL -- NUNCA en cron ni en ningun watchdog/screen.
Envia ORDENES REALES al CLOB (que no pueden llenarse, ver seguridad
abajo). Se ejecuta a mano, cuando hace falta medir el presupuesto de
latencia del camino critico del sniper pre-cierre.

USO PREVISTO: repetir la medicion tras cada cambio de infraestructura de
Polymarket para cuantificar su impacto. Linea base 03-Sep 19:45 UTC (taker
delay 50ms): POST mediana=179,9ms p95=250,8ms max=275,5ms; camino critico
completo ~247ms mediana / ~380ms peor caso. Siguiente medicion obligada:
04-Sep despues de las 14:00 UTC, cuando el taker delay pase a 150ms.
Ver memoria project_diseno_ejecutor_precierre_camino_critico_03sep.

SEGURIDAD -- por que esto no puede perder dinero:
  - Orden BUY FOK con precio limite MUY por debajo del mejor ask (limite
    ~0.02 cuando el ask ronda 0.50). FOK es todo-o-nada Y el limite acota
    el precio MAXIMO a pagar.
  - Nadie vende a 0.02 algo que cotiza a ~0.50, asi que se mata sin fill.
  - Si por un milagro se llenara, habriamos comprado a 0.02 algo que vale
    ~0.50: el riesgo es ASIMETRICO A FAVOR. Exposicion maxima 1.05EUR.
  - No escribe en trades.csv ni toca ningun ledger/circuit breaker.

Esta es la medicion que SI incluye el taker delay (50ms hoy -> 150ms desde
04-Sep 14:00 UTC), por lo que sirve de linea base para medir ese cambio.
"""
import statistics
import sys
import time

sys.path.insert(0, "/root/polymarket-research")

import live_trade as lt  # noqa: E402
from resolution_sniper_observer import token_ids, mercado_slot  # noqa: E402

DUR_S = 300
STAKE = 1.05
LIMITE = 0.02   # muy por debajo de cualquier ask real -> no puede llenar
N = 8


def main() -> None:
    ahora = time.time()
    ts_end = (int(ahora) // DUR_S + 1) * DUR_S
    if ts_end - ahora < 45:          # no medir pegado al cierre
        ts_end += DUR_S
    mkt = slug = None
    for asset in ("BTC", "ETH", "SOL"):
        slug, mkt = mercado_slot(asset, "5m", ts_end - DUR_S)
        if mkt:
            break
    if not mkt:
        print("sin mercado abierto")
        return
    token_yes, _ = token_ids(mkt)

    depth = lt._consultar_profundidad_libro(None, token_yes, 0.50, STAKE)
    ask = depth.get("mejor_ask")
    print(f"mercado ABIERTO {slug} | mejor_ask={ask} | limite FOK={LIMITE} "
          f"(cierra en {ts_end-time.time():.0f}s)")
    if not isinstance(ask, (int, float)) or ask <= LIMITE * 2:
        print(f"ABORTADO: ask={ask} demasiado cerca del limite -- podria llenar")
        return

    client = lt._get_clob_client()
    if client is None:
        print("sin cliente CLOB")
        return
    from py_clob_client_v2 import MarketOrderArgsV2, OrderType  # noqa: E402

    a0 = MarketOrderArgsV2(token_id=token_yes, amount=STAKE, side="BUY", price=LIMITE)
    t0 = time.perf_counter()
    client.create_market_order(a0)
    print(f"  firma de calentamiento: {(time.perf_counter()-t0)*1000:.0f}ms")

    t_post, t_firma = [], []
    for i in range(N):
        args = MarketOrderArgsV2(token_id=token_yes, amount=STAKE, side="BUY", price=LIMITE)
        tf = time.perf_counter()
        signed = client.create_market_order(args)
        t_firma.append((time.perf_counter() - tf) * 1000)
        t0 = time.perf_counter()
        try:
            resp = client.post_order(signed, OrderType.FOK)
            estado = f"RESP:{str(resp)[:90]}"
        except Exception as e:
            estado = f"{type(e).__name__}: {str(e)[:80]}"
        dt = (time.perf_counter() - t0) * 1000
        t_post.append(dt)
        print(f"  post {i+1}: {dt:7.1f}ms -> {estado}")
        time.sleep(0.4)

    def res(nombre, xs):
        s = sorted(xs)
        p95 = s[int(len(s) * 0.95) - 1] if len(s) > 1 else s[0]
        print(f"{nombre:<12} mediana={statistics.median(xs):7.1f}ms  p95={p95:7.1f}ms  max={max(xs):7.1f}ms")

    print()
    res("firma", t_firma)
    res("POST /order", t_post)
    print()
    print(f"CAMINO CRITICO COMPLETO (book 61ms + firma + POST): "
          f"~{61+statistics.median(t_firma)+statistics.median(t_post):.0f}ms mediana / "
          f"~{89+max(t_firma)+max(t_post):.0f}ms peor caso")


if __name__ == "__main__":
    main()
