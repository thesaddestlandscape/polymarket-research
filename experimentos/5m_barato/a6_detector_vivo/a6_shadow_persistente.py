#!/usr/bin/env python3
"""a6_shadow_persistente.py -- A6 / H43 R5K: shadow PERSISTENTE «habría puesto» (misión 5m barato; solo BTC 5m).

SOLO OBSERVA: canal público de mercado del CLOB (WS, lectura), gamma-api pública para el desenlace oficial. Sin órdenes,
sin claves, sin endpoints privados, sin importar nada de producción. No filtra por régimen: registra SIEMPRE ambos (H50 se
evalúa después, con las filas).

Regla H43 (CONGELADA 17-Oct, se importa de detector_r5k / h43_unidades, no se retoca):
  unidad = (mercado, lado s); cum_banda(s) = acciones adquiridas por MAKERS de s con precio equivalente en (0,10; 0,30] y T en
  (60, 300] s, por RECEPCIÓN local (nunca el timestamp del mensaje). Con cum_banda(s) >= 5000 y T en (60, 270]: puja maker
  post-only de TAM=50 acciones al MEJOR BID de s (debe estar en banda, libro no cruzado). Se cancela en T=60.

Por cada unidad que cruza se escribe (jsonl.gz diario en --salida, ver ESQUEMA):
  puesto     decisión: puja, ask, profundidad del nivel, T, cum, hora de recepción Y de exchange, régimen H50 (I = EV
             ponderado por € de la población BTC con cierre en [t-6h, t-60s] ya resuelta y con feed completo; null si no hay base)
  descarte   cruce que NO llega a puja (sin_snapshot/datos_viejos/sin_bid/libro_cruzado/bid_fuera_banda/tarde) -> contabilidad completa
  relleno    relleno SIMULADO de la puja por colas: opt (delante 0), base (0,5 x profundidad del nivel), cons (1,0 x profundidad)
  markout    bid/ask/mid de s a +5/+30/+120 s por recepción, desde la decisión y desde el 1er relleno de cada cola; null con motivo
             si cae tras el cierre o sin libro vivo (missing != 0)
  mercado_fin  cierre de la vigilancia: cobertura (completo/huecos), población de banda por lado, resumen de pujas
  desenlace  resolución oficial (gamma, closed=true) + pnl de cada cola y de la población; ganador null = sin resolver (cuenta como missing)
  latido     estado del proceso cada 10 min (cobertura, motivos, RSS)
Reinicio seguro e idempotente: el ESTADO ES EL PROPIO LOG (al arrancar se releen las filas de los últimos días: claves `k`
ya emitidas no se repiten; mercados con mercado_fin no se revigilan; desenlaces pendientes se reanudan). Un mercado que el
proceso encuentra a medias (arranque tarde) queda `completo=false`.

Supuestos de la cola (explícitos, SIN calibrar: H47 los calibrará): el relleno solo cuenta operaciones recibidas >= decisión + L_ALTA_MS;
una operación a precio < puja barre el nivel y rellena todo lo que queda; a precio == puja consume primero lo de delante.
Comisión maker 0 y rebate NO incluido (consistente con la población de H43). Profundidad del nivel solo de los bids del token s.
Uso:
  nice -n 19 .venv/bin/python -I experimentos/5m_barato/a6_detector_vivo/a6_shadow_persistente.py [--salida DIR]
  --resolver-solo   un pase del resolvedor sobre los pendientes y salir (apto para cron)
  --resumen [DIR]   recuento de filas por tipo y día
  --minutos N --offset-prueba X --salida DIR   SOLO prueba de humo (filas marcadas `prueba`; prohibido con la salida por defecto)
"""
import argparse
import asyncio
import glob
import gzip
import json
import os
import queue
import resource
import signal
import sys
import threading
import time
import zlib
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "h43_unidades"))
import detector_r5k as D  # noqa: E402
from detector_r5k import DetectorR5K, normalizar, BANDA_LO, BANDA_HI, T_MIN, T_MAX  # noqa: E402
import h43_unidades as H  # noqa: E402

# La definición de la regla vive en UN sitio: si divergen detector y h43_unidades el proceso no arranca (fail-loud).
assert (D.OFFSET, D.K, D.T_MIN, D.T_COS_MAX) == (H.OFFSET, H.K, H.T_MIN, H.T_MAX), "detector_r5k y h43_unidades divergen"

VERSION = 1
SALIDA_DEFECTO = "/root/polymarket-research-datalogs/a6_shadow"
GAMMA = "https://gamma-api.polymarket.com"
WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"

TAM = 50.0                       # acciones de la puja (H43: «≤50 acciones»)
T_ENTRADA_MAX = D.T_COS_MAX      # 270 s
L_ALTA_MS = 85                   # alta visible de una GTC post-only (F1 15-Oct: acuse 84 ms); las operaciones anteriores no cuentan
COLAS = {"opt": 0.0, "base": 0.5, "cons": 1.0}        # fracción de la profundidad del nivel que está DELANTE de nosotros
HORIZ_S = (5, 30, 120)
FRESCO_MS = 3000                 # fail-closed: sin mensaje en la conexión desde hace > 3 s -> no se decide
VENTANA_I_S, GUARDA_I_S = 6 * 3600, 60
MIN_MKTS_BASE = 12               # elección de este agente (H50 no la fija): con menos mercados resueltos en la base, regimen = null
ANTES_S = 310                    # se suscribe 310 s antes del cierre (la banda empieza en T=300)
GIVE_UP_DES_S = 6 * 3600
RETENCION_DIAS = 14
RELEER_DIAS = 3
EPS = 1e-9


def ahora_ms():
    return time.time_ns() // 1_000_000


def _r(x, n=4):
    return None if x is None else round(x, n)


def _dia(ms):
    return datetime.fromtimestamp(ms / 1000.0, timezone.utc).strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------------------------------------------------
class Orden:
    __slots__ = ("uid", "mkt", "lado", "token", "puja", "cierre", "r_dec", "t_ready", "ahead", "rest", "fills", "activa")

    def __init__(self, uid, mkt, lado, token, puja, cierre, r_dec, depth):
        self.uid, self.mkt, self.lado, self.token, self.puja, self.cierre = uid, mkt, lado, token, puja, cierre
        self.r_dec, self.t_ready = r_dec, r_dec + L_ALTA_MS
        self.ahead = {e: f * depth for e, f in COLAS.items()}
        self.rest = {e: TAM for e in COLAS}
        self.fills = {e: [] for e in COLAS}                 # esc -> [(recv_ms, acc)]
        self.activa = True

    def aplicar(self, pc, acc, recv_ms):
        """Operación del tomador que adquiere el lado s a pc (maker). Devuelve los escenarios que tuvieron su 1er relleno."""
        primeros = []
        if recv_ms < self.t_ready or pc > self.puja + EPS:
            return primeros
        barre = pc < self.puja - EPS
        for e in COLAS:
            if self.rest[e] <= EPS:
                continue
            if barre:
                self.ahead[e] = 0.0
                f = self.rest[e]                            # el nivel de la puja se agotó antes de llegar al precio inferior
            else:
                usado = min(acc, self.ahead[e])
                self.ahead[e] -= usado
                f = min(acc - usado, self.rest[e])
            if f > EPS:
                if not self.fills[e]:
                    primeros.append(e)
                self.fills[e].append((recv_ms, f))
                self.rest[e] -= f
        return primeros

    def resumen(self):
        out = {}
        for e in COLAS:
            fl = self.fills[e]
            out[e] = {"acc": _r(sum(a for _, a in fl), 4), "n": len(fl), "t1": fl[0][0] if fl else None,
                      "tn": fl[-1][0] if fl else None, "completa": self.rest[e] <= EPS}
        return out


class Mercado:
    __slots__ = ("mkt", "cierre", "tok", "lado_de", "bids", "best", "vivo", "ult_msg", "armados", "ordenes", "pop", "n_trades",
                 "reconex", "arranque_tarde", "cerrado", "descartes", "ult_book")

    def __init__(self, mkt, up, down, cierre):
        self.mkt, self.cierre = mkt, cierre
        self.tok = {"YES": up, "NO": down}
        self.lado_de = {up: "YES", down: "NO"}
        self.bids = {up: {}, down: {}}
        self.best = {up: (None, None), down: (None, None)}  # token -> (best_bid campo, best_ask campo) del último mensaje
        self.vivo = {up: False, down: False}                # True solo tras un snapshot completo desde la última (re)conexión
        self.ult_msg = 0
        self.armados = {}                                   # lado -> info del cruce, pendiente de decisión
        self.ordenes = {}                                   # lado -> Orden
        self.pop = {"YES": [0.0, 0.0], "NO": [0.0, 0.0]}    # lado -> [acciones, coste] de la población (T in (60,270])
        self.n_trades = self.reconex = 0
        self.arranque_tarde = False
        self.cerrado = False
        self.descartes = []
        self.ult_book = {up: 0, down: 0}


class Nucleo:
    """Lógica pura: sin red, sin disco (la salida es un callable). Se alimenta con eventos y la hora de RECEPCIÓN en ms."""

    def __init__(self, salida, emitidos=None, records=None, offset=D.OFFSET, prueba=None):
        self.salida = salida
        self.emitidos = emitidos if emitidos is not None else set()
        self.records = records if records is not None else {}    # mkt -> {cierre, completo, pop, ordenes, ganador, des_emitido}
        self.det = DetectorR5K(guardar_filas=True, max_edad_s=900, offset=offset)
        self.prueba = prueba
        self.mk = {}                                        # mkt -> Mercado
        self.tk = {}                                        # token -> Mercado
        self.markouts = []                                  # [(due_ms, uid, ancla, h, mkt, lado, tok)] ordenado por due
        self.next_ms = 0
        self.stats = Counter()

    # -- emisión idempotente ---------------------------------------------------------------------------------------
    def emit(self, row):
        k = row["k"]
        if k in self.emitidos:
            self.stats["duplicado_evitado"] += 1
            return False
        self.emitidos.add(k)
        row["v"] = VERSION
        if self.prueba is not None:
            row["prueba"] = self.prueba
        self.salida(row)
        return True

    # -- ciclo de vida del mercado -------------------------------------------------------------------------------------
    def nuevo_mercado(self, mkt, up, down, cierre, t_ms):
        m = Mercado(str(mkt), up, down, float(cierre))
        self.mk[m.mkt] = m
        self.tk[up] = self.tk[down] = m
        self.det.alta(up, m.mkt, "YES", cierre)
        self.det.alta(down, m.mkt, "NO", cierre)
        ini = (cierre - ANTES_S - 20) * 1000                # hueco desde antes de suscribir hasta el 1er snapshot
        for t in (up, down):
            self.det.on_gap(t, min(ini, t_ms))
        m.arranque_tarde = t_ms > (cierre - T_MAX) * 1000   # la banda ya empezó: cum parcial (cota inferior)
        return m

    def on_gap(self, mkt, t_ms, motivo=None):
        """Caída de la conexión: libros no vivos hasta el próximo snapshot, hueco para el detector (cum = cota inferior)."""
        m = self.mk.get(mkt)
        if m is None:
            return
        m.reconex += 1
        self.emit({"k": f"gap|{mkt}|{t_ms}", "tipo": "gap", "mkt": mkt, "r": t_ms, "T": _r(m.cierre - t_ms / 1000.0, 2),
                   "motivo": (motivo or "")[:80]})
        for t in m.tok.values():
            m.vivo[t] = False
            m.bids[t] = {}
            m.best[t] = (None, None)
            self.det.on_gap(t, t_ms)

    def cerrar_mercado(self, mkt, t_ms, abortado=False):
        m = self.mk.get(mkt)
        if m is None or m.cerrado:
            return
        m.cerrado = True
        self._tick(t_ms, forzar=True)
        for lado, info in list(m.armados.items()):           # armado sin decisión al cerrar
            self._descartar(m, lado, "tarde" if not abortado else "abortado", t_ms, info)
        for o in m.ordenes.values():
            if o.activa:
                self._expirar(o, t_ms)
        comp = self.det.completo(m.mkt, m.cierre)
        ordenes = {o.uid: {"lado": o.lado, "puja": o.puja, "rell": o.resumen()} for o in m.ordenes.values()}
        pop = {l: {"acc": _r(a, 4), "c": _r(c, 5)} for l, (a, c) in m.pop.items()}
        self.emit({"k": f"fin|{m.mkt}", "tipo": "mercado_fin", "mkt": m.mkt, "cierre": m.cierre, "r": t_ms, "completo": comp,
                   "arranque_tarde": m.arranque_tarde, "abortado": abortado, "reconex": m.reconex, "n_trades": m.n_trades,
                   "huecos_ms": ([[a, b] for a, b in self.det.huecos.get(m.mkt, [])]
                                 + [[ini, None] for tk, ini in self.det._abierto.items() if tk in m.lado_de])[:20],
                   "pop": pop, "ordenes": ordenes, "descartes": m.descartes})
        self.records[m.mkt] = {"cierre": m.cierre, "completo": comp, "pop": pop, "ordenes": ordenes, "ganador": None,
                               "des_emitido": False}
        self.stats["mercados_completos" if comp else "mercados_incompletos"] += 1
        for t in m.tok.values():
            self.tk.pop(t, None)
        self.mk.pop(m.mkt, None)
        self.markouts = [x for x in self.markouts if x[4] != m.mkt]

    # -- libro ----------------------------------------------------------------------------------------------------------
    def on_book(self, token, t_ms, bids, asks):
        m = self.tk.get(token)
        if m is None:
            return
        self._tick(t_ms)
        m.bids[token] = {float(b["price"]): float(b["size"]) for b in bids or [] if float(b["size"]) > 0}
        ba = min((float(a["price"]) for a in asks or [] if float(a["size"]) > 0), default=None)
        bb = max(m.bids[token], default=None)
        m.best[token] = (bb, ba)
        m.vivo[token] = True
        m.ult_msg = t_ms
        m.ult_book[token] = t_ms
        self.det.on_snapshot(token, t_ms)

    def on_price_change(self, t_ms, entries):
        self._tick(t_ms)                                    # ANTES de aplicar: los markouts miran el estado «a la hora t»
        for e in entries:
            tk = e.get("asset_id")
            m = self.tk.get(tk)
            if m is None:
                continue
            m.ult_msg = t_ms
            if e.get("side") == "BUY":
                try:
                    p, s = float(e["price"]), float(e.get("size") or 0)
                except (KeyError, TypeError, ValueError):
                    self.stats["pc_ilegible"] += 1
                    continue
                if s <= 0:
                    m.bids[tk].pop(p, None)
                else:
                    m.bids[tk][p] = s
            try:
                bb = float(e["best_bid"]) if e.get("best_bid") not in (None, "") else None
                ba = float(e["best_ask"]) if e.get("best_ask") not in (None, "") else None
            except (TypeError, ValueError):
                continue
            m.best[tk] = (bb, ba)

    def _top(self, m, tk):
        """(bid, ask) de token tk: bid del diccionario mantenido (profundidad), ask del campo best_ask. None = sin dato."""
        bb = max((p for p, s in m.bids[tk].items() if s > 0), default=None)
        fb, fa = m.best[tk]
        if fb is not None and bb is not None and abs(fb - bb) > 1e-9:
            self.stats["top_incoherente"] += 1
        return bb, fa

    # -- operaciones ------------------------------------------------------------------------------------------------------
    def on_trade(self, token, t_ms, msg):
        m = self.tk.get(token)
        if m is None:
            return
        self._tick(t_ms)
        m.ult_msg = t_ms
        m.n_trades += 1
        try:
            precio, size, side = float(msg["price"]), float(msg.get("size") or 0), msg.get("side")
        except (KeyError, TypeError, ValueError):
            self.stats["trade_ilegible"] += 1
            return
        e_ms = _entero(msg.get("timestamp"))
        eventos = self.det.on_trade(token, t_ms, precio, side, size)
        filas, self.det.filas = self.det.filas, []
        self.det.cruces.clear()
        for (_ts, mkt, lado_c, acc, coste, T, _pc, _recv) in filas:
            if T <= T_ENTRADA_MAX:                          # población = (60,270] (misma que wf.py/h43_unidades)
                m.pop[lado_c][0] += acc
                m.pop[lado_c][1] += coste
        n = normalizar(m.lado_de[token], side, precio, size)
        if n is not None and m.ordenes:
            lado_c, pc, acc, _c = n
            o = m.ordenes.get(lado_c)
            T = m.cierre - t_ms / 1000.0
            if o is not None and o.activa and T > T_MIN:
                for esc in o.aplicar(pc, acc, t_ms):
                    for h in HORIZ_S:
                        self._programar(t_ms + h * 1000, o, f"relleno_{esc}", h, t_ms)
        for ev in eventos:
            if ev["evento"] == "cruce" and ev["lado"] not in m.armados and ev["lado"] not in m.ordenes:
                m.armados[ev["lado"]] = {"r_cruce": t_ms, "e_cruce": e_ms, "T_cruce": ev["T"], "cum_cruce": ev["cum"],
                                         "completo_cruce": ev["completo"]}
                self.stats["cruces"] += 1
                self.next_ms = 0
        self._decidir(m, t_ms, e_ms)

    # -- decisión ------------------------------------------------------------------------------------------------------------
    def _decidir(self, m, t_ms, e_ms=None):
        T = m.cierre - t_ms / 1000.0
        for lado in list(m.armados):
            info = m.armados[lado]
            if T > T_ENTRADA_MAX:
                continue                                    # esperar a T<=270
            if T <= T_MIN:
                self._descartar(m, lado, "tarde", t_ms, info)
                continue
            tk = m.tok[lado]
            if not m.vivo[tk]:
                self._descartar(m, lado, "sin_snapshot", t_ms, info)
                continue
            if t_ms - m.ult_msg > FRESCO_MS:
                self._descartar(m, lado, "datos_viejos", t_ms, info)
                continue
            bb, ba = self._top(m, tk)
            tko = m.tok["NO" if lado == "YES" else "YES"]
            bbo = self._top(m, tko)[0] if m.vivo[tko] else None
            if bb is None:
                self._descartar(m, lado, "sin_bid", t_ms, info)
                continue
            if (ba is not None and bb >= ba - EPS) or (bbo is not None and bb + bbo > 1.0 + EPS):
                self._descartar(m, lado, "libro_cruzado", t_ms, info, bb=bb, ba=ba)
                continue
            if not (BANDA_LO < bb <= BANDA_HI):
                self._descartar(m, lado, "bid_fuera_banda", t_ms, info, bb=bb, ba=ba)
                continue
            self._poner(m, lado, tk, bb, ba, t_ms, e_ms, info, T)

    def _poner(self, m, lado, tk, bb, ba, t_ms, e_ms, info, T):
        uid = f"{m.mkt}:{lado}"
        del m.armados[lado]
        if f"puesto|{uid}" in self.emitidos:                # reinicio: la unidad ya se registró en una vida anterior
            self.stats["duplicado_evitado"] += 1
            return
        depth = m.bids[tk].get(bb, 0.0)
        reg = self.regimen(t_ms)
        o = Orden(uid, m.mkt, lado, tk, bb, m.cierre, t_ms, depth)
        m.ordenes[lado] = o
        self.next_ms = 0                                    # recalcular vencimientos (expiración de la puja)
        self.emit({"k": f"puesto|{uid}", "tipo": "puesto", "uid": uid, "mkt": m.mkt, "lado": lado, "token": tk,
                   "cierre": m.cierre, "r": t_ms, "e": e_ms, "T": _r(T, 3), "puja": bb, "ask": ba, "tam": TAM,
                   "depth_nivel": _r(depth, 3), "spread": _r(ba - bb, 4) if ba is not None else None,
                   "r_cruce": info["r_cruce"], "e_cruce": info["e_cruce"], "T_cruce": info["T_cruce"],
                   "cum_cruce": _r(info["cum_cruce"], 3), "cum_dec": _r(self.det.cum.get((m.mkt, lado), 0.0), 3),
                   "completo_cruce": info["completo_cruce"], "completo_dec": self.det.completo(m.mkt, m.cierre, t_ms),
                   "arranque_tarde": m.arranque_tarde, "t_ready": o.t_ready, "L_ms": L_ALTA_MS,
                   "colas": {e: _r(a, 3) for e, a in o.ahead.items()}, **reg})
        self.stats["puestos"] += 1
        for h in HORIZ_S:
            self._programar(t_ms + h * 1000, o, "decision", h, t_ms)

    def _descartar(self, m, lado, motivo, t_ms, info, bb=None, ba=None):
        m.armados.pop(lado, None)
        uid = f"{m.mkt}:{lado}"
        if self.emit({"k": f"descarte|{uid}", "tipo": "descarte", "uid": uid, "mkt": m.mkt, "lado": lado, "motivo": motivo,
                      "cierre": m.cierre, "r": t_ms, "T": _r(m.cierre - t_ms / 1000.0, 3), "bid": bb, "ask": ba,
                      "r_cruce": info["r_cruce"], "cum_cruce": _r(info["cum_cruce"], 3), "completo_cruce": info["completo_cruce"]}):
            m.descartes.append([lado, motivo])
            self.stats[f"descarte_{motivo}"] += 1

    # -- régimen H50 -------------------------------------------------------------------------------------------------------
    def regimen(self, t_ms):
        """I = Σpnl/Σcoste de la población BTC de banda en los mercados con cierre en [t-6h, t-60s], resueltos y con feed completo."""
        lo, hi = t_ms / 1000.0 - VENTANA_I_S, t_ms / 1000.0 - GUARDA_I_S
        c = p = 0.0
        n = n_inc = n_sd = n_fills = 0
        for r in self.records.values():
            if not (lo <= r["cierre"] <= hi):
                continue
            if not r["completo"]:
                n_inc += 1
                continue
            g = r["ganador"]
            if g is None:
                n_sd += 1
                continue
            n += 1
            for lado, d in r["pop"].items():
                if d["acc"] and d["c"] is not None:
                    c += d["c"]
                    p += d["acc"] * (1.0 if g == lado else 0.0) - d["c"]
                    n_fills += 1
        I = (p / c) if c > 0 else None
        etiqueta = None
        if I is not None and n >= MIN_MKTS_BASE:
            etiqueta = "I_pos" if I > 0 else "I_nonpos"
        return {"I": _r(I, 5), "I_n_mkts": n, "I_n_lados": n_fills, "I_coste": _r(c, 3), "I_n_incompletos": n_inc,
                "I_n_sin_desenlace": n_sd, "regimen": etiqueta}

    # -- markouts ----------------------------------------------------------------------------------------------------------
    def _programar(self, due, o, ancla, h, t0):
        if due >= o.cierre * 1000:
            self.emit({"k": f"markout|{o.uid}|{ancla}|{h}", "tipo": "markout", "uid": o.uid, "ancla": ancla, "h": h,
                       "r": due, "r0": t0, "motivo": "post_cierre", "bid": None, "ask": None, "mid": None})
            return
        self.markouts.append((due, o.uid, ancla, h, o.mkt, o.lado, o.token, t0))
        self.markouts.sort(key=lambda x: x[0])
        self.next_ms = 0

    def _tick(self, t_ms, forzar=False):
        if t_ms < self.next_ms and not forzar:
            return
        # 1) markouts vencidos: estado «a la hora de vencimiento» (esta función se llama ANTES de aplicar el mensaje)
        while self.markouts and self.markouts[0][0] <= t_ms:
            due, uid, ancla, h, mkt, lado, tk, t0 = self.markouts.pop(0)
            m = self.mk.get(mkt)
            row = {"k": f"markout|{uid}|{ancla}|{h}", "tipo": "markout", "uid": uid, "ancla": ancla, "h": h, "r": t_ms,
                   "r0": t0, "due": due, "retraso_ms": t_ms - due}
            if m is None or not m.vivo[tk] or t_ms - m.ult_msg > FRESCO_MS:
                row.update(motivo="sin_libro", bid=None, ask=None, mid=None)
            else:
                bb, ba = self._top(m, tk)
                row.update(motivo=None, bid=bb, ask=ba, mid=_r((bb + ba) / 2, 5) if bb is not None and ba is not None else None,
                           edad_ms=t_ms - m.ult_msg)
            self.emit(row)
        # 2) decisiones pendientes y expiración de pujas
        for m in list(self.mk.values()):
            if m.armados:
                self._decidir(m, t_ms)
            for o in m.ordenes.values():
                if o.activa and m.cierre - t_ms / 1000.0 <= T_MIN:
                    self._expirar(o, t_ms)
        prox = [x[0] for x in self.markouts[:1]]
        for m in self.mk.values():
            if m.armados:
                prox.append(int((m.cierre - T_ENTRADA_MAX) * 1000) if m.cierre - t_ms / 1000.0 > T_ENTRADA_MAX else t_ms + 250)
            prox += [int((m.cierre - T_MIN) * 1000) for o in m.ordenes.values() if o.activa]
        self.next_ms = min(prox) if prox else t_ms + 250

    def _expirar(self, o, t_ms):
        if not o.activa:
            return
        o.activa = False
        res = o.resumen()
        for e in COLAS:
            self.emit({"k": f"relleno|{o.uid}|{e}", "tipo": "relleno", "uid": o.uid, "esc": e, "r": t_ms, **res[e],
                       "puja": o.puja})

    # -- desenlace ---------------------------------------------------------------------------------------------------------
    def pendientes_desenlace(self, ahora_s, espera_s=25):
        return [mk for mk, r in self.records.items() if not r["des_emitido"] and r["cierre"] + espera_s <= ahora_s]

    def on_desenlace(self, mkt, ganador, t_ms, motivo=None):
        r = self.records.get(mkt)
        if r is None or r["des_emitido"]:
            return False
        if ganador is not None:
            r["ganador"] = ganador
        pn = {}
        for uid, o in r["ordenes"].items():
            pn[uid] = {e: (None if ganador is None else _r(d["acc"] * ((1.0 if ganador == o["lado"] else 0.0) - o["puja"]), 5))
                       for e, d in o["rell"].items()}
        popp = {l: (None if ganador is None else _r(d["acc"] * (1.0 if ganador == l else 0.0) - (d["c"] or 0.0), 5))
                for l, d in r["pop"].items()}
        ok = self.emit({"k": f"des|{mkt}", "tipo": "desenlace", "mkt": mkt, "cierre": r["cierre"], "r": t_ms, "ganador": ganador,
                        "motivo": motivo, "pnl": pn, "pnl_pop": popp, "completo": r["completo"]})
        r["des_emitido"] = True
        return ok

    def podar(self, ahora_s):
        self.det.podar(ahora_s)
        viejos = [mk for mk, r in self.records.items() if r["cierre"] < ahora_s - 8 * 3600 and r["des_emitido"]]
        for mk in viejos:
            del self.records[mk]


def _limpia(o):
    if isinstance(o, float) and (o != o or o in (float("inf"), float("-inf"))):
        return None
    if isinstance(o, dict):
        return {k: _limpia(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_limpia(v) for v in o]
    return o


def _entero(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------------------------------------------------------------
# Disco: jsonl.gz diario (miembros gzip añadidos), retención, relectura tolerante
class Salida:
    def __init__(self, d):
        self.d = Path(d)
        self.d.mkdir(parents=True, exist_ok=True)
        self.q = queue.SimpleQueue()
        self.parar = threading.Event()
        self.hilo = threading.Thread(target=self._bucle, daemon=True, name="a6_escritor")
        self.hilo.start()

    def put(self, row):
        self.q.put_nowait(row)

    def _vaciar(self):
        por_dia = {}
        try:
            while True:
                row = self.q.get_nowait()
                try:
                    ln = json.dumps(row, separators=(",", ":"), allow_nan=False)
                except ValueError:                           # NaN/inf: se guarda como null (missing), nunca se pierde el lote
                    ln = json.dumps(_limpia(row), separators=(",", ":"), allow_nan=False)
                por_dia.setdefault(_dia(row.get("r") or ahora_ms()), []).append(ln)
        except queue.Empty:
            pass
        for dia, lineas in por_dia.items():
            blob = gzip.compress(("\n".join(lineas) + "\n").encode(), 6)
            with open(self.d / f"a6_shadow_{dia}.jsonl.gz", "ab") as f:
                f.write(blob)
                f.flush()
                os.fsync(f.fileno())

    def _bucle(self):
        while not self.parar.wait(5):
            try:
                self._vaciar()
            except Exception as e:                           # no matar el hilo: el reintento va con el siguiente ciclo
                print(f"{datetime.now(timezone.utc).isoformat()} escritor: {type(e).__name__}: {e}", file=sys.stderr, flush=True)

    def cerrar(self):
        self.parar.set()
        self.hilo.join(timeout=6)
        self._vaciar()


def leer_gz_tolerante(path):
    """Filas de un jsonl.gz con varios miembros; ignora un miembro final truncado o una línea corrupta."""
    try:
        data = open(path, "rb").read()
    except OSError:
        return
    while data:
        d = zlib.decompressobj(31)
        try:
            txt = d.decompress(data)
        except zlib.error:
            return
        for ln in txt.decode(errors="replace").splitlines():
            try:
                yield json.loads(ln)
            except ValueError:
                continue
        data = d.unused_data
        if not d.eof:
            return


def restaurar(dirn, ahora_s, dias=RELEER_DIAS):
    """Reconstruye (emitidos, records) desde los logs de los últimos `dias` días (el log es el estado)."""
    emitidos, records = set(), {}
    hoy = datetime.fromtimestamp(ahora_s, timezone.utc).date()
    for i in range(dias, -1, -1):
        f = Path(dirn) / f"a6_shadow_{(hoy - timedelta(days=i)).isoformat()}.jsonl.gz"
        if not f.exists():
            continue
        for row in leer_gz_tolerante(f):
            k = row.get("k")
            if k:
                emitidos.add(k)
            t = row.get("tipo")
            if t == "mercado_fin":
                records.setdefault(row["mkt"], {"cierre": row["cierre"], "completo": row["completo"], "pop": row["pop"],
                                                "ordenes": row["ordenes"], "ganador": None, "des_emitido": False})
            elif t == "desenlace" and row["mkt"] in records:
                records[row["mkt"]]["ganador"] = row.get("ganador")
                records[row["mkt"]]["des_emitido"] = True
    return emitidos, records


def aplicar_retencion(dirn, ahora_s, dias=RETENCION_DIAS):
    lim = (datetime.fromtimestamp(ahora_s, timezone.utc) - timedelta(days=dias)).strftime("%Y-%m-%d")
    borrados = []
    for f in glob.glob(str(Path(dirn) / "a6_shadow_*.jsonl.gz")):
        d = os.path.basename(f)[len("a6_shadow_"):-len(".jsonl.gz")]
        if len(d) == 10 and d < lim:
            os.remove(f)
            borrados.append(f)
    return borrados


# ---------------------------------------------------------------------------------------------------------------------
# Red (solo lectura)
def mercado_btc5(ini):
    import requests
    ev = requests.get(f"{GAMMA}/events", params={"slug": f"btc-updown-5m-{ini}"}, timeout=5).json()
    if not ev:
        return None
    m = ev[0]["markets"][0]
    out = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
    toks = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
    if [o.lower() for o in out] != ["up", "down"] or len(toks) != 2:
        raise ValueError(f"btc-updown-5m-{ini}: outcomes {out} inesperados (fail-closed)")
    return {"id": str(m["id"]), "up": toks[0], "down": toks[1]}


def desenlaces_gamma(mids):
    """{mkt: 'YES'|'NO'} de los resueltos (gamma, closed=true, outcomePrices >= 0,999). Ausente = sin resolver (missing)."""
    import requests
    res = {}
    for k in range(0, len(mids), 40):
        lote = mids[k:k + 40]
        r = requests.get(f"{GAMMA}/markets", timeout=20,
                         params=[("id", x) for x in lote] + [("closed", "true"), ("limit", "40")])
        r.raise_for_status()
        for m in r.json() or []:
            out = m.get("outcomes")
            out = json.loads(out) if isinstance(out, str) else out
            pr = m.get("outcomePrices")
            pr = json.loads(pr) if isinstance(pr, str) else pr
            if not out or [o.lower() for o in out] != ["up", "down"] or not pr or len(pr) != 2:
                continue
            if float(pr[0]) >= 0.999:
                res[str(m["id"])] = "YES"
            elif float(pr[1]) >= 0.999:
                res[str(m["id"])] = "NO"
    return res


async def vigilar(nuc, m_info, cierre, parar):
    import websockets
    mkt, up, down = m_info["id"], m_info["up"], m_info["down"]
    toks = [up, down]
    m = nuc.nuevo_mercado(mkt, up, down, cierre, ahora_ms())
    fin_ms = int(cierre * 1000) + 500
    abortado = True
    try:
        while ahora_ms() < fin_ms and not parar.is_set():
            try:
                async with websockets.connect(WS_URL, open_timeout=10, close_timeout=2, max_size=None, ping_interval=None) as ws:
                    await ws.send(json.dumps({"assets_ids": toks, "type": "market"}))

                    async def latido():
                        while True:
                            await asyncio.sleep(5.0)
                            await ws.send("PING")
                    tl = asyncio.create_task(latido())
                    try:
                        while ahora_ms() < fin_ms and not parar.is_set():
                            try:
                                raw = await asyncio.wait_for(ws.recv(), timeout=1.0)
                            except asyncio.TimeoutError:
                                nuc._tick(ahora_ms())
                                continue
                            t = ahora_ms()
                            if raw == "PONG" or not raw:
                                continue
                            try:
                                datos = json.loads(raw)
                            except ValueError:
                                continue
                            for msg in (datos if isinstance(datos, list) else [datos]):
                                if not isinstance(msg, dict):
                                    continue
                                et = msg.get("event_type")
                                try:
                                    if et == "price_change":
                                        nuc.on_price_change(t, msg.get("price_changes") or [])
                                    elif et == "last_trade_price" and msg.get("asset_id") in toks:
                                        nuc.on_trade(msg["asset_id"], t, msg)
                                    elif et == "book" and msg.get("asset_id") in toks:
                                        nuc.on_book(msg["asset_id"], t, msg.get("bids"), msg.get("asks"))
                                except Exception as e:       # un mensaje roto no tumba la conexión, pero se contabiliza
                                    nuc.stats["error_mensaje"] += 1
                                    if nuc.stats["error_mensaje"] in (1, 10, 100, 1000):
                                        nuc.emit({"k": f"error_msg|{t}", "tipo": "error", "r": t, "m": f"{et}: {type(e).__name__}: {str(e)[:80]}"})
                    finally:
                        tl.cancel()
            except asyncio.CancelledError:
                raise
            except Exception as e:
                nuc.on_gap(mkt, ahora_ms(), f"{type(e).__name__}: {e}")
                await asyncio.sleep(0.5)
        abortado = ahora_ms() < fin_ms - 400
    finally:
        nuc.cerrar_mercado(mkt, ahora_ms(), abortado=abortado)


async def resolvedor(nuc, parar, una_vez=False):
    loop = asyncio.get_running_loop()
    while not parar.is_set():
        pend = nuc.pendientes_desenlace(time.time())
        if pend:
            try:
                res = await loop.run_in_executor(None, desenlaces_gamma, pend)
            except Exception as e:
                nuc.stats["gamma_error"] += 1
                print(f"{datetime.now(timezone.utc).isoformat()} gamma desenlaces: {type(e).__name__}: {str(e)[:80]}", file=sys.stderr, flush=True)
                res = {}
            for mk in pend:
                if mk in res:
                    nuc.on_desenlace(mk, res[mk], ahora_ms())
                elif nuc.records[mk]["cierre"] + GIVE_UP_DES_S < time.time():
                    nuc.on_desenlace(mk, None, ahora_ms(), motivo="sin_resolver_6h")
        if una_vez:
            return
        for _ in range(20):
            if parar.is_set():
                return
            await asyncio.sleep(1.0)


def rss_mb():
    with open("/proc/self/status") as f:
        for ln in f:
            if ln.startswith("VmRSS"):
                return int(ln.split()[1]) / 1024.0
    return None


async def principal(args, out, nuc, parar):
    loop = asyncio.get_running_loop()
    lanzados, tareas, fallos = set(), [], {}
    t_fin = time.time() + args.minutos * 60 if args.minutos else None
    t_latido = t_ret = 0.0
    tareas_res = asyncio.create_task(resolvedor(nuc, parar))
    nuc.emit({"k": f"inicio|{ahora_ms()}", "tipo": "inicio", "r": ahora_ms(), "pid": os.getpid(), "minutos": args.minutos,
              "records": len(nuc.records), "emitidos": len(nuc.emitidos)})
    while not parar.is_set() and (t_fin is None or time.time() < t_fin):
        ahora = time.time()
        c = int(ahora // 300) * 300 + 300
        for cierre in (c, c + 300):
            if cierre in lanzados or ahora < cierre - ANTES_S or ahora >= cierre or fallos.get(cierre, (0, 0))[1] > ahora:
                continue
            try:
                info = await loop.run_in_executor(None, mercado_btc5, cierre - 300)
            except Exception as e:
                n = fallos.get(cierre, (0, 0))[0] + 1
                fallos[cierre] = (n, ahora + min(5 * n, 30))
                nuc.stats["gamma_mercado_error"] += 1
                if n in (1, 5, 20):
                    nuc.emit({"k": f"error|{cierre}|{n}", "tipo": "error", "r": ahora_ms(), "m": f"gamma {cierre}: {type(e).__name__}: {str(e)[:80]}"})
                continue
            if info is None:
                fallos[cierre] = (1, ahora + 5)
                continue
            lanzados.add(cierre)
            if f"fin|{info['id']}" in nuc.emitidos:           # ya vigilado en una vida anterior (idempotencia)
                continue
            tareas.append(asyncio.create_task(vigilar(nuc, info, cierre, parar)))
        tareas = [t for t in tareas if not t.done()]
        nuc.podar(time.time())
        if ahora - t_latido > 600:
            t_latido = ahora
            rss = rss_mb()
            nuc.emit({"k": f"latido|{ahora_ms()}", "tipo": "latido", "r": ahora_ms(), "rss_mb": _r(rss, 1), "vigilando": len(nuc.mk),
                      "records": len(nuc.records), "stats": dict(nuc.stats), "detector": dict(nuc.det.stats)})
            if rss and rss > 400:
                print(f"RSS {rss:.0f} MB > 400: salgo para que el watchdog reinicie", file=sys.stderr, flush=True)
                parar.set()
        if ahora - t_ret > 3600:
            t_ret = ahora
            aplicar_retencion(args.salida, ahora)
        await asyncio.sleep(1.0)
    parar.set()
    if tareas:
        await asyncio.gather(*tareas, return_exceptions=True)
    await tareas_res
    nuc.emit({"k": f"fin_proceso|{ahora_ms()}", "tipo": "fin_proceso", "r": ahora_ms(), "stats": dict(nuc.stats)})


def resumen(dirn):
    tot = Counter()
    for f in sorted(glob.glob(str(Path(dirn) / "a6_shadow_*.jsonl.gz"))):
        c = Counter(r.get("tipo") for r in leer_gz_tolerante(f))
        print(os.path.basename(f), dict(c))
        tot.update(c)
    print("TOTAL", dict(tot))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=SALIDA_DEFECTO)
    ap.add_argument("--minutos", type=float, default=None, help="SOLO prueba de humo (acotada)")
    ap.add_argument("--offset-prueba", type=float, default=None, help="SOLO prueba de humo: sustituye OFFSET=5000 (filas marcadas `prueba`)")
    ap.add_argument("--resolver-solo", action="store_true")
    ap.add_argument("--resumen", action="store_true")
    args = ap.parse_args()
    if args.resumen:
        resumen(args.salida)
        return 0
    if (args.offset_prueba is not None or args.minutos) and os.path.abspath(args.salida) == SALIDA_DEFECTO:
        sys.exit("las opciones de prueba exigen --salida distinta de la de producción (fail-closed)")
    try:
        resource.setrlimit(resource.RLIMIT_AS, (1_500_000_000, 1_500_000_000))
    except (ValueError, OSError):
        pass
    Path(args.salida).mkdir(parents=True, exist_ok=True)
    emitidos, records = restaurar(args.salida, time.time())
    out = Salida(args.salida)
    nuc = Nucleo(out.put, emitidos, records, offset=args.offset_prueba or D.OFFSET,
                 prueba=args.offset_prueba if args.offset_prueba is not None else None)
    parar = asyncio.Event()

    async def corre():
        loop = asyncio.get_running_loop()
        for s in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(s, parar.set)
        if args.resolver_solo:
            await resolvedor(nuc, parar, una_vez=True)
        else:
            await principal(args, out, nuc, parar)
    print(f"{datetime.now(timezone.utc).isoformat()} a6_shadow arrancando pid={os.getpid()} salida={args.salida} "
          f"records={len(records)} emitidos={len(emitidos)}", flush=True)
    try:
        asyncio.run(corre())
    finally:
        out.cerrar()
    print(f"{datetime.now(timezone.utc).isoformat()} a6_shadow terminado stats={dict(nuc.stats)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
