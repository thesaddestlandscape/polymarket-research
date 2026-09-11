"""
nested_arb_trade.py — Motor de ejecución LIVE para nested_arb (arb de
contención entre ventanas anidadas: comprar YES_outer+NO_inner o el combo
espejo cuando el coste real de los asks < $1 — ver docstring de
nested_arb_scanner.py para el mecanismo completo).

⚠️ INACTIVO POR DISEÑO. `nested_arb_scanner.py` NO importa ni llama nada
de este fichero todavía, y `config_live.json["nested_arb"]["live_enabled"]`
trae `false` por defecto. Construido 2026-07-14 (petición explícita Javi)
mientras el gate estadístico (`analisis_nested_arb_gate.py`) sigue
madurando en shadow — a esa fecha: n=36 5min15m, garantía 94.4% cruda /
96.9% en trades ejecutables, POR DEBAJO del gate 97%, con 1 fallo limpio
sin diagnosticar (n=1, no cumple ni el propio umbral n>=15 del proyecto
para concluir nada sobre esa cola).

NO ACTIVAR (`live_enabled=true`) sin, en este orden:
  1. Gate cruzado con dato LIMPIO sostenido varios días (no un solo toque
     puntual de 97%) — releer `analisis_nested_arb_gate.py` antes de tocar
     el switch.
  2. `/code-review` adversarial de este fichero — código que toca dinero,
     regla del proyecto sin excepción. **2 PASADAS HECHAS 2026-07-14**:
     1ª pasada, 10 hallazgos confirmados y corregidos (pata 1 verificada
     contra el CLOB tras excepción; ledger de pata-en-curso con order_id
     de la pata 1; sizing por shares en vez de euros; resolución por slug;
     fee real capturada; resolver cierra la fila CSV; watchdog vigila el
     marker nuevo; alerta Telegram con reintento; end_utc ISO; slippage
     de fill capturado). **2ª pasada sobre el código YA corregido, 8
     hallazgos NUEVOS, corregidos también** — el más grave: el sizing por
     shares de la 1ª pasada podía dejar cada pata por debajo del mínimo
     $1 del CLOB (con asks asimétricos, muy frecuente en datos reales —
     **verificado: 0/158 oportunidades reales habrían sido viables al
     rango de stake 1.05-1.50€**, harían falta ~2.50€ para el 42% y ~5€
     para el 78% — bloqueo circular con el gate de escalada n≥15, que
     necesita trades para poder subir el stake). También corregidos:
     pata 2 sin la misma verificación anti-excepción que la pata 1; sin
     red de seguridad entre confirmar pata 1 y marcar pata 2; PnL del
     resolver ignoraba fees y usaba solo shares de una pata; resolver no
     idempotente y contaba hacia el gate incluso sin reconciliar (viola
     "dinero no cuadra → parar"); chequeo de profundidad ~2x más
     estricto de lo necesario; alertas Telegram/JSONL inconsistentes
     entre las 2 rutas de incidente; resolución por slug sin verificar
     coincidencia; 4 llamadas HTTP secuenciales paralelizadas.
     **DECIDIDO por Javi 14-Jul**: el techo de stake (1.05-1.50€) se deja
     TAL CUAL a propósito — el bankroll real hoy (~10.39€) es demasiado
     mínimo para permitirse perder 2.50-5€ en un solo trade (lo que
     costaría desbloquear la mayoría de oportunidades reales, ver hallazgo
     0/158 arriba). Subir el techo ahora sería "un suicidio si pierde un
     trade" (cita literal). Se deja cableado tal cual para que
     `nested_arb_scanner.py` siga acumulando N en shadow (gratis, no
     depende de este módulo) — cuando el bankroll se recupere, se
     revisita el techo. Hasta entonces, casi ninguna oportunidad real
     pasará el chequeo de viabilidad — es el comportamiento esperado, no
     un bug. **PENDIENTE**: 3ª pasada de code-review antes de conectar a
     live, prevista para "próximamente" (sin fecha fija) una vez el
     bankroll lo permita.
  3. n>=15 trades LIVE propios (no heredados de la simulación, ver
     `calcular_stake_nested_arb`) con garantía>=97% antes de escalar el
     stake por encima del suelo.
  4. Aprobación explícita de Javi para el switch.

## Por qué el sizing NO es Kelly clásico
A diferencia de las estrategias direccionales (GBM_LATE), aquí la cola de
pérdida es del 100% del stake (payout=0 en AMBAS patas, no "se pierde el
edge" como en un BUY_YES/BUY_NO fallido) y con solo 1 fallo observado en
32 trades simulados ejecutables, la tasa real de esa cola tiene
muchísima incertidumbre estadística. Un Kelly puntual sobre un parámetro
tan mal estimado sería apostar el tamaño de la posición a un número que
no conocemos con precisión — exactamente el tipo de "sangrado" a evitar.
En su lugar: suelo fijo mientras no hay validación LIVE propia, y solo
entonces un escalón progresivo pequeño con techo absoluto bajo — mismo
patrón "Gate #1" ya usado en el proyecto para el des-pineo de
`max_stake_eur` de GBM_LATE (n>=15 trades limpios antes de escalar).

## Riesgo nuevo específico de 2 patas (no existe en el motor de 1 pata)
Un FOK que falla en la pata 2 tras haber llenado la pata 1 deja una
posición DIRECCIONAL DESNUDA (perdió la cobertura que daba la garantía de
contención). Se trata como el incidente de máxima prioridad del sistema:
alerta Telegram inmediata + circuit breaker duro — 1 SOLO evento pausa
`nested_arb` hasta revisión manual explícita, sin auto-reanudación. Mismo
nivel de severidad que un fallo de garantía (payout=0).
"""
import csv
import json
import requests
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path

from live_trade import (
    _get_clob_client, _consultar_profundidad_libro,
    _resolver_tokens_desde_payload, MIN_ORDEN_CLOB_USD,
)
from live_stake import bankroll_actual
from shadow_digest import enviar_telegram_critico

DIR_LIVE = Path("data/live")
LOG_PATH = Path("logs/live.log")
GAMMA = "https://gamma-api.polymarket.com"

CONFIG_PATH = DIR_LIVE / "config_live.json"
NESTED_ARB_TRADES_CSV = DIR_LIVE / "nested_arb_trades.csv"
NESTED_ARB_STATE_PATH = DIR_LIVE / "nested_arb_live_state.json"
NESTED_ARB_ORDEN_EN_CURSO_PATH = DIR_LIVE / "nested_arb_orden_en_curso.json"
NESTED_ARB_INCIDENTES_PATH = DIR_LIVE / "nested_arb_incidentes.jsonl"

TRADES_COLS = [
    "ts_entrada", "activo", "nesting", "combo", "stake_leg1_eur", "stake_leg2_eur",
    "shares_leg1", "shares_leg2", "coste_real", "fee_leg1_eur", "fee_leg2_eur",
    "coste_real_con_fees",
    "ask_leg1_real", "ask_leg2_real", "fill_price_leg1", "fill_price_leg2",
    "slip_real_leg1", "slip_real_leg2", "outer_slug", "inner_slug",
    "leg1_order_id", "leg2_order_id", "end_utc", "status",
    "gano_leg1", "gano_leg2", "payout_por_share", "pnl_eur", "ts_cierre",
]

# --- Sizing: ver docstring del módulo para el razonamiento ---
NESTED_ARB_MIN_STAKE_EUR = 1.05          # suelo CLOB, igual que el resto del sistema
NESTED_ARB_N_MIN_ESCALAR = 15            # trades LIVE propios antes de escalar (umbral n>=15 del proyecto)
NESTED_ARB_GARANTIA_MIN_ESCALAR = 97.0   # % — mismo gate que analisis_nested_arb_gate.py
NESTED_ARB_PCT_BANKROLL = 0.02           # 2% del bankroll — mitad del 4-5% de estrategias direccionales YA maduras, por la cola de pérdida=100%
NESTED_ARB_MAX_STAKE_EUR = 1.50          # techo absoluto inicial, deliberadamente bajo (la sim usaba $10 — no transfiere a vivo sin validar)
NESTED_ARB_MAX_POSICIONES_SIMULTANEAS = 1  # nunca 2 arbs de contención abiertos a la vez (evita apilar riesgo de cola correlacionado)
NESTED_ARB_MAX_FALLOS_GARANTIA = 1       # 1 solo fallo (payout=0) en vivo -> pausa dura
NESTED_ARB_MAX_NAKED_LEG_EVENTS = 1      # 1 sola pata huérfana -> pausa dura
NESTED_ARB_MAX_ERRORES_RECONCILIACION = 1  # 1 solo cierre sin fila que reconciliar (dinero no cuadra) -> pausa dura
NESTED_ARB_COSTE_MAX_SEGURO = 0.97       # re-cotizado en vivo; margen de 3c sobre el <1.0 teórico para cubrir slippage entre las 2 patas
NESTED_ARB_TOLERANCIA_SHARES = 0.05      # 5% — margen antes de disparar incidente por descuadre de shares entre patas. El driver real NO es el redondeo a céntimo del CLOB (aporta poco, ~1-3% en stakes de 1.05-1.50€) sino el SLIPPAGE DE FILL entre las 2 patas — cada una es un FOK independiente contra un libro distinto, puede llenar a precio distinto del cotizado; no escala con el tamaño del stake (corregido 2ª pasada code-review, 14-Jul — el comentario anterior atribuía esto a redondeo, que la aritmética no sostenía)


def _cargar_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def _log(msg: str):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} [nested_arb] {msg}\n")


def _get_token_ids_por_slug(slug: str) -> tuple[str, str]:
    """(yes_token_id, no_token_id) resolviendo por SLUG, no por market_id
    numérico. `nested_arb_scanner.py` (el productor real de las
    oportunidades) solo conoce slugs (`inner_slug`/`outer_slug` — nunca
    resuelve ni guarda un market_id numérico), así que `_get_token_ids`
    de live_trade.py (que exige un market_id vía `/markets/{id}`) no es
    utilizable aquí directamente. Reutiliza la MISMA validación de orden
    YES/NO que `_get_token_ids` (`_resolver_tokens_desde_payload`) en vez
    de la resolución sin validar que usa `nested_arb_scanner._tokens()`
    (asume ciegamente clobTokenIds[0]=YES) — con dinero real en juego no
    basta la resolución que ya usa el scanner para detectar oportunidades."""
    resp = requests.get(f"{GAMMA}/markets", params={"slug": slug}, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    if isinstance(data, list):
        if not data:
            raise ValueError(f"slug sin mercado en Gamma: {slug}")
        data = data[0]
    # Fail-closed: Gamma podría en teoría devolver un mercado que no sea
    # exactamente el pedido (match parcial, alias). Con dinero real en
    # juego no se toma data[0] a ciegas — se verifica que el slug
    # devuelto coincide con el pedido antes de resolver tokens.
    slug_real = data.get("slug")
    if slug_real != slug:
        raise ValueError(f"Gamma devolvió slug '{slug_real}' para la petición '{slug}' — no coincide")
    return _resolver_tokens_desde_payload(data, f"slug {slug}")


def _cargar_estado() -> dict:
    if not NESTED_ARB_STATE_PATH.exists():
        return {"fallos_garantia": 0, "naked_leg_events": 0, "errores_reconciliacion": 0,
                "pausado": False, "motivo_pausa": None, "n_trades_live": 0, "garantia_ok_live": 0}
    with open(NESTED_ARB_STATE_PATH, encoding="utf-8") as f:
        return json.load(f)


def _guardar_estado(estado: dict):
    NESTED_ARB_STATE_PATH.write_text(json.dumps(estado, indent=2, ensure_ascii=False), encoding="utf-8")


def circuit_breaker_nested_arb_ok() -> tuple[bool, str]:
    """Fail-closed: cualquier duda -> no operar. Se llama SIEMPRE antes de
    intentar ejecutar, y también debería llamarse al arrancar el proceso
    (una orden en curso sin resolver de un ciclo anterior es indicio de
    pata huérfana no procesada — ver `verificar_huerfana_al_arrancar`)."""
    cfg = _cargar_config().get("nested_arb", {})
    if not cfg.get("live_enabled", False):
        return False, "nested_arb.live_enabled=false en config"
    estado = _cargar_estado()
    if estado.get("pausado"):
        return False, f"pausado: {estado.get('motivo_pausa')}"
    if estado.get("fallos_garantia", 0) >= NESTED_ARB_MAX_FALLOS_GARANTIA:
        return False, f"{estado['fallos_garantia']} fallo(s) de garantía en vivo — pausa dura"
    if estado.get("naked_leg_events", 0) >= NESTED_ARB_MAX_NAKED_LEG_EVENTS:
        return False, f"{estado['naked_leg_events']} evento(s) de pata huérfana — pausa dura"
    if estado.get("errores_reconciliacion", 0) >= NESTED_ARB_MAX_ERRORES_RECONCILIACION:
        return False, f"{estado['errores_reconciliacion']} error(es) de reconciliación — pausa dura"
    if NESTED_ARB_ORDEN_EN_CURSO_PATH.exists():
        return False, "orden en curso sin resolver (posible pata huérfana de un ciclo anterior)"
    return True, "ok"


def calcular_stake_nested_arb() -> float:
    """Progresivo: suelo fijo hasta n>=15 trades LIVE propios con garantía
    sostenida >=97%; solo entonces % de bankroll con techo bajo. NUNCA
    hereda la validación de la simulación — cada escalón se gana con dato
    LIVE propio. Ver docstring del módulo para por qué no es Kelly clásico."""
    estado = _cargar_estado()
    n = estado.get("n_trades_live", 0)
    ok = estado.get("garantia_ok_live", 0)
    garantia_pct = (ok / n * 100) if n else 0.0
    if n < NESTED_ARB_N_MIN_ESCALAR or garantia_pct < NESTED_ARB_GARANTIA_MIN_ESCALAR:
        return NESTED_ARB_MIN_STAKE_EUR
    bkr = bankroll_actual()
    pct_stake = bkr * NESTED_ARB_PCT_BANKROLL
    return round(max(NESTED_ARB_MIN_STAKE_EUR, min(pct_stake, NESTED_ARB_MAX_STAKE_EUR)), 2)


def _posiciones_nested_arb_abiertas() -> int:
    if not NESTED_ARB_TRADES_CSV.exists():
        return 0
    with open(NESTED_ARB_TRADES_CSV, encoding="utf-8") as f:
        return sum(1 for r in csv.DictReader(f) if r.get("status") == "OPEN")


def _cargar_trades() -> list:
    if not NESTED_ARB_TRADES_CSV.exists():
        return []
    with open(NESTED_ARB_TRADES_CSV, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _guardar_trades(rows: list):
    with open(NESTED_ARB_TRADES_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=TRADES_COLS)
        w.writeheader()
        w.writerows(rows)


def _marcar_leg_en_curso(leg_num: int, slug: str, token_id: str, oportunidad: dict,
                         leg1_resultado: dict | None = None):
    """Escribe el marcador de orden en vuelo (sobrescribe el anterior a
    propósito: solo debe existir UNA orden en curso a la vez). Si
    leg_num==2, `leg1_resultado` debe llevar el order_id/stake real de la
    pata 1 YA confirmada — si el proceso muere durante el envío de la
    pata 2, `verificar_huerfana_al_arrancar` necesita esos datos para
    poder reconciliar la pata 1 (que si se ejecutó, es dinero real en
    juego); sin esto el marcador solo tendría info de la pata 2 y la
    pata 1 confirmada quedaría invisible para la recuperación."""
    datos = {
        "leg": leg_num, "slug": slug, "token_id": token_id,
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "oportunidad": {k: oportunidad.get(k) for k in
                        ("activo", "nesting", "combo", "outer_slug", "inner_slug")},
    }
    if leg1_resultado is not None:
        datos["leg1_resultado"] = leg1_resultado
    NESTED_ARB_ORDEN_EN_CURSO_PATH.write_text(json.dumps(datos, ensure_ascii=False), encoding="utf-8")


def _limpiar_orden_en_curso():
    NESTED_ARB_ORDEN_EN_CURSO_PATH.unlink(missing_ok=True)


def verificar_huerfana_al_arrancar():
    """Llamar UNA VEZ al arrancar el proceso fast, antes de cualquier
    intento de ejecución nueva. Si el proceso murió con una orden de
    pata 2 en curso, no sabemos si esa pata llegó a ejecutarse en el CLOB
    o no — no se intenta adivinar ni corregir sola (podría empeorar el
    desequilibrio): pausa dura + alerta, revisión manual obligatoria."""
    if not NESTED_ARB_ORDEN_EN_CURSO_PATH.exists():
        return
    try:
        info = json.loads(NESTED_ARB_ORDEN_EN_CURSO_PATH.read_text(encoding="utf-8"))
    except Exception:
        info = {"leg": "desconocida", "raw_ilegible": True}
    _registrar_incidente_naked_leg(
        info, motivo="proceso murió con orden en curso — estado de esa pata desconocido, revisar en Polymarket directamente")
    _limpiar_orden_en_curso()


def _pausar_dura(campo_contador: str, motivo: str, mensaje_telegram: str,
                 tipo_incidente: str, extra_incidente: dict | None = None) -> bool:
    """Pausa dura + persistencia consistente para los 3 incidentes de
    máxima severidad del sistema (pata huérfana, fallo de garantía,
    cierre sin fila que reconciliar). Antes cada uno tenía su propia
    copia de esta secuencia (carga→incrementa→pausa→log→alerta→guarda) y
    una de las copias no dejaba registro en el JSONL de incidentes ni
    mandaba Telegram — con dinero real en juego, las 3 rutas deben
    comportarse EXACTAMENTE igual, no "casi igual". Devuelve si la
    alerta Telegram llegó (ver `shadow_digest.enviar_telegram_critico`,
    patrón extraído de aquí el 14-Jul para reutilizarlo en el resto del
    proyecto en vez de mantener una copia local)."""
    estado = _cargar_estado()
    estado[campo_contador] = estado.get(campo_contador, 0) + 1
    estado["pausado"] = True
    estado["motivo_pausa"] = motivo
    with open(NESTED_ARB_INCIDENTES_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "tipo": tipo_incidente, "motivo": motivo, **(extra_incidente or {}),
        }, ensure_ascii=False) + "\n")
    _log(f"🚨 {tipo_incidente.upper()} — nested_arb pausado. {motivo}")
    alerta_ok = enviar_telegram_critico(mensaje_telegram, log_fn=_log)
    estado["alerta_telegram_fallida"] = not alerta_ok
    _guardar_estado(estado)
    return alerta_ok


def _registrar_incidente_naked_leg(leg_info: dict, motivo: str):
    _pausar_dura(
        "naked_leg_events", f"PATA HUÉRFANA: {motivo}",
        "🚨🚨🚨 NESTED_ARB: pata huérfana detectada.\n"
        f"{motivo}\n"
        "Posible posición direccional SIN cobertura — revisar YA en "
        "Polymarket y en data/live/nested_arb_incidentes.jsonl.\n"
        "nested_arb PAUSADO hasta reactivación manual tras revisar.",
        tipo_incidente="naked_leg", extra_incidente={"leg_info": leg_info},
    )


def _registrar_fallo_garantia(trade: dict, motivo: str):
    _pausar_dura(
        "fallos_garantia", f"FALLO DE GARANTÍA: {motivo}",
        "🚨🚨🚨 NESTED_ARB: fallo de garantía en vivo (payout=0 en ambas patas).\n"
        f"{motivo}\n"
        "nested_arb PAUSADO hasta reactivación manual tras revisar.",
        tipo_incidente="fallo_garantia", extra_incidente={"trade": trade},
    )


def _registrar_error_reconciliacion(leg1_order_id, fila_recibida: dict, motivo: str):
    """Cierre que no se pudo emparejar con ninguna fila OPEN conocida —
    dinero no cuadra. Se trata con la misma severidad que un fallo de
    garantía (regla del proyecto: 'parar, no log y seguir') y NUNCA
    actualiza n_trades_live/garantia_ok_live (ver `resolver_nested_arb_live`)
    — contar un cierre que no se pudo verificar corrompería el gate que
    decide cuándo escalar el stake."""
    _pausar_dura(
        "errores_reconciliacion", motivo,
        "🚨🚨🚨 NESTED_ARB: no se pudo cerrar un trade — "
        f"leg1_order_id={leg1_order_id} no aparece como OPEN en "
        "nested_arb_trades.csv.\nEl dinero no cuadra, revisar manualmente.\n"
        "nested_arb PAUSADO hasta reactivación manual tras revisar.",
        tipo_incidente="cierre_sin_fila",
        extra_incidente={"leg1_order_id": leg1_order_id, "fila_recibida": fila_recibida},
    )


def _enviar_fok(client, token_id: str, stake_eur: float, precio: float):
    """FOK de una pata. Reintento con stake desplazado ±0.01€ ante
    'invalid amounts' — mismo bug de precisión decimal de
    py_clob_client_v2 ya confirmado en real y mitigado en
    `live_trade._ejecutar_orden_polymarket`, replicado aquí porque este
    motor no comparte esa función (dos tokens/mercados distintos por
    llamada, no un solo BUY_YES/BUY_NO)."""
    from py_clob_client_v2 import MarketOrderArgsV2, OrderType
    intentos = [stake_eur, round(stake_eur - 0.01, 2), round(stake_eur + 0.01, 2)]
    intentos = [a for a in intentos if a >= MIN_ORDEN_CLOB_USD]
    ultimo_error = None
    for intento, amt in enumerate(intentos):
        try:
            order_args = MarketOrderArgsV2(token_id=token_id, amount=amt, side="BUY", price=precio)
            signed = client.create_market_order(order_args)
            resp = client.post_order(signed, OrderType.FOK)
            return resp, amt
        except Exception as e:
            ultimo_error = e
            if "invalid amounts" not in str(e):
                raise
    raise RuntimeError(f"no se pudo enviar FOK tras {len(intentos)} intentos: {ultimo_error}")


def _verificar_fill_tras_excepcion(client, token_id: str, ts_antes: datetime) -> bool | None:
    """Tras una excepción en `_enviar_fok` cuya respuesta pudo perderse
    (timeout, parseo fallido, etc.) NO se puede asumir que la orden no
    llegó a ejecutarse — el CLOB puede haberla casado igualmente. Se
    consulta `get_trades` filtrando por token y por timestamp posterior
    al intento para comprobarlo contra la fuente real.

    Devuelve True si hay un trade real después de `ts_antes` en ese
    token (SÍ se ejecutó pese a la excepción), False si 2 consultas
    seguidas (con un respiro entre medias) no encuentran ninguno, None
    si la propia consulta falla. Fail-closed: el caller debe tratar True
    y None igual (como riesgo posible) — None nunca significa "seguro
    que no pasó nada", solo que no se pudo comprobar. Una sola consulta
    inmediata NO basta para confiar en un False: es precisamente el
    escenario en el que el lag de consistencia eventual de la API
    dejaría pasar una pata huérfana real sin detectar (bug encontrado en
    la 2ª pasada de code-review, 14-Jul) — de ahí el reintento con
    espera antes de dar el False por bueno."""
    try:
        from py_clob_client_v2.clob_types import TradeParams
        # after/before del endpoint /data/trades son unix timestamp en
        # SEGUNDOS (verificado 2026-07-14 contra la documentación pública
        # de Polymarket — el propio cliente py_clob_client_v2 no lo
        # documenta ni lo convierte, ver get_trades() en la librería).
        # only_first_page=True: sin esto get_trades pagina TODO el
        # historial hasta agotar el cursor — aquí solo hace falta saber
        # si existe al menos 1 resultado, no enumerarlos todos.
        after_s = int(ts_antes.timestamp())
        params = TradeParams(asset_id=token_id, after=after_s)
        for intento in range(2):
            trades = client.get_trades(params, only_first_page=True)
            if trades:
                return True
            if intento == 0:
                time.sleep(1.5)
        return False
    except Exception:
        return None


def _end_utc_iso(oportunidad: dict) -> str:
    """ISO datetime del cierre de la ventana OUTER, mismo formato que usa
    `nested_arb_scanner.py` en su simulador (`datetime.isoformat`,
    parseable con `datetime.fromisoformat`). `nested_arb_scanner.evaluar_par`
    nunca produce una clave "end_utc" — solo "restante_s" (segundos
    restantes EN EL MOMENTO DEL ESCANEO, un int, no un timestamp
    absoluto) junto con "timestamp_utc" (el instante exacto del escaneo,
    ISO). Guardar el int crudo de restante_s en una columna llamada
    "end_utc" rompería a cualquier resolver que la parseara como
    datetime. Se calcula end_utc = timestamp_utc + restante_s cuando
    ambos están disponibles — usar `datetime.now()` en su lugar (como
    hacía la versión anterior) sería sumar el retraso de TODO el pipeline
    de ejecución (resolución de tokens + 2 consultas de libro + posibles
    reintentos FOK) al resultado, adelantando end_utc respecto al cierre
    real de la ventana. Si llega un "end_utc" ya en formato ISO (p.ej. de
    un caller futuro que sí lo resuelva así) se usa tal cual."""
    end_utc = oportunidad.get("end_utc")
    if end_utc:
        return end_utc
    restante_s = oportunidad.get("restante_s")
    if restante_s is None:
        return ""
    ts_escaneo = oportunidad.get("timestamp_utc")
    try:
        base = datetime.fromisoformat(ts_escaneo) if ts_escaneo else datetime.now(timezone.utc)
    except ValueError:
        base = datetime.now(timezone.utc)
    return (base + timedelta(seconds=int(restante_s))).isoformat(timespec="seconds")


def _fee_de_respuesta(resp: dict, stake_eur: float) -> float:
    """Comisión real en euros a partir de la respuesta del CLOB — mismo
    cálculo que `live_trade._ejecutar_orden_polymarket` (`feeRateBps` en
    puntos básicos sobre el stake realmente ejecutado)."""
    return float(resp.get("feeRateBps", 0)) / 10000 * stake_eur


def _registrar_trade(oportunidad: dict, stake1: float, stake2: float, shares1: float,
                     shares2: float, coste_real: float, fee1: float, fee2: float,
                     coste_real_con_fees: float,
                     ask1: float, ask2: float, fill1: float | None, fill2: float | None,
                     order_id1: str, order_id2: str):
    slip1 = round(fill1 - ask1, 4) if fill1 is not None else ""
    slip2 = round(fill2 - ask2, 4) if fill2 is not None else ""
    existe = NESTED_ARB_TRADES_CSV.exists()
    with open(NESTED_ARB_TRADES_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=TRADES_COLS)
        if not existe:
            w.writeheader()
        w.writerow({
            "ts_entrada": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "activo": oportunidad.get("activo"), "nesting": oportunidad.get("nesting"),
            "combo": oportunidad.get("combo"),
            "stake_leg1_eur": stake1, "stake_leg2_eur": stake2,
            "shares_leg1": round(shares1, 4), "shares_leg2": round(shares2, 4),
            "coste_real": coste_real, "fee_leg1_eur": fee1, "fee_leg2_eur": fee2,
            "coste_real_con_fees": round(coste_real_con_fees, 4),
            "ask_leg1_real": ask1, "ask_leg2_real": ask2,
            "fill_price_leg1": fill1 if fill1 is not None else "",
            "fill_price_leg2": fill2 if fill2 is not None else "",
            "slip_real_leg1": slip1, "slip_real_leg2": slip2,
            "outer_slug": oportunidad.get("outer_slug"), "inner_slug": oportunidad.get("inner_slug"),
            "leg1_order_id": order_id1, "leg2_order_id": order_id2,
            "end_utc": _end_utc_iso(oportunidad),
            "status": "OPEN",
        })


def ejecutar_nested_arb_si_procede(oportunidad: dict) -> dict:
    """oportunidad: dict con claves activo/nesting/combo/outer_slug/
    inner_slug/ask_leg1/ask_leg2/end_utc, tal como las produce
    nested_arb_scanner.py para una fila con pasa_filtro=1 recién medida
    (el scanner solo conoce slugs, nunca un market_id numérico — ver
    `_get_token_ids_por_slug`). Re-cotiza AMBAS patas contra el libro
    real antes de firmar nada — nunca confía en los asks del scanner
    (pueden tener segundos de antigüedad). Fail-closed ante cualquier
    ambigüedad, incluida la pata 1 sola sin poder confirmar la pata 2."""
    ok, motivo = circuit_breaker_nested_arb_ok()
    if not ok:
        return {"ok": False, "motivo": motivo}

    if _posiciones_nested_arb_abiertas() >= NESTED_ARB_MAX_POSICIONES_SIMULTANEAS:
        return {"ok": False, "motivo": "techo de posiciones simultáneas"}

    # Resolución de tokens en PARALELO — 2 llamadas HTTP independientes
    # (outer/inner son mercados distintos, sin dependencia de datos entre
    # sí) que antes se hacían en serie, comiéndose hasta ~20s del margen
    # de segundos que hay antes de que cierre la ventana (2ª pasada de
    # code-review, 14-Jul).
    with ThreadPoolExecutor(max_workers=2) as ex:
        fut_out = ex.submit(_get_token_ids_por_slug, oportunidad["outer_slug"])
        fut_in = ex.submit(_get_token_ids_por_slug, oportunidad["inner_slug"])
        try:
            yes_out, no_out = fut_out.result()
            yes_in, no_in = fut_in.result()
        except Exception as e:
            return {"ok": False, "motivo": f"error resolviendo tokens: {e}"}

    combo = oportunidad["combo"]  # "YESout+NOin" o "NOout+YESin"
    leg1_token = yes_out if combo.startswith("YES") else no_out
    leg2_token = no_in if combo.endswith("NOin") else yes_in

    stake = calcular_stake_nested_arb()

    # Estimación del importe POR PATA (no el stake combinado) para el
    # chequeo de profundidad, usando los asks del scanner como aproximación
    # previa al re-quote real. Antes se pasaba el stake COMBINADO como
    # importe de CADA pata individualmente — hacía el veto de profundidad
    # hasta 2x más estricto de lo necesario, rechazando oportunidades
    # viables (2ª pasada de code-review). También en PARALELO, mismo
    # motivo que la resolución de tokens.
    ask1_scanner = float(oportunidad["ask_leg1"])
    ask2_scanner = float(oportunidad["ask_leg2"])
    coste_scanner = ask1_scanner + ask2_scanner
    monto_leg1_estimado = (stake * ask1_scanner / coste_scanner) if coste_scanner else stake
    monto_leg2_estimado = (stake * ask2_scanner / coste_scanner) if coste_scanner else stake
    with ThreadPoolExecutor(max_workers=2) as ex:
        fut1 = ex.submit(_consultar_profundidad_libro, None, leg1_token, ask1_scanner, monto_leg1_estimado)
        fut2 = ex.submit(_consultar_profundidad_libro, None, leg2_token, ask2_scanner, monto_leg2_estimado)
        depth1 = fut1.result()
        depth2 = fut2.result()
    min_ratio = _cargar_config().get("riesgo", {}).get("min_profundidad_ratio_libro", 5.0)
    if not (depth1.get("ok") and depth2.get("ok")):
        return {"ok": False, "motivo": "libro sin datos en alguna pata (fail-closed)"}
    if (depth1.get("ratio_vs_stake") or 0) < min_ratio or (depth2.get("ratio_vs_stake") or 0) < min_ratio:
        return {"ok": False, "motivo": "profundidad insuficiente en alguna pata"}

    ask1_real = float(depth1["mejor_ask"])
    ask2_real = float(depth2["mejor_ask"])
    coste_real = ask1_real + ask2_real
    if coste_real >= NESTED_ARB_COSTE_MAX_SEGURO:
        return {"ok": False, "motivo": f"coste real {coste_real:.4f} >= margen de seguridad {NESTED_ARB_COSTE_MAX_SEGURO}"}

    # El CLOB exige >=$1 en CADA pata individualmente (MIN_ORDEN_CLOB_USD),
    # no en el conjunto. Con asks muy asimétricos (frecuente en datos
    # reales: p.ej. ask1=0.001/ask2=0.01) la pata barata puede necesitar
    # un stake total muy superior al que calcular_stake_nested_arb()
    # asignaría en esta fase. Sin este chequeo, _enviar_fok filtraría los
    # 3 intentos de esa pata, lanzaría RuntimeError, y el código lo
    # trataría como fallo ambiguo -> pausa dura por "pata huérfana" SIN
    # que se hubiera enviado ninguna orden real — bug CRÍTICO encontrado
    # en la 2ª pasada de code-review (14-Jul): a este nivel de stake casi
    # ninguna oportunidad real habría sido operable. Skip limpio, no es
    # un incidente — simplemente esta combinación de asks no es operable
    # todavía al nivel de stake vigente.
    ask_barata = min(ask1_real, ask2_real)
    stake_minimo_viable = MIN_ORDEN_CLOB_USD * coste_real / ask_barata
    if stake < stake_minimo_viable:
        return {"ok": False, "motivo": f"oportunidad no viable al stake actual ({stake:.2f}€): "
                f"la pata más barata (ask={ask_barata:.4f}) necesitaría "
                f"{stake_minimo_viable:.2f}€ de stake total para llegar al mínimo "
                f"CLOB ${MIN_ORDEN_CLOB_USD:.2f}/pata"}

    # Sizing por SHARES, no por euros: la garantía de contención exige el
    # mismo nº de shares en ambas patas (igual que nested_arb_scanner.py
    # simula con un único n_shares para las 2 patas) — un mismo importe en
    # euros compraría cantidades de shares distintas porque ask1_real y
    # ask2_real casi nunca coinciden. n_shares objetivo = presupuesto total
    # (stake) / coste combinado; el importe en euros de cada pata se
    # deriva de ahí, no al revés.
    n_shares_objetivo = stake / coste_real
    monto_leg1 = round(n_shares_objetivo * ask1_real, 2)

    client = _get_clob_client()

    ts_intento_leg1 = datetime.now(timezone.utc)
    _marcar_leg_en_curso(1, oportunidad["outer_slug"], leg1_token, oportunidad)
    try:
        resp1, stake_real1 = _enviar_fok(client, leg1_token, monto_leg1, ask1_real)
    except Exception as e:
        fill_detectado = _verificar_fill_tras_excepcion(client, leg1_token, ts_intento_leg1)
        if fill_detectado is False:
            _limpiar_orden_en_curso()
            return {"ok": False, "motivo": f"pata 1 no ejecutada (verificado contra el CLOB), sin riesgo abierto: {e}"}
        # True o None (duda): nunca se puede demostrar que NO pasó nada —
        # se trata como posible pata huérfana, mismo nivel que el fallo
        # de la pata 2 más abajo.
        _registrar_incidente_naked_leg(
            {"leg": 1, "slug": oportunidad["outer_slug"], "token_id": leg1_token,
             "monto_objetivo": monto_leg1, "excepcion": str(e), "fill_detectado_en_clob": fill_detectado},
            motivo=f"pata 1 lanzó excepción y no se pudo descartar fill real "
                   f"(fill_detectado_en_clob={fill_detectado}): {e}")
        _limpiar_orden_en_curso()
        return {"ok": False, "motivo": f"PATA 1 AMBIGUA (posible fill sin confirmar): {e}", "naked_leg": True}

    order_id1 = resp1.get("orderID") or resp1.get("id") or str(resp1)
    fill1 = float(resp1["price"]) if resp1.get("price") is not None else None
    precio_efectivo_leg1 = fill1 if fill1 is not None else ask1_real

    # Todo lo que sigue ocurre DESPUÉS de que la pata 1 ya ejecutó con
    # dinero real — cualquier excepción aquí (p.ej. división por cero si
    # el libro devolviera un ask degenerado) no puede tratarse como "no
    # pasó nada": es la misma pata huérfana que si hubiera fallado el
    # envío. Antes esta sección no tenía red de seguridad propia y una
    # excepción se escapaba sin pasar por el circuito de incidente (bug
    # encontrado en la 2ª pasada de code-review).
    try:
        shares_leg1 = stake_real1 / precio_efectivo_leg1
        monto_leg2 = round(shares_leg1 * ask2_real, 2)
        _marcar_leg_en_curso(2, oportunidad["inner_slug"], leg2_token, oportunidad,
                            leg1_resultado={"slug": oportunidad["outer_slug"], "token_id": leg1_token,
                                            "order_id": order_id1, "stake_real": stake_real1,
                                            "shares": shares_leg1})
    except Exception as e:
        _registrar_incidente_naked_leg(
            {"leg": 1, "slug": oportunidad["outer_slug"], "token_id": leg1_token,
             "stake": stake_real1, "order_id": order_id1},
            motivo=f"error preparando la pata 2 tras confirmar la pata 1 (order_id={order_id1}): {e}")
        _limpiar_orden_en_curso()
        return {"ok": False, "motivo": f"PATA HUÉRFANA (error interno post-pata1): {e}", "naked_leg": True}

    ts_intento_leg2 = datetime.now(timezone.utc)
    try:
        resp2, stake_real2 = _enviar_fok(client, leg2_token, monto_leg2, ask2_real)
    except Exception as e:
        # Misma verificación que la pata 1: una excepción no demuestra
        # que la orden no llegó a ejecutarse en el CLOB (2ª pasada de
        # code-review — antes la pata 2 se declaraba huérfana sin
        # comprobar, asimétrico con el cuidado que sí se le daba a la
        # pata 1). En cualquier caso la pata 1 queda sin cobertura
        # confirmada, así que el incidente se registra igual — el
        # resultado de la verificación solo cambia el detalle del motivo.
        fill_detectado = _verificar_fill_tras_excepcion(client, leg2_token, ts_intento_leg2)
        _registrar_incidente_naked_leg(
            {"leg": 1, "slug": oportunidad["outer_slug"], "token_id": leg1_token,
             "stake": stake_real1, "order_id": order_id1,
             "pata2_fill_detectado_en_clob": fill_detectado},
            motivo=f"pata 2 falló tras confirmar pata 1 (order_id={order_id1}), "
                   f"fill_detectado_en_clob={fill_detectado}: {e}")
        _limpiar_orden_en_curso()
        return {"ok": False, "motivo": f"PATA HUÉRFANA: {e}", "naked_leg": True}

    order_id2 = resp2.get("orderID") or resp2.get("id") or str(resp2)
    fill2 = float(resp2["price"]) if resp2.get("price") is not None else None
    precio_efectivo_leg2 = fill2 if fill2 is not None else ask2_real

    # Desvío de shares con el precio de FILL real cuando está disponible,
    # no el ask cotizado — antes comparaba dos estimaciones (el ask
    # usado para disparar la orden), no la realidad de lo ejecutado, así
    # que el chequeo podía dar por bueno un descuadre real o disparar
    # sobre uno que no existía (2ª pasada de code-review). El driver real
    # de este desvío es el slippage de fill entre las 2 patas (cada una
    # es un FOK independiente contra un libro distinto), no el redondeo a
    # céntimo del CLOB — no escala con el tamaño del stake.
    shares_leg2 = stake_real2 / precio_efectivo_leg2
    desvio_shares = abs(shares_leg1 - shares_leg2) / shares_leg1 if shares_leg1 else 1.0
    if desvio_shares > NESTED_ARB_TOLERANCIA_SHARES:
        _registrar_incidente_naked_leg(
            {"leg": "ambas, descuadradas", "leg1_order_id": order_id1, "leg2_order_id": order_id2,
             "shares_leg1": shares_leg1, "shares_leg2": shares_leg2, "desvio_pct": round(desvio_shares * 100, 2)},
            motivo=f"ambas patas ejecutadas pero DESCUADRADAS: shares_leg1={shares_leg1:.4f} "
                   f"vs shares_leg2={shares_leg2:.4f} (desvío {desvio_shares*100:.1f}% > "
                   f"tolerancia {NESTED_ARB_TOLERANCIA_SHARES*100:.0f}%) — la garantía de contención "
                   f"no cubre el excedente sin cobertura")
        _limpiar_orden_en_curso()
        return {"ok": False, "motivo": f"DESCUADRE DE PATAS: {desvio_shares*100:.1f}% > tolerancia", "naked_leg": True}

    _limpiar_orden_en_curso()

    # Coste real INCLUYENDO comisión — coste_real (pre-trade) solo mira los
    # asks re-cotizados, nunca la fee del CLOB. Histórico real de trades.csv
    # (14-Jul): fee media ≈4.0% del stake, mediana ≈3.85%, máxima observada
    # ≈6.7% — con NESTED_ARB_COSTE_MAX_SEGURO=0.97 (solo 3% de margen
    # nominal) un trade que pasa el filtro pre-trade puede terminar siendo
    # pérdida neta una vez se conoce la fee real. No se puede gatear en el
    # momento de disparar (la fee solo se conoce en la respuesta del fill),
    # así que aquí solo se mide y se avisa — la garantía de contención en sí
    # sigue intacta (ambas patas cubren la posición), es la RENTABILIDAD la
    # que puede quedar por debajo de lo esperado.
    fee1 = _fee_de_respuesta(resp1, stake_real1)
    fee2 = _fee_de_respuesta(resp2, stake_real2)
    n_shares_efectivo = (shares_leg1 + shares_leg2) / 2
    coste_real_con_fees = coste_real + ((fee1 + fee2) / n_shares_efectivo if n_shares_efectivo else 0.0)
    if coste_real_con_fees >= 1.0:
        _log(f"⚠️ nested_arb {oportunidad.get('activo')} {combo}: coste_real_con_fees="
             f"{coste_real_con_fees:.4f} >= 1.0 — la garantía de contención sigue intacta "
             f"(ambas patas cubren la posición) pero el trade es NETO PERDEDOR una vez "
             f"aplicada la comisión real (fee1={fee1:.4f}€ fee2={fee2:.4f}€). Revisar si "
             f"NESTED_ARB_COSTE_MAX_SEGURO necesita más margen antes de escalar el stake.")

    _registrar_trade(oportunidad, stake_real1, stake_real2, shares_leg1, shares_leg2,
                     coste_real, fee1, fee2, coste_real_con_fees,
                     ask1_real, ask2_real, fill1, fill2, order_id1, order_id2)
    _log(f"✅ nested_arb ejecutado {oportunidad.get('activo')} {combo} "
         f"stake_leg1={stake_real1:.2f}€ stake_leg2={stake_real2:.2f}€ "
         f"shares≈{shares_leg1:.4f}/{shares_leg2:.4f} coste_real={coste_real:.4f} "
         f"coste_real_con_fees={coste_real_con_fees:.4f}")
    return {"ok": True, "stake_leg1": stake_real1, "stake_leg2": stake_real2,
            "coste_real": coste_real, "coste_real_con_fees": coste_real_con_fees}


def resolver_nested_arb_live(gano_leg1: bool, gano_leg2: bool, fila: dict):
    """Cierra un trade LIVE contra el outcome oficial (llamar desde
    shadow_resolve.py una vez el mercado resuelva, mismo patrón que
    nested_arb_scanner._sim_resolver pero sobre nested_arb_trades.csv).
    `fila` solo necesita traer `leg1_order_id` (clave única del trade,
    generada en `ejecutar_nested_arb_si_procede`) — el resto del contexto
    (activo, combo, shares, coste con fees) se lee de la fila YA
    registrada en el CSV, nunca del `fila` de entrada (que un caller
    real podría no rellenar más allá del order_id).

    Reescribe `status` a CLOSED — sin esto, `_posiciones_nested_arb_abiertas()`
    seguiría contando el trade como OPEN para siempre y, con el techo de
    1 posición simultánea, el primer trade bloquearía la estrategia de
    forma permanente y silenciosa.

    Idempotente: una segunda llamada para un `leg1_order_id` ya CLOSED no
    hace nada (ni CSV ni contadores) — sin esto, un reintento del caller
    duplicaría el conteo hacia el gate de escalada de stake.

    Fail-closed ante dinero que no cuadra: si no se encuentra ninguna
    fila OPEN con ese `leg1_order_id`, NO se actualiza n_trades_live ni
    garantia_ok_live (contar un cierre no verificado corrompería el gate
    que decide escalar el stake) y se pausa con la misma severidad que
    un fallo de garantía — 'parar, no log y seguir'."""
    leg1_order_id = fila.get("leg1_order_id")
    trades = _cargar_trades()
    fila_abierta = None
    ya_cerrada = False
    for t in trades:
        if t.get("leg1_order_id") == leg1_order_id:
            if t.get("status") == "OPEN":
                fila_abierta = t
            elif t.get("status") == "CLOSED":
                ya_cerrada = True
            break

    if ya_cerrada:
        _log(f"resolver_nested_arb_live: leg1_order_id={leg1_order_id} ya estaba "
             f"CLOSED — llamada repetida ignorada (idempotencia)")
        return

    if fila_abierta is None:
        _registrar_error_reconciliacion(
            leg1_order_id, fila,
            motivo=f"CIERRE SIN FILA: leg1_order_id={leg1_order_id} no aparece "
                   f"como OPEN en {NESTED_ARB_TRADES_CSV}")
        return

    payout_ok = gano_leg1 or gano_leg2
    payout_por_share = int(gano_leg1) + int(gano_leg2)
    shares1 = float(fila_abierta.get("shares_leg1") or 0)
    shares2 = float(fila_abierta.get("shares_leg2") or 0)
    # coste_real_con_fees ya lleva las comisiones reales incorporadas por
    # share (ver ejecutar_nested_arb_si_procede) — usarlo aquí en vez de
    # coste_real evita reportar como ganador un trade que en realidad
    # perdió dinero neto una vez pagada la comisión. shares_medio en vez
    # de solo shares_leg1: si hubo un desvío tolerado (<5%) entre patas,
    # el payout real de cada pata es proporcional a SU PROPIO nº de
    # shares, no al de la otra — la media es la aproximación correcta
    # sin llevar contabilidad separada por pata.
    coste_str = fila_abierta.get("coste_real_con_fees") or fila_abierta.get("coste_real") or 0
    coste_real_con_fees = float(coste_str)
    shares_medio = (shares1 + shares2) / 2 if (shares1 or shares2) else 0.0
    pnl_eur = round(shares_medio * (payout_por_share - coste_real_con_fees), 4)

    fila_abierta["gano_leg1"] = int(gano_leg1)
    fila_abierta["gano_leg2"] = int(gano_leg2)
    fila_abierta["payout_por_share"] = payout_por_share
    fila_abierta["pnl_eur"] = pnl_eur
    fila_abierta["ts_cierre"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    fila_abierta["status"] = "CLOSED"
    _guardar_trades(trades)

    estado = _cargar_estado()
    estado["n_trades_live"] = estado.get("n_trades_live", 0) + 1
    if payout_ok:
        estado["garantia_ok_live"] = estado.get("garantia_ok_live", 0) + 1
    _guardar_estado(estado)

    if not payout_ok:
        _registrar_fallo_garantia(
            fila_abierta,
            motivo=f"{fila_abierta.get('activo')} {fila_abierta.get('combo')} — "
                   f"payout=0 en ambas patas, stake perdido")
