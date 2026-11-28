#!/usr/bin/env python3
"""cadena_v2v3.py (27-Nov, engineer 5m barato; ANEXO_V2 §1-§2). UNICO punto para: (a) rutas de la cadena V2+V3 de un dia, (b) mapa token->moneda, (c) COMPLETE POR MONEDA (definicion §2). Todo consumidor de onchain_fills debe usar esto, no copiarlo.
Estados por (dia, moneda): COMPLETE | PARTIAL_POR_MONEDA | BLOCKED_V3 | SIN_MAPA | MANIFEST_NO_COMPLETE. Criterios (todos): manifest del dia COMPLETE (se pasa como argumento) Y filas_cadena(moneda; F de V2+V3) >= MIN_FILAS
Y cobertura del join libro5_tx<->cadena (pares (moneda, tx) de libro5_tx cuya tx esta en la cadena V2+V3) >= 0,90 Y fraccion de libro5_tx sin mapear <= 0,10 Y V3 indexado para el dia si la moneda esta en V3_DESDE y dia >= su fecha.
Mapa token->moneda: sa_ms/ms_DIA.npz (ETH/SOL/XRP 5m y 15m) + mapa_extra opcional (BNB/DOGE/HYPE/BTC via gamma clobTokenIds: cache JSON propia). Sin mapa => SIN_MAPA (nunca se asume COMPLETE)."""
import os, json, glob, gzip, collections
import numpy as np
BASE = '/root/polymarket-research-datalogs/'
V2_DIRS = (BASE, '/mnt/HC_Volume_106538179/datalogs_auto/', '/mnt/HC_Volume_106538179/protegido_forward_11nov/')
V3_DIRS = (BASE, '/mnt/HC_Volume_106538179/datalogs_auto/', '/mnt/HC_Volume_106538179/protegido_forward_11nov/', BASE + 'keep_onchain_v3/')
V3_CKPT = BASE + 'onchain_fills_v3_checkpoint.json'
V3_DESDE = {c: '2026-11-23' for c in ('sol', 'xrp', 'bnb', 'doge', 'hype')}      # ANEXO §1: primer 5m v2 de SOL 23-Nov 13:20-13:30Z; el resto por confirmar por slug (hasta entonces el criterio de join manda)
MIN_FILAS = 200; JOIN_MIN = 0.90; SIN_MAPAR_MAX = 0.10
TXD = '/mnt/HC_Volume_106538179/libro5_tx/'


def _primero(dirs, nombre):
    for d in dirs:
        p = d + nombre
        if os.path.exists(p): return p
    return None


def rutas_cadena(dia, exigir_v3=None):
    """-> [('v2', ruta), ('v3', ruta)?]. V2 obligatoria. V3 obligatoria si algun dia>=23-Nov (exigir_v3=None => automatico) : FileNotFoundError si falta (fail loud: leer solo V2 daria SOL/XRP vacios)."""
    r = []; p2 = _primero(V2_DIRS, f'onchain_fills_{dia}.csv.gz')
    if p2 is None: raise FileNotFoundError(f'sin onchain_fills_{dia}')
    r.append(('v2', p2)); p3 = _primero(V3_DIRS, f'onchain_fills_v3_{dia}.csv.gz')
    ex = (dia >= min(V3_DESDE.values())) if exigir_v3 is None else exigir_v3
    if p3: r.append(('v3', p3))
    elif ex: raise FileNotFoundError(f'sin onchain_fills_v3_{dia} (dia >= {min(V3_DESDE.values())}: la cadena V3 es obligatoria)')
    return r


def v3_cubre_dia(dia):
    """True si el checkpoint V3 ya paso del final del dia (o el dia es el actual y el fichero existe): ultimo_bloque -> ts no disponible offline, asi que se usa el mtime del checkpoint y la existencia del fichero del dia siguiente o del actual."""
    try: ck = json.load(open(V3_CKPT))
    except Exception: return False
    import datetime as dt
    sig = (dt.date.fromisoformat(dia) + dt.timedelta(days=1)).isoformat()
    return bool(_primero(V3_DIRS, f'onchain_fills_v3_{sig}.csv.gz') or ck.get('cubre_hasta_dia', '') >= dia)


def mapa_token_moneda(dia, extra=None, marco='5min'):
    z = np.load(BASE + f'sa_ms/ms_{dia}.npz', allow_pickle=True)
    toks = [str(t) for t in z['tokens']]; acts = [str(a).lower() for a in z['tmap'][:, 0]]
    mcs = [str(x) for x in z['tmap'][:, 1]]
    m = {t: a for t, a, mc in zip(toks, acts, mcs) if marco is None or mc == marco}   # por defecto SOLO 5min (libro5_tx y B son 5m; con 15m el join cadena->prints cae por construccion)
    if extra: m.update({str(k): str(v).lower() for k, v in extra.items()})
    return m


def filas_por_moneda(dia, mapa):
    """Filas F (tipo F) de V2+V3 por (version, moneda) y total de F; unicidad por (tipo,tx,log_index) entre versiones => solape. -> (dict, set de tx, dict solape)."""
    import pandas as pd
    cnt = collections.Counter(); txs = set(); vistos = {}; solape = 0; sin = collections.Counter(); txc = collections.defaultdict(set)
    for ver, p in rutas_cadena(dia):
        txv = set()
        for ch in pd.read_csv(p, usecols=['tipo', 'tx', 'token_id'], dtype=str, chunksize=500000):
            txv.update(ch.tx.tolist())
            f = ch[ch.tipo == 'F']
            cs = f.token_id.map(mapa)
            for c, n in cs.value_counts().items(): cnt[(ver, c)] += int(n)
            for c, x in f.tx.groupby(cs): txc[c].update(x.tolist())
            sin[ver] += int(cs.isna().sum()); cnt[(ver, '_F_total')] += len(f)
        vistos[ver] = txv; txs |= txv
    if 'v2' in vistos and 'v3' in vistos: solape = len(vistos['v2'] & vistos['v3'])
    return dict(cnt), txs, dict(solape_tx_v2_v3=solape, F_sin_mapa=dict(sin), tx_por_version={k: len(v) for k, v in vistos.items()}, tx_por_moneda=txc)


def join_libro5tx(dia, mapa, txs):
    """Por moneda: pares unicos (moneda, tx) de libro5_tx (token mapeado) y cuantos tienen su tx en la cadena. Sin mapear = prints cuyo token no esta en el mapa (fraccion sobre el total de pares (token,tx))."""
    tot = collections.defaultdict(set); hit = collections.defaultdict(set); sinm = set(); todos = set(); tx5 = set()
    for f in sorted(glob.glob(TXD + f'libro5_tx_{dia}_*.csv.gz')):
        with gzip.open(f, 'rt') as fh:
            for ln in fh:
                c = ln.rstrip('\n').split(',')
                if len(c) < 4: continue
                k = (c[1], c[2]); todos.add(k); tx5.add(c[2]); m = mapa.get(c[1])
                if m is None: sinm.add(k); continue
                tot[m].add(c[2])
                if c[2] in txs: hit[m].add(c[2])
    return {m: dict(pares=len(v), con_cadena=len(hit[m]), join=(len(hit[m]) / len(v) if v else None)) for m, v in tot.items()}, dict(pares_total=len(todos), sin_mapear=len(sinm), frac_sin_mapear=(len(sinm) / len(todos) if todos else None)), tx5


def estado_dia_moneda(dia, manifest_complete, extra_mapa=None, monedas=('eth', 'sol', 'xrp', 'bnb', 'doge', 'hype', 'btc')):
    """FUNCION UNICA de COMPLETE por moneda. -> dict moneda -> dict(estado, motivos, filas_cadena, join, ...) + clave '_global'."""
    mapa = mapa_token_moneda(dia, extra_mapa); cnt, txs, sol = filas_por_moneda(dia, mapa); jn, jg, tx5 = join_libro5tx(dia, mapa, txs); txc = sol.pop('tx_por_moneda')
    out = {'_global': dict(manifest_complete=bool(manifest_complete), solape=sol, join_global=jg, rutas=[v for v, _ in rutas_cadena(dia, exigir_v3=False)])}
    for c in monedas:
        filas = sum(n for (v, cc), n in cnt.items() if cc == c); mot = []
        v3_req = c in V3_DESDE and dia >= V3_DESDE[c]
        ja = (jn.get(c) or {}).get('join'); tc = txc.get(c, set()); jb = (len(tc & tx5) / len(tc)) if tc else None      # ja: prints libro5_tx con su tx en la cadena; jb: tx de la cadena (F de la moneda) con print en libro5_tx (cae si libro5 estuvo en pausa)
        j = None if (ja is None or jb is None) else min(ja, jb)
        if c not in set(mapa.values()): est = 'SIN_MAPA'; mot.append('sin tokens en el mapa (falta mapa_extra gamma)')
        else:
            est = 'COMPLETE'
            if not manifest_complete: est = 'MANIFEST_NO_COMPLETE'; mot.append('manifest del dia no COMPLETE')
            if v3_req and not v3_cubre_dia(dia): est = 'BLOCKED_V3'; mot.append('V3 no indexado/cubierto para el dia')
            if filas < MIN_FILAS: est = est if est != 'COMPLETE' else 'PARTIAL_POR_MONEDA'; mot.append(f'filas {filas} < {MIN_FILAS}')
            if j is None or j < JOIN_MIN: est = est if est != 'COMPLETE' else 'PARTIAL_POR_MONEDA'; mot.append(f'join {j} < {JOIN_MIN}')
            # §2 'sin mapear <= 0,10' NO es evaluable offline: libro5_tx/cadena traen TODO Polymarket (84 % fuera del mapa por construccion); solo se evalua con un universo updown de gamma (extra_mapa). Se informa, no bloquea.
            if extra_mapa and c in set(str(v).lower() for v in extra_mapa.values()) and (jg['frac_sin_mapear'] or 0) > SIN_MAPAR_MAX: mot.append('INFO: sin mapear alto (universo no restringido)')
        out[c] = dict(estado=est, motivos=mot, filas_F_v2=cnt.get(('v2', c), 0), filas_F_v3=cnt.get(('v3', c), 0), join=j, join_prints_a_cadena=ja, join_cadena_a_prints=jb, pares_libro5tx=(jn.get(c) or {}).get('pares'))
    return out
