import sys, glob, collections
sys.path.insert(0, '.')
from r5k_io import *
S='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/d'
tok = tokens_btc5([f'{S}/k_2026-10-17.csv', f'{S}/k_2026-10-18.csv'])
print(len(tok), 'tokens btc5')
tg = sorted(glob.glob(S+'/libro5_ms_2026-10-18_3349631.TG.gz'))
ws = []
for e in eventos_libro5(tg, [], tok):
    if e[0]=='T': ws.append(e)
print(len(ws))
# rango
print(ws[0][1], ws[-1][1])
ch = banda_cadena(['/root/polymarket-research-datalogs/vigia_5m_barato_r5k/2026-10-18/out/band_2026-10-18.csv.gz'])
print(len(ch), ch[0])
import datetime
# primer mercado: contar tx con varios filas
cnt = collections.Counter((r['tx'], r['mkt'], r['lado'], round(r['pc'],2)) for r in ch)
print(collections.Counter(cnt.values()).most_common(6))
