#!/usr/bin/env python3
"""5m: COSECHAR PARES AL ABRIR v2 REACTIVA (hipótesis H32, OK Javi 16-Oct). SOLO LECTURA / simulación.

Motivo: v1 (analisis_5m_cosechar_apertura.py, commit 847a2240eb) quedó REJECTED. Sus pares completos ganaban (+0,042 €/€
en OOS) pero la pata SUELTA (21 % de los mercados) perdía −0,80 €/€: casi siempre es la perdedora (selección adversa).
v2 mantiene la entrada de v1 (BTC 5m, 5 acciones por lado, bid de PAR/2 = 0,48 en ambos tokens durante los primeros 15 s,
cola FINAL o CABEZA, defensa A0 / A_BN, cancelación a T = 10 s, desenlace OFICIAL) y añade políticas REACTIVAS que actúan
cuando una pata se rellena y la otra no. NO modifica v1 ni sus cachés: importa sus funciones (escritura atómica, caché,
resumen, constantes) y el modelo de cola (PM.Pata); el bucle de simulación se reescribe porque el de v1 es una clausura.

POLÍTICAS (FIJADAS ANTES DE MIRAR, 16-Oct). Base PAR = 0,96 solamente, defensas A0 y A_BN, colas FINAL y CABEZA:
  BASE   = v1 (sin reacción).
  R1 COMPLETAR  Detección = hora de RECEPCIÓN del trade que rellena la primera pata (t_det). La otra pata maker se cancela
         con efecto en t_det + 65 ms (cancelación medida; hasta entonces aún puede rellenarse). A t_act = t_det + L
         (L = 215 ms, tomador real) se compra la pata corta como TOMADOR al ask de nivel 1 con recepción <= t_act, por la
         diferencia entre acciones conocidas (recepción <= t_act), si coste_par = precio_medio_relleno + ask + 0,07·ask·(1−ask)
         <= U, U ∈ {1,00, 1,02, 1,05}. Lo que no cabe en el nivel 1 queda suelto. Si no se cumple U: pata suelta.
  R2 SALIR      Misma detección y misma cancelación. A t_act se vende el exceso de la pata rellenada como TOMADOR al bid de
         nivel 1 (recepción <= t_act, fee 0,07·p·(1−p)) si bid >= precio_medio_relleno − X, X ∈ {0,03, 0,06, 0,10}; si no, se
         queda.
  R3 = R1 y, si no se cumple (o no hay dato/liquidez), R2.
  S1 SKEW k ∈ {1, 2}  En cada cotización, ret de Binance BTCUSDT a 5 s (referencia = último tick con recepción <= t−5 s, no
         más viejo de 2 s sobre ese instante; precio actual = último tick; por RECEPCIÓN c[7]). Si |ret| >= SKEW_BPS (0,2 bp,
         fijado a priori) la puja del lado favorecido (ret>0 -> YES=Up) va al precio de v1 y la del otro k ticks (0,01) más
         baja; sin señal (o sin dato) -> simétrico como v1.
  Libro cruzado (bid > ask) o sin bid/ask/tamaño en el momento de actuar = SIN DATO: no se opera (motivo registrado).
  REGISTRO CONCATENADO: el m5_registro de un día suele ser la unión de varios tramos cronológicos (10-oct: 22:25-24:00,
  08:10-22:25, 00:00-08:10). v1 no lo trata y su defensa A_BN queda "siempre disparada" tras el primer salto atrás (ventana de
  1 s con un tick de hace horas: 10-oct 94 % y 100 % de los ticks BTC disparan en los tramos 2-3, 12-oct 100 %, frente a 2-7 %
  con la ventana reiniciada). v2 reinicia las ventanas de Binance en cada salto atrás >60 s y descarta las fotos pendientes;
  `--bn-v1` reproduce el comportamiento de v1 (la regresión lo usa).
CONTROL (--control): R1 con U = 0 y SIN cancelación = v1 exactamente (prueba de regresión). OJO: R1 con U = 0 y con
  cancelación (`_R1_U0.00`, ablación) NO es v1: cancelar la otra pata a +65 ms elimina los rellenos maker posteriores.
CONTABILIDAD COMPLETA (unidad = mercado; ninguna fila descartada salvo mercados sin desenlace oficial, contados en la
cobertura): maker (qY, qN), compras tomador (tY, tN), ventas (sY, sN), coste = capital comprado (maker + tomador; las ventas no
lo reducen), fees tomador, pnl = pago del lado ganador sobre posición neta + ventas − compras − fees (SIN reembolso maker, que
se da aparte como en v1), modo_final y motivo. Supuestos: rejilla de fee sin redondeo a céntimo; la posición a completar o
vender usa solo rellenos con recepción <= t_act; los rellenos posteriores quedan en el libro de cuentas (suelto) sin reaccionar;
min_order_size del CLOB no se modela.
Partición como v1: DESC 05-09 (elección SOLO aquí, por EV/€ en cola FINAL entre las políticas reactivas) / OOS 10-14 (juicio único).
Salida: datalogs/m5_cosechar_apertura_v2/ (caché por día con hash del script, informe.txt, desglose_modo_final.txt, manifiesto).
Uso:  nice -n 19 ionice -c3 python3 analisis_5m_cosechar_apertura_v2.py [--dias ...] [--out DIR] [--control]
      [--max-mercados N] (prueba de humo: no cachea)  |  --regresion-v1 (compara BASE/CONTROL con v1 en el mismo fixture)
"""
import argparse
import bisect
import collections
import csv
import gzip
import hashlib
import heapq
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_5m_cosechar_apertura as V1  # noqa: E402  (escritura atómica, caché, resumen, constantes)
import analisis_5m_pares_maker_cola as PM  # noqa: E402  (Pata, SH: mismo modelo de cola)
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5_cosechar_apertura_v2")
DIAS, DESC, OOS = V1.DIAS, V1.DESC, V1.OOS
ENTRADA_S, T_FIN_S, REARME_MS, INF = V1.ENTRADA_S, V1.T_FIN_S, V1.REARME_MS, V1.INF
SH = PM.SH
PAR = 0.96
L_TOMADOR_MS = 215                  # tomador real: envío -> casado (F1 15-Oct)
CANCEL_MS = 65                      # cancelación maker medida (F1 15-Oct)
FEE = 0.07                          # fee cripto del tomador por acción: FEE·p·(1−p)
REB = 0.2                           # reembolso maker: 20 % del fee del tomador
U_LIST = (1.00, 1.02, 1.05)
X_LIST = (0.03, 0.06, 0.10)
K_LIST = (1, 2)
SKEW_BPS = 0.2                      # fijado a priori desde la distribución marginal de |ret 5 s| (10-oct: >=0,2 bp en ~9 % de los instantes), no desde resultados
SKEW_VENT_MS, SKEW_STALE_MS = 5000, 2000
LADOS = ("YES", "NO")
OPUESTO = {"YES": "NO", "NO": "YES"}
EPS = 1e-9

# motores = simulaciones de cola independientes: (nombre, defensa, cola, k_skew)
ENGINES = [(f"{d}_P{int(PAR * 100)}_{c}" + (f"_S1k{k}" if k else ""), d, c, k)
           for d in ("A0", "A_BN") for c in ("FINAL", "CABEZA") for k in (0,) + K_LIST]


def variantes(control=False):
    """Capas reactivas aplicadas a los motores sin skew: (sufijo, tipo, U, X, cancela_otra). BASE = sufijo ''."""
    v = [("", None, None, None, False), ("_R1_U0.00", "R1", 0.0, None, True)]
    v += [(f"_R1_U{u:.2f}", "R1", u, None, True) for u in U_LIST]
    v += [(f"_R2_X{x:.2f}", "R2", None, x, True) for x in X_LIST]
    v += [(f"_R3_U{u:.2f}_X{x:.2f}", "R3", u, x, True) for u in U_LIST for x in X_LIST]
    if control:
        v.append(("_CTRL", "R1", 0.0, None, False))
    return v


def politicas(control=False):
    """[(pol, motor, tipo, variante)] en orden de informe."""
    out = []
    for nom, _d, _c, k in ENGINES:
        for var in (variantes(control) if k == 0 else [("", None, None, None, False)]):
            out.append((nom + var[0], nom, var[1], var))
    return out


class PataLog(PM.Pata):
    """Pata de v1 que además registra cada relleno (t_ex, t_rx, precio, cantidad) para aplicar capas reactivas a posteriori."""
    __slots__ = ("ev",)

    def __init__(self, t_fin):
        super().__init__(t_fin)
        self.ev = []

    def consumir(self, t_ex, pe, t_rx=0):
        prev = [g[5] for g in self.segs]
        nuevo = super().consumir(t_ex, pe)
        if nuevo:
            for g, p0 in zip(self.segs, prev):
                if g[5] > p0 + 1e-12:
                    self.ev.append((t_ex, t_rx, g[0], g[5] - p0))
        return nuevo


def fee_tomador(p):
    return FEE * p * (1.0 - p)


def precio_skew(b, k, lado, señal):
    """Precio de la puja con skew: señal = +1 (Binance sube, favorece YES), −1 (baja, favorece NO) o 0 (sin señal)."""
    if k and señal != 0 and (lado == "YES") != (señal > 0):
        return max(round(b - 0.01 * k, 2), 0.01)
    return b


def señal_binance(bn5, t_rx):
    """+1/−1/0 según ret a 5 s por recepción; recorta la ventana (las consultas llegan en orden de tiempo)."""
    lim = t_rx - SKEW_VENT_MS
    while len(bn5) >= 2 and bn5[1][0] <= lim:
        bn5.popleft()
    if not bn5 or bn5[0][0] > lim or lim - bn5[0][0] > SKEW_STALE_MS:
        return 0
    ret = (bn5[-1][1] / bn5[0][1] - 1.0) * 1e4
    return 0 if abs(ret) < SKEW_BPS else (1 if ret > 0 else -1)


def clasificar(n, compras, ventas):
    """modo_final a partir de las posiciones netas finales n={'YES','NO'} y las acciones tomadoras (acciones totales)."""
    resto = abs(n["YES"] - n["NO"])
    pares = min(n["YES"], n["NO"])
    if compras <= EPS and ventas <= EPS:
        if resto <= EPS:
            return "par_maker" if pares >= SH - EPS else "par_parcial"
        return "suelta"
    if compras > EPS and ventas <= EPS:
        return "completado_tomador" if resto <= EPS else "completado_parcial"
    if ventas > EPS and compras <= EPS:
        return "salida" if n["YES"] + n["NO"] <= EPS else "salida_parcial"
    return "mixto"


def _completar(snap, corta, precio_medio, exc, U):
    s = snap.get(corta) if snap else None
    if s is None:
        return None, "sin_dato"
    bid, ask, _bsz, asz = s
    if bid > ask + EPS:
        return None, "libro_cruzado"
    if not 0.0 < ask < 1.0:
        return None, "sin_ask"
    if asz is None or asz <= EPS:
        return None, "sin_liquidez"
    if precio_medio + ask + fee_tomador(ask) > U + 1e-12:
        return None, "U_no_cumplida"
    return (min(exc, asz), ask), "completa" if asz >= exc - EPS else "completa_parcial"


def _salir(snap, suelta, precio_medio, exc, X):
    s = snap.get(suelta) if snap else None
    if s is None:
        return None, "sin_dato"
    bid, ask, bsz, _asz = s
    if bid > ask + EPS:
        return None, "libro_cruzado"
    if not 0.0 < bid < 1.0:
        return None, "sin_bid"
    if bsz is None or bsz <= EPS:
        return None, "sin_liquidez"
    if bid < precio_medio - X - EPS:
        return None, "X_no_cumplida"
    return (min(exc, bsz), bid), "salida" if bsz >= exc - EPS else "salida_parcial"


def evaluar_variante(var, evs, det, snap, res):
    """Libro de cuentas de UN mercado y UNA variante. evs={'YES':[(t_ex,t_rx,p,q)],'NO':[...]} (rellenos maker del motor
    base); det=(t_det, lado_primer_relleno) o None; snap={'YES':(bid,ask,bsz,asz)|None,'NO':...}|None a t_det+L; res='YES'|'NO'."""
    _suf, kind, U, X, cancela = var
    ev = {l: list(evs[l]) for l in LADOS}
    if kind and cancela and det:
        otro = OPUESTO[det[1]]
        ev[otro] = [e for e in ev[otro] if e[0] <= det[0] + CANCEL_MS]
    t_act = (det[0] + L_TOMADOR_MS) if det else None
    compras = {l: [] for l in LADOS}                    # (cantidad, precio)
    ventas = {l: [] for l in LADOS}
    motivo = ""
    if kind and det:
        q_k, c_k = {}, {}
        for l in LADOS:
            conocidos = [e for e in ev[l] if e[1] <= t_act]
            q_k[l] = sum(e[3] for e in conocidos)
            c_k[l] = sum(e[3] * e[2] for e in conocidos)
        d = q_k["YES"] - q_k["NO"]
        if abs(d) > EPS:
            suelta = "YES" if d > 0 else "NO"
            corta, exc = OPUESTO[suelta], abs(d)
            pm_ = c_k[suelta] / q_k[suelta]
            m1 = m2 = ""
            hecho = False
            if kind in ("R1", "R3"):
                acc, m1 = _completar(snap, corta, pm_, exc, U)
                if acc:
                    compras[corta].append(acc)
                    hecho = True
            if not hecho and kind in ("R2", "R3"):
                acc, m2 = _salir(snap, suelta, pm_, exc, X)
                if acc:
                    ventas[suelta].append(acc)
                    hecho = True
            motivo = "|".join(m for m in (m1, m2) if m)
        else:
            motivo = "sin_desbalance"
    q = {l: sum(e[3] for e in ev[l]) for l in LADOS}
    cm = sum(e[3] * e[2] for l in LADOS for e in ev[l])
    reb = sum(e[3] * REB * fee_tomador(e[2]) for l in LADOS for e in ev[l])
    t_ = {l: sum(a for a, _p in compras[l]) for l in LADOS}
    s_ = {l: sum(a for a, _p in ventas[l]) for l in LADOS}
    cost_t = sum(a * p for l in LADOS for a, p in compras[l])
    fees = sum(a * fee_tomador(p) for l in LADOS for a, p in compras[l] + ventas[l])
    ingreso = sum(a * p for l in LADOS for a, p in ventas[l])
    n = {l: q[l] + t_[l] - s_[l] for l in LADOS}
    coste = cm + cost_t
    return {"qY": q["YES"], "qN": q["NO"], "tY": t_["YES"], "tN": t_["NO"], "sY": s_["YES"], "sN": s_["NO"],
            "coste": coste, "fees": fees, "pnl": n[res] + ingreso - coste - fees, "rebate": reb,
            "completo_maker": int(min(q.values()) >= SH - EPS), "completo": int(min(n.values()) >= SH - EPS),
            "modo_final": clasificar(n, sum(t_.values()), sum(s_.values())), "motivo": motivo}


def correr_flujo(f, max_mercados=None, bn_compat=False):
    """Una pasada por el registro m5 del día: rellenos de todos los motores (con registro de eventos), primer relleno por
    (motor, mercado) y foto del libro de ambos tokens a t_det + L. Devuelve el estado para construir_filas.
    El registro del día es la CONCATENACIÓN de varios tramos, cada uno cronológico (p. ej. 10-oct: 22:25-24:00, 08:10-22:25,
    00:00-08:10). En cada salto atrás de >60 s se descartan las fotos pendientes (quedan sin foto) y se reinicia la ventana de
    5 s de Binance. También se reinicia la ventana de 1 s de la defensa A_BN, que v1 NO reinicia: tras el salto su primer tick
    queda "en el futuro" y la defensa compara cada precio con un tick de hace horas. bn_compat=True reproduce v1."""
    meta, par, por_mkt = {}, {}, {}
    top, topz = {}, {}                              # top: (bid, ask, bsz) como v1; topz: (bid, ask, bsz, asz) o ausente
    est = {}                                        # (motor, token) -> PataLog
    bloqueo = collections.defaultdict(lambda: -INF)
    bn, bn5 = collections.deque(), collections.deque()
    fins, mkts_ord = [], []
    det, snap, heap = {}, {}, []
    seq = [0]
    st = {"lineas": 0, "t_stop": None, "truncado": False, "saltos_tiempo": 0, "cerrados": set()}
    abiertos = {}                                    # mercado cotizado y aún no cerrado -> cierre (corte de prueba)
    motores_a_bn = [e for e in ENGINES if e[1] == "A_BN"]
    base_eng = {e[0] for e in ENGINES if e[3] == 0}

    def con_rellenos(nom, mkt):
        return any(est.get((nom, t)) is not None and est[(nom, t)].lleno > 1e-9 for t in por_mkt[mkt].values())

    def reloj(t):
        """Actualiza el reloj de recepción; detecta el salto atrás entre tramos del archivo."""
        nonlocal t_ult
        if t < t_ult - 60_000:
            st["saltos_tiempo"] += 1
            for _ta, _s, k in heap:
                snap.setdefault(k, None)
            heap.clear()
            bn5.clear()
            if not bn_compat:
                bn.clear()
            t_ult = t
        else:
            t_ult = max(t_ult, t)
        return t_ult

    def avanzar(t):
        while heap and heap[0][0] < t:
            _ta, _s, k = heapq.heappop(heap)
            tks = por_mkt[k[1]]
            snap[k] = {"YES": topz.get(tks.get("YES")), "NO": topz.get(tks.get("NO"))}

    def evaluar(eng, tk, t_rx):
        nom, _defensa, colam, k = eng
        _act, mkt, fin, lado = meta[tk]
        T = (fin - t_rx) / 1000.0
        tp = top.get(tk)
        if tp is None:
            return
        o = est.get((nom, tk))
        if o is not None and o.lleno >= SH - 1e-9:
            return
        hay = con_rellenos(nom, mkt)
        b = round(PAR / 2, 2)
        bid, ask, bsz = tp
        en_entrada = 300 - ENTRADA_S < T <= 300
        ok = T > T_FIN_S and b < ask - 1e-9 and (hay or en_entrada) and t_rx >= bloqueo[(nom, mkt)]
        if o is not None and o.viva(t_rx):
            if ok:
                return
            o.cancelar(t_rx)
            return
        if ok and (o is None or not o.segs or o.lleno <= 1e-9 or hay):
            precio = precio_skew(b, k, lado, señal_binance(bn5, t_rx)) if k else b
            if precio > bid + 1e-9:
                cola = 0.0
            elif abs(precio - bid) < 1e-9:
                cola = 0.0 if colam == "CABEZA" else bsz
            else:
                cola = INF
            if o is None:
                o = est[(nom, tk)] = PataLog(fin - T_FIN_S * 1000)
                abiertos.setdefault(mkt, fin)
            o.cotizar(precio, cola, t_rx, fin - T_FIN_S * 1000)

    def defender(t_rx):
        i0 = bisect.bisect_right(fins, t_rx)
        i1 = bisect.bisect_right(fins, t_rx + 300_000)
        vivos = mkts_ord[i0:i1]
        for eng in motores_a_bn:
            nom = eng[0]
            for mkt in vivos:
                tks = por_mkt[mkt]
                if len(tks) != 2 or con_rellenos(nom, mkt):
                    continue
                bloqueo[(nom, mkt)] = t_rx + REARME_MS
                for t in tks.values():
                    o = est.get((nom, t))
                    if o is not None:
                        o.cancelar(t_rx)

    t_ult = 0
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                tp_ = ln[:2]
                if tp_ not in ("k,", "q,", "t,", "x,"):
                    st["lineas"] += 1
                    continue
                if tp_ == "k,":
                    c = ln.rstrip("\n").split(",")
                    if len(c) >= 8 and c[4] == "5min" and c[3] == "BTC" and c[2] not in meta:
                        fin = int(datetime.fromisoformat(c[6]).timestamp() * 1000)
                        meta[c[2]] = (c[3], c[5], fin, c[7])
                        if c[5] not in por_mkt:
                            k_ = bisect.bisect_right(fins, fin)
                            fins.insert(k_, fin)
                            mkts_ord.insert(k_, c[5])
                        d_ = por_mkt.setdefault(c[5], {})
                        d_[c[7]] = c[2]
                        if len(d_) == 2:
                            a, b_ = d_.get("YES"), d_.get("NO")
                            if a and b_:
                                par[a], par[b_] = b_, a
                    st["lineas"] += 1
                    continue
                if tp_ == "x,":
                    c = ln.rstrip("\n").split(",")
                    if c[2] != "BTCUSDT":
                        st["lineas"] += 1
                        continue
                    try:
                        t_rx, px = int(c[7]), float(c[3])
                    except (ValueError, IndexError):
                        st["lineas"] += 1
                        continue
                    reloj(t_rx)
                    avanzar(t_rx)
                    bn.append((t_rx, px))
                    bn5.append((t_rx, px))
                    while bn and bn[0][0] < t_rx - 1000:
                        bn.popleft()
                    if abs(px / bn[0][1] - 1) * 1e4 >= 2.0:
                        defender(t_rx)
                    st["lineas"] += 1
                    continue
                c = ln.rstrip("\n").split(",")
                tk = c[2]
                if tk not in meta or tk not in par:
                    st["lineas"] += 1
                    continue
                if tp_ == "q,":
                    try:
                        nuevo_top = (float(c[3]), float(c[4]), float(c[5]))
                        t_rx = int(c[7])
                    except (ValueError, IndexError):
                        topz.pop(tk, None)           # libro vacío/ilegible: sin dato para actuar (v1 conserva el anterior)
                        st["lineas"] += 1
                        continue
                    reloj(t_rx)
                    if max_mercados:
                        for m_ in [m for m, fn in abiertos.items() if fn < t_rx]:
                            st["cerrados"].add(m_)
                            del abiertos[m_]
                        if len(st["cerrados"]) >= max_mercados:
                            st["t_stop"] = t_rx
                            break
                    avanzar(t_rx)
                    top[tk] = nuevo_top
                    try:
                        asz = float(c[6])
                    except (ValueError, IndexError):
                        asz = None
                    topz[tk] = nuevo_top + (asz,)
                    for eng in ENGINES:
                        evaluar(eng, tk, t_rx)
                else:
                    try:
                        p, side, sz, t_ex = float(c[3]), c[4], float(c[5]), int(c[1])
                    except (ValueError, IndexError):
                        st["lineas"] += 1
                        continue
                    try:
                        t_rx = int(c[6]) if len(c) > 6 and c[6] else None
                    except ValueError:
                        t_rx = None
                    t_rx = reloj(t_rx) if t_rx is not None else t_ult
                    avanzar(t_rx)
                    if side == "SELL":
                        obj, pe = tk, (p, sz)
                    elif side == "BUY":
                        obj, pe = par[tk], (round(1.0 - p, 4), sz)
                    else:
                        st["lineas"] += 1
                        continue
                    for eng in ENGINES:
                        o = est.get((eng[0], obj))
                        if o is not None and o.consumir(t_ex, pe, t_rx):
                            k = (eng[0], meta[obj][1])
                            if k not in det:
                                det[k] = (t_rx, meta[obj][3])
                                if eng[0] in base_eng:
                                    seq[0] += 1
                                    heapq.heappush(heap, (t_rx + L_TOMADOR_MS, seq[0], k))
                st["lineas"] += 1
        except (EOFError, OSError) as e:
            print(f"  {f.name}: fichero truncado ({type(e).__name__})", file=sys.stderr)
            st["truncado"] = True
    for _ta, _s, k in heap:                          # el archivo acabó antes de t_det + L: sin foto
        snap[k] = None
    return {"meta": meta, "por_mkt": por_mkt, "est": est, "det": det, "snap": snap, "st": st}


def mercados_cerrados(estado):
    """Mercados con tokens en est (alguna cotización) cerrados dentro del tramo leído."""
    meta, st = estado["meta"], estado["st"]
    mk = {meta[tk][1] for (_n, tk) in estado["est"]}
    return mk if st["t_stop"] is None else mk & st["cerrados"]


def construir_filas(d, estado, des, control=False):
    """Filas por (política, mercado) + contadores de cobertura. Mercados sin desenlace oficial se cuentan, no se descartan en silencio."""
    meta, por_mkt, est, det, snap, st = (estado[k] for k in ("meta", "por_mkt", "est", "det", "snap", "st"))
    pols = politicas(control)
    mkts = {meta[tk][1] for (_n, tk) in est}
    t_stop = st["t_stop"]
    cov = {"mercados_vistos": sum(1 for t in por_mkt.values() if len(t) == 2), "mercados_cotizados": 0,
           "mercados_con_rellenos": 0, "sin_desenlace": 0, "no_cerrados_por_corte": 0, "incoherencias_eventos": 0,
           "sin_foto": 0, "filas": 0, "lineas": st["lineas"], "saltos_tiempo": st["saltos_tiempo"]}
    filas = []
    for mkt in sorted(mkts):
        tks = por_mkt[mkt]
        if len(tks) != 2:
            continue
        fin = meta[tks["YES"]][2]
        if t_stop is not None and mkt not in st["cerrados"]:
            cov["no_cerrados_por_corte"] += 1
            continue
        cov["mercados_cotizados"] += 1
        evm = {}
        for nom in {m for m, _d, _c, _k in ENGINES}:
            evm[nom] = {}
            for lado in LADOS:
                o = est.get((nom, tks[lado]))
                evm[nom][lado] = o.ev if o else []
                if o and abs(sum(e[3] for e in o.ev) - o.lleno) > 1e-6:
                    cov["incoherencias_eventos"] += 1
        con_r = any(sum(e[3] for l in LADOS for e in evm[n][l]) > 1e-9 for n in evm)
        cov["mercados_con_rellenos"] += int(con_r)
        for nom in evm:
            if (nom, mkt) in det and snap.get((nom, mkt)) is None and nom in {e[0] for e in ENGINES if e[3] == 0}:
                cov["sin_foto"] += 1
        if mkt not in des:
            cov["sin_desenlace"] += int(con_r)
            continue
        r = des[mkt]
        for pol, motor, _kind, var in pols:
            evs = evm[motor]
            if sum(e[3] for l in LADOS for e in evs[l]) <= 1e-9:
                continue                              # sin rellenos en este motor (igual que v1)
            x = evaluar_variante(var, evs, det.get((motor, mkt)), snap.get((motor, mkt)), r)
            filas.append({"dia": d, "pol": pol, "motor": motor, "mkt": mkt, "con15": int(fin % 900_000 == 0),
                          "qY": round(x["qY"], 4), "qN": round(x["qN"], 4), "tY": round(x["tY"], 4), "tN": round(x["tN"], 4),
                          "sY": round(x["sY"], 4), "sN": round(x["sN"], 4), "coste": round(x["coste"], 6),
                          "fees": round(x["fees"], 6), "pnl": round(x["pnl"], 6), "rebate": round(x["rebate"], 6),
                          "completo_maker": x["completo_maker"], "completo": x["completo"], "modo_final": x["modo_final"],
                          "motivo": x["motivo"]})
    cov["filas"] = len(filas)
    return filas, cov


def hash_fichero(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 22), b""):
            h.update(blk)
    return h.hexdigest()


def simular_dia(d, control=False, max_mercados=None, h10="", bn_compat=False):
    """(filas, cov) del día, de la caché válida o recalculado. None si no hay m5_registro. Con --max-mercados no se cachea."""
    suf = f"{d}_{h10}{'_c' if control else ''}{'_bn1' if bn_compat else ''}"
    cache, side = OUT / f"mercados_{suf}.csv.gz", OUT / f"cobertura_{suf}.json"
    if not max_mercados:
        c_ = V1.leer_cache(cache)
        if c_ is not None:
            try:
                cov = json.loads(side.read_text())
            except (OSError, ValueError):
                cov = None                              # missing, no 0
            return c_, cov
    f = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    if not f.exists():
        return None
    t0 = time.time()
    estado = correr_flujo(f, max_mercados, bn_compat)
    mk = mercados_cerrados(estado)
    des = V1.desenlaces(mk)
    print(f"  {d}: flujo {time.time() - t0:.0f} s, líneas {estado['st']['lineas']}, desenlace oficial "
          f"{sum(1 for m in mk if m in des)}/{len(mk)}", flush=True)
    filas, cov = construir_filas(d, estado, des, control)
    cov["segundos"] = round(time.time() - t0, 1)
    if estado["st"]["truncado"]:
        cov["origen_truncado"] = True
    if not filas:
        print(f"  {d}: dia_sin_filas: no se cachea", flush=True)
    elif estado["st"]["truncado"] or max_mercados:
        print(f"  {d}: resultado parcial (origen truncado o corte de prueba): no se cachea", flush=True)
    else:
        V1.escribir_cache(cache, filas)
        V1.escribir_atomico(side, json.dumps(cov))
    return filas, cov


# ---------------------------------------------------------------- informe
def _fl(r, k):
    return float(r[k])


def desglose(filas, pol, dias):
    x = [r for r in filas if r["pol"] == pol and r["dia"] in dias]
    por = collections.defaultdict(list)
    for r in x:
        por[r["modo_final"]].append(r)
    out = []
    for modo in sorted(por, key=lambda m: -len(por[m])):
        g = por[modo]
        c = sum(_fl(r, "coste") for r in g)
        p = sum(_fl(r, "pnl") for r in g)
        out.append(f"      {modo:20s} merc {len(g):4d} ({len(g) / max(len(x), 1):4.0%}) | PnL {p:+8.2f} $ | coste {c:8.2f} | "
                   f"EV/€ {(p / c if c > 0 else float('nan')):+.4f}")
    return out


def delta_vs_base(filas, pol, motor, dias):
    """Σ(pnl_pol − pnl_BASE) emparejado por mercado + IC90 de la media diaria (bootstrap por días)."""
    base = {(r["dia"], r["mkt"]): _fl(r, "pnl") for r in filas if r["pol"] == motor and r["dia"] in dias}
    pd_ = collections.defaultdict(float)
    n = 0
    for r in filas:
        if r["pol"] == pol and r["dia"] in dias:
            k = (r["dia"], r["mkt"])
            if k in base:
                pd_[r["dia"]] += _fl(r, "pnl") - base[k]
                n += 1
    if not pd_:
        return "Δ vs BASE: n=0"
    v = np.array(list(pd_.values()))
    ic = None
    if len(v) >= 3:
        bt = np.random.default_rng(7).choice(v, size=(5000, len(v))).mean(axis=1)
        ic = (round(float(np.percentile(bt, 5)), 2), round(float(np.percentile(bt, 95)), 2))
    return f"Δ vs BASE emparejado: {v.sum():+.2f} $ en {n} merc, media diaria IC90 {ic}, {int((v > 0).sum())}/{len(v)} días+"


def ev_pol(filas, pol, dias):
    x = [r for r in filas if r["pol"] == pol and r["dia"] in dias]
    c = sum(_fl(r, "coste") for r in x)
    return sum(_fl(r, "pnl") for r in x) / c if c > 0 else -9.0


def main():
    global OUT
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default=",".join(DIAS))
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--control", action="store_true", help="añade _CTRL (R1 U=0 sin cancelación = v1) para la regresión")
    ap.add_argument("--max-mercados", type=int, default=None, help="prueba de humo: para tras N mercados cerrados; no cachea")
    ap.add_argument("--bn-v1", action="store_true", help="NO reinicia la ventana de 1 s de A_BN entre tramos del archivo (como v1)")
    ap.add_argument("--regresion-v1", action="store_true", help="compara BASE/CTRL con v1 sobre el MISMO fixture y sale")
    a = ap.parse_args()
    OUT = Path(a.out)
    V1.OUT = OUT                                    # escribir_cache de v1 usa su global; se apunta a NUESTRO directorio
    OUT.mkdir(parents=True, exist_ok=True)
    if a.regresion_v1:
        sys.exit(regresion_v1(a))
    pedidos = a.dias.split(",")
    codigo = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    man = {"job": "analisis_5m_cosechar_apertura_v2", "script": Path(__file__).name, "script_sha256": codigo,
           "v1_sha256": hashlib.sha256(Path(V1.__file__).read_bytes()).hexdigest(), "args": vars(a),
           "params": {"PAR": PAR, "L_TOMADOR_MS": L_TOMADOR_MS, "CANCEL_MS": CANCEL_MS, "U": U_LIST, "X": X_LIST, "K": K_LIST,
                      "SKEW_BPS": SKEW_BPS, "SH": SH, "FEE": FEE, "REB": REB},
           "dias_pedidos": pedidos, "dias_ok": [], "dias_ausentes": [], "dias_sin_filas": [], "dias_truncados": [],
           "dias_fallidos": {}, "cobertura_dia": {}, "entradas": {}, "inicio_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "fin_utc": None, "estado": "RUNNING"}
    V1.escribir_atomico(OUT / "manifiesto.json", json.dumps(man, indent=1))
    filas, vistos, duplicados = [], set(), 0
    for d in pedidos:
        try:
            ent = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
            if ent.exists():
                man["entradas"][d] = {"bytes": ent.stat().st_size, "sha256": hash_fichero(ent)}
            r = simular_dia(d, a.control, a.max_mercados, codigo[:10], a.bn_v1)
        except Exception as e:
            man["dias_fallidos"][d] = f"{type(e).__name__}: {e}"
            print(f"  {d}: FALLIDO {man['dias_fallidos'][d]}", file=sys.stderr, flush=True)
            V1.escribir_atomico(OUT / "manifiesto.json", json.dumps(man, indent=1))
            continue
        if r is None:
            man["dias_ausentes"].append(d)
            print(f"  {d}: AUSENTE (sin m5_registro)", flush=True)
        else:
            fl, cov = r
            nuevas = []
            for x in fl:
                k = (x["dia"], x["pol"], x["mkt"])
                if k in vistos:
                    duplicados += 1
                else:
                    vistos.add(k)
                    nuevas.append(x)
            filas += nuevas
            man["cobertura_dia"][d] = cov
            (man["dias_ok"] if fl else man["dias_sin_filas"]).append(d)
            if cov and cov.get("origen_truncado"):
                man["dias_truncados"].append(d)
            print(f"  {d}: {len(fl)} filas (mercados {len({x['mkt'] for x in fl})})", flush=True)
        V1.escribir_atomico(OUT / "manifiesto.json", json.dumps(man, indent=1))
    completo = (len(man["dias_ok"]) == len(pedidos) and not man["dias_truncados"] and not man["dias_fallidos"]
                and not duplicados and not a.max_mercados)
    cobertura = (f"COBERTURA: {len(man['dias_ok'])}/{len(pedidos)} días con filas | ausentes (sin registro): "
                 f"{man['dias_ausentes'] or 'ninguno'} | sin filas: {man['dias_sin_filas'] or 'ninguno'} | origen truncado: "
                 f"{man['dias_truncados'] or 'ninguno'} | fallidos: {list(man['dias_fallidos']) or 'ninguno'} | duplicados: "
                 f"{duplicados} | VEREDICTO {'COMPLETE' if completo else 'PARTIAL'}")
    cs = [c for c in man["cobertura_dia"].values() if c]
    cob2 = ("COBERTURA mercados: " + ("n/d" if len(cs) < len(man["cobertura_dia"]) else
            f"vistos {sum(c['mercados_vistos'] for c in cs)} | cotizados {sum(c['mercados_cotizados'] for c in cs)} | con rellenos {sum(c['mercados_con_rellenos'] for c in cs)} | "
            f"sin desenlace oficial {sum(c['sin_desenlace'] for c in cs)} | no cerrados por corte "
            f"{sum(c['no_cerrados_por_corte'] for c in cs)} | filas {sum(c['filas'] for c in cs)} | incoherencias de eventos "
            f"{sum(c['incoherencias_eventos'] for c in cs)} | reacciones sin foto de libro {sum(c['sin_foto'] for c in cs)}"))
    pols = politicas(a.control)
    lines = [cobertura, cob2, f"COSECHAR PARES AL ABRIR v2 REACTIVA — BTC 5m, PAR {PAR}, DESC {DESC[0]}..{DESC[-1]}, "
             f"OOS {OOS[0]}..{OOS[-1]}", "EV/€ = ΣPnL/Σcoste con coste = capital comprado (maker+tomador, sin netear ventas); pnl SIN reembolso "
             "maker (aparte, '+reemb'); compara también el PnL TOTAL y el Δ emparejado."]
    full = list(lines)
    for etiqueta, dias in (("DESC", DESC), ("OOS", OOS)):
        lines.append(f"\n== {etiqueta}")
        full.append(f"\n== {etiqueta}")
        if not any(r["dia"] in dias for r in filas):
            lines.append("  (sin filas en estos días)")
            full.append("  (sin filas en estos días)")
            continue
        for pol, motor, kind, _v in pols:
            ln = f"  {pol:30s} {V1.resumen(filas, pol, dias)}"
            lines.append(ln)
            full.append(ln)
            full += desglose(filas, pol, dias)
            if kind:
                full.append("      " + delta_vs_base(filas, pol, motor, dias))
    elegibles = [p[0] for p in pols if "FINAL" in p[1] and (p[2] in ("R1", "R2", "R3") and p[3][4] and not p[0].endswith("_R1_U0.00")
                                                          or p[1].endswith(("_S1k1", "_S1k2")))]
    if elegibles and any(r["dia"] in DESC for r in filas):
        elegida = max(elegibles, key=lambda p: ev_pol(filas, p, DESC))
        info = next(p for p in pols if p[0] == elegida)
        lines.append(f"\nELEGIDA en DESC (reactivas y skew, cola FINAL, {len(elegibles)} candidatas: elegir el máximo de {len(elegibles)} "
                     f"infla el EV de DESC; el juicio es solo OOS): {elegida}")
        lines.append(f"DESC: {V1.resumen(filas, elegida, DESC)}")
        lines.append(f"OOS juicio elegida: {V1.resumen(filas, elegida, OOS)}")
        lines += ["  desglose modo_final OOS:"] + desglose(filas, elegida, OOS)
        lines.append("  " + delta_vs_base(filas, elegida, info[1], OOS))
        lines.append(f"OOS BASE de su motor ({info[1]}): {V1.resumen(filas, info[1], OOS)}")
        lines += ["  desglose modo_final OOS BASE:"] + desglose(filas, info[1], OOS)
        pos = sum(1 for p in elegibles if ev_pol(filas, p, OOS) > 0)
        lines.append(f"OOS: {pos}/{len(elegibles)} candidatas con EV/€ > 0 (referencia de multiplicidad).")
    txt = "\n".join(lines)
    print(txt)
    if not a.max_mercados:
        V1.escribir_atomico(OUT / "informe.txt", txt + "\n")
        V1.escribir_atomico(OUT / "desglose_modo_final.txt", "\n".join(full) + "\n")
    man["estado"] = "COMPLETE" if completo else "PARTIAL"
    man["fin_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    V1.escribir_atomico(OUT / "manifiesto.json", json.dumps(man, indent=1))


def regresion_v1(a):
    """Control de regresión: v1 y v2 sobre el MISMO fixture (primeras líneas del registro del día, hasta el corte de
    --max-mercados). Compara BASE y CTRL (R1 U=0 sin cancelación) de v2 con las filas de v1 para A0/A_BN P96 FINAL/CABEZA."""
    n = a.max_mercados or 20
    d = a.dias.split(",")[0]
    f = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    estado = correr_flujo(f, n, bn_compat=True)
    st = estado["st"]
    fix = OUT / "fixture" / "m5_registro"
    fix.mkdir(parents=True, exist_ok=True)
    with gzip.open(f, "rt", errors="replace") as fi, gzip.open(fix / f"m5_registro_{d}.csv.gz", "wt") as fo:
        for i, ln in enumerate(fi):
            if i >= st["lineas"]:
                break
            fo.write(ln)
    mk = mercados_cerrados(estado)
    des = V1.desenlaces(mk)
    filas, cov = construir_filas(d, estado, des, control=True)
    print(f"v2: líneas {st['lineas']}, t_stop {st['t_stop']}, cobertura {cov}")
    V1.VOL, V1.OUT = OUT / "fixture", OUT / "v1"
    V1.OUT.mkdir(parents=True, exist_ok=True)
    v1 = V1.simular_dia(d) or []
    nom_v1 = {f"{m}_P96_{c}" for m in ("A0", "A_BN") for c in ("FINAL", "CABEZA")}
    fin_ok = {m for m in mk if m in {r["mkt"] for r in filas}}                 # mercados cerrados por el corte y con desenlace
    v1d = {(r["pol"], r["mkt"]): r for r in v1 if r["pol"] in nom_v1 and r["mkt"] in fin_ok}
    mal, comparadas, maxdif = 0, 0, 0.0
    for sufijo in ("", "_CTRL"):
        v2d = {(r["pol"][:len(r["pol"]) - len(sufijo)] if sufijo else r["pol"], r["mkt"]): r for r in filas
               if r["pol"] in {n_ + sufijo for n_ in nom_v1}}
        if set(v1d) != set(v2d):
            print(f"  [{sufijo or 'BASE'}] CLAVES DISTINTAS: solo v1 {len(set(v1d) - set(v2d))}, solo v2 {len(set(v2d) - set(v1d))}")
            mal += 1
        for k in set(v1d) & set(v2d):
            comparadas += 1
            for c1, c2 in (("qY", "qY"), ("qN", "qN"), ("coste", "coste"), ("pnl", "pnl"), ("rebate", "rebate"),
                           ("completo", "completo_maker")):
                dif = abs(float(v1d[k][c1]) - float(v2d[k][c2]))
                maxdif = max(maxdif, dif)
                if dif > 2e-6:
                    mal += 1
                    print(f"  [{sufijo or 'BASE'}] DIFERENCIA {k} {c1}: v1 {v1d[k][c1]} v2 {v2d[k][c2]}")
    pnl1 = sum(float(r["pnl"]) for r in v1d.values())
    print(f"v1: {len(v1d)} filas P96 comparables, PnL total {pnl1:+.4f} $")
    for s in ("", "_CTRL"):
        x = [r for r in filas if r["pol"] in {n_ + s for n_ in nom_v1}]
        print(f"v2 {s or 'BASE':6s}: {len(x)} filas, PnL total {sum(float(r['pnl']) for r in x):+.4f} $")
    print(f"REGRESIÓN {'OK' if not mal and comparadas else 'FALLA'}: {comparadas} comparaciones fila×campo-grupo, "
          f"diferencias > 2e-6: {mal}, dif máxima {maxdif:.2e}")
    return 0 if (not mal and comparadas) else 1


if __name__ == "__main__":
    main()
