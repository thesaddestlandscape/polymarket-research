#!/usr/bin/env python3
"""etiquetar_dfuerte.py <YYYY-MM-DD|ayer> - ETIQUETADOR FORWARD PASIVO D-FUERTE (solo lectura de datos propios; unico acceso externo: GET PUBLICO de klines 1m Binance, sin clave).
Para cada apertura 5m del dia (288) y moneda (BTC,ETH,SOL,XRP): rasgos causales (barras cerradas <= t_o) y s_hat del MODELO CONGELADO para p_con en {0,10..0,29}; salida
/root/polymarket-research-datalogs/regimen_5m/etiquetas_dfuerte/regimen_dfuerte_<D>.csv.gz . Idempotente, atomico, lock fcntl, retencion 45 d, falla en alto (exit 2) si falta dato.
Modelo: dfuerte/MODELO_CONGELADO.json (pickle + sha256 verificados antes de usarlos). No toca B, ejecutores ni crons."""
import sys, os, json, time, fcntl, hashlib, pickle, datetime as dt, glob, calendar, warnings
import numpy as np, pandas as pd, requests
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import dfuerte_lib as DL
ROOT = '/root/polymarket-research-datalogs/regimen_5m'; ARC = f'{ROOT}/dfuerte_fwd'; OUTD = f'{ROOT}/etiquetas_dfuerte'; RET = 45; WARM = 16
COINS = ['BTC', 'ETH', 'SOL', 'XRP']; PGRID = [0.10, 0.15, 0.20, 0.25, 0.29]
def fail(msg): print('ERROR', msg, file=sys.stderr); sys.exit(2)
def fetch_day(day):
    p = f'{ARC}/kl_{day}.npz'
    if os.path.exists(p): return p
    t0 = calendar.timegm(dt.date.fromisoformat(day).timetuple()) * 1000; z = {}
    for c in COINS:
        rows = []; t = t0
        while t < t0 + 86400000:
            j = None
            for k in range(5):
                try: r = requests.get('https://api.binance.com/api/v3/klines', params=dict(symbol=c + 'USDT', interval='1m', startTime=t, limit=1000), timeout=15); r.raise_for_status(); j = r.json(); break
                except Exception: time.sleep(2)
            if not j: fail(f'sin klines {c} {day}')
            rows += [(x[0], float(x[4]), float(x[2]), float(x[3]), float(x[5]), float(x[9]), float(x[8])) for x in j if x[0] < t0 + 86400000]; t = j[-1][0] + 60000; time.sleep(0.1)
        a = np.array(rows); X = np.full((1440, 6), np.nan); idx = ((a[:, 0] - t0) // 60000).astype(int); X[idx] = a[:, 1:]; z[c] = X
    if day == dt.datetime.utcnow().strftime('%Y-%m-%d'): return None   # dia incompleto: no archivar
    os.makedirs(ARC, exist_ok=True); tmp = p + f'.tmp{os.getpid()}.npz'; np.savez_compressed(tmp, **z); os.replace(tmp, p); return p
def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else 'ayer'
    D = (dt.datetime.utcnow().date() - dt.timedelta(days=1)).isoformat() if arg == 'ayer' else arg
    os.makedirs(OUTD, exist_ok=True); lock = open(f'{ROOT}/etiquetas_dfuerte.lock', 'w'); fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    M = json.load(open(os.path.join(HERE, '..', 'MODELO_CONGELADO.json'))); pk = os.path.join(HERE, '..', M['pickle'])
    if hashlib.sha256(open(pk, 'rb').read()).hexdigest() != M['sha256_pickle']: fail('sha del modelo no coincide')
    kind, fams, model, CUT = pickle.load(open(pk, 'rb'))[M['modelo']]
    d0 = dt.date.fromisoformat(D); days = [(d0 - dt.timedelta(days=k)).isoformat() for k in range(WARM, -1, -1)]; Z = {c: [] for c in COINS}
    for d in days:
        if fetch_day(d) is None: fail(f'dia {d} incompleto')
        z = np.load(f'{ARC}/kl_{d}.npz')
        for c in COINS: Z[c].append(z[c])
    m0 = calendar.timegm(dt.date.fromisoformat(days[0]).timetuple()) // 60 + 1
    ZZ = {c: (m0, np.concatenate(Z[c])) for c in COINS}
    d0m = calendar.timegm(d0.timetuple()) // 60; tm = d0m + 5 * np.arange(288)
    W = DL.all_features(ZZ, COINS, tm=tm)
    cols = list(dict.fromkeys(['lpc'] + sum([DL.FAM[f] for f in fams], [])))
    out = W[['coin', 'tmin', 'rpre', 'o', 'R', 's60']].copy(); out['dia'] = D
    for p in PGRID:
        W['lpc'] = np.log(p / (1 - p)); out['s_p%02d' % round(p * 100)] = model.predict_proba(W[cols].values.astype(float))[:, 1] - p
    out['modelo'] = M['modelo']; out['codigo_sha'] = M['lib_sha256'][:12]
    p_out = f'{OUTD}/regimen_dfuerte_{D}.csv.gz'; tmp = p_out + f'.tmp{os.getpid()}'
    out.to_csv(tmp, index=False, compression='gzip'); os.replace(tmp, p_out)
    for f in sorted(glob.glob(f'{OUTD}/regimen_dfuerte_*.csv.gz'))[:-RET]: os.remove(f)
    print('OK', D, len(out), 'filas;', 'aperturas con score', int(out.s_p20.notna().sum()))
if __name__ == '__main__': main()
