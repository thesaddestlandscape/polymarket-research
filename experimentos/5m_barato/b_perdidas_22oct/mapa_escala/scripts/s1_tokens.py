# s1: mapa token -> (coin, marco, mid, fin_epoch, lado) desde filas k del m15_registro (06..21-Oct y 22 parcial). Solo lectura.
import subprocess, json, sys
from datetime import datetime
V='/mnt/HC_Volume_106538179/m15_registro/'
out={}
for d in range(5,23):
    f=f'{V}m15_registro_2026-10-{d:02d}.csv.'+('tmp' if d==22 else 'gz')
    p=subprocess.run(f"zcat {f} 2>/dev/null | grep -a '^k,'",shell=True,capture_output=True,text=True)
    n=0
    for ln in p.stdout.split('\n'):
        c=ln.split(',')
        if len(c)<8 or c[0]!='k': continue
        try: fin=int(datetime.fromisoformat(c[6]).timestamp())
        except Exception: continue
        out[c[2]]=[c[3],c[4],c[5],fin,c[7]]; n+=1
    print(d,n,len(out),flush=True)
json.dump(out,open('/root/polymarket-research-datalogs/mapa_escala/tokens.json','w'))
