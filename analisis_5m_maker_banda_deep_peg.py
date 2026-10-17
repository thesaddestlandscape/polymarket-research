#!/usr/bin/env python3
"""5m barato H35 DEEP_PEG (+H37 salida maker, +H38 markout) -- motor NUEVO del simulador maker en la banda barata.
SOLO LECTURA / simulación (OK Javi 17-Oct). No manda órdenes, no firma, no toca producción ni procesos.

VERSIÓN NUEVA: este fichero IMPORTA `analisis_5m_maker_banda_simulador` (commit 41ac3b85ae: Motor, Externas, Seg, Pos, reloj de
recepción, metricas, desenlaces) y no lo modifica; los motores JOIN/IMPROVE de aquí son los de esa versión SIN cambios de
comportamiento (prueba de regresión en tests) y sus cachés viven en OTRO directorio (la calibración H26 sigue intacta).

ESPECIFICACIÓN CONGELADA (REGISTRO_HIPOTESIS H35/H37/H38, 17-Oct; cambiarla = versión nueva + OOS nuevo):
 DEEP_PEG  Por (mercado, lado), T en (60, 300] s, bid top en (0,11, 0,30]. Puja de COMPRA en top − k·0,01, k en {1, 2} (se elige SOLO en
           DESC = 05-10 Oct, por moneda y global, entre las pujas de cola CONS). Repega cuando cambia el top (cancelación efectiva
           +60 ms, alta +68 ms, bloqueo en vuelo de 68 ms). Nunca mejora el top (precio < top siempre; con bid subcentavo se baja
           al céntimo inferior). SH = 5 acciones. Parada a T = 60 s (+60 ms). Sin defensa (C0).
 Relleno   CONSERVADOR: solo operaciones (reloj de RECEPCIÓN) que ATRAVIESAN nuestro nivel (precio equivalente < el nuestro: la barrida
           vació el nivel -> relleno completo) o que igualan el nivel y SUPERAN la cola que teníamos delante. Cola = tamaño ya
           presente en el nivel a la hora del ALTA (alta = decisión + 68 ms), leído del registro ms (ver abajo). Si falta ese dato:
           `cola_desconocida` (contada) y cola INFINITA en CONS (solo rellenan las barridas) / cola 0 en OPT.
 Profundidad: el registro NO guarda niveles de BID: las filas l (3 niveles) y L (libro completo, BTC desde 14-Oct 12:26Z) son niveles
           de ASK, y solo de los 5m que cierran con un 15m (1 de cada 3) en sus últimos 305 s, y SOLO en los crudos maker_ms_* (el
           m5_registro del archivo NO las lleva: se leen del archivo filtrado registro_5m_barato/ y de maker_ms_crudo/). Se usa el
           espejo: el bid del YES a p equivale al ask del NO a 1−p (verificado con `--equivalencia`, ver informe) -> el escalón de
           bid del token T en el precio P es el ask del token contrario en 1000−P. 2 de cada 3 mercados: cola_desconocida.
 Brazo BN  (secundario, declarado) DEEP_PEG solo en las decisiones en que Binance (filas x, hora de RECEPCIÓN c[7]) se ha movido
           >= BN_BPS (3) bps EN CONTRA del lado (YES: baja; NO: sube) en los W ms previos (W parámetro); si en la decisión no se
           cumple, se cancela lo vivo. Solo información anterior a la decisión.
 Placebos  (mismo informe) DEEP_FIJO (nivel top−k·0,01 de la primera decisión, SIN repegar), JOIN e IMPROVE de la versión actual en los
           mismos mercados (tabla también restringida a las unidades donde DEEP_PEG puso orden).
 H38       markout +5/+30/+120 s por € de cada relleno (mid del token por RECEPCIÓN; después del cierre = missing, nunca 0): PARADA
           temprana, nunca promoción. En cada motor.
 H37       Tras cada relleno de DEEP_PEG y de JOIN, ask maker a entrada + δ (δ en {0,01; 0,02}) vivo 10 s desde su alta (+68 ms);
           si no se llena, se mantiene a resolución. Relleno de la salida con el mismo criterio conservador (cola del nivel de ask
           del token: top ask q si coincide, 0 si mejora el ask, fila l/L si está más arriba; si no hay dato: cola infinita CONS / 0 OPT).
           La salida se decide EXIT_SETTLE_MS=100 ms después de la recepción del relleno, con el libro vigente entonces (medido 14-Oct, n=49 barridas:
           el top se actualiza p50 3 ms / p99 31 ms tras el print). Sin comisión de salida ni rebate. Si a+δ cruza el bid (ejecutaría como tomador) no se pone la salida (se mantiene).
 Métricas  Unidad mercado-lado; desenlace OFICIAL con cobertura; EV/€ agrupado, IC90 por DÍAS y por CIERRE (remuestreo de cierres),
           sin mejor día, sin los 5 mejores mercados, días +, PnL total (EV titular SIN rebate; rebate aparte).
 Gate H35  (por moneda, OOS >= 14-Oct; los días 11-13 del hallazgo NO cuentan): n_rellenas >= 40, EV/€ >= +0,05, IC90 días > 0 e IC90 cierre
           > 0, sin mejor día > 0, sin 5 mejores mercados > 0, >= 4/6 días +, markout +30 s > 0; DEEP_FIJO y JOIN por debajo, IMPROVE
           negativo. (Esto es lo que hace falta ANTES de hablar de forward; no es un veredicto.)

Contrato de trabajo largo: run_manifest.json, caché durable ATÓMICA por día (unidades_D.csv.gz + meta_D.json con hash de ESTE fichero y del
simulador base), claves únicas (dia, motor, mkt, lado, tramo), cobertura, resumen parcial, log con hora, estado final.
Uso:   nice -n 19 ionice -c3 python3 analisis_5m_maker_banda_deep_peg.py [--dias D1,D2] [--monedas BTC] [--out DIR] [--solo-informe]
Humo:  --dias 2026-10-14 --monedas BTC --recorte-min 30 --max-lineas-ext 2000000 --out <dir temporal> --cache-desenlaces <copia>
Equivalencia YES/NO:  --equivalencia FICHERO_REGISTRO_ARCHIVO [...]
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
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_5m_maker_banda_simulador as S  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5_maker_banda_deep_peg")
ARCHIVO_L = Path("/mnt/HC_Volume_106538179/registro_5m_barato")      # archivo filtrado (k,q,t,x,l,L) desde 05-Oct
CRUDO_L = Path("/mnt/HC_Volume_106538179/maker_ms_crudo")            # crudos completos 12-17 Oct
DIAS_DESC = [f"2026-10-{d:02d}" for d in range(5, 11)]
DIAS_EXCL = ["2026-10-11", "2026-10-12", "2026-10-13"]               # días del hallazgo: ni DESC ni OOS
OOS_DESDE = "2026-10-14"
DIAS_DEF = DIAS_DESC + [f"2026-10-{d:02d}" for d in range(14, 17)]
MONEDAS = S.MONEDAS
P_TOP_LO = 110                       # bid top > 0,11
K_GRID = (1, 2)
DELTAS = (10, 20)                    # milésimas: 0,01 y 0,02
EXIT_MS = 10_000
EXIT_SETTLE_MS = 100                 # la salida se decide con el libro 100 ms después de la recepción del relleno (el top se actualiza tras la barrida)
MARK_S = (5, 30, 120)
BN_BPS, BN_W = 3.0, (1000, 5000)
DEEPFAM = ("DEEP", "DEEPFIJO", "DEEPBN")
INF, EPS = float("inf"), 1e-9
MIN_FILL_COIN, MIN_FILL_ALL = 30, 150
GATE = {"n_fill": 40, "ev": 0.05, "dias_pos": 4}
VERSION = "deep_peg_v1"


# ---------------------------------------------------------------- escalones por niveles (espejo de bids a partir de los asks del contrario)
class Ladders:
    """Filas l (3 niveles de ask) y L (libro de ask completo) por token, con hora de RECEPCIÓN. `nivel(tk, pn, t)` = tamaño en el
    escalón de ASK `pn` (milésimas) del token `tk` a la hora t -> (tamaño, conocido). El escalón de BID del token T a precio P es
    el ask del contrario en 1000−P: `nivel(par[T], 1000−P, t)`. Conocido = el escalón está listado, o se sabe que está vacío
    (cae entre niveles listados o el libro tiene menos de 3 niveles); desconocido = más profundo que el 3er nivel de una fila l
    sin fila L, o no hay ninguna fila anterior."""

    def __init__(self):
        self._l = collections.defaultdict(lambda: [array("q"), array("h"), array("f"), array("h"), array("f"), array("h"), array("f")])
        self._L = collections.defaultdict(lambda: ([], []))
        self._fl, self._fL = {}, {}
        self._cacheL = {}
        self.n_l = self.n_L = 0
        self.tokens = set()

    def add(self, ln, monedas=None, kcoin=None):
        tp = ln[:2]
        if tp == "l,":
            c = ln.rstrip("\n").split(",")
            if len(c) < 10:
                return
            tk = c[2]
            if monedas and kcoin is not None and kcoin.get(tk, next(iter(monedas))) not in monedas:
                return
            try:
                t = int(c[9])
                niv = []
                for i in (3, 5, 7):
                    niv.append((S.mils(c[i]), float(c[i + 1])) if c[i] != "" else (-1, 0.0))
            except ValueError:
                return
            a = self._l[tk]
            a[0].append(t)
            for j, (p, s) in enumerate(niv):
                a[1 + 2 * j].append(p)
                a[2 + 2 * j].append(s)
            self.n_l += 1
            self.tokens.add(tk)
        elif tp == "L,":
            c = ln.rstrip("\n").split(",")
            if len(c) < 5:
                return
            tk = c[2]
            if monedas and kcoin is not None and kcoin.get(tk, next(iter(monedas))) not in monedas:
                return
            try:
                t = int(c[4])
            except ValueError:
                return
            self._L[tk][0].append(t)
            self._L[tk][1].append(c[3])
            self.n_L += 1
            self.tokens.add(tk)

    @classmethod
    def cargar(cls, ficheros, monedas=None, t_corte=None, log=None):
        lad = cls()
        for f in ficheros:
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
                        elif tp == "l," or tp == "L,":
                            lad.add(ln, monedas, kcoin if monedas else None)
                            if t_corte and tp == "l,":
                                n += 1
                                if n % 4096 == 0:
                                    try:
                                        if int(ln.rsplit(",", 1)[1]) > t_corte:
                                            break
                                    except ValueError:
                                        pass
            except (EOFError, OSError) as e:
                if log:
                    log(f"  ladders: {Path(f).name} truncado ({type(e).__name__}); se usa lo leído")
        return lad

    def _fin_l(self, tk):
        """Arrays de la fila l del token ordenados por hora de recepción (se reordena solo si hace falta)."""
        if tk in self._fl:
            return self._fl[tk]
        a = self._l.get(tk)
        if a is not None:
            t = np.asarray(a[0], dtype=np.int64)
            if len(t) > 1 and (np.diff(t) < 0).any():
                o = np.argsort(t, kind="stable")
                a = [np.asarray(x)[o].tolist() for x in a]
        self._fl[tk] = a
        return a

    def _fin_L(self, tk):
        r = self._fL.get(tk)
        if r is None:
            a = self._L.get(tk)
            if a is None:
                return None
            t = np.asarray(a[0], dtype=np.int64)
            o = np.argsort(t, kind="stable")
            r = self._fL[tk] = (t[o].tolist(), [a[1][i] for i in o])
        return r

    def _parseL(self, tk, i, s):
        key = (tk, i)
        d = self._cacheL.get(key)
        if d is None:
            if len(self._cacheL) > 512:
                self._cacheL.clear()
            d = {}
            for part in s.split(";"):
                if ":" in part:
                    p, z = part.split(":")
                    try:
                        d[S.mils(p)] = float(z)
                    except ValueError:
                        pass
            self._cacheL[key] = d
        return d

    def tiene(self, tk):
        return tk in self._l or tk in self._L

    def nivel(self, tk, pn, t):
        rl = self._fin_l(tk) if tk in self._l else None
        rL = self._fin_L(tk) if tk in self._L else None
        il = bisect.bisect_right(rl[0], t) - 1 if rl is not None else -1
        iL = bisect.bisect_right(rL[0], t) - 1 if rL is not None else -1
        if il < 0 and iL < 0:
            return None, False
        usarL = iL >= 0 and (il < 0 or rL[0][iL] >= rl[0][il])
        if usarL:
            return self._parseL(tk, iL, rL[1][iL]).get(pn, 0.0), True
        ps = [rl[1][il], rl[3][il], rl[5][il]]
        ss = [rl[2][il], rl[4][il], rl[6][il]]
        for p, s in zip(ps, ss):
            if p == pn:
                return float(s), True
        lista = [p for p in ps if p >= 0]
        if len(lista) < 3 or pn < lista[-1]:
            return 0.0, True                       # entre niveles listados / por debajo del mejor / libro sin más niveles
        if iL >= 0:                                 # más profundo que el 3º y existe una fila L anterior (algo más vieja): se usa
            return self._parseL(tk, iL, rL[1][iL]).get(pn, 0.0), True
        return None, False


def ficheros_l(dia, dirs=(ARCHIVO_L, CRUDO_L)):
    """Ficheros del registro con filas l/L del día: el primer directorio que tenga alguno (archivo filtrado antes que crudo)."""
    for d in dirs:
        fs = sorted(Path(d).glob(f"maker_ms_{dia}_*.csv.gz"))
        if fs:
            return fs
    return []


# ---------------------------------------------------------------- motores
class EngD(S.Eng):
    """Motor del simulador DEEP: fam en JOIN | IMPROVE | DEEP | DEEPFIJO | DEEPBN. JOIN/IMPROVE son los de la versión base."""

    def __init__(self, idx, fam, k, cola, bn=None, salida=False):
        if fam in ("JOIN", "IMPROVE"):
            pol = fam
        else:
            pol = f"{fam}_k{k}" + (f"_u{bn[0]:g}_w{bn[1]}" if bn else "")
        super().__init__(idx, pol, "C0", cola, S.SH_BASE, None, None)
        self.fam, self.k, self.bn, self.salida = fam, k, bn, salida


def construir_motores(ks=K_GRID, colas=("CONS", "OPT"), bn=True, bn_w=BN_W, bn_bps=BN_BPS, placebos=True):
    E = []

    def add(fam, k, cola, bn_=None, salida=False):
        E.append(EngD(len(E), fam, k, cola, bn_, salida))

    for k in ks:
        for cola in colas:
            add("DEEP", k, cola, salida=True)
    if bn:
        for k in ks:
            for w in bn_w:
                for cola in colas:
                    add("DEEPBN", k, cola, (bn_bps, w), salida=True)
    if placebos:
        for k in ks:
            for cola in colas:
                add("DEEPFIJO", k, cola)
        for cola in colas:
            add("JOIN", 0, cola, salida=True)
        if "CONS" in colas:
            add("IMPROVE", 0, "CONS")
    return E


class Exit:
    __slots__ = ("pos", "rec", "delta", "a", "act", "ceff", "cola", "vol", "fx", "tsum", "qty", "conocida")

    def __init__(self, pos, rec, delta, a, act, ceff, cola, conocida):
        self.pos, self.rec, self.delta, self.a, self.act, self.ceff, self.cola = pos, rec, delta, a, act, ceff, cola
        self.conocida = conocida
        self.vol = self.fx = self.tsum = 0.0
        self.qty = rec[1]


class DeepMotor(S.Motor):
    """Motor de la versión base ampliado: cola por escalón, DEEP/DEEP_FIJO/DEEP_BN, markout y salida maker. JOIN/IMPROVE: igual que la base."""

    def __init__(self, engines, ext, lad, dia_ini_ms=0, deltas=DELTAS, monedas=None, traza=False):
        super().__init__(engines, ext, dia_ini_ms, traza)
        self.lad, self.deltas = lad, tuple(deltas)
        self.monedas = set(monedas) if monedas else None
        self.asz = {}
        self.fl = {}                                    # pos -> [[t_fill, qty, precio_mils], ...]
        self.mo_pend = collections.defaultdict(list)    # token -> [(objetivo_ms, pos, fill_idx, h)]
        self.mo = {}                                    # pos -> {h: [pnl, cost, n, miss]}
        self.ex_live = collections.defaultdict(list)
        self.ex_pend = collections.defaultdict(list)    # token -> [(decisión_ms, pos, rec, delta)]
        self.ex_pos = {}
        self.cd = collections.Counter()                 # pos -> pujas con cola desconocida
        self.cc = collections.Counter()                 # pos -> pujas con cola conocida

    # ---- mapa (filtro de monedas)
    def k(self, c):
        if self.monedas is not None and len(c) >= 8 and c[3] not in self.monedas:
            return
        super().k(c)

    def cerrar_tramo(self):
        if self.t0 is not None:
            for tk, lst in list(self.mo_pend.items()):
                top = self.top.get(tk)
                for it in lst:
                    self._mo_set(it, top if (top and it[0] <= self.t_ult) else None)
            self.mo_pend.clear()
            for tk in list(self.ex_pend):
                self._colocar_pend(tk, INF, self.top.get(tk), self.asz.get(tk, 0.0))
            self.ex_live.clear()
        super().cerrar_tramo()

    # ---- markout
    def _mo_set(self, it, st):
        target, pos, idx, h = it
        d = self.mo.setdefault(pos, {x: [0.0, 0.0, 0, 0] for x in MARK_S})[h]
        rec = self.fl[pos][idx]
        fin = pos.meta.fin
        if st is None or target > fin or not (st[0] > 0 and st[1] > 0):
            d[3] += 1
            return
        mid = (st[0] + st[1]) / 2000.0
        pr = rec[2] / 1000.0
        d[0] += rec[1] * (mid - pr)
        d[1] += rec[1] * pr
        d[2] += 1

    def _mo_resolver(self, tk, prev, t_rx):
        lst = self.mo_pend.get(tk)
        if not lst:
            return
        resta = []
        for it in lst:
            if it[0] < t_rx:
                self._mo_set(it, prev)
            else:
                resta.append(it)
        if resta:
            self.mo_pend[tk] = resta
        else:
            del self.mo_pend[tk]

    # ---- cola por escalón
    def _cola(self, e, tk, precio, act):
        par = self.par.get(tk)
        if par is not None:
            sz, ok = self.lad.nivel(par, 1000 - precio, act)
            if ok:
                return float(sz), True
        return (INF if e.cola == "CONS" else 0.0), False

    def _post_deep(self, e, pos, tk, m, precio, t_rx, bid, bsz):
        self._post(e, pos, tk, m, precio, t_rx, bid, bsz)
        g = pos.cur
        cola, ok = self._cola(e, tk, precio, g.act)
        g.cola, g.pend = cola, False
        g.sprev = cola if (ok and cola > 0) else None
        if ok:
            self.cc[pos] += 1
            self.st["cola_conocida|" + e.nombre] += 1
        else:
            self.cd[pos] += 1
            self.st["cola_desconocida|" + e.nombre] += 1

    def _adv_deep(self, pos, t):
        """Cota optimista de cola (OPT): bajada del escalón no explicada por operaciones -> adelanta la fracción cola_restante/tamaño_previo."""
        par = self.par.get(pos.tk)
        if par is None:
            return
        for g in pos.segs:
            if g.ceff <= t:
                continue
            sz, ok = self.lad.nivel(par, 1000 - g.precio, t)
            if not ok:
                continue
            if g.sprev is not None and g.sprev > 0:
                canc = (g.sprev - sz) - g.volq
                if canc > EPS:
                    ahead = max(0.0, g.cola - g.adv - g.vol)
                    g.adv += canc * min(1.0, ahead / g.sprev)
            g.sprev = float(sz)
            g.volq = 0.0

    def _objetivo(self, bid, k):
        o = bid - k * S.TICK if bid % S.TICK == 0 else (bid // S.TICK - (k - 1)) * S.TICK
        return o if (S.P_LO <= o <= S.P_HI and o < bid) else None

    def _bn_cond(self, e, m, t):
        xs = self.ext.x.get(m.coin)
        if xs is None or not len(xs[0]):
            return False
        u, w = e.bn
        tx, px = xs
        i = int(np.searchsorted(tx, t, side="right")) - 1
        j = int(np.searchsorted(tx, t - w, side="right")) - 1
        if i < 0 or j < 0 or tx[j] < t - w - S.STALE_MS:
            return False
        ret = (px[i] / px[j] - 1.0) * 1e4
        return ret <= -u if m.lado == "YES" else ret >= u

    def _eval_deep(self, e, pl, tk, m, t_rx, bid, ask, bsz):
        pos = pl[e.idx]
        if pos is not None:
            if pos.completo:
                return
            if t_rx < pos.lock:
                self.espera.setdefault(tk, set()).add(e.idx)
                return
            if e.fam == "DEEPFIJO":
                return                                   # nunca repega
        objetivo = self._objetivo(bid, e.k)
        ok = objetivo is not None and objetivo < ask
        if ok and e.bn is not None:
            ok = self._bn_cond(e, m, t_rx)
        cur = pos.cur if pos is not None else None
        if cur is not None:
            if ok and objetivo == cur.precio:
                return
            self._cancelar(pos, t_rx, "recoloca" if ok else "capa")
        if not ok:
            return
        if pos is None:
            pos = pl[e.idx] = S.Pos(e, tk, m, len(self.tramos))
            pos.srcs = []
        self._post_deep(e, pos, tk, m, objetivo, t_rx, bid, bsz)

    # ---- libro (top) del token
    def q(self, tk, bid, ask, bsz, t_ex, t_rx, asz=0.0):
        m = self.meta.get(tk)
        if m is None:
            return
        prev = self.top.get(tk)
        self._mo_resolver(tk, prev, t_rx)
        if self.ex_pend.get(tk):
            self._colocar_pend(tk, t_rx, prev, self.asz.get(tk, 0.0))
        self.top[tk] = (bid, ask, bsz)
        self.asz[tk] = asz
        vv = self.vivos.get(tk)
        T = (m.fin - t_rx) * 0.001
        if vv:
            if T < S.T_MIN - 5:
                for pos in vv:
                    for g in pos.segs:
                        self._cuenta(pos, g)
                    pos.segs = []
                    pos.cur = None
                vv.clear()
            else:
                for pos in vv:
                    if pos.e.fam in DEEPFAM:
                        if pos.opt:
                            self._adv_deep(pos, t_ex)
                    elif pos.opt or t_ex <= pos.last_act:
                        self._libro(pos, bid, bsz, t_ex)
        if T <= S.T_MIN or T > S.T_MAX:
            return
        libro_ok = 0 < ask and bid < ask
        banda_j = libro_ok and S.P_LO < bid <= S.P_HI
        banda_d = libro_ok and P_TOP_LO < bid <= S.P_HI
        if vv:
            for pos in list(vv):
                fam = pos.e.fam
                if pos.cur is None or fam == "DEEPFIJO":
                    continue
                if not (banda_d if fam in DEEPFAM else banda_j):
                    self._cancelar(pos, t_rx, "banda")
        cambio = prev is None or prev[0] != bid or prev[1] != ask
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
            e = self.E[i]
            if e.fam in DEEPFAM:
                if banda_d:
                    self._eval_deep(e, pl, tk, m, t_rx, bid, ask, bsz)
            elif banda_j:
                S.Motor._eval(self, e, pl, tk, m, t_rx, bid, ask, bsz)

    # ---- operaciones
    def t(self, tk, p, side, sz, t_ex, t_rx):
        m = self.meta.get(tk)
        if m is None:
            return
        if side == "SELL":
            obj_b, pe_b, obj_s, pe_s = tk, p, self.par.get(tk), (1000 - p)
        elif side == "BUY":
            obj_b = self.par.get(tk)
            pe_b = 1000 - p
            obj_s, pe_s = tk, p
        else:
            return
        if self.ex_pend:
            for tkp in (tk, self.par.get(tk)):
                if tkp is not None and self.ex_pend.get(tkp):
                    self._colocar_pend(tkp, t_rx, self.top.get(tkp), self.asz.get(tkp, 0.0))
        if obj_b is not None:
            self._fill_compra(obj_b, pe_b, sz, t_ex, t_rx, m)
        if obj_s is not None and self.ex_live.get(obj_s):
            self._fill_salida(obj_s, pe_s, sz, t_ex)

    def _fill_compra(self, obj, pe, sz, t_ex, t_rx, m):
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
                    pos.reb += f * S.REB * (g.precio / 1000.0) * (1 - g.precio / 1000.0)
                    pos.tsum += f * (m.fin - t_ex) / 1000.0
                    self.st["rellenos"] += 1
                    self._reg_fill(pos, obj, g.precio, f, t_ex, t_rx)
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

    def _reg_fill(self, pos, obj, precio, f, t_ex, t_rx):
        fl = self.fl.setdefault(pos, [])
        rec = [t_ex, f, precio]
        fl.append(rec)
        for h in MARK_S:
            self.mo_pend[obj].append((t_ex + h * 1000, pos, len(fl) - 1, h))
        if pos.e.salida:
            for d in self.deltas:
                self.ex_pend[obj].append((t_rx + EXIT_SETTLE_MS, pos, rec, d))

    # ---- H37: salida maker
    def _colocar_pend(self, obj, ahora, top, asz):
        """Coloca las salidas cuya hora de decisión (recepción del relleno + EXIT_SETTLE_MS) es anterior a `ahora`, con el libro `top`
        vigente en esa hora (el estado anterior a la fila q que llega en `ahora`)."""
        lst = self.ex_pend.get(obj)
        if not lst:
            return
        resta = []
        for it in lst:
            if it[0] < ahora:
                self._nueva_salida(it[1], obj, it[2], it[3], it[0], top, asz)
            else:
                resta.append(it)
        if resta:
            self.ex_pend[obj] = resta
        else:
            del self.ex_pend[obj]

    def _nueva_salida(self, pos, obj, rec, delta, t_dec, top, asz):
        if not top:
            self.st["salida_sin_libro"] += 1
            return
        bid, ask, _ = top
        a = rec[2] + delta
        if a <= bid or a >= 1000:
            self.st["salida_cruza_o_fuera"] += 1
            return
        act = t_dec + S.LAT_POST_MS
        ceff = act + EXIT_MS + S.LAT_CANCEL_MS
        if a < ask:
            cola, ok = 0.0, True
        elif a == ask:
            cola, ok = float(asz), True
        else:
            sz, ok = self.lad.nivel(obj, a, act)
            cola = float(sz) if ok else (INF if pos.e.cola == "CONS" else 0.0)
        x = Exit(pos, rec, delta, a, act, ceff, cola, ok)
        self.ex_live[obj].append(x)
        self.ex_pos.setdefault(pos, []).append(x)

    def _fill_salida(self, obj, pe, sz, t_ex):
        keep = []
        for x in self.ex_live[obj]:
            if t_ex > x.ceff:
                continue
            if t_ex >= x.act:
                rem = x.qty - x.fx
                f = 0.0
                if pe > x.a:
                    top = self.top.get(obj)
                    f = rem if (not top or x.a >= top[1]) else min(rem, sz)
                elif pe == x.a:
                    x.vol += sz
                    f = min(rem, max(0.0, x.vol - x.cola - x.fx))
                if f > EPS:
                    x.fx += f
                    x.tsum += f * (t_ex - x.rec[0])
            if x.fx < x.qty - EPS:
                keep.append(x)
        self.ex_live[obj] = keep

    # ---- salida de filas
    def filas_deep(self, dia):
        out = []
        for pos in self.pos_ant:
            if pos.norders == 0:
                continue
            m, e = pos.meta, pos.e
            fl = self.fl.get(pos, [])
            fin = m.fin
            r = {"dia": dia, "motor": e.nombre, "fam": e.fam, "k": e.k, "act": m.coin, "mkt": m.mkt, "lado": m.lado, "tramo": pos.tramo,
                 "completo": int(self.mercado_completo(fin, pos.tramo)), "fin_s": fin // 1000, "norders": pos.norders, "ncap": pos.ncap,
                 "nfills": len(fl), "cola_desc": self.cd.get(pos, 0), "cola_con": self.cc.get(pos, 0), "lleno": round(pos.lleno, 4),
                 "coste": round(pos.coste, 6), "precio_m": round(pos.coste / pos.lleno, 4) if pos.lleno > 0 else "",
                 "rebate": round(pos.reb, 6), "t_libro_s": round(pos.t_libro, 3), "cap_s": round(pos.cap_s, 3),
                 "t_fill_s": round(pos.tsum / pos.lleno, 1) if pos.lleno > 0 else ""}
            mo = self.mo.get(pos, {})
            for h in MARK_S:
                d = mo.get(h, [0.0, 0.0, 0, 0])
                r[f"mo{h}_pnl"], r[f"mo{h}_cost"], r[f"mo{h}_n"], r[f"mo{h}_miss"] = round(d[0], 6), round(d[1], 6), d[2], d[3]
            r["capm"] = round(sum(f[1] * f[2] / 1000.0 * (fin - f[0]) / 60000.0 for f in fl), 4)
            if e.salida:
                for dl in self.deltas:
                    xs = [x for x in self.ex_pos.get(pos, []) if x.delta == dl]
                    fxs = {id(x.rec): x for x in xs}
                    xfq = sum(x.fx for x in xs)
                    xcost = sum(x.fx * x.rec[2] / 1000.0 for x in xs)
                    xpnl = sum(x.fx * (x.a - x.rec[2]) / 1000.0 for x in xs)
                    capm = 0.0
                    for f in fl:
                        x = fxs.get(id(f))
                        fx = x.fx if x else 0.0
                        if x and fx > 0:
                            capm += x.rec[2] / 1000.0 * x.tsum / 60000.0
                        capm += (f[1] - fx) * f[2] / 1000.0 * (fin - f[0]) / 60000.0
                    r[f"x{dl}_n"], r[f"x{dl}_fq"], r[f"x{dl}_cost"] = len(xs), round(xfq, 4), round(xcost, 6)
                    r[f"x{dl}_pnl"], r[f"x{dl}_capm"] = round(xpnl, 6), round(capm, 4)
            out.append(r)
        return out


COLS = (["dia", "motor", "fam", "k", "act", "mkt", "lado", "tramo", "completo", "fin_s", "norders", "ncap", "nfills", "cola_desc", "cola_con",
         "lleno", "coste", "precio_m", "rebate", "t_libro_s", "cap_s", "t_fill_s"]
        + [f"mo{h}_{c}" for h in MARK_S for c in ("pnl", "cost", "n", "miss")] + ["capm"]
        + [f"x{d}_{c}" for d in DELTAS for c in ("n", "fq", "cost", "pnl", "capm")])
CAB = ",".join(COLS + ["des", "pnl"]) + "\n"


def fila_csv(r, des):
    d = des.get(r["mkt"], "")
    pnl = "" if not d else round((r["lleno"] if d == r["lado"] else 0.0) - r["coste"], 6)
    return ",".join(str(r.get(c, "")) for c in COLS) + f",{d},{pnl}\n"


# ---------------------------------------------------------------- lectura del registro (m5) con asz y sin filas l/L
def procesar_registro(f, ext, lad, engines, dia_ini_ms, monedas=None, max_lineas=None, t_corte=None, deltas=DELTAS, traza=False):
    mo = DeepMotor(engines, ext, lad, dia_ini_ms, deltas, monedas, traza)
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


# ---------------------------------------------------------------- hash, parámetros, caché por día
def sha_codigo():
    return hashlib.sha256((S.sha_fichero(Path(__file__)) + S.sha_fichero(Path(S.__file__))).encode()).hexdigest()


def params_dict(engines, deltas):
    return {"version": VERSION, "P_TOP_LO": P_TOP_LO, "ks": sorted({e.k for e in engines if e.fam in DEEPFAM}), "deltas": list(deltas),
            "exit_ms": EXIT_MS, "mark_s": list(MARK_S), "bn": sorted({str(e.bn) for e in engines if e.bn}), "TICK": S.TICK,
            "T": [S.T_MIN, S.T_MAX], "LAT_POST_MS": S.LAT_POST_MS, "LAT_CANCEL_MS": S.LAT_CANCEL_MS, "FEED_MS": S.FEED_MS,
            "SH": S.SH_BASE, "motores": [e.nombre for e in engines]}


def params_hash(engines, deltas):
    return hashlib.sha256(json.dumps(params_dict(engines, deltas), sort_keys=True).encode()).hexdigest()[:16]


def cache_valida(out, d, ph):
    meta, f = out / f"meta_{d}.json", out / f"unidades_{d}.csv.gz"
    if not (meta.exists() and f.exists()):
        return None
    try:
        m = json.loads(meta.read_text())
        if m.get("script_sha") != sha_codigo() or m.get("params_hash") != ph or m.get("cobertura_des", 0) < 0.99:
            return None
        if S.sha_fichero(f) != m.get("sha_unidades"):
            return None
        return m
    except (ValueError, OSError):
        return None


def validar_unicidad(filas):
    c = collections.Counter((r["dia"], r["motor"], r["mkt"], r["lado"], r["tramo"]) for r in filas)
    return [k for k, v in c.items() if v > 1]


def correr_dia(d, engines, out, args, log, des_fn=None):
    t_ini = time.time()
    f5 = S.VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    est = {"dia": d, "estado": "FALTA_ENTRADA", "inicio": datetime.now(timezone.utc).isoformat()}
    if not f5.exists():
        log(f"{d}: falta {f5}")
        return est, None, None, None, None
    monedas = set(args.monedas.split(",")) if args.monedas else None
    dia_ini = int(datetime.fromisoformat(d + "T00:00:00+00:00").timestamp() * 1000)
    t_corte = dia_ini + args.recorte_min * 60_000 if args.recorte_min else None
    if any(e.bn for e in engines):
        ext = S.leer_externas(d, t_corte, args.max_lineas_ext, out)
    else:
        ext = S.Externas()
    fs = ficheros_l(d, tuple(Path(x) for x in args.dirs_l.split(",")))
    lad = Ladders.cargar(fs, monedas, t_corte, log)
    log(f"{d}: externas {ext.estado['x_filas']} ticks Binance; ladders {len(fs)} ficheros, {lad.n_l} filas l, {lad.n_L} filas L, "
        f"{len(lad.tokens)} tokens ({time.time() - t_ini:.0f}s)")
    mo = procesar_registro(f5, ext, lad, engines, dia_ini, monedas, args.max_lineas, t_corte, args.deltas_t)
    filas = mo.filas_deep(d)
    dup = validar_unicidad(filas)
    if dup:
        raise RuntimeError(f"{d}: claves duplicadas {dup[:3]}")
    mids = {r["mkt"] for r in filas}
    universo = mo.universo()
    des_fn = des_fn or S.desenlaces_oficiales
    des = des_fn(mids | set(universo)) if (mids or universo) else {}
    cob = (sum(1 for m in mids if m in des) / len(mids)) if mids else 1.0
    cob_u = (sum(1 for m in universo if m in des) / len(universo)) if universo else 1.0
    est.update({"estado": "OK", "lineas": mo.st["lineas"], "tramos": [[a, b] for a, b in mo.tramos], "filas": len(filas),
                "unidades_incompletas": sum(1 for r in filas if not r["completo"]), "mercados_universo": len(universo),
                "cobertura_des": cob, "cobertura_des_universo": cob_u, "contadores": dict(mo.st),
                "ladders": {"ficheros": [x.name for x in fs], "filas_l": lad.n_l, "filas_L": lad.n_L, "tokens": len(lad.tokens)},
                "segundos": round(time.time() - t_ini, 1)})
    if args.recorte_min or args.max_lineas:
        est["estado"] = "HUMO_NO_CACHEADO"
        return est, filas, des, mo, universo
    if cob < 0.99:
        est["estado"] = "COBERTURA_DES_BAJA"
        log(f"{d}: cobertura de desenlaces {cob:.1%} < 99 %: no se cachea")
        return est, filas, des, mo, universo
    ruta = out / f"unidades_{d}.csv.gz"
    S.escribir_gz_atomico(ruta, [CAB] + [fila_csv(r, des) for r in filas])
    S.escribir_gz_atomico(out / f"universo_{d}.csv.gz", [f"{m}\n" for m in sorted(universo)])
    est.update({"sha_unidades": S.sha_fichero(ruta), "script_sha": sha_codigo(), "params_hash": params_hash(engines, args.deltas_t)})
    S.escribir_atomico(out / f"meta_{d}.json", json.dumps(est, indent=1))
    est["estado"] = "COMPLETO"
    return est, filas, des, mo, universo


# ---------------------------------------------------------------- estadística
def ic90_cierre(F, B=2000, seed=S.RNG_SEED):
    """IC90 de EV/€ agrupado remuestreando CIERRES (varias monedas en el mismo cierre = una apuesta)."""
    if F is None or not len(F):
        return (float("nan"), float("nan"))
    g = F.groupby("fin_s").agg(p=("pnl", "sum"), c=("coste", "sum"))
    if len(g) < 2:
        return (float("nan"), float("nan"))
    p, c = g.p.values, g.c.values
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(g), size=(B, len(g)))
    den = c[idx].sum(1)
    ev = np.where(den > 0, p[idx].sum(1) / np.where(den > 0, den, 1), np.nan)
    return (float(np.nanquantile(ev, .05)), float(np.nanquantile(ev, .95)))


def ev_sin_top_mercados(F, n=5):
    if F is None or not len(F):
        return float("nan")
    g = F.groupby(["dia", "mkt"]).agg(p=("pnl", "sum"), c=("coste", "sum"))
    g = g.drop(index=g.p.nlargest(n).index)
    return float(g.p.sum() / g.c.sum()) if len(g) and g.c.sum() > 0 else float("nan")


def markouts(F, dias_n=None):
    """H38: markout por € a +5/+30/+120 s sobre las unidades rellenas (pooled) con IC90 por días. missing = sin dato, nunca 0."""
    r = {}
    for h in MARK_S:
        c = F[f"mo{h}_cost"].sum() if len(F) else 0.0
        n, miss = (int(F[f"mo{h}_n"].sum()), int(F[f"mo{h}_miss"].sum())) if len(F) else (0, 0)
        if not len(F) or c <= 0:
            r[h] = {"mo": float("nan"), "n": n, "miss": miss, "ic90": (float("nan"), float("nan"))}
            continue
        gd = F.groupby("dia").agg(p=(f"mo{h}_pnl", "sum"), c=(f"mo{h}_cost", "sum"))
        gd = gd[gd.c > 0]
        r[h] = {"mo": float(F[f"mo{h}_pnl"].sum() / c), "n": n, "miss": miss, "ic90": S.ic90_dias((gd.p / gd.c).values)}
    return r


def met(F, total_dias=None):
    """Métricas de una tabla de unidades RELLENAS (con desenlace). Añade IC90 por cierre, sin 5 mejores mercados y markouts."""
    m = S.metricas(F, total_dias=total_dias)
    if not m["n_fill"]:
        return m
    m["ic90_cierre"] = ic90_cierre(F)
    m["ev_sin_top5"] = ev_sin_top_mercados(F, 5)
    m["mark"] = markouts(F)
    return m


def gates(m, n_dias):
    if not m or not m.get("n_fill"):
        return {"n>=40": False, "EV>=+0,05": False, "IC90 días>0": False, "IC90 cierre>0": False, "sin mejor día>0": False,
                "sin top5 mercados>0": False, "días+>=4/6": False, "markout30>0": False}
    ok = lambda x: x == x and x > 0  # noqa: E731
    return {"n>=40": m["n_fill"] >= GATE["n_fill"], "EV>=+0,05": m["ev"] >= GATE["ev"], "IC90 días>0": ok(m["ic90"][0]),
            "IC90 cierre>0": ok(m["ic90_cierre"][0]), "sin mejor día>0": ok(m["ev_sin_mejor"]), "sin top5 mercados>0": ok(m["ev_sin_top5"]),
            "días+>=4/6": m["dias_pos"] >= GATE["dias_pos"] and n_dias >= 6, "markout30>0": ok(m["mark"][30]["mo"])}


def fmt(m):
    if not m or not m.get("n_fill"):
        return "sin rellenos"
    ic = m["ic90"]
    ik = m["ic90_cierre"]
    return (f"rellenas {m['n_fill']} | EV/€ {m['ev']:+.4f} IC90 días ({ic[0]:+.3f},{ic[1]:+.3f}) cierres ({ik[0]:+.3f},{ik[1]:+.3f}) | días+ "
            f"{m['dias_pos']}/{m['dias']} | sin mejor día {m['ev_sin_mejor']:+.4f} sin top5 mkts {m['ev_sin_top5']:+.4f} | PnL {m['pnl']:+.2f} $ "
            f"({m['pnl_dia']:+.2f} $/día) | rebate aparte {m['rebate']:+.2f} $")


def fmt_mark(m):
    if not m or not m.get("n_fill"):
        return ""
    return " | markout " + " ".join(f"+{h}s {m['mark'][h]['mo']:+.4f} (n {m['mark'][h]['n']}, missing {m['mark'][h]['miss']})" for h in MARK_S)


def cargar_unidades(dias, out):
    import pandas as pd
    partes = []
    for d in dias:
        f = out / f"unidades_{d}.csv.gz"
        if f.exists():
            partes.append(pd.read_csv(f, dtype={"mkt": str, "des": str, "pnl": float}))
    return pd.concat(partes, ignore_index=True) if partes else None


def elegir_k(Ud, dias_desc):
    """Elección de k SOLO en DESC, entre DEEP (cola CONS), por moneda y global: máximo EV/€ agrupado con rellenas >= mínimo."""
    sel = {}
    for sc in list(MONEDAS) + ["ALL"]:
        g = Ud if sc == "ALL" else Ud[Ud.act == sc]
        minimo = MIN_FILL_ALL if sc == "ALL" else MIN_FILL_COIN
        cand = []
        for mot, gm in g[(g.fam == "DEEP") & g.motor.str.endswith("|CONS|5")].groupby("motor"):
            F = gm[gm.lleno > 0]
            if len(F) < minimo:
                continue
            m = S.metricas(F, total_dias=len(dias_desc))
            cand.append((m["ev"], mot, int(gm.k.iloc[0]), m))
        cand.sort(key=lambda x: -x[0])
        sel[sc] = (cand[0][1], cand[0][2], cand[0][3], len(cand)) if cand else (None, None, None, 0)
    return sel


def sub(Uc, dias, motor, sc="ALL", claves=None):
    g = Uc[Uc.dia.isin(dias) & (Uc.motor == motor)]
    if sc != "ALL":
        g = g[g.act == sc]
    if claves is not None:
        idx = list(zip(g.dia, g.mkt, g.lado))
        g = g[[i in claves for i in idx]]
    return g


def unidades_con_orden(g):
    return set(zip(g.dia, g.mkt, g.lado))


def lineas_salida(Uc, dias, motor, sc):
    """H37: salida maker a entrada+δ, 10 s, emparejada sobre los MISMOS rellenos de `motor`."""
    g = sub(Uc, dias, motor, sc)
    F = g[g.lleno > 0]
    L = []
    if not len(F):
        return L
    gana = (F.lado == F.des).astype(float)
    base_pnl, base_cost, base_capm = F.pnl.sum(), F.coste.sum(), F.capm.sum()
    for d in DELTAS:
        if f"x{d}_n" not in F:
            continue
        hold_q = F.lleno - F[f"x{d}_fq"]
        hold_c = F.coste - F[f"x{d}_cost"]
        pnl_x = F[f"x{d}_pnl"] + hold_q * gana - hold_c
        n_fills = int(F.nfills.sum())
        n_ex = int(F[f"x{d}_n"].sum())
        fq_tot = F[f"x{d}_fq"].sum()
        pm = pnl_x.sum() / base_cost if base_cost > 0 else float("nan")
        ev_h = base_pnl / base_cost if base_cost > 0 else float("nan")
        ppm_h = base_pnl / base_capm if base_capm > 0 else float("nan")
        ppm_x = pnl_x.sum() / F[f"x{d}_capm"].sum() if F[f"x{d}_capm"].sum() > 0 else float("nan")
        # tasa de llenado de la salida por rellenos (cantidad llenada / cantidad de las salidas puestas)
        q_puestas = F.lleno.sum()
        fr = fq_tot / q_puestas if q_puestas > 0 else float("nan")
        L.append(f"      δ=+{d / 1000:.2f}: salidas puestas {n_ex}/{n_fills} rellenos | se llena {fr:.1%} de la cantidad antes de 10 s | EV/€ mantener "
                 f"{ev_h:+.4f} vs con salida {pm:+.4f} (dif {pm - ev_h:+.4f}) | PnL {base_pnl:+.2f} vs {pnl_x.sum():+.2f} $ | PnL por $·min "
                 f"{ppm_h:+.5f} vs {ppm_x:+.5f}")
        crit = []
        if pm <= ev_h - 0.02:
            crit.append("EV con salida <= mantener − 0,02")
        if ppm_x == ppm_x and ppm_h == ppm_h and ppm_x <= ppm_h:
            crit.append("PnL por $·min no mejora")
        if fr == fr and fr < 0.25:
            crit.append("salida se llena < 25 %")
        L.append("         criterio H37: " + ("REJECTED por: " + "; ".join(crit) if crit else "sin motivo de rechazo en esta muestra (exploratorio)"))
    return L


def informe(out, dias, log=print):
    import pandas as pd
    U = cargar_unidades(dias, out)
    if U is None:
        return "Sin cachés de unidades: nada que informar.", {}
    dias_ok = sorted(U.dia.unique())
    d_desc = [d for d in dias_ok if d in DIAS_DESC]
    d_oos = [d for d in dias_ok if d >= OOS_DESDE]
    d_ex = [d for d in dias_ok if d in DIAS_EXCL]
    tot, inc, sin_des = len(U), int((U.completo == 0).sum()), int(U.des.isna().sum())
    Uc = U[(U.completo == 1) & U.des.notna()].copy()
    res = {"dias": dias_ok, "unidades_total": tot, "incompletas": inc, "sin_desenlace": sin_des}
    L = [f"H35 DEEP_PEG + H37 salida + H38 markout | versión {VERSION} | días con caché {dias_ok}",
         f"DESC={d_desc} | OOS (>= {OOS_DESDE})={d_oos} | excluidos del hallazgo (descriptivo, no cuentan)={d_ex}",
         f"Cobertura: {tot} unidades con orden (todos los motores) | incompletas (tramos) {inc} | sin desenlace {sin_des} (missing, no 0)",
         "Relleno conservador: solo barridas por debajo de nuestro nivel o volumen que supera la cola; cola desconocida = infinita en CONS, "
         "0 en OPT. EV de titular SIN rebate (aparte).", ""]
    # ---- cola conocida / desconocida
    L.append("== 0. COLA: pujas con cola conocida (escalón leído del registro) vs desconocida, por motor (todos los días) ==")
    cd = Uc[Uc.fam.isin(DEEPFAM)].groupby("motor").agg(des=("cola_desc", "sum"), con=("cola_con", "sum"))
    for mot, r in cd.iterrows():
        t_ = r.des + r.con
        L.append(f"  {mot:34} pujas {int(t_):7d} | cola_desconocida {int(r.des):7d} ({r.des / t_:.1%})" if t_ else f"  {mot}: sin pujas")
    # ---- elección en DESC
    sel = {}
    if d_desc:
        sel = elegir_k(Uc[Uc.dia.isin(d_desc)], d_desc)
        L += ["", "== 1. ELECCIÓN DE k EN DESC (DEEP_PEG, cola CONS, SH=5; mayor EV/€ agrupado con rellenas >= "
              f"{MIN_FILL_COIN}/moneda, {MIN_FILL_ALL}/global; k por moneda con su propio dato) =="]
        for sc in list(MONEDAS) + ["ALL"]:
            mot, k, m, nc = sel[sc]
            L.append(f"  {sc:5} candidatas {nc} -> " + (f"{mot} (k={k}): rellenas {m['n_fill']} EV/€ {m['ev']:+.4f}" if mot else "ninguna cumple el mínimo"))
        res["seleccion_desc"] = {sc: {"motor": sel[sc][0], "k": sel[sc][1], "n_candidatas": sel[sc][3]} for sc in sel}
    else:
        L.append("(sin días DESC en la caché: no se puede elegir k; se muestran ambos k)")
    # ---- OOS por moneda
    if d_oos:
        L += ["", f"== 2. OOS {d_oos[0]}..{d_oos[-1]} ({len(d_oos)} días; el gate pide >= 6): DEEP_PEG elegido en DESC frente a placebos =="]
        res["oos"] = {}
        for sc in list(MONEDAS) + ["ALL"]:
            mot, k = sel.get(sc, (None, None, None, 0))[:2]
            L.append(f" [{sc}]")
            if not mot:
                L.append("   DEEP_PEG sin motor elegido en DESC (mínimo de rellenas no alcanzado): se muestran ambos k descriptivos")
                for kk in K_GRID:
                    g = sub(Uc, d_oos, f"DEEP_k{kk}|C0|CONS|5", sc)
                    L.append(f"   DEEP_k{kk} CONS: " + fmt(met(g[g.lleno > 0], len(d_oos))))
                continue
            gD = sub(Uc, d_oos, mot, sc)
            FD = gD[gD.lleno > 0]
            mD = met(FD, len(d_oos))
            L.append(f"   DEEP_PEG k={k} CONS: " + fmt(mD) + fmt_mark(mD) + f" | órdenes {len(gD)}")
            L.append("      gates: " + " ".join(f"{a}{'OK' if b else 'NO'}" for a, b in gates(mD, len(d_oos)).items()))
            mo_ = mot.replace("|CONS|", "|OPT|")
            gO = sub(Uc, d_oos, mo_, sc)
            L.append("   DEEP_PEG k={} OPT (cota): ".format(k) + fmt(met(gO[gO.lleno > 0], len(d_oos))))
            claves = unidades_con_orden(gD)
            for nom, mm in (("DEEP_FIJO", f"DEEPFIJO_k{k}|C0|CONS|5"), ("JOIN", "JOIN|C0|CONS|5"), ("IMPROVE", "IMPROVE|C0|CONS|5")):
                g1 = sub(Uc, d_oos, mm, sc)
                g2 = sub(Uc, d_oos, mm, sc, claves)
                L.append(f"   placebo {nom:9} todas : " + fmt(met(g1[g1.lleno > 0], len(d_oos))) + fmt_mark(met(g1[g1.lleno > 0], len(d_oos))))
                L.append(f"   placebo {nom:9} mismas unidades que DEEP: " + fmt(met(g2[g2.lleno > 0], len(d_oos))))
            res["oos"][sc] = {"motor": mot, "metricas": mD, "gates": gates(mD, len(d_oos))}
            if sc in ("ALL",) or True:
                L += ["   H37 salida maker (emparejada sobre los rellenos de DEEP elegido):"] + lineas_salida(Uc, d_oos, mot, sc)
                L += ["   H37 salida maker (emparejada sobre los rellenos de JOIN CONS):"] + lineas_salida(Uc, d_oos, "JOIN|C0|CONS|5", sc)
    # ---- brazo BN
    bn = sorted(m for m in Uc.motor.unique() if m.startswith("DEEPBN_") and m.endswith("|CONS|5"))
    if bn:
        L += ["", "== 3. BRAZO SECUNDARIO BN (DEEP_PEG solo tras Binance >= BN_BPS en contra en los W ms previos; descriptivo, sin elegir) =="]
        for nombre, ds in (("DESC", d_desc), ("OOS", d_oos)):
            for mot in bn:
                g = Uc[Uc.dia.isin(ds) & (Uc.motor == mot)]
                F = g[g.lleno > 0]
                mm = met(F, len(ds))
                L.append(f"  {nombre} {mot:36} " + fmt(mm) + f" | órdenes {len(g)} (canc. por condición {int(g.ncap.sum())})")
    # ---- tabla descriptiva (DESC y OOS y excluidos)
    L += ["", "== 4. TODOS LOS MOTORES (descriptivo; EV/€ agrupado, global) =="]
    for nombre, ds in (("DESC", d_desc), ("OOS", d_oos), ("EXCL 11-13", d_ex)):
        if not ds:
            continue
        L.append(f" [{nombre} {ds[0]}..{ds[-1]}]")
        for mot in sorted(Uc.motor.unique()):
            g = Uc[Uc.dia.isin(ds) & (Uc.motor == mot)]
            F = g[g.lleno > 0]
            L.append(f"   {mot:36} " + fmt(met(F, len(ds))) + f" | órdenes {len(g)}")
    # ---- markouts
    L += ["", "== 5. H38 MARKOUT (por €, mid del token, reloj de recepción) por motor CONS, OOS y DESC. Parada temprana, NUNCA promoción =="]
    for nombre, ds in (("DESC", d_desc), ("OOS", d_oos)):
        for mot in sorted(m for m in Uc.motor.unique() if m.endswith("|CONS|5")):
            g = Uc[Uc.dia.isin(ds) & (Uc.motor == mot)]
            F = g[g.lleno > 0]
            if len(F):
                mk = markouts(F)
                L.append(f"  {nombre} {mot:34} " + " | ".join(
                    f"+{h}s {mk[h]['mo']:+.4f} IC90d ({mk[h]['ic90'][0]:+.3f},{mk[h]['ic90'][1]:+.3f}) n {mk[h]['n']} miss {mk[h]['miss']}" for h in MARK_S)
                         + f" | EV titular {F.pnl.sum() / F.coste.sum():+.4f}")
    L += ["", f"Cachés: {out} | comando: nice -n 19 ionice -c3 python3 {Path(__file__).name} --solo-informe"]
    return "\n".join(L), res


# ---------------------------------------------------------------- equivalencia bid YES = ask NO a 1−p
def equivalencia(ficheros, log=print):
    """Compara, en el registro archivado (filas q y l), el bid del token con el ask del contrario en 1−p: (a) en momentos quietos
    (ambos sin cambios >= 500 ms) precio y tamaño del top; (b) en cada caída del top de bid: el nuevo top debe ser el 2º/3er nivel
    de ask del contrario justo antes (precio y tamaño). -> (dict, texto)."""
    from datetime import datetime as dt
    meta = {}
    Q = collections.defaultdict(lambda: ([], []))
    lad = Ladders()
    for f in ficheros:
        kc = {}
        try:
            with gzip.open(f, "rt", errors="replace") as fh:
                for ln in fh:
                    tp = ln[:2]
                    if tp == "k,":
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 8 and c[4] == "5min":
                            meta[c[2]] = (c[3], c[5], int(dt.fromisoformat(c[6]).timestamp()), c[7])
                    elif tp == "q,":
                        c = ln.split(",")
                        try:
                            v = (S.mils(c[3]), float(c[5]), S.mils(c[4]), float(c[6]))
                        except (ValueError, IndexError):
                            v = None
                        try:
                            Q[c[2]][0].append(int(c[7]))
                            Q[c[2]][1].append(v)
                        except (ValueError, IndexError):
                            pass
                    elif tp == "l," or tp == "L,":
                        lad.add(ln)
        except (EOFError, OSError):
            pass
    bymkt = collections.defaultdict(dict)
    for tk, m in meta.items():
        bymkt[(m[0], m[1])][m[3]] = tk
    res = collections.Counter()

    def estado(tk, t):
        ts, vs = Q[tk]
        i = bisect.bisect_right(ts, t) - 1
        return (ts[i], vs[i]) if i >= 0 else (None, None)

    for (coin, mkt), d in bymkt.items():
        if "YES" not in d or "NO" not in d:
            continue
        for a, b in ((d["YES"], d["NO"]), (d["NO"], d["YES"])):
            if a not in Q or not lad.tiene(b):
                continue
            fin = meta[a][2] * 1000
            for t in range(fin - 295000, fin - 5000, 2000):
                tq, sq = estado(a, t)
                if sq is None or t - tq < 500:
                    continue
                s, ok = lad.nivel(b, 1000 - sq[0], t)
                rl = lad._fin_l(b) if b in lad._l else None
                il = bisect.bisect_right(rl[0], t) - 1 if rl is not None else -1
                if il < 0 or t - rl[0][il] < 500 or not ok:
                    continue
                res["quieto_n"] += 1
                if s > 0:
                    res["quieto_precio_ok"] += 1
                    if abs(s - sq[1]) <= 1e-4 * max(1.0, sq[1]):
                        res["quieto_tam_ok"] += 1
            ts_, vs_ = Q[a]
            prev, prev_t = None, 0
            for i in range(len(ts_)):
                v = vs_[i]
                if v is None:
                    prev = None
                    continue
                if prev is not None and v[0] < prev[0] and fin - 300000 < ts_[i] < fin - 3000:
                    rl = lad._fin_l(b) if b in lad._l else None
                    if rl is not None:
                        il = bisect.bisect_right(rl[0], ts_[i] - 1) - 1
                        if il >= 0:
                            niv = [(rl[1 + 2 * j][il], rl[2 + 2 * j][il]) for j in range(3) if rl[1 + 2 * j][il] >= 0]
                            if len(niv) >= 2:
                                res["caida_n"] += 1
                                pr = [1000 - p for p, _ in niv]
                                if v[0] in pr:
                                    res["caida_precio_ok"] += 1
                                    j = pr.index(v[0])
                                    res[f"caida_nivel{j + 1}"] += 1
                                    if abs(niv[j][1] - v[1]) <= 1e-4 * max(1.0, v[1]):
                                        res["caida_tam_ok"] += 1
                prev = v
    n1, n2 = res["quieto_n"], res["caida_n"]
    txt = [f"Equivalencia bid(T) = ask(contrario) a 1−p, ficheros {[Path(f).name for f in ficheros]}",
           f"  momentos quietos (>=500 ms sin cambios en ambos): n {n1} | precio coincide {res['quieto_precio_ok']} ({res['quieto_precio_ok'] / n1:.2%}) | "
           f"tamaño coincide {res['quieto_tam_ok']} ({res['quieto_tam_ok'] / n1:.2%})" if n1 else "  sin momentos quietos comparables",
           f"  caídas del top de bid: n {n2} | el nuevo top es un nivel del espejo {res['caida_precio_ok']} ({res['caida_precio_ok'] / n2:.2%}; "
           f"nivel 2: {res['caida_nivel2']}, nivel 3: {res['caida_nivel3']}, nivel 1 = espejo ya actualizado: {res['caida_nivel1']}) | tamaño coincide {res['caida_tam_ok']} "
           f"({res['caida_tam_ok'] / n2:.2%})" if n2 else "  sin caídas comparables"]
    return dict(res), "\n".join(txt)


# ---------------------------------------------------------------- orquestación
def mem_disponible_mb():
    return S.mem_disponible_mb()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default=",".join(DIAS_DEF))
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--solo-informe", action="store_true")
    ap.add_argument("--monedas", default="", help="humo: lista de monedas (por defecto las 6)")
    ap.add_argument("--recorte-min", type=int, default=0)
    ap.add_argument("--max-lineas", type=int, default=0)
    ap.add_argument("--max-lineas-ext", type=int, default=0)
    ap.add_argument("--ks", default=",".join(str(k) for k in K_GRID))
    ap.add_argument("--sin-bn", action="store_true")
    ap.add_argument("--bn-bps", type=float, default=BN_BPS)
    ap.add_argument("--bn-w-ms", default=",".join(str(w) for w in BN_W))
    ap.add_argument("--deltas", default=",".join(str(x) for x in DELTAS), help="milésimas de la salida H37 (10=0,01)")
    ap.add_argument("--dirs-l", default=f"{ARCHIVO_L},{CRUDO_L}")
    ap.add_argument("--cache-desenlaces", default="")
    ap.add_argument("--forzar-horario", action="store_true")
    ap.add_argument("--equivalencia", nargs="*", default=None)
    a = ap.parse_args(argv)
    if a.equivalencia is not None:
        _, txt = equivalencia(a.equivalencia)
        print(txt)
        return 0
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    dias = [d for d in a.dias.split(",") if d]
    job = f"m5_deep_peg_{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}"
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
    a.deltas_t = tuple(int(x) for x in a.deltas.split(",") if x)
    ks = tuple(int(x) for x in a.ks.split(",") if x)
    engines = construir_motores(ks, bn=not a.sin_bn, bn_w=tuple(int(x) for x in a.bn_w_ms.split(",") if x), bn_bps=a.bn_bps)
    ph = params_hash(engines, a.deltas_t)
    man = {"job_id": job, "script": str(Path(__file__).resolve()), "script_sha256": sha_codigo(), "params": params_dict(engines, a.deltas_t),
           "params_hash": ph, "dias_previstos": dias, "inicio": datetime.now(timezone.utc).isoformat(), "estado": "EN_CURSO",
           "entradas": {}, "dias": {}, "comando": " ".join(sys.argv)}
    for d in dias:
        man["entradas"][d] = {}
        for nom, f in (("m5_registro", S.VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"),
                       ("m15_registro", S.VOL / "m15_registro" / f"m15_registro_{d}.csv.gz")):
            man["entradas"][d][nom] = ({"bytes": f.stat().st_size, "mtime": f.stat().st_mtime} if f.exists() else None)
        man["entradas"][d]["ficheros_l"] = [x.name for x in ficheros_l(d, tuple(Path(x) for x in a.dirs_l.split(",")))]

    def guarda():
        txt = json.dumps(man, indent=1, default=str)
        S.escribir_atomico(out / "run_manifest.json", txt)
        S.escribir_atomico(out / f"run_manifest_{job}.json", txt)

    guarda()
    if a.solo_informe:
        txt, res = informe(out, dias, log)
        S.escribir_atomico(out / "informe.txt", txt + "\n")
        S.escribir_atomico(out / "informe.json", json.dumps(res, indent=1, default=str))
        print(txt)
        return 0
    pesado = not (a.recorte_min or a.max_lineas)
    if pesado and 6 <= datetime.now(timezone.utc).hour < 9 and not a.forzar_horario:
        man.update({"estado": "BLOCKED", "motivo": "06:00-09:00Z"})
        guarda()
        log("BLOCKED: franja 06:00-09:00Z")
        return 3
    try:
        load = float(open("/proc/loadavg").read().split()[0])
    except OSError:
        load = 0.0
    if pesado and (load >= 16 or mem_disponible_mb() < 1500):
        man.update({"estado": "BLOCKED", "motivo": f"load {load} o MemAvailable {mem_disponible_mb():.0f} MB"})
        guarda()
        log("BLOCKED: carga o memoria")
        return 3
    log(f"inicio {job}: {len(dias)} días, {len(engines)} motores, hash {man['script_sha256'][:12]}, params {ph}")
    errores = 0
    for d in dias:
        try:
            m = None if not pesado else cache_valida(out, d, ph)
            if m:
                man["dias"][d] = {"estado": "SALTADO_CACHE_VALIDA", "filas": m["filas"], "cobertura_des": m["cobertura_des"]}
                log(f"{d}: caché válida ({m['filas']} filas): se salta")
                guarda()
                continue
            r = correr_dia(d, engines, out, a, log)
            est = r[0]
            man["dias"][d] = {k: est.get(k) for k in ("estado", "filas", "unidades_incompletas", "mercados_universo", "cobertura_des",
                                                      "cobertura_des_universo", "lineas", "tramos", "segundos", "contadores", "ladders")}
            log(f"{d}: {est['estado']} | {est.get('filas')} unidades con orden, incompletas {est.get('unidades_incompletas')}, "
                f"cobertura des {est.get('cobertura_des', 0):.1%}, {est.get('segundos')} s | {est.get('contadores')}")
            if est["estado"] == "HUMO_NO_CACHEADO":
                print(resumen_humo(d, r[1], r[2]))
            if est["estado"] == "COMPLETO":
                txt, _ = informe(out, [x for x in dias if (out / f"unidades_{x}.csv.gz").exists()], log)
                S.escribir_atomico(out / "resumen_parcial.txt", txt + "\n")
        except Exception as e:                                          # nunca queda "terminado" sin informe
            errores += 1
            man["dias"][d] = {"estado": "FALLO", "error": f"{type(e).__name__}: {e}"}
            log(f"{d}: FALLO {type(e).__name__}: {e}")
        guarda()
    ok = [d for d in dias if man["dias"].get(d, {}).get("estado") in ("COMPLETO", "SALTADO_CACHE_VALIDA")]
    man["estado"] = "HUMO" if not pesado else "COMPLETE" if len(ok) == len(dias) else "PARTIAL" if ok else "FAILED" if errores else "BLOCKED"
    man["fin"] = datetime.now(timezone.utc).isoformat()
    guarda()
    if ok and pesado:
        txt, res = informe(out, ok, log)
        S.escribir_atomico(out / "informe.txt", txt + "\n")
        S.escribir_atomico(out / "informe.json", json.dumps(res, indent=1, default=str))
        log("informe final escrito")
    log(f"ESTADO FINAL: {man['estado']} (válidos {len(ok)}/{len(dias)}: {ok}; fallos {errores})")
    return 0 if man["estado"] in ("COMPLETE", "HUMO") else 1


def resumen_humo(d, filas, des):
    import io
    import pandas as pd
    if not filas:
        return f"== HUMO {d}: sin unidades con orden =="
    U = pd.read_csv(io.StringIO(CAB + "".join(fila_csv(r, des) for r in filas)), dtype={"mkt": str, "des": str})
    Uc = U[(U.completo == 1) & U.des.notna()]
    L = [f"== HUMO {d}: unidades con orden {len(U)}, completas con desenlace {len(Uc)} =="]
    for mot, g in Uc.groupby("motor", sort=False):
        F = g[g.lleno > 0].assign(dia=d)
        m = met(F, 1)
        cd, cc = int(g.cola_desc.sum()), int(g.cola_con.sum())
        L.append(f"  {mot:34} órdenes {len(g):4d} pujas {int(g.norders.sum()):5d} (cola desc. {cd}, conocida {cc}) | " + (
            f"rellenas {m['n_fill']:4d} EV/€ {m['ev']:+.3f} PnL {m['pnl']:+.2f}" + fmt_mark(m) if m["n_fill"] else "sin rellenos"))
    return "\n".join(L)


if __name__ == "__main__":
    sys.exit(main())
