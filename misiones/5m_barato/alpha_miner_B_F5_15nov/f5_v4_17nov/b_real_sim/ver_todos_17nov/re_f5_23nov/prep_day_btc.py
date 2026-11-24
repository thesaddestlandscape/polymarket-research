#!/usr/bin/env python3
"""prep_day_btc.py DIA -- (E7 BTC, condicion C4 (2)) cinta on-chain de BTC 5 min = MISMA cadena que prep_day.py de dev (reconstructor_relleno copiado aqui, sha fijo) con los tokens de btc_ms_D.npz (SA_TAG=btc) en lugar de ms_D.npz.
Escribe /root/polymarket-research-datalogs/rf5_btc/tape_btc_D.pkl + bad_btc_D.json (atomico, idempotente: sale si ya existen) y anota el sha en TAPES_SHA256_btc.txt (append-only). Solo lectura de datalogs/volumen; 0 ordenes, 0 red. Se invoca por cron_pesado (btc_backfill.sh), nice 19, ulimit -v 5 GB."""
import sys, os, glob, json, hashlib
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
SHA_RECON = 'cdfe43e469f86d40'      # prefijo del sha256 de reconstructor_relleno.py copiado byte a byte de dev (captura_prints)
DL = os.environ.get('RF5_DL', '/root/polymarket-research-datalogs/'); TXD = os.environ.get('RF5_TXD', '/mnt/HC_Volume_106538179/libro5_tx/'); OUT = os.environ.get('RF5_BTC_OUT', DL + 'rf5_btc/'); REF = HV + 'TAPES_SHA256_btc.txt'

def tokens_btc5(d, dl=None):
    z = np.load((dl or DL) + f'sa_ms/btc_ms_{d}.npz', allow_pickle=True); return {t for t, r in zip(z['tokens'], z['tmap']) if str(r[0]).upper() == 'BTC' and r[1] == '5min'}

def prep(d, dl=None, txd=None, out=None, keep=None):
    dl = dl or DL; txd = txd or TXD; out = out or OUT; os.makedirs(out, exist_ok=True)
    if os.path.exists(out + f'tape_btc_{d}.pkl') and os.path.exists(out + f'bad_btc_{d}.json'): return 'YA'
    if hashlib.sha256(open(HV + 'reconstructor_relleno.py', 'rb').read()).hexdigest()[:16] != SHA_RECON: raise ValueError('reconstructor_relleno.py cambio (sha): fail-closed')
    import reconstructor_relleno as RR
    if not os.path.exists(dl + f'sa_ms/btc_ms_{d}.npz'): return 'SIN_BTC_MS'
    tok5 = tokens_btc5(d, dl)
    if not tok5: return 'SIN_TOKENS_BTC5'
    files = sorted(glob.glob((keep or dl + 'keep_onchain_re_as_b/') + f'onchain_fills_{d}*.csv.gz'))
    if not files: return 'SIN_ONCHAIN'
    ch = []
    for f in files:
        for c in pd.read_csv(f, usecols=['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'], dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=400000): ch.append(c[c.token_id.isin(tok5)])
    fills = RR.fills_makers(pd.concat(ch)); del ch; dd = pd.Timestamp(d); fr = []
    for dday in [(dd + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]:
        for f in sorted(glob.glob(txd + f'libro5_tx_{dday}_*.csv.gz')): fr.append(pd.read_csv(f, header=None, names=['t_ev', 'token', 'tx', 'recv'], dtype={'token': str, 'tx': str}))
    tws, _ = RR.tx_ws(fr, con_tokens=False); del fr; chain = RR.reconstruir(fills, tws); del fills
    ok = RR.horas_sanas(chain, 0.95); t = pd.to_datetime(chain.ts_est, unit='s', utc=True); keep_ = np.array([(a, b) in ok for a, b in zip(t.dt.strftime('%Y-%m-%d'), t.dt.hour)]); bad = sorted([d, h] for h in range(24) if (d, h) not in ok)
    sl = chain[keep_ & (chain.side.values == 0)][['token_id', 'price', 'sh', 'side', 't_ws_ms', 'src', 'tx', 'log_index', 'maker', 'ts_est']].copy()
    sl.to_pickle(out + f'tape_btc_{d}.pkl.tmp'); os.replace(out + f'tape_btc_{d}.pkl.tmp', out + f'tape_btc_{d}.pkl')
    json.dump(dict(bad=bad, fills=int(len(chain)), cob_tx_ws=float((chain.src == 'tx_ws').mean()), side0_sanas=int(len(sl)), tokens_btc5=len(tok5)), open(out + f'bad_btc_{d}.json.tmp', 'w')); os.replace(out + f'bad_btc_{d}.json.tmp', out + f'bad_btc_{d}.json')
    for f in (out + f'tape_btc_{d}.pkl', out + f'bad_btc_{d}.json'):
        h = hashlib.sha256(open(f, 'rb').read()).hexdigest(); lin = f'{h}  {f}\n'
        if f not in open(REF).read() if os.path.exists(REF) else True: open(REF, 'a').write(lin)
    return 'OK'

if __name__ == '__main__':
    for d in sys.argv[1:]: print(d, prep(d))
