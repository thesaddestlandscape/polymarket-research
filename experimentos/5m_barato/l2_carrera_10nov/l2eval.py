#!/usr/bin/env python3
"""l2eval.py -- evaluador determinista de los gates de PREREG_L2_V2 (sha 573dae38...). Solo lectura de datos; 0 ordenes; sin red.
Unidad = fila con: dia, act (moneda), L, fin (cierre), cost (coste base de la unidad, para EV/eur y veto), pot0 / pot2 = delta POTENCIAL de la unidad si la regla la afecta
(rb=0 / rb=0,2), aff = bool (regla la afecta), aff_inv = bool (inversion §3). Para reglas de quita pot = -pnl; para adiciones pot = pnl de lo anadido y aff = True.
Funciones puras (semilla fija). `guard_dias` impide leer dias HOLD (>=2026-11-10) salvo hold=True y escribe eval_log.jsonl (append-only)."""
import json, os, time, hashlib
import numpy as np, pandas as pd
from scipy import stats

H = os.path.dirname(os.path.abspath(__file__)) + '/'
PREREG_SHA = '573dae3893c47adf2b0fbf95c8c4610a894eb3e9b6a975b229025df8d7b4491d'
HOLD_DESDE = '2026-11-10'
K, LOOKS = 8, 2
ALPHA = 0.05 / (K * LOOKS)          # 0,003125 (una cola)
SEED = 20261110
STRAT = ['dia', 'L', 'act']


def sha_ok():
    return hashlib.sha256(open(H + 'PREREG_L2_V2.md', 'rb').read()).hexdigest() == PREREG_SHA


def guard_dias(dias, regla, hold=False, log=H + 'eval_log.jsonl'):
    """Rechaza dias >= HOLD_DESDE salvo hold=True; escribe una linea append-only por llamada (ts, regla, dias leidos). Sin log = dia quemado."""
    dias = sorted(set(dias))
    if any(d >= HOLD_DESDE for d in dias) and not hold:
        raise PermissionError(f'dias HOLD {[d for d in dias if d >= HOLD_DESDE]} bloqueados (hold=False)')
    if not sha_ok():
        raise RuntimeError('PREREG_L2_V2.md cambio: hash distinto del congelado')
    with open(log, 'a') as f:
        f.write(json.dumps(dict(ts=time.strftime('%FT%TZ', time.gmtime()), regla=regla, dias=dias, hold=bool(hold))) + '\n')
    return dias


def pnl_maker(gana, q, L, rb):
    """pnl maker por fila: q*(1{gana} - L + rb*0,07*L*(1-L))."""
    return q * (gana - L + rb * 0.07 * L * (1 - L))


def ev_eur(pnl, cost):
    c = float(np.sum(cost)); return float(np.sum(pnl)) / c if c > 0 else float('nan')


def daily(U, col, mask, dias):
    s = U.loc[mask].groupby('dia')[col].sum()
    return s.reindex(dias).fillna(0.0).values.astype(float)


def boot_lb(x, q, B=20000, seed=SEED):
    """cuantil q de la media del bootstrap por DIAS."""
    rng = np.random.default_rng(seed); n = len(x)
    if n == 0: return float('nan')
    m = x[rng.integers(0, n, (B, n))].mean(1)
    return float(np.quantile(m, q))


def t_lb(x, alpha):
    n = len(x)
    if n < 2: return float('nan')
    sd = x.std(ddof=1); se = sd / np.sqrt(n)
    return float(x.mean() - stats.t.ppf(1 - alpha, n - 1) * se) if se > 0 else float(x.mean())


def placebo(U, aff, pot, B=20000, seed=SEED, pool=None, strat=STRAT):
    """Placebo a IGUAL cobertura estratificado dia x L x moneda: en cada estrato se eligen n_aff unidades al azar (sin reposicion) de las del estrato
    (pool opcional: unidades elegibles, p.ej. con cobertura posible) y se suma su pot. Devuelve (obs, p, media, sim). p = P(sim >= obs)."""
    rng = np.random.default_rng(seed)
    aff = np.asarray(aff, bool); pot = np.asarray(pot, float); pool = np.ones(len(U), bool) if pool is None else np.asarray(pool, bool)
    obs = float(pot[aff].sum()); sim = np.zeros(B)
    for _, ix in U.groupby(strat, sort=True).indices.items():
        n = int(aff[ix].sum())
        if n == 0: continue
        cand = ix[pool[ix]]
        if len(cand) <= n:
            sim += pot[cand].sum() if len(cand) else 0.0; continue
        v = pot[cand]
        for s in range(0, B, 2000):
            e = min(B, s + 2000); R = rng.random((e - s, len(cand)))
            P = np.argpartition(R, n - 1, axis=1)[:, :n]
            sim[s:e] += v[P].sum(1)
    return obs, float((sim >= obs - 1e-12).mean()), float(sim.mean()), sim


def gate(U, dias, regla, rb='both', tipo='quita', B=20000, look=None, aplica_G6=True, nmin=None, pool=None, hold=False, quiet=False):
    """Evalua G1..G10 + REJECTED + veto de PREREG_L2_V2 §3-§4 para cada rb en {0;0,2}. Devuelve dict. look = 10 o 20 (None = solo descriptivo)."""
    dias = sorted(dias); out = dict(regla=regla, n_dias=len(dias), dias=dias, tipo=tipo, alpha_look=ALPHA, rb={})
    nmin = nmin if nmin is not None else (150 if tipo == 'quita' else 40)
    for rbk, col in ((0.0, 'pot0'), (0.2, 'pot2')):
        a = U['aff'].values; pot = U[col].values
        xd = daily(U, col, a, dias); tot = float(xd.sum())
        o, p, pm, sim = placebo(U, a, pot, B=B, pool=pool) if tipo == 'quita' else (tot, float('nan'), float('nan'), None)
        ai = U['aff_inv'].values if 'aff_inv' in U else None
        dinv = float(pot[ai].sum()) if ai is not None else float('nan')
        best2 = np.sort(xd)[::-1][2:].sum() if len(xd) > 2 else float('nan')
        by_coin = U.loc[a].groupby('act')[col].sum()
        coins = U['act'].unique(); ncoin_pos = int(sum(by_coin.get(c, 0.0) > 0 for c in coins))
        cov = float(U.loc[a, 'cost'].sum() / U['cost'].sum()) if tipo == 'quita' and U['cost'].sum() > 0 else float('nan')
        g = {}
        g['G1'] = tot > 0
        lb_b = boot_lb(xd, ALPHA, B); lb_t = t_lb(xd, ALPHA); lb90 = boot_lb(xd, 0.05, B)
        g['G2'] = bool(lb_b > 0 and lb_t > 0 and lb90 > 0)
        g['G3'] = True if tipo != 'quita' else bool(p < ALPHA)
        g['G4'] = bool(best2 > 0)
        g['G5'] = bool((xd > 0).mean() >= 0.60) if len(xd) else False
        g['G6'] = True if not aplica_G6 else bool(ncoin_pos >= int(np.ceil(2 * len(coins) / 3)))
        n_aff = int(a.sum()); g['G7'] = n_aff >= nmin
        g['G8'] = bool(not (dinv > 0)) if ai is not None else False
        g['G9'] = len(dias) >= 10
        if look == 10 and len(xd) >= 10:
            m1, m2 = xd[:5].mean(), xd[5:10].mean(); g['G10'] = bool(m2 >= 0.5 * m1) if m1 > 0 else False
        else: g['G10'] = True if look != 10 else False
        veto = bool(tipo == 'quita' and cov >= 0.85)
        rej = bool(tot <= 0 or (tipo == 'quita' and tot <= pm))
        out['rb'][str(rbk)] = dict(sum_delta=round(tot, 3), delta_eur_per_eur_base=round(tot / U['cost'].sum(), 5) if U['cost'].sum() > 0 else None,
            ev_conservado=None, n_afectadas=n_aff, cobertura_coste=None if np.isnan(cov) else round(cov, 3), placebo_p=None if np.isnan(p) else round(p, 5), placebo_media=None if np.isnan(pm) else round(pm, 3),
            media_dia=round(float(xd.mean()), 4) if len(xd) else None, sd_dia=round(float(xd.std(ddof=1)), 4) if len(xd) > 1 else None, lb_boot_alpha=round(lb_b, 4), lb_t_alpha=round(lb_t, 4), ic90_lb=round(lb90, 4),
            sin_2_mejores=None if np.isnan(best2) else round(float(best2), 3), pct_dias_pos=round(float((xd > 0).mean()), 3) if len(xd) else None, monedas_pos=ncoin_pos, delta_inv=None if ai is None else round(dinv, 3),
            gates=g, veto=veto, rejected=rej, daily=[round(float(v), 3) for v in xd])
        g_all = all(g.values()); out['rb'][str(rbk)]['pasa_todo_rb'] = bool(g_all and not veto)
    r0, r2 = out['rb']['0.0'], out['rb']['0.2']
    out['PROMISING_candidato'] = bool(r0['pasa_todo_rb'] and r2['pasa_todo_rb'])
    out['REJECTED'] = bool(r0['rejected'] or r2['rejected'])
    out['etiqueta'] = 'REJECTED' if out['REJECTED'] else ('PROMISING' if out['PROMISING_candidato'] else ('INSUFFICIENT' if len(dias) < 10 or look is None else 'NO_PASA'))
    return out


def stats_potencia(xd, alpha=ALPHA, power=0.8):
    """Dado el vector de Delta_d: media, sd, SNR y dias necesarios para detectar la media observada (una cola, t aprox. por normal) y media minima detectable a 10 y 20 dias."""
    xd = np.asarray(xd, float); n = len(xd); m = xd.mean(); sd = xd.std(ddof=1) if n > 1 else float('nan')
    za, zb = stats.norm.ppf(1 - alpha), stats.norm.ppf(power)
    need = ((za + zb) * sd / m) ** 2 if m > 0 else float('inf')
    mde = lambda N: (za + zb) * sd / np.sqrt(N) * (1 + 1.5 / N)    # correccion simple por t con pocos dias
    return dict(n_dias=n, media_dia=float(m), sd_dia=float(sd), dias_necesarios=float(need), mde10=float(mde(10)), mde20=float(mde(20)))


def valida_dia(dia, bad_dir, b40_dir, sa_dir, min_horas=12):
    """Dia valido por codigo (sin PnL): >= min_horas sanas (bad_D.json), b40 extraido sin corrupto (stats.json), sa_ms presente."""
    r = dict(dia=dia, valido=False, motivos=[])
    try:
        bad = {int(h) for dd, h in json.load(open(f'{bad_dir}bad_{dia}.json'))['bad'] if dd == dia}
    except Exception as e:
        r['motivos'].append(f'bad_{dia}.json ilegible: {type(e).__name__}'); return r
    r['horas_sanas'] = 24 - len(bad)
    if r['horas_sanas'] < min_horas: r['motivos'].append(f'horas sanas {r["horas_sanas"]} < {min_horas}')
    f = f'{b40_dir}libro5_b40_{dia}.csv.gz'; s = f'{b40_dir}libro5_b40_{dia}.stats.json'
    if not (os.path.exists(f) and os.path.exists(s)): r['motivos'].append('b40 no extraido')
    else:
        st = json.load(open(s)); r['b40_truncados'] = st.get('ficheros_truncados')
        if any(x.get('corrupto') for x in st.get('ficheros', [])): r['motivos'].append('b40 con fichero corrupto')
    if not os.path.exists(f'{sa_dir}ms_{dia}.npz'): r['motivos'].append('sa_ms ausente')
    r['valido'] = not r['motivos']; return r
