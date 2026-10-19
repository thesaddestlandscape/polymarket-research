import sys, collections, gzip, csv
sys.path.insert(0,'.')
from r5k_io import *
S='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/a6/d'
tok = tokens_btc5([f'{S}/k_2026-10-18.csv'])
TX=sys.argv[1]; M=sys.argv[2]
# todas las filas de esa tx en el on-chain crudo (F: maker/taker), no solo banda
inv={t:v for t,v in tok.items()}
rows=[]
with gzip.open('/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_2026-10-18.csv.gz','rt') as fh:
    rd=csv.reader(fh); next(rd)
    for c in rd:
        if c[3].startswith(TX):
            rows.append(c)
for c in rows:
    t=inv.get(c[9]); 
    print(c[0],c[4],c[6][:8],c[7][:8],'side',c[8],(t[1],t[2]) if t else '?', 'maker_amt',c[10],'taker_amt',c[11])
