#!/usr/bin/env python3
"""pares_contabilidad.py -- contabilidad del experimento de pares 15m (experimento_pares_cola_15m.py), REHECHA desde
cero el 12-Oct (Javi: "rehaz la contabilidad desde cero, más acotada y clara") tras 25 pasadas de /code-review que
encontraban un hueco de dinero en cada ronda. Módulo PURO: sin red, sin disco, sin estado. Se prueba con
test_pares_contabilidad.py.

MODELO: cada orden real es un INTERVALO de relleno posible [lo, hi] (acciones).
  lo = mayor lectura de get_order (size_matched) recortada al tamaño. Un relleno no se deshace: lo solo SUBE.
       Ninguna otra fuente lo sube (/trades puede duplicar filas: solo sirve para detectar anomalías).
  hi = tamaño de la orden mientras no esté VERIFICADA. Solo baja por:
       - post_rechazada (4xx limpio: la orden no se creó) y sin ninguna lectura > 0  -> 0
       - alias (hash calculado que el exchange llamó con otro orderID: es la MISMA orden, cuenta una vez) -> 0
       - verificada: lectura de get_order hecha >= T_VERIF_S después de que la orden saliera del libro, f <= tamaño -> f
       - verificada_manual: Javi la cierra a mano (CLI) tras comprobarla fuera del sistema -> f
       Una anomalía (cualquier lectura > tamaño) la SUBE a ese valor y anula las bajadas (no se cree a nadie).
  Siempre hi >= lo.

PEOR CASO (pérdida máxima posible) de un mercado, EXACTO y en forma cerrada. Con a_i en [lo_i, hi_i] acciones de la
orden i a precio p_i y lado s_i, si gana el lado w la pérdida es  sum_i a_i*p_i - sum_{s_i = w} a_i
  = sum_{s_i != w} a_i*p_i + sum_{s_i = w} a_i*(p_i - 1).
El primer término crece con a_i (p_i > 0) -> hi_i; el segundo decrece (p_i < 1) -> lo_i. Así
  peor = max(0, max_w [ sum_{s_i != w} hi_i*p_i + sum_{s_i = w} lo_i*(p_i - 1) ]).
Sin subconjuntos ni cotas aproximadas, y nunca da crédito de par a una acción que no conste (lo) ni deja de cobrar una
que podría existir (hi). Una orden ilegible (lado/precio/tamaño no válidos) cuenta hi*1 sin crédito en ambos lados.

CAPITAL FUERA (tope de apuesta): por mercado, sum hi_i*p_i mientras el mercado no lleve ASIENTO_ONCHAIN_S acabado o
tenga alguna orden con hi > lo; asentado y todo verificado -> acciones que la wallet AÚN tiene on-chain de sus tokens * mayor precio pagado
(las redimidas o vendidas ya no cuentan). Sin lectura on-chain de ese mercado -> sum hi_i*p_i.

DINERO QUE NO CUADRA: saldo_inicial - pUSD on-chain <= sum_all hi_i*p_i + TOLERANCIA. Si no se cumple, salió de la wallet
más dinero del que pueden explicar todas las órdenes del ledger -> kill. (Un depósito o una redención solo lo relajan.)

EVENTOS (solo los "real": true; cualquier otro evento se ignora aquí):
  intencion_post {oid, slug, tok, lado YES|NO, precio, size}   antes del POST (fsync)
  post_rechazada {oid, status}                                  4xx: la orden no se creó
  alias          {oid, de}                                      oid (hash calculado) = la orden `de` del exchange
  lectura        {oid, f, status}                               size_matched de get_order
  fuera_libro    {oid, origen}                                  fuera del libro CONFIRMADO (cancelación o estado)
  verificada     {oid, f}                                       lectura >= T_VERIF_S tras fuera_libro, f <= tamaño
  verificada_manual {oid, f, motivo}                            cierre a mano de Javi
  anomalia       {oid, f, motivo}                               relleno visto > tamaño (get_order o /trades)
  kill / kill_rearmado {motivo, kill, anomalias}
"""
import math
from datetime import datetime

T_VERIF_S = 30.0          # verificación: lectura de get_order >= 30 s después de salir del libro (casados de los ms de
                          # la cancelación ya reflejados en size_matched); antes, la orden cuenta hasta su tamaño
ASIENTO_ONCHAIN_S = 600.0 # las acciones on-chain de un mercado solo se creen 10 min después de su cierre (antes un casado
                          # aún sin minar mostraría MENOS acciones de las que tenemos)
TOLERANCIA_SALDO = 0.05   # USDC de holgura del cuadre on-chain (redondeos de la comisión y del casado)
LADOS = ("YES", "NO")


def ts_epoch(e):
    """Hora (epoch) de un evento; None si falta o es ilegible (quien la necesita para BAJAR hi no la acepta)."""
    try:
        return datetime.fromisoformat(e.get("ts")).timestamp()
    except (TypeError, ValueError):
        return None


def _num(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


class Orden:
    __slots__ = ("oid", "slug", "tok", "lado", "precio", "size", "t_int", "ilegible", "lecturas", "f_max", "rechazada",
                 "alias", "t_fuera", "f_verif", "f_manual")

    def __init__(self, e):
        self.oid = e.get("oid")
        self.slug = e.get("slug")
        self.tok = e.get("tok")
        self.lado = e.get("lado")
        self.precio = _num(e.get("precio"))
        self.size = _num(e.get("size"))
        self.t_int = ts_epoch(e) or 0.0   # hora de la intención (0 si ilegible: cuenta como antigua)
        self.ilegible = not (self.lado in LADOS and self.precio is not None and 0.0 < self.precio < 1.0
                             and self.size is not None and self.size > 0 and isinstance(self.slug, str) and self.slug)
        self.lecturas = 0.0       # mayor lectura VÁLIDA (0 <= f), sin recortar
        self.f_max = 0.0          # mayor valor visto por cualquier fuente (anomalías incluidas)
        self.rechazada = False
        self.alias = False
        self.t_fuera = None       # PRIMER fuera_libro con hora legible
        self.f_verif = None       # última verificación VÁLIDA
        self.f_manual = None

    @property
    def tamano(self):
        return self.size if self.size is not None and self.size > 0 else 0.0

    @property
    def anomala(self):
        return self.f_max > self.tamano + 1e-6 or self.ilegible

    @property
    def lo(self):
        if self.alias:
            return 0.0
        return min(self.lecturas, self.tamano)

    @property
    def hi(self):
        if self.alias:
            return 0.0
        lo = self.lo
        if self.anomala:
            return max(self.tamano, self.f_max, lo)
        if self.f_manual is not None:
            return max(lo, self.f_manual)
        if self.f_verif is not None:
            return max(lo, self.f_verif)
        if self.rechazada and self.lecturas <= 0.0:
            return 0.0
        return max(self.tamano, lo)

    @property
    def abierta(self):
        """True si su relleno aún puede cambiar el presupuesto (hi > lo)."""
        return self.hi > self.lo + 1e-9


def plegar(ledger):
    """{oid: Orden} con SOLO eventos reales. Un oid sin intencion_post previa se ignora (no puede ser una orden nuestra
    sin intención: el POST va siempre después de escribirla con fsync); una 2ª intención del mismo oid no reinicia nada."""
    ords = {}
    for e in ledger:
        if not isinstance(e, dict) or not e.get("real"):
            continue
        t, h = e.get("tipo"), e.get("oid")
        if not h:
            continue
        if t == "intencion_post":
            if h not in ords:
                ords[h] = Orden(e)
            continue
        o = ords.get(h)
        if o is None:
            continue
        f = _num(e.get("f"))
        if t == "lectura":
            if f is not None and f >= 0:
                o.lecturas = max(o.lecturas, f)
                o.f_max = max(o.f_max, f)
        elif t == "anomalia":
            if f is not None:
                o.f_max = max(o.f_max, f)
            else:
                o.ilegible = True            # anomalía sin valor legible: sin crédito y sin bajar nunca
        elif t == "post_rechazada":
            o.rechazada = True
        elif t == "alias":
            o.alias = True
        elif t == "fuera_libro":
            te = ts_epoch(e)
            if te is not None and o.t_fuera is None:
                o.t_fuera = te
        elif t == "verificada":
            te = ts_epoch(e)
            if (f is not None and 0 <= f <= o.tamano + 1e-9 and o.t_fuera is not None and te is not None
                    and te >= o.t_fuera + T_VERIF_S):
                o.f_verif = f
                o.lecturas = max(o.lecturas, f)
        elif t == "verificada_manual":
            if f is not None and 0 <= f <= o.tamano + 1e-9:
                o.f_manual = f
                o.lecturas = max(o.lecturas, f)
    return ords


def peor_mercado(ordenes):
    """Pérdida máxima posible de las órdenes de UN mercado (ver docstring del módulo)."""
    s = {w: 0.0 for w in LADOS}
    for o in ordenes:
        if o.alias:
            continue
        if o.ilegible:
            for w in LADOS:
                s[w] += o.hi * 1.0
            continue
        for w in LADOS:
            s[w] += o.hi * o.precio if o.lado != w else o.lo * (o.precio - 1.0)
    return max(0.0, *s.values())


def por_mercado(ords):
    out = {}
    for o in ords.values():
        out.setdefault(o.slug if (isinstance(o.slug, str) and o.slug) else "?", []).append(o)
    return out


def peor_total(ords, candidata=None):
    """Peor caso sumado de todos los mercados; `candidata` = dict de intencion_post de la orden que se va a enviar."""
    grupos = por_mercado(ords)
    if candidata is not None:
        c = Orden(dict(candidata, oid="__candidata__"))
        grupos.setdefault(c.slug if not c.ilegible else "?", []).append(c)
    return sum(peor_mercado(xs) for xs in grupos.values())


def capital_mercado(ordenes, asentado, acciones_onchain):
    """Capital fuera de UN mercado. asentado: acabó hace >= ASIENTO_ONCHAIN_S. acciones_onchain: {tok: acciones} (puede
    traer tokens de otros mercados), o None si no se pudo leer."""
    bruto = sum(o.hi * (1.0 if o.ilegible else o.precio) for o in ordenes if not o.alias)
    if not asentado or any(o.abierta for o in ordenes) or acciones_onchain is None:
        return bruto
    pmax = {}
    for o in ordenes:
        if not o.alias and o.tok:
            pmax[o.tok] = max(pmax.get(o.tok, 0.0), 1.0 if o.ilegible else o.precio)
    toks = {o.tok for o in ordenes if not o.alias and o.tok}
    if any(t not in acciones_onchain for t in toks):
        return bruto
    return min(bruto, sum(acciones_onchain[t] * pmax.get(t, 1.0) for t in toks))


def exposicion_maxima(ords):
    """sum hi*p de TODAS las órdenes (lo máximo que el ledger puede explicar que haya salido de la wallet)."""
    return sum(o.hi * (1.0 if o.ilegible else o.precio) for o in ords.values() if not o.alias)


def anomalias_vistas(ledger):
    """oids con anomalía (real) que un kill_rearmado POSTERIOR a su PRIMERA detección lista en `anomalias`: Javi la vio.
    Re-detectarla después no vuelve a matar; una anomalía NUEVA (primera detección tras el rearme) sí."""
    primera, vistas = {}, set()
    for i, e in enumerate(ledger):
        if not isinstance(e, dict) or not e.get("real"):
            continue
        if e.get("tipo") == "anomalia" and e.get("oid"):
            primera.setdefault(e["oid"], i)
        elif e.get("tipo") == "kill_rearmado":
            lista = e.get("anomalias") or []
            vistas |= {k for k, i0 in primera.items() if i0 < i and k in lista}
    return vistas


def anomalias_sin_rearmar(ledger):
    """oids con anomalía (real) aún no cubiertos por ningún rearme (lo que --rearmar-kill debe enseñar y listar)."""
    primera = {}
    for i, e in enumerate(ledger):
        if isinstance(e, dict) and e.get("real") and e.get("tipo") == "anomalia" and e.get("oid"):
            primera.setdefault(e["oid"], i)
    return sorted(set(primera) - anomalias_vistas(ledger))
