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
import sec7_run as RU, rf5_core as K5, rf5_gates as GT, cobertura_bruta as CB
import contextlib, rf5_huecos as HU, rf5_rapido as RP
RU.OUT = OUT
PREREG_RF5 = HV + 'PREREG_RF5_ENTRADA_23nov.md'; PREREG_RF5_SHA = '16be06b6194f8bbaf9225ba17fda56fe44a6faf5d4a0a790dfcd5340f82fac5e'
HASHES = HV + 'HASHES_rf5.txt'; FICH_REG = ('rf5_core.py', 'rf5_run.py', 'rf5_eval.py', 'rf5_cortes.json', 'prep_tapes_rf5.sh', 'run_rf5.sh', 'vigia_rf5.py', 'rf5_gates.py', 'cobertura_bruta.py', 'horas_leidas_d1.json', 'rf5_nulo.py', 'rf5_huecos.py', 'rf5_k6.py', 't_proc_cronometro.py', 'rf5_acople_real.py', 'rf5_t_proc_ms.txt',
            'rf5_rapido.py', 'rf5_rapido_prueba.py', 'calma_gate.py', 'calma_hook.py', 'rf5_k6_dia.py', 'run_k6.sh', 'rf5_nulo_run.py', 'c4_btc.py', 'reconstructor_relleno.py', 'prep_day_btc.py', 'c4_equiv_lowmem.py', 'lanza_pesado.sh', 'btc_backfill.sh', 'rf5_fronteras.py', 'rf5_nulo_inc.py', 'run_nulo_inc.sh', 'cron_nulo_inc.txt')
# v3 (adenda interina 24-Nov sec.4 cond.1): TODO lo que el runner importa o lanza FUERA de re_f5_23nov/. 'EXT:' = relativo a /root/polymarket-research/, 'DEV:' = relativo a /root/polymarket-research-dev/ (prep_day.py y su reconstructor: worktree permanente). Se comprueban al arrancar (fail-closed) y entran en el sello de codigo de cada dia.
BS_ = 'misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/'; L2_ = 'experimentos/5m_barato/l2_carrera_10nov/'
FICH_EXT = tuple('EXT:' + x for x in (BS_ + 'b_policy_sim.py', BS_ + 'ejecutor_puro.py', BS_ + 'eng_v5.py', BS_ + 'ver_todos_17nov/r1v2_eval/e1_modelo.py', BS_ + 'ver_todos_17nov/r1v2_eval/familia6.py', BS_ + 'ver_todos_17nov/r1v2_eval/fase_b_run.py', BS_ + 'ver_todos_17nov/r1v2_eval/l2_rasgos.py',
               BS_ + 'ver_todos_17nov/r1v2_eval/puerta0_core.py', BS_ + 'ver_todos_17nov/r1v2_eval/puerta0_run.py', BS_ + 'ver_todos_17nov/r1v2_eval/replay_variantes.py', BS_ + 'ver_todos_17nov/r1v2_eval/variantes_b.py', BS_ + 'ver_todos_17nov/r1v2_sec7/sec7_calculos.py',
               BS_ + 'ver_todos_17nov/r1v2_sec7/sec7_core.py', BS_ + 'ver_todos_17nov/r1v2_sec7/sec7_run.py', 'misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/suelo_causal.py', L2_ + 'engine_clock.py', L2_ + 'engine_v3.py', L2_ + 'engine_v4.py', L2_ + 'passT_v4.py', L2_ + 'relojes.py', L2_ + 'stamp_v3.py',
               L2_ + 'ms_extract_v2.py', 'experimentos/5m_barato/b_seleccion_adversa/scripts/ms_extract_lowmem.py', 'experimentos/5m_barato/b_seleccion_adversa/scripts/ms_extract.py', 'scripts/cron_pesado.sh')) + \
           tuple('DEV:' + x for x in ('misiones/5m_barato/sonda1/p2/precursores_barrido/prep_day.py', 'misiones/5m_barato/sonda1/p2/captura_prints/reconstructor_relleno.py'))
REPO_ = '/root/polymarket-research/'; DEVREPO_ = '/root/polymarket-research-dev/'
def ruta_ext(n): return (DEVREPO_ if n.startswith('DEV:') else REPO_) + n.split(':', 1)[1]
def nombre_ext(n): return os.path.relpath(ruta_ext(n), HV)       # nombre en HASHES_rf5.txt: ruta relativa a re_f5_23nov/ (asi `sha256sum -c HASHES_rf5.txt` funciona desde alli)
OPCIONALES = FICH_REG[7:]                       # todo salvo core/run/eval/cortes/prep/run/vigia: si falta el fichero no entra en el sello de codigo (el registro fail-closed lo comprueba aparte)
COLS = ['dia', 'mid', 'coin', 'k', 'lado', 'L', 'q', 'cost', 'pnl', 'gana', 'fin', 't_dec', 'n_ord', 'motivo_fin', 'canal', 'estrato', 'f5t', 'tercil', 'bloq', 'pol', 'lcancel', 'sin_res', 'hueco']
ts, log, sha, atomic_json, atomic_pkl = RU.ts, RU.log, RU.sha, RU.atomic_json, RU.atomic_pkl

def t_proc():
    """t_proc ms (tiempo de computo MEDIDO, sin default): RF5_T_PROC_MS o rf5_t_proc_ms.txt (lo fija el chief con su medicion; su sha va en HASHES_rf5.txt). None si falta."""
    v = os.environ.get('RF5_T_PROC_MS')
    if v is None and os.path.exists(HV + 'rf5_t_proc_ms.txt'): v = open(HV + 'rf5_t_proc_ms.txt').read().split()[0]
    return None if v is None else float(v)

def code_hashes():
    H = FB.code_hashes(); H['puerta0_run.py'] = sha(V + 'r1v2_eval/puerta0_run.py')
    for f in FICH_REG:
        if f in OPCIONALES and not os.path.exists(HV + f): continue
        H['rf5/' + f] = sha(HV + f)
    for n in FICH_EXT:
        if os.path.exists(ruta_ext(n)): H['ext/' + n] = sha(ruta_ext(n))
    H['PREREG_RF5'] = sha(PREREG_RF5); return H
RU.code_hashes = code_hashes

def ya_completo(modo, d, outs):
    p = RU.mpath(modo, d)
    if not os.path.exists(p): return False
    try:
        m = json.load(open(p))
        ok = m.get('status') == 'COMPLETE' and set(m.get('outputs', {})) == set(outs) and all(os.path.exists(OUT + f) and sha(OUT + f) == h for f, h in m['outputs'].items()) and m.get('code') == code_hashes()
        return bool(ok and (modo not in ('rf5K', 'rf5K6') or (m.get('cobertura') or {}).get('t_proc_ms') == t_proc()))
    except Exception: return False
RU.ya_completo = ya_completo

def verifica_registro():
    """fail-closed: HASHES_rf5.txt (formato sha256sum, escrito ANTES del 1.er dia ciego) debe cubrir cada fichero registrado y coincidir con el disco; PREREG_RF5 = sha firmado. Devuelve lista de problemas."""
    prob = []
    if sha(PREREG_RF5) != PREREG_RF5_SHA: prob.append('PREREG_RF5 sha != firmado')
    if not os.path.exists(HASHES): return prob + ['falta HASHES_rf5.txt (codigo no registrado)']
    reg = {l.split(None, 1)[1].strip(): l.split()[0] for l in open(HASHES) if l.strip() and not l.startswith('#') and len(l.split()) >= 2}
    for n in FICH_EXT:
        p = ruta_ext(n)
        if not os.path.exists(p): prob.append(f'{n} no existe (fichero externo del runner)')
        elif nombre_ext(n) not in reg: prob.append(f'{n} no registrado en HASHES_rf5.txt')
        elif reg[nombre_ext(n)] != sha(p): prob.append(f'{n} sha != HASHES_rf5.txt (cambio de codigo externo = version nueva)')
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

@contextlib.contextmanager
def desenlace_con_marcador():
    """C3 peor caso (ADENDA_RF5_CRITERIOS_v2 3b): mercados SIN desenlace oficial no se saltan; entran en la simulacion con gana=0 (marcador) => todo relleno suyo da pnl = -coste (cota de peor caso exacta) y quedan marcados sin_res. Parche local y reversible del
    capt_outcome del motor (mismo patron que test_b_real_sim.py); devuelve el conjunto de mids sin resolver."""
    import eng_v5 as EV
    global UNRES
    G = EV.G; orig = G.capt_outcome; unres = set(); UNRES = unres
    def f(E, k):
        o = orig(E, k)
        if o is None: unres.add(str(E.D.mid[k])); return 0.0
        return o
    G.capt_outcome = f
    try: yield unres
    finally: G.capt_outcome = orig; UNRES = set()

def _res_huecos(g):
    """resumen por moneda de huecos >=5 s: n y segundos totales (None = sin datos de la moneda)."""
    return {c: (None if v is None else dict(n=len(v), segundos=round(sum(b - a for a, b in v) / 1000.0, 1))) for c, v in g.items()}

def c3_lados(R, **kw):
    """lados mercado-lado con relleno (union de politicas) -> GT.evalua_c3. R con cols mid,k,coin,q,cost,sin_res."""
    X = R[R.q > 0]
    g = X.groupby(['mid', 'k'], as_index=False).agg(coin=('coin', 'first'), coste=('cost', 'max'), sin_res=('sin_res', 'first')) if len(X) else X
    c3 = GT.evalua_c3(g.assign(coin=g.coin.astype(str).str.upper()).to_dict('records') if len(g) else [], **kw); return c3

def bloques4h(R):
    """ordenes y rellenos por bloque de 4 h UTC (t_dec ms epoch; politica base, bloq 0): SOLO conteos (C1: sesgo hora-del-dia; el resultado por bloque lo emite rf5_eval con >=10 dias)."""
    X = R[(R.pol == 'base') & (R.bloq == 0)]
    if not len(X): return {}
    b = ((X.t_dec.astype('int64') // 3600000) % 24 // 4).astype(int); return {int(i) * 4: dict(ordenes=int((b == i).sum()), rellenos=int(((b == i) & (X.q > 0)).sum())) for i in sorted(b.unique())}

def construye_f5tab(hooks_f5, d, bloq, pol):
    return pd.DataFrame([dict(dia=d, bloq=bloq, pol=pol, mid=m, k=k, **v) for (m, k), v in hooks_f5.items()])

def motor(E, activo):
    """EngineBloqueo con memo de run_segment (rapido) o el original (RF5_LENTO=1)."""
    import sec7_core as C
    return C.EngineBloqueo(E, activo=activo) if os.environ.get('RF5_LENTO') else RP.EngineBloqueoCache(E, activo=activo)

def _replay(d, P, W, ctx, nombre, tabla, bsrc, cortes, tp, veto_set=None, bsrc_calma=None, ev_shift=None):
    """bsrc_calma (None => = bsrc): fuente Binance de Calma SOLA; solo el placebo de K6 del nulo la usa (series desplazadas), el resto de llamadas no cambia."""
    import replay_variantes as RV
    W.fills.clear(); HK = K5.construye_hook(nombre, tabla, W._serie, bsrc, cortes, tp, lambda: W.fills, veto_set, bsrc_calma=bsrc_calma, ev_shift=ev_shift)
    R, cov = RP.run_day(d, P, E=W, HK=HK)                    # simulador rapido (identico bit a bit a RV.run_day; RF5_LENTO=1 => lento)
    if len(R):
        import puerta0_core as P0
        R = P0.unidad_primer_relleno(FB.anota(R, ctx, d)); R = R.assign(pol=nombre, lcancel=tabla[nombre][3])
    return R, cov, HK

GAPS = {}; GAPS_BN = {}                         # huecos >=5 s por moneda del job en curso (ms del motor; Binance). Vacio => toda orden se marca hueco (fail-closed)
UNRES = set()                                   # conjunto vivo de mids sin desenlace del job en curso (lo rellena desenlace_con_marcador)
def _col(R, bloq, unres=None):
    R = R.assign(bloq=bloq, sin_res=R.mid.astype(str).isin(UNRES if unres is None else unres).values)
    R = R.assign(hueco=(HU.marca_huecos(R, GAPS) | (HU.marca_huecos(R, GAPS_BN) if GAPS_BN else False)).values)   # E5: la vida de la orden solapa un hueco >=5 s (o dato ausente => True)
    R.loc[R.sin_res, 'gana'] = np.nan                       # C3: desenlace desconocido (pnl = -coste = peor caso por el marcador 0)
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
    global GAPS, GAPS_BN
    GAPS = HU.gaps_de_motor(E); GAPS_BN = {}; cov['huecos_ms'] = _res_huecos(GAPS)
    f5x = []                                                # F5_0 medidos en las replicas VETO_UP/VETO_DN (nulo exacto): tablas aparte, no mezclan con f5s (indexado por bloq)
    with desenlace_con_marcador() as unres: _bucle_A(d, P, E, cortes, Rs, f5s, cov, base, unres, f5x)
    RA = pd.concat(Rs, ignore_index=True); cov['c3'] = c3_lados(RA); cov['por_bloque_4h'] = bloques4h(RA); cov['desenlace']['sin_desenlace_mercados'] = len(unres)
    atomic_pkl(OUT + f'rf5A_{d}.pkl', RA); atomic_pkl(OUT + f'rf5_f5_0_{d}.pkl', pd.concat(f5s + f5x, ignore_index=True))
    return dict(etiqueta='CONTEOS; sin EV', politicas={k: dict(ordenes=v['ordenes'], rellenos=v['rellenos']) for k, v in cov['jobs'].items()}), cov

def _bucle_A(d, P, E, cortes, Rs, f5s, cov, base, unres, f5x):
    import b_policy_sim as BS, sec7_core as C
    for bloq in (0, 1):
        W = motor(E, bool(bloq)); ctx = dict(W=W, serie=W._serie)
        for nombre in K5.POLITICAS_A:
            if bloq == 1 and nombre not in K5.BLOQ1_SOLO: continue
            vs = None
            if nombre == 'INV_F3': vs = K5.lados_a_vetar_inversion(f5s[0], _veto_f3_por_celda(f5s[0], cortes))
            R, c, HK = _replay(d, P, W, ctx, nombre, K5.POLITICAS_A, None, cortes, None, vs)
            if len(R): Rs.append(_col(R, bloq, unres))
            cov['jobs'][f'bloq{bloq}/{nombre}'] = dict(ordenes=int(len(R)), rellenos=int((R.q > 0).sum()) if len(R) else 0, contadores=dict(HK.cont), saltados=c.get('skip'))
            if nombre in ('VETO_UP', 'VETO_DN'): f5x.append(construye_f5tab(HK.f5_0, d, bloq, nombre))
            if nombre == 'base':
                base[bloq] = R; f5b = construye_f5tab(HK.f5_0, d, bloq, 'base'); f5s.append(f5b) if bloq == 0 else f5s.append(f5b)
                cov['desenlace'] = dict(mercados=c.get('mercados'))
            elif nombre in ('F1', 'F2', 'F3', 'U13') and len(R) and bloq in base and len(base[bloq]):
                f5ref = f5s[bloq] if len(f5s) > bloq else f5s[0]
                cov['verif_veto_postfiltro'][f'bloq{bloq}/{nombre}'] = K5.verifica_veto_postfiltro(base[bloq], R, f5ref, nombre, cortes)

def run_K(d):
    with desenlace_con_marcador() as unres:
        res, cov = _run_K(d)
    cov['c3'] = c3_lados(pd.read_pickle(OUT + f'rf5K_{d}.pkl')); cov['desenlace_sin_resolver_mercados'] = len(unres); return res, cov

def _run_K(d):
    import b_policy_sim as BS, eng_v5 as EV, sec7_core as C, variantes_b as VB
    tp = t_proc()
    cortes = K5.lee_cortes(); f5b = pd.read_pickle(OUT + f'rf5_f5_0_{d}.pkl'); f5b0 = f5b[f5b.bloq == 0]; vs = K5.lados_a_vetar_inversion(f5b0, _veto_f3_por_celda(f5b0, cortes))
    bsrc = FB.carga_binance(d)
    if not bsrc: raise RuntimeError('DATA_BLOCKED: sin m5_registro Binance (ETH/SOL/XRP) para V5/V6 en %s' % d)
    E, info = EV.build(d); P = BS.params(); Rs = []; cov = dict(motor=info, t_proc_ms=tp, jobs={}, binance_coins=sorted(bsrc), conjuntos_exclusivos=None)
    global GAPS, GAPS_BN
    GAPS = HU.gaps_de_motor(E); GAPS_BN = HU.gaps_binance(bsrc); cov['huecos_ms'] = _res_huecos(GAPS); cov['huecos_binance'] = _res_huecos(GAPS_BN)
    for bloq in (0, 1):
        W = motor(E, bool(bloq)); ctx = dict(W=W, serie=W._serie)
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

def bad_horas(x, pb=None):
    """horas malas de x (lista de ints) de bad_x.json de prep_day; None si falta/ilegible (fail-closed)."""
    try: return sorted({int(h) for dd, h in json.load(open((pb or RU.PB) + f'bad_{x}.json'))['bad'] if dd == x})
    except Exception: return None

def valida_c1(d, pb=None, cob=None):
    """C1 (ADENDA_RF5_CRITERIOS_v2 3a): cobertura SIN filtrar horas en d-1,d,d+1 + f_horas(d) + horas leidas de d-1/d+1. Devuelve (res, cb) o (None, faltan) si falta alguna fuente (PENDING/INCOMPLETE por antiguedad)."""
    dias = P0R.dias_vec(d); cb = {}; faltan = []
    for x in dias:
        r = (cob or CB.obtener)(x)
        if r is None: faltan.append(x)
        else: cb[x] = r
    if faltan: return None, faltan
    hl = GT.lee_horas_leidas(); res = GT.evalua_c1(dias, {x: dict(units=cb[x]['units'], con_tx=cb[x]['con_tx']) for x in dias}, {x: bad_horas(x, pb) for x in dias}, hl)
    res['detalle']['descriptivo'] = {x: dict(resumen=cb[x].get('resumen'), horas_malas_propias=cb[x].get('horas_malas_propias')) for x in dias}; return res, cb

def suelo_estado(d, cortes):
    """(iii): tabla de suelo sucesora (ruta+sha en rf5_cortes.json) -> estado del dia. Sin entrada para el dia => suelo_pendiente (no VALIDO)."""
    df, info = GT.lee_tabla_suelo(cortes); r = GT.suelo_dia(df, d); r['tabla'] = info; return r

def procesa_dia(d):
    """Devuelve el estado del dia y escribe manifest_rf5dia_D.json. INCOMPLETE es terminal (no se reevalua). Orden: registro/prereg -> cintas -> C1 (cobertura sin filtrar, horas) -> ms2 -> jobs A/K (con desenlace de marcador) -> C3 -> suelo."""
    prev = lee_dia(d)
    if prev and prev.get('status') == 'INCOMPLETE': log('INCOMPLETE terminal', d, prev.get('motivo')); return 'INCOMPLETE'
    base = dict(job=f'rf5 dia {d}', measurement_id='RF5E-COMB-23NOV-v1', dia=d, t_ini=ts(), primer_visto=((prev or {}).get('primer_visto') or ts()), code=code_hashes())
    P0R.sha_prereg()                                       # ValueError => el llamador sale 3 (fail-closed)
    prob = verifica_registro()
    if prob: atomic_json(dia_mpath(d), dict(base, status='BLOCKED', motivo=prob, t_fin=ts())); log('BLOCKED registro', prob); return 'BLOCKED'
    fuentes = estado_fuentes(d); faltan_tape = [x for x in P0R.dias_vec(d) if not (os.path.exists(RU.PB + f'tape_{x}.pkl') and os.path.exists(RU.PB + f'bad_{x}.json'))]
    if faltan_tape:                                        # cinta no producida (o fuente aun no extraida): recuperable <=48 h; mas viejo y sin fuente => perdido (terminal)
        perdido = [x for x in faltan_tape if not fuentes.get(x) and x < dmas(hoy(), -2)]
        st, mot = ('INCOMPLETE', f'fuente sa_ms perdida/ausente para {perdido}') if perdido else ('PENDING', f'sin cinta para {faltan_tape} (fuentes sa_ms: {fuentes})')
        atomic_json(dia_mpath(d), dict(base, status=st, motivo=mot, t_fin=ts())); log(st, d, mot); return st
    c1, cb = valida_c1(d)                                  # (i) sobre TODAS las unidades sin filtrar horas
    if c1 is None:
        st, mot = ('INCOMPLETE', f'sin fuente de cobertura bruta (sa_ms/on-chain) para {cb}') if any(x < dmas(hoy(), -2) for x in cb) else ('PENDING', f'cobertura bruta aun no calculable para {cb}')
        atomic_json(dia_mpath(d), dict(base, status=st, motivo=mot, t_fin=ts())); log(st, d, mot); return st
    if not c1['ok']: atomic_json(dia_mpath(d), dict(base, status='INCOMPLETE', motivo=c1['motivos'], c1=c1, t_fin=ts())); log('INCOMPLETE C1', d, c1['motivos']); return 'INCOMPLETE'
    mot = P0R.incompleto(d, dict(ok=True, dias={}), None)   # solo sha de tape/bad contra TAPES_SHA256_ciegos.txt (la cobertura ya la hizo C1)
    if mot: atomic_json(dia_mpath(d), dict(base, status='INCOMPLETE', motivo=mot, c1=c1, t_fin=ts())); log('INCOMPLETE', d, mot); return 'INCOMPLETE'
    m2 = asegura_ms2(d)
    if m2 != 'OK':
        st, mot = ('INCOMPLETE', 'sa_ms2 sin raw maker_ms (fuente perdida)') if (m2 == 'SIN_RAW' and d < dmas(hoy(), -2)) else (('PENDING', 'sa_ms2: raw maker_ms del dia aun no cerrado') if m2 == 'SIN_RAW' else ('FAILED', 'ms_extract_v2 fallo'))
        atomic_json(dia_mpath(d), dict(base, status=st, motivo=mot, c1=c1, t_fin=ts())); log(st, d, mot); return st
    btc = cobertura_btc(d); cortes = K5.lee_cortes(); st_j = {}
    if prev and prev.get('c3_estado') == 'PENDIENTE':      # el desenlace pendiente pudo resolverse: re-simular (los desenlaces cambian la simulacion)
        for modo in ('rf5A', 'rf5K'):
            if os.path.exists(RU.mpath(modo, d)): os.replace(RU.mpath(modo, d), RU.mpath(modo, d) + '.pre_c3_' + time.strftime('%Y%m%dT%H%M%S', time.gmtime()))
    needs = dict(RU.inputs_dia(d), ms2=SA2 + f'ms2_{d}.npz')
    st_j['A'] = RU.job('rf5A', d, [f'rf5A_{d}.pkl', f'rf5_f5_0_{d}.pkl'], run_A, needs)
    if st_j['A'] == 'COMPLETE':
        if t_proc() is None:
            atomic_json(RU.mpath('rf5K', d), dict(job=f'rf5K {d}', status='BLOCKED', motivo='BLOCKED_T_PROC: falta RF5_T_PROC_MS / rf5_t_proc_ms.txt (sin default)', t_fin=ts())); st_j['K'] = 'BLOCKED'
        else: st_j['K'] = RU.job('rf5K', d, [f'rf5K_{d}.pkl'], run_K, dict(needs, m5=FB.M5 % d))
    c3 = c3s = None
    if st_j.get('A') == 'COMPLETE':                        # C3 sobre las coberturas de cada job; el peor de los dos manda
        ca = (json.load(open(RU.mpath('rf5A', d))).get('cobertura') or {}).get('c3'); ck = (json.load(open(RU.mpath('rf5K', d))).get('cobertura') or {}).get('c3') if st_j.get('K') == 'COMPLETE' else None
        c3s = [x for x in (ca, ck) if x]; c3 = 'OK' if (c3s and all(x['estado'] == 'OK' for x in c3s)) else 'PENDIENTE'
    try: su = suelo_estado(d, cortes)
    except ValueError as ex: su = dict(estado='BLOQUEADO_TABLA', motivo=str(ex), por_moneda={}, tabla=None)
    suelo = 'OK' if su['estado'] == 'OK' else ('PENDIENTE_TABLA_SUELO_SUCESORA' if su['estado'] in ('suelo_pendiente', 'BLOQUEADO_TABLA') else su['estado'])
    ok = st_j.get('A') == 'COMPLETE' and st_j.get('K') == 'COMPLETE'
    st = 'COMPLETE' if ok else ('PENDING' if st_j.get('K') == 'BLOCKED' and st_j.get('A') == 'COMPLETE' else ('BLOCKED' if 'BLOCKED' in st_j.values() else 'FAILED'))
    motivo = ('BLOCKED_T_PROC (K pendiente)' if st == 'PENDING' else None)
    if st == 'COMPLETE' and c3 == 'PENDIENTE':
        if GT.terminal_c3(d, hoy(), dmas): st, motivo = 'INCOMPLETE', 'C3: desenlace oficial < 0,99 en alguna moneda al llegar D+3 (terminal)'
        else: st, motivo = 'PENDING', 'C3: desenlace oficial pendiente (se reintenta hasta D+3)'
    atomic_json(dia_mpath(d), dict(base, status=st, jobs=st_j, c1=c1, c3_estado=c3, c3=c3s, btc=btc, criterio_iv_ok=(None if c3 is None else c3 == 'OK'), criterio_iii_suelo=suelo, suelo=su,
                                   motivo=motivo, t_fin=ts(), t_proc_ms=t_proc(), repro=f'cd {HV} && python3 rf5_run.py dia {d}'))
    log('DIA', d, st, st_j); return st

def estado():
    out = {}
    for f in sorted(os.listdir(OUT)):
        if f.startswith('manifest_rf5dia_') and f.endswith('.json'):
            m = json.load(open(OUT + f)); out[m['dia']] = dict(status=m['status'], motivo=m.get('motivo'), t_fin=m.get('t_fin'), jobs=m.get('jobs'), btc=(m.get('btc') or {}).get('estado'), iv=m.get('criterio_iv_ok'), iii=m.get('criterio_iii_suelo'), c3=m.get('c3_estado'))
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
