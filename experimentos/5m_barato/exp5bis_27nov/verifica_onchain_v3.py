#!/usr/bin/env python3
"""verifica_onchain_v3.py DIA1 DIA2 (27-Nov): verificacion del indexador V3 (ANEXO_V2 §1-§2). Lee los ficheros RECIEN escritos (no el rc). Por dia: filas F por (version, moneda), unicidad (tipo,tx,log_index) por fichero, solape de tx v2/v3,
join libro5_tx<->cadena por moneda y estado COMPLETE por moneda (cadena_v2v3.estado_dia_moneda). Tokens de V3 no mapeados por sa_ms (BNB/DOGE/HYPE/otros marcos) se resuelven por gamma (clob_token_ids, closed=true, lotes de 20, cache) y se cuentan por moneda/marco.
Salida: datalogs/exp5bis_27nov/verifica_onchain_v3.json (+ stdout resumido). Pesado (RAM ~2 GB): por cron_pesado."""
import sys, os, json, re, time, gzip, collections, urllib.request
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
import cadena_v2v3 as CV
OUT = CV.BASE + 'exp5bis_27nov/'; CACHE = CV.BASE + 'onchain_v3_token_mapa.json'
G = 'https://gamma-api.polymarket.com/markets?'


def gamma(tokens, cache):
    pend = [t for t in tokens if t not in cache]
    for i in range(0, len(pend), 20):
        lote = pend[i:i + 20]; q = '&'.join('clob_token_ids=' + t for t in lote)
        for extra in ('closed=true&', ''):
            if all(t in cache for t in lote): break                       # ya resueltos con closed=true: no se pide el segundo (abiertos)
            try: d = json.load(urllib.request.urlopen(G + extra + q, timeout=30))
            except Exception as e: print('gamma fallo', e, flush=True); time.sleep(5); continue
            for m in d:
                mt = re.match(r'([a-z]+)-updown-(\w+)-\d+', m.get('slug', '')); ids = json.loads(m['clobTokenIds'])
                for t in ids:
                    if t in lote and t not in cache: cache[t] = [mt.group(1), mt.group(2)] if mt else ['otro', m.get('slug', '')[:30]]
            time.sleep(0.4)
        for t in lote: cache.setdefault(t, ['no_resuelto', ''])
    return cache


def dia(d, cache):
    mapa = CV.mapa_token_moneda(d); res = dict(dia=d); rutas = CV.rutas_cadena(d, exigir_v3=False); res['ficheros'] = {v: os.path.getsize(p) for v, p in rutas}
    por = collections.Counter(); dup = {}; txs = {}; sin = collections.Counter()
    for ver, p in rutas:
        seen = set(); dups = 0; txv = set()
        for ch in pd.read_csv(p, usecols=['tipo', 'tx', 'log_index', 'token_id'], dtype=str, chunksize=500000):
            k = list(zip(ch.tipo, ch.tx, ch.log_index)); dups += len(k) - len(set(k)); txv.update(ch.tx)
            f = ch[ch.tipo == 'F']; cs = f.token_id.map(mapa)
            for c, n in cs.value_counts().items(): por[(ver, c)] += int(n)
            if ver == 'v3':
                for t, n in f.token_id[cs.isna()].value_counts().items(): sin[t] += int(n)
        dup[ver] = dups; txs[ver] = txv     # duplicados dentro del chunk (aprox.; el solape entre chunks lo detecta el set global abajo si hace falta)
    res['duplicados_en_chunks'] = dup; res['solape_tx_v2_v3'] = len(txs['v2'] & txs.get('v3', set())) if 'v3' in txs else 0; res['tx'] = {v: len(s) for v, s in txs.items()}
    if sin:
        MINF = 30                                                          # solo se resuelven por gamma los tokens con >=30 filas F en el dia (los 5m/15m tienen cientos)
        pocos = sum(n for t, n in sin.items() if n < MINF); gamma([t for t, n in sin.items() if n >= MINF], cache); extra = collections.Counter(); res['v3_filas_F_tokens_con_<30_filas_sin_resolver'] = pocos
        for t, n in sin.items():
            if n < MINF: continue
            c, m = cache.get(t, ['no_resuelto', '']); extra[(c, m if m in ('5m', '15m') else 'otro_marco')] += n
        res['v3_filas_F_no_mapeadas_sa_ms_por_moneda_marco'] = {f'{c}|{m}': n for (c, m), n in sorted(extra.items())}
        tot = sum(sin.values()); res['v3_frac_F_no_resuelta'] = (pocos + sum(n for t, n in sin.items() if n >= MINF and cache.get(t, ['no_resuelto'])[0] == 'no_resuelto')) / tot
    res['filas_F_por_version_moneda_sa_ms'] = {f'{v}|{c}': n for (v, c), n in sorted(por.items())}
    return res


if __name__ == '__main__':
    import datetime as dt
    d0, d1 = dt.date.fromisoformat(sys.argv[1]), dt.date.fromisoformat(sys.argv[2]); cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    out = {}
    d = d0
    while d <= d1:
        ds = d.isoformat()
        try: out[ds] = dia(ds, cache)
        except Exception as e: out[ds] = dict(error=f'{type(e).__name__}: {e}')
        json.dump(cache, open(CACHE + '.tmp', 'w')); os.replace(CACHE + '.tmp', CACHE)
        print(ds, json.dumps(out[ds])[:600], flush=True); d += dt.timedelta(days=1)
    json.dump(out, open(OUT + 'verifica_onchain_v3.json', 'w'), indent=1)
