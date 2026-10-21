import json,sys
import pyarrow.parquet as pq, pyarrow.compute as pc, pyarrow as pa
S,d=sys.argv[1],sys.argv[2]
W=json.load(open(S+'/cp_wallets.json'))
CA='/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
cc=['is_tk','maker','taker','side','act','mkt','lado','fin','ts','maker_amt','taker_amt','fee']
pf=pq.ParquetFile(CA+f'fills_{d}.parquet'); vs=pa.array(W)
out=[]; nm={}; nt={}
for i in range(pf.num_row_groups):
    t=pf.read_row_group(i,columns=cc)
    mk=pc.is_in(t['maker'],value_set=vs)
    tk=t.filter(pc.and_(mk,pc.equal(t['is_tk'],1)))
    out+=tk.to_pylist()
    mm=t.filter(pc.and_(mk,pc.equal(t['is_tk'],0)))
    for w,c in zip(*[x.to_pylist() for x in pc.value_counts(mm['maker']).flatten()]): nm[w]=nm.get(w,0)+c
    # filas en que la wallet es la tomadora de un relleno maker (taker field), solo conteo
    tt=t.filter(pc.is_in(t['taker'],value_set=vs))
    for w,c in zip(*[x.to_pylist() for x in pc.value_counts(tt['taker']).flatten()]): nt[w]=nt.get(w,0)+c
json.dump(dict(tk=out,n_maker=nm,n_taker_field=nt),open(S+f'/cp_{d}.json','w')); print(d,len(out),sorted(nm.items(),key=lambda x:-x[1])[:3])
