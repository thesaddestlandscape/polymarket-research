#!/usr/bin/env python3
"""
resolution_sniper_precierre_executor.py — ejecutor de baja latencia
RESOLUTION_SNIPER_PRECIERRE. Arquitectura obligatoria de
project_diseno_ejecutor_precierre_camino_critico_03sep (Javi, 03-Sep,
textual: "cuando toque ya sabes como lo tiene que hacer, grabatelo a
fuego"): todo lo caro se resuelve en la fase de PRECÁLCULO (T-12s del
instante objetivo), y en el INSTANTE objetivo (offset=-2s respecto al
cierre nominal) solo se hace 1 lectura de libro + firma + POST — nunca
pasa por live_trade._ejecutar_orden_polymarket. Ese camino genérico
gasta ~2s enteros en vetos de ballenas/re-quote/re-chequeo multi-lectura
(pensados para señales con ~20s de vida útil), y fue la causa real y
medida de que la prueba controlada del 03-Sep fallara con "trading is
disabled" exactamente en el segundo del cierre — NO fue el muro de
Polymarket, fue latencia propia (ver la memoria de diseño para el
desglose completo por tramo: GET/book 61ms, firma 3-6ms con caché
caliente, POST/order 180-277ms incl. taker delay).

Presupuesto medido 03-Sep (VPS Helsinki): camino crítico completo
~247ms mediana / ~380ms peor caso (con taker delay 50ms), ~347/480ms
desde el 04-Sep 14:00 UTC (taker delay sube a 150ms). Offset -2s da
2000ms de presupuesto → margen 4,2x sobre el peor caso medido.

DRY_RUN=True por defecto (04-Sep, construcción inicial): recorre TODO
el camino crítico incluida la FIRMA real (mide t_firma real, coste cero
— firmar no gasta nada ni se envía a ningún sitio) pero nunca llama a
post_order, así que no puede mover un solo euro. Pasar a DRY_RUN=False
requiere /code-review + aprobación EXPLÍCITA de Javi (mismo criterio que
ballenas_executor_15min.py: el flag de módulo gobierna qué se ejecuta de
verdad, con independencia de pares_permitidos_live — esta tupla no está
ahí todavía, igual que RESOLUTION_SNIPER_PRECIERRE_TEST no lo estuvo).

Sirve TAMBIÉN como medición continua de latencia in-situ (sustituye,
para el día a día, la repetición manual de medir_latencia_camino_
critico.py — esa herramienta sigue siendo la referencia para medir el
taker delay puro tras un cambio de infraestructura de Polymarket, pero
esto mide el camino real completo incluido el gate en cada ventana real):
cada intento evaluado (dispare orden o no) se registra en
data/shadow/resolution_sniper_precierre_executor_dryrun.csv con
t_lectura_ms/t_firma_ms y el veredicto del gate.

Gate: resolution_sniper_precierre_gate.evaluar(activo, ask, offset_s) —
relee el JSON del disco cada vez (caché por mtime), exige convergencia
grid+fino, fail-closed si no hay evidencia de ESE offset exacto. A
04-Sep solo BTC#5min tiene evidencia confirmada (n=74) — el resto de
activos se evalúan igual (nunca se hardcodea una tabla de zonas, ver F5
en project_lecciones_aprendidas_estrategias) y confirmarán solos en
cuanto n crezca lo suficiente.
"""
import csv
import time
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
import live_guard
import live_stake
import resolution_sniper_precierre_gate as gate
from resolution_sniper_observer import ASSETS, mercado_slot, token_ids, _TAIL

REPO = Path(__file__).resolve().parent
DUR_S = 300
MARCO_TAG = "5m"
SUBTYPE_SUFFIX = "5min"
OFFSET_S = -2                # medido y elegido 03-Sep -- ver docstring arriba
STAKE_EUR = 1.05             # suelo CLOB, mismo criterio que la prueba controlada del 02-Sep
MIN_RATIO_PROFUNDIDAD = 5.0  # mismo umbral que el resto del proyecto
PRECALCULO_ANTES_S = 12      # arrancar precálculo con margen sobre el instante objetivo
DRY_RUN = True                # 04-Sep: construcción inicial -- ver docstring arriba.
STRATEGY = "RESOLUTION_SNIPER_PRECIERRE"

OUT_LOG = REPO / "data" / "shadow" / "resolution_sniper_precierre_executor_dryrun.csv"
_CAMPOS = [
    "timestamp_utc", "ts_end", "dry_run", "activo", "direccion_implicita", "ask_implicita",
    "gate_confirmado", "gate_motivo", "ratio_vs_stake", "vwap_fill_estimado",
    "t_lectura_ms", "t_firma_ms", "t_total_ms", "disparado", "order_ok", "order_error",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _append_csv(row: dict) -> None:
    nuevo = not OUT_LOG.exists()
    with open(OUT_LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=_CAMPOS)
        if nuevo:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in _CAMPOS})


class _Precalculo:
    """Todo lo caro de esta ventana, resuelto ANTES del instante objetivo:
    mercado/tokens por activo (Gamma API, cacheada por mercado_slot) y
    cliente CLOB calentado (paga aquí los 193-278ms de la PRIMERA firma,
    nunca en el disparo)."""

    def __init__(self):
        self.ts_end = None
        self.mercados = {}
        self.client = None

    def preparar(self, ts_end: int) -> None:
        self.ts_end = ts_end
        ts_start = ts_end - DUR_S
        self.mercados = {}
        for activo in ASSETS:
            _slug, mkt = mercado_slot(activo, MARCO_TAG, ts_start)
            if not mkt:
                continue
            token_yes, token_no = token_ids(mkt)
            if not token_yes or not token_no:
                continue
            ref_open = _TAIL.precio_en(activo, ts_start) or _TAIL.precio_en(activo, ts_start + 2)
            self.mercados[activo] = {
                "market_id": mkt.get("id", ""), "question": mkt.get("question", ""),
                "end_date": mkt.get("endDate", ""),
                "token_yes": token_yes, "token_no": token_no, "ref_open": ref_open,
            }
        if self.client is None:
            try:
                self.client = lt._get_clob_client()
            except Exception as e:
                _log(f"aviso: no se pudo crear cliente CLOB ({e})")
                self.client = None
        if self.client is not None and self.mercados:
            try:
                from py_clob_client_v2 import MarketOrderArgsV2
                primer_token = next(iter(self.mercados.values()))["token_yes"]
                # firma de descarte a precio absurdo (nunca se envía) --
                # paga aquí el coste de la PRIMERA firma (fetch tick_size/
                # neg_risk), fuera del camino crítico.
                self.client.create_market_order(
                    MarketOrderArgsV2(token_id=primer_token, amount=STAKE_EUR, side="BUY", price=0.01))
            except Exception as e:
                _log(f"aviso: no se pudo calentar la firma ({e})")


def _profundidad_correcta(token_id: str, stake_eur: float) -> dict:
    """Mismo cálculo que live_trade._consultar_profundidad_libro (téco =
    mejor_ask*1.05, banda real sobre el precio de entrada), pero SIN pasar
    un precio_entrada adivinado: aquí se lee el libro UNA sola vez y se
    ancla el techo al mejor_ask REAL descubierto en esa misma lectura, no a
    un precio_entrada de partida. NO se toca _consultar_profundidad_libro
    (código de seguridad live, CLAUDE.md: no tocar para reutilizar parseo
    con código nuevo) — se replica su lógica aquí en su lugar.

    /code-review 04-Sep, hallazgo real: pasar precio_entrada=1.0 (para
    'cubrir todo el rango de precio' antes de conocer el ask) hacía
    techo=1.05 -- por encima del precio máximo posible (1.0) de un mercado
    binario, así que TODOS los niveles del libro entraban en la suma de
    profundidad, incluidos los que están lejísimos del precio real de
    fill. ratio_vs_stake medía la profundidad de TODO el libro, no la
    profundidad cerca del mejor ask (lo único que importa para una orden
    marketable) -- el gate de profundidad podía pasar con MIN_RATIO_
    PROFUNDIDAD=5.0 aunque el libro estuviera vacío justo donde se
    ejecutaría la orden."""
    book = lt._fetch_book_publico(token_id)
    if book is None:
        return {"ok": False, "error": "sin respuesta del libro (público)"}
    asks = book.get("asks") or []
    mejor_ask = None
    for lvl in asks:
        try:
            p = float(lvl.get("price"))
        except (TypeError, ValueError, AttributeError):
            continue
        if mejor_ask is None or p < mejor_ask:
            mejor_ask = p
    if mejor_ask is None:
        return {"ok": True, "mejor_ask": None, "profundidad_eur": 0.0, "n_niveles": len(asks),
                "ratio_vs_stake": 0.0, "vwap_fill_estimado": None, "fill_completo_en_niveles": False}
    techo = mejor_ask * 1.05
    profundidad_eur = 0.0
    for lvl in asks:
        try:
            p = float(lvl.get("price"))
            s = float(lvl.get("size"))
        except (TypeError, ValueError, AttributeError):
            continue
        if p <= techo:
            profundidad_eur += p * s
    ratio = (profundidad_eur / stake_eur) if stake_eur > 0 else None
    vwap_fill_estimado, fill_completo_en_niveles = lt.vwap_fill_desde_niveles(asks, stake_eur, mejor_ask)
    return {
        "ok": True, "mejor_ask": mejor_ask, "profundidad_eur": round(profundidad_eur, 2),
        "n_niveles": len(asks), "ratio_vs_stake": round(ratio, 1) if ratio is not None else None,
        "vwap_fill_estimado": vwap_fill_estimado, "fill_completo_en_niveles": fill_completo_en_niveles,
    }


def _instante_critico(pre: _Precalculo, activo: str) -> dict | None:
    """El camino crítico de verdad: 1 lectura de libro + gate en memoria +
    firma (+ POST solo si DRY_RUN=False). None si este activo no tiene
    mercado resuelto o precio Chainlink todavía."""
    m = pre.mercados.get(activo)
    if not m or m["ref_open"] is None or m["ref_open"] <= 0:
        return None

    precio_actual = _TAIL.precio_ultimo(activo)
    if precio_actual is None:
        return None
    if precio_actual > m["ref_open"]:
        dir_impl = "Up"
    elif precio_actual < m["ref_open"]:
        dir_impl = "Down"
    else:
        return None
    direction = "BUY_YES" if dir_impl == "Up" else "BUY_NO"
    token_id = m["token_yes"] if dir_impl == "Up" else m["token_no"]

    # ÚNICA lectura de libro del instante crítico (~61ms mediana, /book
    # público, sin cliente autenticado) -- ver _profundidad_correcta() para
    # por qué no se usa live_trade._consultar_profundidad_libro aquí
    # directamente (habría que pasarle un precio_entrada adivinado).
    t0 = time.perf_counter()
    depth = _profundidad_correcta(token_id, STAKE_EUR)
    t_lectura_ms = (time.perf_counter() - t0) * 1000
    base = {"activo": activo, "direccion_implicita": dir_impl, "t_lectura_ms": round(t_lectura_ms, 1)}
    if not depth.get("ok"):
        return {**base, "gate_confirmado": False, "gate_motivo": "sin_libro"}

    ask = depth.get("mejor_ask")
    if ask is None:
        return {**base, "gate_confirmado": False, "gate_motivo": "sin_ask"}

    veredicto = gate.evaluar(activo, ask, OFFSET_S)
    ratio = depth.get("ratio_vs_stake")
    resultado = {
        **base, "ask_implicita": ask,
        "gate_confirmado": veredicto["confirmado"], "gate_motivo": veredicto["motivo"],
        "ratio_vs_stake": ratio, "vwap_fill_estimado": depth.get("vwap_fill_estimado"),
    }
    if not veredicto["confirmado"]:
        return resultado
    if ratio is None or ratio < MIN_RATIO_PROFUNDIDAD:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = f"profundidad_insuficiente_ratio={ratio}"
        return resultado
    if pre.client is None:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = "sin_cliente_clob"
        return resultado

    from py_clob_client_v2 import MarketOrderArgsV2, OrderType
    precio_orden = ask if dir_impl == "Up" else round(1.0 - ask, 6)
    t1 = time.perf_counter()
    try:
        args = MarketOrderArgsV2(token_id=token_id, amount=STAKE_EUR, side="BUY", price=ask)
        signed = pre.client.create_market_order(args)
        t_firma_ms = (time.perf_counter() - t1) * 1000
    except Exception as e:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = f"error_firma:{e}"
        return resultado
    resultado["t_firma_ms"] = round(t_firma_ms, 1)

    if DRY_RUN:
        resultado["disparado"] = False
        _log(f"[DRY-RUN] {activo} {direction} ask={ask} gate={veredicto['motivo']} "
             f"ratio={ratio} t_lectura={t_lectura_ms:.0f}ms t_firma={t_firma_ms:.0f}ms "
             f"-- NO se envía (DRY_RUN=True)")
        return resultado

    # ---- Solo alcanzable con DRY_RUN=False, tras /code-review + aprobación explícita de Javi ----
    t2 = time.perf_counter()
    try:
        resp = pre.client.post_order(signed, OrderType.FOK)
        ok, error = True, None
    except Exception as e:
        resp, ok, error = None, False, str(e)
    t_post_ms = (time.perf_counter() - t2) * 1000
    resultado["disparado"] = True
    resultado["order_ok"] = ok
    resultado["order_error"] = error
    resultado["t_total_ms"] = round(t_lectura_ms + t_firma_ms + t_post_ms, 1)
    _log(f"ORDEN REAL {activo} {direction} ask={ask} -> ok={ok} resp={str(resp)[:120]} "
         f"t_lectura={t_lectura_ms:.0f}ms t_firma={t_firma_ms:.0f}ms t_post={t_post_ms:.0f}ms "
         f"error={error}")
    if ok:
        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": m["market_id"], "question": m["question"], "end_date": m["end_date"],
            "strategy": STRATEGY, "subtype": f"{activo}#{SUBTYPE_SUFFIX}", "direction": direction,
            "stake_eur": STAKE_EUR, "entry_price": precio_orden,
            "signal_ask": round(ask, 4), "slip_real": "",
            "ic_modelo": "", "edge_neto": "", "conviction_score": "", "kelly_recomendado": STAKE_EUR,
            "status": "OPEN", "close_timestamp": "", "exit_price": "", "outcome_real": "",
            "fee_eur": "", "pnl_bruto_eur": "", "pnl_neto_eur": "",
            "notas": f"RESOLUTION_SNIPER_PRECIERRE offset={OFFSET_S}s gate={veredicto['motivo']} "
                     f"t_total={resultado['t_total_ms']}ms",
        }
        lt._registrar_trade(trade)
    return resultado


def procesar_ventana(pre: _Precalculo, ts_end: int) -> None:
    objetivo = ts_end + OFFSET_S
    espera = objetivo - time.time()
    if espera > 0:
        time.sleep(espera)
    for activo in ASSETS:
        r = _instante_critico(pre, activo)
        if r is None:
            continue
        _append_csv({"timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                      "ts_end": ts_end, "dry_run": DRY_RUN, **r})
        if r.get("disparado"):
            break  # un solo intento por ventana, mismo criterio que el resto del proyecto


def main() -> None:
    _TAIL.arrancar()
    time.sleep(2)
    _log(f"resolution_sniper_precierre_executor arrancado -- DRY_RUN={DRY_RUN} "
         f"offset={OFFSET_S}s stake={STAKE_EUR}€ activos={ASSETS}")
    pre = _Precalculo()
    while True:
        try:
            if not DRY_RUN:
                ok_switch, motivo = live_guard.puede_operar_live()
                if not ok_switch:
                    time.sleep(5)
                    continue
                disparado_cb, motivo_cb = live_stake.verificar_circuit_breaker()
                if disparado_cb:
                    _log(f"circuit breaker disparado: {motivo_cb} -- en espera")
                    time.sleep(5)
                    continue
            now = time.time()
            ts_end = (int(now) // DUR_S + 1) * DUR_S
            objetivo_precalculo = ts_end + OFFSET_S - PRECALCULO_ANTES_S
            # /code-review 04-Sep, hallazgo real: un solo sleep(min(margen,30))
            # dormía como mucho 30s y luego arrancaba pre.preparar() de
            # inmediato aunque quedaran minutos de margen -- el precálculo
            # se ejecutaba varios minutos antes de T-12s, no justo antes
            # como dice el diseño. Bucle hasta estar realmente cerca.
            while True:
                margen = objetivo_precalculo - time.time()
                if margen <= 0:
                    break
                time.sleep(min(margen, 30))
            pre.preparar(ts_end)
            procesar_ventana(pre, ts_end)
            resto = ts_end + max(OFFSET_S, 0) + 3 - time.time()
            if resto > 0:
                time.sleep(min(resto, 30))
        except Exception as e:
            # /code-review 04-Sep, hallazgo real: sin este guardián, una
            # excepción de red/parseo en cualquier punto del ciclo (lectura
            # de libro, import de py_clob_client_v2, escritura del CSV)
            # tumbaba el proceso entero -- mismo criterio que el resto de
            # ejecutores persistentes del proyecto (ballenas_executor_5min.py
            # etc.), que sobreviven un ciclo malo y reintentan el siguiente.
            _log(f"error en ciclo principal ({type(e).__name__}: {e}) -- se reintenta en el siguiente ciclo")
            time.sleep(5)


if __name__ == "__main__":
    main()
