import sys
sys.path.insert(0,'.')
from r5k_io import *
S='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/a6/d'
tok=tokens_btc5([f'{S}/k_2026-10-17.csv',f'{S}/k_2026-10-18.csv'])
a=banda_cadena_cruda('/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_2026-10-18.csv.gz',tok)
b=[r for r in banda_cadena(['/root/polymarket-research-datalogs/vigia_5m_barato_r5k/2026-10-18/out/band_2026-10-18.csv.gz']) if True]
ka={(r['tx'],r['li']):r for r in a}; kb={(r['tx'],r['li']):r for r in b}
print('cruda',len(ka),'pass1',len(kb),'en ambas',len(set(ka)&set(kb)))
print('acc cruda',round(sum(r['acc'] for r in ka.values()),1),'pass1',round(sum(r['acc'] for r in kb.values()),1))
dif=[k for k in set(ka)&set(kb) if abs(ka[k]['acc']-kb[k]['acc'])>1e-6 or abs(ka[k]['pc']-kb[k]['pc'])>1e-3 or ka[k]['lado']!=kb[k]['lado']]
print('discrepan en valores',len(dif))
sol=[k for k in set(ka)-set(kb)][:3]; print('solo cruda',len(set(ka)-set(kb)),sol[:2]); print('solo pass1',len(set(kb)-set(ka)))
