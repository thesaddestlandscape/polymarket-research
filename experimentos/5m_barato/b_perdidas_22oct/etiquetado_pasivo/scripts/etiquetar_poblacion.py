#!/usr/bin/env python3
"""etiquetar_poblacion.py -- L1b parte A (23-Oct-2026). Etiqueta rpre/r900/h_w1 de la POBLACION on-chain ETH/SOL/XRP 5m con EL MISMO codigo de L1
(importa Bn/etiquetas/clase de etiquetar_pasivo.py). PREREG: ../PREREG_L1b.md. Solo LEE: sa_r1/units_DIA.csv.gz (R1, ya extraidas; no se re-extrae on-chain),
cola_posicion/datos/pop_units_DIA.csv.gz (backfill 17-22 Oct) y binance_bookticker_D.csv. Escribe SOLO en datalogs/etiquetado_pasivo_B/poblacion/.
Modos: etiquetar [--desde D] | verificar (audita `gana` contra gamma closed=true en una muestra) | cobertura.  Idempotente: clave unica (id) = maker|mercado_id|lado."""
import os, sys, json, glob, gzip, time, hashlib, importlib.util, datetime as dt, argparse, fcntl
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DL = '/root/polymarket-research-datalogs'
OUT = os.environ.get('L1B_OUT', os.path.join(DL, 'etiquetado_pasivo_B', 'poblacion'))
R1 = os.environ.get('L1B_R1', os.path.join(DL, 'sa_r1'))
POPU = os.environ.get('L1B_POPU', '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/cola_posicion/datos')
FWD0 = '2026-10-23'; RETENCION_D = 30; DESDE_DEF = '2026-10-17'


def _cargar_l1():
    sp = importlib.util.spec_from_file_location('l1_etiquetar', os.path.join(HERE, 'etiquetar_pasivo.py'))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m


L1 = _cargar_l1()
COLS = ['id', 'dia', 'fuente', 'forward', 'maker', 'mercado', 'mid', 'coin', 'lado', 'fin_s', 'ts', 'T_s', 'precio', 'acc', 'coste', 'pnl', 'fee_eur', 'gana_lado',
        'rpre_bps', 'r900_bps', 'abs_rpre', 'clase_rpre', 'clase_r900', 'h_w1', 'bn_edad_max_s', 'etiquetado_utc']
STR = ['id', 'dia', 'fuente', 'maker', 'mercado', 'mid', 'coin', 'lado', 'clase_rpre', 'clase_r900', 'etiquetado_utc']


def log(m): print(f"[{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}] {m}", flush=True)
def ahora(): return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def bloquear():
    os.makedirs(OUT, exist_ok=True); f = open(os.path.join(OUT, '.lock'), 'w')
    try: fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError: log('otra corrida en curso (lock): salgo'); sys.exit(0)
    return f


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()[:16]


def leer_dia(d):
    p = os.path.join(OUT, f'pob_{d}.csv.gz')
    if not os.path.exists(p): return pd.DataFrame(columns=COLS)
    try:
        df = pd.read_csv(p, dtype={c: str for c in STR})
        assert 'id' in df.columns and not df.duplicated('id').any()
    except Exception as e:   # checkpoint corrupto: se aparta (no se borra) y se reconstruye de las fuentes
        log(f'CHECKPOINT CORRUPTO {p}: {type(e).__name__}: {e} -> apartado'); os.replace(p, p + f'.corrupt{int(time.time())}')
        return pd.DataFrame(columns=COLS)
    for c in COLS:
        if c not in df: df[c] = np.nan
    return df[COLS]


def normaliza_pop(path):
    x = pd.read_csv(path)
    x = x[x.es_b == 0]
    return pd.DataFrame(dict(dia=x.dia, maker=x.maker, mid=x.mid.astype(str), coin=x.act, lado=x.lado, fin_s=x.fin.astype(float), ts=x.ts.astype(float), precio=x.pc,
                             acc=x.acc, coste=x.coste, pnl=x.pnl, gana_lado=x.gana.astype(float)))


def normaliza_r1(path):
    x = pd.read_csv(path)
    return pd.DataFrame(dict(dia=x.dia, maker=x.maker, mid=x.mkt.astype(str), coin=x.act, lado=x.lado_c, fin_s=x.fin.astype(float), ts=x.ts.astype(float), precio=x.pc,
                             acc=x.sh, coste=x.c, pnl=x.p, gana_lado=x.gana.astype(float)))


def fuentes(desde):
    """[(dia, fuente, path, fn)]. UNA fuente por dia (PREREG_L1b): dias < FWD0 = pop_units (backfill, poblacion que vio W1); dias >= FWD0 = sa_r1 (forward).
    Las dos definiciones NO son identicas (medido 20-21 Oct: R1 tiene +58 % de unidades y el 9 % de las coincidentes difieren en coste), asi que nunca se mezclan en un dia."""
    L = []
    for p in sorted(glob.glob(os.path.join(POPU, 'pop_units_*.csv.gz'))):
        d = os.path.basename(p)[len('pop_units_'):-len('.csv.gz')]
        if desde <= d < FWD0: L.append((d, 'pop_units_backfill', p, normaliza_pop))
    for p in sorted(glob.glob(os.path.join(R1, 'units_*.csv.gz'))):
        d = os.path.basename(p)[len('units_'):-len('.csv.gz')]
        if d >= max(desde, FWD0): L.append((d, 'sa_r1', p, normaliza_r1))
    return L


def etiquetar(desde):
    os.makedirs(OUT, exist_ok=True); fu = fuentes(desde); nuevas_tot = 0; tocados = []; entradas = {}
    por_dia = {}
    for d, nom, p, fn in fu: por_dia.setdefault(d, []).append((nom, p, fn))
    for d in sorted(por_dia):
        ex = leer_dia(d); claves = set(ex.id.astype(str)); add = []
        for nom, p, fn in por_dia[d]:
            entradas[p] = sha(p); x = fn(p)
            x['fuente'] = nom; x['id'] = x.maker.astype(str) + '|' + x.mid.astype(str) + '|' + x.lado.astype(str)
            x = x[~x.id.isin(claves)].drop_duplicates('id'); claves |= set(x.id); add.append(x)
        add = pd.concat(add, ignore_index=True) if add else pd.DataFrame()
        if len(add) == 0 and os.path.exists(os.path.join(OUT, f'pob_{d}.csv.gz')): continue
        if len(add):
            bn = L1.Bn()
            for dd in L1.dias_necesarios(list(add.ts - 5.0) + list(add.fin_s - 300)): bn.cargar(dd)
            r_, r9, ed = [], [], []
            for ts, fin, coin, lado in zip(add.ts.values, add.fin_s.values, add.coin.values, add.lado.values):
                a, b, c = L1.etiquetas(bn, str(coin), 1.0 if lado == 'YES' else -1.0, float(ts) - 5.0, float(fin)); r_.append(a); r9.append(b); ed.append(c)
            add['rpre_bps'] = r_; add['r900_bps'] = r9; add['bn_edad_max_s'] = ed; add['abs_rpre'] = np.abs(add.rpre_bps)
            add['clase_rpre'] = [L1.clase(v) for v in add.rpre_bps]; add['clase_r900'] = [L1.clase(v) for v in add.r900_bps]
            add['h_w1'] = ((add.clase_rpre == 'a_favor') & (add.abs_rpre >= L1.UMBRAL_BPS)).astype(int)
            add['mercado'] = [f'{str(c).lower()}-updown-5m-{int(f - 300)}' for c, f in zip(add.coin, add.fin_s)]
            add['T_s'] = add.fin_s - add.ts; add['forward'] = int(d >= FWD0); add['fee_eur'] = 0.0; add['etiquetado_utc'] = ahora()
            out = pd.concat([ex, add[COLS]], ignore_index=True).drop_duplicates('id', keep='first')
            L1.escribir_atomico(out[COLS], os.path.join(OUT, f'pob_{d}.csv.gz')); nuevas_tot += len(add); tocados.append(d)
            log(f'{d}: +{len(add)} unidades (total {len(out)}) fuentes={[n for n, _, _ in por_dia[d]]}')
        else:
            L1.escribir_atomico(ex[COLS], os.path.join(OUT, f'pob_{d}.csv.gz'))
    return nuevas_tot, tocados, entradas


def retencion():
    lim = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=RETENCION_D)).strftime('%Y-%m-%d')
    for p in glob.glob(os.path.join(OUT, 'pob_*.csv.gz')):
        if os.path.basename(p)[4:14] < lim: os.remove(p); log(f'retencion: borrado {p}')


def cobertura():
    cov = {}
    for p in sorted(glob.glob(os.path.join(OUT, 'pob_*.csv.gz'))):
        d = os.path.basename(p)[4:14]; x = leer_dia(d)
        cov[d] = dict(n=len(x), forward=int(d >= FWD0), rpre_missing=int((x.clase_rpre == 'missing').sum()), rpre_neutra=int((x.clase_rpre == 'neutra').sum()), h_w1=int(x.h_w1.sum()),
                      duplicados=int(x.duplicated('id').sum()), mercados=int(x.mid.nunique()), coste=round(float(x.coste.sum()), 2), pnl=round(float(x.pnl.sum()), 2), sin_gana=int(x.gana_lado.isna().sum()))
    return cov


def verificar(n_max=100, ultimos=3):
    """Resolvedor/auditoria: contrasta `gana_lado` con gamma closed=true en una muestra reproducible de mercados por dia (el desenlace ya viene de gamma via R1/pop_units)."""
    import requests
    ses = requests.Session(); tot = dict(mercados=0, sin_resolver=0, discrepancias=0)
    for p in sorted(glob.glob(os.path.join(OUT, 'pob_*.csv.gz')))[-ultimos:]:
        d = os.path.basename(p)[4:14]; x = leer_dia(d); ms = x.drop_duplicates('mercado')
        ms = ms.sample(min(n_max, len(ms)), random_state=20261023) if len(ms) else ms; res = L1.gamma_resultado(sorted(ms.mercado.unique()))
        for s in ms.mercado:
            tot['mercados'] += 1
            if s not in res: tot['sin_resolver'] += 1; continue
            for r in x[x.mercado == s].itertuples():
                if int(r.gana_lado) != int(res[s] == r.lado.replace('YES', 'Up').replace('NO', 'Down')): tot['discrepancias'] += 1
    log(f'verificar: {tot}'); return tot


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('modo', choices=['etiquetar', 'verificar', 'cobertura']); ap.add_argument('--desde', default=DESDE_DEF)
    a = ap.parse_args(); lock = bloquear(); t0 = ahora(); estado = 'COMPLETE'; extra = {}
    try:
        if a.modo == 'etiquetar': n, dias, ent = etiquetar(a.desde); extra = dict(nuevas=n, dias_tocados=dias, entradas=ent)
        elif a.modo == 'verificar': extra = verificar()
        retencion(); extra['cobertura'] = cobertura(); log(json.dumps(extra['cobertura']))
    except Exception as e:
        estado = 'FAILED'; extra['error'] = f'{type(e).__name__}: {e}'; log('FALLO ' + extra['error']); raise
    finally:
        m = dict(job='l1b_poblacion', modo=a.modo, codigo_sha16=sha(os.path.abspath(__file__)), l1_sha16=sha(os.path.join(HERE, 'etiquetar_pasivo.py')), parametros=dict(umbral_bps=L1.UMBRAL_BPS, desde=a.desde, fwd0=FWD0),
                 inicio=t0, fin=ahora(), estado=estado, **extra)
        with open(os.path.join(OUT, f'run_manifest_{a.modo}.json'), 'w') as fh: json.dump(m, fh, indent=1, default=str)


if __name__ == '__main__':
    main()
