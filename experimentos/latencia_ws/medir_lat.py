import gzip, glob, os, time, sys, numpy as np, collections
corte = int(sys.argv[1]) * 1000           # epoch s del cambio de prioridad
b = collections.defaultdict(list)
for f in glob.glob("/mnt/HC_Volume_106538179/libro5_ms/libro5_ms_2026-10-17_*.csv.gz"):
    if time.time() - os.path.getmtime(f) > 3600: continue
    try:
        for l in gzip.open(f, "rt"):
            x = l.rstrip("\n").split(",")
            if x[0] == "T" and x[1].isdigit() and x[6].isdigit():
                te, r = int(x[1]), int(x[6])
                if r < corte - 15 * 60000: continue
                b[(r - corte) // 300000].append(r - te)
    except EOFError: pass
for k in sorted(b):
    a = np.array(b[k]); q = np.percentile(a, [10, 50, 90, 99]).round(0)
    print(f"{'ANTES ' if k < 0 else 'DESPUÉS'} tramo {k:+d} (5 min) n={len(a):5d} sello→recepción p10/50/90/99 = {q} ms")
