#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""formula_r2_28oct/analysis2.py — manda PREREG_FORMULA_R2.md. Lee out/s_*.csv.gz (sim2.py) + desenlace oficial."""
import gzip, csv, json, glob, sys, math
import numpy as np
BASE = '/root/polymarket-research/experimentos/5m_barato/formula_r2_28oct/'
SMOKE = '--smoke' in sys.argv
OUT = BASE + ('out_smoke/' if SMOKE else 'out/')
G = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
OOS = {'2026-10-23', '2026-10-24', '2026-10-25', '2026-10-26'}
B = 300 if SMOKE else 2000; BP = 100 if SMOKE else 500; SEED = 2811
DELTAS = [('p1', 0.01), ('z0', 0.0), ('m1', -0.01), ('m2', -0.02)]
GATES = ['U', 'G10', 'G5', 'GP5', 'I5']; CAND = ['U', 'G10', 'G5', 'GP5']; OPT = ['O_z0', 'O_m1', 'O_m2']
CUT = {'G10': -0.010, 'G5': -0.005, 'GP5': 0.005}
LN = [g + '_' + d for g in GATES for d, _ in DELTAS] + OPT
CL = [g + '_' + d for g in CAND for d, _ in DELTAS]
def fl(x):
    return float(x) if x not in (None, '', 'None') else float('nan')

seen = set(); dup = 0; miss = 0
D_, C_, BB_, EP_, FV_, GG_, T1_, K_ = [], [], [], [], [], [], [], []
SH = {l: [] for l in LN}; CO = {l: [] for l in LN}
for p in sorted(glob.glob(OUT + 's_*.csv.gz')):
    with gzip.open(p, 'rt') as f:
        for r in csv.DictReader(f):
            key = (r['mercado'], r['lado'])
            if key in seen: dup += 1; continue
            seen.add(key)
            w = G.get(str(r['mercado']))
            if w not in ('YES', 'NO'):
                if SMOKE: w = 'YES' if (sum(map(ord, key[0])) % 2) else 'NO'
                else: miss += 1; continue
            K_.append(key); D_.append(r['dia']); C_.append(r['coin']); BB_.append(float(r['bb_e'])); EP_.append(float(r['eps_e']))
            FV_.append(int(r['fv_e'])); GG_.append(1.0 if w == r['lado'] else 0.0); T1_.append(fl(r['U_p1_t1']))
            for l in LN: SH[l].append(float(r[l + '_sh'])); CO[l].append(float(r[l + '_cost']))
            D_[-1] = r['dia']
print('SMOKE (desenlaces sinteticos si falta; NO interpretable)' if SMOKE else 'DATOS REALES', 'unidades elegibles', len(D_), 'duplicadas', dup, 'sin desenlace', miss)
days = sorted(set(D_)); dmap = {d: i for i, d in enumerate(days)}; ND = len(days)
dayi = np.array([dmap[d] for d in D_], dtype=np.int64); coins = sorted(set(C_)); cid = np.array([coins.index(c) for c in C_], dtype=np.int64)
bbe = np.array(BB_); gw = np.array(GG_); ep = np.array(EP_); N = len(dayi)
bucket = np.clip(((bbe - 0.10) / 0.05 + 1e-9).astype(int), 0, 3)
strat = (dayi * 8 + cid) * 4 + bucket
sh = {l: np.array(SH[l]) for l in LN}; co = {l: np.array(CO[l]) for l in LN}
wr_u = (np.bincount(strat, weights=gw) / np.maximum(np.bincount(strat), 1))[strat]
print('dias', ND, days[0], days[-1], 'monedas', coins, 'fv15 disponible en el %.1f %% de las elegibles' % (100 * np.mean(FV_)))
isd = np.array([d not in OOS for d in days])

def cell(l):
    s = sh[l]; c = co[l]; f = s > 0
    avg = np.zeros(N); avg[f] = c[f] / s[f]
    reb = 0.2 * s * 0.07 * avg * (1.0 - avg)
    pnl = np.where(f, s * gw - c + reb, 0.0); unc = np.where(f, s * wr_u - c + reb, 0.0)
    bc = lambda x: np.bincount(dayi, weights=x, minlength=ND)
    return dict(l=l, s=s, c=c, f=f, reb=reb, pnl=pnl, unc=unc, pnl_d=bc(pnl), sh_d=bc(s), co_d=bc(c), nf_d=bc(f.astype(float)), unc_d=bc(unc))

rng = np.random.default_rng(SEED); IDX = rng.integers(0, ND, size=(B, ND))
def boot(num, den):
    with np.errstate(all='ignore'): return num[IDX].sum(1) / den[IDX].sum(1)
def ratio(num, den, m=None):
    if m is not None: num = num[m]; den = den[m]
    return float(num.sum() / den.sum()) if den.sum() > 0 else float('nan')
CE = {l: cell(l) for l in LN}
rows = {}
for l, c in CE.items():
    p_d, s_d = c['pnl_d'], c['sh_d']
    ev = ratio(p_d, s_d); bs = boot(p_d, s_d); se = float(np.nanstd(bs))
    lo, hi = (np.nanpercentile(bs, [5, 95]) if np.isfinite(bs).any() else (float('nan'), float('nan')))
    keep = np.ones(ND, bool); keep[np.argsort(-p_d)[:2]] = False
    asd = c['unc_d'] - p_d; asb = boot(asd, s_d); asv = ratio(asd, s_d)
    rows[l] = dict(ev=ev, se=se, lo=lo, hi=hi, bs=bs, evw=ratio(p_d, c['co_d']), ev2=ratio(p_d, s_d, keep), evw2=ratio(p_d, c['co_d'], keep),
                   ev_is=ratio(p_d, s_d, isd), ev_oos=ratio(p_d, s_d, ~isd), nf=int(c['f'].sum()), ndias=int((c['nf_d'] >= 5).sum()),
                   lam=float(c['f'].sum() / max(N, 1)), eur=float(p_d.sum()), asv=asv, as_lo=float(np.nanpercentile(asb, 5)) if np.isfinite(asb).any() else float('nan'),
                   as_hi=float(np.nanpercentile(asb, 95)) if np.isfinite(asb).any() else float('nan'), evplace=float(p_d.sum() / max(N, 1)))
# regresion contra unidades P de R1
U = {}
for p in glob.glob('/root/polymarket-research/experimentos/5m_barato/alpha_miner_b_27oct/units/u_*.csv.gz'):
    with gzip.open(p, 'rt') as f:
        for r in csv.DictReader(f): U[(r['mercado'], r['lado'])] = (fl(r['P_sh']), fl(r['P_cost']), fl(r['P_t1']))
ok_sh = ok_c = ok_t = nc = 0
for i, k in enumerate(K_):
    if k not in U: continue
    nc += 1; psh, pc, pt = U[k]; s1 = sh['U_p1'][i]; c1 = co['U_p1'][i]; t1 = T1_[i]
    ok_sh += abs(psh - s1) < 1e-6; ok_c += (abs(pc - c1) < 1e-6) or (psh == 0 and c1 == 0)
    ok_t += (math.isnan(pt) and math.isnan(t1)) or (not math.isnan(pt) and not math.isnan(t1) and abs(pt - t1) < 1.0)
print('REGRESION U_p1 vs P(R1): comunes %d de %d ; sh igual %.2f %% cost igual %.2f %% t1 igual %.2f %%' % (nc, N, 100 * ok_sh / max(nc, 1), 100 * ok_c / max(nc, 1), 100 * ok_t / max(nc, 1)))
print('\n== sigma_eps realizada en las elegibles: std %.4f ; P(eps<-0.010) %.3f P(eps<-0.005) %.3f P(eps<+0.005) %.3f ; media %.5f' % (
    ep.std(), np.mean(ep < -0.010), np.mean(ep < -0.005), np.mean(ep < 0.005), ep.mean()))
for g, c in CUT.items():
    kept = ep[ep >= c]
    print('   cota empirica %s: bloquea %.1f %% ; E[eps|eps>=c]-E[eps] = %+.4f por acc' % (g, 100 * np.mean(ep < c), kept.mean() - ep.mean()))

print('\n== TABLA por celda (EV/acc = sum pnl / sum acc ; IC90 por dias; AS = E[tasa_estrato - gana | relleno])')
print('celda  rellenos  lam  dias  EV/acc [IC90]  EVw  EVw-sin2  EV/acc IS | OOS  AS/acc [IC90]  EUR  EUR/elegible')
for l in LN:
    r = rows[l]
    print('%-7s %6d %.3f %3d %+.4f [%+.4f,%+.4f] %+.4f %+.4f  %+.4f | %+.4f  %+.4f [%+.4f,%+.4f] %+8.1f %+.4f' % (
        l, r['nf'], r['lam'], r['ndias'], r['ev'], r['lo'], r['hi'], r['evw'], r['evw2'], r['ev_is'], r['ev_oos'], r['asv'], r['as_lo'], r['as_hi'], r['eur'], r['evplace']))

# max-statistic bootstrap sobre las 16 celdas candidatas
T = np.array([rows[l]['ev'] / rows[l]['se'] if rows[l]['se'] > 1e-9 and np.isfinite(rows[l]['ev']) else -np.inf for l in CL])
TS = np.stack([(rows[l]['bs'] - rows[l]['ev']) / rows[l]['se'] if rows[l]['se'] > 1e-9 else np.full(B, -np.inf) for l in CL], 1)
pmax = float(np.mean(np.nanmax(np.where(np.isfinite(TS), TS, -np.inf), 1) >= T.max()))
print('\nMAX-STATISTIC (bootstrap de dias centrado, 16 celdas): T_max %.2f en %s ; p_max = %.4f' % (T.max(), CL[int(T.argmax())], pmax))

# placebo: reasignar el desenlace a cada relleno con el de una elegible aleatoria del mismo estrato (moneda x dia x bucket de bb)
order = np.argsort(strat, kind='stable'); W = gw[order]
cnt = np.bincount(strat, minlength=strat.max() + 1); start = np.concatenate(([0], np.cumsum(cnt)[:-1]))
rp = np.random.default_rng(SEED + 1); EVB = {}
for l in CL + OPT:
    c = CE[l]; f = np.where(c['f'])[0]
    if len(f) == 0: continue
    st_i = strat[f]; sh_i = c['s'][f]; den = sh_i.sum()
    pos = start[st_i][None, :] + (rp.random((BP, len(f)), dtype=np.float32) * cnt[st_i][None, :]).astype(np.int64)
    EVB[l] = ((W[pos] * sh_i[None, :]).sum(1) - c['c'][f].sum() + c['reb'][f].sum()) / den
Zo = {}; ZS = []
for l in CL:
    if l not in EVB: continue
    mu, sd = EVB[l].mean(), max(EVB[l].std(), 1e-12); Zo[l] = (rows[l]['ev'] - mu) / sd; ZS.append((EVB[l] - mu) / sd)
pplac_max = float(np.mean(np.max(np.stack(ZS, 1), 1) >= max(Zo.values()))) if Zo else float('nan')
pplac = {l: float(np.mean(EVB[l] >= rows[l]['ev'])) for l in EVB}
print('PLACEBO de relleno (desenlace permutado dentro de estrato): max-statistic p_plac = %.4f ; p por celda: %s' % (
    pplac_max, ' '.join('%s:%.3f' % (l, pplac[l]) for l in CL if l in pplac)))

# compuertas frente a U (mismo delta) y control de inversion
print('\n== COMPUERTAS: EV/acc(g) - EV/acc(U) en el mismo delta [IC90 dias]')
GD = {}
for g in ['G10', 'G5', 'GP5', 'I5']:
    for d, _ in DELTAS:
        a, u = rows[g + '_' + d], rows['U_' + d]
        db = boot(CE[g + '_' + d]['pnl_d'], CE[g + '_' + d]['sh_d']) - boot(CE['U_' + d]['pnl_d'], CE['U_' + d]['sh_d'])
        dm = a['ev'] - u['ev']; lo, hi = np.nanpercentile(db, [5, 95]) if np.isfinite(db).any() else (float('nan'),) * 2
        GD[g + '_' + d] = (dm, lo, hi)
        print('%-7s dEV %+.4f [%+.4f,%+.4f] rellenos %d vs %d' % (g + '_' + d, dm, lo, hi, a['nf'], u['nf']))

# criterios
def crit(l):
    r = rows[l]; c = {}
    c['c1 EV>=0.02'] = r['ev'] >= 0.02; c['c2 n>=750'] = r['nf'] >= 750; c['c3 dias>=10'] = r['ndias'] >= 10
    c['c4 IC90>0'] = r['lo'] > 0; c['c5 sin2>0'] = r['ev2'] > 0; c['c6 pmax<.05'] = pmax < 0.05
    c['c7 pplac<.05'] = pplac_max < 0.05; c['c8 IS&OOS>0'] = r['ev_is'] > 0 and r['ev_oos'] > 0
    g = l.split('_')[0]
    if g in ('G10', 'G5', 'GP5'):
        d = l.split('_')[1]; c['c9 gate>U e inv<U'] = GD[l][1] > 0 and GD['I5_' + d][0] < 0
    return c
print('\n== CRITERIOS (CANDIDATE = todos) ==')
cands = []
for l in CL:
    c = crit(l); allok = all(c.values()); soft = c['c4 IC90>0'] and c['c5 sin2>0'] and c['c8 IS&OOS>0']
    v = 'CANDIDATE' if allok else ('EXPLORATORY' if soft else 'REJECTED')
    if allok: cands.append(l)
    print('%-7s %-11s fallan: %s' % (l, v, ','.join(k.split()[0] for k, x in c.items() if not x) or '-'))
print('VEREDICTO GLOBAL:', 'CANDIDATE en ' + ','.join(cands) if cands else 'REJECTED (ninguna celda cumple todos los criterios)')
print('\n== COTAS OPTIMISTAS (cola 0) vs ESTRICTAS; regla del logger L2 ==')
need = False
for o, s in (('O_z0', 'U_z0'), ('O_m1', 'U_m1'), ('O_m2', 'U_m2')):
    ro, rs = rows[o], rows[s]; up = ro['ev'] >= 0.02 and ro['lo'] > 0; dn = not (rs['ev'] >= 0.02 and rs['lo'] > 0)
    need = need or (up and dn)
    print('%s EV %+.4f [%+.4f,%+.4f] n=%d | estricta %s EV %+.4f n=%d | cota supera umbral: %s' % (o, ro['ev'], ro['lo'], ro['hi'], ro['nf'], s, rs['ev'], rs['nf'], up))
print('LOGGER L2 NECESARIO (cota optimista supera +0.02 con IC90>0 y la estricta no):', need)

# curva lambda, k_eff, x* = R - 1/k sobre U
dep = np.array([0, 1, 2, 3.0]); lam = np.array([rows['U_' + d]['lam'] for d, _ in DELTAS]); evf = np.array([rows['U_' + d]['ev'] for d, _ in DELTAS])
if (lam > 0).all() and np.isfinite(evf).all():
    kef = -np.polyfit(dep, np.log(lam), 1)[0]; e1, e0 = np.polyfit(dep, evf, 1)
    print('\nCURVA U: lambda por profundidad (0..3 c bajo +0.01):', np.round(lam, 4), 'k_eff por centimo %.3f (1/k = %.2f c) ; EV|relleno(d)=%.4f%+.4f*d (c) ' % (kef, 1 / kef if kef > 0 else float('nan'), e0, e1))
    if e1 > 0: print('   d_R (EV|relleno=0) = %.2f c ; d* = d_R + 1/k = %.2f c' % (-e0 / e1, -e0 / e1 + 1 / kef))
    else: print('   EV|relleno no crece con la profundidad (pendiente %+.4f/c): solucion de esquina, no cotizar con ventaja' % e1)
    print('   argmax EV/elegible:', DELTAS[int(np.argmax([rows['U_' + d]['evplace'] for d, _ in DELTAS]))][0], [round(rows['U_' + d]['evplace'], 4) for d, _ in DELTAS])

# desagregado moneda x bucket para U_p1 y la mejor celda candidata con n>=750
best = max([l for l in CL if rows[l]['nf'] >= 750], key=lambda l: rows[l]['ev'], default=None)
for l in ['U_p1'] + ([best] if best and best != 'U_p1' else []):
    c = CE[l]; print('\n== %s por moneda x bucket de bb (n rellenos / EV/acc / EUR) ==' % l)
    for ci, cn in enumerate(coins):
        out = []
        for b in range(4):
            m = (cid == ci) & (bucket == b) & c['f']
            out.append('b%d %4d %+.3f %+6.1f' % (b + 1, m.sum(), c['pnl'][m].sum() / c['s'][m].sum() if m.sum() else float('nan'), c['pnl'][m].sum()))
        m = (cid == ci) & c['f']
        print('%-4s %s | total %4d %+.3f' % (cn, ' | '.join(out), m.sum(), c['pnl'][m].sum() / c['s'][m].sum() if m.sum() else float('nan')))
print('FIN_ANALISIS2')
