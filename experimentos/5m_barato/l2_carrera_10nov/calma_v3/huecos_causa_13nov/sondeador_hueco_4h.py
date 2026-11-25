#!/usr/bin/env python3
"""sondeador_hueco_4h.py -- sondeador PASIVO (solo lectura de /proc y `ss`), 1 muestra/s durante xx:50..(xx+1):08 UTC de las horas 03,07,11,15,19,23.
No importa nada del repo, no toca procesos ni ficheros existentes, sin red. Salida: /root/polymarket-research-datalogs/sondeo_hueco_YYYY-MM-DD_HH.csv.gz (fuera de git, retencion 5 d).
Uso: sondeador_hueco_4h.py            (calcula su ventana: desde ahora hasta el fin de la ventana vigente; sale si no hay ventana)
     sondeador_hueco_4h.py --dur N    (prueba: N segundos desde ya, fichero sondeo_hueco_prueba_*)
Por segundo: load1/5, CPU% global (user/sys/iowait/steal), MemAvailable, swap usado, pswpin/out, red rx/tx bytes+drops (iface por defecto),
 y para PADRE=observadores_fase0.py e HIJO=libro_estado_ws.py --hijo: CPU%, RSS, swap, hilos (R/D/S), ctxt voluntarios/involuntarios, TIEMPO DE ESPERA EN COLA
 de ejecucion (schedstat, ms/s) -> inanicion del lector; del hijo ademas: sockets TCP (n, suma y max de Recv-Q, suma y delta de bytes_received, retrans, lista
 [bytes_recibidos_delta por conexion]) y crecimiento de los ficheros libro5_ms/libro5_tx del dia. Nota: NO mide el pipe hijo->padre (abrirlo desde fuera podria alterarlo)."""
import glob, gzip, json, os, re, subprocess, sys, time
from datetime import datetime, timedelta, timezone
OUT = '/root/polymarket-research-datalogs'; RET_D = 5; TCK = os.sysconf('SC_CLK_TCK')
HORAS = (3, 7, 11, 15, 19, 23)
COLS = ['ts', 'load1', 'load5', 'cpu_user', 'cpu_sys', 'cpu_iow', 'cpu_steal', 'memav_mb', 'swap_mb', 'pswpin', 'pswpout', 'rx_kB', 'tx_kB', 'rx_drop',
        'P_pid', 'P_cpu', 'P_rss_mb', 'P_swap_mb', 'P_thr', 'P_thrR', 'P_thrD', 'P_ctxv', 'P_ctxi', 'P_rqwait_ms',
        'H_pid', 'H_cpu', 'H_rss_mb', 'H_swap_mb', 'H_thr', 'H_thrR', 'H_thrD', 'H_ctxv', 'H_ctxi', 'H_rqwait_ms',
        'H_nsock', 'H_recvq_sum', 'H_recvq_max', 'H_bytes_rx_delta', 'H_retrans', 'H_conn_deltas', 'L5ms_dB', 'L5tx_dB', 'gamma_conns_por_pid']

def ventana(ahora):
    """(ini, fin) de la ventana que contiene 'ahora' o None. Ventana de hora H: H:50:00 .. (H+1):08:00."""
    for off in (0, -1):
        base = (ahora + timedelta(days=off)).replace(hour=0, minute=0, second=0, microsecond=0)
        for h in HORAS:
            ini = base + timedelta(hours=h, minutes=50); fin = base + timedelta(hours=h + 1, minutes=8)
            if ini - timedelta(seconds=90) <= ahora < fin: return max(ini, ahora - timedelta(0)), fin
    return None

def rd(p):
    try:
        with open(p) as f: return f.read()
    except Exception: return ''

def buscar_pids():
    """argv exacto (no subcadena: un bash -c con esos nombres no cuenta)."""
    P = H = None
    for d in os.listdir('/proc'):
        if not d.isdigit(): continue
        a = rd(f'/proc/{d}/cmdline').split('\0')
        if len(a) < 3 or 'python' not in os.path.basename(a[0]): continue
        a = [x for x in a if x]
        if a[-1] == '--hijo' and a[-2].endswith('libro_estado_ws.py'): H = int(d)
        elif a[-1] == 'observadores_fase0.py' or a[-1].endswith('/observadores_fase0.py'): P = int(d)
    return P, H

def proc(pid, prev):
    """-> dict de metricas del pid; prev guarda acumulados para deltas."""
    if not pid: return {}
    st = rd(f'/proc/{pid}/stat')
    if not st: return {}
    f = st[st.rfind(')') + 2:].split(); cpu_t = (int(f[11]) + int(f[12])) / TCK
    s = rd(f'/proc/{pid}/status'); g = lambda k: (re.search(rf'^{k}:\s+(\d+)', s, re.M) or [0, 0])[1]
    ss = rd(f'/proc/{pid}/schedstat').split(); rq = int(ss[1]) / 1e6 if len(ss) >= 2 else 0.0
    thr = {'R': 0, 'D': 0, 'S': 0}
    try:
        for t in os.listdir(f'/proc/{pid}/task'):
            x = rd(f'/proc/{pid}/task/{t}/stat')
            if x:
                e = x[x.rfind(')') + 2:][0]; thr[e if e in 'RD' else 'S'] += 1
    except Exception: pass
    now = time.time(); a = prev.get(pid); out = {}
    cv, ci = int(g('voluntary_ctxt_switches')), int(g('nonvoluntary_ctxt_switches'))
    if a:
        dt = max(now - a[0], 1e-3); out = dict(cpu=round(100 * (cpu_t - a[1]) / dt, 1), ctxv=cv - a[2], ctxi=ci - a[3], rq=round((rq - a[4]) / dt, 1))
    prev[pid] = (now, cpu_t, cv, ci, rq)
    out.update(rss_mb=round(int(g('VmRSS')) / 1024, 1), swap_mb=round(int(g('VmSwap')) / 1024, 1), thr=int(g('Threads')), thrR=thr['R'], thrD=thr['D'])
    return out

def ips(host):
    import socket
    try: return {x[4][0] for x in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)}
    except Exception: return set()

def socks(pid, prev, gamma=()):
    try: o = subprocess.run(['ss', '-tinpH', 'state', 'established'], capture_output=True, text=True, timeout=3).stdout
    except Exception: return {}
    lines = o.splitlines(); conns = []; gp = {}
    for l in lines:                      # conexiones establecidas hacia gamma-api por pid (diagnostico del 429)
        p = l.split()
        if len(p) >= 5 and p[4].rsplit(':', 1)[0].strip('[]') in gamma:
            m = re.search(r'pid=(\d+)', l)
            if m: gp[m.group(1)] = gp.get(m.group(1), 0) + 1
    for i, l in enumerate(lines):
        if f'pid={pid},' in l and i + 1 < len(lines):
            p = l.split(); rq = int(p[0]); det = lines[i + 1]; key = (p[3], p[4])
            br = re.search(r'bytes_received:(\d+)', det); rt = re.search(r'retrans:\d+/(\d+)', det)
            conns.append((key, rq, int(br.group(1)) if br else 0, int(rt.group(1)) if rt else 0))
    deltas = [c[2] - prev.get(c[0], c[2]) for c in conns]
    for c in conns: prev[c[0]] = c[2]
    return dict(nsock=len(conns), rqs=sum(c[1] for c in conns), rqm=max([c[1] for c in conns] or [0]), brd=sum(deltas), retr=sum(c[3] for c in conns), cd=json.dumps(deltas), gp=json.dumps(gp))

def main():
    prueba = '--dur' in sys.argv
    ahora = datetime.now(timezone.utc)
    if prueba: ini, fin = ahora, ahora + timedelta(seconds=int(sys.argv[sys.argv.index('--dur') + 1]))
    else:
        v = ventana(ahora)
        if not v: print('sin ventana'); return
        ini, fin = v
    # retencion
    for f in glob.glob(f'{OUT}/sondeo_hueco_*.csv.gz'):
        if time.time() - os.path.getmtime(f) > RET_D * 86400:
            try: os.remove(f)
            except OSError: pass
    nom = f'{OUT}/sondeo_hueco_{"prueba_" if prueba else ""}{ini:%Y-%m-%d_%H%M}.csv.gz'
    gz = gzip.open(nom, 'at', compresslevel=6)
    if gz.tell() == 0: gz.write(','.join(COLS) + '\n')
    prevP, prevS, pv = {}, {}, {}; cpu0 = None; net0 = None; sw0 = None; L5 = {}; pidP = pidH = None; ult_pids = 0; ult_ips = 0; gamma = set(); n = 0
    def hoy_ficheros():
        d = datetime.now(timezone.utc).strftime('%Y-%m-%d'); r = {}
        for k, pat in (('ms', f'/mnt/HC_Volume_106538179/libro5_ms/libro5_ms_{d}_*'), ('tx', f'/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_{d}_*')):
            r[k] = sum(os.path.getsize(f) for f in glob.glob(pat))
        return r
    while datetime.now(timezone.utc) < fin:
        t0 = time.time()
        if t0 - ult_pids > 30: pidP, pidH = buscar_pids(); ult_pids = t0
        la = rd('/proc/loadavg').split(); c = [int(x) for x in rd('/proc/stat').split('\n')[0].split()[1:9]]  # user nice sys idle iow irq sirq steal
        tot = sum(c); r = {}
        if cpu0:
            dt = max(tot - cpu0[0], 1); r.update(cpu_user=round(100 * (c[0] + c[1] - cpu0[1]) / dt, 1), cpu_sys=round(100 * (c[2] - cpu0[2]) / dt, 1), cpu_iow=round(100 * (c[4] - cpu0[3]) / dt, 1), cpu_steal=round(100 * (c[7] - cpu0[4]) / dt, 1))
        cpu0 = (tot, c[0] + c[1], c[2], c[4], c[7])
        mi = rd('/proc/meminfo'); mg = lambda k: int((re.search(rf'^{k}:\s+(\d+)', mi, re.M) or [0, 0])[1])
        vm = rd('/proc/vmstat'); vg = lambda k: int((re.search(rf'^{k} (\d+)', vm, re.M) or [0, 0])[1])
        sw = (vg('pswpin'), vg('pswpout'))
        nd = rd('/proc/net/dev'); best = None
        for l in nd.splitlines()[2:]:
            nm, v = l.split(':'); v = v.split(); 
            if nm.strip() not in ('lo',) and (best is None or int(v[0]) > best[1]): best = (nm.strip(), int(v[0]), int(v[8]), int(v[3]))
        row = dict(ts=int(t0 * 1000), load1=la[0], load5=la[1], memav_mb=mg('MemAvailable') // 1024, swap_mb=(mg('SwapTotal') - mg('SwapFree')) // 1024, **r)
        if sw0: row.update(pswpin=sw[0] - sw0[0], pswpout=sw[1] - sw0[1])
        sw0 = sw
        if best:
            if net0: row.update(rx_kB=(best[1] - net0[0]) // 1024, tx_kB=(best[2] - net0[1]) // 1024, rx_drop=best[3] - net0[2])
            net0 = (best[1], best[2], best[3])
        for pre, pid in (('P', pidP), ('H', pidH)):
            for k, v in proc(pid, pv).items(): row[f'{pre}_{k}'] = v
        row['P_rqwait_ms'] = row.pop('P_rq', ''); row['H_rqwait_ms'] = row.pop('H_rq', '')
        row['P_pid'], row['H_pid'] = pidP or '', pidH or ''
        if t0 - ult_ips > 300: gamma = ips('gamma-api.polymarket.com'); ult_ips = t0
        if True:
            for k, v in socks(pidH or -1, prevS, gamma).items():
                if k == 'gp': row['gamma_conns_por_pid'] = '"' + v.replace('"', "'") + '"'; continue
                row[{'nsock': 'H_nsock', 'rqs': 'H_recvq_sum', 'rqm': 'H_recvq_max', 'brd': 'H_bytes_rx_delta', 'retr': 'H_retrans', 'cd': 'H_conn_deltas'}[k]] = v
        if n % 5 == 0:
            f = hoy_ficheros()
            for k in ('ms', 'tx'): row[f'L5{k}_dB'] = f[k] - L5.get(k, f[k]) if L5 else ''; 
            L5 = f
        gz.write(','.join('' if row.get(k) is None else (f'"{row[k]}"' if k == 'H_conn_deltas' else str(row[k])) for k in COLS) + '\n')
        n += 1
        if n % 5 == 0: gz.flush()
        time.sleep(max(0.0, 1.0 - (time.time() - t0)))
    gz.close()

if __name__ == '__main__':
    main()
