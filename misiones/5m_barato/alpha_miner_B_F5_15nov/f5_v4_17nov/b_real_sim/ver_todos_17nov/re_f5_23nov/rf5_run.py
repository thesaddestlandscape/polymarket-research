#!/usr/bin/env python3
"""rf5_run.py MODO [DIA ...] -- runner diario de RF5E-COMB-23NOV-v1 (prereg 16be06b6). MODO: dia D... | estado.
 dia D : (1) fail-closed: sha de PREREG/ADENDAS R1v2 (puerta0_run.sha_prereg), PREREG_RF5 y HASHES_rf5.txt (codigo registrado ANTES del primer dia); (2) cobertura libro5_tx con_tx/units >=0,90 en d-1,d,d+1 (puerta0_run.cobertura_tx) y sha de tape/bad
         = TAPES_SHA256_ciegos.txt, si no INCOMPLETE TERMINAL (nunca se rellena); cinta aun no producida/fuente <48 h => PENDING; (3) trabajo A (familia F5: base,F1,F2,F3,U13,INV_F3; bloq0/bloq1) y trabajo K (combinada K1-K5,
         ablacion, V5/V6 aisladas, inversion, L_cancel 111/147; exige RF5_T_PROC_MS o rf5_t_proc_ms.txt, sin default: si falta => BLOCKED_T_PROC, A queda hecho y K se recupera despues).
         Salida en out_rf5_ciego/: rf5A_DIA.pkl, rf5K_DIA.pkl, rf5_f5_0_DIA.pkl, manifests por job y manifest_rf5dia_DIA.json. Solo CONTEOS/cobertura en el resumen parcial: NUNCA EV (el EV solo lo emite rf5_eval.py con >=10 dias validos).
 estado: JSON con el estado por dia (para el vigia). Idempotente: un job COMPLETE con el mismo codigo/sha de salidas se salta; pendientes (PENDING/BLOCKED) se reintentan; INCOMPLETE es terminal.
Reutiliza puerta0_run (cobertura/prereg/sha), fase_b_run (carga_binance, anota), replay_variantes (hooks parcheados sobre b_policy_sim sellado). 0 ordenes, 0 red, nada en data/."""
import sys, os, json, time, hashlib
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; V = os.path.dirname(HV.rstrip('/')) + '/'; BSIM = os.path.dirname(V.rstrip('/')) + '/'
OUT = os.environ.get('RF5_OUT', HV + 'out_rf5_ciego/'); os.makedirs(OUT, exist_ok=True)
os.environ['P0_OUT'] = OUT; os.environ['SEC7_OUT'] = OUT; os.environ['FB_OUT'] = OUT
os.environ.setdefault('P0_TAPES_REF', HV + 'TAPES_SHA256_ciegos.txt')
sys.path.insert(0, HV); sys.path.insert(0, V + 'r1v2_eval/'); sys.path.insert(0, V + 'r1v2_sec7/'); sys.path.insert(0, BSIM)
import numpy as np, pandas as pd
import puerta0_run as P0R                       # fija RU.OUT/PB, cobertura_tx, incompleto, sha_prereg (ver run_puerta0.sh)
import fase_b_run as FB                         # carga_binance, anota; sobrescribe RU.code_hashes/ya_completo -> se re-sobrescriben abajo
import sec7_run as RU, rf5_core as K5
RU.OUT = OUT
PREREG_RF5 = HV + 'PREREG_RF5_ENTRADA_23nov.md'; PREREG_RF5_SHA = '16be06b6194f8bbaf9225ba17fda56fe44a6faf5d4a0a790dfcd5340f82fac5e'
HASHES = HV + 'HASHES_rf5.txt'; FICH_REG = ('rf5_core.py', 'rf5_run.py', 'rf5_eval.py', 'rf5_cortes.json', 'prep_tapes_rf5.sh', 'run_rf5.sh', 'vigia_rf5.py')
COLS = ['dia', 'mid', 'coin', 'k', 'lado', 'L', 'q', 'cost', 'pnl', 'gana', 'fin', 't_dec', 'n_ord', 'motivo_fin', 'canal', 'estrato', 'f5t', 'tercil', 'bloq', 'pol', 'lcancel']
ts, log, sha, atomic_json, atomic_pkl = RU.ts, RU.log, RU.sha, RU.atomic_json, RU.atomic_pkl

def t_proc():
    """t_proc ms (tiempo de computo MEDIDO, sin default): RF5_T_PROC_MS o rf5_t_proc_ms.txt (lo fija el chief con su medicion; su sha va en HASHES_rf5.txt). None si falta."""
    v = os.environ.get('RF5_T_PROC_MS')
    if v is None and os.path.exists(HV + 'rf5_t_proc_ms.txt'): v = open(HV + 'rf5_t_proc_ms.txt').read().split()[0]
    return None if v is None else float(v)

def code_hashes():
    H = FB.code_hashes(); H['puerta0_run.py'] = sha(V + 'r1v2_eval/puerta0_run.py')
    for f in FICH_REG:
        if f in ('prep_tapes_rf5.sh', 'run_rf5.sh', 'vigia_rf5.py') and not os.path.exists(HV + f): continue
        H['rf5/' + f] = sha(HV + f)
    H['PREREG_RF5'] = sha(PREREG_RF5); return H
RU.code_hashes = code_hashes

def ya_completo(modo, d, outs):
    p = RU.mpath(modo, d)
    if not os.path.exists(p): return False
    try:
        m = json.load(open(p))
        ok = m.get('status') == 'COMPLETE' and set(m.get('outputs', {})) == set(outs) and all(os.path.exists(OUT + f) and sha(OUT + f) == h for f, h in m['outputs'].items()) and m.get('code') == code_hashes()
        return bool(ok and (modo != 'rf5K' or (m.get('cobertura') or {}).get('t_proc_ms') == t_proc()))
    except Exception: return False
RU.ya_completo = ya_completo

def verifica_registro():
    """fail-closed: HASHES_rf5.txt (formato sha256sum, escrito ANTES del 1.er dia ciego) debe cubrir cada fichero registrado y coincidir con el disco; PREREG_RF5 = sha firmado. Devuelve lista de problemas."""
    prob = []
    if sha(PREREG_RF5) != PREREG_RF5_SHA: prob.append('PREREG_RF5 sha != firmado')
    if not os.path.exists(HASHES): return prob + ['falta HASHES_rf5.txt (codigo no registrado)']
    reg = {l.split(None, 1)[1].strip(): l.split()[0] for l in open(HASHES) if l.strip() and not l.startswith('#') and len(l.split()) >= 2}
    for f in FICH_REG:
        if not os.path.exists(HV + f): continue
        if f not in reg: prob.append(f'{f} no registrado en HASHES_rf5.txt')
        elif reg[f] != sha(HV + f): prob.append(f'{f} sha != HASHES_rf5.txt (version nueva = cuenta como version nueva, prereg sec.8)')
    return prob

def dia_mpath(d): return OUT + f'manifest_rf5dia_{d}.json'
def lee_dia(d):
    p = dia_mpath(d); return json.load(open(p)) if os.path.exists(p) else None
def hoy(): return time.strftime('%Y-%m-%d', time.gmtime())
def dmas(d, n): return time.strftime('%Y-%m-%d', time.gmtime(time.mktime(time.strptime(d, '%Y-%m-%d')) + n * 86400 + 7200))

def cobertura_btc(d, base='/root/polymarket-research-datalogs/sa_ms/'):
    """DATA_BLOCKED_BTC explicito si sa_ms del dia no trae tokens BTC 5m (el simulador/cinta no cubren BTC)."""
    p = base + 'ms_%s.npz' % d
    if not os.path.exists(p): return dict(estado='SIN_FUENTE', tokens_btc_5m=None)
    z = np.load(p, allow_pickle=True); n = int(sum(1 for r in z['tmap'] if str(r[0]).upper() == 'BTC' and str(r[1]) == '5min'))
    return dict(estado=('OK' if n > 0 else 'DATA_BLOCKED_BTC'), tokens_btc_5m=n)

def estado_fuentes(d):
    """Para PENDING/INCOMPLETE por cinta ausente: ¿existe la fuente sa_ms del dia x en {d-1,d,d+1}? (la produce el cron 10:40Z del dia siguiente)."""
    return {x: os.path.exists('/root/polymarket-research-datalogs/sa_ms/ms_%s.npz' % x) for x in P0R.dias_vec(d)}

SA2 = '/root/polymarket-research-datalogs/sa_ms2/'; DLR = '/root/polymarket-research-datalogs/'; VOLMS = '/mnt/HC_Volume_106538179/maker_ms_crudo/'
EXT_MS2 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/ms_extract_v2.py'
def asegura_ms2(d, sa2=None, dlr=None, volms=None, ext=None):
    """ms2_D.npz (motor DayEngV4: dos relojes) NO lo produce ningun cron para dias >= 15-Nov: se extrae aqui del registro crudo maker_ms (datalogs o su copia 30 d en el volumen) con ms_extract_v2.py (sin modificar; ulimit y cron_pesado
    los pone el llamador). 'OK' | 'SIN_RAW' | 'FALLO'. Solo dias ya cerrados (d < hoy UTC)."""
    import glob, subprocess, tempfile
    sa2 = sa2 or SA2; dlr = dlr or DLR; volms = volms or VOLMS; ext = ext or EXT_MS2
    if os.path.exists(sa2 + f'ms2_{d}.npz'): return 'OK'
    if d >= hoy(): return 'SIN_RAW'
    tmp = tempfile.mkdtemp(prefix='rf5_ms2_'); n = 0
    for dd in (dmas(d, -1), d):
        vistos = set()
        for base in (dlr, volms):
            for f in sorted(glob.glob(base + f'maker_ms_{dd}_*.csv.gz')):
                b = os.path.basename(f)
                if b not in vistos: os.symlink(f, tmp + '/' + b); vistos.add(b); n += (dd == d)
    if not n: return 'SIN_RAW'
    r = subprocess.run([sys.executable, '-I', ext, d], env=dict(os.environ, SA2_DL=tmp + '/', SA2_OUT=sa2), capture_output=True, text=True)
    log('ms_extract_v2', d, 'rc', r.returncode, (r.stdout or '')[-300:], (r.stderr or '')[-300:])
    return 'OK' if (r.returncode == 0 and os.path.exists(sa2 + f'ms2_{d}.npz')) else 'FALLO'

def construye_f5tab(hooks_f5, d, bloq, pol):
    return pd.DataFrame([dict(dia=d, bloq=bloq, pol=pol, mid=m, k=k, **v) for (m, k), v in hooks_f5.items()])

def _replay(d, P, W, ctx, nombre, tabla, bsrc, cortes, tp, veto_set=None):
    import replay_variantes as RV
    W.fills.clear(); HK = K5.construye_hook(nombre, tabla, W._serie, bsrc, cortes, tp, lambda: W.fills, veto_set)
    R, cov = RV.run_day(d, P, E=W, HK=HK)
    if len(R):
        import puerta0_core as P0
        R = P0.unidad_primer_relleno(FB.anota(R, ctx, d)); R = R.assign(pol=nombre, lcancel=tabla[nombre][3])
    return R, cov, HK

def _col(R, bloq):
    R = R.assign(bloq=bloq)
    for c in COLS:
        if c not in R.columns: R[c] = np.nan
    return R[COLS]

def _veto_f3_por_celda(f5b, cortes):
    n = {}
    for r in f5b.itertuples():
        if K5.veta_f5('F3', r.coin, (None if not np.isfinite(r.f5_0) else r.f5_0), cortes): n[(r.dia, r.coin)] = n.get((r.dia, r.coin), 0) + 1
    return n

def run_A(d):
    import b_policy_sim as BS, eng_v5 as EV, sec7_core as C
    cortes = K5.lee_cortes(); E, info = EV.build(d); P = BS.params(); Rs = []; f5s = []; cov = dict(motor=info, jobs={}, verif_veto_postfiltro={}, desenlace={}); base = {}
    for bloq in (0, 1):
        W = C.EngineBloqueo(E, activo=bool(bloq)); ctx = dict(W=W, serie=W._serie)
        for nombre in K5.POLITICAS_A:
            if bloq == 1 and nombre not in K5.BLOQ1_SOLO: continue
            vs = None
            if nombre == 'INV_F3': vs = K5.lados_a_vetar_inversion(f5s[0], _veto_f3_por_celda(f5s[0], cortes))
            R, c, HK = _replay(d, P, W, ctx, nombre, K5.POLITICAS_A, None, cortes, None, vs)
            if len(R): Rs.append(_col(R, bloq))
            cov['jobs'][f'bloq{bloq}/{nombre}'] = dict(ordenes=int(len(R)), rellenos=int((R.q > 0).sum()) if len(R) else 0, contadores=dict(HK.cont), saltados=c.get('skip'))
            if nombre == 'base':
                base[bloq] = R; f5b = construye_f5tab(HK.f5_0, d, bloq, 'base'); f5s.append(f5b) if bloq == 0 else f5s.append(f5b)
                cov['desenlace'] = dict(mercados=c.get('mercados'), sin_desenlace=(c.get('skip') or {}).get('sin_desenlace', 0))
            elif nombre in ('F1', 'F2', 'F3', 'U13') and len(R) and bloq in base and len(base[bloq]):
                f5ref = f5s[bloq] if len(f5s) > bloq else f5s[0]
                cov['verif_veto_postfiltro'][f'bloq{bloq}/{nombre}'] = K5.verifica_veto_postfiltro(base[bloq], R, f5ref, nombre, cortes)
    atomic_pkl(OUT + f'rf5A_{d}.pkl', pd.concat(Rs, ignore_index=True)); atomic_pkl(OUT + f'rf5_f5_0_{d}.pkl', pd.concat(f5s, ignore_index=True))
    return dict(etiqueta='CONTEOS; sin EV', politicas={k: dict(ordenes=v['ordenes'], rellenos=v['rellenos']) for k, v in cov['jobs'].items()}), cov

def run_K(d):
    import b_policy_sim as BS, eng_v5 as EV, sec7_core as C, variantes_b as VB
    tp = t_proc()
    cortes = K5.lee_cortes(); f5b = pd.read_pickle(OUT + f'rf5_f5_0_{d}.pkl'); f5b0 = f5b[f5b.bloq == 0]; vs = K5.lados_a_vetar_inversion(f5b0, _veto_f3_por_celda(f5b0, cortes))
    bsrc = FB.carga_binance(d)
    if not bsrc: raise RuntimeError('DATA_BLOCKED: sin m5_registro Binance (ETH/SOL/XRP) para V5/V6 en %s' % d)
    E, info = EV.build(d); P = BS.params(); Rs = []; cov = dict(motor=info, t_proc_ms=tp, jobs={}, binance_coins=sorted(bsrc), conjuntos_exclusivos=None)
    for bloq in (0, 1):
        W = C.EngineBloqueo(E, activo=bool(bloq)); ctx = dict(W=W, serie=W._serie)
        for nombre in K5.POLITICAS_K:
            if bloq == 1 and nombre not in K5.BLOQ1_SOLO: continue
            R, c, HK = _replay(d, P, W, ctx, nombre, K5.POLITICAS_K, bsrc, cortes, tp, vs if nombre.startswith('INV_') else None)
            if len(R): Rs.append(_col(R, bloq))
            cov['jobs'][f'bloq{bloq}/{nombre}'] = dict(ordenes=int(len(R)), rellenos=int((R.q > 0).sum()) if len(R) else 0, contadores=dict(HK.cont), quien_cancela=pd.Series(list(HK.quien.values())).value_counts().to_dict() if HK.quien else {}, saltados=c.get('skip'))
        if bloq == 0:                                                   # conjuntos exclusivos (descriptivo): flags de V5/V6 en las ordenes de la BASE (mismas funciones que HookRF5)
            Rb = pd.read_pickle(OUT + f'rf5A_{d}.pkl'); Rb = Rb[(Rb.bloq == 0) & (Rb.pol == 'base')]; J = {c_: {n: VB.saltos(*bsrc[c_], v) for n, v in (('V5', VB.V5), ('V6', VB.V6))} for c_ in bsrc}; fl = {}
            f5set = {(r.mid, r.lado): K5.veta_f5('F3', r.coin, (None if not np.isfinite(r.f5_0) else r.f5_0), cortes) for r in f5b0.itertuples()}
            for o in Rb.itertuples():
                key = (o.mid, o.lado); f = fl.setdefault(key, dict(mid=o.mid, lado=o.lado, f5=bool(f5set.get(key, False)), v5=False, v6=False))
                if o.coin not in J: continue
                for n, var in (('V5', VB.V5), ('V6', VB.V6)):
                    adv = VB.adverso(J[o.coin][n], o.lado); f[n.lower()] |= bool(VB.no_armar(adv, int(o.t_dec), var))
            cov['conjuntos_exclusivos'] = K5.conjuntos_exclusivos(Rb.reset_index(drop=True), pd.DataFrame(list(fl.values()))).to_dict('records') if fl else []
    atomic_pkl(OUT + f'rf5K_{d}.pkl', pd.concat(Rs, ignore_index=True))
    return dict(etiqueta='CONTEOS; sin EV', politicas={k: dict(ordenes=v['ordenes'], rellenos=v['rellenos']) for k, v in cov['jobs'].items()}), cov

def procesa_dia(d):
    """Devuelve el estado del dia y escribe manifest_rf5dia_D.json. INCOMPLETE es terminal (no se reevalua)."""
    prev = lee_dia(d)
    if prev and prev.get('status') == 'INCOMPLETE': log('INCOMPLETE terminal', d, prev.get('motivo')); return 'INCOMPLETE'
    base = dict(job=f'rf5 dia {d}', measurement_id='RF5E-COMB-23NOV-v1', dia=d, t_ini=ts(), primer_visto=((prev or {}).get('primer_visto') or ts()), code=code_hashes())
    P0R.sha_prereg()                                       # ValueError => el llamador sale 3 (fail-closed)
    prob = verifica_registro()
    if prob: atomic_json(dia_mpath(d), dict(base, status='BLOCKED', motivo=prob, t_fin=ts())); log('BLOCKED registro', prob); return 'BLOCKED'
    cov = P0R.cobertura_tx(d); fuentes = estado_fuentes(d); faltan_tape = [x for x, v in cov['dias'].items() if v.get('motivo') == 'sin tape']
    if faltan_tape:                                        # cinta no producida (o fuente aun no extraida): recuperable <=48 h; mas viejo y sin fuente => perdido (terminal)
        perdido = [x for x in faltan_tape if not fuentes.get(x) and x < dmas(hoy(), -2)]
        st, mot = ('INCOMPLETE', f'fuente sa_ms perdida/ausente para {perdido}') if perdido else ('PENDING', f'sin cinta para {faltan_tape} (fuentes sa_ms: {fuentes})')
        atomic_json(dia_mpath(d), dict(base, status=st, motivo=mot, cobertura_tx=cov, t_fin=ts())); log(st, d, mot); return st
    mot = P0R.incompleto(d, cov, None)
    if mot: atomic_json(dia_mpath(d), dict(base, status='INCOMPLETE', motivo=mot, cobertura_tx=cov, t_fin=ts())); log('INCOMPLETE', d, mot); return 'INCOMPLETE'
    m2 = asegura_ms2(d)
    if m2 != 'OK':
        st, mot = ('INCOMPLETE', 'sa_ms2 sin raw maker_ms (fuente perdida)') if (m2 == 'SIN_RAW' and d < dmas(hoy(), -2)) else (('PENDING', 'sa_ms2: raw maker_ms del dia aun no cerrado') if m2 == 'SIN_RAW' else ('FAILED', 'ms_extract_v2 fallo'))
        atomic_json(dia_mpath(d), dict(base, status=st, motivo=mot, cobertura_tx=cov, t_fin=ts())); log(st, d, mot); return st
    btc = cobertura_btc(d); cortes = K5.lee_cortes(); st_j = {}
    needs = dict(RU.inputs_dia(d), ms2=SA2 + f'ms2_{d}.npz')
    st_j['A'] = RU.job('rf5A', d, [f'rf5A_{d}.pkl', f'rf5_f5_0_{d}.pkl'], run_A, needs)
    if st_j['A'] == 'COMPLETE':
        if t_proc() is None:
            atomic_json(RU.mpath('rf5K', d), dict(job=f'rf5K {d}', status='BLOCKED', motivo='BLOCKED_T_PROC: falta RF5_T_PROC_MS / rf5_t_proc_ms.txt (sin default)', t_fin=ts())); st_j['K'] = 'BLOCKED'
        else: st_j['K'] = RU.job('rf5K', d, [f'rf5K_{d}.pkl'], run_K, dict(needs, m5=FB.M5 % d))
    ma = json.load(open(RU.mpath('rf5A', d))) if os.path.exists(RU.mpath('rf5A', d)) else {}; den = ((ma.get('cobertura') or {}).get('desenlace') or {})
    frac = None if not den.get('mercados') else 1 - den.get('sin_desenlace', 0) / (den['mercados'] + den.get('sin_desenlace', 0))
    suelo = 'PENDIENTE_TABLA_SUELO_SUCESORA' if not cortes.get('tabla_suelo_sucesora') else 'OK'
    ok = st_j.get('A') == 'COMPLETE' and st_j.get('K') == 'COMPLETE'
    st = 'COMPLETE' if ok else ('PENDING' if st_j.get('K') == 'BLOCKED' and st_j.get('A') == 'COMPLETE' else ('BLOCKED' if 'BLOCKED' in st_j.values() else 'FAILED'))
    atomic_json(dia_mpath(d), dict(base, status=st, jobs=st_j, cobertura_tx=cov, btc=btc, desenlace_frac=frac, criterio_iv_ok=(None if frac is None else frac >= 0.80), criterio_iii_suelo=suelo,
                                   motivo=('BLOCKED_T_PROC (K pendiente)' if st == 'PENDING' else None), t_fin=ts(),
                                   repro=f'cd {HV} && python3 rf5_run.py dia {d}'))
    log('DIA', d, st, st_j); return st

def estado():
    out = {}
    for f in sorted(os.listdir(OUT)):
        if f.startswith('manifest_rf5dia_'):
            m = json.load(open(OUT + f)); out[m['dia']] = dict(status=m['status'], motivo=m.get('motivo'), t_fin=m.get('t_fin'), jobs=m.get('jobs'), btc=(m.get('btc') or {}).get('estado'), iv=m.get('criterio_iv_ok'), iii=m.get('criterio_iii_suelo'))
    return out

if __name__ == '__main__':
    modo = sys.argv[1] if len(sys.argv) > 1 else ''
    if modo == 'estado': print(json.dumps(estado(), indent=1, default=str)); sys.exit(0)
    if modo != 'dia' or len(sys.argv) < 3: raise SystemExit(__doc__)
    rc = 0
    for d in sys.argv[2:]:
        try: r = procesa_dia(d)
        except ValueError as ex: print('BLOQUEADO (fail-closed): prereg/adendas no cuadran:', ex); sys.exit(3)
        except Exception as ex:
            import traceback; traceback.print_exc(); atomic_json(dia_mpath(d), dict(job=f'rf5 dia {d}', dia=d, status='FAILED', motivo=repr(ex), t_fin=ts())); r = 'FAILED'
        rc |= int(r == 'FAILED')
    sys.exit(rc)
