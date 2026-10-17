#!/usr/bin/env python3
"""5m barato H26 -- SIMULADOR DEL MAKER EN LA BANDA BARATA: ¿conseguimos NOSOTROS los rellenos que la población H5M cobra?
SOLO LECTURA / simulación (OK y prioridad de Javi 16-Oct, TODAS LAS MONEDAS: BTC ETH SOL XRP DOGE BNB, cada una con su gate).

Pregunta: la población on-chain (vigía congelado `vigia_5m_barato_maker_forward.py`, H26/H5M-BARATO-MAKER-v1: rellenos maker de
5m que COMPRAN un lado a pc en (0,10, 0,30] con T en (60, 300] s; 7 días 14.307 unidades, EV +0,137 IC90 días (+0,107,+0,155);
final de la cola +0,121; sin BTC +0,122) cobra un EV que nuestras simulaciones previas de cola NO reproducen
(analisis_h5m_cola_simulada.py: ANCLAR −0,20, SEGUIR −0,05, SEGUIR_CABEZA +0,005). Aquí se simula UNA puja nuestra por
(mercado, lado) con el mismo modelo de relleno, contabilidad completa, capas de defensa y calibración contra la población.

DISEÑO FIJADO ANTES DE MIRAR RESULTADOS (16-Oct; cambiarlo = nueva versión + nuevo OOS):
 Universo  Mercados Up/Down 5m de las 6 monedas, días 05-15 Oct del archivo (VOL/m5_registro; VOL/m15_registro para x de Binance
           y los bids de 15m). DESC = 05-09 (única fuente de elección), OOS = 10-15 (juicio único). Unidad = (mercado, lado);
           YES y NO son unidades independientes, nunca un par. Libro cruzado (bid >= ask) = no se cotiza.
 Puja      Una puja de COMPRA por unidad solo mientras el mejor bid del lado esté en (0,10, 0,30] y T en (60, 300] s (T = cierre −
           recepción). Precio de la puja en (0,10, 0,30] y < ask.
           JOIN     al mejor bid; cola delante = tamaño del bid de ese nivel EN EL INSTANTE DE ALTA (última foto q con hora del
                    exchange <= alta); si nuestro nivel ya no es el mejor, se conserva el último tamaño visto.
           IMPROVE  mejor bid + 1 tick (0,01) solo si < ask y <= 0,30 (si no, no se cotiza: sin mezclar con JOIN); cola delante 0
                    salvo que al alta el mejor bid sea ya nuestro nivel (entonces su tamaño).
           Alta efectiva = recepción de la decisión + 68 ms. Recolocación cuando el mejor bid (histórico, sin nosotros) cambia y el
           precio objetivo cambia: cancelación (+60 ms) y alta nueva (+68 ms) en la misma decisión; mientras tanto la orden vieja
           sigue expuesta; sin nueva decisión hasta la alta (bloqueo en vuelo de 68 ms). Tope por unidad = SH acciones (la orden
           nueva pide SH − rellenado). Parada programada a T = 60 s (+60 ms). SH = 5 (mínimo del CLOB); capacidad SH = 25 y 50
           solo para C0 x cola conservadora (se amplía con --sh-cap).
 Relleno   Solo con operaciones (filas t) que ATRAVIESAN o igualan nuestro nivel, con RELOJ DE RECEPCIÓN (17-Oct, chief: el sello c[1]
           del WS del CLOB es de lote, hasta 468 ms antes del casado, y NO se usa; casado modelado = recepción del print − FEED_MS,
           FEED_MS=0 por defecto) dentro de [alta, cancelación efectiva] (la cancelación solo cuenta si llega antes del casado modelado;
           lo mismo para las fotos q de la cola: recepción): ventas tomadoras del token a p <= precio y compras tomadoras del contrario a p' >= 1 − precio
           (acuñación, precio equivalente 1 − p'). Operación a precio equivalente < el nuestro: la barrida vació el nivel -> rellena
           todo lo pendiente (si estamos por encima del mejor bid histórico: solo min(pendiente, tamaño de la operación));
           == al nuestro: suma volumen y rellena lo que supere la cola delante.
           COLA CONSERVADORA (CONS): las cancelaciones de delante NO nos adelantan. COLA OPTIMISTA (OPT, solo JOIN): de cada
           bajada del tamaño del nivel (fotos q) no explicada por operaciones en ese nivel desde la foto anterior, la fracción
           cola_restante/tamaño_previo adelanta (cota; una operación que llegue por otro canal que el libro cuenta como cancelación).
 Defensa   C0 ninguna. C1: cancelar si Binance (filas x del mismo símbolo, hora de RECEPCIÓN c[7]) se mueve EN CONTRA del lado
           (YES: baja, NO: sube) >= u bps respecto al último tick de hace w s (no más viejo que w + 3 s), u en {2, 4} bps, w en
           {1, 5} s; efectiva a +Λ de la RECEPCIÓN de la alarma (Λ = recepción->decisión->cancelación total, parámetro --lambda-ms, 60 por defecto; la rejilla
           30/60/90/120/150/200/300 se lanza cuando H26-MS congele parámetros; u y W también son parámetros --c1-u/--c1-w-ms);
           sin recotizar hasta 2 s después de la última alarma. C2: cancelar si el bid
           del MISMO lado del mercado 15m que contiene al 5m cae >= k ticks (k en {1, 2}) respecto a su máximo de los últimos 3 s;
           mismos +60 ms y 2 s; sin 15m identificable o sin serie = SIN DATO: no se cotiza (a prueba de fallos), contado.
           C1+C2: unión de C1(u,w) y C2 con k = 2 (4 combinaciones). Elección de (u,w,k) solo en DESC.
 Cuentas   Por unidad: nº de órdenes, rellenos parciales, coste, PnL a resolución con desenlace OFICIAL (gamma closed=true con
           fallback /v2/tokens; sin desenlace = missing, nunca 0; cobertura reportada), rebate (20 % de 0,07·p·(1−p) por acción,
           aparte; el EV de titular es SIN rebate), tiempo en libro, capital·s. Mercados no cubiertos de principio a fin por UN
           tramo del registro (el archivo del día es unión de tramos, NO cronológico) quedan marcados `incompleto` y fuera de las
           estadísticas, contados. Ninguna otra fila se descarta.
 Elección  SOLO en DESC (05-09), por moneda y global, entre las pujas SH=5 de cola CONS: máximo EV/€ agrupado con n_rellenas >=
           30 por moneda (>= 150 global). Nº de candidatas (multiplicidad) en el informe. OOS (10-15) = juicio único del elegido.
 Gate (por moneda, OOS, del elegido en DESC; lo que hace falta ANTES de hablar de forward, no un veredicto): n_rellenas >= 40,
           EV/€ >= +0,05, IC90 por días > 0, EV sin el mejor día > 0, >= 4 de los 6 días positivos.
 CALIBRACIÓN (ancla de credibilidad): JOIN+C0 (CONS y OPT) frente a la población on-chain del MISMO universo de mercados y días
           (réplica propia de la regla del vigía, comprobada contra sus cachés): EV, acierto frente a precio, por posición en la cola,
           T, tramo de precio y BTC/ALT, y solapamiento por unidad. Hasta que no se explique la diferencia no se fían las capas.

Reutiliza: desenlaces() de analisis_maker_cancelacion_binance (caché y fallback v2), mapa_tokens, archivo_volumen.VOL, y el modelo de
rellenos de analisis_h5m_cola_simulada / analisis_5m_pares_maker_cola (relleno solo por operación que atraviesa o supera la cola).

Contrato de trabajo largo: run_manifest.json (hash de código, parámetros, entradas, estado por fecha), caché durable ATÓMICA por día
(unidades_D.csv.gz + meta_D.json con hash y recuento; se valida al reanudar y se recalcula si no cuadra), claves únicas
(dia, motor, mkt, lado, tramo), cobertura por día, resumen parcial tras cada fecha, log con hora, informe final
COMPLETE / PARTIAL / FAILED / BLOCKED.

Uso:  nice -n 19 ionice -c3 python3 analisis_5m_maker_banda_simulador.py [--dias D1,D2,..] [--out DIR] [--solo-informe]
      humo: --dias 2026-10-14 --recorte-min 30 --out <dir temporal>  (no escribe cachés si hay recorte)
"""
import argparse
import bisect
import collections
import gzip
import hashlib
import json
import os
import sys
import time
from array import array
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

OUT = Path("/root/polymarket-research-datalogs/m5_maker_banda")
VOL = Path("/mnt/HC_Volume_106538179")
DIAS = [f"2026-10-{d:02d}" for d in range(5, 16)]
DESC, OOS = DIAS[:5], DIAS[5:]
MONEDAS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
SIMBOLO = {"BTC": "BTCUSDT", "ETH": "ETHUSDT", "SOL": "SOLUSDT", "XRP": "XRPUSDT", "DOGE": "DOGEUSDT", "BNB": "BNBUSDT"}
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"

# precios en milésimas (enteros): 0,10 = 100; evita comparar flotantes
P_LO, P_HI, TICK = 100, 300, 10
T_MIN, T_MAX = 60, 300                # s hasta el cierre
LAT_POST_MS, LAT_CANCEL_MS = 68, 60   # F1 15-Oct / 07-Oct medidas
COOL_MS = 2000                        # sin recotizar tras la última alarma
W2_MS = 3000                          # ventana del máximo del bid15 (C2)
STALE_MS = 3000                       # el tick de referencia de Binance no puede ser más viejo que w + STALE
GAP_MS = 10_000                       # silencio del registro > 10 s = hueco (tramo nuevo)
BACK_MS = 60_000                      # salto atrás > 60 s = tramo nuevo (trampa m5_registro no cronológico)
INC_MS = 2000                         # margen de cobertura de tramo
C1_U, C1_W = (2.0, 4.0), (1000, 5000)   # k (bps) y W (ms) de la guarda Binance: PARÁMETROS (--c1-u / --c1-w-ms); sin fijar hasta H26-MS
LAMBDAS = (LAT_CANCEL_MS,)               # Λ total alarma(recepción)->cancelación efectiva; --lambda-ms 30,60,90,120,150,200,300
FEED_MS = 0                              # retraso modelado del feed WS del CLOB: casado modelado = recepción − FEED_MS (--feed-ms)
C2_K = (1, 2)
C12_K = 2
PLC_SHIFT_MS = 1_800_000              # placebo: las alarmas reales desplazadas 30 min (misma densidad, sin relación con la puja)
SH_BASE, SH_CAP = 5.0, (25.0, 50.0)
EPS = 1e-9
INF = float("inf")
REB = 0.2 * 0.07                      # rebate maker por acción = REB·p·(1−p)
RNG_SEED = 26
MIN_FILL_COIN, MIN_FILL_ALL = 30, 150
GATE = {"n_fill": 40, "ev": 0.05, "dias_pos": 4}

_CENT = {}


def mils(s):
    """'0.49' -> 490 (caché de cadenas: el registro repite los mismos precios)."""
    v = _CENT.get(s)
    if v is None:
        v = _CENT[s] = int(round(float(s) * 1000))
    return v


# ---------------------------------------------------------------- motores (combinaciones política x capa x cola x tamaño)
class Eng:
    __slots__ = ("idx", "pol", "capa", "cola", "sh", "c1", "c2", "nombre", "plc", "lam")

    def __init__(self, idx, pol, capa, cola, sh, c1, c2, plc="", lam=None):
        self.idx, self.pol, self.capa, self.cola, self.sh, self.c1, self.c2 = idx, pol, capa, cola, sh, c1, c2
        self.lam = LAT_CANCEL_MS if lam is None else lam   # Λ: ms entre la RECEPCIÓN de la alarma y la cancelación efectiva en el libro
        self.plc = plc            # "" = real | "inv" = alarma de Binance en el sentido CONTRARIO | "shift" = alarmas desplazadas PLC_SHIFT_MS
        self.nombre = f"{pol}|{capa}|{cola}|{sh:g}"


def sfx(lam):
    return "" if lam == LAT_CANCEL_MS else f"_L{lam}"


def capas():
    """[(nombre, c1 (u, w_ms) | None, c2 k | None, Λ ms)]  El nombre lleva _L<Λ> salvo para Λ = LAT_CANCEL_MS (60)."""
    out = [("C0", None, None, LAT_CANCEL_MS)]
    for lam in LAMBDAS:
        out += [(f"C1_u{u:g}_w{w // 1000 if w % 1000 == 0 else w}{sfx(lam)}", (u, w), None, lam) for u in C1_U for w in C1_W]
        out += [(f"C2_k{k}{sfx(lam)}", None, k, lam) for k in C2_K]
        out += [(f"C12_u{u:g}_w{w // 1000 if w % 1000 == 0 else w}_k{C12_K}{sfx(lam)}", (u, w), C12_K, lam) for u in C1_U for w in C1_W]
    return out


def capas_placebo():
    """[(nombre, c1, c2, modo, Λ)] Control de las capas (solo JOIN x CONS x SH=5): C1 invertida (Binance a FAVOR del lado), C1 y C2
    desplazadas 30 min. Si la capa real no mejora a su placebo y a su inversión, no ordena nada (trampa 'ranking cuyo placebo e
    inversión salen igual')."""
    out = []
    for lam in LAMBDAS:
        wn = lambda w: w // 1000 if w % 1000 == 0 else w   # noqa: E731
        out += [(f"PINV_u{u:g}_w{wn(w)}{sfx(lam)}", (u, w), None, "inv", lam) for u in C1_U for w in C1_W]
        out += [(f"PSH_u{u:g}_w{wn(w)}{sfx(lam)}", (u, w), None, "shift", lam) for u in C1_U for w in C1_W]
        out += [(f"PSH_C2_k{k}{sfx(lam)}", None, k, "shift", lam) for k in C2_K]
    return out


def construir_motores(pols=("JOIN", "IMPROVE"), colas=("CONS", "OPT"), sh_cap=SH_CAP, solo_capas=None, placebo=True):
    E = []
    for pol in pols:
        for cap, c1, c2, lam in capas():
            if solo_capas and cap not in solo_capas:
                continue
            for cola in colas:
                if cola == "OPT" and pol != "JOIN":
                    continue
                E.append(Eng(len(E), pol, cap, cola, SH_BASE, c1, c2, lam=lam))
    for pol in pols:
        for sh in sh_cap:
            if not solo_capas or "C0" in solo_capas:
                E.append(Eng(len(E), pol, "C0", "CONS", sh, None, None))
    if placebo and "JOIN" in pols and "CONS" in colas:
        for cap, c1, c2, plc, lam in capas_placebo():
            if solo_capas and cap not in solo_capas:
                continue
            E.append(Eng(len(E), "JOIN", cap, "CONS", SH_BASE, c1, c2, plc, lam))
    return E


# ---------------------------------------------------------------- externas: Binance (x) y bids de 15m, alarmas precalculadas
class Externas:
    def __init__(self):
        self.x = {}            # coin -> (np t int64, np px float) ordenados por recepción
        self.b15 = {}          # token 15m -> (np t, np bid_mils) ordenados
        self.k15 = {}          # (coin, fin_ms, lado) -> token 15m
        self._a1, self._a2 = {}, {}
        self.estado = {"x_filas": 0, "q15_filas": 0, "k15": 0, "fuente": ""}

    def c1(self, coin, u, w, d):
        """Instantes (recepción, ms) en que Binance se movió >= u bps en la ventana w en la dirección d ('dn' / 'up')."""
        k = (coin, u, w, d)
        r = self._a1.get(k)
        if r is None:
            r = array("q")
            xs = self.x.get(coin)
            if xs is not None and len(xs[0]):
                t, px = xs
                ref = np.searchsorted(t, t - w, side="right") - 1
                ok = (ref >= 0) & (t[np.maximum(ref, 0)] >= t - w - STALE_MS)
                ret = np.zeros(len(t))
                ret[ok] = (px[ok] / px[ref[ok]] - 1.0) * 1e4
                sel = ok & ((ret <= -u) if d == "dn" else (ret >= u))
                r = array("q", t[sel].tolist())
            self._a1[k] = r
        return r

    def c2(self, tok15, kt):
        """Instantes en que el bid del token 15m cae >= kt ticks respecto a su máximo de los últimos W2_MS."""
        key = (tok15, kt)
        r = self._a2.get(key)
        if r is None:
            r = array("q")
            s = self.b15.get(tok15)
            if s is not None:
                t, b = s[0].tolist(), s[1].tolist()
                dq = collections.deque()          # (t, bid) con bids decrecientes
                for ti, bi in zip(t, b):
                    while dq and dq[0][0] < ti - W2_MS:
                        dq.popleft()
                    mx = max(dq[0][1], bi) if dq else bi
                    if bi <= mx - kt * TICK:
                        r.append(ti)
                    while dq and dq[-1][1] <= bi:
                        dq.pop()
                    dq.append((ti, bi))
            self._a2[key] = r
        return r

    def tok15_de(self, coin, fin5, lado):
        fin15 = -(-fin5 // 900_000) * 900_000
        return self.k15.get((coin, fin15, lado))


def _ms_iso(s):
    return int(datetime.fromisoformat(s).timestamp() * 1000)


def k15_previo(dia, out):
    """Mapa {(moneda, cierre_ms, lado): token 15m} del día ANTERIOR: el registro de un día no repite las filas k de los mercados listados
    antes de su primer instante (p. ej. BNB 15m que cierra a las 00:15 solo está en el fichero del día previo). Caché en out."""
    prev = (date.fromisoformat(dia) - timedelta(days=1)).isoformat()
    cache = (out / f"k15map_{prev}.csv.gz") if out else None
    m = {}
    if cache is not None and cache.exists():
        with gzip.open(cache, "rt") as fh:
            for ln in fh:
                coin, fin, lado, tk = ln.rstrip("\n").split(",")
                m[(coin, int(fin), lado)] = tk
        return m
    f = VOL / "m15_registro" / f"m15_registro_{prev}.csv.gz"
    if not f.exists():
        return m
    try:
        with gzip.open(f, "rt", errors="replace") as fh:
            for ln in fh:
                if ln[:2] == "k,":
                    c = ln.split(",")
                    if len(c) >= 8 and c[4] == "15min":
                        m[(c[3], _ms_iso(c[6]), c[7].strip())] = c[2]
    except (EOFError, OSError) as e:
        print(f"  k15 previo {prev}: fichero truncado ({type(e).__name__})", file=sys.stderr)
    if cache is not None and m:
        escribir_gz_atomico(cache, [f"{k[0]},{k[1]},{k[2]},{v}\n" for k, v in m.items()])
    return m


def leer_externas(dia, t_corte=None, max_lineas=None, out=None):
    """x de Binance y q de los mercados 15m desde m15_registro (mismo reloj de recepción). Si falta el fichero, x desde m5_registro
    y SIN 15m (C2 = sin dato). t_corte (ms): solo para humo, ignora lo posterior (el fichero NO es cronológico: se lee entero)."""
    ext = Externas()
    f = VOL / "m15_registro" / f"m15_registro_{dia}.csv.gz"
    if not f.exists():
        f = VOL / "m5_registro" / f"m5_registro_{dia}.csv.gz"
        ext.estado["fuente"] = "m5 (sin 15m)"
    else:
        ext.estado["fuente"] = "m15"
    sim2coin = {v: k for k, v in SIMBOLO.items()}
    xt, xp = collections.defaultdict(lambda: array("q")), collections.defaultdict(lambda: array("d"))
    tok15 = set()
    bt, bb, ult = {}, {}, {}
    tiene15 = ext.estado["fuente"] == "m15"
    if tiene15:
        ext.k15.update(k15_previo(dia, out))
        tok15.update(ext.k15.values())
        ext.estado["k15_previo"] = len(ext.k15)
    nl = 0
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                nl += 1
                if max_lineas and nl > max_lineas:
                    break
                tp = ln[:2]
                if tp == "x,":
                    c = ln.split(",")
                    coin = sim2coin.get(c[2])
                    if coin is None:
                        continue
                    try:
                        t = int(c[7])
                        px = float(c[3])
                    except (ValueError, IndexError):
                        continue
                    if t_corte and t > t_corte:
                        continue
                    xt[coin].append(t)
                    xp[coin].append(px)
                elif tp == "q," and tiene15:
                    c = ln.split(",")
                    tk = c[2]
                    if tk not in tok15:
                        continue
                    try:
                        t = int(c[7])
                        b = mils(c[3])
                    except (ValueError, IndexError):
                        continue
                    if ult.get(tk) == b:
                        continue
                    ult[tk] = b
                    if t_corte and t > t_corte:
                        continue
                    if tk not in bt:
                        bt[tk], bb[tk] = array("q"), array("h")
                    bt[tk].append(t)
                    bb[tk].append(b)
                    ext.estado["q15_filas"] += 1
                elif tp == "k," and tiene15:
                    c = ln.split(",")
                    if len(c) >= 8 and c[4] == "15min":
                        try:
                            ext.k15[(c[3], _ms_iso(c[6]), c[7].strip())] = c[2]
                            tok15.add(c[2])
                            ext.estado["k15"] += 1
                        except ValueError:
                            pass
        except (EOFError, OSError) as e:
            print(f"  externas {dia}: fichero truncado ({type(e).__name__})", file=sys.stderr)
    if tiene15 and out is not None and not t_corte and not max_lineas:
        escribir_gz_atomico(out / f"k15map_{dia}.csv.gz", [f"{k[0]},{k[1]},{k[2]},{v}\n" for k, v in ext.k15.items()])
    for coin in xt:
        t, p = np.frombuffer(xt[coin], dtype=np.int64), np.frombuffer(xp[coin], dtype=np.float64)
        o = np.argsort(t, kind="stable")
        ext.x[coin] = (t[o], p[o])
        ext.estado["x_filas"] += len(t)
    for tk in bt:
        t, b = np.frombuffer(bt[tk], dtype=np.int64), np.frombuffer(bb[tk], dtype=np.int16)
        o = np.argsort(t, kind="stable")
        ext.b15[tk] = (t[o], b[o].astype(np.int64))
    return ext


# ---------------------------------------------------------------- estado de la simulación
class Seg:
    """Una puja viva: precio (milésimas), cantidad pedida, decisión, alta, cancelación efectiva y cola."""
    __slots__ = ("precio", "qty", "dec", "act", "ceff", "cola", "adv", "vol", "volq", "sprev", "lleno", "pend", "cont")

    def __init__(self, precio, qty, dec, act, ceff, cola):
        self.precio, self.qty, self.dec, self.act, self.ceff, self.cola = precio, qty, dec, act, ceff, cola
        self.adv = self.vol = self.volq = self.lleno = 0.0
        self.sprev = cola if cola > 0 else None
        self.pend = True
        self.cont = False


class Pos:
    """Posición de un motor en una unidad (token)."""
    __slots__ = ("e", "tk", "meta", "tramo", "segs", "cur", "lock", "lleno", "coste", "reb", "norders", "ncap", "t_libro",
                 "cap_s", "srcs", "sin_dato", "completo", "n_sin_dato", "tsum", "na", "opt", "last_act")

    def __init__(self, e, tk, meta, tramo):
        self.e, self.tk, self.meta, self.tramo = e, tk, meta, tramo
        self.segs, self.cur, self.lock = [], None, -1
        self.lleno = self.coste = self.reb = 0.0
        self.norders = self.ncap = self.n_sin_dato = 0
        self.t_libro = self.cap_s = self.tsum = 0.0
        self.srcs, self.sin_dato, self.completo = None, False, False
        self.na = INF
        self.opt = e.cola == "OPT"
        self.last_act = -1


class Meta:
    __slots__ = ("coin", "mkt", "fin", "lado")

    def __init__(self, coin, mkt, fin, lado):
        self.coin, self.mkt, self.fin, self.lado = coin, mkt, fin, lado


class Motor:
    """Una pasada cronológica (por tramos) por el registro m5 con todos los motores a la vez."""

    def __init__(self, engines, ext, dia_ini_ms=0, traza=False):
        self.traza = [] if traza else None
        self.E = engines
        self.ext = ext
        self.meta, self.par, self.por_mkt = {}, {}, {}
        self.top = {}                 # token -> (bid, ask, bsz) en milésimas / acciones
        self.pos = {}                 # token -> lista de Pos|None (len NE) del tramo actual
        self.pos_ant = []             # posiciones de tramos cerrados
        self.vivos = {}               # token -> set de Pos con pujas que aún pueden rellenar
        self.espera = {}              # token -> set de índices de motor pendientes de reevaluar (bloqueo/vuelo)
        self.fuentes = {}             # (token, idx capa) -> lista de arrays de alarmas | None (sin dato)
        self.tramos = []              # [(t0, t1)]
        self.t0 = self.t_ult = None
        self.dia_ini = dia_ini_ms
        self.cap_min = {}             # idx motor -> np.array por minuto del día (capital·s)
        self.st = collections.Counter()
        self.NE = len(engines)
        self.mercados = {}            # mkt -> (fin, tramo del que se vio)

    # ---- reloj / tramos
    def reloj(self, t):
        if self.t_ult is None:
            self.t0 = self.t_ult = t
            return
        if t < self.t_ult - BACK_MS or t > self.t_ult + GAP_MS:
            self.st["saltos_atras" if t < self.t_ult else "huecos_adelante"] += 1
            self.cerrar_tramo()
            self.t0 = self.t_ult = t
        elif t > self.t_ult:
            self.t_ult = t

    def cerrar_tramo(self):
        if self.t0 is None:
            return
        self.tramos.append((self.t0, self.t_ult))
        self.pos_ant.extend(p for l in self.pos.values() for p in l if p is not None)
        self.pos, self.vivos, self.espera, self.top = {}, {}, {}, {}

    # ---- mapa
    def k(self, c):
        if len(c) >= 8 and c[4] == "5min" and c[2] not in self.meta:
            fin = _ms_iso(c[6])
            m = Meta(c[3], c[5], fin, c[7].strip())
            self.meta[c[2]] = m
            d = self.por_mkt.setdefault(c[5], {})
            d[m.lado] = c[2]
            if len(d) == 2 and "YES" in d and "NO" in d:
                self.par[d["YES"]] = d["NO"]
                self.par[d["NO"]] = d["YES"]

    # ---- alarmas
    def _srcs(self, e, tk, m):
        key = (tk, e.capa)
        if key in self.fuentes:
            return self.fuentes[key]
        s = []
        desp = (lambda a: array("q", [x + PLC_SHIFT_MS for x in a])) if e.plc == "shift" else (lambda a: a)
        if e.c1:
            dn = (m.lado == "YES") != (e.plc == "inv")
            s.append(desp(self.ext.c1(m.coin, e.c1[0], e.c1[1], "dn" if dn else "up")))
        if e.c2:
            t15 = self.ext.tok15_de(m.coin, m.fin, m.lado)
            if t15 is None or t15 not in self.ext.b15:
                s = None
            else:
                s.append(desp(self.ext.c2(t15, e.c2)))
        self.fuentes[key] = s
        return s

    @staticmethod
    def _bloq(srcs, t):
        for a in srcs:
            i = bisect.bisect_right(a, t)
            if i and t - a[i - 1] < COOL_MS:
                return True
        return False

    def _catch(self, pos, t):
        """Aplica con retraso la primera alarma posterior a la decisión de la puja viva (cancelación efectiva alarma + 60 ms)
        y deja al motor en espera para recotizar cuando acabe el enfriamiento."""
        cur = pos.cur
        if cur is None or pos.na > t:
            return
        na = pos.na
        pos.na = INF
        self._cancelar(pos, na, "capa", pos.e.lam)
        self.espera.setdefault(pos.tk, set()).add(pos.e.idx)

    # ---- órdenes
    def _cancelar(self, pos, t, motivo, lat=None):
        cur = pos.cur
        if cur is None:
            return
        cur.ceff = min(cur.ceff, t + (LAT_CANCEL_MS if lat is None else lat))
        pos.cur = None
        if motivo == "capa":
            pos.ncap += 1
        self._cuenta(pos, cur)

    def _cuenta(self, pos, seg):
        """Tiempo en libro y capital·s de una puja cuyo ceff ya es definitivo."""
        if seg.cont:
            return
        seg.cont = True
        dur = max(0.0, seg.ceff - seg.act) / 1000.0
        pos.t_libro += dur
        capital = seg.precio / 1000.0 * (seg.qty - 0.0)
        pos.cap_s += capital * dur
        if dur > 0:
            arr = self.cap_min.get(pos.e.idx)
            if arr is None:
                arr = self.cap_min[pos.e.idx] = np.zeros(1500)
            a0, a1 = seg.act, seg.ceff
            while a0 < a1:
                mi = int((a0 - self.dia_ini) // 60000)
                lim = self.dia_ini + (mi + 1) * 60000
                x1 = min(a1, lim)
                if 0 <= mi < 1500:
                    arr[mi] += capital * (x1 - a0) / 1000.0
                a0 = x1

    def _post(self, e, pos, tk, m, precio, t_rx, bid, bsz):
        if len(pos.segs) > 8:
            self._prune(pos, t_rx)
        qty = e.sh - pos.lleno
        stop = m.fin - T_MIN * 1000 + LAT_CANCEL_MS
        cola = float(bsz) if precio == bid else 0.0
        seg = Seg(precio, qty, t_rx, t_rx + LAT_POST_MS, stop, cola)
        pos.segs.append(seg)
        pos.cur = seg
        pos.lock = t_rx + LAT_POST_MS
        pos.last_act = seg.act
        pos.norders += 1
        self.vivos.setdefault(tk, set()).add(pos)
        self.st["pujas"] += 1
        na = INF
        if pos.srcs:
            for a in pos.srcs:
                i = bisect.bisect_right(a, t_rx)
                if i < len(a) and a[i] < na:
                    na = a[i]
        pos.na = na
        if self.traza is not None:
            self.traza.append((e.nombre, tk, t_rx, precio, qty))

    def _prune(self, pos, t):
        keep = []
        for g in pos.segs:
            if g.ceff < t - 5000 and g is not pos.cur:
                self._cuenta(pos, g)
            else:
                keep.append(g)
        pos.segs = keep

    # ---- eventos
    def q(self, tk, bid, ask, bsz, t_ex, t_rx):
        m = self.meta.get(tk)
        if m is None:
            return
        prev = self.top.get(tk)
        self.top[tk] = (bid, ask, bsz)
        vv = self.vivos.get(tk)
        T = (m.fin - t_rx) * 0.001
        if vv:
            for pos in vv:
                if pos.na <= t_rx:
                    self._catch(pos, t_rx)
            if T < T_MIN - 5:                      # parada programada ya efectiva con margen: se cierran las cuentas
                for pos in vv:
                    for g in pos.segs:
                        self._cuenta(pos, g)
                    pos.segs = []
                    pos.cur = None
                vv.clear()
            else:
                for pos in vv:
                    if pos.opt or t_ex <= pos.last_act:        # solo la cola pendiente de congelar o la optimista miran el tamaño
                        self._libro(pos, bid, bsz, t_ex)
        if T <= T_MIN or T > T_MAX:
            return
        banda = P_LO < bid <= P_HI and 0 < ask and bid < ask
        if not banda:
            if vv:
                for pos in list(vv):
                    if pos.cur is not None:
                        self._catch(pos, t_rx)
                        self._cancelar(pos, t_rx, "banda")
            esp = self.espera.get(tk)
            if esp:
                esp.clear()
            return
        cambio = prev is None or prev[0] != bid or prev[1] != ask
        if cambio and bid % TICK:
            self.st["bid_subcent_en_banda"] += 1
        esp = self.espera.get(tk)
        if not cambio and not esp:
            return
        pl = self.pos.get(tk)
        if pl is None:
            pl = self.pos[tk] = [None] * self.NE
        idxs = range(self.NE) if cambio else sorted(esp)
        if esp:
            esp.clear()
        for i in idxs:
            self._eval(self.E[i], pl, tk, m, t_rx, bid, ask, bsz)

    def libro_vacio(self, tk, t_rx):
        """Fila q sin bid o sin ask: sin dato -> fuera de banda: se cancela lo vivo y no se cotiza."""
        self.st["q_libro_vacio"] += 1
        self.top.pop(tk, None)
        vv = self.vivos.get(tk)
        if vv:
            for pos in list(vv):
                if pos.cur is not None:
                    self._catch(pos, t_rx)
                    self._cancelar(pos, t_rx, "banda")
        esp = self.espera.get(tk)
        if esp:
            esp.clear()

    def _eval(self, e, pl, tk, m, t_rx, bid, ask, bsz):
        pos = pl[e.idx]
        if pos is not None:
            if pos.completo:
                return
            if t_rx < pos.lock:
                self.espera.setdefault(tk, set()).add(e.idx)
                return
            self._catch(pos, t_rx)
        srcs = self._srcs(e, tk, m)
        sin = srcs is None
        bloq = (not sin) and bool(srcs) and self._bloq(srcs, t_rx)
        if e.pol == "JOIN":
            objetivo = bid
        else:
            objetivo = bid + TICK if bid + TICK < ask else None
        ok = (not sin) and (not bloq) and objetivo is not None and P_LO < objetivo <= P_HI and objetivo < ask
        cur = pos.cur if pos is not None else None
        if cur is not None:
            if ok and objetivo == cur.precio:
                return
            self._cancelar(pos, t_rx, "capa" if (bloq or sin) else "recoloca")
        if not ok:
            if bloq:
                self.espera.setdefault(tk, set()).add(e.idx)
            if sin:
                self.st["sin_dato|" + e.nombre] += 1
            return
        if pos is None:
            pos = pl[e.idx] = Pos(e, tk, m, len(self.tramos))
            pos.srcs = srcs
        self._post(e, pos, tk, m, objetivo, t_rx, bid, bsz)

    def _libro(self, pos, bid, bsz, t_ex):
        opt = pos.e.cola == "OPT"
        for g in pos.segs:
            if g.pend:
                if t_ex <= g.act:
                    if bid == g.precio:
                        g.cola = float(bsz)
                        g.sprev = float(bsz)
                    elif bid < g.precio:
                        g.cola = 0.0
                else:
                    g.pend = False
            elif opt and g.ceff > t_ex:
                if bid == g.precio:
                    if g.sprev is not None and g.sprev > 0:
                        canc = (g.sprev - bsz) - g.volq
                        if canc > EPS:
                            ahead = max(0.0, g.cola - g.adv - g.vol)
                            g.adv += canc * min(1.0, ahead / g.sprev)
                    g.sprev = float(bsz)
                else:
                    g.sprev = None
                g.volq = 0.0

    def t(self, tk, p, side, sz, t_ex, t_rx):
        m = self.meta.get(tk)
        if m is None:
            return
        if side == "SELL":
            obj, pe = tk, p
        elif side == "BUY":
            obj = self.par.get(tk)
            if obj is None:
                return
            pe = 1000 - p
        else:
            return
        vv = self.vivos.get(obj)
        if not vv:
            return
        top = self.top.get(obj)
        top_bid = top[0] if top else 0
        for pos in list(vv):
            self._catch(pos, t_rx)
            e = pos.e
            if pos.lleno >= e.sh - EPS:
                continue
            vivo = False
            for g in pos.segs:
                if g.ceff < t_ex - 5000 and g is not pos.cur:
                    continue
                vivo = True
                if t_ex < g.act or t_ex > g.ceff:
                    continue
                rem = min(g.qty - g.lleno, e.sh - pos.lleno)
                if rem <= EPS:
                    continue
                if pe < g.precio:
                    f = rem if g.precio <= top_bid else min(rem, sz)
                elif pe == g.precio:
                    g.vol += sz
                    g.volq += sz
                    f = min(rem, max(0.0, g.vol - (g.cola - g.adv) - g.lleno))
                else:
                    continue
                if f > EPS:
                    g.lleno += f
                    pos.lleno += f
                    pos.coste += f * g.precio / 1000.0
                    pos.reb += f * REB * (g.precio / 1000.0) * (1 - g.precio / 1000.0)
                    pos.tsum += f * (m.fin - t_ex) / 1000.0
                    self.st["rellenos"] += 1
            if pos.lleno >= e.sh - EPS:
                pos.completo = True
                if pos.cur is not None:
                    pos.cur.ceff = min(pos.cur.ceff, t_ex)
                pos.cur = None
                for g in pos.segs:
                    g.ceff = min(g.ceff, t_ex)
                    self._cuenta(pos, g)
                pos.segs = []
                vv.discard(pos)
            elif not vivo:
                self._prune(pos, t_ex)
                if not pos.segs:
                    vv.discard(pos)

    # ---- cierre
    def terminar(self):
        self.cerrar_tramo()
        for pos in self.pos_ant:
            for g in pos.segs:
                if not g.cont:
                    self._cuenta(pos, g)
        return len(self.tramos)

    def mercado_completo(self, fin, tr):
        t0, t1 = self.tramos[tr]
        return fin - 300_000 >= t0 - INC_MS and fin <= t1 + INC_MS

    def filas(self, dia):
        out = []
        for pos in self.pos_ant:
            if pos.norders == 0:
                continue
            m = pos.meta
            comp = self.mercado_completo(m.fin, pos.tramo)
            pm = pos.coste / pos.lleno if pos.lleno > 0 else 0.0
            e = pos.e
            out.append((dia, e.nombre, m.coin, m.mkt, m.lado, pos.tramo, int(comp), pos.norders, pos.ncap, round(pos.lleno, 4),
                        round(pos.coste, 6), round(pm, 4), round(pos.reb, 6), round(pos.t_libro, 3), round(pos.cap_s, 3),
                        round(pos.tsum / pos.lleno, 1) if pos.lleno > 0 else ""))
        return out

    def universo(self):
        """Mercados 5m vistos cuyo ciclo completo [apertura, cierre] cae dentro de un tramo del registro."""
        ok = []
        for mk, d in self.por_mkt.items():
            tk = d.get("YES")
            m = self.meta.get(tk)
            if m is None:
                continue
            if any(self.mercado_completo(m.fin, i) for i in range(len(self.tramos))):
                ok.append(mk)
        return ok


COLS = ["dia", "motor", "act", "mkt", "lado", "tramo", "completo", "norders", "ncap", "lleno", "coste", "precio_m", "rebate",
        "t_libro_s", "cap_s"]


def procesar_registro(f, ext, engines, dia_ini_ms, max_lineas=None, t_corte=None, traza=False):
    """Una pasada por el registro m5 del día. -> Motor terminado."""
    mo = Motor(engines, ext, dia_ini_ms, traza)
    n = 0
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                n += 1
                if max_lineas and n > max_lineas:
                    break
                tp = ln[:2]
                if tp == "q,":
                    c = ln.split(",")
                    tk = c[2]
                    if tk not in mo.meta:
                        continue
                    try:
                        t_rx = int(c[7])
                        t_ex = int(c[1])
                    except (ValueError, IndexError):
                        mo.st["q_ilegibles"] += 1
                        continue
                    if t_corte and t_rx > t_corte:
                        break
                    mo.reloj(t_rx)
                    try:
                        bid, ask, bsz = mils(c[3]), mils(c[4]), float(c[5])
                    except (ValueError, IndexError):
                        mo.libro_vacio(tk, t_rx)         # lado vacío o ilegible: no hay dato para cotizar y se retira lo vivo
                        continue
                    # reloj de RECEPCIÓN: el sello del WS del CLOB es de lote (hasta 468 ms antes del casado); t_ex NO se usa
                    mo.q(tk, bid, ask, bsz, t_rx - FEED_MS, t_rx)
                elif tp == "t,":
                    c = ln.split(",")
                    tk = c[2]
                    if tk not in mo.meta:
                        continue
                    try:
                        t_ex, p, side, sz = int(c[1]), mils(c[3]), c[4], float(c[5])
                    except (ValueError, IndexError):
                        mo.st["t_ilegibles"] += 1
                        continue
                    try:
                        t_rx = int(c[6])
                    except (ValueError, IndexError):
                        t_rx = mo.t_ult if mo.t_ult is not None else t_ex
                    if t_corte and t_rx > t_corte:
                        break
                    mo.reloj(t_rx)
                    # casado modelado = recepción del print − FEED_MS (orden de recepción; la cancelación cuenta solo si ceff >= casado)
                    mo.t(tk, p, side, sz, t_rx - FEED_MS, mo.t_ult)
                elif tp == "k,":
                    mo.k(ln.split(","))
                elif tp == "x,":
                    c = ln.split(",")
                    try:
                        t_rx = int(c[7])
                    except (ValueError, IndexError):
                        continue
                    if t_corte and t_rx > t_corte:
                        break
                    mo.reloj(t_rx)
        except (EOFError, OSError) as e:
            print(f"  {f.name}: fichero truncado ({type(e).__name__}) tras {n} líneas", file=sys.stderr)
            mo.st["truncado"] = 1
    mo.st["lineas"] = n
    mo.terminar()
    return mo


# ---------------------------------------------------------------- desenlaces, cobertura y cachés durables
def sha_fichero(p, bloque=1 << 20):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for b in iter(lambda: fh.read(bloque), b""):
            h.update(b)
    return h.hexdigest()


def sha_codigo():
    return sha_fichero(Path(__file__))


def escribir_atomico(ruta, datos, binario=False):
    tmp = ruta.with_name(ruta.name + f".tmp{os.getpid()}")
    with open(tmp, "wb" if binario else "w") as fh:
        fh.write(datos)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, ruta)


def escribir_gz_atomico(ruta, lineas):
    tmp = ruta.with_name(ruta.name + f".tmp{os.getpid()}")
    with gzip.open(tmp, "wt") as fh:
        for ln in lineas:
            fh.write(ln)
    os.replace(tmp, ruta)


def params_dict(engines):
    return {"P_LO": P_LO, "P_HI": P_HI, "TICK": TICK, "T": [T_MIN, T_MAX], "LAT_POST_MS": LAT_POST_MS,
            "LAT_CANCEL_MS": LAT_CANCEL_MS, "COOL_MS": COOL_MS, "W2_MS": W2_MS, "STALE_MS": STALE_MS, "GAP_MS": GAP_MS,
            "BACK_MS": BACK_MS, "C1": [C1_U, C1_W], "C2_K": C2_K, "C12_K": C12_K, "PLC_SHIFT_MS": PLC_SHIFT_MS, "LAMBDAS": list(LAMBDAS), "FEED_MS": FEED_MS, "SH": [SH_BASE, list(SH_CAP)],
            "motores": [e.nombre for e in engines]}


def params_hash(engines):
    return hashlib.sha256(json.dumps(params_dict(engines), sort_keys=True).encode()).hexdigest()[:16]


def fila_csv(r, des):
    (dia, motor, act, mkt, lado, tramo, comp, no, nc, lleno, coste, pm, reb, tl, cs, tf) = r
    d = des.get(mkt, "")
    pnl = "" if not d else round((lleno if d == lado else 0.0) - coste, 6)
    return ",".join(str(x) for x in (dia, motor, act, mkt, lado, tramo, comp, no, nc, lleno, coste, pm, reb, tl, cs, tf, d, pnl)) + "\n"


CAB = ",".join(COLS + ["t_fill_s", "des", "pnl"]) + "\n"


def cache_valida(out, d, ph):
    meta = out / f"meta_{d}.json"
    f = out / f"unidades_{d}.csv.gz"
    if not (meta.exists() and f.exists()):
        return None
    try:
        m = json.loads(meta.read_text())
        if m.get("script_sha") != sha_codigo() or m.get("params_hash") != ph or m.get("cobertura_des", 0) < 0.99:
            return None
        if sha_fichero(f) != m.get("sha_unidades"):
            return None
        return m
    except (ValueError, OSError):
        return None


def validar_unicidad(filas):
    c = collections.Counter((r[0], r[1], r[3], r[4], r[5]) for r in filas)
    dup = [k for k, v in c.items() if v > 1]
    return dup


def correr_dia(d, engines, out, args, log, des_fn=None):
    """Simula el día d y escribe el checkpoint durable. -> dict de estado/cobertura del día."""
    t_ini = time.time()
    f5 = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    est = {"dia": d, "estado": "FALTA_ENTRADA", "inicio": datetime.now(timezone.utc).isoformat()}
    if not f5.exists():
        log(f"{d}: falta {f5}")
        return est, None, None, None, None
    dia_ini = int(datetime.fromisoformat(d + "T00:00:00+00:00").timestamp() * 1000)
    t_corte = dia_ini + args.recorte_min * 60_000 if args.recorte_min else None
    ext = leer_externas(d, t_corte, args.max_lineas_ext, out)
    log(f"{d}: externas {ext.estado} (Binance {ext.estado['x_filas']} filas, 15m {ext.estado['q15_filas']} cambios de bid, "
        f"{ext.estado['k15']} mercados 15m) en {time.time() - t_ini:.0f}s")
    mo = procesar_registro(f5, ext, engines, dia_ini, args.max_lineas, t_corte)
    filas = mo.filas(d)
    dup = validar_unicidad(filas)
    if dup:
        raise RuntimeError(f"{d}: claves duplicadas {dup[:3]}")
    mids = {r[3] for r in filas}
    universo = mo.universo()
    des_fn = des_fn or desenlaces_oficiales
    des = des_fn(mids | set(universo)) if (mids or universo) else {}
    cob = (sum(1 for m in mids if m in des) / len(mids)) if mids else 1.0
    cob_u = (sum(1 for m in universo if m in des) / len(universo)) if universo else 1.0
    n_inc = sum(1 for r in filas if not r[6])
    est.update({"estado": "OK", "lineas": mo.st["lineas"], "tramos": [[a, b] for a, b in mo.tramos], "filas": len(filas),
                "unidades_incompletas": n_inc, "mercados_universo": len(universo), "cobertura_des": cob,
                "cobertura_des_universo": cob_u, "contadores": dict(mo.st),
                "externas": ext.estado, "segundos": round(time.time() - t_ini, 1)})
    if args.recorte_min or args.max_lineas:
        est["estado"] = "HUMO_NO_CACHEADO"
        return est, filas, des, mo, universo
    if cob < 0.99:
        est["estado"] = "COBERTURA_DES_BAJA"
        log(f"{d}: cobertura de desenlaces {cob:.1%} < 99 %: no se cachea (se reintenta)")
        return est, filas, des, mo, universo
    ruta = out / f"unidades_{d}.csv.gz"
    escribir_gz_atomico(ruta, [CAB] + [fila_csv(r, des) for r in filas])
    escribir_gz_atomico(out / f"universo_{d}.csv.gz", [f"{m}\n" for m in sorted(universo)])
    escribir_gz_atomico(out / f"tokens_{d}.csv.gz", [f"{tk},{m.coin},{m.mkt},{m.fin // 1000},{m.lado}\n"
                                                       for tk, m in mo.meta.items()])
    cap = {str(i): arr.tolist() for i, arr in mo.cap_min.items()}
    escribir_atomico(out / f"capital_min_{d}.json", json.dumps({engines[int(i)].nombre: v for i, v in cap.items()}))
    est.update({"sha_unidades": sha_fichero(ruta), "script_sha": sha_codigo(), "params_hash": params_hash(engines)})
    escribir_atomico(out / f"meta_{d}.json", json.dumps(est, indent=1))
    est["estado"] = "COMPLETO"
    return est, filas, des, mo, universo


def desenlaces_oficiales(mids):
    from analisis_maker_cancelacion_binance import desenlaces
    return desenlaces(set(mids))


# ---------------------------------------------------------------- población on-chain (réplica de la regla del vigía H26)
def poblacion_fills(d, tok, des_fn=None):
    """Rellenos MAKER on-chain de la celda congelada (compran un lado a pc en (0,10, 0,30] con T en (60, 300]) del día d, SOLO de los
    mercados con token en `tok` {token: (coin, mkt, fin_s, lado)}. Réplica de vigia_5m_barato_maker_forward.unidades_dia (que no se
    importa: hashea su fichero) con precio, T y posición en la cola por relleno. -> DataFrame de rellenos con desenlace."""
    import pandas as pd
    f = VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz"
    if not f.exists():
        return None
    t_act = {t: v[0] for t, v in tok.items()}
    t_mkt = {t: v[1] for t, v in tok.items()}
    t_fin = {t: v[2] for t, v in tok.items()}
    t_lado = {t: v[3] for t, v in tok.items()}
    partes = []
    with gzip.open(f, "rt") as fh:
        for x in pd.read_csv(fh, chunksize=150_000, dtype={"token_id": str, "tx": str, "maker": str, "taker": str},
                             usecols=["tipo", "ts_est", "tx", "log_index", "maker", "taker", "side", "token_id", "maker_amt",
                                      "taker_amt"]):
            x = x[(x.tipo == "F") & (x.taker != EXCH) & x.token_id.isin(tok.keys())]
            if not len(x):
                continue
            tk = x.token_id
            venta = x.side.values == 1
            acc = np.where(venta, x.maker_amt.values, x.taker_amt.values).astype(float)
            usdc = np.where(venta, x.taker_amt.values, x.maker_amt.values).astype(float)
            partes.append(pd.DataFrame({
                "tx": x.tx.values, "li": x.log_index.astype(int).values, "act": tk.map(t_act).values, "mkt": tk.map(t_mkt).values,
                "T": tk.map(t_fin).astype(float).values - x.ts_est.astype(float).values, "lado": tk.map(t_lado).values,
                "venta": venta, "acc": acc, "usdc": usdc}))
    if not partes:
        return pd.DataFrame()
    X = pd.concat(partes, ignore_index=True)
    X = X[X.acc > 0]
    X["lado_c"] = np.where(X.venta, np.where(X.lado == "YES", "NO", "YES"), X.lado)
    X["pc"] = np.where(X.venta, 1 - X.usdc / X.acc, X.usdc / X.acc)
    X["coste"] = np.where(X.venta, X.acc - X.usdc, X.usdc)
    X = X[X.coste > 0]
    X["nivel"] = X.pc.round(3)
    g = X.groupby(["tx", "lado_c", "nivel"]).li
    X["n_niv"] = g.transform("size")
    X["rk"] = g.rank(method="first")
    X["cola"] = np.where(X.n_niv < 2, "solo", np.where(X.rk == 1, "cabeza", np.where(X.rk == X.n_niv, "final", "medio")))
    C = X[(X.pc > 0.10) & (X.pc <= 0.30) & (X["T"] > 60) & (X["T"] <= 300)].copy()
    des_fn = des_fn or desenlaces_oficiales
    des = des_fn(set(X.mkt))
    C["des"] = C.mkt.map(des)
    C = C[C.des.notna()]
    C["pnl"] = np.where(C.lado_c == C.des, C.acc, 0.0) - C.coste
    return C[["mkt", "lado_c", "act", "T", "pc", "acc", "coste", "cola", "des", "pnl"]].reset_index(drop=True)


def unidades_poblacion(C):
    """Agrupa los rellenos por unidad (mercado, lado comprado), como el vigía."""
    g = C.groupby(["mkt", "lado_c"], sort=False)
    U = g.agg(act=("act", "first"), pnl=("pnl", "sum"), coste=("coste", "sum"), acc=("acc", "sum"), n=("pc", "size"),
              T=("T", "mean"), des=("des", "first")).reset_index()
    U["pc"] = U.coste / U.acc
    U["gana"] = (U.lado_c == U.des).astype(int)
    return U


# ---------------------------------------------------------------- estadística del informe
def ic90_dias(v, seed=RNG_SEED, B=4000):
    v = np.asarray([x for x in v if x == x], float)
    if len(v) < 2:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    m = v[rng.integers(0, len(v), size=(B, len(v)))].mean(1)
    return (float(np.quantile(m, .05)), float(np.quantile(m, .95)))


def metricas(U, total_dias=None):
    """U: DataFrame de unidades RELLENAS con columnas dia, pnl, coste (más lleno/rebate opcionales). -> dict (EV pooled, por días)."""
    if U is None or not len(U):
        return {"n_fill": 0, "ev": float("nan"), "ev_dias": float("nan"), "ic90": (float("nan"), float("nan")), "dias": 0,
                "dias_pos": 0, "ev_sin_mejor": float("nan"), "ev_sin_2mejores": float("nan"), "pnl": 0.0, "pnl_dia": float("nan"), "coste": 0.0}
    pd_ = U.groupby("dia").agg(pnl=("pnl", "sum"), coste=("coste", "sum"), n=("pnl", "size"))
    evd = (pd_.pnl / pd_.coste).values
    mejor = pd_.pnl.idxmax()
    resto = pd_.drop(index=mejor)
    resto2 = pd_.drop(index=pd_.pnl.nlargest(2).index)
    nd = total_dias or len(pd_)
    return {"n_fill": int(len(U)), "ev": float(U.pnl.sum() / U.coste.sum()), "ev_dias": float(np.mean(evd)),
            "ic90": ic90_dias(evd), "dias": int(len(pd_)), "dias_pos": int((pd_.pnl > 0).sum()),
            "ev_sin_mejor": float(resto.pnl.sum() / resto.coste.sum()) if len(resto) and resto.coste.sum() > 0 else float("nan"),
            "ev_sin_2mejores": float(resto2.pnl.sum() / resto2.coste.sum()) if len(resto2) and resto2.coste.sum() > 0 else float("nan"),
            "pnl": float(U.pnl.sum()), "pnl_dia": float(U.pnl.sum() / nd), "coste": float(U.coste.sum()),
            "rebate": float(U.rebate.sum()) if "rebate" in U else float("nan"),
            "ev_con_rebate": float((U.pnl.sum() + U.rebate.sum()) / U.coste.sum()) if "rebate" in U else float("nan"),
            "uds_dia": float(len(U) / nd)}


def cargar_unidades(dias, out):
    import pandas as pd
    partes = []
    for d in dias:
        f = out / f"unidades_{d}.csv.gz"
        if f.exists():
            partes.append(pd.read_csv(f, dtype={"mkt": str, "des": str, "pnl": float}))
    if not partes:
        return None
    return pd.concat(partes, ignore_index=True)


def tabla_motor(U, dias):
    """Por motor: unidades con orden, rellenas, métricas. U ya filtrado a completo==1 y con desenlace. -> list[dict]."""
    out = []
    for mot, g in U.groupby("motor"):
        F = g[g.lleno > 0]
        r = metricas(F, total_dias=len(dias))
        r.update({"motor": mot, "n_ord": int(len(g)), "n_pujas": int(g.norders.sum()), "n_cap": int(g.ncap.sum()),
                  "t_libro_s": float(g.t_libro_s.sum()), "cap_medio": float(g.cap_s.sum() / 86400.0 / max(1, len(dias)))})
        out.append(r)
    return out


def elegir_desc(U_desc, dias_desc, scopes):
    """Elección SOLO en DESC. -> {scope: (motor, métricas, nº candidatas elegibles)}."""
    sel = {}
    for sc in scopes:
        g = U_desc if sc == "ALL" else U_desc[U_desc.act == sc]
        minimo = MIN_FILL_ALL if sc == "ALL" else MIN_FILL_COIN
        cand = []
        for mot, gm in g.groupby("motor"):
            if not mot.endswith("|CONS|5") or "|PINV_" in mot or "|PSH_" in mot:      # los placebos NUNCA se eligen
                continue
            F = gm[gm.lleno > 0]
            if len(F) < minimo:
                continue
            m = metricas(F, total_dias=len(dias_desc))
            cand.append((m["ev"], mot, m))
        cand.sort(key=lambda x: -x[0])
        sel[sc] = (cand[0][1], cand[0][2], len(cand)) if cand else (None, None, 0)
    return sel


def gates(m, n_dias_oos):
    if m is None or m["n_fill"] == 0:
        return {"n_fill>=40": False, "EV>=+0,05": False, "IC90_dias>0": False, "sin_mejor_dia>0": False, "dias_pos>=4": False}
    return {"n_fill>=40": m["n_fill"] >= GATE["n_fill"], "EV>=+0,05": m["ev"] >= GATE["ev"], "IC90_dias>0": m["ic90"][0] > 0,
            "sin_mejor_dia>0": m["ev_sin_mejor"] == m["ev_sin_mejor"] and m["ev_sin_mejor"] > 0,
            "dias_pos>=4": m["dias_pos"] >= GATE["dias_pos"]}


def fmt(m):
    if m is None or m["n_fill"] == 0:
        return "sin rellenos"
    return (f"rellenas {m['n_fill']} | EV/€ {m['ev']:+.4f} IC90 días ({m['ic90'][0]:+.4f},{m['ic90'][1]:+.4f}) | días+ "
            f"{m['dias_pos']}/{m['dias']} | sin mejor día {m['ev_sin_mejor']:+.4f} | PnL {m['pnl']:+.2f} $ ({m['pnl_dia']:+.2f} $/día, "
            f"{m['uds_dia']:.1f} uds/día) | con rebate {m['ev_con_rebate']:+.4f}")


def _buckets(serie, cortes, etiquetas):
    return np.array(etiquetas, dtype=object)[np.searchsorted(cortes, serie.values, side="left")]


def calibracion(U, pob, dias, motor_ref="JOIN|C0|CONS|5"):
    """Texto de calibración: población on-chain frente a JOIN+C0 (y OPT / IMPROVE) en los mismos mercados y días."""
    import pandas as pd
    L = []
    partes = [pob[d].assign(dia=d) for d in dias if d in pob and pob[d] is not None and len(pob[d])]
    P = pd.concat(partes, ignore_index=True) if partes else None
    if P is None or not len(P):
        return ["(sin población on-chain para estos días)"], {}
    PU = unidades_poblacion(P)
    PU["dia"] = P.groupby(["mkt", "lado_c"], sort=False).dia.first().values
    res = {}

    def linea(nombre, m, hit, pr, n_ord=None):
        extra = f" | órdenes {n_ord}" if n_ord is not None else ""
        return (f"  {nombre:34} unidades {m['n_fill']:6d}{extra} | EV/€ {m['ev']:+.4f} IC90 días ({m['ic90'][0]:+.4f},{m['ic90'][1]:+.4f})"
                f" | acierto {hit:.1%} vs precio {pr:.3f} ({(hit - pr) * 100:+.1f} pp) | días+ {m['dias_pos']}/{m['dias']}")

    mp = metricas(PU, total_dias=len(dias))
    L.append(linea("POBLACIÓN on-chain (réplica H26)", mp, PU.gana.mean(), float(PU.coste.sum() / PU.acc.sum())))
    res["poblacion"] = {k: mp[k] for k in ("n_fill", "ev", "ev_dias", "ic90", "dias_pos")}
    fin = P[P.cola == "final"]
    UF = unidades_poblacion(fin)
    UF["dia"] = fin.groupby(["mkt", "lado_c"], sort=False).dia.first().values
    mf = metricas(UF, total_dias=len(dias))
    res["poblacion_final"] = {k: mf[k] for k in ("n_fill", "ev", "ev_dias", "ic90", "dias_pos")}
    L.append(linea("  población, solo 'final de la cola'", mf, UF.gana.mean(), float(UF.coste.sum() / UF.acc.sum())))
    for motor in (motor_ref, "JOIN|C0|OPT|5", "IMPROVE|C0|CONS|5"):
        g = U[U.motor == motor]
        if not len(g):
            continue
        F = g[g.lleno > 0].copy()
        m = metricas(F, total_dias=len(dias))
        F["gana"] = (F.lado == F.des).astype(int)
        L.append(linea(f"NOSOTROS {motor}", m, F.gana.mean() if len(F) else float("nan"),
                       float(F.coste.sum() / F.lleno.sum()) if len(F) else float("nan"), n_ord=len(g)))
        N = g[g.lleno == 0]
        if len(N):
            ganan = (N.lado == N.des).mean()
            L.append(f"      sin relleno: {len(N)} órdenes, su lado ACIERTA {ganan:.1%} (selección adversa si > el de las rellenas)")
        res[motor] = {k: m[k] for k in ("n_fill", "ev", "ev_dias", "ic90", "dias_pos")}
    g = U[U.motor == motor_ref]
    F = g[g.lleno > 0].copy()
    # desglose por momento, precio y moneda: población vs nosotros
    L.append("  Desglose (EV/€ agrupado; n unidades). Población: por relleno; nosotros: por unidad.")
    cT, eT = [120, 180, 240], ["T 60-120", "T 120-180", "T 180-240", "T 240-300"]
    cP, eP = [0.15, 0.20, 0.25], ["p 0,10-0,15", "p 0,15-0,20", "p 0,20-0,25", "p 0,25-0,30"]
    P["bT"] = _buckets(P["T"], [120, 180, 240], eT)
    P["bP"] = _buckets(P["pc"], [0.15, 0.20, 0.25], eP)
    if len(F):
        F["bT"] = _buckets(F["t_fill_s"].astype(float), [120, 180, 240], eT)
        F["bP"] = _buckets(F["precio_m"].astype(float), [0.15, 0.20, 0.25], eP)
    for col, etqs in (("bT", eT), ("bP", eP)):
        for e_ in etqs:
            a = P[P[col] == e_]
            b = F[F[col] == e_] if len(F) else F
            ea = a.pnl.sum() / a.coste.sum() if len(a) else float("nan")
            eb = b.pnl.sum() / b.coste.sum() if len(b) else float("nan")
            L.append(f"    {e_:12} población {ea:+.4f} (n {len(a):5d}) | nosotros {eb:+.4f} (n {len(b):5d})")
    for e_, ca in (("BTC", P.act == "BTC"), ("ALT", P.act != "BTC")):
        a = P[ca]
        b = F[(F.act == "BTC") if e_ == "BTC" else (F.act != "BTC")] if len(F) else F
        ea = a.pnl.sum() / a.coste.sum() if len(a) else float("nan")
        eb = b.pnl.sum() / b.coste.sum() if len(b) else float("nan")
        L.append(f"    {e_:12} población {ea:+.4f} (n {len(a):5d}) | nosotros {eb:+.4f} (n {len(b):5d})")
    for cl in ("solo", "cabeza", "medio", "final"):
        a = P[P.cola == cl]
        if len(a):
            L.append(f"    cola {cl:7} población {a.pnl.sum() / a.coste.sum():+.4f} (n {len(a):5d} rellenos; acierto de la acción "
                     f"{(a.lado_c == a.des).mean():.1%} vs precio {a.pc.mean():.3f})")
    # solapamiento por unidad
    if len(F):
        kp = set(zip(PU.dia, PU.mkt, PU.lado_c))
        kn = set(zip(F.dia, F.mkt, F.lado))
        both = kp & kn
        L.append(f"  Solapamiento (dia, mercado, lado): población {len(kp)}, nosotros {len(kn)}, comunes {len(both)}")
        for nom, fk, df, kcol in (("población", kp, PU, ("dia", "mkt", "lado_c")), ("nosotros", kn, F, ("dia", "mkt", "lado"))):
            idx = pd.MultiIndex.from_frame(df[list(kcol)])
            com = np.array([k in both for k in idx])
            for etq, msk in (("comunes", com), ("solo " + nom, ~com)):
                x = df[msk]
                if len(x):
                    L.append(f"    {nom:10} {etq:16} n {len(x):6d} EV/€ {x.pnl.sum() / x.coste.sum():+.4f}")
    return L, res


def cargar_poblacion(dias, out, des_fn=None):
    """Rellenos de la población por día restringidos al universo de mercados completos (caché en out)."""
    import pandas as pd
    pob = {}
    for d in dias:
        cache = out / f"pob_fills_{d}.csv.gz"
        if cache.exists():
            pob[d] = pd.read_csv(cache, dtype={"mkt": str, "lado_c": str, "act": str, "cola": str, "des": str})
            continue
        ft, fu = out / f"tokens_{d}.csv.gz", out / f"universo_{d}.csv.gz"
        if not (ft.exists() and fu.exists()):
            continue
        tok = {}
        with gzip.open(ft, "rt") as fh:
            for ln in fh:
                tk, coin, mkt, fin, lado = ln.rstrip("\n").split(",")
                tok[tk] = (coin, mkt, int(fin), lado)
        uni = set(l.strip() for l in gzip.open(fu, "rt"))
        tok = {k: v for k, v in tok.items() if v[1] in uni}
        C = poblacion_fills(d, tok, des_fn)
        if C is None:
            continue
        escribir_gz_atomico(cache, [C.to_csv(index=False)])
        pob[d] = C
    return pob


def comprobar_poblacion(d, out, des_fn=None):
    """Compara la réplica con la caché del vigía (mismos mercados): unidades y PnL. -> texto."""
    import pandas as pd
    v = Path("/root/polymarket-research-datalogs/vigia_5m_barato_maker") / f"unidades_{d}.csv.gz"
    if not v.exists():
        return f"{d}: sin caché del vigía"
    V = pd.read_csv(v, dtype={"mkt": str})
    pob = cargar_poblacion([d], out, des_fn)
    if d not in pob:
        return f"{d}: sin réplica"
    R = unidades_poblacion(pob[d])
    com = V.merge(R, left_on=["mkt", "lado"], right_on=["mkt", "lado_c"], suffixes=("_v", "_r"))
    solo_v = len(V) - len(com)
    return (f"{d}: vigía {len(V)} unidades (PnL {V.pnl.sum():+.2f}, coste {V.coste.sum():.2f}) | réplica restringida a nuestro universo "
            f"{len(R)} | comunes {len(com)} (dif. máx. |pnl| {np.abs(com.pnl_v - com.pnl_r).max() if len(com) else float('nan'):.6f}) "
            f"| solo en el vigía {solo_v} (mercados fuera de nuestro universo completo)")


TOL_CAL = 0.05


def veredicto_calibracion(cres, tol=TOL_CAL):
    """Criterio FIJADO ANTES de mirar (16-Oct): la población on-chain 'final de la cola' (la de la celda H5M, +0,12) debe caer dentro
    del haz [EV(JOIN+C0 cola CONSERVADORA) - tol, EV(JOIN+C0 cola OPTIMISTA) + tol] medido en los MISMOS mercados y días. Si la población
    queda por encima de la cota optimista del simulador, el simulador no explica lo que la población cobra: PARAR (no se fían las capas).
    -> dict(estado PASA|NO_REPRODUCE|SIN_DATOS, ...)."""
    r = {"estado": "SIN_DATOS", "tol": tol}
    try:
        pf, cons, opt = cres["poblacion_final"]["ev"], cres["JOIN|C0|CONS|5"]["ev"], cres["JOIN|C0|OPT|5"]["ev"]
    except (KeyError, TypeError):
        return r
    if any(x != x for x in (pf, cons, opt)):
        return r
    lo, hi = min(cons, opt) - tol, max(cons, opt) + tol
    r.update({"ev_poblacion_final": pf, "ev_join_cons": cons, "ev_join_opt": opt, "haz": [lo, hi],
              "estado": "PASA" if lo <= pf <= hi else "NO_REPRODUCE"})
    return r


def lineas_placebo(Uc, dias, etiqueta):
    """Capas reales frente a su placebo (alarmas desplazadas 30 min) y su inversión (Binance a favor), JOIN x CONS x SH=5.
    Se compara PnL TOTAL y EV/€ (esperar/cancelar puede subir el EV/€ y bajar el PnL: trampa 14-Oct)."""
    L = []
    base = "JOIN|C0|CONS|5"
    motores = sorted({m for m in Uc.motor.unique() if m.startswith("JOIN|") and m.endswith("|CONS|5")})
    if not dias or not len(motores):
        return L
    L.append(f"  [{etiqueta} {dias[0]}..{dias[-1]}] global; EV/€ agrupado | PnL total (con rebate aparte) | rellenas | órdenes")
    for mot in sorted(motores, key=lambda x: (x != base, x)):
        g = Uc[Uc.dia.isin(dias) & (Uc.motor == mot)]
        F = g[g.lleno > 0]
        m = metricas(F, total_dias=len(dias))
        if not m["n_fill"]:
            L.append(f"    {mot:34} sin rellenos (órdenes {len(g)})")
            continue
        etq = "PLACEBO " if "|PSH_" in mot else "INVERSIÓN" if "|PINV_" in mot else "REAL    " if mot != base else "BASE    "
        L.append(f"    {etq} {mot:34} EV {m['ev']:+.4f} IC90d ({m['ic90'][0]:+.3f},{m['ic90'][1]:+.3f}) | PnL {m['pnl']:+8.2f} $ | "
                 f"rellenas {m['n_fill']:5d} | órdenes {len(g):5d} | sin 2 mejores días {m['ev_sin_2mejores']:+.4f}")
    return L


def lineas_pares(Uc, dias, motor="JOIN|C0|CONS|5"):
    """Diagnóstico descriptivo de 'pares quietos' dentro de la banda: PnL por MERCADO sumando las dos unidades (YES y NO) cuando ambas
    llevaron orden. El simulador es de un lado por diseño; esta línea solo mide cuántos mercados tuvieron las dos patas cotizadas
    y qué hace la pata suelta. Referencia del proyecto (pares 15m quietos): -6/-10 c por mercado; en esta banda pocos mercados
    cotizan las dos patas (bid YES y bid NO ambos <= 0,30 exige un spread enorme)."""
    L = []
    g = Uc[Uc.dia.isin(dias) & (Uc.motor == motor)]
    if not len(g):
        return L
    g = g.assign(pnl_f=np.where(g.lleno > 0, g.pnl, 0.0))
    por = g.groupby(["dia", "mkt"]).agg(n=("lado", "nunique"), pnl=("pnl_f", "sum"), lleno=("lleno", "sum"), cost=("coste", "sum"))
    dos = por[por.n == 2]
    L.append(f"  Pares quietos ({motor}): mercados con orden {len(por)}, con las DOS patas cotizadas {len(dos)}")
    if len(dos):
        L.append(f"    PnL medio por mercado con dos patas {dos.pnl.mean() * 100:+.2f} c (n {len(dos)}, coste medio {dos.cost.mean():.2f} $) "
                 f"| solo una pata cotizada {por[por.n == 1].pnl.mean() * 100:+.2f} c (n {int((por.n == 1).sum())})")
    return L


def informe(out, dias, log=print, des_fn=None):
    import pandas as pd
    U = cargar_unidades(dias, out)
    if U is None:
        return "Sin cachés de unidades: nada que informar.", {}
    dias_ok = sorted(U.dia.unique())
    d_desc = [d for d in dias_ok if d in DESC]
    d_oos = [d for d in dias_ok if d in OOS]
    tot = len(U)
    inc = int((U.completo == 0).sum())
    sin_des = int(U.des.isna().sum())
    Uc = U[(U.completo == 1) & U.des.notna()].copy()
    res = {"dias": dias_ok, "unidades_total": tot, "incompletas": inc, "sin_desenlace": sin_des}
    L = [f"H26 simulador maker en la banda barata | días con caché {dias_ok}", f"DESC={d_desc} OOS={d_oos}",
         f"Cobertura: {tot} unidades con orden (todos los motores) | incompletas (tramos) {inc} | sin desenlace {sin_des} (missing, no 0)",
         f"Diseño fijado: banda (0,10-0,30], T (60-300], puja {SH_BASE:g} acc, alta +{LAT_POST_MS} ms, cancelación +{LAT_CANCEL_MS} ms, "
         f"rellena solo si la operación atraviesa/iguala y supera la cola; EV de titular SIN rebate.", ""]
    # ---- calibración
    L.append("== 1. CALIBRACIÓN: población on-chain vs nuestro JOIN+C0 (mismos mercados completos y días) ==")
    for d in dias_ok[:2]:
        L.append("  comprobación de la réplica: " + comprobar_poblacion(d, out, des_fn))
    pob = cargar_poblacion(dias_ok, out, des_fn)
    for nombre, ds in (("DESC", d_desc), ("OOS", d_oos)):
        if ds:
            L.append(f" [{nombre} {ds[0]}..{ds[-1]}]")
            cl, cres = calibracion(Uc[Uc.dia.isin(ds)], pob, ds)
            L += cl
            res[f"calibracion_{nombre}"] = cres
            vc = veredicto_calibracion(cres)
            res[f"veredicto_calibracion_{nombre}"] = vc
            L.append(f"  VEREDICTO CALIBRACIÓN {nombre}: {vc['estado']}" + (
                f" | población 'final de la cola' {vc['ev_poblacion_final']:+.4f} frente al haz del simulador "
                f"[{vc['haz'][0]:+.4f}, {vc['haz'][1]:+.4f}] (CONS {vc['ev_join_cons']:+.4f}, OPT {vc['ev_join_opt']:+.4f}, tol {vc['tol']})"
                if "haz" in vc else ""))
            L += lineas_pares(Uc, ds)
    # ---- elección en DESC
    scopes = list(MONEDAS) + ["ALL"]
    sel = {}
    if d_desc:
        sel = elegir_desc(Uc[Uc.dia.isin(d_desc)], d_desc, scopes)
        L += ["", "== 2. ELECCIÓN EN DESC (cola CONS, SH=5; criterio: mayor EV/€ agrupado con rellenas >= "
              f"{MIN_FILL_COIN}/moneda, {MIN_FILL_ALL}/global) =="]
        for sc in scopes:
            mot, m, nc = sel[sc]
            L.append(f"  {sc:5} candidatas elegibles {nc:3d} -> " + (f"{mot}: " + fmt(m) if mot else "ninguna cumple el mínimo"))
        L.append(f"  multiplicidad: {sum(sel[s][2] for s in scopes)} (moneda x motor) comparaciones en total; el máximo de una rejilla "
                 "sobreestima: el juicio es el OOS")
        res["seleccion_desc"] = {sc: {"motor": sel[sc][0], "n_candidatas": sel[sc][2]} for sc in scopes}
    # ---- OOS del elegido
    if d_oos and sel:
        L += ["", f"== 3. OOS {d_oos[0]}..{d_oos[-1]} (juicio único del motor elegido en DESC, por moneda y global) =="]
        res["oos"] = {}
        for sc in scopes:
            mot = sel[sc][0]
            if not mot:
                L.append(f"  {sc:5} sin motor elegido")
                continue
            g = Uc[Uc.dia.isin(d_oos) & (Uc.motor == mot)]
            g = g if sc == "ALL" else g[g.act == sc]
            F = g[g.lleno > 0]
            m = metricas(F, total_dias=len(d_oos))
            gt = gates(m, len(d_oos))
            cap = g.cap_s.sum() / 86400.0 / max(1, len(d_oos))
            L.append(f"  {sc:5} {mot}: " + fmt(m) + f" | órdenes {len(g)} (pujas {int(g.norders.sum())}, canc. por capa {int(g.ncap.sum())}) "
                     f"| capital medio {cap:.2f} $")
            L.append("        gates: " + " ".join(f"{k}{'OK' if v else 'NO'}" for k, v in gt.items()))
            opt = mot.replace("|CONS|", "|OPT|") if mot.startswith("JOIN") else None
            if opt:
                go = Uc[Uc.dia.isin(d_oos) & (Uc.motor == opt)]
                go = go if sc == "ALL" else go[go.act == sc]
                L.append("        cota optimista de cola (OPT): " + fmt(metricas(go[go.lleno > 0], total_dias=len(d_oos))))
            res["oos"][sc] = {"motor": mot, "metricas": m, "gates": gt}
    # ---- placebo / inversión de las capas de defensa
    L += ["", "== 3b. PLACEBO e INVERSIÓN de las capas (alarmas desplazadas 30 min; Binance a favor). Una capa real vale algo solo si "
          "supera a las dos =="]
    for nombre, ds in (("DESC", d_desc), ("OOS", d_oos)):
        L += lineas_placebo(Uc, ds, nombre)
    # ---- referencias fijas (no elegidas) y capacidad
    L += ["", "== 4. REFERENCIAS FIJAS (descriptivo, NO para elegir): JOIN+C0 e IMPROVE+C0, DESC y OOS, por moneda =="]
    for mot in ("JOIN|C0|CONS|5", "JOIN|C0|OPT|5", "IMPROVE|C0|CONS|5"):
        for nombre, ds in (("DESC", d_desc), ("OOS", d_oos)):
            if not ds:
                continue
            g = Uc[Uc.dia.isin(ds) & (Uc.motor == mot)]
            L.append(f"  {mot} {nombre}: " + fmt(metricas(g[g.lleno > 0], total_dias=len(ds))))
            for sc in MONEDAS:
                gc = g[g.act == sc]
                L.append(f"      {sc:5}: " + fmt(metricas(gc[gc.lleno > 0], total_dias=len(ds))))
    cap_m = [m for m in sorted(Uc.motor.unique()) if not m.endswith("|5")]
    if cap_m:
        L += ["", "== 5. CAPACIDAD (JOIN/IMPROVE+C0, SH 25/50; todos los días) =="]
        for mot in cap_m:
            g = Uc[Uc.motor == mot]
            F = g[g.lleno > 0]
            enteras = int((F.lleno >= float(mot.split("|")[-1]) - 1e-9).sum())
            L.append(f"  {mot}: " + fmt(metricas(F, total_dias=len(dias_ok))) + f" | enteras {enteras}/{len(F)}")
    # ---- rejilla DESC completa a disco (descriptivo)
    tabla = tabla_motor(Uc[Uc.dia.isin(d_desc)], d_desc) if d_desc else []
    if tabla:
        pd.DataFrame([{k: (v if not isinstance(v, tuple) else v[0]) for k, v in r.items()} for r in tabla]).to_csv(
            out / "rejilla_desc_global.csv", index=False)
    L += ["", f"Cachés: {out} | comando: nice -n 19 ionice -c3 python3 {Path(__file__).name} --solo-informe"]
    return "\n".join(L), res


# ---------------------------------------------------------------- orquestación (manifiesto, log, reanudación idempotente)
def resumen_humo(d, filas, des, mo, universo, con_poblacion=True):
    """Resumen de una pasada recortada (sin caché): tabla por motor y, si hay on-chain, calibración contra la población."""
    import io
    import pandas as pd
    U = pd.read_csv(io.StringIO(CAB + "".join(fila_csv(r, des) for r in filas)), dtype={"mkt": str, "des": str})
    Uc = U[(U.completo == 1) & U.des.notna()]
    L = [f"== HUMO {d}: unidades con orden {len(U)}, completas con desenlace {len(Uc)} (universo de mercados completos {len(universo)}) =="]
    for mot, g in Uc.groupby("motor", sort=False):
        F = g[g.lleno > 0]
        m = metricas(F.assign(dia=d), total_dias=1)
        L.append(f"  {mot:30} órdenes {len(g):4d} pujas {int(g.norders.sum()):5d} canc.capa {int(g.ncap.sum()):4d} | "
                 + (f"rellenas {m['n_fill']:4d} EV/€ {m['ev']:+.3f} PnL {m['pnl']:+.2f}" if m["n_fill"] else "sin rellenos"))
    if con_poblacion and len(universo):
        tok = {tk: (m.coin, m.mkt, m.fin // 1000, m.lado) for tk, m in mo.meta.items() if m.mkt in set(universo)}
        C = poblacion_fills(d, tok)
        if C is not None and len(C):
            cl, _ = calibracion(Uc.assign(dia=d), {d: C}, [d])
            L += ["", "== calibración (humo) =="] + cl
    return "\n".join(L)


def mem_disponible_mb():
    try:
        for ln in open("/proc/meminfo"):
            if ln.startswith("MemAvailable"):
                return int(ln.split()[1]) / 1024.0
    except OSError:
        pass
    return float("inf")


def main():
    global LAMBDAS, C1_U, C1_W, FEED_MS
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default=",".join(DIAS))
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--solo-informe", action="store_true")
    ap.add_argument("--recorte-min", type=int, default=0, help="humo: solo los primeros N minutos del día (no cachea)")
    ap.add_argument("--max-lineas", type=int, default=0, help="humo: solo las primeras N líneas del registro (no cachea)")
    ap.add_argument("--max-lineas-ext", type=int, default=0, help="humo: líneas del registro 15m para x/bids de 15m")
    ap.add_argument("--capas", default="", help="lista separada por comas de capas a correr (por defecto todas)")
    ap.add_argument("--pols", default="JOIN,IMPROVE")
    ap.add_argument("--colas", default="CONS,OPT")
    ap.add_argument("--sh-cap", default="25,50", help="tamaños de capacidad (solo C0 x CONS); '' para ninguno")
    ap.add_argument("--cache-desenlaces", default="", help="humo: copia privada de la caché de desenlaces (no toca la compartida)")
    ap.add_argument("--forzar-horario", action="store_true")
    ap.add_argument("--exigir-calibracion", action="store_true",
                    help="tras escribir el informe, sale con código 4 si el veredicto de calibración no es PASA (parada del encargo)")
    ap.add_argument("--sin-placebo", action="store_true")
    ap.add_argument("--lambda-ms", default=str(LAT_CANCEL_MS),
                    help="Λ total (ms) alarma-recepción -> cancelación efectiva, lista (p. ej. 30,60,90,120,150,200,300); no se fija sin H26-MS")
    ap.add_argument("--c1-u", default=",".join(f"{x:g}" for x in C1_U), help="umbral k de la guarda Binance (bps), lista")
    ap.add_argument("--c1-w-ms", default=",".join(str(x) for x in C1_W), help="ventana W de la guarda Binance (ms), lista")
    ap.add_argument("--feed-ms", type=int, default=FEED_MS,
                    help="retraso modelado del feed del CLOB: casado = recepción del print − feed-ms (0 = recepción tal cual)")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    dias = [d for d in a.dias.split(",") if d]
    job = f"m5_maker_banda_{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}"
    logf = out / f"{job}.log"

    def log(msg):
        ln = f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S}Z {msg}"
        print(ln, flush=True)
        with open(logf, "a") as fh:
            fh.write(ln + "\n")

    if a.cache_desenlaces:
        import analisis_maker_cancelacion_binance as AM
        AM.CACHE = Path(a.cache_desenlaces)
        AM.TOKENS_CACHE = Path(a.cache_desenlaces + ".tokens")
    LAMBDAS = tuple(int(x) for x in a.lambda_ms.split(",") if x)
    C1_U = tuple(float(x) for x in a.c1_u.split(",") if x)
    C1_W = tuple(int(x) for x in a.c1_w_ms.split(",") if x)
    FEED_MS = a.feed_ms
    sh_cap = tuple(float(x) for x in a.sh_cap.split(",") if x)
    engines = construir_motores(tuple(a.pols.split(",")), tuple(a.colas.split(",")), sh_cap,
                                set(a.capas.split(",")) if a.capas else None, placebo=not a.sin_placebo)
    ph = params_hash(engines)
    man = {"job_id": job, "script": str(Path(__file__).resolve()), "script_sha256": sha_codigo(), "params": params_dict(engines),
           "params_hash": ph, "dias_previstos": dias, "inicio": datetime.now(timezone.utc).isoformat(), "estado": "EN_CURSO",
           "entradas": {}, "dias": {}, "comando": " ".join(sys.argv)}
    for d in dias:
        man["entradas"][d] = {}
        for nom, f in (("m5_registro", VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"),
                       ("m15_registro", VOL / "m15_registro" / f"m15_registro_{d}.csv.gz"),
                       ("m5_onchain", VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz")):
            man["entradas"][d][nom] = ({"bytes": f.stat().st_size, "mtime": f.stat().st_mtime} if f.exists() else None)

    def guarda_manifiesto():
        txt_m = json.dumps(man, indent=1, default=str)
        escribir_atomico(out / "run_manifest.json", txt_m)
        escribir_atomico(out / f"run_manifest_{job}.json", txt_m)          # una copia por trabajo: la fase 1 y la 2 no se pisan

    guarda_manifiesto()
    if a.solo_informe:
        txt, res = informe(out, dias, log)
        escribir_atomico(out / "informe.txt", txt + "\n")
        escribir_atomico(out / "informe.json", json.dumps(res, indent=1, default=str))
        print(txt)
        return 0
    pesado = not (a.recorte_min or a.max_lineas)
    ahora = datetime.now(timezone.utc)
    if pesado and 6 <= ahora.hour < 9 and not a.forzar_horario:
        man.update({"estado": "BLOCKED", "motivo": "06:00-09:00Z: no se lanza el trabajo pesado"})
        guarda_manifiesto()
        log("BLOCKED: franja 06:00-09:00Z")
        return 3
    if mem_disponible_mb() < 1500:
        man.update({"estado": "BLOCKED", "motivo": f"MemAvailable {mem_disponible_mb():.0f} MB < 1500"})
        guarda_manifiesto()
        log("BLOCKED: memoria disponible insuficiente")
        return 3
    log(f"inicio {job}: {len(dias)} días, {len(engines)} motores, hash código {man['script_sha256'][:12]}, params {ph}")
    errores = 0
    for d in dias:
        try:
            m = None if (a.recorte_min or a.max_lineas) else cache_valida(out, d, ph)
            if m:
                man["dias"][d] = {"estado": "SALTADO_CACHE_VALIDA", "filas": m["filas"], "cobertura_des": m["cobertura_des"]}
                log(f"{d}: caché válida ({m['filas']} filas, cobertura {m['cobertura_des']:.1%}): se salta")
                guarda_manifiesto()
                continue
            r = correr_dia(d, engines, out, a, log)
            est = r[0]
            man["dias"][d] = {k: est.get(k) for k in ("estado", "filas", "unidades_incompletas", "mercados_universo", "cobertura_des",
                                                      "cobertura_des_universo", "lineas", "tramos", "segundos", "contadores")}
            log(f"{d}: {est['estado']} | {est.get('filas')} unidades con orden, incompletas {est.get('unidades_incompletas')}, "
                f"tramos {len(est.get('tramos', []))}, cobertura des {est.get('cobertura_des', 0):.1%}, "
                f"{est.get('segundos')} s | {est.get('contadores')}")
            if est["estado"] == "HUMO_NO_CACHEADO":
                print(resumen_humo(d, r[1], r[2], r[3], r[4]))
            if est["estado"] == "COMPLETO":
                txt, _ = informe(out, [x for x in dias if (out / f'unidades_{x}.csv.gz').exists()], log)
                escribir_atomico(out / "resumen_parcial.txt", txt + "\n")
        except Exception as e:                                           # nunca queda "terminado" sin informe
            errores += 1
            man["dias"][d] = {"estado": "FALLO", "error": f"{type(e).__name__}: {e}"}
            log(f"{d}: FALLO {type(e).__name__}: {e}")
        guarda_manifiesto()
    ok = [d for d in dias if man["dias"].get(d, {}).get("estado") in ("COMPLETO", "SALTADO_CACHE_VALIDA")]
    if not pesado:
        man["estado"] = "HUMO"
    elif len(ok) == len(dias):
        man["estado"] = "COMPLETE"
    elif ok:
        man["estado"] = "PARTIAL"
    else:
        man["estado"] = "FAILED" if errores else "BLOCKED"
    man["fin"] = datetime.now(timezone.utc).isoformat()
    guarda_manifiesto()
    if ok and pesado:
        txt, res = informe(out, ok, log)
        escribir_atomico(out / "informe.txt", txt + "\n")
        escribir_atomico(out / "informe.json", json.dumps(res, indent=1, default=str))
        log("informe final escrito")
        vcs = {k: v for k, v in res.items() if k.startswith("veredicto_calibracion_")}
        escribir_atomico(out / "veredicto_calibracion.json", json.dumps(vcs, indent=1, default=str))
        log(f"veredicto calibración: { {k[len('veredicto_calibracion_'):]: v['estado'] for k, v in vcs.items()} }")
        if a.exigir_calibracion and (not vcs or any(v["estado"] != "PASA" for v in vcs.values())):
            man.update({"estado": "PARADA_CALIBRACION" if pesado else man["estado"]})
            guarda_manifiesto()
            log("PARADA: la calibración contra la población H5M no PASA; el simulador no se considera fiable")
            return 4
    log(f"ESTADO FINAL: {man['estado']} (válidos {len(ok)}/{len(dias)}: {ok}; fallos {errores})")
    return 0 if man["estado"] in ("COMPLETE", "HUMO") else 1


if __name__ == "__main__":
    sys.exit(main())
