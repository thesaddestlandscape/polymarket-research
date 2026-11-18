#!/usr/bin/env python3
"""checks_H.py: ejecuta sobre el FIXTURE del 12-Nov (dia de DISENO; sufijos _fxM1/_fxM2) los 25 criterios H de ADENDA_06. NO toca ningun dia de veredicto.
Uso: checks_H.py [--final]   (--final comprueba H1 y H25: hashes congelados y mtime)"""
import sys, os, json, pickle, hashlib, subprocess, shutil, re, collections, bisect, glob, gzip
import numpy as np, pandas as pd
from scipy import stats as sst
P = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); O = P + '/out'; V = O + '/verif_adenda07'
SCR = '/tmp/claude-0/-root-polymarket-research/5055698c-f1c6-493f-8e00-51095bf98a56/scratchpad'
FX = SCR + '/fx3h/fx3h.csv.gz'; FINAL = '--final' in sys.argv; RES = collections.OrderedDict()
def put(h, status, det): RES[h] = dict(estado=status, detalle=det); print(f'H{h:>2} {status}: {det}'[:400], flush=True)
def sha(f): return hashlib.sha256(open(f, 'rb').read()).hexdigest()
SUF = '_fxM1'; d1 = pickle.load(open(f'{O}/p1_btc_2026-11-12{SUF}.pkl', 'rb')); EV, PL, PW, CP = d1['EV'], d1['PL'], d1['PW'], d1['CP'][['dist_ticks', 'edad_nivel', 'edad_cens']].copy(); d1['CP'] = None; d1 = None
r7 = json.load(open(f'{O}/p7_btc_2026-11-12{SUF}.json')); p3 = json.load(open(f'{O}/p3_btc_act{SUF}_DISENO.json')) if os.path.exists(f'{O}/p3_btc_act{SUF}_DISENO.json') else None
DF = ['dist_ticks', 'SQ_mej', 'act2_mej', 'spread', 'dp_signed', 'sg', 'edad_nivel']
# ---- H1 / H25 (solo --final)
REQ = ['p1_dia.py', 'p3_agrega.py', 'p7_ipw_balance.py', 'p5_control_sin_relleno.py', 'run_p1.sh', 'ADENDA_07_18nov.md', 'ADENDA_09_18nov.md']
if FINAL:
    last = {}
    for ln in open(P + '/HASHES_CODIGO.txt'):
        p_ = ln.split()
        if len(p_) == 2 and re.fullmatch(r'[0-9a-f]{64}', p_[0]): last[p_[1]] = p_[0]
    bad = [n for n in REQ if last.get(n) != sha(f'{P}/{n}')]
    put(1, 'cumple' if not bad else 'NO cumple', f'sha256 de {REQ} en HASHES_CODIGO.txt (ultimo bloque) coinciden con disco' if not bad else f'discrepan {bad}')
    hm = os.path.getmtime(P + '/HASHES_CODIGO.txt'); late = [n for n in REQ if os.path.getmtime(f'{P}/{n}') > hm + 1]
    put(25, 'cumple' if not late else 'NO cumple', 'ningun fichero de la lista modificado despues de HASHES_CODIGO.txt (hash y mtime)' if not late else f'mtime posterior: {late}')
else: put(1, 'pendiente', 'se escribe al congelar (paso 4); se verifica con --final'); put(25, 'pendiente', 'idem (hash y mtime) con --final')
# ---- H2/H3 : p3 en directorio aislado (copias), sin tocar dias de veredicto
T = SCR + '/h23'; shutil.rmtree(T, ignore_errors=True); os.makedirs(T + '/out')
for n in REQ: shutil.copy(f'{P}/{n}', f'{T}/{n}')
open(T + '/HASHES_CODIGO.txt', 'w').write(''.join(f'{sha(f"{T}/{n}")}  {n}\n' for n in REQ))
def run_p3(env_extra=None):
    env = dict(os.environ); env.pop('P3_DISENO', None); env.pop('PISTA_SUF', None); env.update(env_extra or {})
    r = subprocess.run([sys.executable, T + '/p3_agrega.py', 'btc', 'act'], capture_output=True, text=True, env=env, timeout=600)
    j = glob.glob(T + '/out/p3_btc_act_BLOCKED.json'); return r.returncode, r.stdout.strip()[-300:], (json.load(open(j[0])) if j else None)
def clean(): [os.remove(f) for f in glob.glob(T + '/out/*')]
pk = f'{O}/p1_btc_2026-11-12{SUF}.pkl'
# H2: pkl de 12 y 16-Nov presentes, ninguno de veredicto -> el 12/16 no se lee ni se lista
for D_ in ('2026-11-12', '2026-11-16'): os.symlink(pk, f'{T}/out/p1_btc_{D_}.pkl')
rc, so, bj = run_p3(); lista = bj['dias_lista'] if bj else None
ok2 = (rc == 2 and bj is not None and lista == ['2026-11-13', '2026-11-14', '2026-11-15', '2026-11-17', '2026-11-18', '2026-11-19'] and 'ningun dia valido' in bj['motivo'])
put(2, 'cumple' if ok2 else 'NO cumple', f'p3 en modo veredicto con pkl de 12 y 16-Nov presentes: rc={rc}, lista={lista}, motivo={bj and bj["motivo"]}; el codigo falla (assert) si el pkl trae un dia fuera de la lista')
# H3: falta informe E / dia incompleto / hash alterado
clean(); os.symlink(pk, f'{T}/out/p1_btc_2026-11-13.pkl'); rc1, _, b1 = run_p3()
clean(); os.symlink(pk, f'{T}/out/p1_btc_2026-11-13.pkl'); shaP = sha(pk)
open(f'{T}/out/p7w_btc_2026-11-13.pkl', 'wb').write(b'x'); json.dump(dict(SHA256_pkl_p1=shaP, dia_completo=dict(ok=False), dia_valido_E=True, E4_fallos=[]), open(f'{T}/out/p7_btc_2026-11-13.json', 'w')); rc2, _, b2 = run_p3()
clean(); os.symlink(pk, f'{T}/out/p1_btc_2026-11-13.pkl'); open(f'{T}/out/p7w_btc_2026-11-13.pkl', 'wb').write(b'x'); json.dump(dict(SHA256_pkl_p1=shaP, dia_completo=dict(ok=True), dia_valido_E=False, E4_fallos=['E1 simulado']), open(f'{T}/out/p7_btc_2026-11-13.json', 'w')); rc3, _, b3 = run_p3()
clean(); open(f'{T}/p7_ipw_balance.py', 'a').write('\n# alterado\n'); rc4, _, b4 = run_p3(); shutil.copy(f'{P}/p7_ipw_balance.py', f'{T}/p7_ipw_balance.py')
ok3 = (rc1 == 2 and 'falta el informe de balance' in b1['motivo'] and rc2 == 2 and 'incompleto' in b2['motivo'] and rc3 == 2 and b3['extra'].get('excluidos_E') and rc4 == 2 and 'hash de p7_ipw_balance.py' in b4['motivo'])
put(3, 'cumple' if ok3 else 'NO cumple', f'BLOCKED sin leer tasas si: falta informe E ({b1 and b1["motivo"]}), dia incompleto ({b2 and b2["motivo"]}), hash alterado ({b4 and b4["motivo"]}); dia con E fallido se excluye y se lista: {b3 and b3["extra"]}')
put(15, 'cumple' if ok3 and 'dia_valido_E' in r7 and 'E4_fallos' in r7 else 'NO cumple', f'p7 escribe dia_valido_E={r7["dia_valido_E"]} y E4_fallos ({len(r7["E4_fallos"])}); p3 excluye automaticamente el dia que falla E (prueba aislada arriba, excluidos_E={b3 and list(b3["extra"].get("excluidos_E", {}))})')
# ---- H4/H5/H6
fields_ok = {n: all(c in X.columns for c in DF + ['D_maxrx']) for n, X in (('EV', EV), ('PL', PL), ('PW', PW))}
cpok = all(c in CP.columns for c in ('dist_ticks', 'edad_nivel', 'edad_cens'))
put(4, 'cumple' if all(fields_ok.values()) else 'NO cumple', f'campos D en EV/PL/PW (misma funcion dfields): {fields_ok}; ademas dist_ticks/edad en CP={cpok}; n EV={len(EV)}, PL={len(PL)}, PW={len(PW)}; NaN EV={ {c: int(EV[c].isna().sum()) for c in DF} }')
viol = {n: int((X.D_maxrx > X.t - 1000).sum()) for n, X in (('EV', EV), ('PL', PL), ('PW', PW))}; nrows = {n: len(X) for n, X in (('EV', EV), ('PL', PL), ('PW', PW))}
# recomputo independiente de 30 eventos (dist_ticks, spread, dp_signed, edad_nivel) desde las lineas crudas
rs = np.random.default_rng(5); ev = EV[EV.dist_ticks.notna() & EV.spread.notna() & EV.dp_signed.notna()]; sample = ev.iloc[rs.choice(len(ev), 40, replace=False)]
d0 = pd.Timestamp('2026-11-12'); comp = {}
for dd in (d0 - pd.Timedelta(days=1), d0, d0 + pd.Timedelta(days=1)):
    fn = f'/root/polymarket-research-datalogs/sonda1/pasivo/sonda1_fotos_l2_{dd.date()}.csv.gz'
    if not os.path.exists(fn): continue
    rows = collections.defaultdict(dict)
    for ch in pd.read_csv(fn, usecols=['slug', 'token', 'rol'], dtype=str, chunksize=300000):
        ch = ch[ch.slug.str.startswith('btc-updown-5m')].drop_duplicates(['slug', 'rol'])
        for r in ch.itertuples(): rows[r.slug][r.rol] = r.token
    for s_, t in rows.items():
        if 'tok' in t and 'comp' in t: comp[t['tok']] = t['comp']; comp[t['comp']] = t['tok']
needlv = set(zip(sample.X, sample.p)); need = set(sample.X) | {comp[x] for x in sample.X}; tf = f'{SCR}/h5_tokens.txt'; open(tf, 'w').write('\n'.join(need) + '\n')
bk = collections.defaultdict(dict); ser = collections.defaultdict(list); lvh = collections.defaultdict(list)
pr = subprocess.Popen(f'zcat {FX} | grep -F -f {tf}', shell=True, stdout=subprocess.PIPE, text=True)
for l in pr.stdout:
    p = l.rstrip('\n').split(',')
    if len(p) < 8 or p[2] not in need: continue
    r = int(p[6]) if p[0] in ('B', 'd') and p[6].isdigit() else None
    if r is None: continue
    tk = p[2]; b = bk[tk]
    if p[0] == 'B':
        b.clear()
        for x in p[3].split(';'):
            if x: a_, s_ = x.split(':'); b[round(float(a_), 2)] = float(s_)
        for q in b:
            if (tk, q) in needlv: lvh[(tk, q)].append((r, b[q]))
    elif p[0] == 'd' and p[3] == 'B':
        q = round(float(p[4]), 2); z = float(p[5])
        if z > 0: b[q] = z
        else: b.pop(q, None)
        if (tk, q) in needlv: lvh[(tk, q)].append((r, z))
    else: continue
    bm = max(b) if b else np.nan
    if not ser[tk] or not (ser[tk][-1][1] == bm or (bm != bm and ser[tk][-1][1] != ser[tk][-1][1])): ser[tk].append((r, bm))
def best(tk, t):
    L = ser.get(tk, []); i = bisect.bisect_right([x[0] for x in L], t) - 1; return L[i][1] if i >= 0 else np.nan
def lvl_at(tk, q, t):
    L = lvh.get((tk, q), []); i = bisect.bisect_right([x[0] for x in L], t) - 1; return (i, L[i][1]) if i >= 0 else (-1, 0.0)
mm = collections.Counter()
for r in sample.itertuples():
    tr = r.t - 1000; cX = comp[r.X]; b0 = best(r.X, tr); bC = best(cX, tr); b1 = best(r.X, tr - 1000)
    exp = dict(dist_ticks=(b0 - r.p) / 0.01, spread=100 * (1 - bC - b0), dp_signed=(b0 - b1) / 0.01)
    for k, v in exp.items(): mm[k + '_ok'] += int(np.isfinite(v) and abs(v - getattr(r, k)) < 1e-6); mm[k + '_n'] += 1
    i, z = lvl_at(r.X, r.p, tr)
    if z > 0:
        L = lvh[(r.X, r.p)]; j = i
        while j > 0 and L[j - 1][1] > 0: j -= 1
        ed = tr - L[j][0]; cens_exp = (j == 0)
        mm['edad_ok'] += int(abs(ed - r.edad_nivel) <= 1 or r.edad_cens); mm['edad_n'] += 1
    else: mm['edad_ok'] += int(r.edad_nivel == 0); mm['edad_n'] += 1
ok5 = all(v == 0 for v in viol.values()) and all(n >= 1000 for n in nrows.values()) and all(mm[k + '_ok'] >= 0.9 * mm[k + '_n'] for k in ('dist_ticks', 'spread', 'dp_signed', 'edad'))
put(5, 'cumple' if ok5 else 'NO cumple', f'D_maxrx<=t-1000 en el 100 % de las filas (violaciones {viol}, filas {nrows}); p1 asierta ademas en ejecucion; recomputo independiente (replay propio de las lineas crudas) de {len(sample)} eventos: ' + ', '.join(f'{k}: {mm[k+"_ok"]}/{mm[k+"_n"]}' for k in ('dist_ticks', 'spread', 'dp_signed', 'edad')))
put(6, 'cumple' if r7['D3_NaN_SMD_leq_010'] else 'NO cumple', 'SMD del indicador NaN evento vs control: ' + json.dumps({k: v['SMD_indicador'] for k, v in r7['D3_indicador_NaN'].items()}) + '; dist_ticks NaN = estrato propio nand (ADENDA_09 §6): n eventos nand=' + str(r7['prim|vec']['universo'].get('n_dist_nan_estrato_nand')) + ', viable=' + str((r7['prim|vec']['por_clase']['lo']['estratos'].get('nand') or {}).get('viable', 'sin eventos nand en la clase lo')))
# ---- H7..H14 desde el informe p7
lo = r7['prim|vec']['por_clase']['lo']; Ec = r7.get('E', {})
wl = pickle.load(open(f'{O}/p7w_btc_2026-11-12{SUF}.pkl', 'rb'))['pesos']; dup = {k: int(v['W'].index.duplicated().sum()) for k, v in wl.items() if len(v['W'])}
stl = r7['prim|vec']['por_clase']['lo']['estratos']; ex = {t: v.get('soporte_por_peldano_eventos') for t, v in stl.items()}; ks_d = {t: (v.get('E2_KS') or {}).get('dist_ticks') for t, v in Ec.get('estratos', {}).items()}
ok7 = 'dist_ticks' in Ec.get('E1_covariables', []) and 'sens_igualdad_exacta_dist_ticks' in r7 and all(v == 0 for v in dup.values()) and all(('soporte_por_peldano_eventos' in v) or v.get('n_soporte', 0) == 0 for v in stl.values()) and all(v is not None and v <= 0.10 for v in ks_d.values())
put(7, 'cumple' if ok7 else 'NO cumple', f'igualdad EXACTA de rango (ADENDA_09, declarada PRIMARIA): escalera R1-R4/R1-R2 con reclamacion exclusiva, controles duplicados en los pesos={dup}; eventos por peldano {ex}; KS ponderado de dist_ticks por estrato {ks_d}; E1 simple restringido al rango (frac sin pareja {Ec.get("E1_simple", {}).get("frac_sin_pareja_sobre_universo")}); version estricta (k exacto sin bins) frac_sin_pareja={r7.get("sens_igualdad_exacta_dist_ticks", {}).get("frac_sin_pareja_sobre_universo")}')
eks = lo.get('edad_KS'); consist = bool(eks) and (lo['usa_edad_EB'] == any(v['KS'] is not None and v['KS'] > 0.10 for v in eks.values()))
put(8, 'cumple' if consist else 'NO cumple', f'KS(edad_nivel) por estrato n>=100: {eks}; usa_edad_EB={lo["usa_edad_EB"]} (automatico, escrito en informe)')
put(9, 'cumple' if set(r7['prim|vec']['por_clase']) <= {'lo', 'hi', 'indet'} and 'lo' in r7['prim|vec']['por_clase'] else 'NO cumple', 'fit separado por clase: ' + str({k: v.get('n_univ') for k, v in r7['prim|vec']['por_clase'].items()}) + ' (hi/indet sin eventos en el fixture: estructura implementada, no ejercitada con datos)')
put(10, 'cumple' if 'sens_solo_nivel_propio' in r7 else 'NO cumple', 'solo nivel propio: ' + json.dumps({k: r7.get('sens_solo_nivel_propio', {}).get(k) for k in ('n_soporte', 'n_eff_pooled', 'n_eff_por_estrato')}))
put(11, 'cumple' if 'con_z0' in Ec.get('pooled', {}) and 'sin_z0' in Ec.get('pooled', {}) else 'NO cumple', 'pooled con z0 n=%s n_eff=%s; sin z0 n=%s n_eff=%s' % (Ec['pooled']['con_z0']['n'], Ec['pooled']['con_z0']['n_eff'], Ec['pooled'].get('sin_z0', {}).get('n'), Ec['pooled'].get('sin_z0', {}).get('n_eff')))
e1 = {t: (v['n'], max([abs(x) for x in v['SMD'].values() if x is not None], default=None)) for t, v in Ec['E1_simple']['por_estrato'].items()}
put(12, 'cumple' if e1 else 'NO cumple', f'E1 implementado (tope 0,15 / marca 0,10 por estrato n>=100): (n, max|SMD|) por estrato {e1}; fixture: {"supera" if not any("E1" in x for x in r7["E4_fallos"]) else "NO supera"} E1')
e2 = {t: dict(KS=v.get('E2_KS'), n_eff=v['n_eff']) for t, v in Ec['estratos'].items()}
put(13, 'cumple' if all('E2_KS' in v and set(v['E2_KS']) == {'act2', 'WA_q', 'ttc', 'absr5', 'dist_ticks'} for v in Ec['estratos'].values()) else 'NO cumple', f'E2 KS ponderado en las 5 variables y n_eff por estrato implementado; fixture: {"supera" if not any("E2" in x for x in r7["E4_fallos"]) else "NO supera"} (ver fallos)')
cols_used = set(sum(r7['columnas_usadas'].values(), [])); nof = not any(c.startswith(('f_', 'F', 'C')) and c not in ('CP',) for c in cols_used if c not in ('D', 'D_maxrx'))
put(14, 'cumple' if r7['aserto_sin_columnas_de_desenlace'] and nof and any('E3_propio_vs_vecino' in v for v in Ec['estratos'].values()) else 'NO cumple', 'E3 (propio vs vecino, z0 y small) calculado con lista blanca de columnas (aserto en p7: ninguna f_*, C*, F*); fixture: ' + str({t: v['E3_propio_vs_vecino'].get('max_abs_pond') for t, v in Ec['estratos'].items() if 'E3_propio_vs_vecino' in v}) + ' (umbral 0,10)')
# ---- H16..H21, H23, H24 (p3 en DISENO sobre el fixture + pruebas unitarias de las funciones)
src = open(P + '/p3_agrega.py').read(); i0 = src.index("rg = np.random.default_rng(20261118)"); i1 = src.index("CONF = dict(etiqueta='CONFIRMATORIO'")
ns = dict(np=np, pd=pd, sst=sst, pickle=pickle, H=P, COIN='btc', SUF='', CAND=[], E=pd.DataFrame(dict(evid=['x'])), json=json)
exec(src[i0:i1], ns)
C = (p3 or {}).get('CONFIRMATORIO', {})
put(16, 'cumple' if C and len(C.get('maxstat_V1_V7', {})) == 7 and C.get('B_permutaciones') == 2000 and 'V1' in C.get('maxstat_V1_V7', {}) else 'NO cumple', 'test confirmatorio V1 pooled IPW+EB clase lo: max-estadistico sobre V1..V7, 2.000 permutaciones con signo por mercado sobre d_m (ejecutado en el fixture DISENO, sin veredicto)')
put(17, 'cumple' if all('p_holm_x3' in v for k, v in C.get('estratos_holm', {}).items() if 'p_perm_V1' in v) and C.get('EXPLORATORIO', {}).get('etiqueta') == 'EXPLORATORIO' and p3.get('seccion_heredada_v3') == 'EXPLORATORIO' else 'NO cumple', f'Holm x3 en estratos {[ (k, v.get("p_holm_x3")) for k, v in C.get("estratos_holm", {}).items()]}; EXPLORATORIO marcado en JSON')
h = ns['holm']({'a': 0.01, 'b': 0.02, 'c': 0.5}); ok_h = h == {'a': 0.03, 'b': 0.04, 'c': 0.5}
x = [0.1, 0.2, 0.3, 0.4, 0.5]; ic = ns['ic_t'](x); ref = 0.3 + sst.t.ppf(0.95, 4) * np.std(x, ddof=1) / np.sqrt(5)
put(18, 'cumple' if ok_h and abs(ic[1] - ref) < 1e-12 and 'C2' in C.get('V1', {}) and 'IC_mas_ancho' in C.get('V1', {}) else 'NO cumple', f't de Student df=n-1 verificada (ic_t=[{ic[0]:.4f},{ic[1]:.4f}] frente a scipy {ref:.4f}), Holm verificado, bootstrap por mercado C2 presente, IC decisivo = el mas ancho (cual={C.get("V1", {}).get("IC_mas_ancho", {}).get("cual")})')
dc = ns['decidir']; g = dict(dif=0.05, low1=0.01, up=0.09, hs=0.02, pmx=0.01, c5=True, LR=2.0, ddv=0.01, nd=6, ne=500)
def dcd(**kw): a = dict(g); a.update(kw); return dc(a['dif'], a['low1'], a['up'], a['hs'], a['pmx'], a['c5'], a['LR'], a['ddv'], a['nd'], a['ne'], a.get('f1', False), a.get('c1', None))[0]
t19 = [dcd() == 'SOPORTADA', dcd(hs=0.031) == 'INSUFFICIENT', dcd(hs=0.03) == 'SOPORTADA', dcd(dif=-0.01, low1=-0.04, up=0.019, hs=0.03, pmx=0.5, LR=0.9) == 'NO SOPORTADA', dcd(dif=-0.01, low1=-0.05, up=0.02, hs=0.035, pmx=0.5) == 'INSUFFICIENT',
       dcd(dif=-0.01, low1=-0.05, up=0.03, hs=0.04, pmx=0.5) == 'INSUFFICIENT', dcd(dif=-0.01, low1=-0.04, up=0.019, hs=0.03, pmx=0.5, nd=4) == 'INSUFFICIENT', dcd(dif=-0.01, low1=-0.04, up=0.019, hs=0.03, pmx=0.5, ne=299) == 'INSUFFICIENT',
       dcd(c5=False) == 'INSUFFICIENT', dcd(LR=1.4) == 'INSUFFICIENT', dcd(ddv=-0.01) == 'INSUFFICIENT', dcd(pmx=0.06) == 'INSUFFICIENT', dcd(low1=-0.001) == 'INSUFFICIENT']
sm = (C.get('estratos_holm', {}).get('small') or {}).get('semiancho_leq_006')
put(19, 'cumple' if all(t19) else 'NO cumple', f'gates 0,02(NO SOPORTADA: limite superior<+0,02 segun ADENDA_07 D1) / 0,03 (SOPORTADA) / small 0,06 implementados; tabla de 13 casos sinteticos de decidir(): {sum(t19)}/13 correctos; small semiancho<=0,06 en el fixture: {sm}')
rg2 = np.random.default_rng(1); ev_ = []; ct_ = []
for k, (D_, n) in enumerate([(f'2026-11-1{i}', 100) for i in range(3, 9)]):
    ev_.append(pd.DataFrame(dict(evid=[f'{D_}{j}' for j in range(n)], st='normal', D=D_, end=np.arange(n) + 1000 * k + 0.0, V1=(rg2.random(n) < 0.3).astype(float)))); ct_.append(pd.DataFrame(dict(st='normal', om=np.ones(n), D=D_, end=np.arange(n) + 1000 * k + 0.0, V1=(rg2.random(n) < 0.2).astype(float))))
evs, cts = pd.concat(ev_, ignore_index=True), pd.concat(ct_, ignore_index=True); an = ns['analiza'](evs, cts, 'V1', B=300)
big = evs.copy(); ctb = cts.copy(); extra = pd.DataFrame(dict(evid=[f'z{j}' for j in range(1500)], st='normal', D='2026-11-13', end=np.arange(1500) + 0.0, V1=1.0)); ctx = pd.DataFrame(dict(st='normal', om=np.ones(1500), D='2026-11-13', end=np.arange(1500) + 0.0, V1=0.0))
an2 = ns['analiza'](pd.concat([evs, extra], ignore_index=True), pd.concat([cts, ctx], ignore_index=True), 'V1', B=300)
flip = ev_[0].copy(); flip['V1'] = 0.0; ev_f = pd.concat([flip] + ev_[1:], ignore_index=True); ct_f = pd.concat([ct_[0].assign(V1=1.0)] + ct_[1:], ignore_index=True); an3 = ns['analiza'](ev_f, ct_f, 'V1', B=300)
ok20 = an['C5']['cumple_35'] and an['C5']['signos_iguales'] and (not an2['C5']['cumple_35']) and (not an3['C5']['signos_iguales']) and set(an['C5']['leave_one_day_out']) == set(f'2026-11-1{i}' for i in range(3, 9))
put(20, 'cumple' if ok20 and 'C5' in C.get('V1', {}) else 'NO cumple', f'C5 probada con datos sinteticos: 6 dias iguales (max frac {an["C5"]["max_dia_frac_masa"]}) -> cumple; un dia con >35 % ({an2["C5"]["max_dia_frac_masa"]}) -> no; un dia que invierte el signo en LODO -> signos_iguales={an3["C5"]["signos_iguales"]}; LODO y fraccion por dia en el JSON del fixture')
f1 = r7['F1']; t21 = dc(0.05, 0.01, 0.09, 0.02, 0.01, True, 2.0, 0.01, 6, 500, True, -0.02)[0] == 'INSUFFICIENT' and dc(0.05, 0.01, 0.09, 0.02, 0.01, True, 2.0, 0.01, 6, 500, True, 0.03)[0] == 'SOPORTADA'
put(21, 'cumple' if 'SMD' in f1 and 'activar_veredicto_c1all' in f1 and t21 and 'c1all_V1' in C else 'NO cumple', f'F1 por dia: max|SMD| n_mk NaN vs unido = {f1["max_abs"]} (activar_c1all={f1["activar_veredicto_c1all"]}, n NaN={f1["n_nmk_nan"]}, unidos={f1["n_unidos"]}); p3 calcula c1all y discrepancia de signo => INSUFFICIENT (probado con decidir)')
put(22, 'pendiente', '')
p5j = json.load(open(O + '/p5_control_sin_relleno_fxtest.json')); g5 = p5j['post_estratificado_global']
ok22 = p5j['bins_fijos_ADENDA_07'] == dict(dt_ms=[555, 1839], vida_ms=[354, 997], vida_menos_dt_min_ms=500, repegado_excl_ms=300) and 'fraccion_pujas_cubierta' in p5j['cobertura'] and 'anclas_excl_repegado_300ms' in p5j['cobertura'] and 'M3_estado' in g5 and 'SMD_post_estrato' in g5
put(22, 'cumple' if ok22 else 'NO cumple', f'p5 v3 (humo con 40 ficheros L2; no es dia de veredicto): bins fijos 555/1839 y 354/997 asertados contra los datos de diseno, vida-dt>=500, exclusion +-300 ms de repegado ({p5j["cobertura"]["anclas_excl_repegado_300ms"]} anclas), estratos moneda x dt x vida ({len(g5["estratos"])} estratos), fraccion cubierta (pujas {p5j["cobertura"]["fraccion_pujas_cubierta"]}, rellenos {g5["fraccion_rellenos_cubiertos"]}), M3_estado={g5["M3_estado"][:12]}')
vset = set()
for a in range(40):
    vv = dc(float(rs.normal(0, .05)), float(rs.normal(0, .05)), float(rs.uniform(-.05, .1)), float(rs.uniform(0, .06)), float(rs.random()), bool(rs.random() < .5), float(rs.uniform(.5, 4)), float(rs.normal(0, .1)), int(rs.integers(2, 8)), int(rs.integers(100, 900)), bool(rs.random() < .3), float(rs.normal(0, .05)))
    vset.add(vv[0])
put(23, 'cumple' if vset <= {'SOPORTADA', 'NO SOPORTADA', 'INSUFFICIENT'} and (p3 or {}).get('CONFIRMATORIO', {}).get('veredicto') in ('NO_APLICA_DISENO',) else 'NO cumple', f'decidir() solo devuelve {sorted(vset)} en 40 casos aleatorios; en DISENO el JSON emite NO_APLICA_DISENO (no veredicto)')
keys = ['n_eventos', 'dias', 'mercados', 'n_eff_controles_Kish', 'sin_2_mejores_dias', 'C1', 'C2']; V1 = C.get('V1', {})
put(24, 'cumple' if all(k in V1 for k in keys) and all(k in C.get('V1_e250', {}) for k in keys) and 'n_eventos_primarios' in C else 'NO cumple', 'JSON confirmatorio incluye ' + str(keys) + ' para V1 y V1_e250; n_eventos_primarios=%s' % C.get('n_eventos_primarios'))
json.dump(RES, open(V + '/checks_H.json' if not FINAL else V + '/checks_H_final.json', 'w'), indent=1, default=str)
print(json.dumps({k: v['estado'] for k, v in RES.items()}))
