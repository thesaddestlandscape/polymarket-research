"""h23_regla.py -- H23-MAKER-V1: regla CONGELADA (20-Oct-2026), fuente UNICA para el replay, el shadow persistente y el paquete real.
Pura: sin red, sin disco, sin importar nada de produccion. Cambiar CUALQUIER constante = version nueva + OOS nuevo (hash en `hash_config`).

QUE ES (informe v4_comprar_lo_bueno/informe.md §4; sim r3/sim_dia3.py, primario join mq=-0,05 clk=rx cancel=60):
  Par anidado BTC 5m/15m que cierra en C. Lado s por TWAP60 oficiales (ref15=twap60(C-900), ref5=twap60(C-300), |gap|>=1 bp:
  ref15>ref5 -> Up). Cota: bid15(s) <= P(s en el 5m). Maker: puja de compra POST-ONLY en el 5m lado s, UNIRSE al mejor bid
  (join) mientras la cota siga dejando margen; CANCELAR en cuanto la condicion se rompe (la cancelacion es el edge: sin ella el mismo
  simulador da +0,06, con ella +0,80).
"""
import hashlib
import json
import math
from pathlib import Path

CONFIG = {
    "version": 1,
    "nombre": "H23-MAKER-V1",
    # umbral de la COTA para el precio de la puja: p <= p_limite(bid15, umbral) <=> bid15 - p - fee(p) >= umbral.
    # Brazo A = umbral actual de V4 (0,05; es el que tiene la evidencia). Brazo B = variante 0,02 (informe §3: 24 ejecutables vs 12).
    "brazos": {"A": 0.05, "B": 0.02},
    # variantes: join = sim-fiel (re-unirse al instante, como r3/sim_dia3); join_r = lo que permite el arnes real H47 (tras cancelar hay que ASENTAR
    # >= 1,5 s antes de volver a pujar: se pierde el relleno si no, y se rompe «un relleno cierra la puja»); nc = control SIN cancelar.
    "repost_min_ms": {"join": 0, "join_r": 1500, "nc": 0},
    "mq": -0.05,                 # margen de MERCADO minimo (bid15 - ask5 - fee(ask5)) para estar cotizando (sim: mq=-0,05)
    "fee_tomador": 0.07,
    "rebate": 0.20,              # el maker recibe el 20 % de la comision del tomador (comision maker = 0)
    "gap_min_bps": 1.0,
    "ref_conocible_ms": 1500,    # solo se cotiza con t >= (C-300)s + 1,5 s (la referencia 5m existe desde ahi)
    "fin_margen_s": 10,          # no se cotiza con t >= C-10 s
    "stake_eur": 2.0,
    "min_acciones": 5.0,
    # latencias (F2/H47-A): acuse real mediano 79 ms; visible en el WS 254 ms (p90 573); cancelacion 60 ms ida y vuelta.
    "lat_post_ms": 79,           # central: la orden puede casar desde decision + 79 ms
    "lat_post_cons_ms": 254,     # conservadora: desde que es visible en el WS
    "lat_cancel_ms": 60,
    "lat_cancel_cons_ms": 150,
    # fraccion de la profundidad del nivel que esta DELANTE de nosotros al unirnos (calibracion_colas.md: base central, rango [opt, cons])
    "colas": {"opt": 0.0, "base": 0.5, "cons": 1.0},
    # topes del shadow (el real los hereda de H47: 5 $ de presupuesto util, suelo dinamico, N fijo)
    "max_cotiz_por_mercado": 20,  # cancelaciones+reposiciones en un mercado (carga de API; sim sin tope: se registra cuantas habria)
    "gate": {"n_rellenos": 40, "dias": 10, "ev_pond_min": 0.10, "ic90_dias_min": 0.0, "sin2mejores_min": 0.0},
    "kill_brazo": {"n_rellenos": 20, "ev_pond_sin2mejores_max": -0.15},   # REJECTED del brazo (ver h23_analisis.py: falso disparo simulado)
}


def fee(p, cfg=CONFIG):
    return cfg["fee_tomador"] * p * (1.0 - p)


def p_limite(bid15, umbral):
    """Mayor precio de rejilla 0,01 con bid15 - p - fee(p) >= umbral (identico al simulador r3: floor con +1e-9)."""
    if bid15 is None or isinstance(bid15, float) and math.isnan(bid15):
        return None
    p = math.floor(bid15 * 100 + 1e-9) / 100
    while p > 0 and round(bid15 - p - fee(p), 4) < umbral - 1e-12:   # redondeo a 4 decimales como V4 (margen())
        p = round(p - 0.01, 2)
    return p if p > 0 else None


def margen(bid15, ask5):
    return round(bid15 - ask5 - fee(ask5), 4)


def lado_de_refs(ref15, ref5, gap_min_bps=None):
    """'Up' | 'Down' | None (gap < minimo). ref15 > ref5 -> Up (como V4/F2)."""
    g = CONFIG["gap_min_bps"] if gap_min_bps is None else gap_min_bps
    if not ref15 or not ref5 or ref15 <= 0:
        return None
    if abs((ref5 / ref15 - 1.0) * 1e4) < g:
        return None
    return "Up" if ref15 > ref5 else "Down"


def querer(bid5, ask5, bid15, ask15, umbral, mq=None):
    """Precio al que QUEREMOS estar pujando en este instante (join del mejor bid del 5m lado s) o None (= no cotizar / cancelar).
    Identico a `want` de r3/sim_dia3.py: libro valido y no cruzado, cota con margen, precio <= p_limite, siempre < ask y >= 0,01."""
    mq = CONFIG["mq"] if mq is None else mq
    for x in (bid5, ask5, bid15):
        if x is None or isinstance(x, float) and math.isnan(x):
            return None
    if ask15 is not None and not (isinstance(ask15, float) and math.isnan(ask15)) and bid15 > ask15:
        return None                                    # libro 15m cruzado
    if bid5 > ask5:
        return None                                    # libro 5m cruzado
    pl = p_limite(bid15, umbral)
    if pl is None:
        return None
    cand = bid5                                        # JOIN: nunca mejoramos el mejor bid
    if not (cand <= pl + 1e-9 and cand < ask5 - 1e-9 and cand >= 0.01 and margen(bid15, ask5) >= mq):
        return None
    return round(cand, 2)


def acciones(precio, cfg=CONFIG):
    """max(5, 2 EUR / precio), en centesimas hacia arriba (rejilla del CLOB)."""
    return max(cfg["min_acciones"], math.ceil(cfg["stake_eur"] / precio * 100 - 1e-9) / 100)


def pnl_relleno(acc, precio_medio, gana, cfg=CONFIG):
    """PnL de una posicion maker: pago 1/0 por accion - coste + rebate (20 % de la comision que habria pagado el tomador)."""
    return acc * (1.0 if gana else 0.0) - acc * precio_medio + cfg["rebate"] * fee(precio_medio, cfg) * acc


def hash_config():
    h = hashlib.sha256(json.dumps(CONFIG, sort_keys=True).encode())
    h.update(Path(__file__).read_bytes())
    return h.hexdigest()[:16]
