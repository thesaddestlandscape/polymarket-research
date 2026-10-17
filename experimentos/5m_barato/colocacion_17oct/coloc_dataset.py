#!/usr/bin/env python3
"""5m barato H43 MODELO DE COLOCACION del maker -- constructor del DATASET (una pasada por día; SOLO LECTURA / simulación).
No manda órdenes, no firma, no toca producción ni procesos. Fichero NUEVO (17-Oct, encargo del chief): IMPORTA el simulador base
`analisis_5m_maker_banda_simulador` (S) y el motor DEEP `analisis_5m_maker_banda_deep_peg` (H) SIN modificarlos ni tocar sus cachés;
sus cachés (m5_maker_banda*) quedan intactos. Salida en /root/polymarket-research-datalogs/m5_maker_colocacion/.

PREGUNTA: E[pnl/€ de una puja NUEVA de 5 acciones colocada en el instante t_q a profundidad k (k=0 unirse al top = JOIN, k=1,2 ticks por
debajo = DEEP) | estado observable en t_q], con la vida de la puja y su repegado IGUALES a H35 (parada T=60 s, alta +68 ms, cancelación +60 ms,
bloqueo en vuelo, relleno CONSERVADOR: solo operaciones que atraviesan el nivel o superan la cola; cola desconocida = infinita).

MECANISMO (reutilización del motor, sin copiar su lógica de relleno): `ColocMotor` hereda `DeepMotor` y, en cada punto de decisión t_q de
un token (primer evento q con bid top en (0,11, 0,30], T en (60, 300] s y luego cada >= SPAWN_MS ms), CREA tres órdenes independientes
(k=0 con la rutina JOIN del motor base, k=1 y k=2 con `_eval_deep`) que el propio motor rellena/repega/cancela como a cualquier posición
(están en `vivos`). Además corren los motores de LÍNEA BASE de H35 (JOIN, DEEP_k1, DEEP_k2; primera decisión de la unidad): la primera
orden creada de cada unidad debe coincidir con ellos (prueba de regresión en tests y comparación con la caché de H35).

RASGOS (lista FIJADA antes de mirar OOS; solo información con recepción <= t_q; ver FEATS):
  libro del token (bid, ask, tamaños, spread, imbalance, T, nº de cambios del top en 1/5/30 s, tiempo desde el último cambio, deriva del
  bid/ask en 5/30 s), flujo (volumen vendedor tomador que golpea el bid en 1/5/30 s, ventas por debajo del bid, nº de operaciones, compras
  tomadoras, precio de la última, antigüedad), contrario (bid/ask, hueco de paridad), Binance (aggTrade por RECEPCIÓN c[7]: retorno 1/5/30 s en
  bps con el signo del lado, volatilidad 30 s, nº ticks), 15m del mismo subyacente y lado (bid15, ask15, margen bid15−ask5, T15, tramo 0/1/2
  dentro del 15m: SOLO en el grupo B), profundidad espejo de las filas l (SOLO en el grupo C), moneda y lado.
ETIQUETAS por decisión y k: disponible (se pudo colocar), lleno, coste, rebate, T medio de relleno, nº de órdenes (repegados), precio inicial,
cola conocida; el pnl (con desenlace OFICIAL) se calcula al cargar: pnl = lleno·1[gana el lado] − coste. missing != 0.

Contrato de trabajo largo: run_manifest.json, caché durable ATÓMICA por día (dp_D.npz + meta_D.json con hash de este fichero, del simulador
y de los parámetros), claves únicas (mkt, lado, tq_ms), cobertura (días, mercados, desenlaces), resumen parcial, log con hora y estado
final COMPLETE/PARTIAL/FAILED/BLOCKED.
Uso (RAM acotada): ulimit -v 2000000; nice -n 19 ionice -c3 python3 coloc_dataset.py --dias 2026-10-05,... [--recorte-min 30 humo]
"""
import argparse
import bisect
import collections
import gzip
import hashlib
import json
import math
import os
import pickle
import sys
import time
from array import array
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ))
import analisis_5m_maker_banda_simulador as S  # noqa: E402
import analisis_5m_maker_banda_deep_peg as H  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5_maker_colocacion")
K15_DIRS = (Path("/root/polymarket-research-datalogs/m5_maker_banda_deep_peg"), Path("/root/polymarket-research-datalogs/m5_maker_banda"))
VERSION = "coloc_v1"
KS = (0, 1, 2)
SPAWN_MS = 1000                      # separación mínima entre decisiones de un mismo token (rejilla de eventos)
WIN_MS = (1000, 5000, 30000)
MONEDAS = S.MONEDAS
COIN_IDX = {c: i for i, c in enumerate(MONEDAS)}
SYM2COIN = {v: k for k, v in S.SIMBOLO.items()}
NAN = float("nan")
HORA_BLOQUEO = (6 * 60, 9 * 60 + 15)     # 06:00-09:15Z: no se lanza trabajo pesado

# ---- lista de rasgos FIJADA (el orden es el de las columnas del .npz)
F_BOOK = ["bid", "ask", "spr", "lbsz", "lasz", "imb", "T", "chg1", "chg5", "chg30", "tsb", "tsa", "dbid5", "dbid30", "dask5", "dask30",
          "par_bid", "par_ask", "pair_gap"]
F_FLOW = ["hit1", "hit5", "hit30", "hitb30", "nhit5", "nhit30", "lift5", "lift30", "lhit_rel", "tlast"]
F_BN = ["bn_r1", "bn_r5", "bn_r30", "bn_rv30", "bn_n5"]
F_15 = ["b15", "a15", "m15", "T15", "seg15"]
F_LAD = ["dq1", "dq2", "dq3"]
F_CAT = [f"c_{c}" for c in MONEDAS] + ["lado_yes"]
FEATS = F_BOOK + F_FLOW + F_BN + F_15 + F_LAD + F_CAT
NF = len(FEATS)
FI = {n: i for i, n in enumerate(FEATS)}


def sha_codigo():
    return hashlib.sha256((S.sha_fichero(Path(__file__)) + S.sha_fichero(Path(S.__file__)) + S.sha_fichero(Path(H.__file__))).encode()).hexdigest()


def params_dict():
    return {"version": VERSION, "ks": list(KS), "spawn_ms": SPAWN_MS, "win_ms": list(WIN_MS), "feats": FEATS, "P_TOP_LO": H.P_TOP_LO,
            "T": [S.T_MIN, S.T_MAX], "LAT_POST_MS": S.LAT_POST_MS, "LAT_CANCEL_MS": S.LAT_CANCEL_MS, "SH": S.SH_BASE, "TICK": S.TICK,
            "cola": "CONS", "ladders": "solo filas l (sin L)"}


def params_hash():
    return hashlib.sha256(json.dumps(params_dict(), sort_keys=True).encode()).hexdigest()[:16]


# ---------------------------------------------------------------- historiales por token (ventanas deslizantes con recorte)
def _recorta(listas, t, ret_ms=40000):
    """Quita lo anterior a t-ret_ms CONSERVANDO una entrada previa (el estado vigente en t-ret_ms)."""
    ts = listas[0]
    cut = bisect.bisect_left(ts, t - ret_ms) - 1
    if cut > 0:
        for l in listas:
            del l[:cut]


class Hist:
    __slots__ = ("t", "b", "a")

    def __init__(self):
        self.t, self.b, self.a = [], [], []

    def add(self, t, b, a):
        if self.t and t < self.t[-1]:
            t = self.t[-1]                      # desorden de pocos ms entre filas: se fija monótono (no usa futuro)
        self.t.append(t)
        self.b.append(b)
        self.a.append(a)
        if len(self.t) > 800:
            _recorta((self.t, self.b, self.a), t)

    def en(self, t):
        i = bisect.bisect_right(self.t, t) - 1
        return (self.b[i], self.a[i]) if i >= 0 else None


class Flujo:
    __slots__ = ("t", "p", "s")

    def __init__(self):
        self.t, self.p, self.s = [], [], []

    def add(self, t, p, s):
        if self.t and t < self.t[-1]:
            t = self.t[-1]
        self.t.append(t)
        self.p.append(p)
        self.s.append(s)
        if len(self.t) > 800:
            _recorta((self.t, self.p, self.s), t)


def _mils_o(s):
    try:
        return S.mils(s)
    except (ValueError, TypeError):
        return -1


# ---------------------------------------------------------------- 15m del mismo subyacente (pre-pasada sobre m15_registro, caché por día)
class B15:
    def __init__(self):
        self.q = {}        # token 15m -> (t list, bid list, ask list)   (-1 = lado vacío)
        self.k15 = {}      # (coin, fin15_ms, lado) -> token 15m

    def estado(self, tok, t):
        s = self.q.get(tok)
        if s is None:
            return None
        i = bisect.bisect_right(s[0], t) - 1
        return (s[1][i], s[2][i]) if i >= 0 else None


def k15_previo(dia):
    from datetime import date, timedelta
    prev = (date.fromisoformat(dia) - timedelta(days=1)).isoformat()
    m = {}
    for d in K15_DIRS:
        f = d / f"k15map_{prev}.csv.gz"
        if f.exists():
            with gzip.open(f, "rt") as fh:
                for ln in fh:
                    coin, fin, lado, tk = ln.rstrip("\n").split(",")
                    m[(coin, int(fin), lado)] = tk
            return m
    return m


def leer_b15(dia, out, log, t_corte=None, max_lineas=None):
    cache = out / f"b15_{dia}.pkl"
    if cache.exists() and not t_corte and not max_lineas:
        try:
            with open(cache, "rb") as fh:
                dd = pickle.load(fh)
            b = B15()
            b.q, b.k15 = dd["q"], dd["k15"]
            return b
        except Exception:
            pass
    b = B15()
    b.k15.update(k15_previo(dia))
    f = S.VOL / "m15_registro" / f"m15_registro_{dia}.csv.gz"
    if not f.exists():
        log(f"{dia}: sin m15_registro -> rasgos 15m ausentes (NaN, missing != 0)")
        return b
    toks = set(b.k15.values())
    qt, qb, qa = collections.defaultdict(lambda: array("q")), collections.defaultdict(lambda: array("h")), collections.defaultdict(lambda: array("h"))
    ult = {}
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
                    if tk not in toks:
                        continue
                    try:
                        t = int(c[7])
                    except (ValueError, IndexError):
                        continue
                    if t_corte and t > t_corte:
                        continue
                    bb, aa = _mils_o(c[3]), _mils_o(c[4])
                    if ult.get(tk) == (bb, aa):
                        continue
                    ult[tk] = (bb, aa)
                    qt[tk].append(t)
                    qb[tk].append(bb)
                    qa[tk].append(aa)
                elif tp == "k,":
                    c = ln.split(",")
                    if len(c) >= 8 and c[4] == "15min":
                        try:
                            b.k15[(c[3], S._ms_iso(c[6]), c[7].strip())] = c[2]
                            toks.add(c[2])
                        except ValueError:
                            pass
        except (EOFError, OSError) as e:
            log(f"{dia}: m15_registro truncado ({type(e).__name__}) tras {n} líneas")
    for tk in qt:
        t = np.frombuffer(qt[tk], dtype=np.int64)
        o = np.argsort(t, kind="stable")           # el fichero NO es cronológico (unión de tramos): se ordena por recepción
        b.q[tk] = (t[o].tolist(), np.frombuffer(qb[tk], dtype=np.int16)[o].astype(int).tolist(),
                   np.frombuffer(qa[tk], dtype=np.int16)[o].astype(int).tolist())
    if not t_corte and not max_lineas:
        tmp = cache.with_name(cache.name + f".tmp{os.getpid()}")
        with open(tmp, "wb") as fh:
            pickle.dump({"q": b.q, "k15": b.k15}, fh, protocol=4)
        os.replace(tmp, cache)
    return b


# ---------------------------------------------------------------- el motor
class Rec:
    __slots__ = ("pos", "did", "k", "e", "pend", "p0", "known0")


class ColocMotor(H.DeepMotor):
    """DeepMotor + órdenes creadas en cada punto de decisión (k=0,1,2) y vector de rasgos causal por decisión."""

    def __init__(self, engines, ext, lad, b15, dia_ini_ms=0, monedas=None, spawn_ms=SPAWN_MS):
        super().__init__(engines, ext, lad, dia_ini_ms, (), monedas, False)
        self.b15 = b15
        self.spawn_ms = spawn_ms
        self.E_sp = {}
        for k in KS:
            fam = "JOIN" if k == 0 else "DEEP"
            e = H.EngD(self.NE, fam, k, "CONS", None, False)
            self.E_sp[k] = e
        self.hist = collections.defaultdict(Hist)
        self.hit = collections.defaultdict(Flujo)       # token -> ventas tomadoras que golpean SU bid (equivalentes por acuñación)
        self.lift = collections.defaultdict(Flujo)      # token -> compras tomadoras sobre SU ask
        self.last_trade = {}
        self.last_sp = {}
        self.live = collections.defaultdict(list)       # token -> [Rec]
        self.xt = collections.defaultdict(list)         # coin -> tiempos de ticks Binance (recepción)
        self.xp = collections.defaultdict(list)
        # salida compacta
        self.d_meta = []        # (mkt, lado01, coin, fin_s, tq, tramo)
        self.d_feat = array("f")
        self.l_av = {k: array("b") for k in KS}
        self.l_lleno = {k: array("f") for k in KS}
        self.l_coste = {k: array("f") for k in KS}
        self.l_reb = {k: array("f") for k in KS}
        self.l_tf = {k: array("f") for k in KS}
        self.l_nord = {k: array("h") for k in KS}
        self.l_p0 = {k: array("h") for k in KS}
        self.l_known = {k: array("b") for k in KS}
        self.st["decisiones"] = 0

    # ---- no se guardan los markouts / salidas de H35 (no hacen falta y cuestan memoria)
    def _reg_fill(self, pos, obj, precio, f, t_ex, t_rx):
        return

    # ---- Binance por recepción
    def x(self, coin, t, px):
        if self.xt[coin] and t < self.xt[coin][-1]:
            t = self.xt[coin][-1]
        self.xt[coin].append(t)
        self.xp[coin].append(px)
        if len(self.xt[coin]) > 6000:
            _recorta((self.xt[coin], self.xp[coin]), t)

    def _px_en(self, coin, t):
        ts = self.xt.get(coin)
        if not ts:
            return None
        i = bisect.bisect_right(ts, t) - 1
        if i < 0 or t - ts[i] > S.STALE_MS + 30000:
            return None
        return self.xp[coin][i]

    def cerrar_tramo(self):
        self._finaliza_todo()
        super().cerrar_tramo()
        self.hist.clear()
        self.hit.clear()
        self.lift.clear()
        self.last_trade.clear()
        self.last_sp.clear()
        self.xt.clear()
        self.xp.clear()

    # ---- operaciones: se registra el flujo por RECEPCIÓN y luego lo normal del motor
    def t(self, tk, p, side, sz, t_ex, t_rx):
        m = self.meta.get(tk)
        if m is None:
            return
        par = self.par.get(tk)
        if side == "SELL":
            self.hit[tk].add(t_rx, p, sz)
            if par is not None:
                self.lift[par].add(t_rx, 1000 - p, sz)
        elif side == "BUY":
            self.lift[tk].add(t_rx, p, sz)
            if par is not None:
                self.hit[par].add(t_rx, 1000 - p, sz)
        self.last_trade[tk] = t_rx
        if par is not None:
            self.last_trade[par] = t_rx
        super().t(tk, p, side, sz, t_ex, t_rx)

    # ---- libro
    def q(self, tk, bid, ask, bsz, t_ex, t_rx, asz=0.0):
        m = self.meta.get(tk)
        if m is None:
            return
        prev = self.top.get(tk)
        super().q(tk, bid, ask, bsz, t_ex, t_rx, asz)
        cambio = prev is None or prev[0] != bid or prev[1] != ask
        if cambio:
            self.hist[tk].add(t_rx, bid, ask)
        T = (m.fin - t_rx) * 0.001
        lv = self.live.get(tk)
        if T < S.T_MIN - 5:
            if lv:
                self._finaliza_tk(tk)
            return
        if T <= S.T_MIN or T > S.T_MAX:
            return
        libro_ok = 0 < ask and bid < ask
        banda_d = libro_ok and H.P_TOP_LO < bid <= S.P_HI
        if lv:
            self._repega(tk, m, lv, cambio, banda_d, t_rx, bid, ask, bsz)
        if not banda_d:
            return
        ls = self.last_sp.get(tk)
        if ls is not None and t_rx - ls < self.spawn_ms:
            return
        self.last_sp[tk] = t_rx
        self._decide(tk, m, t_rx, bid, ask, bsz, asz, T)

    # ---- repegado de las órdenes creadas (misma rutina que los motores de H35)
    def _eval_rec(self, rec, tk, m, t_rx, bid, ask, bsz):
        e = rec.e
        pl = [None] * (self.NE + 1)
        pl[self.NE] = rec.pos
        esp = self.espera.get(tk)
        antes = bool(esp) and self.NE in esp
        if e.fam == "JOIN":
            S.Motor._eval(self, e, pl, tk, m, t_rx, bid, ask, bsz)
        else:
            self._eval_deep(e, pl, tk, m, t_rx, bid, ask, bsz)
        esp = self.espera.get(tk)
        if esp and self.NE in esp:
            if not antes:
                rec.pend = True
            esp.discard(self.NE)
        return pl[self.NE]

    def _repega(self, tk, m, lv, cambio, banda_d, t_rx, bid, ask, bsz):
        libro_ok = 0 < ask and bid < ask
        banda_j = libro_ok and S.P_LO < bid <= S.P_HI
        resta = []
        for rec in lv:
            pos = rec.pos
            if pos.completo:
                self._finaliza(rec)
                continue
            resta.append(rec)
            ok_banda = banda_j if rec.e.fam == "JOIN" else banda_d
            if not ok_banda:
                continue
            if cambio or rec.pend:
                rec.pend = False
                self._eval_rec(rec, tk, m, t_rx, bid, ask, bsz)
        lv[:] = resta

    # ---- punto de decisión: rasgos causales + creación de las tres órdenes
    def _decide(self, tk, m, t, bid, ask, bsz, asz, T):
        did = len(self.d_meta)
        fv = self._feats(tk, m, t, bid, ask, bsz, asz, T)
        self.d_meta.append((m.mkt, 1 if m.lado == "YES" else 0, COIN_IDX[m.coin], m.fin // 1000, t, len(self.tramos)))
        self.d_feat.extend(fv)
        self.st["decisiones"] += 1
        for k in KS:
            self.l_av[k].append(0)
            self.l_lleno[k].append(0.0)
            self.l_coste[k].append(0.0)
            self.l_reb[k].append(0.0)
            self.l_tf[k].append(NAN)
            self.l_nord[k].append(0)
            self.l_p0[k].append(-1)
            self.l_known[k].append(-1)
            e = self.E_sp[k]
            rec = Rec()
            rec.e, rec.did, rec.k, rec.pend = e, did, k, False
            rec.pos = None
            pos = self._eval_rec(rec, tk, m, t, bid, ask, bsz)
            if pos is None:
                continue
            rec.pos = pos
            rec.p0 = pos.cur.precio if pos.cur is not None else -1
            rec.known0 = 1 if (k == 0 or self.cc.get(pos, 0) > 0) else 0
            self.l_av[k][did] = 1
            self.l_p0[k][did] = rec.p0
            self.l_known[k][did] = rec.known0
            self.live[tk].append(rec)

    def _finaliza(self, rec):
        pos, did, k = rec.pos, rec.did, rec.k
        self.l_lleno[k][did] = pos.lleno
        self.l_coste[k][did] = pos.coste
        self.l_reb[k][did] = pos.reb
        self.l_tf[k][did] = (pos.tsum / pos.lleno) if pos.lleno > 0 else NAN
        self.l_nord[k][did] = min(pos.norders, 30000)
        self.cc.pop(pos, None)                  # los Counter del motor retendrían cada Pos para siempre
        self.cd.pop(pos, None)
        self.vivos_quita(pos)

    def vivos_quita(self, pos):
        vv = self.vivos.get(pos.tk)
        if vv:
            vv.discard(pos)

    def _finaliza_tk(self, tk):
        lv = self.live.get(tk)
        if not lv:
            return
        for rec in lv:
            self._finaliza(rec)
        lv.clear()

    def _finaliza_todo(self):
        for tk in list(self.live):
            self._finaliza_tk(tk)

    def terminar(self):
        self._finaliza_todo()
        return super().terminar()

    # ---- rasgos
    def _suma(self, fl, t, w):
        i = bisect.bisect_right(fl.t, t - w)
        s = 0.0
        for j in range(i, len(fl.t)):
            if fl.t[j] <= t:
                s += fl.s[j]
        return s

    def _feats(self, tk, m, t, bid, ask, bsz, asz, T):
        f = [NAN] * NF
        h = self.hist[tk]
        f[FI["bid"]] = bid / 1000.0
        f[FI["ask"]] = ask / 1000.0
        f[FI["spr"]] = (ask - bid) / 10.0
        f[FI["lbsz"]] = math.log1p(max(bsz, 0.0))
        f[FI["lasz"]] = math.log1p(max(asz, 0.0))
        f[FI["imb"]] = (bsz - asz) / (bsz + asz) if bsz + asz > 0 else NAN
        f[FI["T"]] = T
        for nm, w in zip(("chg1", "chg5", "chg30"), WIN_MS):
            f[FI[nm]] = float(len(h.t) - bisect.bisect_right(h.t, t - w))
        n = len(h.t)
        if n:
            j = n - 1
            while j > 0 and h.b[j - 1] == h.b[j]:
                j -= 1
            f[FI["tsb"]] = (t - h.t[j]) / 1000.0
            j = n - 1
            while j > 0 and h.a[j - 1] == h.a[j]:
                j -= 1
            f[FI["tsa"]] = (t - h.t[j]) / 1000.0
        for nm, w in (("5", 5000), ("30", 30000)):
            s = h.en(t - w)
            if s is not None:
                f[FI["dbid" + nm]] = (bid - s[0]) / 10.0
                f[FI["dask" + nm]] = (ask - s[1]) / 10.0
        par = self.par.get(tk)
        tp = self.top.get(par) if par is not None else None
        if tp is not None:
            f[FI["par_bid"]] = tp[0] / 1000.0
            f[FI["par_ask"]] = tp[1] / 1000.0
            f[FI["pair_gap"]] = (tp[1] + bid - 1000) / 10.0
        hit, lift = self.hit.get(tk), self.lift.get(tk)
        if hit is not None:
            for nm, w in zip(("hit1", "hit5", "hit30"), WIN_MS):
                f[FI[nm]] = self._suma(hit, t, w)
            i5 = bisect.bisect_right(hit.t, t - 5000)
            i30 = bisect.bisect_right(hit.t, t - 30000)
            f[FI["nhit5"]] = float(sum(1 for j in range(i5, len(hit.t)) if hit.t[j] <= t))
            f[FI["nhit30"]] = float(sum(1 for j in range(i30, len(hit.t)) if hit.t[j] <= t))
            f[FI["hitb30"]] = float(sum(hit.s[j] for j in range(i30, len(hit.t)) if hit.t[j] <= t and hit.p[j] < bid))
            j = bisect.bisect_right(hit.t, t) - 1
            if j >= 0:
                f[FI["lhit_rel"]] = (hit.p[j] - bid) / 10.0
        else:
            for nm in ("hit1", "hit5", "hit30", "hitb30", "nhit5", "nhit30"):
                f[FI[nm]] = 0.0
        if lift is not None:
            f[FI["lift5"]] = self._suma(lift, t, 5000)
            f[FI["lift30"]] = self._suma(lift, t, 30000)
        else:
            f[FI["lift5"]] = f[FI["lift30"]] = 0.0
        lt = self.last_trade.get(tk)
        f[FI["tlast"]] = min((t - lt) / 1000.0, 300.0) if lt is not None else 300.0
        # Binance (signo: a favor del token = +)
        sg = 1.0 if m.lado == "YES" else -1.0
        p0 = self._px_en(m.coin, t)
        if p0:
            for nm, w in zip(("bn_r1", "bn_r5", "bn_r30"), WIN_MS):
                pw = self._px_en(m.coin, t - w)
                if pw:
                    f[FI[nm]] = sg * (p0 / pw - 1.0) * 1e4
            rets, prev = [], None
            for sec in range(30, -1, -1):
                pw = self._px_en(m.coin, t - sec * 1000)
                if pw and prev:
                    rets.append((pw / prev - 1.0) * 1e4)
                prev = pw if pw else prev
            if len(rets) >= 10:
                f[FI["bn_rv30"]] = float(np.std(rets))
            ts = self.xt[m.coin]
            f[FI["bn_n5"]] = float(len(ts) - bisect.bisect_right(ts, t - 5000))
        # 15m del mismo subyacente y lado
        fin15 = -(-m.fin // 900_000) * 900_000
        tok15 = self.b15.k15.get((m.coin, fin15, m.lado))
        if tok15 is not None:
            st = self.b15.estado(tok15, t)
            f[FI["seg15"]] = (fin15 - m.fin) / 300_000.0
            f[FI["T15"]] = (fin15 - t) / 1000.0
            if st is not None:
                b15, a15 = st
                if b15 > 0:
                    f[FI["b15"]] = b15 / 1000.0
                    f[FI["m15"]] = (b15 - ask) / 1000.0
                if a15 > 0:
                    f[FI["a15"]] = a15 / 1000.0
        # profundidad espejo (filas l): tamaño en los escalones 1-3 ticks por debajo del top
        if par is not None:
            for j, nm in ((1, "dq1"), (2, "dq2"), (3, "dq3")):
                sz, ok = self.lad.nivel(par, 1000 - (bid - j * S.TICK), t)
                if ok:
                    f[FI[nm]] = float(sz)
        f[FI["c_" + m.coin]] = 1.0
        for c in MONEDAS:
            if c != m.coin:
                f[FI["c_" + c]] = 0.0
        f[FI["lado_yes"]] = 1.0 if m.lado == "YES" else 0.0
        return f


# ---------------------------------------------------------------- lectura del registro m5 (con filas x)
def procesar(f, engines, lad, b15, dia_ini, monedas, max_lineas, t_corte, spawn_ms):
    mo = ColocMotor(engines, S.Externas(), lad, b15, dia_ini, monedas, spawn_ms)
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
                        bid, ask, bsz = S.mils(c[3]), S.mils(c[4]), float(c[5])
                    except (ValueError, IndexError):
                        mo.libro_vacio(tk, t_rx)
                        continue
                    try:
                        asz = float(c[6])
                    except (ValueError, IndexError):
                        asz = 0.0
                    mo.q(tk, bid, ask, bsz, t_rx - S.FEED_MS, t_rx, asz)
                elif tp == "t,":
                    c = ln.split(",")
                    tk = c[2]
                    if tk not in mo.meta:
                        continue
                    try:
                        t_ex, p, side, sz = int(c[1]), S.mils(c[3]), c[4], float(c[5])
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
                    mo.t(tk, p, side, sz, t_rx - S.FEED_MS, mo.t_ult)
                elif tp == "k,":
                    mo.k(ln.split(","))
                elif tp == "x,":
                    c = ln.split(",")
                    try:
                        t_rx = int(c[7])
                        px = float(c[3])
                    except (ValueError, IndexError):
                        continue
                    if t_corte and t_rx > t_corte:
                        break
                    mo.reloj(t_rx)
                    coin = SYM2COIN.get(c[2])
                    if coin is not None and (monedas is None or coin in monedas):
                        mo.x(coin, t_rx, px)
        except (EOFError, OSError) as e:
            print(f"  {Path(f).name}: fichero truncado ({type(e).__name__}) tras {n} líneas", file=sys.stderr)
            mo.st["truncado"] = 1
    mo.st["lineas"] = n
    mo.terminar()
    return mo


def cargar_ladders(d, monedas, t_corte, log):
    """Solo filas l (3 niveles de ask); se descartan las L (libro completo BTC desde 14-Oct) para igualar los 9 días y ahorrar RAM."""
    lad = H.Ladders()
    fs = H.ficheros_l(d, (H.ARCHIVO_L, H.CRUDO_L))
    for f in fs:
        kcoin = {}
        n = 0
        try:
            with gzip.open(f, "rt", errors="replace") as fh:
                for ln in fh:
                    tp = ln[:2]
                    if tp == "k,":
                        c = ln.split(",")
                        if len(c) >= 8:
                            kcoin[c[2]] = c[3]
                    elif tp == "l,":
                        lad.add(ln, monedas, kcoin if monedas else None)
                        if t_corte:
                            n += 1
                            if n % 4096 == 0:
                                try:
                                    if int(ln.rsplit(",", 1)[1]) > t_corte:
                                        break
                                except ValueError:
                                    pass
        except (EOFError, OSError) as e:
            log(f"  ladders: {Path(f).name} truncado ({type(e).__name__}); se usa lo leído")
    return lad, fs


# ---------------------------------------------------------------- empaquetado, caché y cobertura
def empaquetar(mo, des):
    n = len(mo.d_meta)
    mk = np.array([x[0] for x in mo.d_meta], dtype="U12") if n else np.array([], dtype="U12")
    lado = np.array([x[1] for x in mo.d_meta], dtype=np.int8)
    coin = np.array([x[2] for x in mo.d_meta], dtype=np.int8)
    fin = np.array([x[3] for x in mo.d_meta], dtype=np.int64)
    tq = np.array([x[4] for x in mo.d_meta], dtype=np.int64)
    tramo = np.array([x[5] for x in mo.d_meta], dtype=np.int16)
    comp = np.array([1 if mo.mercado_completo(x[3] * 1000, x[5]) else 0 for x in mo.d_meta], dtype=np.int8)
    win = np.array([(-1 if x[0] not in des else (1 if (des[x[0]] == "YES") == bool(x[1]) else 0)) for x in mo.d_meta], dtype=np.int8)
    X = np.frombuffer(mo.d_feat, dtype=np.float32).reshape(n, NF).copy() if n else np.zeros((0, NF), np.float32)
    d = {"mkt": mk, "lado_yes": lado, "coin": coin, "fin_s": fin, "tq": tq, "tramo": tramo, "completo": comp, "win": win, "X": X}
    for k in KS:
        d[f"av{k}"] = np.frombuffer(mo.l_av[k], dtype=np.int8).copy()
        d[f"lleno{k}"] = np.frombuffer(mo.l_lleno[k], dtype=np.float32).copy()
        d[f"coste{k}"] = np.frombuffer(mo.l_coste[k], dtype=np.float32).copy()
        d[f"reb{k}"] = np.frombuffer(mo.l_reb[k], dtype=np.float32).copy()
        d[f"tf{k}"] = np.frombuffer(mo.l_tf[k], dtype=np.float32).copy()
        d[f"nord{k}"] = np.frombuffer(mo.l_nord[k], dtype=np.int16).copy()
        d[f"p0{k}"] = np.frombuffer(mo.l_p0[k], dtype=np.int16).copy()
        d[f"known{k}"] = np.frombuffer(mo.l_known[k], dtype=np.int8).copy()
    return d


def guardar_npz(ruta, d):
    tmp = ruta.with_name(ruta.name + f".tmp{os.getpid()}")
    with open(tmp, "wb") as fh:
        np.savez_compressed(fh, **d)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, ruta)


def validar(d):
    """Unicidad (mkt, lado, tq) y coherencia de columnas; -> lista de problemas."""
    pr = []
    n = len(d["mkt"])
    for k, v in d.items():
        if len(v) != n:
            pr.append(f"longitud {k}")
    claves = collections.Counter(zip(d["mkt"].tolist(), d["lado_yes"].tolist(), d["tq"].tolist()))
    dup = [c for c, v in claves.items() if v > 1]
    if dup:
        pr.append(f"claves duplicadas {dup[:3]}")
    return pr


def cache_valida(out, dia):
    meta, f = out / f"meta_{dia}.json", out / f"dp_{dia}.npz"
    if not (meta.exists() and f.exists()):
        return None
    try:
        m = json.loads(meta.read_text())
        if m.get("script_sha") != sha_codigo() or m.get("params_hash") != params_hash() or m.get("cobertura_des", 0) < 0.99:
            return None
        if S.sha_fichero(f) != m.get("sha_npz"):
            return None
        return m
    except (ValueError, OSError):
        return None


def mem_disponible_mb():
    return S.mem_disponible_mb()


def esperar_recursos(log, max_horas=20.0, mem_min=2500.0, load_max=16.0, forzar_horario=False):
    """Espera (10 min entre intentos) a: MemAvailable > mem_min MB, load1 < load_max, fuera de 06:00-09:15Z. -> True si hay hueco."""
    t0 = time.time()
    while True:
        now = datetime.now(timezone.utc)
        hm = now.hour * 60 + now.minute
        try:
            load = float(open("/proc/loadavg").read().split()[0])
        except OSError:
            load = 0.0
        mem = mem_disponible_mb()
        en_franja = HORA_BLOQUEO[0] <= hm < HORA_BLOQUEO[1] and not forzar_horario
        if mem > mem_min and load < load_max and not en_franja:
            return True
        if time.time() - t0 > max_horas * 3600:
            return False
        log(f"espera recursos: MemAvailable {mem:.0f} MB, load {load:.1f}, franja {en_franja}")
        time.sleep(600)


def correr_dia(d, out, a, log):
    t_ini = time.time()
    f5 = S.VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    est = {"dia": d, "estado": "FALTA_ENTRADA", "inicio": datetime.now(timezone.utc).isoformat()}
    if not f5.exists():
        return est, None
    monedas = set(a.monedas.split(",")) if a.monedas else None
    dia_ini = int(datetime.fromisoformat(d + "T00:00:00+00:00").timestamp() * 1000)
    t_corte = dia_ini + a.recorte_min * 60_000 if a.recorte_min else None
    b15 = leer_b15(d, out, log, t_corte, a.max_lineas_ext)
    log(f"{d}: b15 {len(b15.q)} tokens 15m con libro, {len(b15.k15)} mercados 15m ({time.time() - t_ini:.0f}s)")
    lad, fs = cargar_ladders(d, monedas, t_corte, log)
    log(f"{d}: ladders {len(fs)} ficheros, {lad.n_l} filas l, {len(lad.tokens)} tokens ({time.time() - t_ini:.0f}s)")
    engines = [H.EngD(0, "DEEP", 1, "CONS"), H.EngD(1, "DEEP", 2, "CONS"), H.EngD(2, "JOIN", 0, "CONS")]
    for i, e in enumerate(engines):
        e.idx = i
    mo = procesar(f5, engines, lad, b15, dia_ini, monedas, a.max_lineas, t_corte, a.spawn_ms)
    base = mo.filas_deep(d)
    mids = set(x[0] for x in mo.d_meta) | {r["mkt"] for r in base}
    des = S.desenlaces_oficiales(mids) if mids else {}
    cob = (sum(1 for m in mids if m in des) / len(mids)) if mids else 1.0
    dp = empaquetar(mo, des)
    pr = validar(dp)
    if pr:
        raise RuntimeError(f"{d}: {pr}")
    est.update({"estado": "OK", "lineas": mo.st["lineas"], "tramos": [[x, y] for x, y in mo.tramos], "decisiones": int(len(dp["mkt"])),
                "mercados": len(mids), "cobertura_des": cob, "contadores": dict(mo.st), "ladders": {"ficheros": [x.name for x in fs], "filas_l": lad.n_l},
                "segundos": round(time.time() - t_ini, 1), "base_unidades": len(base)})
    if a.recorte_min or a.max_lineas:
        est["estado"] = "HUMO_NO_CACHEADO"
        return est, (dp, base, des)
    if cob < 0.99:
        est["estado"] = "COBERTURA_DES_BAJA"
        log(f"{d}: cobertura de desenlaces {cob:.1%} < 99 %: no se cachea")
        return est, (dp, base, des)
    ruta = out / f"dp_{d}.npz"
    guardar_npz(ruta, dp)
    S.escribir_gz_atomico(out / f"base_{d}.csv.gz", [H.CAB] + [H.fila_csv(r, des) for r in base])
    est.update({"sha_npz": S.sha_fichero(ruta), "script_sha": sha_codigo(), "params_hash": params_hash()})
    S.escribir_atomico(out / f"meta_{d}.json", json.dumps(est, indent=1, default=str))
    est["estado"] = "COMPLETO"
    return est, (dp, base, des)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default="2026-10-05,2026-10-06,2026-10-07,2026-10-08,2026-10-09,2026-10-10,2026-10-14,2026-10-15,2026-10-16")
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--monedas", default="")
    ap.add_argument("--recorte-min", type=int, default=0)
    ap.add_argument("--max-lineas", type=int, default=0)
    ap.add_argument("--max-lineas-ext", type=int, default=0)
    ap.add_argument("--spawn-ms", type=int, default=SPAWN_MS)
    ap.add_argument("--cache-desenlaces", default="")
    ap.add_argument("--esperar", action="store_true", help="esperar hueco de recursos antes de cada día (10 min entre intentos)")
    ap.add_argument("--forzar-horario", action="store_true")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    dias = [d for d in a.dias.split(",") if d]
    job = f"coloc_{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}"
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
    man = {"job_id": job, "script": str(Path(__file__).resolve()), "script_sha256": sha_codigo(), "params": params_dict(),
           "params_hash": params_hash(), "dias_previstos": dias, "inicio": datetime.now(timezone.utc).isoformat(), "estado": "EN_CURSO",
           "entradas": {}, "dias": {}, "comando": " ".join(sys.argv)}
    for d in dias:
        f = S.VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
        man["entradas"][d] = {"m5_registro": {"bytes": f.stat().st_size, "mtime": f.stat().st_mtime} if f.exists() else None,
                              "ficheros_l": [x.name for x in H.ficheros_l(d, (H.ARCHIVO_L, H.CRUDO_L))]}

    def guarda():
        txt = json.dumps(man, indent=1, default=str)
        S.escribir_atomico(out / "run_manifest.json", txt)
        S.escribir_atomico(out / f"run_manifest_{job}.json", txt)

    guarda()
    pesado = not (a.recorte_min or a.max_lineas)
    log(f"inicio {job}: {len(dias)} días, hash {man['script_sha256'][:12]}, params {man['params_hash']}")
    errores = 0
    for d in dias:
        try:
            m = None if not pesado else cache_valida(out, d)
            if m:
                man["dias"][d] = {"estado": "SALTADO_CACHE_VALIDA", "decisiones": m["decisiones"], "cobertura_des": m["cobertura_des"]}
                log(f"{d}: caché válida ({m['decisiones']} decisiones): se salta")
                guarda()
                continue
            if pesado:
                if a.esperar:
                    hueco = esperar_recursos(log, forzar_horario=a.forzar_horario)
                else:
                    now = datetime.now(timezone.utc)
                    hm = now.hour * 60 + now.minute
                    hueco = a.forzar_horario or not (HORA_BLOQUEO[0] <= hm < HORA_BLOQUEO[1])
                    if hueco and (mem_disponible_mb() < 2500.0 or float(open("/proc/loadavg").read().split()[0]) >= 16.0):
                        hueco = False
                if not hueco:
                    man["dias"][d] = {"estado": "BLOCKED", "motivo": "recursos u horario"}
                    log(f"{d}: BLOCKED (recursos u horario)")
                    guarda()
                    continue
            est, _ = correr_dia(d, out, a, log)
            man["dias"][d] = {k: est.get(k) for k in ("estado", "decisiones", "mercados", "cobertura_des", "lineas", "tramos", "segundos",
                                                      "contadores", "ladders", "base_unidades")}
            log(f"{d}: {est['estado']} | {est.get('decisiones')} decisiones, {est.get('mercados')} mercados, cobertura des "
                f"{est.get('cobertura_des', 0):.1%}, {est.get('segundos')} s | {est.get('contadores')}")
        except Exception as e:
            errores += 1
            man["dias"][d] = {"estado": "FALLO", "error": f"{type(e).__name__}: {e}"}
            log(f"{d}: FALLO {type(e).__name__}: {e}")
        guarda()
    ok = [d for d in dias if man["dias"].get(d, {}).get("estado") in ("COMPLETO", "SALTADO_CACHE_VALIDA")]
    man["estado"] = ("HUMO" if not pesado else "COMPLETE" if len(ok) == len(dias) else "PARTIAL" if ok else "FAILED" if errores else "BLOCKED")
    man["fin"] = datetime.now(timezone.utc).isoformat()
    guarda()
    log(f"ESTADO FINAL: {man['estado']} (válidos {len(ok)}/{len(dias)}: {ok}; fallos {errores})")
    return 0 if man["estado"] in ("COMPLETE", "HUMO") else 1


if __name__ == "__main__":
    sys.exit(main())
