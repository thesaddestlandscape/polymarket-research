#!/usr/bin/env python3
"""preal_resolver.py - desenlace OFICIAL (gamma closed=true) de los mercados 5m de `preal/ask_t0_DIA.csv.gz`. Uso: python3 -I preal_resolver.py DIA [DIA ...]  |  --todos
Cache propia /root/polymarket-research-datalogs/preal/desenl_cache.json {id: 'YES'|'NO'} sembrada (solo lectura) con maker_ms_desenlaces_cache.json. Sin resolucion clara -> ausente (missing), nunca inventada.
Sale con codigo 3 si la cobertura de algun dia <99 %. Solo GET publico de gamma-api. Escritura atomica, lock fcntl."""
import sys, os, json, glob, gzip, csv, time, fcntl, requests
D = '/root/polymarket-research-datalogs/preal'; SEED = '/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'
def ids_dia(d):
    f = f'{D}/ask_t0_{d}.csv.gz'; s = set()
    with gzip.open(f, 'rt') as r:
        for row in csv.DictReader(r): s.add(row['mid'])
    return s
def main():
    a = sys.argv[1:]; dias = sorted(os.path.basename(f)[7:17] for f in glob.glob(f'{D}/ask_t0_*.csv.gz')) if a == ['--todos'] else a
    lk = open(f'{D}/.lock_res', 'w'); fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
    try: c = json.load(open(f'{D}/desenl_cache.json'))
    except Exception: c = {}
    try: seed = json.load(open(SEED))
    except Exception: seed = {}
    por_dia = {d: ids_dia(d) for d in dias}; todos = set().union(*por_dia.values()) if por_dia else set()
    for m in todos:
        if m not in c and seed.get(m) in ('YES', 'NO'): c[m] = seed[m]
    pend = sorted(m for m in todos if m not in c); ses = requests.Session(); ng = 0
    for k in range(0, len(pend), 40):
        try:
            r = ses.get('https://gamma-api.polymarket.com/markets', timeout=25, params=[('id', x) for x in pend[k:k + 40]] + [('closed', 'true'), ('limit', '40')])
            for m in r.json() or []:
                pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
                if pr and float(pr[0]) >= 0.999: c[str(m['id'])] = 'YES'; ng += 1
                elif pr and float(pr[1]) >= 0.999: c[str(m['id'])] = 'NO'; ng += 1
        except Exception as e: print('lote', k // 40, type(e).__name__, file=sys.stderr)
        time.sleep(0.15)
    tmp = f'{D}/desenl_cache.json.tmp'; json.dump(c, open(tmp, 'w')); os.replace(tmp, f'{D}/desenl_cache.json')
    bad = 0
    for d in dias:
        n = len(por_dia[d]); ok = sum(1 for m in por_dia[d] if m in c); cov = ok / n if n else 0
        print(f'{d}: mercados {n} con desenlace oficial {ok} ({100 * cov:.2f} %)'); bad += cov < 0.99
    print('gamma nuevos', ng, 'pendientes sin resolver', sum(1 for m in todos if m not in c)); sys.exit(3 if bad else 0)
if __name__ == '__main__': main()
