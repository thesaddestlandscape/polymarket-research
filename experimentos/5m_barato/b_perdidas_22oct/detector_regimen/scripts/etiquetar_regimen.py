#!/usr/bin/env python3
"""etiquetar_regimen.py - ETIQUETADOR FORWARD PASIVO del regimen (PREREG_RTEND). Solo lectura de bookTicker de Binance (la misma fuente de L1). No importa modulos del repo, no toca B/ejecutores, sin red ni claves.
Uso:  python3 -I etiquetar_regimen.py dia [YYYY-MM-DD]   (por defecto AYER UTC; reconstruye barras del dia y etiqueta sus 288 aperturas x 6 monedas)
      python3 -I etiquetar_regimen.py cobertura
Salidas (fuera de git): /root/polymarket-research-datalogs/regimen_5m/barras_dia/bars_D.npz (1440 x 6, para siempre: ~70 kB/dia)
                         /root/polymarket-research-datalogs/regimen_5m/etiquetas/regimen_D.csv.gz (retencion 45 d), manifest.json
Etiquetas = las del detector R/D/COH congelado (misma regimen_lib que el analisis). Escritura atomica, idempotente, lock fcntl."""
import sys, os, glob, json, fcntl, hashlib, datetime as dt, numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import regimen_lib as L
OUT = '/root/polymarket-research-datalogs/regimen_5m'; BD = f'{OUT}/barras_dia'; ED = f'{OUT}/etiquetas'
COINS = ['BTC', 'ETH', 'SOL', 'XRP', 'BNB', 'DOGE']; HIST = 17
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:12]
def barras_dia(d):
    """Barras 1m (cierre = ultimo mid con recepcion < fin de minuto; ffill <=2) de bookTicker del dia d y del siguiente tramo no hace falta."""
    f = f'/root/polymarket-research-datalogs/binance_bookticker_{d}.csv'
    if not os.path.exists(f): return None
    x = pd.read_csv(f, usecols=['ts_recepcion_ms', 'activo', 'mid']); x = x[np.isfinite(x.ts_recepcion_ms) & np.isfinite(x.mid)]
    m0 = int(dt.datetime.fromisoformat(d).replace(tzinfo=dt.timezone.utc).timestamp() // 60); z = {'m0': np.int64(m0)}
    for c in COINS:
        g = x[x.activo == c].sort_values('ts_recepcion_ms'); P = np.full(1441, np.nan)   # P[k]: cierre al final del minuto m0+k  (k=0 -> m0, ancla = ultimo tick del dia previo: no disponible -> NaN)
        if len(g):
            mn = (g.ts_recepcion_ms.values // 60000).astype(np.int64); last = np.r_[np.nonzero(np.diff(mn))[0], len(mn) - 1]
            k = mn[last] + 1 - m0; ok = (k >= 0) & (k <= 1440); P[k[ok]] = g.mid.values[last][ok]; P = pd.Series(P).ffill(limit=2).values
        z[c] = P
    return z
def concat(ds):
    """Une barras de dias consecutivos (m0, 1441 puntos con solape de 1 punto) en series continuas."""
    B = {}
    ms = []
    for d in ds:
        p = f'{BD}/bars_{d}.npz'
        if os.path.exists(p): ms.append((d, np.load(p)))
    if not ms: return None
    m0 = int(ms[0][1]['m0']); n = (int(ms[-1][1]['m0']) - m0) + 1441; out = {}
    for c in COINS:
        P = np.full(n, np.nan)
        for d, z in ms:
            o = int(z['m0']) - m0; a = z[c]; sel = np.isfinite(a); P[o:o + 1441][sel] = a[sel]
        out[c] = (m0, P)
    return out
def etiquetar(d):
    os.makedirs(BD, exist_ok=True); os.makedirs(ED, exist_ok=True)
    day = dt.date.fromisoformat(d); z = barras_dia(d)
    if z is None: print('sin bookTicker', d); return 2
    np.savez_compressed(f'{BD}/bars_{d}.npz.tmp.npz', **z); os.replace(f'{BD}/bars_{d}.npz.tmp.npz', f'{BD}/bars_{d}.npz')
    ds = [(day - dt.timedelta(days=k)).isoformat() for k in range(HIST, -2, -1)]; ds = [x for x in ds if x <= (day + dt.timedelta(days=1)).isoformat()]
    S = concat([x for x in ds]); 
    if S is None: return 2
    Bs = {c: L.base_series(m0, P) for c, (m0, P) in S.items()}
    d0 = int(day.strftime('%s')) if False else int(dt.datetime(day.year, day.month, day.day, tzinfo=dt.timezone.utc).timestamp() // 60)
    tm = np.arange(d0, d0 + 1440, 5)
    sg = []
    for c in L.COH_COINS:
        B = Bs[c]; sg.append(np.sign(L.lp_at(B, tm - B['m0']) - L.lp_at(B, tm - 60 - B['m0'])))
    coh = np.abs(np.nansum(sg, axis=0)); coh = np.where(np.all([np.isfinite(s) for s in sg], axis=0), coh, np.nan)
    rows = []
    for c in COINS:
        B = Bs[c]; days_all = sorted(set(range(d0 // 1440 - HIST, d0 // 1440 + 1)))
        # features de todo el tramo (para la mediana de 14 d) y de hoy
        tm_h = np.arange((B['m0'] + 1500 + 4) // 5 * 5, d0 + 1440, 5); io_h = tm_h - B['m0']
        f = L.features_open(B, io_h)
        cm = np.full(len(tm_h), np.nan)
        df = pd.DataFrame({'coin': c, 'tmin': tm_h, 'dia': tm_h // 1440, **f, 'COH': np.nan})
        erd = L.er_dia_prev_table(B, sorted(set(tm_h // 1440) | {(d0 // 1440) - k for k in range(0, 17)}))
        df['D'] = df.dia.map(L.d_class(erd)).fillna('NA'); df['ER_dia_prev'] = (df.dia - 1).map(erd)
        df = L.add_classes(df); t = df[df.dia == d0 // 1440].copy(); t = t[t.tmin.isin(tm)]
        t['COH'] = pd.Series(coh, index=tm).reindex(t.tmin.values).values; rows.append(t)
    R = pd.concat(rows, ignore_index=True); R['fin_s'] = (R.tmin + 5) * 60; R['version'] = sha(os.path.join(HERE, 'regimen_lib.py'))
    R = R[['coin', 'tmin', 'fin_s', 'dia', 'rpre', 'r60', 'ER60', 'VR240', 'VOLR', 'DAYT', 'COH', 'med_ER', 'ER_dia_prev', 'R', 'D', 'version']]
    tmp = f'{ED}/regimen_{d}.csv.gz.tmp'; R.to_csv(tmp, index=False, compression='gzip'); chk = pd.read_csv(tmp, compression='gzip')
    assert len(chk) == len(R); os.replace(tmp, f'{ED}/regimen_{d}.csv.gz')
    for f_ in glob.glob(f'{ED}/regimen_*.csv.gz'):
        if os.path.basename(f_)[8:18] < (day - dt.timedelta(days=45)).isoformat(): os.remove(f_)
    json.dump(dict(dia=d, filas=len(R), cobertura_R=float((R.R != 'NA').mean()), version=R.version.iloc[0], utc=dt.datetime.now(dt.timezone.utc).isoformat()), open(f'{OUT}/manifest_etiquetas.json', 'w'))
    print(d, 'filas', len(R), 'R no NA', round(float((R.R != 'NA').mean()), 3)); return 0
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); lk = open(f'{OUT}/.lock_etiquetas', 'w')
    try: fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError: print('lock ocupado'); sys.exit(0)
    a = sys.argv[1] if len(sys.argv) > 1 else 'dia'
    if a == 'dia':
        d = sys.argv[2] if len(sys.argv) > 2 else (dt.datetime.now(dt.timezone.utc).date() - dt.timedelta(days=1)).isoformat(); sys.exit(etiquetar(d))
    if a == 'barras':      # backfill de barras por dia: barras YYYY-MM-DD YYYY-MM-DD
        d1 = dt.date.fromisoformat(sys.argv[2]); d2 = dt.date.fromisoformat(sys.argv[3]); os.makedirs(BD, exist_ok=True)
        while d1 <= d2:
            z = barras_dia(d1.isoformat())
            if z is not None: np.savez_compressed(f'{BD}/bars_{d1}.npz.tmp.npz', **z); os.replace(f'{BD}/bars_{d1}.npz.tmp.npz', f'{BD}/bars_{d1}.npz')
            d1 += dt.timedelta(days=1)
        sys.exit(0)
    if a == 'cobertura':
        for f in sorted(glob.glob(f'{ED}/regimen_*.csv.gz'))[-10:]: x = pd.read_csv(f); print(os.path.basename(f), len(x), 'R!=NA', round(float((x.R != 'NA').mean()), 3))
