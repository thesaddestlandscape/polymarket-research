#!/usr/bin/env python3
"""retirada_liquidez.py -- L1b parte B (23-Oct-2026). Etiqueta PASIVA de la retirada del nivel (EXIT de S1) a tau = 150/200/250 (+300 de continuidad) ms antes de cada
print de la poblacion (E), de instantes de control (C) y de cada orden de B (BF relleno / BR sin relleno). PREREG: ../PREREG_L1b.md (parte B).
Reutiliza SIN copiar: d1_l2_motor.carga/S/best/cons_between (parser de S1) y s1_extrae.exit_u/top_is (definicion exacta de EXIT). Solo LEE el libro5 del volumen, el ledger de B y
sa_r1/gmap. Escribe SOLO en datalogs/etiquetado_pasivo_B/retirada/ (ret_DIA.csv.gz + dias/DIA.json + run_manifest) y un mk temporal que borra.
Modos:  dia DIA [--force]        extrae del libro5 el dia (mercados con APERTURA en DIA) y etiqueta  (DIA debe estar cerrado)
        backfill                 20-22 Oct con el mk ya extraido por S1 (cola_vs_cruce/mk): forward=0
        resolver                 rellena gana/pnl_h de filas sin desenlace (gamma closed=true)
        cobertura
Tiempo: reloj de RECEPCION. fee maker 0, rebate NO sumado (declarado)."""
import os, sys, io, re, json, glob, gzip, time, zlib, shutil, hashlib, subprocess, argparse, fcntl, datetime as dt
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(EXP, 'control_misma_edad', 'scripts'))
import s1_extrae as s1          # asserta sha de PREREG_S1; importa d1_l2_motor (asserta sha de PREREG_CONTROL)
M = s1.M
DL = '/root/polymarket-research-datalogs'
OUT = os.environ.get('L1B_RET_OUT', os.path.join(DL, 'etiquetado_pasivo_B', 'retirada'))
LIBRO5 = os.environ.get('L1B_LIBRO5', '/mnt/HC_Volume_106538179/libro5_ms')
TMP = os.environ.get('L1B_TMP', '/mnt/HC_Volume_106538179/tmp_l1b')
R1 = os.environ.get('L1B_R1', os.path.join(DL, 'sa_r1'))
LEDGER = os.environ.get('L1B_LEDGER', os.path.join(DL, 'experimento_h47_B_ledger.jsonl'))
FWD0 = '2026-10-23'; TAUS = (150, 200, 250, 300); RETENCION_D = 30; SEED = 20261023
STRC = ['grp', 'dia', 'act', 'mid', 'mercado', 'banda', 'oid', 'loc_metodo', 'resuelto_utc']


def log(m): print(f"[{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}] {m}", flush=True)
def ahora(): return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def utc_dia(t): return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime('%Y-%m-%d')


def bloquear():
    os.makedirs(OUT, exist_ok=True); f = open(os.path.join(OUT, '.lock'), 'w')
    try: fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError: log('otra corrida en curso (lock): salgo'); sys.exit(0)
    return f


def escribir_atomico(df, path):
    tmp = path + f'.tmp{os.getpid()}'
    with gzip.open(tmp, 'wt', newline='') as fh: df.to_csv(fh, index=False)
    with gzip.open(tmp, 'rt') as fh: n = sum(1 for _ in fh) - 1
    assert n == len(df), (n, len(df)); os.replace(tmp, path)


# ---------- mapa de tokens / desenlace ----------
def mapa_dia_gmap(D):
    """token -> (act, mid, 'YES'|'NO', fin); win[(act,mid)] -> 'Y'|'N'|None.  Mercados con APERTURA en el dia D (UTC)."""
    g = json.load(open(os.path.join(R1, f'gmap_{D}.json'))); t0 = dt.datetime.fromisoformat(D).replace(tzinfo=dt.timezone.utc).timestamp()
    tm = {}; win = {}; nm = 0
    for slug, v in g.items():
        st = int(slug.rsplit('-', 1)[1]); act = slug.split('-')[0].upper()
        if not (t0 <= st < t0 + 86400): continue
        nm += 1; mid = str(v['id'])
        for t, l in zip(v['toks'], ('YES', 'NO')): tm[t] = (act, mid, l, float(st + 300))
        win[(act, mid)] = {'YES': 'Y', 'NO': 'N'}.get(v.get('des'))
    return tm, win, nm


def extraer_mk(D, tm, mkdir):
    """libro5 del dia D -> mkdir/<ACT>_<mid>.gz (formato de p2_extract: L,B|d|T|G,...). Solo bids; tokens del dia."""
    fl = sorted(glob.glob(os.path.join(LIBRO5, f'libro5_ms_{D}_*.csv.gz')))
    if not fl: return None, []
    first = {}
    for f in fl:
        try:
            z = subprocess.run(f"zcat '{f}' 2>/dev/null | head -n 2 | tail -n 1", shell=True, capture_output=True, text=True, timeout=120).stdout.split(',')
            first[f] = int(z[1])
        except Exception: first[f] = 0
    fl = sorted(fl, key=lambda f: first[f])
    os.makedirs(mkdir, exist_ok=True); tk = os.path.join(mkdir, 'tokens.txt')
    open(tk, 'w').write('\n'.join(tm) + '\n')
    H = {}
    def fh(key):
        f = H.get(key)
        if f is None:
            if len(H) > 48: H.pop(next(iter(H))).close()
            f = gzip.open(os.path.join(mkdir, key + '.gz'), 'at', compresslevel=6); H[key] = f
        return f
    n = 0
    for f in fl:
        p = subprocess.Popen(f"zcat '{f}' 2>/dev/null | grep -a -F -f '{tk}'", shell=True, stdout=subprocess.PIPE, text=True, errors='replace', bufsize=1 << 20)
        for ln in p.stdout:
            c = ln.rstrip('\n').split(',')
            if len(c) < 8: continue
            t = c[0]; v = tm.get(c[2])
            if v is None: continue
            L = v[2][0]; key = f'{v[0]}_{v[1]}'
            if t == 'G': fh(key).write(f'{L},G,{c[6]},{c[3]}\n')
            elif t == 'd':
                if c[3] == 'B': fh(key).write(f'{L},d,{c[6]},{c[4]},{c[5]}\n')
            elif t == 'T': fh(key).write(f'{L},T,{c[6]},{c[4]},{c[3]},{c[5]}\n')
            elif t == 'B': fh(key).write(f'{L},B,{c[6]},{c[3]},\n')
            n += 1
        p.wait()
    for h in H.values(): h.close()
    return n, fl


# ---------- etiquetado ----------
def tau_cols(lvn, prn, tp, L, q, r, oth=None):
    """EXIT a u=r-tau para cada tau. ok=1 si el nivel q es el mejor bid en u y S(u-850)>=5. (ex, s0, ok) por tau. oth: funcion de talla ajena (B) o None (cinta)."""
    d = {}; any_ok = False
    for tau in TAUS:
        u = r - tau; ok = 0; ex = np.nan; s0 = 0.0
        if s1.top_is(tp, L, q, u):
            if oth is None: e, s0, ok = s1.exit_u(lvn, prn, L, q, u); ex = e if ok else np.nan
            else:
                s0 = oth(u - 850)
                if s0 >= 5:
                    c, _ = M.cons_between(prn, L, q, u - 850, u); ok = 1; ex = float((s0 - c - oth(u)) >= 0.8 * s0)
        d[f'ok{tau}'] = ok; d[f'ex{tau}'] = ex; d[f's{tau}'] = s0; any_ok |= bool(ok)
    return d, any_ok


def resultado(win, L, q, a):
    """fill hipotetico min(a,10) acciones del largo L a q (mills): coste y pnl (sin fee maker, sin rebate). win None => pnl NaN (missing)."""
    acc = min(a, 10.0); coste = acc * q / 1000.0
    if win is None: return acc, coste, np.nan, np.nan
    g = float(win == L); return acc, coste, acc * g - coste, g


def procesa_mercado(path, act, mid, fin, win, forward_dia):
    rng = np.random.default_rng(zlib.crc32(os.path.basename(path).encode()) ^ SEED)
    lvn, prn, tp, ap = M.carga(path); out = []; dia = utc_dia(fin - 300)
    ht = {'ngaps': 0}
    for (L, q), (rt, rs) in prn.items():
        bd = M.banda(q)
        if bd is None: continue
        for r, a in zip(rt, rs):
            T = fin - r / 1000
            if not (50 <= T <= 300): continue
            d, ok = tau_cols(lvn, prn, tp, L, q, r)
            if not ok: continue
            acc, co, pn, g = resultado(win, L, q, a)
            row = dict(grp='E', dia=dia, act=act, mid=mid, mercado=f'{act.lower()}-updown-5m-{int(fin - 300)}', L=L, fin=fin, r=int(r), q=q, banda=bd, T=T, a=float(a), acc_h=acc, coste_h=co, pnl_h=pn, gana_L=g, **d)
            out.append(row)
            if not d['ok300']: continue
            kk = 0
            for _ in range(40):
                if kk >= 3: break
                t = int(r + rng.integers(-60000, 60001)); Tt = fin - t / 1000
                if abs(t - r) < 4000 or not (50 <= Tt <= 300): continue
                c, n = M.cons_between(prn, L, q, t - 2000, t + 3000)
                if n > 0: continue
                if not s1.top_is(tp, L, q, t - 300): continue
                if M.S(lvn, L, q, t - 300 - 850) < 5: continue
                dc, _ = tau_cols(lvn, prn, tp, L, q, t)
                out.append(dict(grp='C', dia=dia, act=act, mid=mid, mercado=row['mercado'], L=L, fin=fin, r=t, q=q, banda=bd, T=Tt, a=float(a), pair=int(r), **dc)); kk += 1
    return out, (lvn, prn, tp)


def ordenes_b(ledger_path):
    """oid -> dict(tok, slug, coin, lado, precio, size, t_dec, tc, t_fuera, t_cancel, rel[(t_det, acc)]) a partir del ledger de B (tolera ultima linea a medias; el orden de los eventos
    de un mismo oid NO se asume: post_lat/fuera_libro pueden preceder a puja_post)."""
    O = {}; tok = {}; tcall = {}; fuera = {}; canc = {}; rel = {}
    for l in open(ledger_path):
        try: d = json.loads(l)
        except Exception: continue
        t = d.get('tipo'); oid = d.get('oid')
        if t == 'intencion_post': tok[oid] = d.get('tok')
        elif t == 'puja_post': O.setdefault(oid, dict(oid=oid, slug=d['slug'], coin=d['coin'].upper(), lado=d['lado'], precio=d['precio'], size=d['size'], t_dec=d['t_dec']))
        elif t == 'post_lat': tcall.setdefault(oid, d.get('t_call0'))
        elif t == 'fuera_libro': fuera.setdefault(oid, d['ts'])
        elif t == 'intencion_cancel': canc.setdefault(oid, d['ts'])
        elif t == 'puja_fin':
            for r in d.get('rellenos') or []: rel.setdefault(r['oid'], set()).add((float(r['t_deteccion']), float(r['acc'])))
    for oid, o in O.items(): o.update(tok=tok.get(oid), tc=tcall.get(oid), t_fuera=fuera.get(oid), t_cancel=canc.get(oid), rel=sorted(rel.get(oid, [])))
    return O


iso_ms = lambda s: int(pd.Timestamp(s).timestamp() * 1000)


def etiqueta_b(o, lvn, prn, tp, act, mid, L, fin, win):
    q = M.mills(o['precio']); size = float(o['size']); tc = int(float(o['tc']) * 1000) if o['tc'] else None
    if tc is None: return [], 'sin_t_call0'
    arr = tc + 122                       # llegada aproximada (S1 usaba t_arr del libro cuando existia)
    end_fuera = iso_ms(o['t_fuera']) if o['t_fuera'] else (iso_ms(o['t_cancel']) + 65 if o['t_cancel'] else None)
    e = lvn.get((L, q))
    def oth(t, end):
        s = M.S(lvn, L, q, t); return max(0.0, s - (size if arr <= t <= end else 0.0))
    base = dict(dia=utc_dia(fin - 300), act=act, mid=mid, mercado=o['slug'], oid=o['oid'], L=L, fin=fin, q=q, banda=M.banda(q) or '', a=size, arr=arr)
    rows = []; pr = prn.get((L, q))
    for k, (td, acc) in enumerate(sorted(o['rel'])):
        c_ = np.nan; meto = 'sin_print'
        if pr is not None:
            lo, hi = int(td * 1000) - 5000, int(td * 1000) + 300
            m = np.where((pr[0] >= lo) & (pr[0] <= hi))[0]
            if len(m):
                ex = [i for i in m if abs(pr[1][i] - acc) <= max(0.03, 0.002 * acc)]
                i = ex[-1] if ex else m[-1]; c_ = int(pr[0][i]); meto = 'acc_exacto' if ex else 'ultimo_antes_det'
        r = dict(base, grp='BF', loc_metodo=meto, t_det=td, acc_fill=acc, r=c_, idx_fill=k)
        if np.isfinite(c_):
            end = int(c_); r['edad'] = (c_ - arr) / 1000
            d, _ = tau_cols(lvn, prn, tp, L, q, c_, oth=lambda t, end=end: oth(t, end)); r.update(d)
            acc_h, co, pn, g = resultado(win, L, q, acc); r.update(acc_h=acc_h, coste_h=co, pnl_h=pn, gana_L=g)
        rows.append(r)
    if not o['rel'] and end_fuera and end_fuera - arr >= 1260:   # sin relleno: un instante uniforme (R de S1)
        rng = np.random.default_rng(zlib.crc32(o['oid'].encode()) ^ SEED); t = int(rng.integers(arr + 1200, end_fuera - 50))
        r = dict(base, grp='BR', loc_metodo='uniforme', r=t, edad=(t - arr) / 1000, end=end_fuera)
        d, _ = tau_cols(lvn, prn, tp, L, q, t, oth=lambda tt: oth(tt, end_fuera)); r.update(d); rows.append(r)
    return rows, 'ok'


def procesa_dia(D, mk, tm, win, es_fwd, ordenes):
    """mk: dir con <ACT>_<mid>.gz; tm: token->(act,mid,lado,fin); win[(act,mid)]. Devuelve (DataFrame, cobertura)."""
    t0 = dt.datetime.fromisoformat(D).replace(tzinfo=dt.timezone.utc).timestamp()
    mercados = sorted({(v[0], v[1], v[3]) for v in tm.values() if t0 <= v[3] - 300 < t0 + 86400})
    tokmk = {t: v for t, v in tm.items()}
    porB = {}
    for o in ordenes.values():
        v = tokmk.get(o['tok'])
        if v: porB.setdefault((v[0], v[1]), []).append((o, 'Y' if v[2] == 'YES' else 'N', v[3]))
    rows = []; cov = dict(mercados_esperados=len(mercados), con_libro=0, sin_libro=[], error=[], filas_E=0, filas_C=0, ordenes_b=0, ordenes_b_sin_libro=0, ordenes_b_sin_t_call0=0, sin_desenlace=0)
    for act, mid, fin in mercados:
        path = os.path.join(mk, f'{act}_{mid}.gz')
        if not os.path.exists(path): cov['sin_libro'].append(f'{act}_{mid}'); cov['ordenes_b_sin_libro'] += len(porB.get((act, mid), [])); continue
        M.FIN[(act, mid)] = fin
        try:
            r, (lvn, prn, tp) = procesa_mercado(path, act, mid, fin, win.get((act, mid)), es_fwd)
            for o, L, fin_ in porB.get((act, mid), []):
                br, st = etiqueta_b(o, lvn, prn, tp, act, mid, L, fin, win.get((act, mid)))
                if st != 'ok': cov['ordenes_b_sin_t_call0'] += 1
                r += br; cov['ordenes_b'] += 1
        except Exception as e:
            cov['error'].append(f'{act}_{mid}: {type(e).__name__}: {e}'); continue
        cov['con_libro'] += 1; rows += r
        if win.get((act, mid)) is None: cov['sin_desenlace'] += 1
    df = pd.DataFrame(rows)
    if len(df):
        df['forward'] = int(es_fwd); df['resuelto'] = (df.gana_L.notna() | df.grp.isin(['C', 'BR'])).astype(int) if 'gana_L' in df else 1
        if 'resuelto_utc' not in df: df['resuelto_utc'] = ''
        df['etiquetado_utc'] = ahora()
        cov['filas_E'] = int((df.grp == 'E').sum()); cov['filas_C'] = int((df.grp == 'C').sum())
    return df, cov


# ---------- modos ----------
def hecho(D):
    j = os.path.join(OUT, 'dias', f'{D}.json'); p = os.path.join(OUT, f'ret_{D}.csv.gz')
    if not (os.path.exists(j) and os.path.exists(p)): return False
    try:
        m = json.load(open(j)); n = pd.read_csv(p, usecols=['grp']).shape[0]
        return m.get('estado') == 'COMPLETE' and m.get('filas') == n
    except Exception: return False


def modo_dia(D, force):
    ya = utc_dia(time.time() - 86400)
    if D > ya: log(f'{D} no esta cerrado (ayer = {ya}): no se procesa'); return 2
    if hecho(D) and not force: log(f'{D} ya COMPLETE: nada que hacer'); return 0
    os.makedirs(os.path.join(OUT, 'dias'), exist_ok=True)
    if not os.path.exists(os.path.join(R1, f'gmap_{D}.json')): log(f'{D}: falta sa_r1/gmap_{D}.json (R1 aun no lo ha generado): BLOCKED'); return 3
    tm, win, nm = mapa_dia_gmap(D); mk = os.path.join(TMP, f'mk_{D}'); shutil.rmtree(mk, ignore_errors=True)
    t_ini = ahora(); n, fl = extraer_mk(D, tm, mk)
    if n is None: log(f'{D}: sin ficheros libro5 en {LIBRO5}: BLOCKED'); return 3
    log(f'{D}: libro5 {len(fl)} ficheros, {n} lineas de tokens del dia; mercados={nm}')
    ordenes = ordenes_b(LEDGER); df, cov = procesa_dia(D, mk, tm, win, D >= FWD0, ordenes); shutil.rmtree(mk, ignore_errors=True)
    estado = 'COMPLETE' if cov['con_libro'] >= 0.8 * max(1, cov['mercados_esperados']) and not cov['error'] else 'PARTIAL'
    if len(df): escribir_atomico(df, os.path.join(OUT, f'ret_{D}.csv.gz'))
    man = dict(job='l1b_retirada', dia=D, estado=estado, filas=len(df), cobertura={k: (v if not isinstance(v, list) else dict(n=len(v), muestra=v[:10])) for k, v in cov.items()},
               libro5=[dict(f=os.path.basename(f), bytes=os.path.getsize(f)) for f in fl], codigo_sha16=hashlib.sha256(open(__file__, 'rb').read()).hexdigest()[:16], ledger_bytes=os.path.getsize(LEDGER), inicio=t_ini, fin=ahora())
    json.dump(man, open(os.path.join(OUT, 'dias', f'{D}.json'), 'w'), indent=1); log(f'{D}: {estado} filas={len(df)} cov={json.dumps(man["cobertura"])[:400]}')
    return 0 if estado == 'COMPLETE' else 4


def modo_backfill():
    TM = M.TM; mkd = M.MK; os.makedirs(os.path.join(OUT, 'dias'), exist_ok=True)
    pu = pd.concat([pd.read_csv(f, usecols=['act', 'mid', 'lado', 'gana']) for f in glob.glob(os.path.join(EXP, 'cola_posicion', 'datos', 'pop_units_*.csv.gz'))]); pu['mid'] = pu.mid.astype(str)
    pu['w'] = np.where(((pu.lado == 'YES') & (pu.gana == 1)) | ((pu.lado == 'NO') & (pu.gana == 0)), 'Y', 'N'); win = {(r.act, r.mid): r.w for r in pu.drop_duplicates(['act', 'mid']).itertuples()}
    tm = {t: (v[0], str(v[1]), v[2], float(v[3])) for t, v in TM.items()}; ordenes = ordenes_b(LEDGER)
    for D in ('2026-10-20', '2026-10-21', '2026-10-22'):
        if hecho(D): log(f'{D} ya COMPLETE (backfill)'); continue
        t_ini = ahora(); df, cov = procesa_dia(D, mkd, tm, win, False, ordenes)
        estado = 'COMPLETE' if cov['con_libro'] >= 0.8 * max(1, cov['mercados_esperados']) and not cov['error'] else 'PARTIAL'
        if len(df): escribir_atomico(df, os.path.join(OUT, f'ret_{D}.csv.gz'))
        man = dict(job='l1b_retirada_backfill', dia=D, estado=estado, filas=len(df), forward=0, nota='mk de S1 (cola_vs_cruce); 22-Oct hasta ~16:15Z; desenlace de pop_units (sin resolver = missing)',
                   cobertura={k: (v if not isinstance(v, list) else dict(n=len(v), muestra=v[:10])) for k, v in cov.items()}, codigo_sha16=hashlib.sha256(open(__file__, 'rb').read()).hexdigest()[:16], inicio=t_ini, fin=ahora())
        json.dump(man, open(os.path.join(OUT, 'dias', f'{D}.json'), 'w'), indent=1); log(f'{D}: {estado} filas={len(df)} cov={json.dumps(man["cobertura"])[:300]}')
    return 0


def gamma_resultado(slugs):
    import requests
    ses = requests.Session(); res = {}
    for k in range(0, len(slugs), 20):
        try:
            r = ses.get('https://gamma-api.polymarket.com/markets', timeout=25, params=[('slug', s) for s in slugs[k:k + 20]] + [('closed', 'true'), ('limit', '40')]); r.raise_for_status()
            for m in r.json() or []:
                pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr; oc = m.get('outcomes'); oc = json.loads(oc) if isinstance(oc, str) else oc
                if pr and oc and len(pr) == 2 and oc == ['Up', 'Down']:
                    if float(pr[0]) >= 0.999: res[m['slug']] = 'Y'
                    elif float(pr[1]) >= 0.999: res[m['slug']] = 'N'
        except Exception as e: log(f'gamma lote {k // 20}: {type(e).__name__}: {e}')
        time.sleep(0.3)
    return res


def modo_resolver():
    tot = dict(pendientes=0, resueltas=0, sin_resolver=0, discrepancias=0)
    for p in sorted(glob.glob(os.path.join(OUT, 'ret_*.csv.gz'))):
        x = pd.read_csv(p, dtype={c: str for c in STRC}); pend = x[(x.resuelto != 1) & (x.fin < time.time() - 90)]
        tot_d = 0
        if len(pend):
            tot['pendientes'] += len(pend); res = gamma_resultado(sorted(pend.mercado.unique()))
            for i in pend.index:
                w = res.get(x.at[i, 'mercado'])
                if w is None: tot['sin_resolver'] += 1; continue
                g = float(w == x.at[i, 'L']); x.at[i, 'gana_L'] = g; x.at[i, 'resuelto'] = 1; x.at[i, 'resuelto_utc'] = ahora()
                if x.at[i, 'grp'] in ('E', 'BF') and pd.notna(x.at[i, 'acc_h']): x.at[i, 'pnl_h'] = x.at[i, 'acc_h'] * g - x.at[i, 'coste_h']
                tot['resueltas'] += 1; tot_d += 1
            if tot_d: escribir_atomico(x, p)
    log(f'resolver: {tot}'); return tot


def cobertura():
    cov = {}
    for p in sorted(glob.glob(os.path.join(OUT, 'ret_*.csv.gz'))):
        x = pd.read_csv(p, usecols=['grp', 'resuelto', 'forward']); d = os.path.basename(p)[4:14]
        cov[d] = dict(forward=int(x.forward.iloc[0]), **{g: int(n) for g, n in x.grp.value_counts().items()}, sin_resolver=int((x.resuelto != 1).sum()))
    return cov


def retencion():
    lim = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=RETENCION_D)).strftime('%Y-%m-%d')
    for p in glob.glob(os.path.join(OUT, 'ret_*.csv.gz')):
        if os.path.basename(p)[4:14] < lim: os.remove(p); log(f'retencion: borrado {p}')


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('modo', choices=['dia', 'backfill', 'resolver', 'cobertura']); ap.add_argument('dia', nargs='?'); ap.add_argument('--force', action='store_true')
    a = ap.parse_args(); lock = bloquear(); rc = 0
    try:
        if a.modo == 'dia': rc = modo_dia(a.dia, a.force)
        elif a.modo == 'backfill': rc = modo_backfill()
        elif a.modo == 'resolver': modo_resolver()
        retencion(); log(json.dumps(cobertura()))
    finally:
        shutil.rmtree(TMP, ignore_errors=True) if (a.modo == 'dia' and os.path.isdir(TMP) and not os.listdir(TMP)) else None
    sys.exit(rc)


if __name__ == '__main__':
    main()
