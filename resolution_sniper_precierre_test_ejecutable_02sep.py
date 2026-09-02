#!/usr/bin/env python3
"""
resolution_sniper_precierre_test_ejecutable_02sep.py — PRUEBA CONTROLADA,
UN SOLO INTENTO, dinero real mínimo (stake CLOB 1.05€).

Propuesta #1 del barrido "minar pasta de verdad" (02-Sep, diseño discutido
y aprobado explícitamente por Javi antes de escribir código -- ver
idea_resolution_sniper_precierre_confirmado_02sep en memoria nativa).
Resuelve el bloqueante nº1 de RESOLUTION_SNIPER_PRECIERRE (B3): si
Polymarket acepta órdenes reales a offset -2s ANTES del cierre nominal.
Nunca se ha probado con dinero real -- el trade más ajustado al cierre en
todo el histórico del proyecto es a -9s. RESOLUTION_SNIPER_NAIVE (offset
0-3s DESPUÉS del cierre) falló 59/59 con "trading is disabled" -- este
test prueba el lado simétrico ANTES del cierre, donde el libro sigue
confirmadamente abierto en modo lectura.

02-Sep, CORRECCIÓN v2 (misma sesión, petición explícita de Javi tras
revisar el diseño): la v1 hardcodeaba BTC#[0.47,0.52) como constantes
fijas en el código -- exactamente el antipatrón que el proyecto ya
prohibió (F5, project_lecciones_aprendidas_estrategias: "NUNCA crear
tabla de zonas hardcodeada, generalizar el mecanismo ya existente"). El
gate de micro-bucket (grid+fino) se regenera y puede cambiar de un día
para otro -- una zona buena hoy puede revertir mañana, y una zona nueva
(BNB/DOGE/SOL/XRP, hoy con n<40) puede confirmar en cualquier momento.
v2: la "tupla" está ABIERTA a los 6 activos de 5min; antes de cada
intento se reconsulta EN VIVO `resolution_sniper_precierre_gate.py::
evaluar(activo, ask)` (relee el JSON con caché por mtime, exige
convergencia grid+fino, fail-closed si el dato está viejo o ausente) --
nunca se decide con una constante congelada en el momento de escribir
el script. También corregido: `_TAIL.arrancar()` nunca se llamaba en la
v1 (bug real, 2 ventanas evaluadas "sin precio Chainlink" antes de que
Javi pidiera revisar el diseño -- ningún dinero se movió, el tail vacío
hacía que la condición nunca se cumpliera).

Mecanismo:
  - Reusa la detección YA construida (resolution_sniper_observer.py:
    mercado_slot/token_ids/libro/tail Chainlink) -- nada nuevo en la
    parte de detección de mercado/dirección.
  - En cada ventana de 5min, evalúa los 6 activos. Para cada uno,
    calcula direccion_implicita (Chainlink) y ask del lado implícito, y
    consulta `resolution_sniper_precierre_gate.evaluar(activo, ask)` --
    solo dispara si CONVERGEN grid Y fino AHORA MISMO, sea cual sea el
    activo/bucket que confirme ese día.
  - offset=-2s (7s más tarde que cualquier trade real hecho hasta hoy en
    todo el proyecto, pero 1s más conservador que el límite teórico -1s
    que sí mide el observador FASE0).
  - Verifica profundidad real (lt._consultar_profundidad_libro,
    ratio_vs_stake>=5x) antes de intentar -- mismo criterio de todo el
    sistema.
  - UNA orden real, stake=1.05€ (mínimo CLOB), vía
    lt._ejecutar_orden_polymarket -- hereda automáticamente sus guardas
    (fee real, veto ballenas, dedup entre procesos, requote).
  - edge_dir sintético (EDGE_SINTETICO=0.05, NO es un edge modelado real)
    se pasa únicamente para activar la protección de _decidir_requote().
  - SINGLE-SHOT DE VERDAD: en cuanto se intenta una orden (éxito o
    fallo) el script termina. Si no aparece la condición en MAX_VENTANAS
    ciclos de 5min (~30min), también termina sin haber intentado nada.
    No se registra en ninguna screen/cron -- se lanza a mano, supervisado.
  - Aviso por Telegram con el resultado exacto.

Resultado registrado en data/live/trades.csv (strategy=
"RESOLUTION_SNIPER_PRECIERRE_TEST") y en
data/shadow/resolution_sniper_precierre_test_resultado.json.

NO se añade a pares_permitidos_live, NO se conecta a shadow_predict.py,
NO se registra en observadores_fase0.py/vigias_frecuentes_fase0.py -- es
un experimento de un solo uso para resolver una incógnita concreta.
"""
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
import resolution_sniper_precierre_gate as gate
from resolution_sniper_observer import ASSETS, mercado_slot, token_ids, libro, _TAIL

REPO = Path(__file__).resolve().parent
DUR_S = 300
MARCO_TAG = "5m"
OFFSET_S = -2
STAKE_EUR = 1.05
MIN_RATIO = 5.0
MAX_VENTANAS = 6  # ~30 min a 5min/ventana

OUT_RESULTADO = REPO / "data" / "shadow" / "resolution_sniper_precierre_test_resultado.json"


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _guardar_resultado(resultado: dict) -> None:
    OUT_RESULTADO.write_text(json.dumps(resultado, indent=1, ensure_ascii=False, default=str),
                              encoding="utf-8")


def _evaluar_activo(asset: str, ts_end: int) -> dict | None:
    """None si este activo no dio condición esta ventana. dict con
    'intentado' si se llegó a evaluar/enviar una orden real."""
    ts_start = ts_end - DUR_S
    slug, mkt = mercado_slot(asset, MARCO_TAG, ts_start)
    if not mkt:
        return None
    market_id = mkt.get("id", "")
    token_yes, token_no = token_ids(mkt)
    if not token_yes or not token_no:
        return None
    ref_open = _TAIL.precio_en(asset, ts_start) or _TAIL.precio_en(asset, ts_start + 2)

    precio = _TAIL.precio_ultimo(asset)
    if precio is None or ref_open is None or ref_open <= 0:
        _log(f"[{asset}] ts_end={ts_end}: sin precio Chainlink (precio={precio}, ref_open={ref_open})")
        return None
    if precio > ref_open:
        dir_impl = "Up"
    elif precio < ref_open:
        dir_impl = "Down"
    else:
        return None

    ask_yes, ask_no, _, _ = libro(token_yes, token_no)
    ask_impl = ask_yes if dir_impl == "Up" else ask_no
    if ask_impl is None:
        return None

    veredicto_gate = gate.evaluar(asset, ask_impl)
    if not veredicto_gate["confirmado"]:
        _log(f"[{asset}] ts_end={ts_end}: dir={dir_impl} ask={ask_impl} "
             f"gate NO confirma ({veredicto_gate['motivo']}) -- se pasa")
        return None

    _log(f"[{asset}] ts_end={ts_end}: GATE CONFIRMA (convergencia grid+fino) "
         f"dir={dir_impl} ask={ask_impl} -- comprobando profundidad real")

    token_impl = token_yes if dir_impl == "Up" else token_no
    depth = lt._consultar_profundidad_libro(None, token_impl, ask_impl, STAKE_EUR)
    ratio = depth.get("ratio_vs_stake")
    if ratio is None or ratio < MIN_RATIO:
        _log(f"[{asset}] ts_end={ts_end}: profundidad insuficiente (ratio={ratio}) -- no se intenta orden real")
        return {"intentado": False, "motivo": f"profundidad insuficiente ratio={ratio}",
                "ts_end": ts_end, "activo": asset, "direccion_implicita": dir_impl, "ask_implicita": ask_impl}

    direction = "BUY_YES" if dir_impl == "Up" else "BUY_NO"
    py_perspectiva_yes = ask_impl if dir_impl == "Up" else round(1.0 - ask_impl, 6)
    edge_dir_sintetico = 0.05 if direction == "BUY_YES" else -0.05

    _log(f"[{asset}] ts_end={ts_end}: DISPARANDO ORDEN REAL {direction} market_id={market_id} "
         f"precio(perspectiva YES)={py_perspectiva_yes} stake={STAKE_EUR}€ "
         f"gate={veredicto_gate['motivo']}")

    resultado = lt._ejecutar_orden_polymarket(
        market_id, direction, STAKE_EUR, py_perspectiva_yes,
        edge_dir=edge_dir_sintetico,
        contexto={"strategy": "RESOLUTION_SNIPER_PRECIERRE_TEST", "subtype": f"{asset}#5min",
                  "end_date": mkt.get("endDate", "")},
    )

    trade = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "market_id": market_id, "question": mkt.get("question", ""), "end_date": mkt.get("endDate", ""),
        "strategy": "RESOLUTION_SNIPER_PRECIERRE_TEST", "subtype": f"{asset}#5min", "direction": direction,
        "stake_eur": STAKE_EUR if resultado.get("ok") else 0.0,
        "entry_price": resultado.get("entry_price", py_perspectiva_yes),
        "signal_ask": round(py_perspectiva_yes, 4), "slip_real": resultado.get("slip_real", ""),
        "ic_modelo": "", "edge_neto": "", "conviction_score": "", "kelly_recomendado": STAKE_EUR,
        "status": "OPEN" if resultado.get("ok") else "ERROR",
        "close_timestamp": "", "exit_price": "", "outcome_real": "",
        "fee_eur": resultado.get("fee_eur", 0), "pnl_bruto_eur": "", "pnl_neto_eur": "",
        "notas": (f"PRUEBA CONTROLADA ejecutabilidad offset={OFFSET_S}s gate={veredicto_gate['motivo']}"
                  if resultado.get("ok")
                  else f"PRUEBA CONTROLADA offset={OFFSET_S}s -- {resultado.get('error', '')}"),
    }
    lt._registrar_trade(trade)

    return {"intentado": True, "resultado": resultado, "trade": trade,
            "ts_end": ts_end, "activo": asset, "direccion_implicita": dir_impl,
            "ask_implicita": ask_impl, "ratio": ratio, "gate": veredicto_gate}


def intentar_ventana(ts_end: int) -> dict | None:
    objetivo = ts_end + OFFSET_S
    espera = objetivo - time.time()
    if espera > 0:
        time.sleep(espera)
    for asset in ASSETS:
        salida = _evaluar_activo(asset, ts_end)
        if salida is not None:
            return salida
    return None


def main() -> None:
    _TAIL.arrancar()
    time.sleep(2)  # margen para que el tail lea al menos una vez antes del primer chequeo
    _log(f"resolution_sniper_precierre_test_ejecutable_02sep (v2, gate vivo) arrancado -- "
         f"activos={ASSETS} offset={OFFSET_S}s stake={STAKE_EUR}€ max_ventanas={MAX_VENTANAS}")
    for i in range(MAX_VENTANAS):
        now = time.time()
        ts_end = (int(now) // DUR_S + 1) * DUR_S
        salida = intentar_ventana(ts_end)
        if salida and salida.get("intentado"):
            resultado = salida["resultado"]
            ok = resultado.get("ok")
            msg = (
                f"🧪 *PRUEBA CONTROLADA RESOLUTION_SNIPER_PRECIERRE — resultado*\n"
                f"{'✅ ORDEN ACEPTADA' if ok else '❌ ORDEN RECHAZADA/NO EJECUTADA'}\n"
                f"activo={salida['activo']} gate={salida['gate']['motivo']}\n"
                f"market_id={salida['trade']['market_id']}\n"
                f"direction={salida['trade']['direction']} precio={salida['trade']['signal_ask']}\n"
                f"stake={salida['trade']['stake_eur']}€\n"
                + (f"entry_price={resultado.get('entry_price')}" if ok
                   else f"error={resultado.get('error')}")
            )
            _log(msg)
            try:
                lt.enviar_telegram(msg)
            except Exception as e:
                _log(f"aviso: no se pudo enviar Telegram ({e})")
            _guardar_resultado({
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "intentado": True, "ok": ok, "resultado": resultado, "trade": salida["trade"],
                "gate": salida["gate"],
            })
            _log("PRUEBA COMPLETADA -- script termina, no reintenta solo.")
            return
        resto = ts_end + max(OFFSET_S, 0) + 3 - time.time()
        if resto > 0:
            time.sleep(min(resto, 90))

    msg = (f"🧪 PRUEBA CONTROLADA RESOLUTION_SNIPER_PRECIERRE — sin condición "
           f"(convergencia grid+fino viva en ningún activo) en {MAX_VENTANAS} ventanas (~30min), "
           f"script termina sin intentar ninguna orden real")
    _log(msg)
    try:
        lt.enviar_telegram(msg)
    except Exception as e:
        _log(f"aviso: no se pudo enviar Telegram ({e})")
    _guardar_resultado({"timestamp_utc": datetime.now(timezone.utc).isoformat(), "intentado": False})


if __name__ == "__main__":
    main()
