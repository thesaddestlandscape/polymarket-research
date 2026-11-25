#!/usr/bin/env python3
"""E7 (ADDENDUM1 (c)): Calma-T1 con sello v3, POSTPROCESO de solo lectura sobre los dec2v3_D.pkl del juez (calma_v3/recalc_13nov/out, producidos por esc_dec2_v3.py = esc_dec2.py de dev ejecutado SIN editar con el sello `stamp_v3`);
NO toca dev, el motor sellado ni v3/. Verifica el sello (hash de stamp_v3.py y de su copia en huecos_fix_13nov, `sello_print` de los manifiestos, diferencia de tf frente al dec2 viejo). Calcula T1-G0 en EUR (IC90 por dias y por cierre, bootstrap 3000 como ana_dec.py),
dias+, sin 2 mejores, EV absoluto con IC90 por dias, T1-PLA_T1, desglose por epoca (tf) y hole60 (pkl de huecos_fix_13nov si el sello verifica por hash; si no, DATA_BLOCKED).
Criterios de etiqueta FIJADOS antes de ejecutar (los pedidos por Javi): VALIDADA-mitigacion = >=10 dias, IC90 dias inf>0, dias+ >= 80 %, sin 2 mejores > 0, T1-PLA_T1 IC90 dias inf>0; si no EXPLORATORIA/INSUFFICIENT.
EV absoluto contra el criterio literal PREREG_CALMA_T1 (REFUTA si EV(T1)<=0 con >=10 dias): se reporta SIN cerrar la puerta."""
import os, sys, glob, re, hashlib; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib1 import *
CV = L2 + 'calma_v3/'; JD = CV + 'recalc_13nov/out/'; DEVO = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/'; HF = CV + 'huecos_fix_13nov/'
sh = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]
txt = [f'# E7 Calma-T1 con sello v3 (postproceso solo lectura; ADDENDUM1 sha {ADD_SHA[:8]})']
# ---------------- verificacion del sello v3
src = open(CV + 'esc_dec2_v3.py').read(); assert 'import stamp_v3 as ST' in src and 'ST.stamp_events' in src and "'dec2v3'" in src, 'esc_dec2_v3 no usa stamp_v3'
txt.append(f'Sello: esc_dec2_v3.py importa stamp_v3 (ST.stamp_events) y etiqueta dec2v3 | sha stamp_v3.py {sh(L2 + "stamp_v3.py")} | copia huecos_fix_13nov/stamp_v3.py {sh(HF + "stamp_v3.py") if os.path.exists(HF + "stamp_v3.py") else "AUSENTE"}')
mf = {}
for p in sorted(glob.glob(JD + 'manifest_juez_v3_*.json')):
    m = json.load(open(p)); mf[m['dia']] = (m.get('sello_print'), m.get('estado'))
txt.append(f'Manifiestos del juez: {len(mf)} dias, sello_print distintos {sorted(set(v[0] for v in mf.values()))}, estados {sorted(set(v[1] for v in mf.values()))} (dias {min(mf)}..{max(mf)})')
def carga(prefijo, dirs, d0='2026-10-26', d1='2026-11-14'):
    out = []
    for f in sorted(glob.glob(dirs + prefijo + '_*.pkl')):
        d = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(f)).group(1)
        if d0 <= d <= d1: out.append(pd.read_pickle(f))
    return pd.concat(out, ignore_index=True)
V3 = carga('dec2v3', JD); OLD = carga('dec2', DEVO); V3 = V3[V3.act.isin(['SOL', 'XRP', 'ETH'])]; OLD = OLD[OLD.act.isin(['SOL', 'XRP', 'ETH'])]
dias3 = sorted(V3.dia.unique()); txt.append(f'dec2v3: {len(dias3)} dias {dias3[0]}..{dias3[-1]}, {len(V3)} filas, variantes {sorted(V3["var"].unique())}')
# diferencia de tf (v3 vs viejo) para G0 (misma clave dia,mkt,lado,L,k): prueba de que los pkl son del sello nuevo
kk = ['dia', 'mkt', 'lado', 'L', 'k']; a = V3[V3['var'] == 'G0'][kk + ['tf']].drop_duplicates(kk); b = OLD[OLD['var'] == 'G0'][kk + ['tf']].drop_duplicates(kk); mm = a.merge(b, on=kk, suffixes=('_v3', '_old'))
dtf = (mm.tf_v3 - mm.tf_old).values; txt.append(f'G0: {len(mm)} fills comunes viejo/v3; tf_v3 - tf_viejo p5/p50/p95 = {np.percentile(dtf, [5, 50, 95]).round(0).tolist()} ms; distintos en {100*np.mean(dtf != 0):.1f} % (si fuese 0 %, el pkl NO tendria sello nuevo)')
assert np.mean(dtf != 0) > 0.5, 'los dec2v3 no difieren del sello viejo: no son v3'
rng = np.random.default_rng(20261115)
def pairs(X, Y, key, B=3000):
    """Suma de diferencias emparejadas X-Y por clave (dia o cierre) con bootstrap por clave; devuelve (suma, ic90, vector por clave)."""
    x = X.groupby(key).pnl.sum(); y = Y.groupby(key).pnl.sum(); dd = x.sub(y, fill_value=0.0); v = dd.values
    bs = np.array([v[rng.integers(0, len(v), len(v))].sum() for _ in range(B)]) if len(v) >= 3 else np.full(B, np.nan); return float(v.sum()), (float(np.nanpercentile(bs, 5)), float(np.nanpercentile(bs, 95))), dd
def tabla(R, nombre, var_ref='G0', variantes=('T1', 'T05', 'T1_ambos', 'PLA_T1')):
    L = [f'## {nombre}  (dias {R.dia.nunique()}, filas {len(R)})']; o = {}; G = R[R['var'] == var_ref]
    for v in variantes:
        X = R[R['var'] == v]
        if len(X) == 0: continue
        s_d, ic_d, dd = pairs(X, G, 'dia'); s_c, ic_c, _ = pairs(X, G, 'fin'); s2 = float(dd.sort_values(ascending=False).iloc[2:].sum()); evd = X.groupby('dia').apply(lambda d: d.pnl.sum() / d.cost.sum(), include_groups=False)
        lo, p, mu = t_ic(evd.values); o[v] = dict(n=int(len(X)), EUR=float(X.pnl.sum()), cost=float(X.cost.sum()), EV=float(X.pnl.sum() / X.cost.sum()), dEUR=s_d, ic90_dias=ic_d, ic90_cierre=ic_c, dias_pos=int((dd > 0).sum()), n_dias=int(len(dd)), sin2mejores=s2,
                                          EV_dia_medio=float(mu), EV_dia_ic90_inf=float(lo), EV_G0=float(G.pnl.sum() / G.cost.sum()))
        L.append(f"{v}: rellenos {len(X)} | EUR {X.pnl.sum():+.1f} | EV pond. {o[v]['EV']:+.3f} (G0 {o[v]['EV_G0']:+.3f}) | dEUR vs G0 {s_d:+.1f} IC90 dias ({ic_d[0]:+.1f},{ic_d[1]:+.1f}) IC90 cierre ({ic_c[0]:+.1f},{ic_c[1]:+.1f}) | dias+ {o[v]['dias_pos']}/{o[v]['n_dias']} | sin 2 mejores {s2:+.1f} | EV medio diario {mu:+.3f} IC90 inf {lo:+.3f}")
    if 'T1' in o and 'PLA_T1' in o:
        s, ic, dd = pairs(R[R['var'] == 'T1'], R[R['var'] == 'PLA_T1'], 'dia'); o['T1_menos_PLA'] = dict(dEUR=s, ic90_dias=ic, dias_pos=int((dd > 0).sum()), n_dias=int(len(dd)), sin2mejores=float(dd.sort_values(ascending=False).iloc[2:].sum()))
        L.append(f"T1 - PLA_T1 (merito de la senal): {s:+.1f} EUR IC90 dias ({ic[0]:+.1f},{ic[1]:+.1f}) | dias+ {o['T1_menos_PLA']['dias_pos']}/{o['T1_menos_PLA']['n_dias']} | sin 2 mejores {o['T1_menos_PLA']['sin2mejores']:+.1f}")
    return L, o
X12 = V3[(V3.dia >= '2026-11-02') & (V3.dia <= '2026-11-12')]; G12 = X12[X12['var'] == 'G0']; T12 = X12[X12['var'] == 'T1']; P12 = X12[X12['var'] == 'PLA_T1']; s12, ic12, dd12 = pairs(T12, G12, 'dia'); sp12, icp12, _ = pairs(T12, P12, 'dia')
txt.append(f"Chequeo contra lo documentado (02..12-Nov, {X12.dia.nunique()} dias; memoria 13-Nov: T1-G0 +351,5 EUR IC90 (129;556) 9/11 dias+, EV abs T1 -0,073 / G0 -0,185, PLA_T1 +161 EUR, merito ~+190): T1-G0 = {s12:+.1f} EUR IC90 dias ({ic12[0]:+.1f},{ic12[1]:+.1f}) {int((dd12 > 0).sum())}/{len(dd12)} dias+ | EV abs T1 {T12.pnl.sum() / T12.cost.sum():+.3f} / G0 {G12.pnl.sum() / G12.cost.sum():+.3f} | T1-PLA_T1 {sp12:+.1f}")
RES = {}; ep = epoca(V3.tf.values); V3 = V3.assign(epoca=ep); eo = epoca(OLD.tf.values); OLD = OLD.assign(epoca=eo)
txt.append('Reparto de fills por epoca (tf): ' + str(V3[V3['var'] == 'G0'].epoca.value_counts().to_dict()))
# chequeo cruzado con los datos sueltos del coordinador (EV diario con sello v3, dias 13 y 14-Nov): T1 -0,634/G0 -0,637 (13) y T1 -0,221/G0 -0,378 (14)
chk = {}
for d, (t1, g0) in {'2026-11-13': (-0.634, -0.637), '2026-11-14': (-0.221, -0.378)}.items():
    X = V3[V3.dia == d]
    if len(X): e1 = X[X['var'] == 'T1'].pnl.sum() / X[X['var'] == 'T1'].cost.sum(); e0 = X[X['var'] == 'G0'].pnl.sum() / X[X['var'] == 'G0'].cost.sum(); chk[d] = (round(e1, 3), round(e0, 3), (t1, g0))
txt.append(f'Chequeo con datos sueltos del coordinador (EV diario T1/G0 recalculado vs citado): {chk}')
for nombre, R, Ro in (('FORWARD 02-Nov..14-Nov (R2)', V3[(V3.dia >= '2026-11-02')], OLD[(OLD.dia >= '2026-11-02')]), ('TODO 26-Oct..14-Nov', V3, OLD), ('R2 por timestamp de fill (tf >= 27-Oct 11:47Z)', V3[V3.epoca == 'R2'], OLD[OLD.epoca == 'R2']), ('R1 por timestamp de fill (26-27 Oct antes de 11:47Z)', V3[V3.epoca == 'R1'], OLD[OLD.epoca == 'R1'])):
    L, o = tabla(R, nombre + ' -- SELLO v3'); txt += [''] + L; RES[nombre] = o
    if nombre.startswith('FORWARD') or nombre.startswith('TODO'):
        L2_, o2 = tabla(Ro, nombre + ' -- sello VIEJO (NO VALIDADO, solo comparacion)', variantes=('T1', 'PLA_T1')); txt += L2_; RES[nombre + ' VIEJO'] = o2
# hole60: pkl de huecos_fix_13nov (misma cadena con la correccion de huecos) si el stamp verifica por hash
H60 = sorted(glob.glob(HF + 'out/hole60_dec2v3_2026-*.pkl')); same = os.path.exists(HF + 'stamp_v3.py') and sh(HF + 'stamp_v3.py') == sh(L2 + 'stamp_v3.py')
txt += ['', f'## hole60 (excluir solo hueco +-60 s): {len(H60)} pkl; stamp_v3 copia == original por hash: {same}']
if H60 and same:
    Rh = pd.concat([pd.read_pickle(f) for f in H60], ignore_index=True); Rh = Rh[Rh.act.isin(['SOL', 'XRP', 'ETH'])]; L, o = tabla(Rh, f'hole60 -- SELLO v3 (stamp_v3 verificado por hash), dias {sorted(Rh.dia.unique())}'); txt += L; RES['hole60'] = o
else: txt.append('DATA_BLOCKED: no se puede validar hole60 con sello v3 (sin pkl o stamp_v3 distinto); NO se usa el sello viejo.')
# ---------------- criterios LITERALES del PREREG_CALMA_T1 (dev .../descomp/PREREG_CALMA_T1.md): CONFIRMA si >=10 dias con EV(T1)>0, dEUR IC90 dias y cierre >0, EV(T1)>EV(PLA_T1) en >=2/3 de los dias, sin 2 mejores >0; REFUTA si EV(T1)<=0 o EV(T1)<=EV(PLA_T1) con >=10 dias
def evdia(R, v): X = R[R['var'] == v]; return X.groupby('dia').apply(lambda d: d.pnl.sum() / d.cost.sum(), include_groups=False)
LIT = {}
for nombre, R in (('main 02..14-Nov', V3[V3.dia >= '2026-11-02']), ('hole60 02..12-Nov', Rh if (H60 and same) else None)):
    if R is None: continue
    e1_, ep_ = evdia(R, 'T1'), evdia(R, 'PLA_T1'); both = e1_.index.intersection(ep_.index); fr = float((e1_[both] > ep_[both]).mean()); X3 = R[R['var'] == 'T1_c300']; ev300 = float(X3.pnl.sum() / X3.cost.sum()) if len(X3) else np.nan; evT1 = float(R[R['var'] == 'T1'].pnl.sum() / R[R['var'] == 'T1'].cost.sum()); evPL = float(R[R['var'] == 'PLA_T1'].pnl.sum() / R[R['var'] == 'PLA_T1'].cost.sum())
    LIT[nombre] = dict(n_dias=int(len(both)), EV_T1=evT1, EV_PLA=evPL, frac_dias_T1_mayor_PLA=fr, EV_T1_c300=ev300, veredicto_literal=('REFUTA (EV(T1) <= 0)' if evT1 <= 0 else ('REFUTA (EV(T1) <= EV(PLA_T1))' if evT1 <= evPL else ('CONFIRMA-candidato' if fr >= 2 / 3 else 'INSUFFICIENT'))))
    txt.append(f"PREREG_CALMA_T1 literal [{nombre}]: {len(both)} dias | EV(T1) {evT1:+.3f}, EV(PLA_T1) {evPL:+.3f}, EV(T1)>EV(PLA) en {100*fr:.0f} % de los dias (>= 67 % requerido), T1_c300 EV {ev300:+.3f} (si <= 0 la latencia <= 100 ms es obligatoria) -> {LIT[nombre]['veredicto_literal']}  [no se cierra la puerta: ver ETIQUETAS]")
RES['literal_prereg'] = LIT
# ---------------- etiquetas
F = RES['FORWARD 02-Nov..14-Nov (R2)']; T1 = F['T1']; P = F.get('T1_menos_PLA', {})
ok = (T1['n_dias'] >= 10 and T1['ic90_dias'][0] > 0 and T1['dias_pos'] / T1['n_dias'] >= 0.8 and T1['sin2mejores'] > 0 and P and P['ic90_dias'][0] > 0)
lab_mit = 'CUMPLE los criterios con sello v3 (R2 forward; falta validacion independiente)' if ok else 'EXPLORATORIA'
lab_abs = 'REFUTA segun PREREG_CALMA_T1 literal (EV(T1)<=0 con >=10 dias); la puerta NO se cierra (analisis de por que T1 no neutraliza la AS: horas recuperadas/rotacion 4 h)' if (T1['EV'] <= 0 and T1['n_dias'] >= 10) else 'EV absoluto > 0'
txt += ['', f'ETIQUETAS (forward R2, {T1["n_dias"]} dias): valor de mitigacion T1-G0 = {lab_mit} [dEUR {T1["dEUR"]:+.1f}, IC90 dias ({T1["ic90_dias"][0]:+.1f},{T1["ic90_dias"][1]:+.1f}), dias+ {T1["dias_pos"]}/{T1["n_dias"]}, sin 2 mejores {T1["sin2mejores"]:+.1f}, T1-PLA {P.get("dEUR", float("nan")):+.1f} IC90 ({P.get("ic90_dias", (np.nan, np.nan))[0]:+.1f},{P.get("ic90_dias", (np.nan, np.nan))[1]:+.1f})];',
        f'EV absoluto T1 = {T1["EV"]:+.3f} (G0 {T1["EV_G0"]:+.3f}) -> {lab_abs}. Limites: engine legacy (reloj EX) sin dedupe; 13-14 Nov recalculados por el juez; dias con hueco libro5_tx (hole60 aparte).']
write(EXP + 'E7_calma.txt', txt); json.dump(RES, open(EXP + 'E7_calma.json', 'w'), default=float, indent=1); estado_fase('E7', 'COMPLETE', dias=len(dias3), etiqueta_mitigacion=lab_mit); print('\n'.join(txt))
