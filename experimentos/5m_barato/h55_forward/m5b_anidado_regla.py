"""m5b_anidado_regla.py -- DECISION PURA (sin E/S) de las reglas H55 / H53 / V4 / maker H23 del par anidado 5m/15m.
Es el UNICO sitio donde viven las reglas: el vigia offline (vectorizado sobre los instantes de un cierre) y el brazo H55 del
ejecutor F2 (escalar, en vivo) IMPORTAN estas funciones; no se copian. Cambiar cualquier constante = nueva VERSION y nuevo OOS.

Convenciones (identicas al descubrimiento 06-18 Oct, experimentos/5m_barato/anticipacion_v4/p6,p11 y v4_comprar_lo_bueno/r3/sim_dia3.py):
  par anidado de un cierre C (multiplo de 900): 5m que cierra en C y 15m que cierra en C. Lado s por TWAP60 oficiales
  (ref15 = twap60(C-900), ref5 = twap60(C-300); ref15 > ref5 => s = Up; |gap| >= 1 bp). BTC.
  instante t = HORA DE RECEPCION de una fila q del 5m-s o del 15m-s con (C-300)*1000+1500 <= t < (C-10)*1000, libro NO cruzado.
  margen = bid15(s) - ask5(s) - 0,07*ask5*(1-ask5)  (sin redondear, como el descubrimiento).
  compra virtual TOMADOR: llega a t+215 ms; se llena contra el ask NIVEL 1 vigente a t+215 si ask <= limite (+1e-9); acciones
  = min(objetivo, tamano del nivel 1); objetivo = max(5, 2/limite). Precio = ask a t+215 (no el limite).
"""
import numpy as np

VERSION = 1
FEE_TOMADOR = 0.07
REBATE_MAKER = 0.20
LAT_TOMADOR_MS = 215
LAT_POST_MS, LAT_CANCEL_MS = 68, 60
REF_CONOCIBLE_MS, FIN_MARGEN_S, GAP_MIN_BPS = 1500, 10, 1.0
STAKE_EUR, MIN_ACCIONES = 2.0, 5.0
REGLAS = {
    # nombre: (ask_min, ask_max, margen_min, tolerancia)
    "H55": (0.50, 0.95, -0.05, 1e-9),       # favorito anidado (variante F3 del registro)
    "H53": (0.0, 1.0, 0.02, 1e-9),          # V4b: umbral 0,02
    "V4": (0.0, 1.0, 0.05, 1e-12),          # V4 congelada (replica nivel 1; limite = p_limite(bid15))
}
MAKER_H23 = {"margen_min": -0.05}           # join en el bid 5m-s, cancelacion 60 ms, rebate 20 %


def fee(p):
    return FEE_TOMADOR * p * (1 - p)


def margen(bid15, ask5):
    return bid15 - ask5 - fee(ask5)


def p_limite(bid15, umbral=0.05):
    """Mayor precio de rejilla 0,01 con bid15 - p - fee(p) >= umbral (regla V4)."""
    p = np.floor(bid15 * 100 + 1e-9) / 100
    while p > 0 and bid15 - p - fee(p) < umbral - 1e-12:
        p = round(p - 0.01, 2)
    return p if p > 0 else None


def libro_cruzado(bid15, ask15, bid5, ask5):
    """True si alguna pata tiene bid > ask (bid no real). NaN -> False (se trata aparte como dato ausente)."""
    with np.errstate(invalid="ignore"):
        return (np.asarray(bid15) > np.asarray(ask15)) | (np.asarray(bid5) > np.asarray(ask5))


def senal(regla, ask5, bid15, bid5, ask15):
    """Condicion de disparo de `regla` en cada instante. Acepta escalares o arrays; NaN -> False. Sin libro cruzado."""
    amin, amax, mmin, tol = REGLAS[regla]
    a5, b15 = np.asarray(ask5, dtype=float), np.asarray(bid15, dtype=float)
    with np.errstate(invalid="ignore"):
        m = margen(b15, a5)
        ok = ~np.isnan(m) & ~libro_cruzado(b15, ask15, bid5, a5) & (m >= mmin - tol)
        if regla == "H55":
            ok &= (a5 >= amin - 1e-9) & (a5 <= amax + 1e-9)
    return ok


def acciones_objetivo(limite):
    return max(MIN_ACCIONES, STAKE_EUR / limite)


def limite_orden(regla, ask5_t, bid15_t):
    """Precio limite de la orden FOK: H55/H53 = ask5(t) (no pagar mas de lo visto); V4 = p_limite(bid15)."""
    return p_limite(bid15_t) if regla == "V4" else ask5_t


def llegada_tomador(ask_llegada, asz_llegada, limite, acc_obj):
    """Relleno virtual al nivel 1 vigente a la llegada. -> (acciones, precio) ; (0.0, None) si no llena."""
    if limite is None or ask_llegada is None or ask_llegada != ask_llegada:
        return 0.0, None
    if ask_llegada <= limite + 1e-9:
        return float(min(acc_obj, asz_llegada)), float(ask_llegada)
    return 0.0, None


def pnl_tomador(acc, precio, gana):
    """(pnl, coste) de una compra tomadora que resuelve a 1 si gana. gana None -> (None, coste)."""
    if acc <= 0 or precio is None:
        return 0.0, 0.0
    coste = acc * (precio + fee(precio))
    return (None if gana is None else acc * (float(gana) - precio - fee(precio))), coste


def pnl_maker(lleno, coste_sin_fee, gana):
    """El maker no paga comision y cobra el 20 % de la comision teorica del tomador."""
    if lleno <= 0:
        return 0.0, 0.0
    rebate = REBATE_MAKER * fee(coste_sin_fee / lleno) * lleno
    return (None if gana is None else lleno * float(gana) - coste_sin_fee + rebate), coste_sin_fee


def maker_join(inst, ask5, bid5, bid15, ask15, bsz5, fills, t_fin_ms, mq=None, lat_post=LAT_POST_MS, lat_cancel=LAT_CANCEL_MS):
    """Maker H23 'join' (port exacto de sim_dia3.py, variante join/-0,05/rx/60 ms). Bid en reposo en el 5m-s al precio del bid
    mientras bid <= p_limite(bid15) y margen >= mq y libro valido; se cancela (lat_cancel) al romper la condicion; alta a
    t+lat_post. Relleno solo si una operacion TOMADORA atraviesa la cola: `fills` = lista ordenada de (rx_ms, precio_equiv, tam)
    de ventas del token s a precio p o compras del token contrario a 1-p. Prioridad: atravesar el nivel = barrido; al mismo
    precio se consume primero la cola previa (bsz al unirse). -> dict(lleno, coste, t_rel, p_rel, n_cotiz, n_fill)."""
    mq = MAKER_H23["margen_min"] if mq is None else mq
    inst, ask5, bid5, bid15, ask15, bsz5 = (np.asarray(x) for x in (inst, ask5, bid5, bid15, ask15, bsz5))
    with np.errstate(invalid="ignore"):
        m = margen(bid15, ask5)
        cruz = (bid15 > ask15) | (bid5 > ask5)
        valid = ~cruz & ~np.isnan(ask5) & ~np.isnan(bid15) & ~np.isnan(bid5)
        pl = np.array([(np.nan if (p_limite(b) is None) else p_limite(b)) if v else np.nan for b, v in zip(bid15, valid)], dtype=float)
        cand = bid5.copy()
        okq = valid & ~np.isnan(pl) & (cand <= pl + 1e-9) & (cand < ask5 - 1e-9) & (cand >= bid5 - 1e-9) & (cand >= 0.01) & (m >= mq)
    want = np.full(len(inst), np.nan)
    want[okq] = cand[okq]
    segs, cur = [], np.nan      # [precio, cola, t_post, t_decision_cancel]
    for t, w, bsz, b5 in zip(inst, want, bsz5, bid5):
        if (np.isnan(w) and np.isnan(cur)) or (not np.isnan(w) and not np.isnan(cur) and abs(w - cur) < 1e-9):
            continue
        if not np.isnan(cur):
            segs[-1][3] = t
        if not np.isnan(w):
            segs.append([w, (bsz if abs(w - b5) < 1e-9 else 0.0), t + lat_post, None])
        cur = w
    need = max(MIN_ACCIONES, STAKE_EUR / segs[0][0]) if segs else MIN_ACCIONES
    fe = np.array([f[0] for f in fills], dtype=np.int64)
    lleno, coste, t_rel, p_rel, nfill = 0.0, 0.0, None, None, 0
    for sg in segs:
        if lleno >= need - 1e-9:
            break
        tc = (sg[3] + lat_cancel) if sg[3] is not None else t_fin_ms + lat_cancel
        a, b = np.searchsorted(fe, sg[2], "left"), np.searchsorted(fe, tc, "right")
        cola = sg[1]
        for ex_, pe, sz in fills[a:b]:
            falta = need - lleno
            if falta <= 1e-9:
                break
            if pe < sg[0] - 1e-9:
                x = falta
            elif abs(pe - sg[0]) < 1e-9:
                tomo = min(cola, sz)
                cola -= tomo
                x = min(falta, sz - tomo)
            else:
                x = 0.0
            if x > 0:
                lleno += x
                coste += x * sg[0]
                nfill += 1
                if t_rel is None:
                    t_rel, p_rel = ex_, sg[0]
    return {"lleno": round(lleno, 4), "coste": round(coste, 6), "t_rel": t_rel, "p_rel": p_rel, "n_cotiz": len(segs), "n_fill": nfill}


def combinado_una_via(mk_lleno, mk_t_rel, t_h53, h53_ejecuta):
    """H54: maker primero; el tomador H53 solo si el maker no se ha rellenado <= t_disparo + 60 ms. -> 'maker'|'tomador'|'nada'."""
    mf = (mk_lleno or 0) > 0
    tg = t_h53 is not None
    if mf and (not tg or mk_t_rel <= t_h53 + LAT_CANCEL_MS):
        return "maker"
    if tg and h53_ejecuta:
        return "tomador"
    return "nada"
