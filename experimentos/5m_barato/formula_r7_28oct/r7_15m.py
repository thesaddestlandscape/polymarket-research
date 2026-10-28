import sys, os, subprocess, gzip, datetime, numpy as np
E4 = '/root/polymarket-research/experimentos/5m_barato/'
sys.path.insert(0, E4 + 'formula_r3_28oct'); import identity3 as I
OUT = E4 + 'formula_r7_28oct/k15/'
AWK = r'''BEGIN { FS = ","; n = 0 }
$1 == "k" { if ($4 == "BTC" && $5 == "15min" && ($8 == "YES" || $8 == "NO") && !($3 in ID)) { ID[$3] = n; print n, $7, $8 > KF; n++ } next }
$1 == "q" { if ($3 in ID) { r = $8; if (r !~ /^[0-9.]+$/) r = $2; if ($4 ~ /^[0-9.]+$/ && $5 ~ /^[0-9.]+$/ && ($4 + 0) < ($5 + 0)) print r, ID[$3], $4, $5, $6 > QF } }'''
def run(day):
    out = OUT + 'k_%s.npz' % day
    if os.path.exists(out): return
    kf = OUT + 'tmp_k_%s.txt' % day; qf = OUT + 'tmp_q_%s.txt' % day
    subprocess.run(['bash', '-c', "nice -n 19 ionice -c3 zcat '%s' | LC_ALL=C gawk -v KF='%s' -v QF='%s' '%s'" % ('/mnt/HC_Volume_106538179/m15_registro/m15_registro_%s.csv.gz' % day, kf, qf, AWK)], check=True)
    ks = [ln.split() for ln in open(kf)]
    start = np.array([datetime.datetime.fromisoformat(k[1] + ' ' + k[2]).timestamp() for k in ks]); side = np.array([0 if k[3] == 'YES' else 1 for k in ks], np.int8)
    q = np.loadtxt(qf, ndmin=2) if os.path.getsize(qf) else np.zeros((0, 5))
    o = np.lexsort((q[:, 0], q[:, 1])); q = q[o]
    np.savez_compressed(out, kstart=start, kside=side, qt=q[:, 0], qk=q[:, 1].astype(np.int32), qbb=q[:, 2], qba=q[:, 3], qbs=q[:, 4].astype(np.float32))
    os.remove(kf); os.remove(qf); print(day, 'ok tokens', len(ks), 'q', len(q), flush=True)
if __name__ == '__main__':
    for d in sorted(f[2:12] for f in os.listdir(E4 + 'formula_r6_28oct/fills') if f.startswith('f_')): run(d)
