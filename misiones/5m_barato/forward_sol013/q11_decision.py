#!/usr/bin/env python3
"""Logica comun ADDENDUM3_Q11 (sha c991602c) + ADDENDUM4_Q11 (sha 3dac1bf4; sustituye REFUTA y la tabla de veredicto): dias comparables, victoria
estricta, test entero 5k>=3n, nd_validos>=10, CONFIRMA en dos muestras, REFUTA solo con evidencia contraria significativa (R1-R3, IC90 por cierre Y
por dia), tabla A-H, estado terminal persistido (escritura atomica), dias cortados en el tope 2026-12-31, bootstrap B=4000 y placebo.
Solo codigo de evaluacion (0 ordenes). Lo importan filtro_sol013.py, q11/eval_pistas.py, q11/eval_giro.py."""
import os, re, glob, json, hashlib, datetime as dt
import numpy as np, pandas as pd

TOPE = '2026-12-31'
EJEC_CIERRE = '2027-01-01'   # ADDENDUM4 sec. 4 fila F: fecha de ejecucion UTC >= esta => CERRADO_INSUFFICIENT si nd<20
SEEDS_DIA = {'SOL013': 20261113, 'P-A': 20261114, 'P-B': 20261115, 'P-C': 20261116, 'thru1': 20261107}   # ADDENDUM4 sec. 2
TERMINALES = ('CONFIRMA_FINAL', 'REFUTA', 'REFUTED', 'CERRADO_INSUFFICIENT')
DEC_OUT = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/'
NAN = float('nan')
CL_CACHE = '/root/polymarket-research-datalogs/q11_cl_cache/'   # rasgo Chainlink congelado por dia (data/prices rota a ~20 d: scripts/comprimir_data_historica.sh DIAS_BORRAR=20)
PRICES = '/root/polymarket-research/data/prices/'
COINS = ('ETH', 'SOL', 'XRP')


def f3(v): return 'nan' if v is None or v != v else f'{v:+.3f}'
def si(b): return 'si' if b else 'no'
def gt(v, t=0.0): return bool(v is not None and v == v and v > t)
def lt(v, t=0.0): return bool(v is not None and v == v and v < t)
def ok60(k, nd): return nd >= 10 and 5 * k >= 3 * nd  # ">= 60 %" en enteros (ADDENDUM3 sec. 0)


def cargar_dias(out, desde, hasta='9999-12-31'):
    """Dias validos = dec2_D y dec3s100_D (D>=desde, <=min(hasta, TOPE)). Devuelve (dias, R2, R3, errores). Filas con cost<=0 = sin relleno (se descartan).
    Solo cuentan nombres canonicos dec2_YYYY-MM-DD.pkl / dec3s100_YYYY-MM-DD.pkl (dias = sorted(set(...))); un fichero dec2_*/dec3s100_* con otro nombre que cite una
    fecha de la ventana (copia, .bak, _old) es ambiguo => ERROR_DATOS (fail-closed). Toda fila debe tener dia == D del fichero; si no, errores != [] y el llamador
    debe emitir INSUFFICIENT (ERROR_DATOS)."""
    hasta = min(hasta, TOPE)   # ADDENDUM4 sec. 4: un dia posterior al tope nunca entra aunque la evaluacion se ejecute tarde
    pat = {nm: re.compile(nm + r'_(\d{4}-\d{2}-\d{2})\.pkl') for nm in ('dec2', 'dec3s100')}; found = {nm: set() for nm in pat}; err = []
    for nm in pat:
        for f in glob.glob(out + nm + '_*.pkl'):
            b = os.path.basename(f); m = pat[nm].fullmatch(b)
            if m: found[nm].add(m.group(1)); continue
            m2 = re.search(r'(\d{4}-\d{2}-\d{2})', b)
            if m2 and desde <= m2.group(1) <= hasta: err.append(f'{b}: nombre no canonico que cita el dia {m2.group(1)} (ambiguo; retirar o renombrar)')
    dias = [d for d in sorted(found['dec2'] & found['dec3s100']) if desde <= d <= hasta]
    R2, R3 = [], []
    for d in dias:
        for nm, lst in (('dec2', R2), ('dec3s100', R3)):
            x = pd.read_pickle(f'{out}{nm}_{d}.pkl')
            if len(x) and (x['dia'].astype(str) != d).any(): err.append(f'{nm}_{d}.pkl: filas con dia != {d}')
            lst.append(x[x.cost > 0] if len(x) else x)
    cat = lambda L: pd.concat(L, ignore_index=True) if L else pd.DataFrame()
    return dias, cat(R2), cat(R3), err


def nd_ficheros(out, desde, hasta='9999-12-31'):
    """ADDENDUM5 sec. 1: numero de dias D, desde <= D <= min(hasta, TOPE), con dec2_D y dec3s100_D canonicos presentes, contado SOLO por nombre (sin leer ni calcular nada)."""
    _, got = dias_sin_pareja(out, desde, hasta); hasta = min(hasta, TOPE)
    return len([d for d in got['dec2'] & got['dec3s100'] if desde <= d <= hasta])


def dias_sin_pareja(out, desde, hasta='9999-12-31'):
    """Dias de la ventana con dec2_D pero sin dec3s100_D (o al reves): no son error ni dia valido; los evaluadores los muestran como AVISO explicito (nunca en silencio)."""
    hasta = min(hasta, TOPE); got = {}
    for nm in ('dec2', 'dec3s100'):
        pat = re.compile(nm + r'_(\d{4}-\d{2}-\d{2})\.pkl'); got[nm] = {m.group(1) for f in glob.glob(out + nm + '_*.pkl') for m in [pat.fullmatch(os.path.basename(f))] if m}
    return sorted(d for d in (got['dec2'] ^ got['dec3s100']) if desde <= d <= hasta), got


def cl_dia(dia, hoy=None, cache=None, prices=None, coins=COINS):
    """Serie Chainlink (source=='chainlink', reloj de RECEPCION) de UN dia para ETH/SOL/XRP, leyendo el CSV UNA vez (asset.isin). Cache propia primero: se congela al leer un
    dia COMPLETO (dia < hoy) con metadatos (dia, creado, fuente, sha256 de la fuente); el CSV de data/prices rota a ~20 dias. ERROR_DATOS solo si no esta en cache Y falta el CSV (o
    falta/esta vacia alguna de `coins`, o la cache es ilegible). -> (dict moneda -> DataFrame['ms','p'] ordenado y sin duplicados, error|None)"""
    cache = CL_CACHE if cache is None else cache; prices = PRICES if prices is None else prices; cf = f'{cache}cl_{dia}.pkl'
    def val(ser, orig):
        for c in coins:
            if c not in ser or not len(ser[c]): return None, f'chainlink {dia}: {orig} sin filas source=chainlink de {c} (ERROR_DATOS)'
        return ser, None
    if os.path.exists(cf):
        try:
            c = pd.read_pickle(cf); assert c['dia'] == dia and isinstance(c['series'], dict), 'metadatos no coinciden'
        except Exception as e: return None, f'chainlink {dia}: cache {cf} ilegible/invalida ({e}) (ERROR_DATOS)'
        return val(c['series'], 'cache')
    f = next((prices + f'chainlink_{dia}{e}' for e in ('.csv.gz', '.csv') if os.path.exists(prices + f'chainlink_{dia}{e}')), None)
    if f is None: return None, f'chainlink {dia}: sin cache ni CSV (ERROR_DATOS)'
    x = pd.read_csv(f, usecols=['timestamp_utc', 'asset', 'price_usd', 'source']); x = x[(x.source == 'chainlink') & x.asset.isin(COINS)]
    ms = pd.to_datetime(x.timestamp_utc, utc=True).dt.as_unit('ms').astype('int64').values   # as_unit('ms'): pandas>=3 devuelve us
    ser = {}
    for c in COINS:
        m = (x.asset == c).values; d_ = pd.DataFrame({'ms': ms[m], 'p': x.price_usd.values[m]}).sort_values('ms').drop_duplicates('ms').reset_index(drop=True); ser[c] = d_
    if dia < (hoy or hoy_utc()):   # dia completo: se congela
        try:
            os.makedirs(cache, exist_ok=True); tmp = cf + '.tmp'
            meta = dict(dia=dia, creado=dt.datetime.now(dt.timezone.utc).strftime('%FT%TZ'), fuente=f, sha256_fuente=hashlib.sha256(open(f, 'rb').read()).hexdigest(), n={c: len(v) for c, v in ser.items()}, series=ser)
            pd.to_pickle(meta, tmp); os.replace(tmp, cf)
        except OSError: pass   # sin cache el evaluador sigue leyendo el CSV (la politica fail-closed la da val)
    return val(ser, 'CSV')


def cl_series(dias, coins=COINS, hoy=None, cache=None, prices=None):
    """Une los dias pedidos (cache o CSV, una lectura por dia). -> ({moneda: (ms ndarray, p ndarray)}, [errores ERROR_DATOS]); con algun error el dict va vacio."""
    parts = {c: [] for c in coins}; err = []
    for d in sorted(set(dias)):
        ser, e = cl_dia(d, hoy, cache, prices, coins)
        if e: err.append(e); continue
        for c in coins: parts[c].append(ser[c])
    if err: return {}, err
    out = {}
    for c in coins: s_ = pd.concat(parts[c]).sort_values('ms').drop_duplicates('ms'); out[c] = (s_.ms.values, s_.p.values)
    return out, []


# ---------- metricas ----------
def ev(x): return x.pnl.sum() / x.cost.sum() if x is not None and len(x) and x.cost.sum() > 0 else NAN


def evdia(x):
    if x is None or not len(x): return pd.Series(dtype=float)
    g = x.groupby('dia')[['pnl', 'cost']].sum(); g = g[g.cost > 0]; return g.pnl / g.cost


def dias_relleno(x): return set(evdia(x).index)


def sin2(x, mejores=True):
    """EV sin los 2 mejores (o peores) dias por PNL; NaN con <=2 dias."""
    if x is None or not len(x): return NAN
    g = x.groupby('dia')[['pnl', 'cost']].sum(); g = g[g.cost > 0]
    if len(g) <= 2: return NAN
    r = g.sort_values('pnl', ascending=not mejores).iloc[2:]
    return r.pnl.sum() / r.cost.sum() if r.cost.sum() > 0 else NAN


def _gc(x): return x.groupby('fin')[['pnl', 'cost']].sum().values


def vec_cierre(x, B, seed):
    """Bootstrap de cierres del ratio sum(pnl)/sum(cost); None con <3 cierres."""
    if x is None or not len(x): return None
    g = _gc(x)
    if len(g) < 3: return None
    i = np.random.default_rng(seed).integers(0, len(g), (B, len(g)))
    s = g[i].sum(axis=1)
    with np.errstate(all='ignore'): return s[:, 0] / s[:, 1]


def vec_dif(A, Bm, B, seed):
    """Bootstrap de cierres de EV(Bm) - EV(A) (cada brazo remuestreado por separado); None con <3 cierres en alguno."""
    if A is None or Bm is None or not len(A) or not len(Bm): return None
    ga, gb = _gc(A), _gc(Bm)
    if len(ga) < 3 or len(gb) < 3: return None
    rng = np.random.default_rng(seed)
    sa = ga[rng.integers(0, len(ga), (B, len(ga)))].sum(axis=1); sb = gb[rng.integers(0, len(gb), (B, len(gb)))].sum(axis=1)
    with np.errstate(all='ignore'): return sb[:, 0] / sb[:, 1] - sa[:, 0] / sa[:, 1]


def q(v, p): return NAN if v is None else float(np.quantile(v, p))


def placebo_p(df, sig, maskfun, n=1000, seed=20261106):
    """Permuta `sig` (array alineado con df) DENTRO de cada dia; spread = EV(C)-EV(H) con H=maskfun(sig). p bilateral =
    (1+#{|s_perm|>=|s_obs|})/(1+n) (ADDENDUM3 sec. 6). NaN si el observado no es definido."""
    if df is None or not len(df): return NAN
    pnl, cost, sig = df.pnl.values, df.cost.values, np.asarray(sig)
    grupos = [np.where(df['dia'].values == d)[0] for d in pd.unique(df['dia'])]
    def spread(s):
        m = maskfun(s)
        if m.sum() == 0 or (~m).sum() == 0 or cost[m].sum() <= 0 or cost[~m].sum() <= 0: return NAN
        return pnl[~m].sum() / cost[~m].sum() - pnl[m].sum() / cost[m].sum()
    obs = spread(sig)
    if obs != obs: return NAN
    rng = np.random.default_rng(seed); c = 0; tot = 0
    for _ in range(n):
        sp = sig.copy()
        for ix in grupos: sp[ix] = rng.permutation(sig[ix])
        v = spread(sp)
        if v == v: tot += 1; c += abs(v) >= abs(obs) - 1e-15
    return (1 + c) / (1 + tot) if tot else NAN


# ---------- estado terminal persistido ----------
def cargar_estado(path):
    if not os.path.exists(path): return {'racha': 0, 'last_nd': 0, 'terminal': None}
    with open(path) as f: return json.load(f)  # JSON corrupto => excepcion (fail-closed: no se sobrescribe)


def guardar_estado(path, st):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w') as f: json.dump(st, f, indent=1, default=str); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)


def hoy_utc(): return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d')


def err_dias(err):
    """Fechas (YYYY-MM-DD) citadas por cada mensaje de ERROR_DATOS; None si el mensaje no trae fecha (se trata como afectando a todo)."""
    out = []
    for e in err:
        m = re.search(r'(\d{4}-\d{2}-\d{2})', str(e)); out.append(m.group(1) if m else None)
    return out


def ic_dia(x, seed, B=4000, nmin=10):
    """IC90 por dia (ADDENDUM4 sec. 2): unidad = dia; (SUMA pnl_d, SUMA cost_d) del conjunto juzgado x (ya restringido a D_AB); B remuestras de nd dias con
    reposicion, idx = default_rng(seed).integers(0, nd, (B, nd)); estadistico = SUMA pnl / SUMA cost (ponderado por EUR); cuantiles 0,05/0,95 por defecto.
    NaN con nd < nmin (nd_validos >= 10)."""
    if x is None or not len(x): return NAN, NAN
    g = x.groupby('dia')[['pnl', 'cost']].sum(); g = g[g.cost > 0]; nd = len(g)
    if nd < nmin: return NAN, NAN
    idx = np.random.default_rng(seed).integers(0, nd, (B, nd)); pn, co = g.pnl.values, g.cost.values
    with np.errstate(all='ignore'): r = pn[idx].sum(axis=1) / co[idx].sum(axis=1)
    return float(np.quantile(r, 0.05)), float(np.quantile(r, 0.95))


def refuta_r123(n, cierres, n_min, cierres_min, evx, ic_c, ic_d, signo):
    """ADDENDUM4 sec. 1. signo='neg' (SOL013: hipotesis EV(T1)>0 => REFUTA con EV<0 y limite SUPERIOR de ambos IC90 <0) o 'pos' (P-A/P-B/P-C: hipotesis
    EV_w(H|Z)<0 => REFUTA con EV>0 y limite INFERIOR de ambos IC90 >0). ic_c, ic_d = (lo, hi). R1 metricas definidas (no NaN) con >=3 cierres; R2 minimos de
    fills y cierres; R3 evidencia contraria. Devuelve (refuta: bool, dict R1/R2/R3). NaN, <3 cierres o minimos => False (nunca REFUTA)."""
    k = 1 if signo == 'neg' else 0; cc, cd = ic_c[k], ic_d[k]
    r1 = cierres >= 3 and all(v is not None and v == v for v in (evx, cc, cd))
    r2 = n >= n_min and cierres >= cierres_min
    r3 = bool(r1 and ((evx < 0 and cc < 0 and cd < 0) if signo == 'neg' else (evx > 0 and cc > 0 and cd > 0)))
    return bool(r1 and r2 and r3), dict(R1=bool(r1), R2=bool(r2), R3=r3)


def en_revision(causa, nd_ficheros=0, err=(), thru1=False):
    """UNICA regla de `en_revision` del terminal B2 (ADDENDUM5 sec. 1): true si la causa es ERROR_DATOS (o hay `err`) o si nd_ficheros >= 20. `thru1=True`: el B2 por brazo de thru1 lleva en_revision=true
    siempre (ADDENDUM5 sec. 2). La usan SOL013, P-A/P-B/P-C (via veredicto), thru1 (salida temprana) y la rama PC_AS."""
    return bool(thru1 or err or causa == 'ERROR_DATOS' or nd_ficheros >= 20)


def veredicto(st, err, nvalid, nd, confirma, refuta, hoy=None, nd_ficheros=0):
    """Tabla de decision ADDENDUM4 sec. 4 (filas A-H) con la fila B2 de ADDENDUM5 sec. 1. Devuelve (token, detalle, estado_nuevo).
    confirma: sec. 3 de ADDENDUM3 cumplida (NaN = no cumplida). refuta: R1-R3 de ADDENDUM4 sec. 1 YA evaluadas por el llamador (False si NaN/minimos).
    nd = nd_validos de la comparacion principal; nvalid = dias validos (dec2+dec3s100 canonicos); nd_ficheros = dias con ambos ficheros por nombre (B2).
    A: terminal emitido => se mantiene (5b); ERROR_DATOS se anota y el llamador NO escribe estado; el token lleva ' [EN REVISION]' si el terminal trae en_revision=true
       (B2, persistido) o si el error afecta a un dia <= fecha del terminal (nunca se anula solo).
    B (hoy < 2027-01-01): ERROR_DATOS o nvalid=0 => INSUFFICIENT sin escribir estado. B2 (hoy >= 2027-01-01): => CERRADO_INSUFFICIENT terminal con nd = last_nd del estado cargado
       (NO el nd actual), causa ERROR_DATOS|SIN_DIAS_VALIDOS, motivo, nd_ficheros, en_revision (causa ERROR_DATOS o nd_ficheros>=20): cierre ADMINISTRATIVO. El llamador debe
       guardar el estado si el devuelto trae terminal nuevo (veredicto_sin_datos lo hace).
    Reevaluacion tras reabrir un B2 (ADDENDUM5 sec. 3, st['reabierto'] persistido por reabrir_b2): CONFIRMA_FINAL (fila C) y CONFIRMA provisional (fila G) NO se emiten; solo
    REFUTA, REFUTED o CERRADO_INSUFFICIENT."""
    hoy = hoy or hoy_utc(); st = dict(st); reeval = bool(st.get('reabierto'))
    if reeval: confirma = False
    if st.get('terminal'):   # A
        t = st['terminal']; tok = t['veredicto']; why = f"terminal desde {t['fecha']} (nd={t['nd']}); no se recalcula"
        if t.get('causa'): why += f" | cierre B2 ADMINISTRATIVO (causa={t['causa']}, nd_ficheros={t.get('nd_ficheros')}): no es evidencia a favor ni en contra de la hipotesis"
        en_rev = bool(t.get('en_revision'))
        if err:
            afecta = any(d is None or d <= t['fecha'] for d in err_dias(err))
            why += ' | ERROR_DATOS (no se escribe estado): ' + '; '.join(err[:3])
            if afecta: en_rev = True; why += ' | EN REVISION: el error afecta a dias <= fecha del terminal; escalar a la sesion principal (solo se anula por correccion de bug anotada en DECISION_LOG)'
        if en_rev: tok += ' [EN REVISION]'
        return tok, why, st
    if err or nvalid == 0:
        causa = 'ERROR_DATOS' if err else 'SIN_DIAS_VALIDOS'; motivo = '; '.join(err[:3]) if err else '0 dias validos'
        if hoy >= EJEC_CIERRE:   # B2
            st['last_eval'] = hoy
            st['terminal'] = {'veredicto': 'CERRADO_INSUFFICIENT', 'fecha': hoy, 'nd': st.get('last_nd', 0), 'causa': causa, 'motivo': motivo, 'nd_ficheros': nd_ficheros, 'en_revision': en_revision(causa, nd_ficheros, err)}
            tok = 'CERRADO_INSUFFICIENT' + (' [EN REVISION]' if st['terminal']['en_revision'] else '')
            return tok, f'B2 tope: ejecucion {hoy}>={EJEC_CIERRE} con causa={causa} ({motivo}); cierre ADMINISTRATIVO (nd=last_nd={st["terminal"]["nd"]}, nd_ficheros={nd_ficheros})', st
        return 'INSUFFICIENT', ('ERROR_DATOS: ' + motivo) if err else '0 dias validos', st   # B (no cuenta ningun dia nuevo; el llamador no escribe estado)
    baja = nd < st.get('last_nd', 0)
    if baja: st['racha'] = 0; st['last_nd'] = nd   # invariante last_nd <= nd: si nd baja (dia perdido, datos retirados) la racha se reinicia sin credito
    nuevo = nd > st.get('last_nd', 0)
    if nuevo:  # evaluaciones sin dia comparable nuevo no rompen ni alargan la racha
        st['racha'] = st.get('racha', 0) + 1 if confirma else 0
        st['last_nd'] = nd
    st['last_eval'] = hoy
    k = st.get('racha', 0)
    def term(v, why):
        st['terminal'] = {'veredicto': v, 'fecha': hoy, 'nd': nd}; return v, why, st
    if confirma and k >= 3 and nd <= 20: return term('CONFIRMA_FINAL', f'CONFIRMA en 3 evaluaciones consecutivas con nd aumentando (nd={nd})')   # C
    if nd >= 20: return term('REFUTED', f'nd={nd}>=20 sin CONFIRMA_FINAL (una racha en curso, {k}/3, no lo evita)')   # D
    if nd >= 10 and refuta: return term('REFUTA', f'R1-R3 de ADDENDUM4 sec. 1 cumplidas (nd={nd})')   # E
    if hoy >= EJEC_CIERRE: return term('CERRADO_INSUFFICIENT', f'tope: ejecucion {hoy}>={EJEC_CIERRE} con nd={nd}<20')   # F
    if confirma: return 'CONFIRMA', f'provisional {k}/3 (nd={nd}{"" if nuevo else ", sin dia comparable nuevo"}{", nd BAJO: racha reiniciada" if baja else ""})', st   # G
    if nd <= 2: why = f'nd={nd}<=2'   # H
    elif nd <= 9: why = f'nd={nd}<10 (REFUTA/REFUTED no disponibles)'
    else: why = f'nd={nd}: CONFIRMA y REFUTA no cumplidas (REFUTA incluye NaN/minimos no alcanzados) y nd<20'
    return 'INSUFFICIENT', why, st


def congelar_promocion(st_antes, st, linea, ok):
    """PROMOCION congelada en el instante del terminal (ADDENDUM3 sec. 4: un terminal no se recalcula). Devuelve (linea, ok, st): si ya habia terminal antes de esta
    evaluacion, se devuelve lo guardado en su dict (o 'NO' si el terminal es anterior a este mecanismo); si el terminal se emite ahora, se guarda; si no hay terminal, la
    linea es la recalculada (provisional, no se guarda)."""
    t0 = (st_antes or {}).get('terminal')
    if t0: return t0.get('promocion_linea', 'PROMOCION (alfa/4): NO | terminal previo sin linea congelada'), bool(t0.get('promocion_ok', False)), st
    if st.get('terminal'): st['terminal'] = dict(st['terminal'], promocion_linea=linea, promocion_ok=bool(ok))
    return linea, bool(ok), st


def reabrir_b2(estado_path, ref, hoy=None):
    """ADDENDUM5 sec. 3 (unica via, sin automatismo): anula un terminal B2 (el que trae `causa`) SOLO con una referencia escrita (ref: asiento de DECISION_LOG con sha, decidida
    ANTES de reevaluar). Conserva el terminal anulado y la ref en st['reabierto'], reinicia racha y last_nd; desde entonces veredicto() no puede emitir CONFIRMA_FINAL/CONFIRMA."""
    if not ref or not str(ref).strip(): raise SystemExit('reabrir B2: falta la referencia escrita (DECISION_LOG) de la decision')
    st = cargar_estado(estado_path); t = st.get('terminal')
    if not t or not t.get('causa'): raise SystemExit('reabrir B2: el estado no tiene un terminal B2 (CERRADO_INSUFFICIENT con causa)')
    st['reabierto'] = list(st.get('reabierto', [])) + [{'terminal': t, 'ref': str(ref), 'fecha': hoy or hoy_utc()}]; st['terminal'] = None; st['racha'] = 0; st['last_nd'] = 0
    guardar_estado(estado_path, st); return st


def reabrir_si_b2(estado_path, ref, hoy=None):
    """Para evaluadores con flag --reevaluar-b2 REF: reabre solo si el estado trae un terminal B2 (con `causa`); otros terminales NO se tocan. Devuelve True si reabrio."""
    if not os.path.exists(estado_path): return False
    t = cargar_estado(estado_path).get('terminal')
    if not t or not t.get('causa'): return False
    reabrir_b2(estado_path, ref, hoy); return True


def veredicto_sin_datos(estado_path, err, hoy=None, nd_ficheros=0):
    """Salida temprana de un evaluador (ERROR_DATOS, 0 dias validos, Chainlink ausente): un terminal ya emitido se imprime (A) con el aviso; el estado se guarda SOLO si
    veredicto() devuelve un terminal NUEVO (B2, hoy >= 2027-01-01; ADDENDUM5 sec. 1). Antes de esa fecha NO escribe estado (B)."""
    st0 = cargar_estado(estado_path); tok, why, st = veredicto(st0, err, 0, 0, False, False, hoy, nd_ficheros)
    if st.get('terminal') and not st0.get('terminal'): guardar_estado(estado_path, st)
    return tok, why


# ---------- contraste de pares P-A / P-B / P-C (H juzgado, C comparador) ----------
def par_muestra(H, C, seed, Bs=2000, Bp=4000):
    """Metricas de una muestra. IC90 de seguimiento con Bs=2000; IC de promocion (1,25 %/98,75 %) con corrida aparte Bp=4000 y la misma semilla."""
    m = dict(nH=len(H), cH=H.fin.nunique() if len(H) else 0, evH=ev(H), evC=ev(C), s2peorH=sin2(H, False), s2mejC=sin2(C, True))
    m['spread'] = m['evC'] - m['evH']
    v1, v2 = vec_cierre(H, Bs, seed), vec_dif(H, C, Bs, seed + 1)
    p1, p2 = vec_cierre(H, Bp, seed), vec_dif(H, C, Bp, seed + 1)
    m.update(icH_sup=q(v1, .95), icH_inf=q(v1, .05), icS_inf=q(v2, .05), icS_lo=q(v2, .05), icS_hi=q(v2, .95), pH_sup=q(p1, .9875), pS_inf=q(p2, .0125))
    return m


def evaluar_par(name, lab, Hn, Cn, dias, err, estado_path, hoy, extra, placebo, seed, p_aplica=True, seed_dia=None):
    """Aplica ADDENDUM3 a un par (H,C). lab=(nombre de H, nombre de C). extra(ds)->dict de condiciones adicionales (bool) sobre el
    conjunto de dias ds; placebo(ds)->p bilateral (o None). seed_dia = semilla del IC90 por dia (ADDENDUM4 sec. 2; por defecto SEEDS_DIA[name]).
    REFUTA = R1-R3 de ADDENDUM4 sec. 1 sobre D_HC (EV_w(H)>0 con limite INFERIOR de IC90 por cierre y por dia >0, n(H)>=40 y >=25 cierres).
    Devuelve (token, lineas, info). Guarda el estado (salvo ERROR_DATOS)."""
    dH, dC = dias_relleno(Hn), dias_relleno(Cn); D = sorted(set(dH) & set(dC)); nd = len(D)
    mu = {'todos los dias validos': (Hn, Cn, set(dias)), 'dias comparables D_HC': (Hn[Hn.dia.isin(D)] if len(Hn) else Hn, Cn[Cn.dia.isin(D)] if len(Cn) else Cn, set(D))}
    M, conds, ps = {}, {}, {}
    for k, (H, C, ds) in mu.items():
        m = par_muestra(H, C, seed); M[k] = m
        c = {f'n({lab[0]})>=40 y >=25 cierres': m['nH'] >= 40 and m['cH'] >= 25,
             f'1 EV_w({lab[0]})<0 e IC90 cierre sup<0': lt(m['evH']) and lt(m['icH_sup']),
             f'2 {lab[1]}-{lab[0]}>0 e IC90 cierre inf>0': gt(m['spread']) and gt(m['icS_inf']),
             f'3a EV_w({lab[0]}) sin 2 peores dias<0': lt(m['s2peorH'])}
        c.update(extra(ds))
        if placebo is not None:
            ps[k] = placebo(ds); c['placebo p_bil<=0,10'] = ps[k] == ps[k] and ps[k] <= 0.10
        conds[k] = c
    confirma = nd >= 10 and all(all(c.values()) for c in conds.values())
    mc = M['dias comparables D_HC']
    Hmc = Hn[Hn.dia.isin(D)] if len(Hn) else Hn
    icd = ic_dia(Hmc, SEEDS_DIA[name] if seed_dia is None else seed_dia)
    refuta, r123 = refuta_r123(mc['nH'], mc['cH'], 40, 25, mc['evH'], (mc['icH_inf'], mc['icH_sup']), icd, 'pos')
    refuta_def = r123['R1'] and r123['R2']
    st_antes = cargar_estado(estado_path)
    tok, why, st = veredicto(st_antes, err, len(dias), nd, confirma, refuta, hoy)
    ma, mb = M['todos los dias validos'], M['dias comparables D_HC']
    c1 = lt(ma['pH_sup']) and lt(mb['pH_sup']); c2 = gt(ma['pS_inf']) and gt(mb['pS_inf'])
    pv = [p for p in ps.values()]; pmax = max(pv) if pv and all(p == p for p in pv) else NAN
    if p_aplica and placebo is not None: pc = lt(pmax, 0.025000001) and pmax == pmax; ptxt = f'placebo p_bil={"nan" if pmax != pmax else f"{pmax:.4f}"} (1000 perm) req <=0,025: {si(pc)}'
    else: pc = True; ptxt = 'placebo: no aplica'
    promo = tok == 'CONFIRMA_FINAL' and c1 and c2 and pc
    prom = (f'PROMOCION (alfa/4): {"SI" if promo else "NO"} | seguimiento={tok} | c1 EV_w({lab[0]}) IC cierre sup 98,75% todos/comparables=({f3(ma["pH_sup"])},{f3(mb["pH_sup"])}) req <0: {si(c1)}'
            f' | c2 {lab[1]}-{lab[0]} IC cierre inf 1,25% todos/comparables=({f3(ma["pS_inf"])},{f3(mb["pS_inf"])}) req >0: {si(c2)} | {ptxt}')
    prom, promo, st = congelar_promocion(st_antes, st, prom, promo)   # un terminal no se recalcula: PROMOCION congelada al emitirlo
    if not err: guardar_estado(estado_path, st)
    L = [f'## {name}: dias validos={len(dias)} ({dias[0] if dias else None}..{dias[-1] if dias else None}) | con relleno {lab[0]}={len(dH)} {lab[1]}={len(dC)} | nd_validos(D_HC)={nd}']
    for k, m in M.items():
        L.append(f'[{k}] n({lab[0]})={m["nH"]} cierres={m["cH"]} EV_w({lab[0]})={f3(m["evH"])} IC90c sup {f3(m["icH_sup"])} | EV_w({lab[1]})={f3(m["evC"])} | {lab[1]}-{lab[0]}={f3(m["spread"])} IC90c ({f3(m["icS_lo"])},{f3(m["icS_hi"])}) | sin2peores({lab[0]})={f3(m["s2peorH"])} sin2mejores({lab[1]})={f3(m["s2mejC"])}' + (f' | placebo p_bil={ps[k]:.4f}' if k in ps and ps[k] == ps[k] else ''))
        L += [f'   - [{"x" if v else " "}] {kk}' for kk, v in conds[k].items()]
    L += [f'REFUTA(sobre D_HC, ADDENDUM4): R1={si(r123["R1"])} R2={si(r123["R2"])} R3={si(r123["R3"])} (EV_w({lab[0]})={f3(mc["evH"])} IC90 inf cierre={f3(mc["icH_inf"])} dia=({f3(icd[0])},{f3(icd[1])}))  => {si(refuta)} | racha {st.get("racha")}/3 last_nd={st.get("last_nd")}', prom, f'VEREDICTO {name}: {tok} ({why})']
    return tok, L, dict(nd=nd, confirma=confirma, refuta_def=refuta_def, refuta=refuta, r123=r123, ic_dia=icd, promocion=promo, detalle=why)
