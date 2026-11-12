#!/usr/bin/env python3
"""guard_rss.py [--max-rss-mb N=3500] [--min-avail-mb N=1200] [--vmem-kb N=7000000] [--esperar-min N=0] -- CMD...   Ejecuta CMD bajo nice 19 / ionice idle / ulimit -v (VIRTUAL holgado) y VIGILA EL RSS REAL cada 2 s:
mata SOLO el pid que lanzo (nunca pgrep/pkill -f) si su RSS supera --max-rss-mb o si MemAvailable cae bajo --min-avail-mb (proteger observadores). Antes de arrancar espera (hasta --esperar-min) a: fuera de 06-09Z y load5 < 6 y MemAvailable >= 2500 MB.
Codigos: 0 ok, 97 abortado por RSS/memoria, 98 no se dieron las condiciones de arranque. Escribe una linea de estado por 30 s a stderr con RSS pico."""
import os, sys, time, subprocess, signal, datetime as dt


def avail_mb():
    for l in open('/proc/meminfo'):
        if l.startswith('MemAvailable'): return int(l.split()[1]) // 1024


def rss_mb(pid):
    try:
        for l in open(f'/proc/{pid}/status'):
            if l.startswith('VmRSS'): return int(l.split()[1]) // 1024
    except OSError: return -1
    return -1


def ok_arranque():
    h = dt.datetime.now(dt.timezone.utc).hour; l5 = float(open('/proc/loadavg').read().split()[1])
    return (not (6 <= h < 9)) and l5 < 6 and avail_mb() >= 2500, (h, l5, avail_mb())


def main():
    a = sys.argv[1:]; cfg = dict(max_rss=3500, min_avail=1200, vmem=7000000, esperar=0)
    while a and a[0].startswith('--') and a[0] != '--':
        k = a.pop(0); v = int(a.pop(0)); cfg = {**cfg, dict({'--max-rss-mb': 'max_rss', '--min-avail-mb': 'min_avail', '--vmem-kb': 'vmem', '--esperar-min': 'esperar'})[k]: v}
    if a and a[0] == '--': a.pop(0)
    if not a: sys.exit('uso: guard_rss.py [opts] -- CMD...')
    t0 = time.time()
    while True:
        ok, det = ok_arranque()
        if ok: break
        if time.time() - t0 > cfg['esperar'] * 60: print('guard: condiciones de arranque no cumplidas (hora, load5, MemAvailable)', det, file=sys.stderr, flush=True); sys.exit(98)
        time.sleep(30)
    p = subprocess.Popen(['nice', '-n', '19', 'ionice', '-c3', 'bash', '-c', f'ulimit -v {cfg["vmem"]}; exec "$@"', '_'] + a); pico = 0; last = 0
    try:
        while p.poll() is None:
            r = rss_mb(p.pid); pico = max(pico, r); av = avail_mb()
            if r > cfg['max_rss'] or av < cfg['min_avail']:
                print(f'guard: RSS {r} MB (tope {cfg["max_rss"]}) / MemAvailable {av} MB (min {cfg["min_avail"]}): mato SOLO pid {p.pid}', file=sys.stderr, flush=True); p.kill(); p.wait(); sys.exit(97)
            if time.time() - last > 30: last = time.time(); print(f'guard: pid {p.pid} RSS {r} MB pico {pico} MemAvailable {av}', file=sys.stderr, flush=True)
            time.sleep(2)
    except KeyboardInterrupt: p.kill(); raise
    print(f'guard: fin rc={p.returncode} RSS pico {pico} MB', file=sys.stderr, flush=True); sys.exit(p.returncode)


if __name__ == '__main__': main()
