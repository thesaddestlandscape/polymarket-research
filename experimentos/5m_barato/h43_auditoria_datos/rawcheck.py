"""Cruce raw (datalogs onchain_fills_D) vs m5_onchain_D: filas F de tokens BTC 5min (mapa kall del vigia) y sus M/F por tx. Solo lectura."""
import csv, gzip, sys
d=sys.argv[1]
toks=set()
for c in csv.reader(open("/root/polymarket-research-datalogs/vigia_5m_barato_r5k/2026-10-17/kall.csv")):
    if c[2]=="5min" and c[1]=="BTC": toks.add(c[0])
def cnt(f):
    n=0; keys=set(); vol=0.0
    with gzip.open(f,"rt",errors="replace") as fh:
        rd=csv.reader(fh); next(rd)
        for c in rd:
            if c[0]=="F" and c[9] in toks:
                n+=1; keys.add((c[3],c[4]))
    return n,keys
a,ka=cnt(f"/root/polymarket-research-datalogs/onchain_fills_{d}.csv.gz")
b,kb=cnt(f"/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz")
print(d,"raw F BTC5m",a,"m5_onchain F BTC5m",b,"solo raw",len(ka-kb),"solo m5",len(kb-ka))
