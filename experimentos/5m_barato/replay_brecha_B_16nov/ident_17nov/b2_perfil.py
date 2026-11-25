#!/usr/bin/env python3
"""b2_perfil.py (ident_17nov, Tarea B) -- SOLO LECTURA. Perfil de las wallets tomadoras (b1_ordenes.pkl + alineado ms B_al_D.pkl) y clasificacion de los
FN SOLO (89) y SOLO_ARRIBA (25) de fn_16nov/tomadores.pkl. El LIMITE del tomador NO es observable on-chain (el OrderFilled da lo casado, no lo firmado):
se usan proxies: niveles y profundidad del barrido en el tx, resto en reposo (limite revelado), posicion de la 1a pata frente al tope ms visto,
tamano frente al tamano del tope, edad del tope y si el tope nacio de una CAIDA (firma de cazar cotizacion rancia). Perfil SIN las ordenes que casan con B.
Salida: B_perfil.json, B_wallets.csv, B_eventos.csv."""
import os, glob, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
OD = pd.read_pickle(H + 'b1_ordenes.pkl')
AL = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'B_al_*.pkl'))], ignore_index=True) if glob.glob(H + 'B_al_*.pkl') else pd.DataFrame(columns=['tx', 'wallet', 'al'])
OD = OD.merge(AL, on=['tx', 'wallet'], how='left')
TK = pd.read_pickle(H + '../fn_16nov/tomadores.pkl')
EV = TK[(TK.cls == 'FN') & TK.estructura.isin(['SOLO', 'SOLO_ARRIBA'])].copy()
NMIN = 20
def perfil(g):
    a = g[g.al == 'ok']
    r = dict(n_ordenes=int(len(g)), dias=int(g.dia.nunique()), ordenes_dia=round(len(g) / max(1, g.dia.nunique()), 1),
             frac_multinivel=round(float((g.n_niveles >= 2).mean()), 3), prof_c_p50=float(g.prof_c.median()), prof_c_p90=float(g.prof_c.quantile(.9)),
             frac_prof_ge1c=round(float((g.prof_c >= 0.99).mean()), 3), frac_mint=round(float(g.mint.mean()), 3), frac_vende=round(float(g.vende.mean()), 3),
             frac_resto_reposo=round(float(g.resto_reposo.mean()), 3), sh_p50=float(g.sh.median()),
             n_alineadas=int(len(a)), cobertura_al=round(len(a) / max(1, len(g)), 3))
    if len(a) >= 5:
        r.update(frac_1apata_en_tope=round(float((a.mejor_vs_top_c.abs() <= 0.5).mean()), 3), frac_1apata_peor_tope=round(float((a.mejor_vs_top_c > 0.5).mean()), 3),
                 frac_lift_exacto=round(float(((a.sh_vs_topsz - 1).abs() <= 0.002).mean()), 3), sh_vs_topsz_p50=round(float(a.sh_vs_topsz.median()), 3),
                 frac_top_por_caida=round(float(a.top_por_caida.mean()), 3), frac_caida_edad_le500=round(float((a.top_por_caida & (a.edad_top_ms <= 500)).mean()), 3),
                 edad_top_p50_ms=float(a.edad_top_ms.median()), d_bloque_p50_ms=float(a.d_bloque_ms.median()))
    return r
NB = OD[~OD.con_B]
W = {w: perfil(g) for w, g in NB.groupby('wallet')}
pd.DataFrame(W).T.to_csv(H + 'B_wallets.csv')
# eventos propios (los 114) con su alineado: la orden tomadora que nos casa (con_B, mismo tx)
own = OD[OD.con_B][['tx', 'wallet', 'n_niveles', 'prof_c', 'resto_reposo', 'rest_ts', 'al', 'top', 'top_sz', 'edad_top_ms', 'top_por_caida', 'mejor_vs_top_c', 'sh_vs_topsz']]
EV = EV.merge(own, left_on=['tx', 'tk_addr'], right_on=['tx', 'wallet'], how='left')
def clase(r):
    p = W.get(r.tk_addr)
    if isinstance(r.resto_reposo, (bool, np.bool_)) and r.resto_reposo: return 'C1_limite_revelado'
    if r.desp_debajo > 0: return 'C2_sigue_debajo_5s'
    if p is None or p['n_ordenes'] < NMIN: return 'C6_sin_historial'
    if p['frac_multinivel'] >= 0.5 or p['frac_prof_ge1c'] >= 0.5: return 'C3_barredor'
    if p.get('frac_caida_edad_le500', 0) >= 0.5: return 'C4_caza_tope_recien_caido'
    if p.get('frac_lift_exacto', 0) >= 0.5 and p['frac_multinivel'] <= 0.2: return 'C5_levanta_nivel_exacto'
    return 'C7_mixto'
EV['clase'] = EV.apply(clase, axis=1)
EV['wallet_n'] = EV.tk_addr.map(lambda w: W.get(w, {}).get('n_ordenes', 0))
EV[['oid', 'dia', 'coin', 'L', 'estructura', 'tk_addr', 'wallet_n', 'clase', 'desp_debajo', 'parcial', 'taker_sh', 'own_sh_tx', 'n_niveles', 'prof_c', 'resto_reposo',
    'al', 'edad_top_ms', 'top_por_caida', 'mejor_vs_top_c', 'sh_vs_topsz', 'gana', 'p_r', 'c_r']].to_csv(H + 'B_eventos.csv', index=False)
res = dict(ordenes_tomadoras=int(len(OD)), sin_B=int(len(NB)), wallets=int(OD.wallet.nunique()), dias=sorted(OD.dia.unique().tolist()),
           cobertura_alineado=round(float((OD.al == 'ok').mean()), 3) if 'al' in OD else None, motivos_no_alineado=OD.al.value_counts(dropna=False).to_dict())
for est, g in EV.groupby('estructura'):
    a = g[g.al == 'ok']
    res[est] = dict(n=len(g), wallets=int(g.tk_addr.nunique()), clases=g.clase.value_counts().to_dict(),
                    taker_sh_igual_nuestro=int(((g.taker_sh - g.own_sh_tx).abs() < 1e-6).sum()), parciales=int(g.parcial.sum()),
                    alineados=int(len(a)), edad_top_p50_ms=(float(a.edad_top_ms.median()) if len(a) else None),
                    frac_top_por_caida=(round(float(a.top_por_caida.mean()), 3) if len(a) else None),
                    frac_caida_le500=(round(float((a.top_por_caida & (a.edad_top_ms <= 500)).mean()), 3) if len(a) else None),
                    EV_por_clase={c: dict(n=len(h), ev=(round(float(h.p_r.sum() / h.c_r.sum()), 4) if h.c_r.sum() > 0 else None)) for c, h in g.groupby('clase')})
# perfil agregado de las wallets de SOLO/SOLO_ARRIBA (ponderado por evento) vs el resto de tomadoras de B
def agg(ws, peso):
    P = pd.DataFrame({w: W[w] for w in ws if w in W}).T
    if not len(P): return None
    wts = np.array([peso.get(w, 1) for w in P.index], float)
    return {c: round(float(np.average(P[c].astype(float).fillna(np.nan).dropna(), weights=wts[P[c].astype(float).notna().values])), 3) for c in P.columns if P[c].astype(float).notna().any()}
pe = EV.tk_addr.value_counts().to_dict()
res['perfil_wallets_SOLO_y_ARRIBA_ponderado_evento'] = agg(set(EV.tk_addr), pe)
otras = set(TK.tk_addr) - set(EV.tk_addr); res['perfil_otras_tomadoras_B'] = agg(otras, {})
res['top_wallets'] = {w: dict(eventos=int(n), **W.get(w, {})) for w, n in EV.tk_addr.value_counts().head(8).items()}
json.dump(res, open(H + 'B_perfil.json', 'w'), indent=1, default=str); print(json.dumps(res, indent=1, default=str)[:12000])
