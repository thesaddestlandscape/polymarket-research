#!/usr/bin/env python3
"""paso0_lib_v3.py -- COPIA de paso0_lib_v2.py (no se edita) con el FIX de `cargar`: v2 confundia 'rellenos sin segmento' con 'bidL NaN' (el segmento existe pero no habia bid vivo en g-300: bl = b300 - L = NaN);
run_C.log 10:40Z: RuntimeError '3 de 4630 rellenos sin segmento' en paso0_run_v2 e1n1/x1 causal (paso0_lib_v2.py:28). v3 distingue: (1) segmento ausente de verdad (merge indicator) -> RuntimeError (integridad);
(2) segmento presente con bidL NaN -> se cuenta (U.attrs['n_bidL_nan']) y geo6=False, como el original (NaN >= 0,06 es False). cargar(..., modo='legacy') reproduce paso0_lib.cargar (sin comprobacion, `assert ... or True`).
Docstring de v2: paso0_lib_v2.py -- COPIA de paso0_lib.py (NO se edita el original: su sha esta en ADDENDUM_A1) con (a) assert REAL + conteo de rellenos sin segmento (condicion 2 de INTEGRIDAD_V2_REVISION_A1_11nov) y
(b) x1_dia parametrizado por RELOJ/fuente (CONTRATO_RELOJES.md). Carga determinista de G0 (g0_fills/g0_segs, solo dias quemados <= 2026-11-09) + reglas E1, N1, X1 sobre unidades pareadas. Solo lectura; 0 ordenes."""
import os, sys, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, H)
import l2eval as E

SA2_DIR = '/root/polymarket-research-datalogs/sa_ms2/'

DIAS = ['2026-10-26', '2026-10-27', '2026-10-28', '2026-10-29', '2026-10-30', '2026-10-31', '2026-11-01', '2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07', '2026-11-08', '2026-11-09']
BAD_DIR = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'
B40_DIR = '/mnt/HC_Volume_106538179/libro5_b40/'; SA_DIR = '/root/polymarket-research-datalogs/sa_ms/'
D_DET, LAM_CANC, T_TOMADOR = 250, 60, 175


def cargar(fills=H + 'out/g0_fills.pkl', segs=H + 'out/g0_segs.pkl', dias=None, permitir_sin_segmento=False, modo='v3', hasta='2026-11-09'):
    """Fills G0 + segmento (bidL=b300-L -> GEO6, T al armar). Una fila por relleno. Devuelve (U, S).
    modo='legacy': igual que paso0_lib.cargar original (sin comprobar segmentos). modo='v3': U.attrs['n_rellenos_sin_segmento'] = rellenos SIN fila de segmento (merge indicator; >0 y no permitido -> RuntimeError);
    U.attrs['n_bidL_nan'] = rellenos con segmento pero sin bid vivo en g-300 (geo6=False, no es error). hasta: tope de dia (HOLD cerrado)."""
    assert modo in ('v3', 'legacy'), modo
    dias = dias or DIAS
    E.guard_dias(dias, 'paso0_cargar_v3', log=H + 'eval_log_v3.jsonl')   # log propio: eval_log.jsonl (A1) y eval_log_v2.jsonl no se tocan
    F = pd.read_pickle(fills); S = pd.read_pickle(segs)
    assert F.dia.max() <= hasta and S.dia.max() <= hasta
    key = ['dia', 'k', 'L', 'seg']
    assert not S.duplicated(key).any(), 'clave de segmento no unica'
    U = F.merge(S[key + ['bidL', 'T']].rename(columns={'T': 'T_arm'}), on=key, how='left', validate='m:1', indicator=True)
    n_sin = int((U._merge == 'left_only').sum()); n_nan = int((U.bidL.isna() & (U._merge == 'both')).sum()); U = U.drop(columns=['_merge'])
    if modo == 'v3' and n_sin and not permitir_sin_segmento: raise RuntimeError(f'{n_sin} de {len(U)} rellenos sin segmento (merge): se perderian en silencio en geo6/N1')
    U['geo6'] = U.bidL >= 0.06 - 1e-6
    U['pnl0'] = E.pnl_maker(U.gana, U.q, U.L, 0.0); U['pnl2'] = E.pnl_maker(U.gana, U.q, U.L, 0.2)
    assert np.allclose(U.pnl2, U.pnl), 'pnl de RT (rb 0,2) no reproducido'
    U['hora'] = ((U.t_dec // 3600000) % 24).astype(int); U['bloque'] = U.hora // 6
    U['trb'] = np.where(U.T_arm < 120, 0, np.where(U.T_arm < 210, 1, 2))
    U['fin_ms'] = U.fin.astype('int64') * 1000
    U = U.reset_index(drop=True); U.attrs['n_rellenos_sin_segmento'] = n_sin; U.attrs['n_bidL_nan'] = n_nan; U.attrs['n_rellenos'] = len(U)
    return U, S


def resumen_ev(U, S=None, dias=None, B=20000):
    """EV incondicional: nº colocaciones, rellenos, coste, pnl rb0/0,2, EV/eur ponderado, IC90 por dias (bootstrap de dias sobre razon de sumas), sin 2 mejores dias, % dias +."""
    dias = dias or sorted(U.dia.unique()); rng = np.random.default_rng(E.SEED)
    g = U.groupby('dia').agg(fills=('pnl0', 'size'), cost=('cost', 'sum'), pnl0=('pnl0', 'sum'), pnl2=('pnl2', 'sum')).reindex(dias).fillna(0)
    if S is not None: g['colocaciones'] = S[S.dia.isin(dias)].groupby('dia').size().reindex(dias).fillna(0)
    out = dict(n_dias=len(dias), fills=int(g.fills.sum()), cost=round(float(g.cost.sum()), 2), colocaciones=int(g.colocaciones.sum()) if 'colocaciones' in g else None)
    for nm in ('pnl0', 'pnl2'):
        num = g[nm].values; den = g.cost.values; n = len(dias)
        ix = rng.integers(0, n, (B, n)); bs = num[ix].sum(1) / np.maximum(den[ix].sum(1), 1e-9)
        o2 = np.argsort(-num / np.maximum(den, 1e-9))[2:]
        out[nm] = dict(pnl=round(float(num.sum()), 2), ev_eur=round(float(num.sum() / den.sum()), 4), ic90_dias=[round(float(np.quantile(bs, .05)), 4), round(float(np.quantile(bs, .95)), 4)],
                       ev_sin_2_mejores_dias=round(float(num[o2].sum() / den[o2].sum()), 4), pct_dias_pos=round(float((num > 0).mean()), 3), sd_pnl_dia=round(float(num.std(ddof=1)), 2),
                       pnl_por_colocacion=round(float(num.sum() / g.colocaciones.sum()), 5) if 'colocaciones' in g else None)
    return out


# ---------------------------------------------------------------- E1
def e1_aff(U, lam):
    """E1: una ficha por (dia, token, fin). Se conservan rellenos con tf <= t1 + lam (t1 = primer relleno); aff = quitados. Inversion: ultimo grupo (tf >= tlast - lam)."""
    g = U.groupby(['dia', 'token', 'fin'])['tf']
    t1 = g.transform('min').values; tl = g.transform('max').values; tf = U.tf.values
    return tf > t1 + lam, tf < tl - lam


def placebo_tokwin(U, aff, pot, B=20000, seed=E.SEED):
    """Placebo de GRUPO ALEATORIO por token-ventana: en cada (dia, token, fin) con r quitados de m rellenos se quitan r al azar de los m."""
    rng = np.random.default_rng(seed); sim = np.zeros(B); pot = np.asarray(pot, float); aff = np.asarray(aff)
    for _, ix in U.groupby(['dia', 'token', 'fin']).indices.items():
        r = int(aff[ix].sum()); m = len(ix)
        if r == 0: continue
        if r == m: sim += pot[ix].sum(); continue
        R = rng.random((B, m)); P = np.argpartition(R, r - 1, axis=1)[:, :r]; sim += pot[ix][P].sum(1)
    obs = float(pot[aff].sum()); return obs, float((sim >= obs - 1e-12).mean()), float(sim.mean())


# ---------------------------------------------------------------- N1
BASE_MIN_RELL, BASE_MIN_DIAS, MARGEN = 30, 5, 0.02


def n1_celdas(U):
    """TRAIN N1 sobre los rellenos G0^GEO6 de U: celdas (act, L, bloque, trb) armadas si n>=30, >=5 dias distintos y P^=(aciertos+0,5)/(n+1) >= L+0,02. Devuelve DataFrame de celdas."""
    G = U[U.geo6]; rows = []
    for (a, L, b, t), g in G.groupby(['act', 'L', 'bloque', 'trb']):
        n = len(g); p = (g.gana.sum() + 0.5) / (n + 1); dd = g.dia.nunique()
        rows.append(dict(act=a, L=L, bloque=int(b), trb=int(t), n=n, dias=dd, p_hat=round(float(p), 4), arma=bool(n >= BASE_MIN_RELL and dd >= BASE_MIN_DIAS and p >= L + MARGEN)))
    return pd.DataFrame(rows)


def n1_aplica(U, celdas):
    """aff = fila G0^GEO6 NO armada (quitada). Base = G0^GEO6. Las filas fuera de la base (no GEO6) no cuentan (pot=0, aff=False)."""
    arm = {(r.act, r.L, r.bloque, r.trb) for r in celdas.itertuples() if r.arma}
    k = list(zip(U.act, U.L, U.bloque, U.trb)); armed = np.array([x in arm for x in k])
    return U.geo6.values & ~armed, U.geo6.values & armed          # (quitada, armada)


# ---------------------------------------------------------------- X1
def _tick(a):
    return np.where((a > 0.96) | (a < 0.04), 0.001, 0.01)


def x1_dia(U, dia, d_det=D_DET, ticks_adj=0, clock='ex', fuente='v2'):
    """X1 para un dia: devuelve DataFrame (indice de U) con M, pot_x (Delta por unidad si se cubriera, rb-indep.), cov_ok, qc, a, mirror, size_ok. Lee sa_ms del dia (solo lectura).
    RELOJ (CONTRATO_RELOJES.md): X1 lee el ESTADO FISICO del libro del exchange en tf (relleno), en t_dec+68 y en tf+d_det+T_TOMADOR (llegada de nuestro tomador) -> clock='ex' (defecto, tf debe ser EXCHANGE:
    RT modo causal/legacy). d_det = latencia de deteccion DESDE el relleno real, ya incluye el desfase exchange->recepcion. clock='rx' = sensibilidad. fuente='v1' reproduce el sa_ms original (solo ex)."""
    assert clock in ('ex', 'rx') and fuente in ('v1', 'v2')
    if fuente == 'v1':
        assert clock == 'ex', 'sa_ms v1 solo tiene reloj exchange'
        z = np.load(SA_DIR + f'ms_{dia}.npz', allow_pickle=True); qk_ = z['q_k']; qt_ = z['q_t'].astype(np.int64); V_ = [z[f'q_v{j}'] for j in range(4)]
    else:
        z = np.load(SA2_DIR + f'ms2_{dia}.npz', allow_pickle=True); qk_ = z['q_k']; qt_ = z['q_t_ex' if clock == 'ex' else 'q_t_rx'].astype(np.int64); V_ = [z[f'q_v{j}'] for j in range(4)]
        if clock == 'rx':
            ok_ = qt_ >= 0; o_ = np.lexsort((np.arange(ok_.sum()), qt_[ok_], qk_[ok_].astype(np.int64))); qk_ = qk_[ok_][o_]; qt_ = qt_[ok_][o_]; V_ = [v[ok_][o_] for v in V_]
    toks = list(z['tokens']); tm = z['tmap']; t0 = int(z['t0']); ti = {t: i for i, t in enumerate(toks)}
    grp = {}
    for i, (act, marco, mid, fin, lado) in enumerate(tm): grp.setdefault((act, marco, mid, fin), {})[lado] = i
    comp = np.full(len(toks), -1)
    for g in grp.values():
        if len(g) == 2:
            a, b = list(g.values()); comp[a] = b; comp[b] = a
    qk = qk_.astype(np.int64); qt = qt_ + t0; v0, v1, v2, v3 = V_
    ks = np.searchsorted(qk, np.arange(len(toks) + 1))          # q ordenado por (k, t)
    D = U[U.dia == dia]; out = []
    for i, r in D.iterrows():
        k = ti.get(r.token, -1); res = dict(idx=i, M=np.nan, cov_ok=False, pot_x=0.0, qc=0.0, a=np.nan, mirror=False, size_ok=False)
        if k < 0: out.append(res); continue
        s, e = ks[k], ks[k + 1]; t = qt[s:e]; b = v0[s:e]
        lo = np.searchsorted(t, r.t_dec + 68); hi = np.searchsorted(t, r.tf, side='right')
        w = np.where(b[lo:hi] <= r.L + 1e-6)[0]
        if len(w): res['M'] = float(r.tf - t[lo + w[0]])
        j = np.searchsorted(t, r.tf, side='right') - 1
        btf = b[j] if j >= 0 else np.nan
        c = comp[k]
        if not np.isfinite(btf): out.append(res); continue
        alim = np.floor(np.round((1.01 - btf) * 100, 6)) / 100.0 - ticks_adj * 0.01
        tick = float(_tick(alim)); alim = np.floor(np.round(alim / tick, 6)) * tick
        tx = r.tf + d_det + T_TOMADOR
        a = np.nan; sz = np.nan; mir = False
        if c >= 0:
            s2, e2 = ks[c], ks[c + 1]; t2 = qt[s2:e2]; jj = np.searchsorted(t2, tx, side='right') - 1
            if jj >= 0 and np.isfinite(v1[s2 + jj]) and v1[s2 + jj] > 0: a = float(v1[s2 + jj]); sz = float(v3[s2 + jj])
        if not np.isfinite(a):
            jx = np.searchsorted(t, tx, side='right') - 1
            if jx >= 0 and np.isfinite(b[jx]): a = float(1.0 - b[jx]); sz = r.q; mir = True
        if not np.isfinite(a) or a > alim + 1e-9: out.append(res); continue
        qc = min(r.q, sz) if np.isfinite(sz) else r.q
        if qc <= 0: out.append(res); continue
        fee = round(0.07 * a * (1 - a), 5)
        res.update(cov_ok=True, qc=float(qc), a=a, mirror=mir, size_ok=bool(qc >= r.q - 1e-9), pot_x=float(qc * ((1 - a - fee) - r.gana)))
        out.append(res)
    return pd.DataFrame(out).set_index('idx')
