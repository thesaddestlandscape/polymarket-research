#!/usr/bin/env python3
"""h23_shadow.py -- H23-MAKER-V1 SHADOW persistente (DRY-RUN): «habria puesto / cancelado / rellenado» (misión 5m barato, solo BTC).

SOLO OBSERVA: WS publico del CLOB (lectura), gamma-api publica (desenlace oficial), CSV de PolyBolt (twap60 oficial). Sin órdenes, sin claves,
sin endpoints privados, sin importar nada de produccion. Regla: h23_regla.py (congelada; hash en cada fila `inicio`).

Por cada par BTC 5m/15m que cierra en C (C % 900 == 0), con lado s por TWAP60 oficial (ref15 = twap60(C-900), ref5 = twap60(C-300), |gap| >= 1 bp)
y para los DOS brazos (A umbral 0,05 · B umbral 0,02) y las dos variantes (join con cancelacion · nc = control SIN cancelar):
  puesto    segmento de puja: precio (= mejor bid del 5m lado s), profundidad del nivel, ask5, bid15, margen, T, hora de RECEPCION
  cancela   decision de cancelar y CAUSA (bid5_baja = desplome del bid / bid5_sube / cota_cae / margen / cruzado / sin_libro / gap / fin)
  relleno   al terminar el par, por escenario (cola opt|base|cons x latencia c|k): acciones, coste, n, T del 1er relleno; la puja no se rellena
            de forma optimista: solo cuentan operaciones recibidas >= decision + L_alta y < decision de cancelar + L_cancel
  markout   bid/ask/mid del 5m lado s a +5/+30/+120 s del 1er relleno (null con motivo si cae tras el cierre o sin libro; missing != 0)
  par       refs, lado, gap, retraso real de ref5 (la regla offline lo supone conocido a +1,5 s), motivos de no cotizar
  mercado_fin cobertura (completo/huecos/reconexiones), cotizaciones, ahorro de API (cuantas altas+bajas habria hecho)
  desenlace resolucion oficial (gamma, closed=true) + pnl por (brazo, var, escenario) con rebate 20 % (EV ponderado por € lo calcula h23_analisis.py)
  latido    estado del proceso cada 10 min
Escenarios: cola opt (0 delante) | base (0,5 x profundidad) | cons (1,0 x profundidad) -- calibracion_colas.md: base central, rango SIEMPRE [opt, cons];
latencia c = alta 79 / cancelacion 60 ms (central) | k = 254 / 150 ms (conservadora).
Reinicio seguro e idempotente: el ESTADO ES EL PROPIO LOG (claves `k` ya emitidas no se repiten; pares con `fin|` no se revigilan; desenlaces pendientes se
reanudan). Un par a medias al arrancar queda `completo=false`.
Salida: /root/polymarket-research-datalogs/h23_shadow/h23_shadow_YYYY-MM-DD.jsonl.gz (miembros gzip anadidos), retencion 14 d, fuera de git.
Uso:  nice -n 19 .venv/bin/python -I experimentos/5m_barato/h23_maker/h23_shadow.py [--salida DIR]
      --resolver-solo | --resumen | --minutos N --salida DIR (SOLO humo; prohibido con la salida por defecto)
"""
import argparse
import asyncio
import glob
import gzip
import json
import math
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
import h23_regla as R  # noqa: E402

VERSION = 1
SALIDA_DEFECTO = "/root/polymarket-research-datalogs/h23_shadow"
PRICES = Path("/root/polymarket-research/data/prices")
GAMMA = "https://gamma-api.polymarket.com"
WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
CFG = R.CONFIG
ANTES_S = 70                       # se suscribe 70 s antes de abrir el 5m (libro listo al abrir)
FRESCO_MS = 3000                   # sin mensaje en la conexion desde hace > 3 s -> sin vista -> se cancela (fail-closed)
HORIZ_S = (5, 30, 120)
RETENCION_DIAS, RELEER_DIAS, GIVE_UP_DES_S = 14, 3, 6 * 3600
EPS = 1e-9
LAT = {"c": (CFG["lat_post_ms"], CFG["lat_cancel_ms"]), "k": (CFG["lat_post_cons_ms"], CFG["lat_cancel_cons_ms"])}
ESCS = [f"{c}|{l}" for c in CFG["colas"] for l in LAT]
INF = float("inf")


def ahora_ms():
    return time.time_ns() // 1_000_000


def _r(x, n=4):
    return None if x is None else round(x, n)


def _dia(ms):
    return datetime.fromtimestamp(ms / 1000.0, timezone.utc).strftime("%Y-%m-%d")


def normalizar(lado_token, side, precio, size):
    """(lado_c, pc, acc): el MAKER adquiere lado_c a pc segun el lado del TOMADOR (identico a detector_r5k.normalizar)."""
    if size is None or size <= 0 or precio is None or not (0.0 < precio < 1.0):
        return None
    if side == "BUY":
        return ("NO" if lado_token == "YES" else "YES"), round(1.0 - precio, 4), size
    if side == "SELL":
        return lado_token, round(precio, 4), size
    return None


# ---------------------------------------------------------------------------------------------------------------------
class Libro:
    """L2 de un token (bids y asks), valido solo tras un snapshot desde la ultima (re)conexion."""
    __slots__ = ("bids", "asks", "vivo", "ult")

    def __init__(self):
        self.bids, self.asks, self.vivo, self.ult = {}, {}, False, 0

    def top(self):
        bb = max((p for p, s in self.bids.items() if s > 0), default=None)
        ba = min((p for p, s in self.asks.items() if s > 0), default=None)
        return bb, ba


class Trader:
    """Un brazo virtual (arm, var): segmentos de puja y relleno por escenario. var = join (cancela) | nc (control: no cancela)."""

    def __init__(self, arm, var, umbral):
        self.arm, self.var, self.umbral = arm, var, umbral
        self.segs = []                                   # {n, precio, depth, t_dec, t_can, causa, ahead{cola}, fills{esc}:[(t,acc)]}
        self.need = None
        self.lleno = {e: 0.0 for e in ESCS}
        self.coste = {e: 0.0 for e in ESCS}
        self.nfill = {e: 0 for e in ESCS}
        self.t1 = {e: None for e in ESCS}
        self.n_alta = self.n_baja = 0
        self.cur = None                                  # segmento vigente (sin decision de cancelar)
        self.parado = False                              # nc: tras el primer segmento no se vuelve a cotizar
        self.bloq = 0                                    # no se puede volver a pujar antes de esta hora (repost minimo tras cancelar)

    def activo(self, seg, esc, t):
        lp, lc = LAT[esc.split("|")[1]]
        return t >= seg["t_dec"] + lp and (seg["t_can"] is None or t < seg["t_can"] + lc)


class Par:
    __slots__ = ("c", "m5", "m15", "tok", "lib", "s", "tc", "to", "tco", "traders", "t_ini", "t_fin", "gap_bps", "ref", "ref5_rx",
                 "arranque_tarde", "reconex", "n_msgs", "motivos", "cerrado", "ult_msg", "pend_mark", "n_ev", "cuenta_cross")

    def __init__(self, c, m5, m15, t_ms):
        self.c, self.m5, self.m15 = c, m5, m15
        self.tok = {"5u": m5["up"], "5d": m5["down"], "15u": m15["up"], "15d": m15["down"]}
        self.lib = {t: Libro() for t in self.tok.values()}
        self.s = self.tc = self.to = self.tco = None
        self.traders = [Trader(a, v, u) for a, u in CFG["brazos"].items() for v in ("join", "join_r", "nc")]
        self.t_ini, self.t_fin = (c - 300) * 1000 + CFG["ref_conocible_ms"], (c - CFG["fin_margen_s"]) * 1000
        self.gap_bps = self.ref = self.ref5_rx = None
        self.arranque_tarde = t_ms > (c - 300) * 1000 + 5000
        self.reconex = self.n_msgs = 0
        self.motivos = Counter()
        self.cerrado = False
        self.ult_msg = 0
        self.pend_mark = []                              # [(due, arm, var, esc, h)]
        self.n_ev = 0


class Nucleo:
    """Logica pura: sin red, sin disco (salida = callable). Se alimenta con eventos y la hora de RECEPCION en ms."""

    def __init__(self, salida, emitidos=None, records=None, prueba=None):
        self.salida = salida
        self.emitidos = emitidos if emitidos is not None else set()
        self.records = records if records is not None else {}
        self.prueba = prueba
        self.pares = {}                                  # mkt5 -> Par
        self.tk = {}                                     # token -> Par
        self.stats = Counter()

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

    # -- ciclo de vida ----------------------------------------------------------------------------------------------
    def nuevo_par(self, c, m5, m15, t_ms):
        p = Par(c, m5, m15, t_ms)
        self.pares[m5["id"]] = p
        for t in p.tok.values():
            self.tk[t] = p
        return p

    def fijar_lado(self, p, ref15, ref5, t_ms, ts_fetcher=None):
        """Llega la referencia 5m: lado s por TWAP60 oficial. None -> par descartado (gap < minimo)."""
        p.ref = (ref15, ref5)
        p.gap_bps = (ref5 / ref15 - 1.0) * 1e4 if ref15 else None
        p.ref5_rx = t_ms
        s = R.lado_de_refs(ref15, ref5)
        fila = {"k": f"par|{p.m5['id']}", "tipo": "par", "mkt": p.m5["id"], "mkt15": p.m15["id"], "cierre": p.c, "r": t_ms, "ref15": ref15,
                "ref5": ref5, "gap_bps": _r(p.gap_bps, 3), "lado": s, "ref5_retraso_ms": t_ms - (p.c - 300) * 1000,
                "arranque_tarde": p.arranque_tarde}
        if s is None:
            fila["descartado"] = "gap<min"
            p.motivos["gap<min"] += 1
        else:
            p.s = s
            p.tc, p.to = (p.tok["5u"], p.tok["15u"]) if s == "Up" else (p.tok["5d"], p.tok["15d"])
        self.emit(fila)
        if s is not None:
            self.evaluar(p, t_ms)

    def sin_refs(self, p, t_ms):
        p.motivos["sin_ref"] += 1
        self.emit({"k": f"par|{p.m5['id']}", "tipo": "par", "mkt": p.m5["id"], "cierre": p.c, "r": t_ms, "lado": None,
                   "descartado": "sin_ref", "ref15": p.ref[0] if p.ref else None})

    def on_gap(self, p, t_ms, motivo=None):
        if p.cerrado:
            return
        p.reconex += 1
        self.emit({"k": f"gap|{p.m5['id']}|{t_ms}", "tipo": "gap", "mkt": p.m5["id"], "r": t_ms, "T": _r(p.c - t_ms / 1000.0, 2),
                   "motivo": (motivo or "")[:80]})
        for l in p.lib.values():
            l.bids, l.asks, l.vivo = {}, {}, False
        self.evaluar(p, t_ms, forzar_causa="gap")

    # -- libro --------------------------------------------------------------------------------------------------------
    def on_book(self, token, t_ms, bids, asks):
        p = self.tk.get(token)
        if p is None:
            return
        l = p.lib[token]
        l.bids = {float(b["price"]): float(b["size"]) for b in bids or [] if float(b["size"]) > 0}
        l.asks = {float(a["price"]): float(a["size"]) for a in asks or [] if float(a["size"]) > 0}
        l.vivo, l.ult, p.ult_msg = True, t_ms, t_ms
        p.n_msgs += 1
        self.evaluar(p, t_ms)

    def on_price_change(self, t_ms, entries):
        tocados = {}
        for e in entries:
            p = self.tk.get(e.get("asset_id"))
            if p is None:
                continue
            l = p.lib[e["asset_id"]]
            try:
                px, sz = float(e["price"]), float(e.get("size") or 0)
            except (KeyError, TypeError, ValueError):
                self.stats["pc_ilegible"] += 1
                continue
            lado = l.bids if e.get("side") == "BUY" else l.asks
            if sz <= 0:
                lado.pop(px, None)
            else:
                lado[px] = sz
            l.ult, p.ult_msg = t_ms, t_ms
            tocados[id(p)] = p
        for p in tocados.values():
            p.n_msgs += 1
            self.evaluar(p, t_ms)

    # -- operaciones: rellenos simulados -------------------------------------------------------------------------------
    def on_trade(self, token, t_ms, msg):
        p = self.tk.get(token)
        if p is None or p.s is None:
            return
        try:
            precio, size, side = float(msg["price"]), float(msg.get("size") or 0), msg.get("side")
        except (KeyError, TypeError, ValueError):
            self.stats["trade_ilegible"] += 1
            return
        if token not in (p.tok["5u"], p.tok["5d"]):
            return                                       # solo el 5m genera rellenos de nuestra puja
        lado_tok = "YES" if token == p.tok["5u"] else "NO"
        n = normalizar(lado_tok, side, precio, size)
        s_lado = "YES" if p.s == "Up" else "NO"
        if n is None or n[0] != s_lado:
            return
        _, pc, acc = n
        p.ult_msg = t_ms
        for tr in p.traders:
            if tr.need is None:
                continue
            for seg in tr.segs:
                for esc in ESCS:
                    if tr.lleno[esc] >= tr.need - EPS or not tr.activo(seg, esc, t_ms):
                        continue
                    cola = esc.split("|")[0]
                    falta = tr.need - tr.lleno[esc]
                    if pc < seg["precio"] - EPS:
                        x = falta                        # atraviesa nuestro nivel: barrido completo
                    elif abs(pc - seg["precio"]) < EPS:
                        tomo = min(seg["ahead"][cola], acc)
                        seg["ahead"][cola] -= tomo
                        x = min(falta, acc - tomo)
                    else:
                        x = 0.0
                    if x > EPS:
                        tr.lleno[esc] += x
                        tr.coste[esc] += x * seg["precio"]
                        tr.nfill[esc] += 1
                        seg["fills"].setdefault(esc, []).append((t_ms, round(x, 4)))
                        if tr.t1[esc] is None:
                            tr.t1[esc] = t_ms
                            for h in HORIZ_S:
                                self._marcar(p, t_ms + h * 1000, tr, esc, h, t_ms)

    # -- decision -----------------------------------------------------------------------------------------------------------
    def _top(self, p, tk):
        l = p.lib[tk]
        return l.top() if l.vivo else (None, None)

    def evaluar(self, p, t_ms, forzar_causa=None):
        if p.cerrado:
            return
        self._markouts(p, t_ms)
        if p.s is None:
            return
        fin = t_ms >= p.t_fin
        sin_vista = (t_ms - p.ult_msg > FRESCO_MS) or not (p.lib[p.tc].vivo and p.lib[p.to].vivo)
        b5, a5 = self._top(p, p.tc)
        b15, a15 = self._top(p, p.to)
        for tr in p.traders:
            if tr.var == "nc" and tr.parado and tr.cur is None:
                continue
            if fin:
                want, causa = None, "fin"
            elif t_ms < p.t_ini:
                want, causa = None, "antes_de_ventana"
            elif forzar_causa or sin_vista:
                want, causa = None, forzar_causa or "sin_libro"
            else:
                want = R.querer(b5, a5, b15, a15, tr.umbral)
                causa = None
            cur = tr.cur
            if cur is not None and tr.var == "nc":
                if fin:
                    self._cancelar(p, tr, cur, p.t_fin, "fin")
                continue                                  # control: nunca cancela salvo fin
            if (want is None and cur is None) or (want is not None and cur is not None and abs(want - cur["precio"]) < EPS):
                continue
            if cur is not None:
                self._cancelar(p, tr, cur, p.t_fin if fin else t_ms, causa or self._causa(p, cur, b5, a5, b15, a15, tr.umbral))
            if want is not None and not fin and (tr.var != "nc" or not tr.parado):
                if t_ms < tr.bloq:
                    p.motivos["repost_espera"] += 1
                    continue
                if tr.n_alta >= CFG["max_cotiz_por_mercado"]:
                    p.motivos["tope_cotiz"] += 1
                    continue
                self._poner(p, tr, want, t_ms, b5, a5, b15)

    @staticmethod
    def _causa(p, cur, b5, a5, b15, a15, umbral):
        if b5 is None or a5 is None or b15 is None:
            return "sin_libro"
        if (a15 is not None and b15 > a15) or b5 > a5:
            return "cruzado"
        if b5 < cur["precio"] - EPS:
            return "bid5_baja"                            # desplome del bid del 5m (el nivel de delante se consumio/retiro)
        if b5 > cur["precio"] + EPS:
            return "bid5_sube"
        pl = R.p_limite(b15, umbral)
        if pl is None or cur["precio"] > pl + EPS:
            return "cota_cae"
        return "margen"

    def _poner(self, p, tr, precio, t_ms, b5, a5, b15):
        n = tr.n_alta + 1
        tr.n_alta = n
        depth = p.lib[p.tc].bids.get(precio, 0.0)
        seg = {"n": n, "precio": precio, "depth": depth, "t_dec": t_ms, "t_can": None, "causa": None,
               "ahead": {c: f * depth for c, f in CFG["colas"].items()}, "fills": {}}
        if tr.need is None:
            tr.need = R.acciones(precio)
        tr.segs.append(seg)
        tr.cur = seg
        if tr.var == "nc":
            tr.parado = True
        self.emit({"k": f"puesto|{p.m5['id']}|{tr.arm}|{tr.var}|{n}", "tipo": "puesto", "mkt": p.m5["id"], "arm": tr.arm, "var": tr.var, "n": n,
                   "lado": p.s, "cierre": p.c, "r": t_ms, "T": _r(p.c - t_ms / 1000.0, 3), "precio": precio, "depth": _r(depth, 3),
                   "ask5": a5, "bid5": b5, "bid15": b15, "margen": _r(R.margen(b15, a5), 4), "need": _r(tr.need, 2), "lat": LAT,
                   "arranque_tarde": p.arranque_tarde, "t_ready": {l: t_ms + LAT[l][0] for l in LAT}})
        self.stats["puestos"] += 1

    def _cancelar(self, p, tr, seg, t_ms, causa):
        seg["t_can"], seg["causa"] = t_ms, causa
        tr.cur = None
        tr.bloq = t_ms + CFG["repost_min_ms"][tr.var]
        tr.n_baja += 1
        self.emit({"k": f"cancela|{p.m5['id']}|{tr.arm}|{tr.var}|{seg['n']}", "tipo": "cancela", "mkt": p.m5["id"], "arm": tr.arm, "var": tr.var,
                   "n": seg["n"], "r": t_ms, "T": _r(p.c - t_ms / 1000.0, 3), "causa": causa, "precio": seg["precio"],
                   "vida_ms": t_ms - seg["t_dec"], "eff": {l: t_ms + LAT[l][1] for l in LAT}})
        self.stats[f"cancela_{causa}"] += 1

    # -- markouts ----------------------------------------------------------------------------------------------------------------
    def _marcar(self, p, due, tr, esc, h, t0):
        if due >= p.c * 1000:
            self.emit({"k": f"markout|{p.m5['id']}|{tr.arm}|{tr.var}|{esc}|{h}", "tipo": "markout", "mkt": p.m5["id"], "arm": tr.arm, "var": tr.var,
                       "esc": esc, "h": h, "r": due, "r0": t0, "motivo": "post_cierre", "bid": None, "ask": None, "mid": None})
            return
        p.pend_mark.append((due, tr.arm, tr.var, esc, h, t0))
        p.pend_mark.sort()

    def _markouts(self, p, t_ms):
        while p.pend_mark and p.pend_mark[0][0] <= t_ms:
            due, arm, var, esc, h, t0 = p.pend_mark.pop(0)
            row = {"k": f"markout|{p.m5['id']}|{arm}|{var}|{esc}|{h}", "tipo": "markout", "mkt": p.m5["id"], "arm": arm, "var": var, "esc": esc,
                   "h": h, "r": t_ms, "r0": t0, "due": due, "retraso_ms": t_ms - due}
            l = p.lib[p.tc]
            if not l.vivo or t_ms - p.ult_msg > FRESCO_MS:
                row.update(motivo="sin_libro", bid=None, ask=None, mid=None)
            else:
                bb, ba = l.top()
                row.update(motivo=None, bid=bb, ask=ba, mid=_r((bb + ba) / 2, 5) if bb is not None and ba is not None else None)
            self.emit(row)

    def vivo(self, p, t_ms):
        """PONG/latido de la conexion: el libro de un token callado sigue siendo valido."""
        if not p.cerrado:
            p.ult_msg = max(p.ult_msg, t_ms)

    def tick(self, t_ms):
        for p in list(self.pares.values()):
            if not p.cerrado:
                self.evaluar(p, t_ms)

    # -- cierre y desenlace -----------------------------------------------------------------------------------------------------------
    def cerrar_par(self, mkt, t_ms, abortado=False):
        p = self.pares.get(mkt)
        if p is None or p.cerrado:
            return
        if abortado:
            self.evaluar(p, t_ms, forzar_causa="abortado")
        else:
            self.evaluar(p, max(t_ms, p.t_fin))
        p.cerrado = True
        res = {}
        for tr in p.traders:
            for seg in tr.segs:
                if seg["t_can"] is None:
                    seg["t_can"], seg["causa"] = p.t_fin, "fin"
            for esc in ESCS:
                fl = [f for seg in tr.segs for f in seg["fills"].get(esc, [])]
                res[f"{tr.arm}|{tr.var}|{esc}"] = {"acc": _r(tr.lleno[esc], 4), "coste": _r(tr.coste[esc], 5), "n": tr.nfill[esc], "t1": tr.t1[esc],
                                                   "T1": _r(p.c - tr.t1[esc] / 1000.0, 2) if tr.t1[esc] else None, "need": _r(tr.need, 2)}
            self.emit({"k": f"relleno|{mkt}|{tr.arm}|{tr.var}", "tipo": "relleno_resumen", "mkt": mkt, "arm": tr.arm, "var": tr.var, "r": t_ms,
                       "n_alta": tr.n_alta, "n_baja": tr.n_baja, "need": _r(tr.need, 2),
                       "esc": {e: res[f"{tr.arm}|{tr.var}|{e}"] for e in ESCS}})
        # el resto de markouts programados que no llegaron a tiempo: se cierran como missing (tras el cierre del libro)
        for due, arm, var, esc, h, t0 in p.pend_mark:
            self.emit({"k": f"markout|{mkt}|{arm}|{var}|{esc}|{h}", "tipo": "markout", "mkt": mkt, "arm": arm, "var": var, "esc": esc, "h": h,
                       "r": t_ms, "r0": t0, "motivo": "sin_libro_al_vencer", "bid": None, "ask": None, "mid": None})
        p.pend_mark = []
        comp = (not abortado) and (not p.arranque_tarde) and p.reconex == 0 and p.lib[p.tc or p.tok["5u"]].ult > 0
        self.emit({"k": f"fin|{mkt}", "tipo": "mercado_fin", "mkt": mkt, "mkt15": p.m15["id"], "cierre": p.c, "r": t_ms, "completo": comp,
                   "arranque_tarde": p.arranque_tarde, "abortado": abortado, "reconex": p.reconex, "n_msgs": p.n_msgs, "lado": p.s,
                   "motivos": dict(p.motivos),
                   "api": {f"{t.arm}|{t.var}": {"altas": t.n_alta, "bajas": t.n_baja} for t in p.traders}})
        self.records[mkt] = {"cierre": p.c, "lado": p.s, "res": {k: v for k, v in res.items()}, "ganador": None, "des_emitido": False,
                             "completo": comp}
        for t in p.tok.values():
            self.tk.pop(t, None)
        self.pares.pop(mkt, None)
        self.stats["pares_completos" if comp else "pares_incompletos"] += 1

    def pendientes_desenlace(self, ahora_s, espera_s=25):
        return [mk for mk, r in self.records.items() if not r["des_emitido"] and r["cierre"] + espera_s <= ahora_s]

    def on_desenlace(self, mkt, ganador, t_ms, motivo=None):
        r = self.records.get(mkt)
        if r is None or r["des_emitido"]:
            return False
        if ganador is not None:
            r["ganador"] = ganador
        pn = {}
        s_lado = "YES" if r["lado"] == "Up" else "NO" if r["lado"] else None
        for k, d in r["res"].items():
            if ganador is None or s_lado is None:
                pn[k] = None
            elif not d["acc"]:
                pn[k] = 0.0
            else:
                pm = d["coste"] / d["acc"]
                pn[k] = _r(R.pnl_relleno(d["acc"], pm, ganador == s_lado), 5)
        ok = self.emit({"k": f"des|{mkt}", "tipo": "desenlace", "mkt": mkt, "cierre": r["cierre"], "r": t_ms, "ganador": ganador,
                        "gana_s": None if ganador is None or s_lado is None else ganador == s_lado, "motivo": motivo, "pnl": pn,
                        "completo": r["completo"]})
        r["des_emitido"] = True
        return ok

    def podar(self, ahora_s):
        for mk in [mk for mk, r in self.records.items() if r["cierre"] < ahora_s - 8 * 3600 and r["des_emitido"]]:
            del self.records[mk]


def _limpia(o):
    if isinstance(o, float) and (o != o or o in (INF, -INF)):
        return None
    if isinstance(o, dict):
        return {k: _limpia(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_limpia(v) for v in o]
    return o


# ---------------------------------------------------------------------------------------------------------------------
# Disco: jsonl.gz diario (miembros gzip anadidos), retencion, relectura tolerante
class Salida:
    def __init__(self, d):
        self.d = Path(d)
        self.d.mkdir(parents=True, exist_ok=True)
        self.q = queue.SimpleQueue()
        self.parar = threading.Event()
        self.hilo = threading.Thread(target=self._bucle, daemon=True, name="h23_escritor")
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
                except ValueError:
                    ln = json.dumps(_limpia(row), separators=(",", ":"), allow_nan=False)
                por_dia.setdefault(_dia(row.get("r") or ahora_ms()), []).append(ln)
        except queue.Empty:
            pass
        for dia, lineas in por_dia.items():
            blob = gzip.compress(("\n".join(lineas) + "\n").encode(), 6)
            with open(self.d / f"h23_shadow_{dia}.jsonl.gz", "ab") as f:
                f.write(blob)
                f.flush()
                os.fsync(f.fileno())

    def _bucle(self):
        while not self.parar.wait(5):
            try:
                self._vaciar()
            except Exception as e:
                print(f"{datetime.now(timezone.utc).isoformat()} escritor: {type(e).__name__}: {e}", file=sys.stderr, flush=True)

    def cerrar(self):
        self.parar.set()
        self.hilo.join(timeout=6)
        self._vaciar()


def leer_gz_tolerante(path):
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
    """Reconstruye (emitidos, records) desde los logs de los ultimos `dias` dias (el log es el estado)."""
    emitidos, records = set(), {}
    hoy = datetime.fromtimestamp(ahora_s, timezone.utc).date()
    for i in range(dias, -1, -1):
        f = Path(dirn) / f"h23_shadow_{(hoy - timedelta(days=i)).isoformat()}.jsonl.gz"
        if not f.exists():
            continue
        for row in leer_gz_tolerante(f):
            k = row.get("k")
            if k:
                emitidos.add(k)
            t = row.get("tipo")
            if t == "relleno_resumen":
                rr = records.setdefault(row["mkt"], {"cierre": None, "lado": None, "res": {}, "ganador": None, "des_emitido": False, "completo": False})
                for e, d in row["esc"].items():
                    rr["res"][f"{row['arm']}|{row['var']}|{e}"] = {"acc": d["acc"], "coste": d["coste"], "n": d["n"], "t1": d["t1"],
                                                                    "T1": d.get("T1"), "need": d.get("need")}
            elif t == "mercado_fin" and row["mkt"] in records:
                records[row["mkt"]].update(cierre=row["cierre"], lado=row.get("lado"), completo=row["completo"])
            elif t == "desenlace" and row["mkt"] in records:
                records[row["mkt"]]["ganador"] = row.get("ganador")
                records[row["mkt"]]["des_emitido"] = True
    return emitidos, {k: v for k, v in records.items() if v["cierre"] is not None}


def aplicar_retencion(dirn, ahora_s, dias=RETENCION_DIAS):
    lim = (datetime.fromtimestamp(ahora_s, timezone.utc) - timedelta(days=dias)).strftime("%Y-%m-%d")
    borrados = []
    for f in glob.glob(str(Path(dirn) / "h23_shadow_*.jsonl.gz")):
        d = os.path.basename(f)[len("h23_shadow_"):-len(".jsonl.gz")]
        if len(d) == 10 and d < lim:
            os.remove(f)
            borrados.append(f)
    return borrados


# ---------------------------------------------------------------------------------------------------------------------
# Referencias TWAP60 oficiales (CSV de PolyBolt, source=chainlink) -- solo lectura
class Refs:
    def __init__(self, prices=PRICES):
        self.prices, self.v, self.lock = Path(prices), {}, threading.Lock()
        self.parar = threading.Event()
        self.hilo = threading.Thread(target=self._seguir, daemon=True, name="h23_refs")
        self.hilo.start()

    def _linea(self, ln, t_ms):
        c = ln.rstrip("\n").split(",")
        if len(c) < 7 or c[2] != "twap60" or c[6] != "chainlink" or c[1] != "BTC":
            return
        try:
            e = int(c[4]) // 1000
            if e % 300:
                return
            with self.lock:
                self.v.setdefault(e, (float(c[3]), t_ms))
        except ValueError:
            pass

    def _seguir(self):
        abiertos = {}                                       # dia -> [file, pos, historico_ya_leido]
        while not self.parar.is_set():
            try:
                hoy = datetime.now(timezone.utc).date()
                for d in (hoy - timedelta(days=1), hoy):
                    ds = d.isoformat()
                    if ds not in abiertos:
                        p = self.prices / f"polybolt_{ds}.csv"
                        if p.exists():
                            abiertos[ds] = [open(p), True]    # primera pasada = historico (sin hora de lectura)
                for ds, st in list(abiertos.items()):
                    f, hist = st
                    while True:
                        pos = f.tell()
                        ln = f.readline()
                        if not ln:
                            break
                        if not ln.endswith("\n"):
                            f.seek(pos)
                            break
                        self._linea(ln, None if hist else ahora_ms())
                    st[1] = False
                    if ds < (hoy - timedelta(days=1)).isoformat():
                        f.close()
                        del abiertos[ds]
            except Exception as e:
                print(f"[h23] refs: {type(e).__name__}: {e}", file=sys.stderr, flush=True)
            time.sleep(0.05)

    def get(self, e):
        with self.lock:
            return self.v.get(e)


# ---------------------------------------------------------------------------------------------------------------------
# Red (solo lectura)
def mercado_btc(marco, ini):
    import requests
    ev = requests.get(f"{GAMMA}/events", params={"slug": f"btc-updown-{marco}-{ini}"}, timeout=5).json()
    if not ev:
        return None
    m = ev[0]["markets"][0]
    out = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
    toks = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
    if [o.lower() for o in out] != ["up", "down"] or len(toks) != 2:
        raise ValueError(f"btc-updown-{marco}-{ini}: outcomes {out} inesperados (fail-closed)")
    return {"id": str(m["id"]), "up": toks[0], "down": toks[1]}


def desenlaces_gamma(mids):
    import requests
    res = {}
    for k in range(0, len(mids), 40):
        r = requests.get(f"{GAMMA}/markets", timeout=20, params=[("id", x) for x in mids[k:k + 40]] + [("closed", "true"), ("limit", "40")])
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


async def vigilar(nuc, refs, c, m5, m15, parar):
    import websockets
    toks = [m5["up"], m5["down"], m15["up"], m15["down"]]
    p = nuc.nuevo_par(c, m5, m15, ahora_ms())
    fin_ms = int(c * 1000) + 500
    abortado = True
    lado_fijado = False

    async def esperar_refs():
        nonlocal lado_fijado
        while not parar.is_set() and ahora_ms() < p.t_fin and not lado_fijado:
            r15, r5 = refs.get(c - 900), refs.get(c - 300)
            if r15 and r5:
                lado_fijado = True
                nuc.fijar_lado(p, r15[0], r5[0], r5[1] if r5[1] else ahora_ms())     # r5[1]=None si ya estaba en el historico al arrancar
                return
            await asyncio.sleep(0.02)
        if not lado_fijado and not parar.is_set():
            nuc.sin_refs(p, ahora_ms())
    tr_refs = asyncio.create_task(esperar_refs())
    try:
        while ahora_ms() < fin_ms and not parar.is_set():
            try:
                async with websockets.connect(WS_URL, open_timeout=10, close_timeout=2, max_size=None, ping_interval=None) as ws:
                    await ws.send(json.dumps({"assets_ids": toks, "type": "market"}))

                    async def latido():
                        while True:
                            await asyncio.sleep(2.0)
                            await ws.send("PING")
                    tl = asyncio.create_task(latido())
                    try:
                        while ahora_ms() < fin_ms and not parar.is_set():
                            try:
                                raw = await asyncio.wait_for(ws.recv(), timeout=1.0)
                            except asyncio.TimeoutError:
                                nuc.tick(ahora_ms())
                                continue
                            t = ahora_ms()
                            if raw == "PONG" or not raw:
                                nuc.vivo(p, t)               # conexion viva: un libro quieto no es un libro roto
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
                                except Exception as e:
                                    nuc.stats["error_mensaje"] += 1
                                    if nuc.stats["error_mensaje"] in (1, 10, 100, 1000):
                                        nuc.emit({"k": f"error_msg|{t}", "tipo": "error", "r": t, "m": f"{et}: {type(e).__name__}: {str(e)[:80]}"})
                    finally:
                        tl.cancel()
            except asyncio.CancelledError:
                raise
            except Exception as e:
                nuc.on_gap(p, ahora_ms(), f"{type(e).__name__}: {e}")
                await asyncio.sleep(0.5)
        abortado = ahora_ms() < fin_ms - 400
    finally:
        tr_refs.cancel()
        nuc.cerrar_par(m5["id"], ahora_ms(), abortado=abortado)


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


async def principal(args, out, nuc, refs, parar):
    loop = asyncio.get_running_loop()
    lanzados, tareas, fallos = set(), [], {}
    t_fin = time.time() + args.minutos * 60 if args.minutos else None
    t_latido = t_ret = 0.0
    tr_res = asyncio.create_task(resolvedor(nuc, parar))
    nuc.emit({"k": f"inicio|{ahora_ms()}", "tipo": "inicio", "r": ahora_ms(), "pid": os.getpid(), "minutos": args.minutos,
              "records": len(nuc.records), "emitidos": len(nuc.emitidos), "hash_regla": R.hash_config(), "config": {k: CFG[k] for k in ("brazos", "mq", "lat_post_ms", "lat_cancel_ms")}})
    while not parar.is_set() and (t_fin is None or time.time() < t_fin):
        ahora = time.time()
        c = (int(ahora // 900) + 1) * 900                    # proximo cierre de 15m (= cierre de su ultimo 5m)
        if c not in lanzados and c - 300 - ANTES_S <= ahora < c and fallos.get(c, (0, 0))[1] <= ahora:
            try:
                m5 = await loop.run_in_executor(None, mercado_btc, "5m", c - 300)
                m15 = await loop.run_in_executor(None, mercado_btc, "15m", c - 900)
            except Exception as e:
                n = fallos.get(c, (0, 0))[0] + 1
                fallos[c] = (n, ahora + min(3 * n, 20))
                nuc.stats["gamma_mercado_error"] += 1
                if n in (1, 5, 20):
                    nuc.emit({"k": f"error|{c}|{n}", "tipo": "error", "r": ahora_ms(), "m": f"gamma {c}: {type(e).__name__}: {str(e)[:80]}"})
            else:
                if not m5 or not m15:
                    fallos[c] = (1, ahora + 3)
                else:
                    lanzados.add(c)
                    if f"fin|{m5['id']}" not in nuc.emitidos:
                        tareas.append(asyncio.create_task(vigilar(nuc, refs, c, m5, m15, parar)))
        tareas = [t for t in tareas if not t.done()]
        nuc.podar(time.time())
        if ahora - t_latido > 600:
            t_latido = ahora
            rss = rss_mb()
            nuc.emit({"k": f"latido|{ahora_ms()}", "tipo": "latido", "r": ahora_ms(), "rss_mb": _r(rss, 1), "vigilando": len(nuc.pares),
                      "records": len(nuc.records), "stats": dict(nuc.stats)})
            if rss and rss > 400:
                print(f"RSS {rss:.0f} MB > 400: salgo para que el watchdog reinicie", file=sys.stderr, flush=True)
                parar.set()
        if ahora - t_ret > 3600:
            t_ret = ahora
            aplicar_retencion(args.salida, ahora)
        await asyncio.sleep(0.5)
    parar.set()
    if tareas:
        await asyncio.gather(*tareas, return_exceptions=True)
    await tr_res
    nuc.emit({"k": f"fin_proceso|{ahora_ms()}", "tipo": "fin_proceso", "r": ahora_ms(), "stats": dict(nuc.stats)})


def resumen(dirn):
    tot = Counter()
    for f in sorted(glob.glob(str(Path(dirn) / "h23_shadow_*.jsonl.gz"))):
        c = Counter(r.get("tipo") for r in leer_gz_tolerante(f))
        print(os.path.basename(f), dict(c))
        tot.update(c)
    print("TOTAL", dict(tot))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=SALIDA_DEFECTO)
    ap.add_argument("--minutos", type=float, default=None, help="SOLO prueba de humo (acotada)")
    ap.add_argument("--resolver-solo", action="store_true")
    ap.add_argument("--resumen", action="store_true")
    args = ap.parse_args()
    if args.resumen:
        resumen(args.salida)
        return 0
    if args.minutos and os.path.abspath(args.salida) == SALIDA_DEFECTO:
        sys.exit("--minutos exige --salida distinta de la de produccion (fail-closed)")
    try:
        resource.setrlimit(resource.RLIMIT_AS, (1_500_000_000, 1_500_000_000))
    except (ValueError, OSError):
        pass
    Path(args.salida).mkdir(parents=True, exist_ok=True)
    emitidos, records = restaurar(args.salida, time.time())
    out = Salida(args.salida)
    nuc = Nucleo(out.put, emitidos, records, prueba=True if args.minutos else None)
    refs = None if args.resolver_solo else Refs()
    parar = asyncio.Event()

    async def corre():
        loop = asyncio.get_running_loop()
        for s in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(s, parar.set)
        if args.resolver_solo:
            await resolvedor(nuc, parar, una_vez=True)
        else:
            await principal(args, out, nuc, refs, parar)
    print(f"{datetime.now(timezone.utc).isoformat()} h23_shadow arrancando pid={os.getpid()} salida={args.salida} records={len(records)} "
          f"emitidos={len(emitidos)} hash_regla={R.hash_config()}", flush=True)
    try:
        asyncio.run(corre())
    finally:
        out.cerrar()
        if refs:
            refs.parar.set()
    print(f"{datetime.now(timezone.utc).isoformat()} h23_shadow terminado stats={dict(nuc.stats)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
