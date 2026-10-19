import sys, glob, collections
sys.path.insert(0, '.')
from r5k_io import *
S='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/d'
tok = tokens_btc5([f'{S}/k_2026-10-17.csv', f'{S}/k_2026-10-18.csv'])
tg = sorted(glob.glob(S+'/libro5_ms_2026-10-18_3349631.TG.gz'))
ws = [e for e in eventos_libro5(tg, [], tok) if e[0]=='T']
ch = banda_cadena(['/root/polymarket-research-datalogs/vigia_5m_barato_r5k/2026-10-18/out/band_2026-10-18.csv.gz'])
# mercado con muchos eventos
mk_ws = collections.Counter(tok[e[3]][0] for e in ws)
mk_ch = collections.Counter(r['mkt'] for r in ch)
com = [m for m in mk_ws if m in mk_ch]
print(len(com), 'mercados comunes')
m = sorted(com, key=lambda m: -mk_ch[m])[3]
fin = [v[2] for t,v in tok.items() if v[0]==m][0]
print('mkt', m, 'fin', fin)
print('--- WS (todo el mercado, banda sin filtrar) ---')
rows=[]
for e in ws:
    mk, lado, f = tok[e[3]]
    if mk!=m: continue
    rows.append((e[1]/1000, 'WS', lado, e[4], e[5], e[6], fin-e[1]/1000))
for r in ch:
    if r['mkt']==m: rows.append((r['ts'],'CH', r['lado'], r['pc'], '', r['acc'], r['T'], r['tx'][:8]))
rows.sort()
n=0
for r in rows:
    if r[6] is not None and 55<r[6]<305:
        print(r); n+=1
        if n>70: break
