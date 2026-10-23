#!/usr/bin/env python3
"""e1b_diario.py -- extraccion diaria IDEMPOTENTE de los dias FORWARD de E1b (PREREG_E1b_CONFIRMACION_S1.md, dias >= 2026-10-23).
Solo lectura de produccion: registro ms (archivo m5_registro/m15_registro del volumen, o maker_ms_D_*.csv.gz crudo si el archivo falta),
GET publico de gamma. No toca B, procesos, config ni ordenes. Heavy -> lanzar con nice -n 19 ionice -c3 y ulimit -v 3000000 (e1b_cron.sh).

Uso:  e1b_diario.py run [--dias D ...] [--fwd0 2026-10-23] [--hasta D]   (por defecto: fwd0..ayer UTC)
Por dia D (manifest datalogs/e1b/dias/D.json, escritura atomica):
  1 extract  : e1b/extraer_e1b.py (copia de salida/scripts/extraer.py + tev; el original no se toca) con OUT -> E1B/ms_D.npz (tmp + rename)
  2 desenlaces: oficial gamma closed=true (outcomePrices>0,99) de los mercados 5m ETH/SOL/XRP del dia que no esten en
               maker_ms_desenlaces_cache.json -> E1B/desenlaces_extra.json (fusion atomica); cobertura contada
  3 sim      : scripts/e1_sim.py (congelado, sha en HASHES_E1.txt, SIN cambios de parametros) con msdata.DD y OUT -> E1B ->
               e1_D.csv.gz ; ademas aux_D.csv.gz (bid15 mismo lado - obj en r-100 ms, para R2-falso) y breal_D.csv.gz (B real, descriptivo)
  4 validar  : claves (mid,var) unicas, BASE>0, cobertura; estado COMPLETE | PARTIAL | BLOCKED | FAILED
Reanudar = relanzar: cada etapa se salta si su salida existe y su registro en el manifest coincide (sha de entradas/codigo).
Estados: COMPLETE (todo + cobertura >= 80 % de los 864 esperados con desenlace), PARTIAL (etapas hechas pero cobertura <80 % o desenlaces pendientes
-> se reintenta en la siguiente ejecucion), BLOCKED (fuentes ausentes/corruptas: nada que hacer), FAILED (excepcion)."""
import sys, os, json, glob, gzip, time, hashlib, subprocess, datetime, tempfile, math, traceback, argparse
import numpy as np, pandas as pd

AQUI = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.abspath(os.path.join(AQUI, '..'))
SAL = os.path.abspath(os.path.join(PLAN, '..', 'salida', 'scripts'))
E1B = os.environ.get('E1B_DIR', '/root/polymarket-research-datalogs/e1b/').rstrip('/') + '/'
SRC_VOL = os.environ.get('E1B_SRC_VOL', '/mnt/HC_Volume_106538179/').rstrip('/') + '/'
SRC_DL = os.environ.get('E1B_SRC_DL', '/root/polymarket-research-datalogs/').rstrip('/') + '/'
CACHE_DES = os.environ.get('E1B_CACHE_DES', SRC_DL + 'maker_ms_desenlaces_cache.json')
FWD0 = '2026-10-23'
ESPERADOS = 864          # 3 monedas x 288 ventanas de 5 min por dia UTC
COBERTURA_MIN = 0.80     # PREREG E1b: dia valido
KEEP_NPZ_DIAS = 8        # retencion de los npz (60-80 MB); e1_D/aux/breal/manifest se conservan siempre
COINS = ('ETH', 'SOL', 'XRP')
CODE = {'e1b_diario.py': os.path.join(AQUI, 'e1b_diario.py'), 'extraer_e1b.py': os.path.join(AQUI, 'extraer_e1b.py'), 'e1b_sim_ext.py': os.path.join(AQUI, 'e1b_sim_ext.py'), 'msdata.py': os.path.join(SAL, 'msdata.py'),
        'e1_sim.py': os.path.join(PLAN, 'scripts', 'e1_sim.py')}


def sha(path, n=None):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 22), b''): h.update(b)
    return h.hexdigest() if n is None else h.hexdigest()[:n]


def now(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def log(*a): print(now(), *a, flush=True)


def atomic_json(path, obj):
    tmp = f'{path}.tmp.{os.getpid()}'
    with open(tmp, 'w') as f: json.dump(obj, f, indent=1, sort_keys=True, default=str); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)


def load_json(path, default):
    """JSON corrupto -> se devuelve default y se renombra a .corrupto (nunca se pisa en silencio)"""
    if not os.path.exists(path): return default
    try: return json.load(open(path))
    except Exception:
        os.replace(path, f'{path}.corrupto.{int(time.time())}'); log('AVISO json corrupto apartado:', path); return default


def code_hashes(): return {k: sha(v, 16) for k, v in CODE.items()}


# ---------------------------------------------------------------- fuentes
def fuentes(d):
    """-> (tipo, ficheros) ; 'archivo' = m5_registro+m15_registro del volumen (preferido, 60 d) ; 'crudo' = maker_ms_D_*.csv.gz ; ('none', [])"""
    a = SRC_VOL + f'm5_registro/m5_registro_{d}.csv.gz'; b = SRC_VOL + f'm15_registro/m15_registro_{d}.csv.gz'
    if os.path.exists(a) and os.path.exists(b): return 'archivo', [a, b]
    raw = sorted(glob.glob(SRC_DL + f'maker_ms_{d}_*.csv.gz'))
    return ('crudo', raw) if raw else ('none', [])


def gzip_ok(path):
    return subprocess.run(['gzip', '-t', path], stderr=subprocess.DEVNULL).returncode == 0


def firma_fuentes(files):
    return [{'f': f, 'size': os.path.getsize(f), 'mtime': int(os.path.getmtime(f)), 'sha256': sha(f)} for f in files]


# ---------------------------------------------------------------- etapas hijas (procesos aparte para acotar la RAM)
def child_extract(d):
    sys.path.insert(0, AQUI); import extraer_e1b as extraer      # copia de extraer.py que ademas guarda tev (qd, td); resto de arrays identico (test)
    extraer.VOL = SRC_VOL; extraer.DL = SRC_DL
    tmpd = tempfile.mkdtemp(prefix=f'ext_{d}_', dir=E1B); extraer.OUT = tmpd
    extraer.day(d)
    src = os.path.join(tmpd, f'ms_{d}.npz')
    if not os.path.exists(src): raise RuntimeError('extraer no produjo npz')
    os.replace(src, E1B + f'ms_{d}.npz'); os.rmdir(tmpd)


def lvl15_aux(Dia, d):
    """bid15 del mismo lado - obj en r-100 ms para cada relleno BASE del dia (definicion de e1_posthoc.py)."""
    X = pd.read_csv(E1B + f'e1_{d}.csv.gz'); B = X[(X['var'] == 'BASE') & (X.fill == 1)]
    D = Dia(d); out = []
    for u in B.itertuples():
        f15 = int(math.ceil(u.fin / 900.0) * 900); k = D.tok(u.act, '15min', f15, 'YES' if u.yes else 'NO')
        q = D.top(k, int(u.r) - 100) if k is not None else None
        v = (q[0] - u.obj) if (q and q[0] == q[0] and q[0] > 0 and not (q[1] == q[1] and q[0] >= q[1])) else np.nan
        out.append((u.mid, v))
    return pd.DataFrame(out, columns=['mid', 'lvl15'])


def breal_aux(Dia, SYM, d, unidades):
    """DESCRIPTIVO: rellenos reales de B del dia con/sin senal S1 antes del print (e1_posthoc.py §4). Missing = sin print en WS."""
    U = pd.read_csv(unidades); U = U[U.t_det.notna() & (U.dia == d)]
    if not len(U): return pd.DataFrame(columns=['gana', 'coste', 'pnl', 'coin', 'dia', 'flag'])
    D = Dia(d); rows = []
    for u in U.itertuples():
        fin5 = int(u.mercado.split('-')[-1]) + 300; lado = 'YES' if u.outcome == 'Up' else 'NO'
        own = D.tok(u.coin, '5min', fin5, lado); opp = D.tok(u.coin, '5min', fin5, 'NO' if lado == 'YES' else 'YES')
        td = int(u.t_det * 1000); pr = None
        for k, isown in ((own, True), (opp, False)):
            if k is None: continue
            r, v = D.trades(k, td - 5000, td)
            for rr, (p, sd, sz) in zip(r, v):
                if (isown and sd == 0 and p <= u.p_fill + 1e-6) or ((not isown) and sd == 1 and p >= 1 - u.p_fill - 1e-6):
                    pr = int(rr) if pr is None else min(pr, int(rr))
        base = dict(gana=u.gana, coste=u.coste, pnl=u.payout - u.coste, coin=u.coin, dia=d)
        if pr is None: rows.append({**base, 'flag': np.nan}); continue
        sym = SYM[u.coin]; a, b_ = D.xs[sym], D.xs[sym + 1]; xr = D.xr[a:b_]; xv = D.xv[a:b_].astype(float); sg = 1 if lado == 'YES' else -1
        i0, i1 = np.searchsorted(xr, pr - 2068 - 2000), np.searchsorted(xr, pr - 100, 'right')
        rr = xr[i0:i1]; vv = xv[i0:i1]; flag = 0
        if len(rr) > 1:
            j = np.searchsorted(rr, rr - 2000, 'right') - 1; ok = (j >= 0) & (rr >= pr - 2068)
            ret = np.where(ok, (vv / vv[np.clip(j, 0, None)] - 1) * 1e4 * sg, 0); flag = int((ret <= -2).any())
        rows.append({**base, 'flag': flag})
    return pd.DataFrame(rows)


def child_sim(d):
    """e1_sim congelado con DD/OUT redirigidos a E1B. Luego aux y breal."""
    sys.path.insert(0, SAL); import msdata
    msdata.DD = E1B                                  # Dia() lee E1B/ms_D.npz ; e1_sim lee E1B/desenlaces_extra.json
    sys.path.insert(0, os.path.join(PLAN, 'scripts')); sys.path.insert(0, AQUI); import e1_sim
    e1_sim.des.update(load_json(CACHE_DES, {}))     # e1_sim fija la ruta del cache; aqui se respeta CACHE_DES (identico en produccion)
    tmpd = tempfile.mkdtemp(prefix=f'sim_{d}_', dir=E1B); e1_sim.OUT = tmpd
    e1_sim.day(d)
    import e1b_sim_ext                                 # extras del ADDENDUM (A4 X50, controles 250 ms, A5 C1/C2); no toca la salida de e1_sim
    e1b_sim_ext.day(d, tmpd)
    os.replace(os.path.join(tmpd, f'e1x_{d}.csv.gz'), E1B + f'e1x_{d}.csv.gz')
    os.replace(os.path.join(tmpd, f'e1_{d}.csv.gz'), E1B + f'e1_{d}.csv.gz'); os.rmdir(tmpd)
    aux = lvl15_aux(msdata.Dia, d); tmp = E1B + f'aux_{d}.csv.gz.tmp'; aux.to_csv(tmp, index=False, compression='gzip'); os.replace(tmp, E1B + f'aux_{d}.csv.gz')
    ub = E1B + 'unidades_b.csv' if os.path.exists(E1B + 'unidades_b.csv') else os.path.join(SAL, '..', 'datos', 'unidades_b.csv')
    br = breal_aux(msdata.Dia, msdata.SYM, d, ub) if os.path.exists(ub) else pd.DataFrame(columns=['gana', 'coste', 'pnl', 'coin', 'dia', 'flag'])
    tmp = E1B + f'breal_{d}.csv.gz.tmp'; br.to_csv(tmp, index=False, compression='gzip'); os.replace(tmp, E1B + f'breal_{d}.csv.gz')


# ---------------------------------------------------------------- desenlaces + cobertura
def mercados_5m(d):
    """mercados 5m ETH/SOL/XRP del npz con fin dentro del dia UTC d (lo que cuenta como 'esperado' son 864)."""
    z = np.load(E1B + f'ms_{d}.npz', allow_pickle=False); lo = pd.Timestamp(d, tz='UTC').timestamp(); hi = lo + 86400
    M = {}
    for act, marco, mid, fin, lado in z['tmap']:
        if str(marco) != '5min' or str(act) not in COINS: continue
        fe = pd.Timestamp(str(fin)).timestamp()
        M[str(mid)] = (str(act), fe)
    return M, lo, hi


def resolver_desenlaces(d, sess=None):
    """Completa E1B/desenlaces_extra.json con los desenlaces oficiales que falten (mercados cerrados hace >10 min). Devuelve cobertura."""
    M, lo, hi = mercados_5m(d)
    des = load_json(CACHE_DES, {}); fx = E1B + 'desenlaces_extra.json'; ex = load_json(fx, {})
    ahora = time.time(); pend = sorted(m for m, (a, fe) in M.items() if m not in des and m not in ex and fe < ahora - 600)
    log(d, 'desenlaces: mercados 5m en npz', len(M), 'pendientes de resolver', len(pend))
    if pend:
        import requests
        ses = sess or requests.Session(); ok = 0; errs = 0
        for i in range(0, len(pend), 40):
            lote = pend[i:i + 40]
            try: r = ses.get('https://gamma-api.polymarket.com/markets', params=[('id', x) for x in lote] + [('closed', 'true'), ('limit', '40')], timeout=25).json()
            except Exception as e: errs += 1; log('gamma err', repr(e)[:120]); time.sleep(2); continue
            for m in r:
                pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
                if pr and len(pr) == 2 and m.get('umaResolutionStatus', 'resolved') in ('resolved', None, ''):
                    a, b = float(pr[0]), float(pr[1])
                    if a > 0.99: ex[str(m['id'])] = 'YES'; ok += 1
                    elif b > 0.99: ex[str(m['id'])] = 'NO'; ok += 1
            time.sleep(0.3)
        atomic_json(fx, ex); log(d, 'desenlaces resueltos', ok, 'errores de red', errs)
    dia_m = {m: v for m, v in M.items() if lo < v[1] <= hi}
    con = {m for m in dia_m if m in des or m in ex}
    por_coin = {c: {'recibidos': sum(1 for v in dia_m.values() if v[0] == c), 'con_desenlace': sum(1 for m in con if dia_m[m][0] == c)} for c in COINS}
    horas = {}
    for m, (a, fe) in dia_m.items():
        h = int((fe - lo) // 3600); horas.setdefault(h, [0, 0]); horas[h][0] += 1; horas[h][1] += m in con
    return {'esperados': ESPERADOS, 'recibidos_dia': len(dia_m), 'con_desenlace': len(con), 'sin_desenlace': len(dia_m) - len(con),
            'faltan_en_registro': ESPERADOS - len(dia_m), 'cobertura': len(con) / ESPERADOS, 'por_moneda': por_coin,
            'horas_con_algun_hueco': {str(h): {'recibidos': v[0], 'con_desenlace': v[1]} for h, v in sorted(horas.items()) if v[0] < 36 or v[1] < v[0]},
            'markets_fuera_de_dia_en_npz': len(M) - len(dia_m)}


# ---------------------------------------------------------------- validacion
def validar_sim(d):
    X = pd.read_csv(E1B + f'e1_{d}.csv.gz'); dup = int(X.duplicated(['mid', 'var']).sum()); B = X[X['var'] == 'BASE']
    Y = pd.read_csv(E1B + f'e1x_{d}.csv.gz'); dupx = int(Y.duplicated(['mid', 'var']).sum()); yb = Y.drop_duplicates('mid').set_index('mid').n_cand
    ncand_ok = bool((yb == B.set_index('mid').n_cand.reindex(yb.index)).all()) and set(Y.mid) <= set(B.mid)
    return {'filas': len(X), 'mercados_base': len(B), 'rellenos_base': int(B.fill.sum()), 'duplicados_mid_var': dup, 'variantes': int(X['var'].nunique()),
            'extras_filas': len(Y), 'extras_variantes': int(Y['var'].nunique()), 'extras_duplicados': dupx, 'extras_ncand_igual_base': ncand_ok,
            'ok': dup == 0 and dupx == 0 and ncand_ok and len(B) > 0 and X['var'].nunique() == 1 + 7 * 12, 'nota': 'variantes esperadas 1+7*(D100,D250,D0,INV,8 SH)=85'}


# ---------------------------------------------------------------- orquestacion de un dia
def correr_dia(d):
    os.makedirs(E1B + 'dias', exist_ok=True)
    mf = E1B + f'dias/{d}.json'; M = load_json(mf, {}); ch = code_hashes()
    M.setdefault('dia', d); M['inicio'] = M.get('inicio') or now(); M['ultima_ejecucion'] = now(); M['codigo'] = ch
    M.setdefault('etapas', {})
    hoy = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
    if d >= hoy: M['estado'] = 'BLOCKED'; M['motivo'] = 'dia no terminado'; atomic_json(mf, M); return M
    try:
        tipo, files = fuentes(d)
        if tipo == 'none': M['estado'] = 'BLOCKED'; M['motivo'] = 'sin fuentes (archivo ni crudo): irrecuperable si ya rotaron'; atomic_json(mf, M); return M
        bad = [f for f in files if not gzip_ok(f)]
        if bad: M['estado'] = 'BLOCKED'; M['motivo'] = f'gzip corrupto/incompleto: {bad}'; atomic_json(mf, M); return M
        e = M['etapas'].get('extract', {}); npz = E1B + f'ms_{d}.npz'
        sig = [[f, os.path.getsize(f), int(os.path.getmtime(f))] for f in files]
        vigente = (os.path.exists(npz) and e.get('ok') and e.get('codigo') == [ch['extraer_e1b.py']] and e.get('fuentes_tipo') == tipo
                   and e.get('sig') == sig and e.get('npz_sha') == sha(npz, 16))
        # --- extract
        if vigente: log(d, 'extract: ya hecho (fuentes, codigo y sha del npz coinciden)')
        else:
            if os.path.exists(npz): log(d, 'extract: npz sin manifest valido o fuentes/codigo distintos: se rehace'); os.remove(npz)
            log(d, 'extract desde', tipo, files); t0 = time.time(); fs = firma_fuentes(files)
            r = subprocess.run([sys.executable, '-I', os.path.abspath(__file__), '_extract', d], stdout=sys.stdout, stderr=sys.stderr)
            if r.returncode != 0 or not os.path.exists(npz): raise RuntimeError(f'_extract rc={r.returncode}')
            z = np.load(npz, allow_pickle=False)
            M['etapas']['extract'] = {'ok': True, 'fuentes_tipo': tipo, 'fuentes': fs, 'sig': sig, 'npz_sha': sha(npz, 16), 'npz_bytes': os.path.getsize(npz), 'segundos': round(time.time() - t0),
                                      'tokens': int(len(z['tokens'])), 'q': int(len(z['qr'])), 't': int(len(z['tr'])), 'x': int(len(z['xr'])), 'codigo': [ch['extraer_e1b.py']]}
            for st in ('desenlaces', 'sim'): M['etapas'].pop(st, None)   # dependen del npz
            atomic_json(mf, M)
        # --- desenlaces (siempre se reintenta: puede haber cerrado mas mercados desde ayer)
        cov = resolver_desenlaces(d); M['etapas']['desenlaces'] = {'ok': True, **cov, 'cuando': now()}; M['cobertura'] = cov; atomic_json(mf, M)
        # --- sim: se rehace si cambia la cobertura de desenlaces (mas mercados resueltos) o el codigo
        s = M['etapas'].get('sim', {}); out = E1B + f'e1_{d}.csv.gz'
        sim_ok = (os.path.exists(out) and s.get('ok') and s.get('codigo') == [ch['e1_sim.py'], ch['e1b_sim_ext.py'], ch['msdata.py'], ch['e1b_diario.py']]
                  and s.get('con_desenlace') == cov['con_desenlace'] and os.path.exists(E1B + f'e1x_{d}.csv.gz') and os.path.exists(E1B + f'aux_{d}.csv.gz') and os.path.exists(E1B + f'breal_{d}.csv.gz'))
        if sim_ok: log(d, 'sim: ya hecha (misma cobertura de desenlaces y codigo)')
        else:
            log(d, 'sim'); t0 = time.time(); fx = E1B + 'desenlaces_extra.json'
            if not os.path.exists(fx): atomic_json(fx, {})
            r = subprocess.run([sys.executable, '-I', os.path.abspath(__file__), '_sim', d], stdout=sys.stdout, stderr=sys.stderr)
            if r.returncode != 0 or not os.path.exists(out): raise RuntimeError(f'_sim rc={r.returncode}')
            v = validar_sim(d)
            M['etapas']['sim'] = {'ok': v['ok'], 'segundos': round(time.time() - t0), 'con_desenlace': cov['con_desenlace'], 'validacion': v,
                                  'codigo': [ch['e1_sim.py'], ch['e1b_sim_ext.py'], ch['msdata.py'], ch['e1b_diario.py']], 'e1_sha': sha(out, 16)}
            atomic_json(mf, M)
        v = M['etapas']['sim']['validacion']
        if not v['ok']: M['estado'] = 'FAILED'; M['motivo'] = f'validacion e1_{d}: {v}'
        elif cov['cobertura'] < COBERTURA_MIN: M['estado'] = 'PARTIAL'; M['motivo'] = f"cobertura {cov['cobertura']:.3f} < {COBERTURA_MIN}: dia NO valido todavia (se reintenta; si falta registro es irrecuperable)"
        else: M['estado'] = 'COMPLETE'; M.pop('motivo', None)
        M['fin'] = now(); atomic_json(mf, M)
    except Exception as ex:
        M['estado'] = 'FAILED'; M['motivo'] = repr(ex)[:500]; M['traceback'] = traceback.format_exc()[-1500:]; atomic_json(mf, M); log(d, 'FAILED', repr(ex))
    return M


def retencion():
    lim = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=KEEP_NPZ_DIAS)).strftime('%Y-%m-%d'); n = 0
    for f in glob.glob(E1B + 'ms_*.npz'):
        d = os.path.basename(f)[3:13]
        if d < lim and load_json(E1B + f'dias/{d}.json', {}).get('estado') in ('COMPLETE',):
            os.remove(f); n += 1
    for f in glob.glob(E1B + 'logs/*.log'):
        if os.path.getmtime(f) < time.time() - 45 * 86400: os.remove(f)
    for pat in ('ext_*', 'sim_*'):   # tmp huerfanos de ejecuciones muertas (> 1 dia)
        for p in glob.glob(E1B + pat):
            if os.path.isdir(p) and os.path.getmtime(p) < time.time() - 86400:
                for q in glob.glob(p + '/*'): os.remove(q)
                os.rmdir(p)
    return n


def dias_objetivo(args):
    if args.dias: return sorted(args.dias)
    ayer = datetime.datetime.now(datetime.timezone.utc).date() - datetime.timedelta(days=1)
    d0 = datetime.date.fromisoformat(args.fwd0); hasta = datetime.date.fromisoformat(args.hasta) if args.hasta else ayer
    out = []; d = d0
    while d <= hasta: out.append(d.isoformat()); d += datetime.timedelta(days=1)
    return out


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == '_extract': return child_extract(sys.argv[2])
    if len(sys.argv) >= 3 and sys.argv[1] == '_sim': return child_sim(sys.argv[2])
    ap = argparse.ArgumentParser(); ap.add_argument('cmd', choices=['run']); ap.add_argument('--dias', nargs='*'); ap.add_argument('--fwd0', default=FWD0); ap.add_argument('--hasta')
    args = ap.parse_args(); os.makedirs(E1B, exist_ok=True); os.makedirs(E1B + 'runs', exist_ok=True)
    dias = dias_objetivo(args)
    # contrato: antes de nada comprobar que el preregistro no ha cambiado
    pre = PLAN + '/PREREG_E1b_CONFIRMACION_S1.md'; esperado = open(PLAN + '/PREREG_E1b_CONFIRMACION_S1.sha256').read().split()[0]
    if sha(pre) != esperado: print('PREREGISTRO E1b CAMBIADO: abortar'); return 4
    run = {'job': 'e1b_diario', 'id': f'{time.strftime("%Y%m%dT%H%M%S", time.gmtime())}_{os.getpid()}', 'inicio': now(), 'codigo': code_hashes(), 'prereg_sha256': esperado,
           'parametros': {'cobertura_min': COBERTURA_MIN, 'esperados_dia': ESPERADOS, 'keep_npz_dias': KEEP_NPZ_DIAS, 'E1B': E1B, 'SRC_VOL': SRC_VOL, 'SRC_DL': SRC_DL},
           'dias_previstos': dias, 'estado': 'RUNNING', 'comando': ' '.join(sys.argv),
           'hash_entradas_desenlaces_cache': sha(CACHE_DES, 16) if os.path.exists(CACHE_DES) else None}
    rf = E1B + f'runs/run_{run["id"]}.json'; atomic_json(rf, run); rc = 0; res = {}
    for d in dias:
        M = correr_dia(d); res[d] = M.get('estado'); log(d, M.get('estado'), M.get('motivo', ''))
        if M.get('estado') in ('FAILED',): rc = 1
    run['retencion_npz_borrados'] = retencion(); run['resultado_por_dia'] = res; run['fin'] = now()
    run['estado'] = 'FAILED' if rc else ('COMPLETE' if all(v == 'COMPLETE' for v in res.values()) else 'PARTIAL')
    # alerta con latch por FIRMA de los dias no completos (no por cifras): rc 1 = FAILED (siempre), rc 3 = firma nueva de PARTIAL/BLOCKED, 0 = sin novedad
    sig = {d: v for d, v in res.items() if v != 'COMPLETE'}; lf = E1B + 'alerta_latch.json'; prev = load_json(lf, {})
    if not rc and sig and prev.get('firma') != sig: rc = 3
    if not rc or rc == 3: atomic_json(lf, {'firma': sig, 'cuando': now()})
    atomic_json(rf, run); print(json.dumps({'run': run['id'], 'estado': run['estado'], 'dias': res, 'rc': rc})); return rc


if __name__ == '__main__': sys.exit(main())
