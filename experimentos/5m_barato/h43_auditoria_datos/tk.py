import csv, gzip, sys
from collections import Counter
VOL="/mnt/HC_Volume_106538179/m5_onchain"
for d in sys.argv[1:]:
    cm=Counter(); ct=Counter(); n=0
    with gzip.open(f"{VOL}/m5_onchain_{d}.csv.gz","rt") as fh:
        rd=csv.reader(fh); next(rd)
        for c in rd:
            if c[0]!="F": continue
            n+=1; ct[c[7]]+=1; cm[c[6]]+=1
    print(d,n,"top takers",[(a[:10],k) for a,k in ct.most_common(3)],"top makers",[(a[:10],k) for a,k in cm.most_common(3)],flush=True)
