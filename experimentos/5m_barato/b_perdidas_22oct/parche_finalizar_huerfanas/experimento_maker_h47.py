#!/usr/bin/env python3
"""experimento_maker_h47.py -- H47 SIM-REAL: micro-órdenes MAKER reales H35 DEEP_PEG (5m ETH/SOL/XRP) para CALIBRAR el simulador.
⚠️ HERRAMIENTA MANUAL que, con --confirmo-dinero-real, ENVÍA ÓRDENES REALES con la wallet DEDICADA. Nunca en cron/screen/watchdog.
Requiere /code-review (medium) + OK final de Javi. Sin --confirmo-dinero-real es un ENSAYO EN SECO: no crea cliente CLOB, no firma, no
envía ni cancela nada; lee solo datos PÚBLICOS (gamma + WS de mercado) y simula los rellenos con el modelo conservador (CONS).

QUÉ MIDE (REGISTRO_HIPOTESIS H47, regla fijada ANTES de empezar): ¿el simulador maker predice la tasa de relleno, el acuerdo puja a puja y el
markout reales? Válido si |tasa real − simulada| <= 8 pp, acuerdo >= 0,70 en ambas direcciones y |markout| dif <= 0,03 (preregistrado con ~230 pujas, ~70
rellenos; tope ampliado a 500 pujas el 22-Oct por Javi para tener más muestra, el criterio de validez no cambia). NO mide EV (harían falta ~4.500 rellenos). Si falla, el hilo maker offline se cierra.

POLÍTICA (H35 DEEP_PEG, idéntica al motor `analisis_5m_maker_banda_deep_peg.DeepMotor`): por (mercado, cara), T en (60, 300] s, bid top en
(0,11, 0,30]; puja GTC post-only BUY en top − k·0,01 (k: ETH 2, SOL 1, XRP 1, fijados en DESC), nunca mejora el top y siempre < ask; con el
top fuera de la rejilla se baja al céntimo inferior; repega cuando el objetivo cambia (cancelar, leer el relleno, volver a pujar); parada a
T = 60 s (--t-stop 90 = variante H35b, se registra aparte). Una sola cara por mercado: la primera cuyo bid top entra en la banda (bid de una
cara barata <= 0,30 implica la contraria >= 0,70: no hay dos). Un relleno (aunque sea parcial) CIERRA la puja (nunca órdenes < 5 acc).
PUJA = unidad (mercado, cara). N cuenta mercados con al menos una intención de POST (se persiste en el ledger: un reinicio no lo reinicia).

ESCALONES (se eligen con --escalon; ledger separado por escalón, un ÚNICO lock y un ÚNICO fichero .KILL para toda la wallet):
  A  hasta 40 pujas a 0,01-0,03 (escalera 0,02 -> 0,01 -> 0,03 en cada "repegado" que haría la regla B): no deben rellenarse; validan
     maquinaria, latencias, ledger, cancelación y si el exchange acepta notional < 1 $ en post-only (5 acc * 0,03 = 0,15 $).
  B  N FIJO de 500 pujas (tope duro del código; subido de 230 el 22-Oct por Javi), máx 5 vivas a la vez, precio de la regla H35.
  Parada SOLO por: saldo de la dedicada < SUELO (la puja nueva exige saldo − comprometido − coste >= SUELO; saldo ilegible -> no se envía y,
  si dura > 2 min, se para; < SUELO sin nada vivo durante 15 min -> se para), fallo de maquinaria/ledger descuadrado (kill persistente) o N
  alcanzado. SIN kill por PnL.
  SUELO DINÁMICO (Javi, opción b, 19-Oct; 2ª y 3ª /code-review): SUELO = saldo verificado en el arranque − PRESUPUESTO_UTIL (5 USD por
  decisión de Javi 19-Oct; --presupuesto-util, en real nunca más de 5). «Verificado» = dos lecturas on-chain FIJADAS A UN BLOQUE (reciente,
  <= 60 s, y la 2ª de un bloque ESTRICTAMENTE mayor) que coinciden (<= 0,05); se usa la ÚLTIMA lectura. Cada lectura posterior que decide
  enviar o cuadrar exige también bloque reciente y no anterior al último visto (si no: saldo ilegible, fail-closed). Sin verificar, con saldo
  de arranque < presupuesto + 1 USD, o con una línea ilegible/corrupta en un ledger real -> no hay suelo -> NO se opera (fail-closed).
  El suelo se ESCRIBE (fsync) al enviar la primera orden real, no al arrancar, y nunca baja respecto a los ya fijados en esa wallet (max con
  los de TODOS los ledgers reales: escalones H47 y experimento_pares_dedicada; +<= 0,05 sobre el máximo previo es ruido). Dentro de la
  ejecución el suelo SUBE con el saldo: un alza confirmada (2ª lectura de un bloque más nuevo, entre 2 y 10 s después; una ilegible la anula)
  eleva el máximo de saldo y con él el suelo (máx. − 5); se gasta contra min(saldo, máximo). Mientras no se confirma no se envía.
  Ledgers: UN solo escaneo por arranque. Retirada voluntaria: `--reiniciar-suelo "motivo"` (saldo verificado + confirmación escrita + locks de
  H47 y de pares) deja `suelo_reiniciado` (suelos anteriores dejan de contar y `saldo_base` pasa a ser la BASE del cuadre; solo explican las
  órdenes posteriores). Línea ilegible tras un crash: `--aceptar-linea-ilegible "motivo"` la acepta por sha SIN perder los suelos válidos.
  4ª review: ambas exigen kill limpio, nada abierto en ledgers ni exchange y saldo verificado; el reseteo nº 3 y siguientes de una wallet
  exige `--segundo-motivo` y confirmación reforzada; la base nueva del cuadre la lee también experimento_pares_dedicada
  (reinicio_suelo_compartido). Aceptar solo vale para líneas que parezcan JSON cortado (se guarda la cruda en base64).
  NO se borra ningún ledger a mano.

TAMAÑO: 5 acciones (mínimo del mercado, orderMinSize=5). Si el mínimo de 1 $ de nocional aplicara a post-only (se descubre en el escalón A
con rechazos 4xx), --min-nocional 1.0 (defecto) sube el tamaño a ceil(1/precio) acc (tope 10); con --min-nocional 0 se envían 5 acc tal cual.
El tamaño real va en cada intención del ledger: el simulador debe reproducir ESE tamaño (SH).

REGISTRO por puja/orden (ledger JSONL en /root/polymarket-research-datalogs/, eventos con "real"): `config`, `puja_post` (decisión, libro de
5 niveles de bid, cola delante al entrar, objetivo H35, k, T), `post_lat` (envío, retorno, ms), `post_ok`/`visto` (hora en que el WS muestra
nuestra orden), `cancel_lat`, `lectura`/`relleno` (get_order cada POLL_S + match_time de get_trades), `gemelo_relleno` (predicción CONS del
simulador para ESA misma orden: modelo de analisis_maker_cancelacion_binance.simular_token, con operaciones del WS del CLOB), `puja_fin`
(resumen, markout +5/+30/+120 s por € sobre el mid del token por RECEPCIÓN, missing si pasa del cierre) y `mercado_fin`.
La contabilidad de dinero es la de `pares_contabilidad` (intervalo [lo, hi] por orden, verificación a los 30 s, cuadre on-chain).

SEGURIDAD (pase de casos límite de CLAUDE.md, todo fail-closed): ver tests test_experimento_maker_h47.py. Heredada de Exp (25 /code-review):
identidad por hash EIP-712 antes de enviar, intención con fsync, kill persistente, señales, cancelación por hash, reinicio que cancela lo
propio. Nueva: suelo de saldo dinámico, N persistente, tope por orden (3 $), tope de órdenes por puja (400) y total (20.000), una orden viva por puja.

Uso:  .venv/bin/python experimento_maker_h47.py --escalon B                       (ENSAYO EN SECO, por defecto)
      .venv/bin/python experimento_maker_h47.py --escalon A --confirmo-dinero-real  (REAL, tras code-review + OK Javi)
"""
import argparse
import base64
import hashlib
import json
import math
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import experimento_pares_cola_15m as X          # noqa: E402  (harness revisado: Exp, Libro, ledger, kill, cliente dedicado)
import pares_contabilidad as C                  # noqa: E402
try:                                            # parche robustez (solo registros): si falla el import, el ejecutor sigue SIN el
    import h47_robustez as R                    # noqa: E402
except Exception as _ex_r:
    R = None
    print(f"[h47_robustez] no disponible: {type(_ex_r).__name__}: {_ex_r}", file=sys.stderr, flush=True)

DATALOGS = Path("/root/polymarket-research-datalogs")
K_POR_MONEDA = {"eth": 2, "sol": 1, "xrp": 1}
T_INI = 298.0
T_STOP_DEF = 60.0
POLL_S = 0.5                 # lectura de get_order de las órdenes vivas (la fecha de relleno tiene esa resolución + match_time)
LOOP_S = 0.1
ASENTAR_H47_S = 1.5          # 1ª /code-review #1: IGUAL al harness (X.ASENTAR_S, 9ª review): un casado de ms antes del cancel puede tardar ~1 s en verse
ASENTAR_MIN_REAL_S = 1.5     # en real NUNCA por debajo (se pierde el relleno, se repuja el mismo bid y se rompe «un relleno cierra la puja»)
MIN_ENTRE_ACCIONES_S = 0.1
REQUOTE_INVALIDO_S = 2.0
FIN_ESPERA_S = 35.0          # tras el cierre: markouts, get_trades
PRESUPUESTO_UTIL = 5.0       # USD que el experimento puede gastar: suelo = saldo verificado en el arranque − esto (Javi, 19-Oct: 5, no 12)
SALDO_TOL_VERIF = 0.05       # dos lecturas on-chain seguidas deben coincidir en <= esto para dar el saldo por verificado
SALDO_ARRANQUE_MARGEN = 1.0  # 2ª /code-review #3: saldo de arranque >= presupuesto + esto (si no, el suelo sería ~0: no se opera)
BLOQUE_EDAD_MAX_S = 60.0     # 2ª /code-review #4: el bloque de la lectura debe ser así de reciente (Polygon ~2 s/bloque)
BLOQUE_ADELANTO_MAX_S = 30.0 # ... y su hora no puede estar más adelantada que esto respecto al reloj local
ALZA_CONFIRMA_S = 2.0        # un alza de saldo sobre el máximo se confirma con otra lectura >= esto después (caché de saldo = 2 s)
ALZA_CADUCA_S = 10.0         # 3ª /code-review #8: un alza sin confirmar caduca (la siguiente lectura alta empieza otra confirmación)
BLOQUE_RETROCESO_TOL = 3     # 4ª /code-review B2: nodos desalineados unos bloques no son «retroceso» (el máximo visto nunca baja)
REINICIOS_MAX = 2            # 4ª /code-review M2: reseteos del suelo por wallet sin segundo motivo escrito y confirmación reforzada
ROTACION_SALDO_DURO = 12.0   # 20-Oct (Javi, opción 2): --rotar-tanda NO rota con saldo verificado < esto + presupuesto (tope real de pérdida acumulada)
ROTACION_MAX_DIA = 12        # rotaciones automáticas por día UTC (cada una = una tanda más de PRESUPUESTO_UTIL)
ROTACION_MARGEN_AGOTADA = 1.5  # tanda agotada si saldo verificado − suelo vigente < esto (una puja mínima cuesta ~1,1-1,35 USD)
ESPERA_LECTURAS_S = 2.5      # 3ª /code-review #6: entre las dos lecturas del arranque (> 1 bloque de Polygon): la 2ª exige un bloque MAYOR
SALDO_REINTENTOS = 3
ESPERA_REINTENTO_S = 1.0
ESPERA_SALDO_BAJO_S = 900.0
SALDO_ILEGIBLE_MAX_S = 120.0
COSTE_MAX_ORDEN = 3.0        # $ por orden (10 acc * 0,30)
MAX_ORDENES_PUJA, MAX_ORDENES_TOTAL = 400, 20000
N_MAX = {"A": 40, "B": 500}
MAX_VIVAS = 5
MAX_EXC_CTX = 3              # 1ª /code-review #4: excepciones de paso() por mercado antes de abandonarlo (sin bucle infinito de excepciones)
SIZE_MIN, SIZE_MAX = 5, 10
A_ESCALERA = (0.02, 0.01, 0.03)
MARK_S = (5, 30, 120)
GAMMA = "https://gamma-api.polymarket.com/markets"
LOCK_PARES = DATALOGS / "experimento_pares_dedicada.lock"


# ---------------------------------------------------------------- reglas puras (probadas sin red)
def mils(p):
    return int(round(float(p) * 1000))


def en_banda(bid, ask):
    """Banda de la decisión DEEP: libro válido y bid top en (0,11, 0,30] (analisis_5m_maker_banda_deep_peg.banda_d)."""
    try:
        b, a = mils(bid), mils(ask)
    except (TypeError, ValueError):
        return False
    return 0 < a and b < a and 110 < b <= 300


def objetivo_h35(bid, ask, k):
    """Precio de la puja DEEP (mismo cálculo que DeepMotor._objetivo en milésimas): top − k ticks si el top está en rejilla; si no, el
    céntimo inferior − (k−1) ticks. Nunca >= bid ni >= ask; fuera de [0,10, 0,30] -> None."""
    b, a = mils(bid), mils(ask)
    o = b - k * 10 if b % 10 == 0 else (b // 10 - (k - 1)) * 10
    return round(o / 1000.0, 3) if (100 <= o <= 300 and o < b and o < a) else None


def en_rejilla(p):
    return abs(p * 100 - round(p * 100)) <= 1e-6


def contar_intenciones(eventos, real):
    """(total, {slug: n}) de órdenes DISTINTAS con intencion_post de ese modo (real/seco) en una lista de eventos de ledger. Un alias del
    hash (segunda intención con `alias_de`) es la MISMA orden y no cuenta dos veces."""
    total, por_slug = 0, {}
    for e in eventos:
        if isinstance(e, dict) and e.get("tipo") == "intencion_post" and bool(e.get("real")) == bool(real) and not e.get("alias_de"):
            total += 1
            por_slug[e.get("slug")] = por_slug.get(e.get("slug"), 0) + 1
    return total, por_slug


def tamano_orden(precio, size_base, min_nocional):
    """Tamaño a enviar: size_base (>= 5) o, si el nocional < min_nocional, ceil(min_nocional/precio) acc (tope SIZE_MAX).
    None si no cabe (no se envía)."""
    if size_base < SIZE_MIN or size_base > SIZE_MAX or precio <= 0:
        return None
    s = float(size_base)
    if min_nocional > 0 and s * precio < min_nocional - 1e-9:
        s = float(math.ceil(min_nocional / precio - 1e-9))
    if s > SIZE_MAX or s < SIZE_MIN:
        return None
    return s


def precio_a(n):
    """Escalón A: escalera 0,02 -> 0,01 -> 0,03 (cada repegado que haría la regla B)."""
    return A_ESCALERA[n % len(A_ESCALERA)]


def sim_uno(lib, par, o, f_prev):
    """Predicción CONS para UNA orden (copia de X.Exp.simular_rellenos; 1ª /code-review #9: NO se toca el harness revisado 25 veces, la
    igualdad la fija test_sim_uno_igual_que_simular_rellenos_del_harness_en_flujos_aleatorios: si el simulador cambia, ese test falla): operaciones del CLOB (last_trade_price) por DEBAJO de nuestro
    precio llenan entera; volumen A nuestro precio por encima de la cola delante al entrar = parcial. Consumen un bid del token las ventas
    tomadoras del token y las compras tomadoras del contrario (acuñación). Solo operaciones con hora del exchange >= envío + 70 ms y
    <= cancelación + 60 ms. -> acciones simuladas llenadas (monótono)."""
    t_can = o.get("t_cancel")
    q = float(o["precio"])
    f = f_prev
    idx = o.setdefault("i_sim", {})
    o.setdefault("vol_sim", 0.0)
    for tk, lado_tomador in ((o["tok"], "SELL"), (par[o["tok"]], "BUY")):
        if tk not in idx:
            idx[tk] = lib.indice_trades(tk, o["t_post"] - 1.0)
        nuevos = lib.trades_desde(tk, idx[tk])
        idx[tk] += len(nuevos)
        for _tr, tx, p, sz, sd in nuevos:
            if sd != lado_tomador or tx < o["t_post"] + X.LAT_POST_S:
                continue
            if t_can is not None and tx > t_can + X.LAT_CANCEL_S:
                continue
            pe = p if tk == o["tok"] else round(1.0 - p, 2)
            if f >= o["size"] - 1e-9:
                break
            if pe < q - 1e-9:
                f = float(o["size"])
            elif abs(pe - q) < 1e-9:
                o["vol_sim"] += sz
                f = min(float(o["size"]), max(f, o["vol_sim"] - float(o["cola"] or 0.0)))
    return f


def mercado_5m(coin, ini):
    r = requests.get(GAMMA, params={"slug": f"{coin}-updown-5m-{ini}"}, timeout=10).json()
    if not r:
        return None
    m = r[0]
    toks, outs = json.loads(m["clobTokenIds"]), json.loads(m["outcomes"])
    return {"slug": m["slug"], "id": str(m["id"]), "fin": ini + 300, "toks": dict(zip(outs, toks)), "coin": coin, "ini": ini,
            "min_size": m.get("orderMinSize")}


# ---------------------------------------------------------------- saldo con bloque, ledgers hermanos y suelos (2ª /code-review)
TIPOS_SUELO = ("suelo_fijado", "suelo_subido")
TIPOS_ACEPTA = ("suelo_reiniciado", "linea_ilegible_aceptada")


class LedgerIlegible(Exception):
    """Un ledger real de la wallet no se puede leer, o tiene una línea de suelo ilegible/corrupta: sin suelo fiable NO se opera."""


def saldo_con_bloque(wallet):
    """(pUSD, número de bloque, hora del bloque) de la wallet, con la lectura FIJADA a ese bloque (2ª /code-review #4: dos lecturas «latest»
    del mismo RPC no prueban frescura; un nodo atrasado devuelve el mismo bloque viejo). None si falla (no se opera)."""
    try:
        from polygon_rpc import hex_valido, llamar
        blk = llamar("eth_getBlockByNumber", ["latest", False], grupo="latest", intentos=1, timeout=(2, 3), plazo_total_s=6, log=None,
                     validar=lambda r: isinstance(r, dict) and hex_valido(r.get("number")) and hex_valido(r.get("timestamp")))
        num, ts = int(blk["number"], 16), float(int(blk["timestamp"], 16))
        res = llamar("eth_call", [{"to": X.PUSD, "data": "0x70a08231" + wallet[2:].lower().rjust(64, "0")}, blk["number"]],
                     grupo="latest", intentos=1, timeout=(2, 3), plazo_total_s=6, validar=hex_valido, log=None)
        return int(res, 16) / 1e6, num, ts
    except Exception:
        return None


def lecturas_verificadas(a, b, ahora):
    """¿Dos lecturas (saldo, bloque, hora del bloque) prueban un saldo vigente? Ambas legibles, bloques recientes (<= BLOQUE_EDAD_MAX_S, sin
    adelanto absurdo), bloque de la 2ª ESTRICTAMENTE mayor que el de la 1ª (3ª /code-review #6: el mismo bloque dos veces no prueba que el
    nodo avance) y saldos que coinciden en <= SALDO_TOL_VERIF."""
    if a is None or b is None:
        return False
    for _s, _n, ts in (a, b):
        edad = ahora - ts
        if edad > BLOQUE_EDAD_MAX_S or edad < -BLOQUE_ADELANTO_MAX_S:
            return False
    return b[1] > a[1] and abs(a[0] - b[0]) <= SALDO_TOL_VERIF + 1e-9


def lectura_valida(r, ahora, bloque_visto):
    """3ª /code-review #5: una lectura suelta (saldo, bloque, hora) sirve para decidir enviar/cuadrar solo si su bloque es reciente y no
    anterior al último visto (monotonía). -> (ok, motivo)."""
    if r is None:
        return False, "sin_lectura"
    _s, n, ts = r
    edad = ahora - ts
    if edad > BLOQUE_EDAD_MAX_S or edad < -BLOQUE_ADELANTO_MAX_S:
        return False, "bloque_no_reciente"
    if bloque_visto is not None and n < bloque_visto - BLOQUE_RETROCESO_TOL:
        return False, "bloque_retrocede"
    return True, None


def saldo_verificado_wallet(wallet):
    """(saldo, bloque) VERIFICADO de la wallet (dos lecturas a bloques reciente y estrictamente crecientes que coinciden en <= tolerancia,
    hasta SALDO_REINTENTOS rondas); la ÚLTIMA lectura, no el máximo. None si no se puede verificar."""
    for i in range(SALDO_REINTENTOS):
        a = saldo_con_bloque(wallet)
        time.sleep(ESPERA_LECTURAS_S)
        b = saldo_con_bloque(wallet)
        if lecturas_verificadas(a, b, time.time()):
            return b[0], b[1]
        if i + 1 < SALDO_REINTENTOS:
            time.sleep(ESPERA_REINTENTO_S)
    return None


def ledgers_reales_hermanos():
    """2ª /code-review #8: helper ÚNICO de los ledgers de la MISMA wallet dedicada distintos del propio: los escalones H47 reales (no los
    `_seco_`) y el real de experimento_pares_dedicada. Lo usan el tope total de órdenes y los suelos previos."""
    d = Path(X.LEDGER).parent
    propio = Path(X.LEDGER).resolve()
    out = [f for f in sorted(d.glob("experimento_h47_*_ledger.jsonl")) if "_seco_" not in f.name]
    out.append(d / "experimento_pares_dedicada_ledger.jsonl")
    return [f for f in out if f.exists() and f.resolve() != propio]


def _sha(txt):
    return hashlib.sha256(txt.encode("utf-8", "replace")).hexdigest()[:16]


def parece_truncada(t):
    """4ª /code-review M1: ¿la línea ilegible parece un JSON CORTADO por un crash (empieza por «{», no cierra y no tiene bytes de control ni
    sustitutos de decodificación)? Una línea con basura binaria, o completa pero inválida, NO lo es (no se puede aceptar)."""
    return t.startswith("{") and not t.endswith("}") and "\ufffd" not in t and not any(ord(c) < 32 for c in t)


def _defecto(f, t):
    return (f.name, _sha(t), t[:80], parece_truncada(t), t[:2000])


def _lineas(f):
    """Líneas del fichero en streaming (3ª /code-review #9: sin cargar el ledger entero)."""
    try:
        with open(f, "rb") as fh:
            for raw in fh:
                yield raw.decode("utf-8", "replace")
    except OSError as e:
        raise LedgerIlegible(f"ledger {Path(f).name} no se puede leer ({type(e).__name__}): no hay suelo fiable") from e


def escanear_ledgers_reales(wallet):
    """UN solo recorrido (streaming) del ledger propio y los hermanos (RAW, sin la tolerancia de X.leer_ledger). Devuelve
    {suelos: [(ts, tipo, valor)], reinicio_ts, reinicio_epoch, reinicio_base, aceptadas: {(fichero, sha)}, defectos: [(fichero, sha, texto)],
    intenciones_otros: n}. Defecto = línea no JSON, o evento suelo_*/suelo_reiniciado/linea_ilegible_aceptada real con wallet/ts/valores no
    válidos. Un `suelo_reiniciado` de esta wallet descarta los suelos con ts <= su ts y fija la BASE del cuadre (saldo_base); tanto él como
    `linea_ilegible_aceptada` aceptan los defectos que listan (fichero + sha de la línea) SIN descartar suelos el segundo."""
    propio = Path(X.LEDGER)
    ficheros = ([propio] if propio.exists() else []) + ledgers_reales_hermanos()
    suelos, resets, aceptan, defectos, intenciones = [], [], [], [], 0
    rotaciones = []            # 20-Oct: reinicios AUTOMÁTICOS (origen rotar_tanda); no consumen el tope REINICIOS_MAX del reseteo manual
    for f in ficheros:
        vistos = set()
        for ln in _lineas(f):
            t = ln.strip()
            if not t:
                continue
            try:
                e = json.loads(t)
            except ValueError:
                defectos.append(_defecto(f, t))
                continue
            if not isinstance(e, dict):
                defectos.append(_defecto(f, t))
                continue
            tipo = e.get("tipo")
            if f != propio and tipo == "intencion_post" and e.get("real") and not e.get("alias_de") and e.get("oid") not in vistos:
                vistos.add(e.get("oid"))
            if tipo not in TIPOS_SUELO + TIPOS_ACEPTA or not e.get("real"):
                continue
            w, ts = e.get("wallet"), None
            try:
                ts = datetime.fromisoformat(str(e.get("ts")))
                if ts.tzinfo is None:
                    raise ValueError("ts sin zona")
            except (TypeError, ValueError):
                ts = None
            v = C._num(e.get("suelo")) if tipo in TIPOS_SUELO else 0.0
            if not isinstance(w, str) or not w or ts is None or v is None or v < 0:
                defectos.append(_defecto(f, t))
                continue
            if w.lower() != str(wallet).lower():
                continue
            if tipo == "suelo_reiniciado":
                b = C._num(e.get("saldo_base"))
                resets.append((ts, b if (b is not None and b > 0) else None))      # None = formato antiguo (sin saldo_base): ver suelos_previos
                if e.get("origen") == "rotar_tanda" and b is not None and b > 0:
                    rotaciones.append(ts)
                aceptan.append(e)
            elif tipo == "linea_ilegible_aceptada":
                aceptan.append(e)
            else:
                suelos.append((ts, tipo, v))
        intenciones += len(vistos)
    reinicio_ts, reinicio_base = max(resets, key=lambda x: x[0]) if resets else (None, None)
    legacy = reinicio_ts is not None and reinicio_base is None
    aceptadas = set()
    for e in aceptan:
        for par in e.get("ilegibles_aceptadas") or []:
            if isinstance(par, (list, tuple)) and len(par) == 2:
                aceptadas.add((str(par[0]), str(par[1])))
    if reinicio_ts is not None:
        suelos = [x for x in suelos if x[0] > reinicio_ts]
    return {"suelos": suelos, "reinicio_ts": reinicio_ts, "reinicio_epoch": reinicio_ts.timestamp() if reinicio_ts else None,
            "reinicio_base": reinicio_base, "reinicio_legacy": legacy, "n_reinicios": sum(1 for _, b in resets if b is not None), "n_rotaciones": len(rotaciones),
            "aceptadas": aceptadas, "defectos": defectos, "intenciones_otros": intenciones}


def suelos_previos(wallet, esc=None):
    """Suelos ya fijados en esta wallet (todos los ledgers reales, desde el último reinicio). FAIL-CLOSED: un ledger ilegible o una línea
    defectuosa no aceptada por un `suelo_reiniciado`/`linea_ilegible_aceptada` lanza LedgerIlegible. `esc`: escaneo ya hecho (se reutiliza)."""
    r = esc if esc is not None else escanear_ledgers_reales(wallet)
    malos = [d for d in r["defectos"] if (d[0], d[1]) not in r["aceptadas"]]
    if malos:
        raise LedgerIlegible(f"{len(malos)} línea(s) ilegible(s)/corrupta(s) en ledgers reales (p. ej. {malos[0][0]}: {malos[0][2]!r}): "
                             "no hay suelo fiable; revisar y, si procede, --aceptar-linea-ilegible o --reiniciar-suelo")
    if r.get("reinicio_legacy"):            # 4ª /code-review B1: ruta de recuperación explícita, no circular
        raise LedgerIlegible("el último `suelo_reiniciado` es del formato antiguo (sin saldo_base): no fija la base del cuadre. Recuperación: "
                             "volver a ejecutar --reiniciar-suelo (verifica el saldo, escribe un evento nuevo con saldo_base y lo supera)")
    return [v for _, _, v in r["suelos"]]


def _fsync_ledger():
    """fsync del ledger propio (el X.log del harness solo lo hace para intencion_post/kill)."""
    fd = os.open(str(X.LEDGER), os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _confirmar(leer, clave):
    return str(leer(f"Escribe exactamente «{clave}» para confirmar: ")).strip() == clave


def ordenes_abiertas_en_ledgers():
    """Órdenes REALES con relleno aún sin cerrar (hi > lo: sin verificar) en el ledger propio y los hermanos: nº. Ilegibles se saltan (no
    suman ni restan: el escaneo de suelos ya las trata como defecto)."""
    n = 0
    for f in [Path(X.LEDGER)] + ledgers_reales_hermanos():
        evs = []
        if Path(f).exists():
            for ln in _lineas(f):
                try:
                    e = json.loads(ln)
                except ValueError:
                    continue
                if isinstance(e, dict):
                    evs.append(e)
        n += sum(1 for o in C.plegar(evs).values() if not o.alias and o.abierta)
    return n


def comprobar_para_reseteo(wallet, cli, nombre):
    """4ª /code-review M1/M2: precondiciones COMUNES de --reiniciar-suelo y --aceptar-linea-ilegible (todas fail-closed, SystemExit): sin kill
    pendiente (ledger o ficheros .KILL de H47 y pares: si lo hay, hay que investigar y --rearmar-kill antes), ninguna orden sin cerrar en los
    ledgers ni viva en el exchange (así nada anterior deja de ser «explicable») y saldo on-chain verificado. -> (saldo, bloque)."""
    k = X.kill_pendiente()
    if k:
        raise SystemExit(f"{nombre}: hay un kill pendiente ({str(k)[:140]}): investigar y --rearmar-kill antes; no se toca nada")
    d = Path(X.LEDGER).parent
    for kf in ("experimento_h47.KILL", "experimento_pares_dedicada.KILL"):
        if (d / kf).exists():
            raise SystemExit(f"{nombre}: existe {kf} (kill de la wallet): investigar y --rearmar-kill antes")
    n = ordenes_abiertas_en_ledgers()
    if n:
        raise SystemExit(f"{nombre}: {n} orden(es) real(es) sin cerrar/verificar en los ledgers: esperar a que se verifiquen")
    if cli is None:
        raise SystemExit(f"{nombre}: sin cliente no se pueden comprobar las órdenes abiertas del exchange: fail-closed")
    try:
        vivas = cli.get_open_orders()
    except Exception as e:
        raise SystemExit(f"{nombre}: no se pudieron consultar las órdenes abiertas del exchange ({type(e).__name__}): fail-closed") from e
    if vivas:
        raise SystemExit(f"{nombre}: hay {len(vivas)} orden(es) viva(s) en el exchange: cancelarlas y verificarlas antes")
    sv = saldo_verificado_wallet(wallet)
    if sv is None:
        raise SystemExit(f"{nombre}: no se puede verificar el saldo on-chain (bloque reciente, lecturas que coinciden): no se hace nada")
    return sv


def reiniciar_suelo(wallet, motivo, leer=input, cli=None, motivo2=None):
    """2ª /code-review #7 + 3ª #2 + 4ª M2: reseteo EXPLÍCITO y auditado del suelo (retirada voluntaria de fondos). Exige las precondiciones de
    comprobar_para_reseteo (kill limpio, nada abierto en ledgers ni exchange, saldo verificado) y confirmación escrita; deja UN
    `suelo_reiniciado` (fsync) con los suelos descartados, las líneas ilegibles aceptadas y `saldo_base`: la BASE del cuadre pasa a ser ese
    saldo (y solo cuentan como explicables las órdenes posteriores al evento; también para experimento_pares_dedicada, ver
    reinicio_suelo_compartido). Los suelos con ts <= el del evento dejan de contar en TODOS los ledgers. A partir del REINICIOS_MAX-ésimo
    reseteo de la wallet hace falta un segundo motivo escrito (`motivo2`) y una confirmación reforzada. No toca ningún fichero existente."""
    if motivo is None or not str(motivo).strip():
        raise SystemExit("--reiniciar-suelo exige un motivo no vacío")
    sv = comprobar_para_reseteo(wallet, cli, "--reiniciar-suelo")
    r = escanear_ledgers_reales(wallet)
    n = r["n_reinicios"] - r["n_rotaciones"]          # solo los reseteos manuales cuentan para el tope REINICIOS_MAX
    reforzado = n >= REINICIOS_MAX
    if reforzado and (motivo2 is None or not str(motivo2).strip()):
        raise SystemExit(f"--reiniciar-suelo: esta wallet ya tiene {n} reseteos (máx. {REINICIOS_MAX}): exige --segundo-motivo no vacío "
                         "y una confirmación reforzada")
    previos = [v for _, _, v in r["suelos"]]
    print(f"wallet {wallet}\nsaldo verificado (nueva base del cuadre): {sv[0]:.4f} (bloque {sv[1]})\nreseteos previos de la wallet: {n}\n"
          f"suelos que dejarían de contar: {previos}\n"
          f"líneas ilegibles que se darían por vistas: {[(d[0], d[2]) for d in r['defectos'] if (d[0], d[1]) not in r['aceptadas']]}", flush=True)
    if not _confirmar(leer, f"REINICIAR SUELO {wallet[-6:]}" + (f" VEZ {n + 1}" if reforzado else "")):
        print("no confirmado: nada cambia")
        return None
    ev = {"tipo": "suelo_reiniciado", "wallet": wallet, "motivo": str(motivo)[:300], "suelos_descartados": previos,
          "saldo_base": sv[0], "bloque": sv[1], "n_reinicio": n + 1,
          "ilegibles_aceptadas": sorted({(d[0], d[1]) for d in r["defectos"]} | r["aceptadas"])}
    if reforzado:
        ev["motivo2"] = str(motivo2)[:300]
    X.log(dict(ev, real=True))
    _fsync_ledger()
    time.sleep(0.01)                  # los eventos posteriores llevan un ts estrictamente mayor
    return ev


def rotar_tanda(wallet, cli=None, hoy=None):
    """20-Oct (Javi, opción 2): rotación AUTOMÁTICA y auditada de la tanda (sin confirmación interactiva), para el vigilante de tandas. Un
    `suelo_reiniciado` con origen='rotar_tanda' que sube la base del cuadre al saldo verificado: la tanda siguiente puede arriesgar de nuevo
    PRESUPUESTO_UTIL. Todo fail-closed (SystemExit), SIN saltarse nada de H47: (1) las MISMAS precondiciones que --reiniciar-suelo (sin kill,
    nada abierto en ledgers ni exchange, saldo on-chain verificado); (2) la tanda debe estar REALMENTE agotada (saldo verificado − suelo vigente <
    ROTACION_MARGEN_AGOTADA) -> no se puede usar para subir el riesgo con una tanda viva; (3) saldo verificado >= ROTACION_SALDO_DURO +
    PRESUPUESTO_UTIL (la pérdida acumulada nunca baja de ese suelo duro); (4) como mucho ROTACION_MAX_DIA rotaciones por día UTC."""
    sv = comprobar_para_reseteo(wallet, cli, "--rotar-tanda")
    r = escanear_ledgers_reales(wallet)
    try:
        previos = suelos_previos(wallet, r)          # FAIL-CLOSED: línea ilegible/defectuosa o reinicio en formato antiguo -> no se rota
    except LedgerIlegible as e:
        raise SystemExit(f"--rotar-tanda: {e}") from e
    if not previos:
        raise SystemExit("--rotar-tanda: no hay ningún suelo fijado desde el último reinicio: nada que rotar")
    suelo = max(previos)
    if sv[0] - suelo >= ROTACION_MARGEN_AGOTADA:
        raise SystemExit(f"--rotar-tanda: la tanda NO está agotada (saldo {sv[0]:.4f} − suelo {suelo:.4f} >= {ROTACION_MARGEN_AGOTADA}): no se rota")
    if sv[0] < ROTACION_SALDO_DURO + PRESUPUESTO_UTIL - 1e-9:
        raise SystemExit(f"--rotar-tanda: saldo {sv[0]:.4f} < suelo duro {ROTACION_SALDO_DURO} + presupuesto {PRESUPUESTO_UTIL}: no se rota")
    # CUADRE (misma condición que Exp47.cuadre): una bajada de saldo que el ledger no explica NO es «tanda agotada»; rebasear el saldo la taparía.
    evs = X.leer_ledger()
    base = r["reinicio_base"] if r["reinicio_base"] is not None else next(
        (C._num(e.get("valor")) for e in evs if e.get("tipo") == "saldo_inicial" and e.get("real")), None)
    if base is None:
        raise SystemExit("--rotar-tanda: sin saldo base (saldo_inicial/reinicio) en el ledger: fail-closed")
    ords = C.plegar(evs)
    if r["reinicio_epoch"] is not None:
        ords = {k: o for k, o in ords.items() if o.t_int > r["reinicio_epoch"]}
    explicable = C.exposicion_maxima(ords)
    if base - sv[0] > explicable + C.TOLERANCIA_SALDO:
        raise SystemExit(f"--rotar-tanda: salieron {base - sv[0]:.4f} pUSD y el ledger solo explica {explicable:.4f}: dinero que no cuadra, no se rota")
    ahora = datetime.now(timezone.utc)
    corte = (ahora - timedelta(hours=24)).timestamp() if hoy is None else None
    n_24 = 0
    for f in [Path(X.LEDGER)] + ledgers_reales_hermanos():           # tope sobre TODOS los ledgers reales de la wallet, ventana móvil de 24 h
        if not Path(f).exists():
            continue
        for ln in _lineas(f):
            try:
                e = json.loads(ln)
            except ValueError:
                continue
            if not (isinstance(e, dict) and e.get("tipo") == "suelo_reiniciado" and e.get("origen") == "rotar_tanda"
                    and str(e.get("wallet", "")).lower() == str(wallet).lower()):
                continue
            try:
                t = datetime.fromisoformat(str(e.get("ts"))).timestamp()
            except ValueError:
                continue
            if (corte is not None and t >= corte) or (hoy is not None and str(e.get("ts", ""))[:10] == hoy):
                n_24 += 1
    if n_24 >= ROTACION_MAX_DIA:
        raise SystemExit(f"--rotar-tanda: ya hay {n_24} rotaciones en 24 h (máx. {ROTACION_MAX_DIA}): no se rota")
    ev = {"tipo": "suelo_reiniciado", "wallet": wallet, "origen": "rotar_tanda",
          "motivo": f"rotación automática de tanda: saldo {sv[0]:.4f}, suelo {suelo:.4f} agotado; Javi 20-Oct (opción 2), suelo duro {ROTACION_SALDO_DURO}",
          "suelos_descartados": previos, "saldo_base": sv[0], "bloque": sv[1], "rotacion_n_24h": n_24 + 1,
          "ilegibles_aceptadas": sorted(r["aceptadas"])}     # NUNCA acepta defectos nuevos: eso lo ve un humano
    X.log(dict(ev, real=True))
    _fsync_ledger()
    time.sleep(0.01)
    return ev


def aceptar_linea_ilegible(wallet, motivo, leer=input, cli=None):
    """3ª /code-review #4 + 4ª M1: acepta (por fichero + sha, auditado, fsync) las líneas ilegibles ACTUALES de los ledgers reales SIN descartar
    los suelos válidos (el reseteo completo es otra opción). Exige las mismas precondiciones que el reseteo (kill limpio, nada abierto,
    saldo verificado) y SOLO acepta líneas que parezcan JSON CORTADO por un crash (parece_truncada): si hay alguna ilegible de otro tipo
    (basura, JSON completo pero inválido) no acepta ninguna. Nota: el harness cierra con «\\n» la línea cortada y sigue escribiendo, así que
    la cortada ya no es la última del fichero; por eso el criterio es su forma y no su posición. Guarda la línea cruda (base64) además de
    sha y fichero. Lo que decía se pierde: un suelo_* cortado no llegó a usarse (se escribe ANTES de la orden)."""
    if motivo is None or not str(motivo).strip():
        raise SystemExit("--aceptar-linea-ilegible exige un motivo no vacío")
    sv = comprobar_para_reseteo(wallet, cli, "--aceptar-linea-ilegible")
    r = escanear_ledgers_reales(wallet)
    nuevas = [d for d in r["defectos"] if (d[0], d[1]) not in r["aceptadas"]]
    if not nuevas:
        print("no hay líneas ilegibles sin aceptar")
        return None
    raras = [d for d in nuevas if not d[3]]
    if raras:
        raise SystemExit(f"--aceptar-linea-ilegible: {len(raras)} línea(s) ilegible(s) NO parecen un JSON cortado por un crash "
                         f"(p. ej. {raras[0][0]}: {raras[0][2]!r}): investigar a mano; no se acepta ninguna")
    print(f"wallet {wallet}\nsaldo verificado {sv[0]:.4f} (bloque {sv[1]})\nlíneas cortadas que se aceptarían: {[(d[0], d[2]) for d in nuevas]}\n"
          f"suelos válidos que se CONSERVAN: {[v for _, _, v in r['suelos']]}", flush=True)
    if not _confirmar(leer, f"ACEPTAR LINEA ILEGIBLE {wallet[-6:]}"):
        print("no confirmado: nada cambia")
        return None
    ev = {"tipo": "linea_ilegible_aceptada", "wallet": wallet, "motivo": str(motivo)[:300], "saldo_verificado": sv[0], "bloque": sv[1],
          "ilegibles_aceptadas": sorted({(d[0], d[1]) for d in nuevas}),
          "lineas_crudas": {d[1]: {"fichero": d[0], "base64": base64.b64encode(d[4].encode("utf-8", "replace")).decode()} for d in nuevas}}
    X.log(dict(ev, real=True))
    _fsync_ledger()
    return ev


class Ctx:
    """Un mercado 5m en curso (una moneda)."""

    def __init__(self, coin, mk, lib, k):
        self.coin, self.mk, self.lib, self.k = coin, mk, lib, k
        toks = mk["toks"]
        self.up, self.dn = toks.get("Up") or toks.get("Yes"), toks.get("Down") or toks.get("No")
        self.par = {self.up: self.dn, self.dn: self.up}
        self.lados = {self.up: "YES", self.dn: "NO"}
        self.estado = {t: {"llenas": 0.0, "coste": 0.0, "oid": None, "rellenos": [], "cerrado": False} for t in (self.up, self.dn)}
        self.fase = "previa"
        self.tok = None                 # cara elegida (una sola)
        self.hashes = []
        self.n_ord = 0
        self.t_accion = 0.0
        self.fuera_desde = None
        self.viejo_desde = None
        self.ult_poll = 0.0
        self.ult_poll_can = 0.0
        self.ult_cancel = 0.0
        self.t_cierre = None
        self.motivo_cierre = None
        self.t_inicio = time.time()
        self.libro_dec = None
        self.obj_a = None               # escalón A: objetivo B vigente al colocar
        self.n_a = 0
        self.medido = False
        self.posteado = False
        self.fin_puja = None
        self.sync_n = -1                # longitud del ledger incremental en la última sincronización de rellenos
        self.n_exc = 0                  # excepciones de paso() en este mercado (4ª /code-review #4)


class Exp47(X.Exp):
    def __init__(self, real, escalon="B", n_max=None, t_stop=T_STOP_DEF, size=5, min_nocional=1.0, monedas=("eth", "sol", "xrp"),
                 presupuesto=PRESUPUESTO_UTIL, max_vivas=MAX_VIVAS):
        self.escalon, self.t_stop, self.size, self.min_nocional = escalon, float(t_stop), size, float(min_nocional)
        self.monedas, self.presupuesto, self.max_vivas = tuple(monedas), float(presupuesto), int(max_vivas)
        self.saldo_min = None               # SUELO (pUSD): None = sin fijar -> no se envía nada (fail-closed); lo fija fijar_suelo() en real
        self.saldo_verificado = None
        self.bloque_saldo = None            # número de bloque de la lectura de arranque
        self.hwm = None                     # máximo de saldo verificado (pico): el suelo es >= hwm − presupuesto
        self._alza_pend = None              # (saldo, hora) de un alza sobre el máximo aún sin confirmar
        self._suelo_escrito = False         # el `suelo_fijado` se escribe (fsync) al enviar la 1ª orden real, no al arrancar
        self.suelos_previos_log = []
        self._esc, self._esc_error = None, None     # UN solo escaneo de los ledgers reales por arranque (3ª /code-review #9)
        self._bloque_visto = None           # 3ª /code-review #5: último bloque aceptado en una lectura de saldo (monotonía)
        self._bloque_lectura = None         # bloque de la última lectura válida (para confirmar un alza con una lectura MÁS NUEVA)
        self.n_max = int(n_max if n_max is not None else N_MAX[escalon])
        if escalon not in N_MAX or self.n_max > N_MAX[escalon] or self.n_max < 1:
            sys.exit(f"--n debe estar en 1..{N_MAX.get(escalon)} para el escalón {escalon}")
        if not (0 < self.presupuesto < math.inf) or (real and self.presupuesto > PRESUPUESTO_UTIL + 1e-9):
            sys.exit(f"--presupuesto-util debe estar en (0, {PRESUPUESTO_UTIL}] (en real no puede superar {PRESUPUESTO_UTIL}; finito)")
        if real and self.max_vivas > MAX_VIVAS:
            sys.exit(f"--max-vivas <= {MAX_VIVAS}")
        if size < SIZE_MIN or size > SIZE_MAX:
            sys.exit(f"--size entre {SIZE_MIN} y {SIZE_MAX}")
        if real and ASENTAR_H47_S < ASENTAR_MIN_REAL_S - 1e-9:
            sys.exit(f"ASENTAR_H47_S {ASENTAR_H47_S} < {ASENTAR_MIN_REAL_S} s: no se envía en real")
        X.T_STOP = self.t_stop              # X.Exp.post() usa la constante del módulo para su re-chequeo tras firmar
        X.ASENTAR_S = ASENTAR_H47_S         # liquidar()/cerrar_salida() del harness leen la constante del módulo X
        self.ctxs = {}
        self.gem, self.gem_lleno = {}, {}   # gemelo CONS de cada orden REAL (en seco los rellenos simulados son los reales de mentira)
        self.slugs_usados = set()
        self.parada = None
        self.n_ordenes_total = 0            # se reconstruye del ledger al final de __init__
        self.saldo_ilegible_desde = None
        self.saldo_bajo_desde = None
        self.ult_cuadre = 0.0
        self._visto_log = set()
        self._inc, self._inc_n, self._ev_oid = {}, 0, {}      # contabilidad incremental (ver ordenes())
        self._ult_verif = 0.0
        self.rechazos_seguidos = 0
        self.cancel_all_hecho = False
        self._gamma_err = {}
        self.enfriar_tok = {}               # 1ª /code-review #5: enfriamiento por TOKEN (el harness lo guarda por lado YES/NO, común a todos los mercados)
        super().__init__(real)
        for e in X.leer_ledger():
            if e.get("tipo") == "intencion_post" and bool(e.get("real")) == bool(real) and e.get("slug"):
                self.slugs_usados.add(e["slug"])
        # 1ª /code-review #6: el tope TOTAL de órdenes se reconstruye del ledger (y de los demás escalones reales: misma wallet) para que
        # un reinicio no lo ponga a 0; el tope por puja se hace cumplir al no reentrar en un mercado ya operado (ver crear_ctx).
        # (en seco no hay wallet que proteger: el ledger seco acumula de ensayo en ensayo y el tope se aplica por proceso)
        # 3ª /code-review #9/#10: el escaneo único alimenta tope total, base del cuadre y suelos; si no se puede leer un ledger la cuenta
        # NO es fiable: el tope se da por agotado (no se envía) y fijar_suelo() deja saldo_min=None registrado.
        esc = self._escaneo() if real else None
        if not real:
            self.n_ordenes_total = 0
        elif esc is None:
            self.n_ordenes_total = MAX_ORDENES_TOTAL
        else:
            self.n_ordenes_total = contar_intenciones(X.leer_ledger(), True)[0] + esc["intenciones_otros"]
        if real:
            self.fijar_suelo()
        else:
            self.saldo_min = 0.0            # en seco no hay dinero ni suelo

    # ---------------------------------------------------------------- suelo dinámico
    def _escaneo(self):
        """Escaneo único (cacheado) de los ledgers reales; None si un ledger no se puede leer (motivo en self._esc_error)."""
        if self._esc is None and self._esc_error is None:
            try:
                self._esc = escanear_ledgers_reales(self.funder)
            except LedgerIlegible as e:
                self._esc_error = str(e)
        return self._esc

    def leer_saldo_verificado(self):
        """pUSD on-chain de la dedicada VERIFICADO (2ª /code-review #4/#6): dos lecturas seguidas fijadas a un bloque reciente y monótono que
        coinciden en <= SALDO_TOL_VERIF (hasta SALDO_REINTENTOS rondas). Devuelve la ÚLTIMA lectura (no el máximo: el ruido no infla el suelo)
        y guarda su bloque en self.bloque_saldo. None si no se puede verificar."""
        r = saldo_verificado_wallet(self.funder)
        if r is None:
            return None
        self.bloque_saldo = self._bloque_visto = r[1]
        return r[0]

    def _no_fijado(self, motivo):
        self.saldo_min = None
        self._log47({"tipo": "suelo_no_fijado", "motivo": motivo})
        print(f"AVISO: suelo NO fijado, no se opera: {motivo}", file=sys.stderr, flush=True)

    def fijar_suelo(self):
        """Opción (b) de Javi: SUELO = saldo verificado en el arranque − presupuesto útil (5 USD). Sin saldo verificable, saldo de arranque
        < presupuesto + 1 USD o ledger de suelos ilegible -> saldo_min queda en None y puede_enviar() NO envía (run() para). El suelo no baja
        respecto al ya fijado en esta wallet (ver cabecera). Aquí SOLO se calcula (memoria); el `suelo_fijado` durable se escribe al enviar
        la primera orden real (_post_real), así un arranque que sale enseguida no sube nada (2ª /code-review #5)."""
        esc = self._escaneo()
        if esc is None:
            return self._no_fijado(self._esc_error or "ledgers reales sin escanear: no hay suelo fiable")
        try:
            previos = suelos_previos(self.funder, esc)
        except LedgerIlegible as e:
            return self._no_fijado(str(e))
        s = self.leer_saldo_verificado()
        if s is None:
            return self._no_fijado("saldo on-chain no verificable en el arranque (bloque no reciente/no creciente, lecturas que no coinciden o RPC caído)")
        if s < self.presupuesto + SALDO_ARRANQUE_MARGEN - 1e-9:
            return self._no_fijado(f"saldo de arranque {s:.4f} < presupuesto {self.presupuesto} + margen {SALDO_ARRANQUE_MARGEN}: no se opera")
        nuevo = s - self.presupuesto
        mx = max(previos) if previos else None
        # un saldo que supera el máximo previo en <= tolerancia es ruido (sin acumulación entre reinicios)
        suelo = mx if (mx is not None and nuevo <= mx + SALDO_TOL_VERIF + 1e-9) else nuevo
        self.saldo_verificado, self.hwm, self.saldo_min = s, s, suelo
        self.suelos_previos_log = [round(v, 6) for v in previos]
        self._log47({"tipo": "suelo_calculado", "wallet": self.funder, "saldo": round(s, 6), "bloque": self.bloque_saldo,
                     "presupuesto": self.presupuesto, "suelo": round(suelo, 6), "suelo_sin_historial": round(nuevo, 6),
                     "suelos_previos": self.suelos_previos_log})

    def _escribir_suelo(self, tipo, hwm=None, suelo=None, bloque=None):
        """`suelo_fijado`/`suelo_subido` DURABLE (fsync, como intencion_post/kill). Lanza si no llega a disco. hwm/suelo: valores a escribir
        (por defecto los vigentes); no modifica el estado en memoria."""
        hwm = self.hwm if hwm is None else hwm
        suelo = self.saldo_min if suelo is None else suelo
        self._log47({"tipo": tipo, "wallet": self.funder, "saldo": round(hwm, 6), "bloque": self.bloque_saldo if bloque is None else bloque,
                     "presupuesto": self.presupuesto, "suelo": math.ceil(suelo * 1e6) / 1e6,   # nunca redondea hacia abajo
                     "suelos_previos": self.suelos_previos_log})
        _fsync_ledger()
        self._suelo_escrito = True

    def _post_real(self, h, signed, *a, **k):
        """Antes del PRIMER POST real de la ejecución se escribe el suelo (durable). Si no llega a disco: kill y no se envía."""
        if not self._suelo_escrito:
            try:
                self._escribir_suelo("suelo_fijado")
            except Exception as e:
                self.kill = f"no se pudo escribir suelo_fijado antes de la primera orden real: {type(e).__name__}: {str(e)[:120]}"
                return None
        return super()._post_real(h, signed, *a, **k)

    def _alza_saldo(self, on):
        """2ª /code-review #1 + 3ª #7/#8: si el saldo sube sobre el máximo (redención, depósito) el suelo sube con él (suelo >= máximo −
        presupuesto). El alza hay que confirmarla con otra lectura VÁLIDA y de un bloque MÁS NUEVO, >= ALZA_CONFIRMA_S después y antes de
        ALZA_CADUCA_S (si no, caduca y se empieza otra); una lectura ilegible entre medias la anula. Se toma la menor de las dos. Si el
        suelo_subido no llega a disco: kill, False y NADA cambia en memoria. True = se puede seguir; False = no se envía."""
        if on <= self.hwm + SALDO_TOL_VERIF + 1e-9:
            self._alza_pend = None
            return True
        ahora, b = time.time(), self._bloque_lectura
        p = self._alza_pend
        if p is None or ahora - p[1] > ALZA_CADUCA_S:
            self._alza_pend = (on, ahora, b)
            return False
        if ahora - p[1] < ALZA_CONFIRMA_S or b is None or p[2] is None or b <= p[2]:
            return False
        hwm = max(self.hwm, min(p[0], on))
        suelo = max(self.saldo_min, hwm - self.presupuesto)
        if suelo > self.saldo_min + 1e-9 and self._suelo_escrito:
            try:
                self._escribir_suelo("suelo_subido", hwm, suelo, bloque=b)         # bloque de la lectura que CONFIRMÓ el alza
            except Exception as e:
                self._alza_pend = None
                self.kill = f"no se pudo escribir suelo_subido: {type(e).__name__}: {str(e)[:120]}"
                return False
        self._alza_pend = None
        self.hwm, self.saldo_min = hwm, suelo
        return True

    def pujas_en_libro(self):
        """Slugs con alguna orden en el libro o con la cancelación sin confirmar (vivas + canceladas), más las pujas activas con orden
        propia pendiente de reponer: 1ª /code-review #8 (antes solo contaba fase 'activa' y podía haber hasta el doble de órdenes)."""
        slugs = {o.get("slug") for o in list(self.vivas.values()) + list(self.canceladas.values())}
        slugs |= {x.mk["slug"] for x in self.ctxs.values() if isinstance(x, Ctx) and x.posteado and x.fase in ("activa", "asentando")
                  and x.tok is not None and not x.estado[x.tok]["cerrado"]}
        return slugs

    def ordenes(self):
        """{oid: C.Orden} IDÉNTICO a C.plegar(ledger) pero incremental: plegar es independiente por oid, así que solo se re-pliegan los
        eventos de los oids tocados desde la última llamada (con miles de órdenes el plegado completo en cada lectura frenaría el bucle)."""
        led = X.leer_ledger()
        n = len(led)
        if n < self._inc_n:
            self._inc, self._inc_n, self._ev_oid = {}, 0, {}
        if n != self._inc_n:
            tocados = set()
            for e in led[self._inc_n:n]:
                if isinstance(e, dict) and e.get("real") and e.get("oid"):
                    self._ev_oid.setdefault(e["oid"], []).append(e)
                    tocados.add(e["oid"])
            for oid in tocados:
                sub = C.plegar(self._ev_oid[oid])
                if oid in sub:
                    self._inc[oid] = sub[oid]
            self._inc_n = n
        return self._inc

    def _log47(self, ev):
        ev.setdefault("escalon", self.escalon)
        self._log(ev)

    def n_usadas(self):
        return len(self.slugs_usados)

    def comprometido(self):
        return sum(float(o["size"]) * float(o["precio"]) for o in list(self.vivas.values()) + list(self.canceladas.values()))

    def saldo(self):
        """pUSD on-chain de la dedicada con caché de 2 s; None si no se puede leer. En seco no hay dinero: nunca None."""
        if not self.real:
            return 1e9
        ahora = time.time()
        if ahora - self._on_cache[0] < 2.0:
            return self._on_cache[1]
        r = saldo_con_bloque(self.funder)
        ok, motivo = lectura_valida(r, time.time(), self._bloque_visto)
        on = r[0] if ok else None
        if ok:
            self._bloque_lectura = r[1]
            self._bloque_visto = max(self._bloque_visto or 0, r[1])
        else:                               # fail-closed: ni se envía ni se cuadra con una lectura vieja/retrocedida; el alza pendiente se anula
            self._bloque_lectura = None
            self._alza_pend = None
            if r is not None:
                self._log_bloqueo(("lectura_saldo", motivo), {"tipo": "lectura_saldo_rechazada", "motivo": motivo, "bloque": r[1],
                                                               "visto": self._bloque_visto})
        self._on_cache = (ahora, on)
        return on

    def cuadre(self, on):
        """DINERO QUE NO CUADRA: salieron de la wallet más pUSD de los que el ledger puede explicar -> kill. True si cuadra. Misma condición que
        X.Exp.capital_fuera (1ª /code-review #9: test_cuadre_igual_que_capital_fuera_del_harness las compara con varios saldos)."""
        if not self.real or on is None:
            return True
        ords = self.ordenes()
        if self.t_reinicio is not None:             # tras un reseteo auditado la base es el saldo de ese momento: solo explican las órdenes posteriores
            ords = {k: o for k, o in ords.items() if o.t_int > self.t_reinicio}
        explicable = C.exposicion_maxima(ords)
        if self.saldo_inicial - on > explicable + C.TOLERANCIA_SALDO:
            self._log47({"tipo": "dinero_no_cuadra", "saldo_inicial": self.saldo_inicial, "onchain": on, "explicable": round(explicable, 4)})
            self.kill = self.kill or (f"dinero que no cuadra: salieron {self.saldo_inicial - on:.4f} pUSD y el ledger solo explica "
                                      f"{explicable:.4f}")
            return False
        return True

    def puede_enviar(self, coste):
        """Compuerta ANTES de cada POST real: suelo fijado, saldo legible, cuadre, tope por orden y suelo (saldo − comprometido − coste >=
        saldo_min, el SUELO dinámico)."""
        if not self.real:
            return True
        if coste > COSTE_MAX_ORDEN + 1e-9:
            self._bloqueo(("coste", coste), {"tipo": "bloqueo_coste_orden", "coste": round(coste, 4)})
            return False
        if self.saldo_min is None or not (self.saldo_min >= 0):          # `is None`/finito: nunca se evalúa «if saldo_min» (0.0 es falsy)
            self._bloqueo(("suelo_no_fijado",), {"tipo": "bloqueo_suelo_no_fijado"})
            return False
        on = self.saldo()
        if on is None:
            self._bloqueo(("saldo_ilegible",), {"tipo": "bloqueo_saldo_ilegible"})
            return False
        if not self.cuadre(on):
            return False
        if not self._alza_saldo(on):
            self._bloqueo(("alza",), {"tipo": "bloqueo_alza_saldo_sin_confirmar", "saldo": round(on, 4), "maximo": round(self.hwm, 4)})
            return False
        self._bloqueo_prev.pop(("alza",), None)
        disp = min(on, self.hwm) - self.comprometido() - coste      # 3ª #7: nunca se gasta el exceso sobre el pico confirmado
        if disp < self.saldo_min - 1e-9:
            self._bloqueo(("suelo",), {"tipo": "bloqueo_suelo_saldo", "saldo": round(on, 4), "comprometido": round(self.comprometido(), 4),
                                        "coste": round(coste, 4), "minimo": self.saldo_min})
            return False
        self._bloqueo_prev.pop(("suelo",), None)
        self._bloqueo_prev.pop(("saldo_ilegible",), None)
        return True

    def _bloqueo(self, clave, ev):
        self._log_bloqueo(clave, ev)

    # ---------------------------------------------------------------- órdenes: medición de latencias y gemelo CONS
    def post(self, slug, tok, lado, precio, size, cola, lib=None, ajeno_dec=None, ask_dec=None, fin=None):
        t0 = time.time()
        n_ev = len(X.leer_ledger())
        prev_enf = dict(self.enfriar)
        h = super().post(slug, tok, lado, precio, size, cola, lib=lib, ajeno_dec=ajeno_dec, ask_dec=ask_dec, fin=fin)
        # 1ª /code-review #5: el harness enfría por LADO ('YES'/'NO') -> un 4xx en ETH YES bloqueaba 10 s los YES de SOL/XRP. Se traslada a
        # una clave por TOKEN (exclusiva de este mercado) y se restaura el valor anterior del lado.
        if self.enfriar.get(lado, 0) != prev_enf.get(lado, 0):
            self.enfriar_tok[tok] = max(self.enfriar_tok.get(tok, 0), self.enfriar[lado])
            if lado in prev_enf:
                self.enfriar[lado] = prev_enf[lado]
            else:
                self.enfriar.pop(lado, None)
        # 1ª /code-review #6: cada intención (aunque el POST se corte o lo rechacen) cuenta en el tope total
        self.n_ordenes_total += contar_intenciones(X.leer_ledger()[n_ev:], self.real)[0]
        if h is None and any(e.get("tipo") == "post_rechazada" and e.get("real") for e in X.leer_ledger()[n_ev:]):
            self.rechazos_seguidos += 1                  # 4xx limpio: el exchange no aceptó la orden (p. ej. nocional < 1 $)
            if self.rechazos_seguidos >= 5 and not self.parada:
                self.parar(f"{self.rechazos_seguidos} rechazos 4xx seguidos del exchange (último a {precio} x {size}): ver post_rechazada en el ledger")
        elif h is not None:
            self.rechazos_seguidos = 0
        if h is not None:
            t1 = time.time()
            self._log47({"tipo": "post_lat", "oid": h, "t_call0": t0, "t_ret": t1, "ms": round((t1 - t0) * 1000, 1),
                                "t_post_gemelo": float(self.vivas.get(h, {}).get("t_post") or t1)})
            if self.real:
                # 1ª /code-review #3: el gemelo CONS cuenta operaciones desde t_post + LAT_POST_S, y t_post es el de la RESPUESTA del POST
                # (el mismo que usa el harness en vivas[h]), NO t0 (antes de firmar + neg_risk + POST: 150-400 ms en que la orden aún no
                # estaba en el libro y que sobrepredecían el relleno). t_call0 se guarda solo para análisis.
                t_post = float(self.vivas.get(h, {}).get("t_post") or t1)
                self.gem[h] = {"tok": tok, "precio": precio, "size": size, "t_post": t_post, "t_call0": t0, "cola": cola, "vol_sim": 0.0,
                               "slug": slug}
        return h

    def cancelar(self, h):
        t0 = time.time()
        r = super().cancelar(h)
        t1 = time.time()
        g = self.gem.get(h)
        if g is not None and g.get("t_cancel") is None:
            g["t_cancel"] = t0
        self._log47({"tipo": "cancel_lat", "oid": h, "ok": bool(r), "ms": round((t1 - t0) * 1000, 1)})
        return r

    def simular(self, c):
        """Rellenos CONS de las órdenes de ESTE mercado: en seco son los rellenos (simulados) que lee `consultar`; en real son el gemelo."""
        if self.real:
            for h, g in list(self.gem.items()):
                if g["tok"] not in c.estado:
                    continue
                f0 = self.gem_lleno.get(h, 0.0)
                f = sim_uno(c.lib, c.par, g, f0)
                if f > f0 + 1e-9:
                    self.gem_lleno[h] = f
                    self._log47({"tipo": "gemelo_relleno", "oid": h, "acc_total": f, "precio": g["precio"]})
            return
        for h, o in list(self.vivas.items()) + list(self.canceladas.items()):
            if not str(h).startswith("seco-") or o["tok"] not in c.estado:
                continue
            f0 = self.sim_lleno.get(h, 0.0)
            f = sim_uno(c.lib, c.par, o, f0)
            if f > f0 + 1e-9:
                self.sim_lleno[h] = f
                self._log47({"tipo": "relleno_simulado", "oid": h, "acc_total": f, "precio": o["precio"], "real": False})

    # ---------------------------------------------------------------- ciclo de un mercado
    def crear_ctx(self, coin, mk):
        toks = mk["toks"]
        up, dn = toks.get("Up") or toks.get("Yes"), toks.get("Down") or toks.get("No")
        if not up or not dn:
            self._log47({"tipo": "mercado_sin_tokens", "mk": mk})
            return None
        if mk["slug"] in self.slugs_usados:
            # 1ª /code-review #6: reinicio a mitad de una puja. Reentrar la dejaría con n_ord=0 y sin saber si ya se rellenó (rompe «un relleno
            # cierra la puja» y el tope por puja): NO se reentra; N ya la cuenta. Queda registrada como interrumpida (sin puja_fin).
            self._log47({"tipo": "mercado_ya_operado_no_reentra", "slug": mk["slug"],
                         "n_ordenes_previas": contar_intenciones(X.leer_ledger(), self.real)[1].get(mk["slug"], 0)})
            return None
        try:
            lib = X.Libro([up, dn], registrar_trades=True)
        except Exception as ex:
            self._log47({"tipo": "ws_no_conecta_salto", "slug": mk["slug"], "e": str(ex)[:160]})
            return None
        c = Ctx(coin, mk, lib, K_POR_MONEDA[coin])
        if self.real:
            try:
                ticks = {str(self.cli.get_tick_size(t)) for t in (up, dn)}
            except Exception as ex:
                ticks = {f"error {ex}"}
            if ticks != {"0.01"}:
                self._log47({"tipo": "tick_no_001_salto", "slug": mk["slug"], "ticks": sorted(ticks)})
                lib.parar = True
                return None
        return c

    def cerrar_ctx(self, c, motivo):
        c.motivo_cierre, c.fase, c.t_cierre = motivo, "asentando", time.time()
        self._log47({"tipo": "cierre_mercado", "slug": c.mk["slug"], "motivo": motivo, "T": round(c.mk["fin"] - time.time(), 1)})

    def paso(self, c):
        ahora = time.time()
        T = c.mk["fin"] - ahora
        if c.fase == "previa":
            if self.kill or self.senal or self.parada or self.n_usadas() >= self.n_max:
                self.cerrar_ctx(c, "sin_puja_previa")           # mercado aún no abierto: nada que cancelar
                return
            if T > T_INI:
                return
            c.fase = "activa"
            self._log47({"tipo": "mercado_inicio", "slug": c.mk["slug"], "id": c.mk["id"], "coin": c.coin, "k": c.k, "real": self.real})
        if c.fase == "activa":
            motivo = None
            if self.kill:
                motivo = "kill"
            elif self.senal:
                motivo = "senal"
            elif T <= self.t_stop:
                motivo = "t_stop"
            elif c.tok is None and c.mk["slug"] not in self.slugs_usados and (self.parada or self.n_usadas() >= self.n_max):
                motivo = "sin_puja_n_o_parada"
            elif c.lib.tick_cambiado:
                motivo = "tick_cambiado"
            elif not c.lib.fresco():
                c.viejo_desde = c.viejo_desde or ahora
                if ahora - c.viejo_desde > X.WS_MAX_S:
                    motivo = "ws_viejo"
                else:
                    return
            else:
                c.viejo_desde = None
            if motivo:
                self.cerrar_ctx(c, motivo)
                return
            c.medido = True
            self.simular(c)
            if ahora - c.ult_poll >= POLL_S:
                c.ult_poll = ahora
                self.liquidar_todo(c.estado, c.lib, T)
                if ahora - self._ult_verif >= 1.0:              # una pasada por segundo para TODOS los mercados
                    self._ult_verif = ahora
                    self.verificar(limite=3)
            elif ahora - c.ult_poll_can >= 0.15:                # canceladas pendientes de asentar: relectura rápida (repegado)
                c.ult_poll_can = ahora
                for h, o in list(self.canceladas.items()):          # una sola relectura, justo al cumplirse ASENTAR_S (no martillear la API)
                    if o["tok"] in c.estado and ahora - float(o.get("t_cancel") or 0.0) >= X.ASENTAR_S:
                        self.liquidar(h, o, True, c.estado, c.lib, T)
            self.decidir(c, T, ahora)
        elif c.fase == "asentando":
            self.simular(c)
            for h, o in list(self.vivas.items()):
                if o["tok"] in c.estado and ahora - c.ult_cancel >= 2.0:       # sin martillear la API si no se confirma
                    c.ult_cancel = ahora
                    self.cancelar(h)
                    if h in self.canceladas:
                        self.liquidar(h, self.canceladas[h], True, c.estado, c.lib, T)
            self.liquidar_todo(c.estado, c.lib, T)
            pend = [h for h, o in list(self.vivas.items()) + list(self.canceladas.items()) if o["tok"] in c.estado]
            if not pend:
                c.fase = "espera_fin"
            elif ahora - c.t_cierre > 60:
                self.kill = self.kill or f"{len(pend)} órdenes de {c.mk['slug']} sin confirmar fuera del libro tras 60 s"
                c.fase = "espera_fin"
        elif c.fase == "espera_fin":
            self.simular(c)
            if ahora >= c.mk["fin"] + FIN_ESPERA_S or self.senal:
                self.finalizar(c)

    def elegir_cara(self, c):
        for tok in (c.up, c.dn):
            b, a = c.lib.top(tok)
            if b is not None and a is not None and en_rejilla(b[0]) and en_banda(b[0], a[0]):
                return tok
        return None

    def sincronizar_rellenos(self, c):
        """1ª /code-review #2: reincorpora a `c.estado` lo que el LEDGER ya sabe del relleno de las órdenes de esta puja (`lo` = mayor
        lectura de get_order, incluidas las de verificar() a ~30 s y las de cerrar_salida): sin esto un relleno visto fuera de
        liquidar() cambiaba la contabilidad pero NO la medición (relleno_real=False, puja sin cerrar, se repuja) y sesgaba H47 hacia
        «el simulador sobrepredice». Solo get_order sube `lo` (/trades puede duplicar filas: no se usa para sumar). Devuelve las
        acciones tardías incorporadas."""
        if not self.real or c.tok is None or not c.hashes:
            return 0.0
        ords = self.ordenes()
        if self._inc_n == c.sync_n:
            return 0.0
        c.sync_n = self._inc_n
        e, extra = c.estado[c.tok], 0.0
        prev_por_oid = {}
        for r in e["rellenos"]:
            prev_por_oid[r["oid"]] = prev_por_oid.get(r["oid"], 0.0) + r["acc"]
        for h in c.hashes:
            o = ords.get(h)
            if o is None or o.alias:
                continue
            dif = o.lo - prev_por_oid.get(h, 0.0)
            if dif > 1e-9:
                t = time.time()
                e["llenas"] += dif
                e["coste"] += dif * o.precio
                e["rellenos"].append({"oid": h, "acc": dif, "precio": o.precio, "t_deteccion": t, "espera_s": None, "cola": None,
                                      "mid0": c.lib.mid_en(o.tok, t), "tras_cancel": True, "tardio": True})
                self._log47({"tipo": "relleno_tardio", "oid": h, "acc": dif, "precio": o.precio, "slug": c.mk["slug"]})
                extra += dif
        return extra

    def decidir(self, c, T, ahora):
        lib = c.lib
        self.sincronizar_rellenos(c)
        tok = c.tok or self.elegir_cara(c)
        if tok is None:
            return
        e = c.estado[tok]
        o = self.vivas.get(e["oid"]) if e["oid"] else None
        if e["cerrado"] or e["llenas"] > 1e-9:
            e["cerrado"] = True
            c.fin_puja = c.fin_puja or "relleno"
            if o is not None:
                h = e["oid"]
                if self.cancelar(h):
                    self.liquidar(h, o, True, c.estado, lib, T)
                    e["oid"] = None
            return
        b, a = lib.top(tok)
        valido = b is not None and a is not None and b[0] < a[0] and en_rejilla(b[0])
        objetivo = objetivo_h35(b[0], a[0], c.k) if valido and en_banda(b[0], a[0]) else None
        if o is not None:
            resto = float(o["size"]) - sum(r["acc"] for r in e["rellenos"] if r["oid"] == e["oid"])
            if not o.get("visto"):
                # 1ª /code-review #10: dos criterios, con el motivo registrado. «nivel»: el WS muestra cola + nuestro resto (el nivel puede
                # no sumarlo si la cola delantera se consume: por eso también hay plazo). «plazo»: POST + VISTO_MAX_S, TAMBIÉN en seco
                # (antes en seco 'visto' podía no registrarse nunca y la métrica de visibilidad quedaba sesgada).
                nivel_ok = lib.tamano_nivel(tok, o["precio"]) >= (o.get("cola") or 0.0) + max(0.0, resto) - 1e-9
                plazo_ok = ahora - float(o.get("t_post") or 0.0) >= X.VISTO_MAX_S
                if nivel_ok or plazo_ok:
                    o["visto"] = True
                    self._log47({"tipo": "visto", "oid": e["oid"], "t": ahora, "espera_s": round(ahora - float(o["t_post"]), 3),
                                 "criterio": "nivel" if nivel_ok else "plazo", "simulado": not self.real})
            if not valido:
                c.fuera_desde = c.fuera_desde or ahora
                if ahora - c.fuera_desde >= REQUOTE_INVALIDO_S:
                    h = e["oid"]
                    if self.cancelar(h):
                        self.liquidar(h, o, True, c.estado, lib, T)
                        self._log47({"tipo": "cancel_libro_invalido", "slug": c.mk["slug"]})
                        e["oid"], c.fuera_desde = None, None
                return
            c.fuera_desde = None
            if ahora - c.t_accion < MIN_ENTRE_ACCIONES_S:
                return
            if self.escalon == "A":
                mover = objetivo is None or objetivo != c.obj_a                     # mismo cadencia que el repegado de la regla B
            else:
                mover = objetivo is None or abs(objetivo - float(o["precio"])) > 1e-9
            if not mover:
                return
            h = e["oid"]
            if self.cancelar(h):
                c.t_accion = time.time()
                self.liquidar(h, o, True, c.estado, lib, T)                           # relleno previo a la cancelación, AHORA
                self._log47({"tipo": "repega" if objetivo is not None else "cancela_banda", "slug": c.mk["slug"], "de": o["precio"],
                             "objetivo": objetivo, "bid": b[0] if b else None, "ask": a[0] if a else None, "T": round(T, 1)})
                e["oid"] = None
                if e["llenas"] > 1e-9:
                    e["cerrado"] = True
            return
        # ---- sin orden viva: ¿colocar?
        if objetivo is None or self.parada or self.kill or self.senal:
            return
        if any(x["tok"] == tok for x in self.canceladas.values()):
            return                                                                    # cancelada sin asentar: no se repone todavía
        if time.time() < self.enfriar_tok.get(tok, 0) or ahora - c.t_accion < MIN_ENTRE_ACCIONES_S:
            return
        if c.mk["slug"] not in self.slugs_usados:                                     # primera puja de este mercado
            if self.n_usadas() >= self.n_max:
                return                                                                # N alcanzado
            if len(self.pujas_en_libro() - {c.mk["slug"]}) >= self.max_vivas:
                return
        if len(self.vivas) + len(self.canceladas) >= self.max_vivas:
            return                                                                    # 1ª /code-review #8: nunca > max_vivas órdenes reales a la vez (vivas + cancelación sin confirmar)
        if c.n_ord >= MAX_ORDENES_PUJA or self.n_ordenes_total >= MAX_ORDENES_TOTAL:
            c.fin_puja = c.fin_puja or "tope_ordenes"
            e["cerrado"] = True
            if self.n_ordenes_total >= MAX_ORDENES_TOTAL and not self.parada:
                self.parar(f"tope total de órdenes alcanzado ({self.n_ordenes_total} >= {MAX_ORDENES_TOTAL})")
            return
        if self.escalon == "A":
            precio = precio_a(c.n_a)
            if b[0] < precio + 0.05:
                return                                                                # el escalón A no debe poder rellenarse
        else:
            precio = objetivo
        size = tamano_orden(precio, self.size, self.min_nocional if self.escalon == "B" else 0.0)
        if size is None:
            self._bloqueo(("tam", precio), {"tipo": "bloqueo_tamano", "precio": precio})
            return
        mn = c.mk.get("min_size")
        if mn is not None and size < float(mn) - 1e-9:
            self._bloqueo(("minsize",), {"tipo": "bloqueo_min_size_mercado", "min": mn, "size": size})
            return
        if not self.puede_enviar(size * precio):
            return
        if c.mk["fin"] - time.time() <= self.t_stop + 2 or lib.tick_cambiado:
            return
        cola_dec = lib.tamano_nivel(tok, precio)
        lado = c.lados[tok]
        libro_dec = self._libro5(lib, tok)
        # la intención (ledger, fsync) la escribe X.Exp.post: N cuenta el mercado si hay intención aunque el POST se corte o lo rechacen
        ajeno = lib.mejor_bid_ajeno(tok)
        n_ev = len(X.leer_ledger())
        h = self.post(c.mk["slug"], tok, lado, precio, size, cola_dec, lib=lib, ajeno_dec=ajeno, ask_dec=a[0], fin=c.mk["fin"])
        c.t_accion = time.time()
        if h is not None or any(ev.get("tipo") == "intencion_post" and ev.get("slug") == c.mk["slug"] for ev in X.leer_ledger()[n_ev:]):
            self.slugs_usados.add(c.mk["slug"])
            c.tok = c.tok or tok
        if h is None:
            return
        e["oid"] = h
        c.hashes.append(h)
        c.n_ord += 1
        c.n_a += 1
        c.posteado = True
        c.obj_a = objetivo
        if c.libro_dec is None:
            c.libro_dec = libro_dec
        self._log47({"tipo": "puja_post", "oid": h, "slug": c.mk["slug"], "coin": c.coin, "lado": lado, "k": c.k, "precio": precio, "size": size,
                     "objetivo_h35": objetivo, "cola": cola_dec, "libro": libro_dec, "T": round(T, 2), "n_orden": c.n_ord,
                     "variante": "H35b" if self.t_stop >= 90 else "H35", "t_dec": ahora})

    def _libro5(self, lib, tok):
        with lib.lk:
            L = lib.L[tok]
            bids = sorted(((p, s) for p, s in L["bids"].items() if s > 0), reverse=True)[:5]
            asks = sorted((p, s) for p, s in L["asks"].items() if s > 0)[:3]
        return {"bids": bids, "asks": asks}

    # ---------------------------------------------------------------- fin de mercado
    def finalizar(self, c):
        lib, fin = c.lib, c.mk["fin"]
        trades, acc_trades = {}, {}
        if self.real:
            try:
                self.verificar(limite=80)       # 1ª /code-review #2: lo que ya salió del libro hace >= 30 s se lee ANTES de resumir
            except Exception as ex:
                self._log47({"tipo": "verificar_error_en_fin", "slug": c.mk["slug"], "e": f"{type(ex).__name__}: {str(ex)[:160]}"})
            self.sincronizar_rellenos(c)
            tok_de = {str(o.oid).lower(): o.tok for o in self.ordenes().values() if o.slug == c.mk["slug"] and o.tok in (c.up, c.dn)}
            try:
                from py_clob_client_v2.clob_types import TradeParams
                tr = self.cli.get_trades(TradeParams(after=int(c.t_inicio) - 2)) or []
            except Exception as ex:
                tr = None
                trades = {"error": str(ex)[:160]}
            if tr is not None:
                rell, malos = self.anomalias_trades(c.t_inicio - 60, slug=c.mk["slug"], tr=tr)
                if malos:
                    trades["ilegibles"] = sorted(malos)
                for r in rell:
                    tok = tok_de.get(r["oid"])
                    if tok is not None:
                        trades.setdefault(c.lados[tok], []).append({k: r.get(k) for k in ("id", "match_time", "status", "rol", "acc", "price", "side")})
                        acc_trades[r["oid"]] = acc_trades.get(r["oid"], 0.0) + float(r.get("acc") or 0.0)
        for tok, e in c.estado.items():
            for r in e["rellenos"]:
                t0 = r["t_deteccion"]
                mk_ = {}
                for s in MARK_S:
                    m = lib.mid_en(tok, t0 + s) if (t0 + s <= fin and not r.get("tardio")) else None   # después del cierre o relleno tardío = missing, nunca 0
                    mk_[f"mid_{s}s"] = m
                    mk_[f"markout_{s}s"] = (m - r["precio"]) / r["precio"] if m is not None else None
                r.update(mk_)
        ords = self.ordenes() if self.real else {}
        resumen = None
        if c.tok is not None:
            e = c.estado[c.tok]
            f_gem = [self.gem_lleno.get(h, 0.0) for h in c.hashes] if self.real else [self.sim_lleno.get(h, 0.0) for h in c.hashes]
            lo_hi = {h: [round(ords[h].lo, 4), round(ords[h].hi, 4)] for h in c.hashes if h in ords}
            # /trades solo como contraste: si ve más relleno que las lecturas de get_order, se marca (no se suma a la contabilidad)
            mas_trades = sorted(h for h in c.hashes if h in ords and acc_trades.get(str(h).lower(), 0.0) > ords[h].lo + 1e-6)
            sin_verificar = sorted(h for h in c.hashes if h in ords and ords[h].abierta and not ords[h].alias)
            resumen = {"tipo": "puja_fin", "slug": c.mk["slug"], "coin": c.coin, "lado": c.lados[c.tok], "k": c.k, "n_ordenes": len(c.hashes),
                       "llenas_detectadas": e["llenas"],
                       "llenas_en_vuelo": sum(r["acc"] for r in e["rellenos"] if not r.get("tardio")),
                       "rellenos_tardios": sum(1 for r in e["rellenos"] if r.get("tardio")),
                       "coste_detectado": e["coste"], "fin_puja": c.fin_puja or c.motivo_cierre,
                       "relleno_real": bool(e["llenas"] > 1e-9 or mas_trades) if self.real else None,
                       "relleno_solo_trades": mas_trades, "ordenes_sin_verificar": sin_verificar,
                       "relleno_cota_inferior": bool(sin_verificar) if self.real else None,
                       "sim_relleno_cualquiera": bool(any(x > 1e-9 for x in f_gem)), "sim_acciones_max": max(f_gem) if f_gem else 0.0,
                       "rellenos": e["rellenos"], "libro_dec": c.libro_dec, "variante": "H35b" if self.t_stop >= 90 else "H35",
                       "lo_hi_por_orden": lo_hi}
            self._log47(resumen)
        self._log47({"tipo": "mercado_fin", "slug": c.mk["slug"], "coin": c.coin, "motivo": c.motivo_cierre, "medido": c.medido,
                     "posteado": c.posteado, "trades_propios": trades, "kill": self.kill, "senal": self.senal,
                     "ws_malos": getattr(lib, "malos", 0), "ws_ultimo_malo": getattr(lib, "ultimo_malo", None)})
        lib.parar = True
        c.fase = "fin"
        for h in c.hashes:                  # el gemelo y las lecturas de esta puja ya no se necesitan en memoria
            self.gem.pop(h, None)

    # ---------------------------------------------------------------- bucle principal
    def vigilar_saldo(self, ahora):
        """Parada por saldo (único criterio de parada además de kill y N). No cancela nada: deja de colocar y deja morir los mercados."""
        if not self.real or self.parada:
            return
        if self.saldo_min is None:
            self.parar("suelo de saldo sin fijar (saldo de arranque no verificable, insuficiente o ledger ilegible): fail-closed")
            return
        on = self.saldo()
        if on is None:
            self.saldo_ilegible_desde = self.saldo_ilegible_desde or ahora
            if ahora - self.saldo_ilegible_desde > SALDO_ILEGIBLE_MAX_S:
                self.parar("saldo ilegible durante más de 2 min (fail-closed)")
            return
        self.saldo_ilegible_desde = None
        if ahora - self.ult_cuadre >= 5.0:
            self.ult_cuadre = ahora
            self.cuadre(on)
        self._alza_saldo(on)
        if on < self.saldo_min:
            self.saldo_bajo_desde = self.saldo_bajo_desde or ahora
            nada_vivo = not self.vivas and not self.canceladas
            if nada_vivo and ahora - self.saldo_bajo_desde >= ESPERA_SALDO_BAJO_S:
                self.parar(f"saldo {on:.2f} < {self.saldo_min} pUSD sin posiciones por liquidar durante 15 min")
        else:
            self.saldo_bajo_desde = None

    def parar(self, motivo):
        self.parada = motivo
        self._log47({"tipo": "parada", "motivo": motivo})
        print(f"PARADA: {motivo}", flush=True)

    def lanzar_mercados(self, ahora):
        if self.parada or self.kill or self.senal or self.n_usadas() >= self.n_max:
            return
        ini_act = int(ahora // 300 * 300)
        resta = ini_act + 300 - ahora
        for sl in [k for k, v in self.ctxs.items() if not isinstance(v, Ctx)]:       # centinelas de hace > 1 h
            try:
                if int(sl.rsplit("-", 1)[1]) < ahora - 3600:
                    del self.ctxs[sl]
            except (ValueError, IndexError):
                pass
        for sl in [k for k, t in self._gamma_err.items() if t < ahora - 3600]:
            del self._gamma_err[sl]
        for coin in self.monedas:
            for ini in ((ini_act,) if resta > self.t_stop + 30 else ()) + ((ini_act + 300,) if resta <= 30 else ()):
                slug = f"{coin}-updown-5m-{ini}"
                if slug in self.ctxs or ahora < self._gamma_err.get(slug, 0):
                    continue
                try:
                    mk = mercado_5m(coin, ini)
                except Exception as e:
                    self._gamma_err[slug] = ahora + 10
                    self._log47({"tipo": "gamma_error", "slug": slug, "e": str(e)[:160]})
                    continue
                if not mk:
                    self._gamma_err[slug] = ahora + 10
                    continue
                c = self.crear_ctx(coin, mk)
                self.ctxs[slug] = c if c is not None else "saltado"

    def paso_seguro(self, c):
        """paso() con red de seguridad. 1ª /code-review #4: una excepción REPETIDA en la fase 'asentando' (p. ej. un KeyError en sim_uno)
        daba un bucle infinito (~36.000 líneas/h en el ledger real) y el mercado nunca llegaba a fin ni a verificación con el lock de la
        wallet tomado. Ahora: kill en la 1ª; a la 3ª excepción del mercado se ABANDONA (fase 'fin'); el ledger solo guarda las 3 primeras.
        Lo que quede vivo lo cancela cancelar_todo (kill) y cerrar_salida al terminar run(). 1ª /code-review #7: un mercado en 'fin' libera
        su contexto (Libro con todos los trades) y se sustituye por un centinela."""
        try:
            self.paso(c)
        except Exception as ex:                 # un fallo inesperado de código = fallo de maquinaria: kill y salir limpio
            c.n_exc += 1
            self.kill = self.kill or f"excepción en {c.mk['slug']}: {type(ex).__name__}: {str(ex)[:160]}"
            if c.n_exc <= MAX_EXC_CTX:
                self._log47({"tipo": "excepcion", "slug": c.mk["slug"], "n": c.n_exc, "fase": c.fase, "e": f"{type(ex).__name__}: {str(ex)[:300]}"})
            if c.fase in ("previa", "activa"):
                c.fase = "asentando"
                c.t_cierre = c.t_cierre or time.time()
            elif c.n_exc >= MAX_EXC_CTX and c.fase != "fin":
                self._log47({"tipo": "mercado_abandonado", "slug": c.mk["slug"], "fase": c.fase, "excepciones": c.n_exc,
                             "n_ordenes": len(c.hashes), "vivas_sin_cerrar": sorted(h for h in c.hashes if h in self.vivas or h in self.canceladas)})
                c.fase = "fin"
                try:
                    c.lib.parar = True
                except Exception:
                    pass
        if c.fase == "fin":
            self.liberar_ctx(c)

    def liberar_ctx(self, c):
        """Centinela en lugar del contexto terminado: la memoria y los recorridos de self.ctxs no crecen con los mercados pasados."""
        for h in c.hashes:
            self.gem.pop(h, None)
            self.gem_lleno.pop(h, None)
            self.sim_lleno.pop(h, None)
        self.ctxs[c.mk["slug"]] = "terminado"

    def run(self, duracion_max_s=None):
        t_ini = time.time()
        self._log47({"tipo": "config", "real": self.real, "escalon": self.escalon, "n_max": self.n_max, "t_stop": self.t_stop, "size": self.size,
                     "min_nocional": self.min_nocional, "monedas": self.monedas, "k": K_POR_MONEDA, "saldo_min": self.saldo_min,
                     "presupuesto_util": self.presupuesto, "saldo_verificado": self.saldo_verificado, "bloque_saldo": self.bloque_saldo,
                     "max_vivas": self.max_vivas, "codigo_sha": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:16],
                     "robustez_sha": (R.sha_codigo() if R is not None else None),
                     "n_usadas_previas": self.n_usadas(), "saldo_inicial": self.saldo_inicial})
        if self.real:
            on = self.saldo()
            if self.saldo_min is None:
                self.parar("suelo de saldo sin fijar (saldo de arranque no verificable, insuficiente o ledger ilegible): fail-closed")
            elif on is None or on < self.saldo_min + 1.0:
                self.parar(f"saldo de arranque {on} insuficiente (suelo {self.saldo_min:.4f})")
        if R is not None:
            R.instalar(self)                            # atexit (puja_fin parcial sin red) + hilo daemon de huérfanas; fail-safe
        ult_lanzar = 0.0
        while True:
            ahora = time.time()
            if ahora - ult_lanzar >= 1.0:
                ult_lanzar = ahora
                self.vigilar_saldo(ahora)
                self.lanzar_mercados(ahora)
            if duracion_max_s and ahora - t_ini > duracion_max_s and not self.parada:
                self.parar(f"duración máxima del ensayo ({duracion_max_s} s)")
            if self.kill and not self.cancel_all_hecho:
                self.cancel_all_hecho = True
                self.cancelar_todo("kill")
            activos = [c for c in self.ctxs.values() if isinstance(c, Ctx) and c.fase != "fin"]
            for c in activos:
                if R is not None:
                    R.tick(self, c)                     # volcado incremental de mids (nunca lanza)
                self.paso_seguro(c)
            hay_trabajo = bool(activos)
            fin_n = self.n_usadas() >= self.n_max
            if not hay_trabajo and (self.parada or self.kill or self.senal or fin_n):
                break
            time.sleep(LOOP_S)
        for c in self.ctxs.values():
            if isinstance(c, Ctx) and c.fase != "fin":
                c.lib.parar = True
        self.cerrar_salida()
        if self.real:                                   # verificar todo lo cancelado (>= T_VERIF_S) antes de dar la cuenta por cerrada
            limite = time.time() + 20 * 60
            while self.verificar(limite=20) > 0 and time.time() < limite and not self.senal:
                time.sleep(1.0)
        self._log47({"tipo": "fin_ejecucion", "pujas": self.n_usadas(), "ordenes": self.n_ordenes_total, "kill": self.kill, "parada": self.parada,
                     "abiertas_sin_verificar": sum(1 for o in self.ordenes().values() if o.abierta and not o.alias) if self.real else 0})
        print(f"fin: pujas={self.n_usadas()}/{self.n_max} ordenes={self.n_ordenes_total} kill={self.kill} parada={self.parada}", flush=True)


# ---------------------------------------------------------------- rutas, rearme y main
def configurar_rutas(real, escalon, t_stop=T_STOP_DEF):
    """Ledger por escalón (y aparte para H35b, t_stop 90); un único lock y un único .KILL para TODA la wallet real (un kill de A bloquea B).
    El seco nunca los comparte."""
    if t_stop >= 90:
        escalon = f"{escalon}_t90"
    if real:
        X.LEDGER = DATALOGS / f"experimento_h47_{escalon}_ledger.jsonl"
        X.KILL_FICHERO = DATALOGS / "experimento_h47.KILL"
        X.LOCK = DATALOGS / "experimento_h47.lock"
    else:
        X.LEDGER = DATALOGS / f"experimento_h47_seco_{escalon}_ledger.jsonl"
        X.KILL_FICHERO = DATALOGS / "experimento_h47_seco.KILL"
        X.LOCK = DATALOGS / "experimento_h47_seco.lock"
    X._CACHE = None


def tomar_lock_pares():
    """La wallet dedicada también la usa experimento_pares_cola_15m: no se corre H47 real mientras aquel esté activo (cuadre on-chain)."""
    import fcntl
    fd = open(LOCK_PARES, "w")
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        sys.exit("el experimento de pares usa la wallet dedicada (lock): no arranco")
    return fd


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--escalon", choices=("A", "B"), default="B")
    ap.add_argument("--n", type=int, default=None, help="pujas (A <= 40, B <= 500)")
    ap.add_argument("--confirmo-dinero-real", action="store_true")
    ap.add_argument("--t-stop", type=float, default=T_STOP_DEF, choices=(60.0, 90.0), help="60 = H35; 90 = H35b (se registra aparte)")
    ap.add_argument("--size", type=int, default=5)
    ap.add_argument("--min-nocional", type=float, default=1.0)
    ap.add_argument("--monedas", default="eth,sol,xrp")
    ap.add_argument("--presupuesto-util", type=float, default=PRESUPUESTO_UTIL,
                    help="USD gastables: suelo = saldo verificado en el arranque − esto (en real <= 5)")
    ap.add_argument("--max-vivas", type=int, default=MAX_VIVAS)
    ap.add_argument("--duracion-max-min", type=float, default=None, help="ensayo en seco: tope de duración")
    ap.add_argument("--rotar-tanda", action="store_true",
                    help="rotación automática de tanda (vigilante): reinicia el suelo SOLO si la tanda está agotada, saldo >= suelo duro + presupuesto y "
                         "dentro del tope diario; auditado, sin confirmación interactiva (solo real)")
    ap.add_argument("--rearmar-kill", default=None)
    ap.add_argument("--reiniciar-suelo", default=None, metavar="MOTIVO",
                    help="retirada voluntaria de fondos: los suelos previos dejan de contar y la base del cuadre pasa al saldo actual "
                         "(evento auditado + confirmación escrita; solo real)")
    ap.add_argument("--segundo-motivo", default=None, metavar="MOTIVO2",
                    help=f"obligatorio en el reseteo nº {REINICIOS_MAX + 1} y siguientes de la misma wallet (junto a una confirmación reforzada)")
    ap.add_argument("--aceptar-linea-ilegible", default=None, metavar="MOTIVO",
                    help="acepta (por sha, auditado) las líneas ilegibles de los ledgers reales SIN descartar los suelos válidos (solo real)")
    a = ap.parse_args(argv)
    real = a.confirmo_dinero_real
    monedas = tuple(x.strip() for x in a.monedas.split(",") if x.strip())
    if not monedas or any(m not in K_POR_MONEDA for m in monedas):
        sys.exit(f"--monedas: elegir entre {tuple(K_POR_MONEDA)} (BTC/DOGE/BNB fuera de la prueba)")
    configurar_rutas(real, a.escalon, a.t_stop)
    for nombre, val in (("--rearmar-kill", a.rearmar_kill), ("--reiniciar-suelo", a.reiniciar_suelo),
                        ("--aceptar-linea-ilegible", a.aceptar_linea_ilegible)):
        if val is not None and not val.strip():             # 3ª /code-review #1: "" es falsy y arrancaría un real normal
            sys.exit(f"{nombre} exige un motivo no vacío")
    if sum(v is not None for v in (a.rearmar_kill, a.reiniciar_suelo, a.aceptar_linea_ilegible)) > 1:
        sys.exit("--rearmar-kill, --reiniciar-suelo y --aceptar-linea-ilegible son excluyentes")
    if a.rearmar_kill is not None:
        if not real:
            sys.exit("--rearmar-kill solo con --confirmo-dinero-real")
        import fcntl
        fd = open(X.LOCK, "w")
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            sys.exit("otra instancia sigue activa (lock)")
        X._CACHE = None
        k = X.kill_pendiente()
        if not k:
            sys.exit("no hay kill pendiente")
        an = C.anomalias_sin_rearmar(X.leer_ledger())
        print(f"kill que se rearma: {k}" + (f"\nanomalías dadas por vistas: {an}" if an else ""))
        X.log({"tipo": "kill_rearmado", "real": True, "motivo": a.rearmar_kill[:300], "kill": str(k)[:300], "anomalias": an})
        if X.KILL_FICHERO.exists():
            X.KILL_FICHERO.unlink()
        print("kill rearmado; relanzar sin --rearmar-kill")
        return 0
    if a.reiniciar_suelo is not None or a.aceptar_linea_ilegible is not None or a.rotar_tanda:
        if not real:
            sys.exit("--reiniciar-suelo/--aceptar-linea-ilegible/--rotar-tanda solo con --confirmo-dinero-real")
        import fcntl
        _ = tomar_lock_pares()                              # 4ª M B4: MISMO orden que el arranque real (pares primero, luego X.LOCK de Exp)
        fd = open(X.LOCK, "w")
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            sys.exit("otra instancia sigue activa (lock)")
        X._CACHE = None
        wallets = {str(e.get("wallet", "")).lower(): e["wallet"] for e in X.leer_ledger() if e.get("tipo") == "saldo_inicial" and e.get("real")}
        if len(wallets) != 1:
            sys.exit(f"no se puede determinar la wallet dedicada del ledger propio ({len(wallets)} wallets con saldo_inicial): nada que hacer")
        w = next(iter(wallets.values()))
        cli, funder = X.cliente_dedicado()                  # solo para consultar las órdenes abiertas del exchange (M1/M2); no envía nada
        if str(funder).lower() != w.lower():
            sys.exit(f"la wallet del cliente ({funder}) no es la del ledger ({w}): no se hace nada")
        if a.rotar_tanda:
            ev = rotar_tanda(w, cli=cli)
            print("tanda rotada: relanzar sin --rotar-tanda" if ev else "sin cambios")
        elif a.reiniciar_suelo is not None:
            ev = reiniciar_suelo(w, a.reiniciar_suelo, cli=cli, motivo2=a.segundo_motivo)
            print("suelo reiniciado: relanzar sin --reiniciar-suelo" if ev else "sin cambios")
        else:
            ev = aceptar_linea_ilegible(w, a.aceptar_linea_ilegible, cli=cli)
            print("líneas aceptadas: relanzar sin --aceptar-linea-ilegible" if ev else "sin cambios")
        return 0
    if real:
        _ = tomar_lock_pares()
    ex = Exp47(real, a.escalon, a.n, a.t_stop, a.size, a.min_nocional, monedas, a.presupuesto_util, a.max_vivas)
    print(f"{'REAL' if real else 'ENSAYO EN SECO'} H47 escalón {a.escalon}: N={ex.n_max} (ya usadas {ex.n_usadas()}), monedas {monedas}, "
          f"t_stop {a.t_stop}, size {a.size}, min_nocional {a.min_nocional}; kill={ex.kill}; ledger {X.LEDGER}", flush=True)
    if real and ex.kill:
        sys.exit("kill pendiente: revisar y rearmar")
    ex.run(duracion_max_s=a.duracion_max_min * 60 if a.duracion_max_min else None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
