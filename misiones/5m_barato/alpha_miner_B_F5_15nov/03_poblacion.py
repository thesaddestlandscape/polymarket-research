#!/usr/bin/env python3
"""Paso 3 (PREREG_B_F5): poblacion (prints_D forward 24-Oct..14-Nov; r_D/l_D 06-23 Oct). EV por tercil de F5 a lag 100/250 ms, todo vs 'tipo B' (q <= bid-0,01), reglas G1/G2/inv; IC90 por dias, por cierre, placebo (dia x moneda x hora), sin 2 mejores dias."""
import os, sys, json, glob, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from lib_ev import *
AQ = os.path.dirname(os.path.abspath(__file__)); DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'; FW = DL + 'forward/'
COLS = ['dia', 'coin', 'hora', 'fin', 'q', 'pnl', 'coste', 'F5', 'bid', 'F5_250', 'bid_250']
def carga_fwd(d0, d1):
    out = []; malos = []
    for p in sorted(glob.glob(FW + 'prints_2026-*.pkl')):
        d = os.path.basename(p)[7:17]
        if not (d0 <= d <= d1): continue
        try: man = json.load(open(FW + f'manifest_{d}.json')); c = man['cobertura']
        except Exception: malos.append((d, 'sin manifiesto')); continue
        if man.get('estado') != 'COMPLETE' or c['cobertura_desenlace_coste'] < 0.995 or c['F5_valido'] < 0.98: malos.append((d, c.get('cobertura_desenlace_coste'), c.get('F5_valido'))); continue
        F = pd.read_pickle(p); F = F[F.coin.isin(('ETH', 'SOL', 'XRP'))][COLS].copy(); out.append(F)
    return pd.concat(out, ignore_index=True), malos
def prep(F, lag, tipoB):
    f5 = F['F5' if lag == 100 else 'F5_250'].values; bid = F['bid' if lag == 100 else 'bid_250'].values
    G = pd.DataFrame({'dia': F.dia.values, 'coin': F.coin.values, 'hora': F.hora.values, 'cl': F.fin.values, 'pnl': F.pnl.values, 'coste': F.coste.values, 'ter': ter(f5)})
    if tipoB: G = G[(np.isfinite(bid) & ((bid - F.q.values) >= 0.0099))[np.arange(len(F)) if False else slice(None)]] if False else G[np.isfinite(bid) & ((bid - F.q.values) >= 0.0099)]
    return G.reset_index(drop=True)
def bloque(G, nombre, perm=True):
    L = [f'## {nombre}  (filas {len(G)}, cierres {G.cl.nunique()}, dias {G.dia.nunique()})']; o = {}
    tot = ev(G.pnl, G.coste)
    por_dia = G.groupby('dia').apply(lambda d: pd.Series({r: ev(d.pnl[d.ter.isin(RET[r])], d.coste[d.ter.isin(RET[r])]) for r in ('todo', 'bajo', 'medio', 'alto', 'G1', 'G2', 'inv')}), include_groups=False)
    L.append('EV pond. pooled: ' + ' | '.join(f"{r} {ev(G.pnl[G.ter.isin(RET[r])], G.coste[G.ter.isin(RET[r])]):+.3f} (fracc coste {G.coste[G.ter.isin(RET[r])].sum()/G.coste.sum()*100:.0f}%)" for r in ('todo', 'bajo', 'medio', 'alto', 'nan')))
    dba = por_dia.bajo - por_dia.alto; lo, p, m = t_ic(dba); L.append(f'bajo-alto por dia {m:+.3f} (IC90 inf {lo:+.3f}; dias+ {(dba>0).sum()}/{len(dba)}); monotonia bajo>medio>alto pooled: {ev(G.pnl[G.ter=="bajo"],G.coste[G.ter=="bajo"])>ev(G.pnl[G.ter=="medio"],G.coste[G.ter=="medio"])>ev(G.pnl[G.ter=="alto"],G.coste[G.ter=="alto"])}')
    o['bajo_alto_dia'] = dict(m=m, lo=lo, pos=int((dba > 0).sum()), n=len(dba))
    PL = placebo_multi(G, ['G1', 'G2'], ['dia', 'coin', 'hora'], B=1000) if perm else {}
    for r in ('G1', 'G2', 'inv'):
        m_ = G.ter.isin(RET[r]); e = ev(G.pnl[m_], G.coste[m_]); d = por_dia[r]; lo, p, mm = t_ic(d); dd = d - por_dia.todo; lod, pd_, md = t_ic(dd)
        (a, b), (da, db) = boot_cluster(G, r, 1000)
        x = dict(ev=e, dev=e - tot, ev_dia_medio=mm, ic90_dias_inf=lo, p_dias=p, dias_pos=int((d > 0).sum()), n_dias=len(d), dev_dia_inf=lod, dev_dias_pos=int((dd > 0).sum()), ic90_cl=(a, b), dev_ic90_cl=(da, db),
                 sin2dias=sin_mejores(G, r, 'dia'), fracc=float(G.coste[m_].sum() / G.coste.sum()))
        if perm and r in ('G1', 'G2'):
            ob, pv, mu = PL[r]; x.update(placebo_dev=ob, placebo_p=pv, placebo_mu=mu)
        o[r] = x
        L.append(f"{r}: EV {e:+.3f} (DeltaEV {e-tot:+.3f}) | media diaria {mm:+.3f} IC90 dias inf {lo:+.3f} p {p:.3f} dias+ {(d>0).sum()}/{len(d)} | DeltaEV diario IC90 inf {lod:+.3f} dias+ {(dd>0).sum()}/{len(dd)} | IC90 cierre ({a:+.3f},{b:+.3f}) | sin 2 mejores dias {x['sin2dias']:+.3f}" + (f" | placebo p {x['placebo_p']:.3f} (DeltaEV obs {x['placebo_dev']:+.3f}, media perm {x['placebo_mu']:+.3f})" if 'placebo_p' in x else ''))
    o['todo'] = tot; o['por_dia'] = por_dia.round(4).reset_index().to_dict('records')
    return L, o, por_dia
res = {}; txt = []
for per, (d0, d1) in {'P_OOS 04-14Nov': ('2026-11-04', '2026-11-14'), 'P_DER 24Oct-03Nov': ('2026-10-24', '2026-11-03')}.items():
    F, malos = carga_fwd(d0, d1); txt.append(f'# {per}: dias cargados {F.dia.nunique()}; excluidos {malos}; filas ETH/SOL/XRP {len(F)}')
    for lag in (100, 250):
        for tipoB in (False, True):
            G = prep(F, lag, tipoB); nm = f"{per} | lag {lag} ms | {'tipo B (q<=bid-0,01)' if tipoB else 'todas las filas banda'}"
            L, o, pdia = bloque(G, nm); txt += L + ['por dia (EV pond.):', pdia.round(3).to_string(), '']; res[nm] = o
    del F
open(AQ + '/poblacion_por_tercil.txt', 'w').write('\n'.join(txt)); json.dump(res, open(AQ + '/poblacion_por_tercil.json', 'w'), default=float, indent=1); print('\n'.join(txt))
