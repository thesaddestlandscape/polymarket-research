#!/usr/bin/env python3
"""cobertura_bruta.py DIA -- (ADENDA_RF5_CRITERIOS_v2 3a, C1) cobertura libro5_tx con_tx/units sobre TODAS las unidades de la cinta on-chain (side 0) ANTES de filtrar horas sanas (el prep_day de dev guarda solo la cinta ya
filtrada, lo que hacia vacia la comprobacion). Misma cadena que prep_day.py (reconstructor_relleno, solo lectura de datalogs/volumen; 0 ordenes, 0 red). units = tx distintos de fills side 0; con_tx = los que estan en libro5_tx de x-1..x+1.
Por hora UTC: fills, units, con_tx, nocional USD, volatilidad de precio (media por token de la desviacion tipica del precio), bandera sana (misma regla que horas_sanas 0,95). Escribe out_rf5_ciego/cobertura_bruta_DIA.json (atomico, idempotente por sha de codigo).
Funciones puras (agrega_horas) testeadas con fixtures sinteticas."""
import os, sys, json, glob, hashlib
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
DEVP = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'; DL = '/root/polymarket-research-datalogs/'; TXD = '/mnt/HC_Volume_106538179/libro5_tx/'
OUT = os.environ.get('RF5_OUT', HV + 'out_rf5_ciego/')
UMBRAL_HORA = 0.95; NMIN_HORA = 50

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

def agrega_horas(chain, tev, umbral=UMBRAL_HORA, nmin=NMIN_HORA):
    """chain: DataFrame (ts_est, side, tx, price, sh, token_id, src) de fills de makers (salida de reconstruir); tev: set de tx presentes en libro5_tx (x-1..x+1).
    Devuelve dict(units, con_tx, cov, horas=[...]) sobre side 0 y SIN filtrar horas. 'sana' = misma regla que horas_sanas (cobertura de fills src=='tx_ws' >= umbral y n >= nmin, sobre todos los lados)."""
    t = pd.to_datetime(chain.ts_est, unit='s', utc=True); chain = chain.assign(dia=t.dt.strftime('%Y-%m-%d').values, hora=t.dt.hour.values)
    tev = set(tev); c0 = chain[chain.side.values == 0]; tx0 = c0.tx.astype(str); units = set(tx0); con = units & tev
    horas = []
    for (d, h), g in chain.groupby(['dia', 'hora']):
        s0 = g[g.side.values == 0]; u = set(s0.tx.astype(str)); cob = float((g.src == 'tx_ws').mean()); n = int(len(g))
        vol = g.assign(p=g.price.astype(float)).groupby('token_id').p.std().dropna(); nocional = float((g.price.astype(float) * g.sh.astype(float)).sum())
        horas.append(dict(dia=d, hora=int(h), n_fills=n, units=len(u), con_tx=len(u & tev), cob_fills_tx_ws=cob, nocional_usd=nocional, vol_precio=(float(vol.mean()) if len(vol) else None), sana=bool(n >= nmin and cob >= umbral)))
    return dict(units=len(units), con_tx=len(con), cov=(len(con) / len(units) if units else None), horas=horas)

def resumen_excluidas_vs_validas(horas):
    """volumen (nocional, fills) y volatilidad media de las horas excluidas (no sanas) frente a las validas (descriptivo C1)."""
    out = {}
    for nom, sel in (('excluidas', [h for h in horas if not h['sana']]), ('validas', [h for h in horas if h['sana']])):
        v = [h['vol_precio'] for h in sel if h['vol_precio'] is not None]
        out[nom] = dict(horas=len(sel), fills=int(sum(h['n_fills'] for h in sel)), nocional_usd=float(sum(h['nocional_usd'] for h in sel)), nocional_medio_por_hora=(float(sum(h['nocional_usd'] for h in sel) / len(sel)) if sel else None), vol_precio_media=(float(np.mean(v)) if v else None))
    return out

def calcula(x, dl=None, txd=None, devp=None, keep=None):
    """cadena de prep_day.py hasta 'chain' (sin filtrar). Devuelve dict serializable o None si falta alguna fuente (el llamador decide PENDING/INCOMPLETE)."""
    dl = dl or DL; txd = txd or TXD
    if devp: sys.path.insert(0, devp + 'captura_prints')                  # solo tests/forzado explicito
    else:
        import hashlib; sys.path.insert(0, HV)                              # copia LOCAL byte a byte de dev/captura_prints/reconstructor_relleno.py (sha pinned): sin rutas a dev en ejecucion
        if hashlib.sha256(open(HV + 'reconstructor_relleno.py', 'rb').read()).hexdigest()[:16] != 'cdfe43e469f86d40': raise ValueError('reconstructor_relleno.py cambio (sha): fail-closed')
    import reconstructor_relleno as RR
    ms = dl + f'sa_ms/ms_{x}.npz'; files = sorted(glob.glob((keep or dl + 'keep_onchain_re_as_b/') + f'onchain_fills_{x}*.csv.gz'))
    if not os.path.exists(ms) or not files: return None
    z = np.load(ms, allow_pickle=True); tok5 = set(tt for tt, r in zip(z['tokens'], z['tmap']) if r[1] == '5min'); del z
    ch = []
    for f in files:
        for c in pd.read_csv(f, usecols=['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'], dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=400000): ch.append(c[c.token_id.isin(tok5)])
    fills = RR.fills_makers(pd.concat(ch)); del ch
    dd = pd.Timestamp(x); fr = []; tfiles = []
    for dday in [(dd + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]:
        for f in sorted(glob.glob(txd + f'libro5_tx_{dday}_*.csv.gz')): tfiles.append(f); fr.append(pd.read_csv(f, header=None, names=['t_ev', 'token', 'tx', 'recv'], dtype={'token': str, 'tx': str}))
    tws, _ = RR.tx_ws(fr, con_tokens=False); del fr
    chain = RR.reconstruir(fills, tws); del fills
    r = agrega_horas(chain, set(tws.index.astype(str))); ok = RR.horas_sanas(chain, UMBRAL_HORA, NMIN_HORA)
    r.update(dia=x, resumen=resumen_excluidas_vs_validas(r['horas']), horas_malas_propias=sorted(h for h in range(24) if (x, h) not in ok),
             fuentes=dict(onchain=[os.path.basename(f) for f in files], libro5_tx=[os.path.basename(f) for f in tfiles], ms_npz=os.path.basename(ms)), codigo_sha=sha(os.path.abspath(__file__)))
    return r

def obtener(x, out=None, hoy=None, **kw):
    """lee/crea out/cobertura_bruta_X.json. Cache solo si el dia x ya termino hace >=2 dias (libro5_tx de x+1 completo) y mismo sha de codigo."""
    import time
    out = out or OUT; p = out + f'cobertura_bruta_{x}.json'; me = sha(os.path.abspath(__file__))
    if os.path.exists(p):
        try:
            j = json.load(open(p))
            if j.get('codigo_sha') == me: return j
        except Exception: pass
    r = calcula(x, **kw)
    if r is None: return None
    json.dump(r, open(p + '.tmp', 'w'), indent=1); os.replace(p + '.tmp', p); return r

if __name__ == '__main__':
    for d in sys.argv[1:]:
        r = obtener(d); print(d, 'SIN_FUENTE' if r is None else dict(units=r['units'], con_tx=r['con_tx'], cov=r['cov'], malas=r['horas_malas_propias']))
