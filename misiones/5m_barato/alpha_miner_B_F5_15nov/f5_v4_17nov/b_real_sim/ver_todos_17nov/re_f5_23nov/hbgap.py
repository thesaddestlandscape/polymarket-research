# Variante de scratchpad/hb.py (chief): mismas filas q (recepcion c5 = campo 8) por conexion coin#5min, pero vuelca CADA hueco >15 s: dia conn t_ini_ms t_fin_ms dur_s
import sys, subprocess, numpy as np, collections, array
d = sys.argv[1]; f = f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{d}.csv.gz'
p = subprocess.Popen(['bash','-c',f"nice -n 19 ionice -c3 zcat {f} | awk -F, '$1==\"k\"||$1==\"q\"{{print $1\",\"$3\",\"$4\",\"$5\",\"$8}}'"], stdout=subprocess.PIPE, text=True)
m = {}; r = collections.defaultdict(lambda: array.array("q"))
for l in p.stdout:
    a = l.rstrip('\n').split(',')
    if a[0] == 'k': m[a[1]] = a[2] + '#' + a[3]
    elif a[1] in m and m[a[1]] in ('ETH#5min','SOL#5min','XRP#5min'):
        try: r[m[a[1]]].append(int(a[4]))
        except ValueError: pass
for c in sorted(r):
    x = np.sort(np.frombuffer(r[c], dtype=np.int64)); g = np.diff(x)
    for i in np.where(g > 15000)[0]: print(d, c, int(x[i]), int(x[i+1]), round(g[i]/1000, 1))
    print(d, c, 'PRIMERA_ULTIMA', int(x[0]), int(x[-1]), -1)
