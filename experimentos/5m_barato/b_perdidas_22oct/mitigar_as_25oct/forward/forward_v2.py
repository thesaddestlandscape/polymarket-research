#!/usr/bin/env python3
"""forward_v2.py (04-Nov) — juez de PREREG_FWD_V2.md (sha en PREREG_FWD_V2.sha256). Lee prints_D.pkl de forward_a1 (solo lectura). Solo días >= --desde (def. 2026-11-04) con
cobertura desenlace>=0,995 y F5_valido>=0,98. Escribe RESUMEN_V2.md. Telegram diario (latch por día). --desde 2026-10-24 = ensayo sobre la derivación (NO es veredicto)."""
import glob, hashlib, json, os, subprocess, sys
import numpy as np, pandas as pd
from scipy import stats
AQ = os.path.dirname(os.path.abspath(__file__)); DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/forward/'
assert hashlib.sha256(open(AQ + '/PREREG_FWD_V2.md', 'rb').read()).hexdigest() == open(AQ + '/PREREG_FWD_V2.sha256').read().split()[0], 'prereg V2 alterado'
C0, C1 = 3.526360511779785, 4.717426776885986
F2E = np.array(json.load(open(AQ + '/regla_congelada.json'))['F2_deciles_train'])  # idéntico a forward_a1 (que ejecuta main al importar)
def cell_f2(F2): return np.where(np.isfinite(F2), np.searchsorted(F2E, np.nan_to_num(F2), 'right'), -1)  # copia literal de forward_a1.cell_f2
desde = sys.argv[sys.argv.index('--desde') + 1] if '--desde' in sys.argv else '2026-11-04'
ensayo = desde < '2026-11-04'
def t_ic(x):
    x = np.asarray(x, float); n = len(x)
    if n < 3: return np.nan, np.nan, np.nan
    se = x.std(ddof=1) / np.sqrt(n); t = x.mean() / se if se > 0 else np.nan
    return x.mean() - stats.t.ppf(0.95, n - 1) * se, stats.t.sf(t, n - 1), x.mean()
def main():
    dias, malos, filas, cier = [], [], [], []
    for p in sorted(glob.glob(DL + 'prints_2026-*.pkl')):
        d = os.path.basename(p)[7:17]
        if d < desde: continue
        try: man = json.load(open(DL + f'manifest_{d}.json')); c = man['cobertura']
        except Exception: malos.append((d, 'sin manifiesto')); continue
        if man.get('estado') != 'COMPLETE' or c['cobertura_desenlace_coste'] < 0.995 or c['F5_valido'] < 0.98: malos.append((d, f"cob {c.get('cobertura_desenlace_coste')} F5 {c.get('F5_valido')}")); continue
        F = pd.read_pickle(p)[['coin', 'F5', 'F2', 'hora', 'pnl', 'coste', 'fin']]; G = F[F.coin.isin(('ETH', 'SOL', 'XRP'))]
        f5, pn, co = G.F5.values, G.pnl.values, G.coste.values; ok = np.isfinite(f5)
        ter = {'bajo': ok & (f5 <= C0), 'medio': ok & (f5 > C0) & (f5 <= C1), 'alto': ok & (f5 > C1)}
        r = dict(dia=d)
        for t, m in ter.items():
            fd = co[m].sum() / co.sum(); r['exc_' + t] = fd * pn.sum() - pn[m].sum(); r['pnl_' + t] = pn[m].sum(); r['co_' + t] = co[m].sum()
        cell = pd.Series(cell_f2(G.F2.values).astype(str)) + '|' + pd.Series(G.coin.values) + '|' + pd.Series(G.hora.values.astype(str))  # RT = base F2xmonedaxhora (forward_a1)
        es = 0.0
        for _, gg in pd.DataFrame({'c': cell.values, 'pnl': pn, 'co': co, 'm': ter['alto']}).groupby('c'):
            cs = gg.co.sum()
            if cs > 0: es += gg.co[gg.m].sum() / cs * gg.pnl.sum() - gg.pnl[gg.m].sum()
        r['exc_rt'] = es
        fd = co[ter['alto']].sum() / co.sum(); e = pd.DataFrame({'fin': G.fin.values, 'e': fd * pn - np.where(ter['alto'], pn, 0)}).groupby('fin').e.sum()
        cier += [(d, k, v) for k, v in e.items()]; filas.append(r); dias.append(d)
    R = pd.DataFrame(filas); n = len(R)
    L = [f"# RESUMEN FWD-V2 ({'ENSAYO SOBRE DERIVACION, NO VEREDICTO' if ensayo else 'forward'}) desde {desde} — {pd.Timestamp.now("UTC"):%FT%TZ}", f"Días válidos: {n} {dias}", f"Días malos/excluidos: {malos}", ""]
    if n < 3:
        L.append('Insuficiente (<3 días).'); gate = None
    else:
        ev = {t: R['pnl_' + t].sum() / R['co_' + t].sum() for t in ('bajo', 'medio', 'alto')}
        dba = R.pnl_bajo / R.co_bajo - R.pnl_alto / R.co_alto
        ic1, p1, m1 = t_ic(R.exc_alto); sin2 = R.exc_alto.sort_values().iloc[:-2].sum()
        rng = np.random.default_rng(20261104); C = pd.DataFrame(cier, columns=['d', 'k', 'v']).groupby('k').v.sum().values
        bs = np.array([rng.choice(C, len(C)).sum() for _ in range(1000)]); icc = np.percentile(bs, 5)
        icd, _, mdd = t_ic(dba)
        icr, _, _ = t_ic(R.exc_rt)
        g = {'1_exc_alto>0 IC90 dias inf>0': bool(R.exc_alto.sum() > 0 and ic1 > 0), '2_p<0,05': bool(p1 < 0.05), '3_sin2mejores>0': bool(sin2 > 0), '4_exc_bajo<0': bool(R.exc_bajo.sum() < 0),
             '5_monotonia': bool(ev['bajo'] > ev['medio'] > ev['alto'] and (dba > 0).mean() >= 2 / 3 and icd > 0), '6_IC90 cierre inf>0': bool(icc > 0), '7_dias exc_alto>0 >=2/3': bool((R.exc_alto > 0).mean() >= 2 / 3), 'RT_base F2xmonedaxhora SumEXCESO>0 (literal del prereg)': bool(R.exc_rt.sum() > 0)}
        gate = all(g.values())
        L += [f"EV bajo/medio/alto: {ev['bajo']:+.3f} / {ev['medio']:+.3f} / {ev['alto']:+.3f}", f"exceso alto {R.exc_alto.sum():+.0f} (IC90 dias inf {ic1:+.0f}, p {p1:.4f}, sin 2 mejores {sin2:+.0f}, dias+ {(R.exc_alto>0).sum()}/{n}), exceso bajo {R.exc_bajo.sum():+.0f}",
              f"bajo-alto por dia {mdd:+.3f} (IC90 inf {icd:+.3f}; dias+ {(dba>0).sum()}/{n}); IC90 cierre exceso alto inf {icc:+.0f}", '', f"RT (base F2xmonedaxhora) exceso {R.exc_rt.sum():+.0f} (IC90 dias inf {icr:+.0f}, dias+ {(R.exc_rt>0).sum()}/{n})", '', '## Gate (incluye placebo RT)'] + [f"- {k}: {'SI' if v else 'no'}" for k, v in g.items()]
        L.append(f"**{'ENSAYO' if ensayo else ('LISTO: gate cumplido (incl. RT) si n>=10' if gate and n >= 10 else 'EN CURSO (n=%d/10 días válidos)' % n)}**")
    open(AQ + ('/RESUMEN_V2_ensayo.md' if ensayo else '/RESUMEN_V2.md'), 'w').write('\n'.join(L)); print('\n'.join(L))
    if not ensayo and '--no-telegram' not in sys.argv:
        lat = DL + 'v2_latch.json'; hoy = pd.Timestamp.now("UTC").strftime('%F')
        if (json.load(open(lat)) if os.path.exists(lat) else {}).get('d') != hoy:
            msg = f"F5-V2 forward: {n}/10 días válidos. " + (L[4] if n >= 3 else 'sin datos aún') + ((' | ' + L[5]) if n >= 3 else '')
            r = subprocess.run(['/usr/bin/python3', '-c', "import sys; sys.path.insert(0,'/root/polymarket-research'); from shadow_digest import enviar_telegram as e; e(sys.argv[1])", msg[:900]], capture_output=True)
            if r.returncode == 0: json.dump({'d': hoy}, open(lat, 'w'))
main()
