#!/usr/bin/env python3
"""etiquetar_pasivo.py -- L1 (23-Oct-2026). Etiquetado PASIVO de rpre/r900 para cada orden y posicion de B.
Solo LEE: ledger de B (experimento_h47_B_ledger.jsonl), contabilidad_wallet_dedicada/posiciones.csv y binance_bookticker_D.csv.
Escribe SOLO en datalogs: etiquetado_pasivo_B/etiquetado_B_YYYY-MM-DD.csv.gz (+ run_manifest.json, log). No importa ni edita
ningun modulo del repo (cadena de imports de observadores/ejecutores intacta). PREREG: ../PREREG_L1.md.
Modos:  etiquetar [--desde YYYY-MM-DD]   anade filas nuevas (clave unica unidad+id) -> idempotente
        resolver                         rellena desenlace oficial (gamma closed=true) y pnl de posiciones
        retencion                        borra ficheros > 30 d (se llama en cada corrida)
"""
import os, sys, io, json, csv, gzip, glob, time, datetime as dt, argparse, hashlib, fcntl
import numpy as np, pandas as pd

DL = '/root/polymarket-research-datalogs'
OUT = os.environ.get('L1_OUT', os.path.join(DL, 'etiquetado_pasivo_B'))
LEDGER = os.path.join(DL, 'experimento_h47_B_ledger.jsonl')
POSIC = '/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv'
UMBRAL_BPS = 7.7          # PREREG_L1: no se reajusta
MAX_EDAD_BN = 300.0       # s: tick Binance mas antiguo que esto = missing
RETENCION_D = 30
SYM = {'ETH', 'SOL', 'XRP', 'BTC', 'DOGE', 'BNB'}
COLS = ['unidad', 'id', 'dia', 'mercado', 'token', 'coin', 'lado', 'outcome', 'precio', 'acc', 'acc_llena', 'coste', 't0', 't0_fuente', 'fin_s', 'T_s',
        'rpre_bps', 'r900_bps', 'abs_rpre', 'clase_rpre', 'clase_r900', 'h_w1', 'bn_edad_max_s', 'etiquetado_utc',
        'resuelto', 'gana_lado', 'pnl', 'pnl_fuente', 'resuelto_utc']


STR = ['unidad', 'id', 'dia', 'mercado', 'token', 'coin', 'lado', 'outcome', 't0_fuente', 'clase_rpre', 'clase_r900', 'etiquetado_utc', 'pnl_fuente', 'resuelto_utc']


def log(m):
    print(f"[{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}] {m}", flush=True)


def dia_de(p): return os.path.basename(p)[len('etiquetado_B_'):len('etiquetado_B_') + 10]


def ahora(): return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def bloquear():
    os.makedirs(OUT, exist_ok=True)
    f = open(os.path.join(OUT, '.lock'), 'w')
    try: fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        log('otra corrida en curso (lock): salgo'); sys.exit(0)
    return f


def escribir_atomico(df, path):
    tmp = path + f'.tmp{os.getpid()}'
    with gzip.open(tmp, 'wt', newline='') as fh: df.to_csv(fh, index=False)
    with gzip.open(tmp, 'rt') as fh: n = sum(1 for _ in fh) - 1       # valida lectura antes de reemplazar
    assert n == len(df), (n, len(df))
    os.replace(tmp, path)


def leer_dia(d):
    p = os.path.join(OUT, f'etiquetado_B_{d}.csv.gz')
    if not os.path.exists(p): return pd.DataFrame(columns=COLS)
    try:
        df = pd.read_csv(p, dtype={c: str for c in STR})
        assert set(['unidad', 'id']) <= set(df.columns) and not df.duplicated(['unidad', 'id']).any()
    except Exception as e:     # checkpoint corrupto: se aparta (no se borra) y se reconstruye de las fuentes; el resolver rehace el desenlace
        log(f'CHECKPOINT CORRUPTO {p}: {type(e).__name__}: {e} -> apartado como .corrupt'); os.replace(p, p + f'.corrupt{int(time.time())}')
        return pd.DataFrame(columns=COLS)
    for c in COLS:
        if c not in df: df[c] = np.nan
    return df[COLS]


# ---------- Binance (bookTicker, recepcion) ----------
class Bn:
    def __init__(s): s.c = {}; s.files = {}
    def cargar(s, d):
        if d in s.files: return
        p = os.path.join(DL, f'binance_bookticker_{d}.csv'); s.files[d] = os.path.exists(p)
        if not s.files[d]: return
        x = pd.read_csv(p, usecols=['ts_recepcion_ms', 'activo', 'mid'])
        x['ts_recepcion_ms'] = pd.to_numeric(x.ts_recepcion_ms, errors='coerce'); x['mid'] = pd.to_numeric(x.mid, errors='coerce')
        x = x.dropna(subset=['ts_recepcion_ms', 'mid'])
        for a, g in x.groupby('activo'):
            g = g.sort_values('ts_recepcion_ms', kind='stable')
            s.c.setdefault(a, []).append((g.ts_recepcion_ms.values.astype(np.int64), g.mid.values.astype(float)))
    def listo(s, a):
        if a in s.c and isinstance(s.c[a], list):
            t = np.concatenate([u[0] for u in s.c[a]]); m = np.concatenate([u[1] for u in s.c[a]])
            o = np.argsort(t, kind='stable'); s.c[a] = (t[o], m[o])
        return s.c.get(a)
    def en(s, a, tsec):
        """(mid del ultimo tick con recepcion <= tsec, edad en s). (nan, nan) si no hay o la edad > MAX_EDAD_BN."""
        v = s.listo(a)
        if v is None: return np.nan, np.nan
        t, m = v; tm = int(round(tsec * 1000)); j = np.searchsorted(t, tm, 'right') - 1
        if j < 0: return np.nan, np.nan
        edad = (tm - t[j]) / 1000.0
        return (m[j], edad) if edad <= MAX_EDAD_BN else (np.nan, edad)


def dias_necesarios(t0s):
    ds = set()
    for t in t0s:
        for k in (0, -900 - 300 - 60):   # t0 y 21 min antes (rpre mira open-900 con open <= t0)
            ds.add(dt.datetime.fromtimestamp(t + k, dt.timezone.utc).strftime('%Y-%m-%d'))
    return sorted(ds)


def etiquetas(bn, coin, sgn, t0, fin):
    a = coin.upper()
    op = fin - 300.0
    p_t0, e1 = bn.en(a, t0); p_t0m, e2 = bn.en(a, t0 - 900.0); p_op, e3 = bn.en(a, op); p_opm, e4 = bn.en(a, op - 900.0)
    r900 = (p_t0 / p_t0m - 1) * 1e4 * sgn if np.isfinite(p_t0 * p_t0m) else np.nan
    rpre = (p_op / p_opm - 1) * 1e4 * sgn if np.isfinite(p_op * p_opm) else np.nan
    edades = [e for e in (e1, e2, e3, e4) if np.isfinite(e)]
    return rpre, r900, (max(edades) if edades else np.nan)


def clase(x):
    if not np.isfinite(x): return 'missing'
    if x == 0: return 'neutra'
    return 'a_favor' if x > 0 else 'en_contra'


def acc_orden(rellenos, tardios):
    """acc_llena de una orden = suma de rellenos UNICOS. Un `relleno_tardio` queda registrado tambien dentro de puja_fin.rellenos (tardio=True):
    sumar ambos duplicaba la cantidad (16/194 ordenes rellenas el 20-23 Oct, acc_o = 2*acc). Cada tardio del ledger se descuenta una vez si ya figura en rellenos."""
    rs = [r for r in rellenos.values()]; acc = sum(r['acc'] for r in rs)
    ya = [r['acc'] for r in rs if r.get('tardio')]
    for a in tardios:
        if a in ya: ya.remove(a)          # ya contado dentro de puja_fin.rellenos
        else: acc += a
    return acc


def cargar_fuentes():
    """Devuelve (ordenes, posiciones) como listas de dict. Lee el ledger tolerando una ultima linea a medias."""
    post, tok, rell, tard, nbad = {}, {}, {}, {}, 0
    tdet = {}
    for l in open(LEDGER):
        try: d = json.loads(l)
        except Exception: nbad += 1; continue
        t = d.get('tipo')
        if t == 'intencion_post': tok[d['oid']] = d.get('tok')
        elif t == 'puja_post': post.setdefault(d['oid'], d)                      # clave unica oid
        elif t == 'puja_fin':
            out = 'Up' if d['lado'] == 'YES' else 'Down'
            for r in d.get('rellenos') or []:
                rell.setdefault(r['oid'], {})[(r['t_deteccion'], r['acc'])] = r
                tdet.setdefault((d['slug'], out), []).append(r['t_deteccion'])
        elif t == 'relleno_tardio': tard.setdefault(d['oid'], []).append(d.get('acc') or 0)
    ordenes = []
    for oid, d in post.items():
        slug = d['slug']; fin = float(slug.rsplit('-', 1)[1]) + 300.0
        acc = acc_orden(rell.get(oid, {}), tard.get(oid, []))
        ordenes.append(dict(unidad='orden', id=oid, mercado=slug, token=tok.get(oid), coin=d['coin'].upper(), lado=d['lado'],
                            outcome='Up' if d['lado'] == 'YES' else 'Down', precio=d['precio'], acc=d['size'], acc_llena=acc, coste=np.nan,
                            t0=float(d['t_dec']), t0_fuente='t_dec', fin_s=fin, dia=dt.datetime.fromtimestamp(float(d['t_dec']), dt.timezone.utc).strftime('%Y-%m-%d')))
    pos = []
    for r in csv.DictReader(open(POSIC)):
        if not r['tanda_B']: continue
        k = (r['mercado'], r['outcome']); td = tdet.get(k)
        fin = dt.datetime.fromisoformat(r['fin_mercado_utc'].replace('Z', '+00:00')).timestamp()
        pf = dt.datetime.fromisoformat(r['fecha_primer_fill_utc'].replace('Z', '+00:00')).timestamp()
        t0, fu = (min(td) - 4.0, 't_det-4') if td else (pf - 5.0, 'primer_fill_chain-5[sin t_det]')
        pos.append(dict(unidad='posicion', id=f"{r['mercado']}|{r['outcome']}", mercado=r['mercado'], token=r['condition_id'], coin=r['mercado'].split('-')[0].upper(),
                        lado='YES' if r['outcome'] == 'Up' else 'NO', outcome=r['outcome'], precio=float(r['precio_medio']), acc=float(r['acciones']),
                        acc_llena=float(r['acciones']), coste=float(r['coste']), t0=t0, t0_fuente=fu, fin_s=fin,
                        dia=r['fecha_primer_fill_utc'][:10]))
    return ordenes, pos, nbad


def etiquetar(desde):
    ordenes, pos, nbad = cargar_fuentes()
    filas = [f for f in ordenes + pos if f['dia'] >= desde]
    exist = {}
    for d in sorted({f['dia'] for f in filas}): exist[d] = leer_dia(d)
    claves = {d: set(zip(x.unidad, x.id.astype(str))) for d, x in exist.items()}
    nuevas = [f for f in filas if (f['unidad'], str(f['id'])) not in claves[f['dia']]]
    log(f'ledger: {len(ordenes)} ordenes, {len(pos)} posiciones B; ledger lineas ilegibles={nbad}; filas desde {desde}: {len(filas)}; nuevas: {len(nuevas)}')
    if nuevas:
        bn = Bn()
        for d in dias_necesarios([f['t0'] for f in nuevas] + [f['fin_s'] - 300 for f in nuevas]): bn.cargar(d)
        ts = ahora()
        for f in nuevas:
            sgn = 1.0 if f['lado'] == 'YES' else -1.0
            rpre, r900, edad = etiquetas(bn, f['coin'], sgn, f['t0'], f['fin_s'])
            f.update(T_s=f['fin_s'] - f['t0'], rpre_bps=rpre, r900_bps=r900, abs_rpre=abs(rpre) if np.isfinite(rpre) else np.nan,
                     clase_rpre=clase(rpre), clase_r900=clase(r900), bn_edad_max_s=edad, etiquetado_utc=ts, resuelto=0)
            f['h_w1'] = int(f['clase_rpre'] == 'a_favor' and f['abs_rpre'] >= UMBRAL_BPS)
    N = pd.DataFrame(nuevas)
    tocados = set(); acc_ok = {f['id']: f['acc_llena'] for f in ordenes}; corregidas = 0
    for d, x in exist.items():       # auto-correccion idempotente de acc_llena (bug de doble conteo de rellenos tardios, 26-Oct)
        m = (x.unidad == 'orden') & x.id.isin(acc_ok)
        ok = x.id.map(acc_ok); mal = m & ((x.acc_llena.fillna(0) - ok).abs() > 1e-9)
        if mal.any(): x.loc[mal, 'acc_llena'] = ok[mal]; corregidas += int(mal.sum()); tocados.add(d); exist[d] = x; escribir_atomico(x[COLS], os.path.join(OUT, f'etiquetado_B_{d}.csv.gz'))
    if corregidas: log(f'acc_llena corregida en {corregidas} ordenes existentes')
    for d, x in exist.items():
        add = N[N.dia == d] if len(N) else N
        out = pd.concat([x, add[[c for c in COLS if c in add]]], ignore_index=True) if len(add) else x
        out = out.drop_duplicates(['unidad', 'id'], keep='first')
        if len(add): tocados.add(d)
        if len(add) or not os.path.exists(os.path.join(OUT, f'etiquetado_B_{d}.csv.gz')):
            escribir_atomico(out[COLS], os.path.join(OUT, f'etiquetado_B_{d}.csv.gz'))
    return len(nuevas), sorted(tocados)


def gamma_resultado(slugs):
    import requests
    ses = requests.Session(); res = {}
    for k in range(0, len(slugs), 20):
        lote = slugs[k:k + 20]
        try:
            r = ses.get('https://gamma-api.polymarket.com/markets', timeout=25, params=[('slug', s) for s in lote] + [('closed', 'true'), ('limit', '40')])
            r.raise_for_status()
            for m in r.json() or []:
                pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
                oc = m.get('outcomes'); oc = json.loads(oc) if isinstance(oc, str) else oc
                if pr and oc and len(pr) == 2 and oc == ['Up', 'Down']:
                    if float(pr[0]) >= 0.999: res[m['slug']] = 'Up'
                    elif float(pr[1]) >= 0.999: res[m['slug']] = 'Down'
        except Exception as e:
            log(f'gamma lote {k // 20}: {type(e).__name__}: {e}')
        time.sleep(0.3)
    return res


def resolver():
    pc = {}
    for r in csv.DictReader(open(POSIC)):
        if r['tanda_B']: pc[(r['mercado'], r['outcome'])] = r
    ahora_s = time.time(); tot = {'pendientes': 0, 'resueltas': 0, 'sin_resolver': 0, 'discrepancias_vs_posiciones_csv': 0}
    for p in sorted(glob.glob(os.path.join(OUT, 'etiquetado_B_*.csv.gz'))):
        d = dia_de(p); x = leer_dia(d)
        pend = x[(x.resuelto != 1) & (x.fin_s < ahora_s - 90)]
        if pend.empty: continue
        tot['pendientes'] += len(pend)
        res = gamma_resultado(sorted(pend.mercado.unique()))
        cambio = 0
        for i in pend.index:
            slug, out = x.at[i, 'mercado'], x.at[i, 'outcome']
            ganador = res.get(slug)
            if ganador is None:
                tot['sin_resolver'] += 1; continue
            gana = int(ganador == out); x.at[i, 'gana_lado'] = gana; x.at[i, 'resuelto'] = 1; x.at[i, 'resuelto_utc'] = ahora(); cambio += 1
            if x.at[i, 'unidad'] == 'posicion':
                r = pc.get((slug, out))
                if r and r['estado'] in ('liquidada_ganada', 'liquidada_perdida'):
                    if (r['estado'] == 'liquidada_ganada') != bool(gana): tot['discrepancias_vs_posiciones_csv'] += 1
                    x.at[i, 'pnl'] = float(r['pnl_realizado']); x.at[i, 'pnl_fuente'] = 'posiciones.csv'
                    x.at[i, 'coste'] = float(r['coste'])
                else:   # estimacion: sin fee (maker) ni rebate
                    x.at[i, 'pnl'] = x.at[i, 'acc'] * gana - x.at[i, 'coste']; x.at[i, 'pnl_fuente'] = 'estimado_gamma'
        tot['resueltas'] += cambio
        if cambio: escribir_atomico(x[COLS], p)
    log(f'resolver: {tot}')
    return tot


def retencion():
    lim = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=RETENCION_D)).strftime('%Y-%m-%d')
    for p in glob.glob(os.path.join(OUT, 'etiquetado_B_*.csv.gz')):
        if dia_de(p) < lim: os.remove(p); log(f'retencion: borrado {p}')


def cobertura():
    """Cobertura por dia: filas, missing por unidad/clase, resueltas. Imprime y devuelve dict."""
    cov = {}
    for p in sorted(glob.glob(os.path.join(OUT, 'etiquetado_B_*.csv.gz'))):
        x = leer_dia(dia_de(p)); d = dia_de(p)
        c = {}
        for u, g in x.groupby('unidad'):
            c[u] = dict(n=len(g), rpre_missing=int((g.clase_rpre == 'missing').sum()), rpre_neutra=int((g.clase_rpre == 'neutra').sum()), r900_missing=int((g.clase_r900 == 'missing').sum()), r900_neutra=int((g.clase_r900 == 'neutra').sum()), h_w1=int(g.h_w1.sum()),
                        resueltas=int((g.resuelto == 1).sum()), duplicados=int(g.duplicated(['unidad', 'id']).sum()))
        cov[d] = c
    return cov


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('modo', choices=['etiquetar', 'resolver', 'retencion', 'cobertura'])
    ap.add_argument('--desde', default=(dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=3)).strftime('%Y-%m-%d'))
    a = ap.parse_args(); lock = bloquear(); t_ini = ahora(); estado = 'COMPLETE'; extra = {}
    try:
        if a.modo == 'etiquetar': n, dias = etiquetar(a.desde); extra = dict(nuevas=n, dias_tocados=dias)
        elif a.modo == 'resolver': extra = resolver()
        elif a.modo == 'cobertura': pass
        retencion(); extra['cobertura'] = cobertura()
        log(json.dumps(extra['cobertura']))
    except Exception as e:
        estado = 'FAILED'; extra['error'] = f'{type(e).__name__}: {e}'; log('FALLO ' + extra['error']); raise
    finally:
        h = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()[:16]
        m = dict(job='etiquetado_pasivo_B_L1', modo=a.modo, codigo_sha16=h, parametros=dict(umbral_bps=UMBRAL_BPS, max_edad_bn_s=MAX_EDAD_BN, desde=a.desde),
                 entradas=dict(ledger=LEDGER, ledger_bytes=os.path.getsize(LEDGER), posiciones=POSIC), inicio=t_ini, fin=ahora(), estado=estado, **{k: v for k, v in extra.items()})
        with open(os.path.join(OUT, f'run_manifest_{a.modo}.json'), 'w') as fh: json.dump(m, fh, indent=1, default=str)


if __name__ == '__main__':
    main()
