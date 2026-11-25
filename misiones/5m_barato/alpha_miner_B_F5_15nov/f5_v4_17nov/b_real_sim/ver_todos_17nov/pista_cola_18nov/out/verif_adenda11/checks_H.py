#!/usr/bin/env python3
"""checks_H.py v11 (ADENDA_11): ejecuta sobre el FIXTURE del 12-Nov (dia de DISENO; sufijo _fxP1, p1 v11) los 25 criterios H de ADENDA_06 adaptados por ADENDA_11 (B1, Holm x2, dia incompleto se excluye, 4d, n_eff) + extras X1-X4. NO toca ningun dia de veredicto.
Uso: checks_H.py [--final]   (--final comprueba H1 y H25: hashes congelados y mtime)"""
import sys, os, json, pickle, hashlib, subprocess, shutil, re, collections, bisect, glob, gzip
import numpy as np, pandas as pd
from scipy import stats as sst
P = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')); O = P + '/out'; V = O + '/verif_adenda11'
SCR = V + '/tmp'; os.makedirs(SCR, exist_ok=True)
FX = '/root/polymarket-research-datalogs/pista_cola_18nov/fx3h/fx3h.csv.gz'; FINAL = '--final' in sys.argv; RES = collections.OrderedDict()
def put(h, status, det): RES[h] = dict(estado=status, detalle=det); print(f'H{h:>2} {status}: {det}'[:600], flush=True)
def sha(f): return hashlib.sha256(open(f, 'rb').read()).hexdigest()
SUF = '_fxP1'; d1 = pickle.load(open(f'{O}/p1_btc_2026-11-12{SUF}.pkl', 'rb')); EV, PL, PW, CP = d1['EV'], d1['PL'], d1['PW'], d1['CP'][['dist_ticks', 'edad_nivel', 'edad_cens']].copy(); CFIX = d1.get('cover_fich'); VERS = d1.get('version'); d1['CP'] = None; d1 = None
r7 = json.load(open(f'{O}/p7_btc_2026-11-12{SUF}.json')); p3 = json.load(open(f'{O}/p3_btc_act{SUF}_DISENO.json')) if os.path.exists(f'{O}/p3_btc_act{SUF}_DISENO.json') else None
DF = ['dist_ticks', 'SQ_mej', 'act2_mej', 'spread', 'dp_signed', 'sg', 'edad_nivel']
# ---- H1 / H25 (solo --final)
REQ = ['p1_dia.py', 'p3_agrega.py', 'p7_ipw_balance.py', 'p5_control_sin_relleno.py', 'run_p1.sh', 'ADENDA_07_18nov.md', 'ADENDA_09_18nov.md', 'ADENDA_10_19nov.md', 'ADENDA_11_19nov.md']
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
open(f'{T}/out/p7w_btc_2026-11-13.pkl', 'wb').write(b'x'); json.dump(dict(SHA256_pkl_p1=shaP, dia_completo=dict(ok=False, cover_fich=[]), dia_valido_E=True, E4_fallos=[]), open(f'{T}/out/p7_btc_2026-11-13.json', 'w')); rc2, _, b2 = run_p3()
clean(); os.symlink(pk, f'{T}/out/p1_btc_2026-11-13.pkl'); open(f'{T}/out/p7w_btc_2026-11-13.pkl', 'wb').write(b'x'); json.dump(dict(SHA256_pkl_p1=shaP, dia_completo=dict(ok=True), dia_valido_E=False, E4_fallos=['E1 simulado']), open(f'{T}/out/p7_btc_2026-11-13.json', 'w')); rc3, _, b3 = run_p3()
clean(); open(f'{T}/p7_ipw_balance.py', 'a').write('\n# alterado\n'); rc4, _, b4 = run_p3(); shutil.copy(f'{P}/p7_ipw_balance.py', f'{T}/p7_ipw_balance.py')
ok3 = (rc1 == 2 and 'falta el informe de balance' in b1['motivo'] and rc2 == 2 and 'ningun dia valido' in b2['motivo'] and '2026-11-13' in b2['extra'].get('excluidos_incompletos', {}) and not b2['extra'].get('excluidos_E') and rc3 == 2 and b3['extra'].get('excluidos_E') and rc4 == 2 and 'hash de p7_ipw_balance.py' in b4['motivo'])
put(3, 'cumple' if ok3 else 'NO cumple', f'ADENDA_11 4a: BLOCKED sin leer tasas si falta informe E ({b1 and b1["motivo"]}) o hash alterado ({b4 and b4["motivo"]}); el dia INCOMPLETO ya no bloquea: se EXCLUYE y se lista ({b2 and b2["extra"].get("excluidos_incompletos", {}).keys()}; solo bloquea si no queda ningun dia valido); dia con E fallido se excluye y se lista: {b3 and b3["extra"]}')
put(15, 'cumple' if ok3 and 'dia_valido_E' in r7 and 'E4_fallos' in r7 else 'NO cumple', f'p7 escribe dia_valido_E={r7["dia_valido_E"]} y E4_fallos ({len(r7["E4_fallos"])}); p3 excluye automaticamente el dia que falla E (prueba aislada arriba, excluidos_E={b3 and list(b3["extra"].get("excluidos_E", {}))})')
# ---- H4/H5/H6
fields_ok = {n: all(c in X.columns for c in DF + ['D_maxrx', 'absr5_rx']) for n, X in (('EV', EV), ('PL', PL), ('PW', PW))}
cpok = all(c in CP.columns for c in ('dist_ticks', 'edad_nivel', 'edad_cens'))
put(4, 'cumple' if all(fields_ok.values()) else 'NO cumple', f'campos D en EV/PL/PW (misma funcion dfields): {fields_ok}; ademas dist_ticks/edad en CP={cpok}; n EV={len(EV)}, PL={len(PL)}, PW={len(PW)}; NaN EV={ {c: int(EV[c].isna().sum()) for c in DF} }')
viol = {n: int((X.D_maxrx > X.t - 1000).sum()) + int((X.absr5_rx > X.t - 1000).sum()) for n, X in (('EV', EV), ('PL', PL), ('PW', PW))}; nrows = {n: len(X) for n, X in (('EV', EV), ('PL', PL), ('PW', PW))}
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
# ---- ADENDA_11 §8(4): >=1.000 filas al azar (EV/PL/PW) recalculadas con codigo INDEPENDIENTE (python puro, bisect sobre listas) leyendo m5_registro col 7 (recepcion)
bxl, bpl = [], []
for dd in (d0, d0 + pd.Timedelta(days=1)):
    fn_ = f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{dd.date()}.csv.gz'
    if not os.path.exists(fn_): continue
    pr_ = subprocess.Popen(f"zcat {fn_} 2>/dev/null | grep -F ',BTCUSDT,' | grep '^x,'", shell=True, stdout=subprocess.PIPE, text=True)
    for l_ in pr_.stdout: q_ = l_.split(','); bxl.append(int(q_[7])); bpl.append(float(q_[3]))
oo = sorted(range(len(bxl)), key=bxl.__getitem__); bxl = [bxl[i] for i in oo]; bpl = [bpl[i] for i in oo]
def indep(t):
    def at(tt):
        i = bisect.bisect_right(bxl, tt) - 1
        return (bpl[i], bxl[i]) if i >= 0 and tt - bxl[i] < 5000 else (None, None)
    (b1, r1), (b0, r0) = at(t - 1000), at(t - 6000)
    return (None, -1) if (b1 is None or b0 is None) else (b1 / b0 - 1, r1)
rs2 = np.random.default_rng(11); nchk = collections.Counter(); bad_ind = []
for nm_, X_ in (('EV', EV), ('PL', PL), ('PW', PW)):
    for r_ in X_.iloc[rs2.choice(len(X_), 400, replace=False)].itertuples():
        ret_, rx_ = indep(int(r_.t)); okv = (np.isnan(r_.absr5) if ret_ is None else (abs(r_.absr5 - abs(ret_)) < 1e-12)) and int(r_.absr5_rx) == rx_ and (ret_ is None or rx_ <= r_.t - 1000)
        nchk[nm_ + '_n'] += 1; nchk[nm_ + '_ok'] += int(okv)
        if not okv: bad_ind.append((nm_, int(r_.t), r_.absr5, ret_, int(r_.absr5_rx), rx_))
ok_ind = bool(sum(v for k, v in nchk.items() if k.endswith('_n')) >= 1000 and not bad_ind)
ok5 = ok_ind and all(v == 0 for v in viol.values()) and all(n >= 1000 for n in nrows.values()) and all(mm[k + '_ok'] >= 0.9 * mm[k + '_n'] for k in ('dist_ticks', 'spread', 'dp_signed', 'edad'))
put(5, 'cumple' if ok5 else 'NO cumple', f'D_maxrx y absr5_rx<=t-1000 en el 100 % de las filas (violaciones {viol}, filas {nrows}); absr5/absr5_rx recalculados con codigo independiente (m5_registro col 7): {dict(nchk)} discrepancias={bad_ind[:3]}; p1 asierta ademas en ejecucion; recomputo independiente (replay propio de las lineas crudas) de {len(sample)} eventos: ' + ', '.join(f'{k}: {mm[k+"_ok"]}/{mm[k+"_n"]}' for k in ('dist_ticks', 'spread', 'dp_signed', 'edad')))
put(6, 'cumple' if r7['D3_NaN_SMD_leq_010'] else 'NO cumple', 'SMD del indicador NaN evento vs control: ' + json.dumps({k: v['SMD_indicador'] for k, v in r7['D3_indicador_NaN'].items()}) + '; dist_ticks NaN = estrato propio nand (ADENDA_09 §6): n eventos nand=' + str(r7['prim|vec']['universo'].get('n_dist_nan_estrato_nand')) + ', viable=' + str((r7['prim|vec']['por_clase']['lo']['estratos'].get('nand') or {}).get('viable', 'sin eventos nand en la clase lo')))
# ---- H7..H14 desde el informe p7
lo = r7['prim|vec']['por_clase']['lo']; Ec = r7.get('E', {})
wl = pickle.load(open(f'{O}/p7w_btc_2026-11-12{SUF}.pkl', 'rb'))['pesos']; dup = {k: int(v['W'].index.duplicated().sum()) for k, v in wl.items() if len(v['W'])}
stl = r7['prim|vec']['por_clase']['lo']['estratos']; ex = {t: v.get('soporte_por_peldano_eventos') for t, v in stl.items()}; ks_d = {t: (v.get('E2_KS') or {}).get('dist_ticks') for t, v in Ec.get('estratos', {}).items() if v.get('gating')}
ok7 = 'dist_ticks' in Ec.get('E1_covariables', []) and 'sens_igualdad_exacta_dist_ticks' in r7 and all(v == 0 for v in dup.values()) and all(('soporte_por_peldano_eventos' in v) or v.get('n_soporte', 0) == 0 for v in stl.values()) and all(v is not None and v <= 0.10 for v in ks_d.values())
put(7, 'cumple' if ok7 else 'NO cumple', f'igualdad EXACTA de rango (ADENDA_09, declarada PRIMARIA): escalera R1-R4/R1-R2 con reclamacion exclusiva, controles duplicados en los pesos={dup}; eventos por peldano {ex}; KS ponderado de dist_ticks por estrato {ks_d}; E1 simple restringido al rango (frac sin pareja {Ec.get("E1_simple", {}).get("frac_sin_pareja_sobre_universo")}); version estricta (k exacto sin bins) frac_sin_pareja={r7.get("sens_igualdad_exacta_dist_ticks", {}).get("frac_sin_pareja_sobre_universo")}')
eks = lo.get('edad_KS'); consist = bool(eks) and (lo['usa_edad_EB'] == any(v['KS'] is not None and v['KS'] > 0.10 for v in eks.values()))
put(8, 'cumple' if consist else 'NO cumple', f'KS(edad_nivel) por estrato n>=100: {eks}; usa_edad_EB={lo["usa_edad_EB"]} (automatico, escrito en informe)')
put(9, 'cumple' if set(r7['prim|vec']['por_clase']) <= {'lo', 'hi', 'indet'} and 'lo' in r7['prim|vec']['por_clase'] else 'NO cumple', 'fit separado por clase: ' + str({k: v.get('n_univ') for k, v in r7['prim|vec']['por_clase'].items()}) + ' (hi/indet sin eventos en el fixture: estructura implementada, no ejercitada con datos)')
put(10, 'cumple' if 'sens_solo_nivel_propio' in r7 else 'NO cumple', 'solo nivel propio: ' + json.dumps({k: r7.get('sens_solo_nivel_propio', {}).get(k) for k in ('n_soporte', 'n_eff_ctrl_kish_pooled', 'n_eff_contraste_pooled', 'n_eff_ctrl_kish_por_estrato')}))
pz = Ec['pooled']; put(11, 'cumple' if 'primario_z0_normal' in pz and 'sin_z0_normal' in pz and 'con_small_EXPLORATORIO' in pz else 'NO cumple', 'pooled z0+normal (primario) n=%s kish=%s n_eff_contraste=%s; normal sola n=%s; con small (exploratorio) n=%s' % (pz['primario_z0_normal']['n'], pz['primario_z0_normal']['n_eff_ctrl_kish'], pz['primario_z0_normal']['n_eff_contraste'], pz['sin_z0_normal']['n'], pz['con_small_EXPLORATORIO']['n']))
e1 = {t: (v['n'], max([abs(x) for x in v['SMD'].values() if x is not None], default=None)) for t, v in Ec['E1_simple']['por_estrato'].items()}
put(12, 'cumple' if e1 else 'NO cumple', f'E1 implementado (tope 0,15 / marca 0,10 por estrato n>=100): (n, max|SMD|) por estrato {e1}; fixture: {"supera" if not any("E1" in x for x in r7["E4_fallos"]) else "NO supera"} E1')
e2 = {t: dict(KS=v.get('E2_KS'), n_eff_ctrl_kish=v['n_eff_ctrl_kish'], n_eff_contraste=v['n_eff_contraste']) for t, v in Ec['estratos'].items()}
put(13, 'cumple' if all('E2_KS' in v and set(v['E2_KS']) == {'act2', 'WA_q', 'ttc', 'absr5', 'dist_ticks'} for v in Ec['estratos'].values()) else 'NO cumple', f'E2 KS ponderado en las 5 variables y n_eff_ctrl_kish / n_eff_contraste por estrato implementado; fixture: {"supera" if not any("E2" in x for x in r7["E4_fallos"]) else "NO supera"} (ver fallos)')
cols_used = set(sum(r7['columnas_usadas'].values(), [])); nof = not any(c.startswith(('f_', 'F', 'C')) and c not in ('CP',) for c in cols_used if c not in ('D', 'D_maxrx'))
put(14, 'cumple' if r7['aserto_sin_columnas_de_desenlace'] and nof and any('E3_propio_vs_vecino' in v for v in Ec['estratos'].values()) else 'NO cumple', 'E3 (propio vs vecino, z0 y small) calculado con lista blanca de columnas (aserto en p7: ninguna f_*, C*, F*); fixture: ' + str({t: v['E3_propio_vs_vecino'].get('max_abs_pond') for t, v in Ec['estratos'].items() if 'E3_propio_vs_vecino' in v}) + ' (umbral 0,10)')
# ---- H16..H21, H23, H24 (p3 en DISENO sobre el fixture + pruebas unitarias de las funciones)
src = open(P + '/p3_agrega.py').read(); i0 = src.index("rg = np.random.default_rng(20261118)"); i1 = src.index("CONF = dict(etiqueta='CONFIRMATORIO'")
ns = dict(np=np, pd=pd, sst=sst, pickle=pickle, H=P, COIN='btc', SUF='', CAND=[], E=pd.DataFrame(dict(evid=['x'])), json=json)
exec(src[i0:i1], ns)
C = (p3 or {}).get('CONFIRMATORIO', {})
put(16, 'cumple' if C and len(C.get('maxstat_V1_V7', {})) == 7 and C.get('B_permutaciones') == 2000 and 'V1' in C.get('maxstat_V1_V7', {}) else 'NO cumple', 'test confirmatorio V1 pooled IPW+EB clase lo: max-estadistico sobre V1..V7, 2.000 permutaciones con signo por mercado sobre d_m (ejecutado en el fixture DISENO, sin veredicto)')
put(17, 'cumple' if set(C.get('estratos_holm', {})) <= {'z0', 'normal'} and all('p_holm_x2' in v for k, v in C.get('estratos_holm', {}).items() if 'p_perm_V1' in v) and 'small' not in C.get('estratos_holm', {}) and 'small_EXPLORATORIO' in C and 'EXPLORATORIO' in C['small_EXPLORATORIO'].get('etiqueta', '') and C.get('EXPLORATORIO', {}).get('etiqueta') == 'EXPLORATORIO' and p3.get('seccion_heredada_v3') == 'EXPLORATORIO' else 'NO cumple', f'ADENDA_11 B1: Holm x2 en estratos {[ (k, v.get("p_holm_x2")) for k, v in C.get("estratos_holm", {}).items()]}; small fuera de Holm (EXPLORATORIO, p sin corregir {C.get("small_EXPLORATORIO", {}).get("p_perm_V1_sin_corregir")}); secciones EXPLORATORIO marcadas en JSON')
h = ns['holm']({'a': 0.01, 'b': 0.02, 'c': 0.5}); ok_h = h == {'a': 0.03, 'b': 0.04, 'c': 0.5}
x = [0.1, 0.2, 0.3, 0.4, 0.5]; ic = ns['ic_t'](x); ref = 0.3 + sst.t.ppf(0.95, 4) * np.std(x, ddof=1) / np.sqrt(5)
put(18, 'cumple' if ok_h and abs(ic[1] - ref) < 1e-12 and 'C2' in C.get('V1', {}) and 'IC_mas_ancho' in C.get('V1', {}) else 'NO cumple', f't de Student df=n-1 verificada (ic_t=[{ic[0]:.4f},{ic[1]:.4f}] frente a scipy {ref:.4f}), Holm verificado, bootstrap por mercado C2 presente, IC decisivo = el mas ancho (cual={C.get("V1", {}).get("IC_mas_ancho", {}).get("cual")})')
dc = ns['decidir']; g = dict(dif=0.05, low1=0.01, up=0.09, hs=0.02, pmx=0.01, c5=True, LR=2.0, ddv=0.01, nd=6, ne=500)
def dcd(**kw): a = dict(g); a.update(kw); return dc(a['dif'], a['low1'], a['up'], a['hs'], a['pmx'], a['c5'], a['LR'], a['ddv'], a['nd'], a['ne'], a.get('f1', False), a.get('c1', None), a.get('upc', None))[0]
NS = dict(dif=-0.01, low1=-0.04, up=0.019, hs=0.03, pmx=0.5, LR=0.9)       # condiciones de NO SOPORTADA sin F1
t19 = [dcd() == 'SOPORTADA', dcd(hs=0.031) == 'INSUFFICIENT', dcd(hs=0.03) == 'SOPORTADA', dcd(**NS) == 'NO SOPORTADA', dcd(dif=-0.01, low1=-0.05, up=0.02, hs=0.035, pmx=0.5) == 'INSUFFICIENT',
       dcd(dif=-0.01, low1=-0.05, up=0.03, hs=0.04, pmx=0.5) == 'INSUFFICIENT', dcd(nd=4, **NS) == 'INSUFFICIENT', dcd(ne=299, **NS) == 'INSUFFICIENT',
       dcd(c5=False) == 'INSUFFICIENT', dcd(LR=1.4) == 'INSUFFICIENT', dcd(ddv=-0.01) == 'INSUFFICIENT', dcd(pmx=0.06) == 'INSUFFICIENT', dcd(low1=-0.001) == 'INSUFFICIENT',
       # ADENDA_11 4a: un dia incompleto se excluye -> 5 de 6 dias validos = 5 (cumple), 4 de 6 = <5 (INSUFFICIENT), n_dias cuenta solo dias validos
       dcd(nd=5) == 'SOPORTADA', dcd(nd=4) == 'INSUFFICIENT',
       # ADENDA_11 4d (F1 activo): signo distinto bloquea SOPORTADA; NO SOPORTADA exige IC superior c1all < 0,02 y NO exige igualdad de signo
       dcd(f1=True, c1=-0.02, upc=0.01) == 'INSUFFICIENT', dcd(f1=True, c1=0.03, upc=0.09) == 'SOPORTADA', dcd(f1=True, c1=None, upc=0.09) == 'INSUFFICIENT',
       dcd(f1=True, c1=0.03, upc=0.019, **NS) == 'NO SOPORTADA', dcd(f1=True, c1=-0.03, upc=0.019, **NS) == 'NO SOPORTADA', dcd(f1=True, c1=-0.03, upc=0.02, **NS) == 'INSUFFICIENT',
       dcd(f1=True, c1=-0.03, upc=None, **NS) == 'INSUFFICIENT', dcd(f1=False, c1=-0.03, upc=0.5, **NS) == 'NO SOPORTADA']
sm = (C.get('small_EXPLORATORIO') or {}).get('p_perm_V1_sin_corregir')
put(19, 'cumple' if all(t19) else 'NO cumple', f'gates 0,02 (NO SOPORTADA: limite superior<+0,02, ADENDA_07 D1) / 0,03 (SOPORTADA); gate small 0,06 ELIMINADO (ADENDA_11 B1); 4a (dia incompleto cuenta contra >=5 dias) y 4d (F1: signo solo para SOPORTADA, IC superior c1all<0,02 para NO SOPORTADA); tabla de {len(t19)} casos sinteticos de decidir(): {sum(t19)}/{len(t19)} correctos {[i for i, x in enumerate(t19) if not x]}; small EXPLORATORIO p sin corregir en el fixture: {sm}')
rg2 = np.random.default_rng(1); ev_ = []; ct_ = []
for k, (D_, n) in enumerate([(f'2026-11-1{i}', 100) for i in range(3, 9)]):
    ev_.append(pd.DataFrame(dict(evid=[f'{D_}{j}' for j in range(n)], st='normal', D=D_, end=np.arange(n) + 1000 * k + 0.0, V1=(rg2.random(n) < 0.3).astype(float)))); ct_.append(pd.DataFrame(dict(st='normal', om=np.ones(n), D=D_, end=np.arange(n) + 1000 * k + 0.0, V1=(rg2.random(n) < 0.2).astype(float))))
evs, cts = pd.concat(ev_, ignore_index=True), pd.concat(ct_, ignore_index=True); an = ns['analiza'](evs, cts, 'V1', B=300)
big = evs.copy(); ctb = cts.copy(); extra = pd.DataFrame(dict(evid=[f'z{j}' for j in range(1500)], st='normal', D='2026-11-13', end=np.arange(1500) + 0.0, V1=1.0)); ctx = pd.DataFrame(dict(st='normal', om=np.ones(1500), D='2026-11-13', end=np.arange(1500) + 0.0, V1=0.0))
an2 = ns['analiza'](pd.concat([evs, extra], ignore_index=True), pd.concat([cts, ctx], ignore_index=True), 'V1', B=300)
flip = ev_[0].copy(); flip['V1'] = 0.0; ev_f = pd.concat([flip] + ev_[1:], ignore_index=True); ct_f = pd.concat([ct_[0].assign(V1=1.0)] + ct_[1:], ignore_index=True); an3 = ns['analiza'](ev_f, ct_f, 'V1', B=300)
ok20 = an['C5']['cumple_35'] and an['C5']['signos_iguales'] and (not an2['C5']['cumple_35']) and (not an3['C5']['signos_iguales']) and set(an['C5']['leave_one_day_out']) == set(f'2026-11-1{i}' for i in range(3, 9))
put(20, 'cumple' if ok20 and 'C5' in C.get('V1', {}) else 'NO cumple', f'C5 probada con datos sinteticos: 6 dias iguales (max frac {an["C5"]["max_dia_frac_masa"]}) -> cumple; un dia con >35 % ({an2["C5"]["max_dia_frac_masa"]}) -> no; un dia que invierte el signo en LODO -> signos_iguales={an3["C5"]["signos_iguales"]}; LODO y fraccion por dia en el JSON del fixture')
f1 = r7['F1']; t21 = dc(0.05, 0.01, 0.09, 0.02, 0.01, True, 2.0, 0.01, 6, 500, True, -0.02, 0.01)[0] == 'INSUFFICIENT' and dc(0.05, 0.01, 0.09, 0.02, 0.01, True, 2.0, 0.01, 6, 500, True, 0.03, 0.09)[0] == 'SOPORTADA' and 'c1all_balance_E_por_dia' in C
put(21, 'cumple' if 'SMD' in f1 and 'activar_veredicto_c1all' in f1 and t21 and 'c1all_V1' in C else 'NO cumple', f'F1 por dia: max|SMD| n_mk NaN vs unido = {f1["max_abs"]} (activar_c1all={f1["activar_veredicto_c1all"]}, n NaN={f1["n_nmk_nan"]}, unidos={f1["n_unidos"]}); p3 calcula c1all; F1: discrepancia de signo bloquea SOPORTADA, IC superior c1all<+0,02 exigido a NO SOPORTADA (probado con decidir, tabla de H19)')
put(22, 'pendiente', '')
p5j = json.load(open(O + '/p5_control_sin_relleno_fxtest.json')); g5 = p5j['post_estratificado_global']
ok22 = p5j['bins_fijos_ADENDA_07'] == dict(dt_ms=[555, 1839], vida_ms=[354, 997], vida_menos_dt_min_ms=500, repegado_excl_ms=300) and 'fraccion_pujas_cubierta' in p5j['cobertura'] and 'anclas_excl_repegado_300ms' in p5j['cobertura'] and 'M3_estado' in g5 and 'SMD_post_estrato' in g5
put(22, 'cumple' if ok22 else 'NO cumple', f'p5 v3 (humo con 40 ficheros L2; no es dia de veredicto): bins fijos 555/1839 y 354/997 asertados contra los datos de diseno, vida-dt>=500, exclusion +-300 ms de repegado ({p5j["cobertura"]["anclas_excl_repegado_300ms"]} anclas), estratos moneda x dt x vida ({len(g5["estratos"])} estratos), fraccion cubierta (pujas {p5j["cobertura"]["fraccion_pujas_cubierta"]}, rellenos {g5["fraccion_rellenos_cubiertos"]}), M3_estado={g5["M3_estado"][:12]}')
vset = set()
for a in range(40):
    vv = dc(float(rs.normal(0, .05)), float(rs.normal(0, .05)), float(rs.uniform(-.05, .1)), float(rs.uniform(0, .06)), float(rs.random()), bool(rs.random() < .5), float(rs.uniform(.5, 4)), float(rs.normal(0, .1)), int(rs.integers(2, 8)), int(rs.integers(100, 900)), bool(rs.random() < .3), float(rs.normal(0, .05)))
    vset.add(vv[0])
put(23, 'cumple' if vset <= {'SOPORTADA', 'NO SOPORTADA', 'INSUFFICIENT'} and (p3 or {}).get('CONFIRMATORIO', {}).get('veredicto') in ('NO_APLICA_DISENO',) else 'NO cumple', f'decidir() solo devuelve {sorted(vset)} en 40 casos aleatorios; en DISENO el JSON emite NO_APLICA_DISENO (no veredicto)')
keys = ['n_eventos', 'dias', 'mercados', 'n_eff_ctrl_kish', 'n_eff_contraste', 'n_mercados_ev', 'sin_2_mejores_dias', 'C1', 'C2']; V1 = C.get('V1', {})
put(24, 'cumple' if all(k in V1 for k in keys) and all(k in C.get('V1_e250', {}) for k in keys) and 'n_eventos_primarios' in C else 'NO cumple', 'JSON confirmatorio incluye ' + str(keys) + ' para V1 y V1_e250; n_eventos_primarios=%s' % C.get('n_eventos_primarios'))

# ======================= EXTRAS ADENDA_11 =======================
# X1: cover_fich (A) = recuento independiente en python del fixture + reglas de completitud de p7 (casos sinteticos sobre el codigo real de p7)
mn_, mx_, n_ = None, None, 0
pr_ = subprocess.Popen(f"zcat {FX} 2>/dev/null | grep -E '^[BdT],'", shell=True, stdout=subprocess.PIPE, text=True)
for l_ in pr_.stdout:
    q_ = l_.rstrip('\n').split(',')
    if len(q_) >= 8 and len(q_[6]) == 13 and q_[6].isdigit() and q_[6][0] == '1':
        r_ = int(q_[6]); n_ += 1; mn_ = r_ if mn_ is None else min(mn_, r_); mx_ = r_ if mx_ is None else max(mx_, r_)
ok_cf = bool(CFIX and len(CFIX) == 1 and CFIX[0]['min'] == mn_ and CFIX[0]['max'] == mx_ and CFIX[0]['n'] == n_ and VERS == 'p1_v11_ADENDA11' and r7['dia_completo']['cover_fich'] == CFIX)
src7 = open(P + '/p7_ipw_balance.py').read(); a7 = src7.index('# completitud por FICHEROS libro5'); b7 = src7.index("R['SHA256_codigo']"); code7 = src7[a7:b7]
from datetime import datetime, timezone, timedelta
def comp(cf, miss=()):
    D_ = '2026-11-13'; dd_ = datetime.strptime(D_, '%Y-%m-%d').replace(tzinfo=timezone.utc); t0_ = int(dd_.timestamp() * 1000); t1_ = t0_ + 86400000
    paths = [f'/root/polymarket-research-datalogs/onchain_fills_{D_}.csv.gz', '/root/polymarket-research-datalogs/onchain_fills_2026-11-14.csv.gz', f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{D_}.csv.gz', '/mnt/HC_Volume_106538179/m5_registro/m5_registro_2026-11-14.csv.gz']
    dloc = dict(D=D_, cover_fich=[dict(fichero=f'x{i}', min=t0_ + a_, max=t1_ + b_, n=nn) for i, (a_, b_, nn) in enumerate(cf)], inputs=[dict(path=p_, size=(None if p_ in miss else 1)) for p_ in paths]); ns_ = dict(d=dloc, R={}); exec(code7, ns_); return ns_['R']['dia_completo']['ok']
# casos de hueco explicitos (los ficheros se definen por min/max relativos a t0): hueco 300 s ok, 301 s no
def comp2(gap_ms): 
    D_ = '2026-11-13'; dd_ = datetime.strptime(D_, '%Y-%m-%d').replace(tzinfo=timezone.utc); t0_ = int(dd_.timestamp() * 1000); mid = t0_ + 40000000
    paths = [f'/root/polymarket-research-datalogs/onchain_fills_{D_}.csv.gz', '/root/polymarket-research-datalogs/onchain_fills_2026-11-14.csv.gz', f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{D_}.csv.gz', '/mnt/HC_Volume_106538179/m5_registro/m5_registro_2026-11-14.csv.gz']
    cf_ = [dict(fichero='a', min=t0_ + 1000, max=mid, n=5), dict(fichero='b', min=mid + gap_ms, max=t0_ + 86400000 - 1000, n=5)]
    ns_ = dict(d=dict(D=D_, cover_fich=cf_, inputs=[dict(path=p_, size=1) for p_ in paths]), R={}); exec(code7, ns_); return ns_['R']['dia_completo']['ok']
cases = [comp([(60000, -60000, 9)]) is True, comp([(121000, -60000, 9)]) is False, comp([(120000, -120000, 9)]) is True, comp([(60000, -121000, 9)]) is False, comp([(60000, -60000, 0)]) is False,
         comp([(60000, -60000, 9)], miss=('/root/polymarket-research-datalogs/onchain_fills_2026-11-14.csv.gz',)) is False, comp([(60000, -60000, 9)], miss=('/mnt/HC_Volume_106538179/m5_registro/m5_registro_2026-11-13.csv.gz',)) is False,
         comp2(300000) is True, comp2(301000) is False, comp2(-5000) is True]
put('X1_cover_fich', 'cumple' if ok_cf and all(cases) else 'NO cumple', f'cover_fich del fixture {CFIX} == recuento independiente (min {mn_}, max {mx_}, n {n_}); p7 usa cover_fich (dia_completo del fixture: ok={r7["dia_completo"]["ok"]}, cobertura_ok={r7["dia_completo"]["cobertura_ok"]}, inputs_ok={r7["dia_completo"]["inputs_ok"]}: el fixture dura 3 h); reglas de completitud de p7 (cabecera 120 s, cola 120 s, hueco 300/301 s, n=0, onchain/m5_registro de D y D+1 ausentes, solape) = {sum(cases)}/{len(cases)} casos sinteticos sobre el codigo real de p7')
# X2: B1 (small exploratorio, fuera de dia_valido_E)
sm_ = r7['prim|vec']['por_clase']['lo']['estratos'].get('small', {}); eg_s = Ec['estratos'].get('small', {})
put('X2_B1_small_exploratorio', 'cumple' if (eg_s.get('exploratorio') is True and eg_s.get('gating') is False and not any(' small ' in x for x in r7['E4_fallos']) and set(Ec['estratos_condicion_de_fallo']) == {'z0', 'normal'} and r7['dia_valido_E'] == (len(r7['E4_fallos']) == 0)) else 'NO cumple',
    f'small n_univ={eg_s.get("n_univ")}: gating={eg_s.get("gating")} exploratorio={eg_s.get("exploratorio")}; fallos E4 {r7["E4_fallos"]}; dia_valido_E={r7["dia_valido_E"]}; p3: estratos_holm={list(C.get("estratos_holm", {}))}, small_EXPLORATORIO presente={"small_EXPLORATORIO" in C}')
# X3: n_eff_ctrl_kish / n_eff_contraste / n_mercados_ev (4) y reproduccion de las cifras esperadas con los p7 ANTIGUOS (§4.3)
def nec_(n, k): return round(1 / (1 / n + 1 / k), 1)
okn = True; det = {}
for t_, v in r7['prim|vec']['por_clase']['lo']['estratos'].items():
    if v.get('n_soporte', 0) > 0 and v.get('n_eff_ctrl_kish'): okn &= (v['n_eff_contraste'] == nec_(v['n_soporte'], v['n_eff_ctrl_kish']) and v['n_mercados_ev'] >= 1 and 'n_eff' not in v); det[t_] = (v['n_soporte'], v['n_eff_ctrl_kish'], v['n_eff_contraste'], v['n_mercados_ev'])
exp = {'12': dict(small=46.8, normal=797.2), '16': dict(small=53.5, normal=2057.6)}; got = {}
for dd_, ex in exp.items():
    fo = f'{O}/obsoletos_preD1/p7_btc_2026-11-{dd_}_DISENO_preADENDA11.json'
    if not os.path.exists(fo): okn = False; got[dd_] = 'falta ' + fo; continue
    ro = json.load(open(fo))['prim|vec']['por_clase']['lo']['estratos']; got[dd_] = {t_: nec_(ro[t_]['n_soporte'], ro[t_]['n_eff']) for t_ in ex}; okn &= (got[dd_] == ex)
put('X3_n_eff_contraste', 'cumple' if okn else 'NO cumple', f'fixture (n_soporte, Kish, n_eff_contraste, n_mercados_ev) por estrato {det}; con los p7 antiguos de 12/16-Nov: {got} (esperado {exp})')
# X4: E de c1all publicado y sin efecto en dia_valido_E
put('X4_E_c1all', 'cumple' if 'E_c1all' in r7 and 'E4_fallos_c1all' in r7 and 'c1all_balance_E_por_dia' in C and r7['dia_valido_E'] == (len(r7['E4_fallos']) == 0) else 'NO cumple', f'E_c1all pooled z0+normal={ (r7.get("E_c1all", {}).get("pooled", {}).get("primario_z0_normal") or {}).get("n")} eventos, fallos c1all informativos={r7.get("E4_fallos_c1all")}; p3 publica c1all_balance_E_por_dia={list(C.get("c1all_balance_E_por_dia", {}))}')
json.dump(RES, open(V + '/checks_H.json' if not FINAL else V + '/checks_H_final.json', 'w'), indent=1, default=str)
print(json.dumps({k: v['estado'] for k, v in RES.items()})); print('H cumplen:', sum(1 for k, v in RES.items() if isinstance(k, int) and v['estado'] == 'cumple'), '/ 25;', 'X cumplen:', sum(1 for k, v in RES.items() if isinstance(k, str) and v['estado'] == 'cumple'), '/', sum(1 for k in RES if isinstance(k, str)))
