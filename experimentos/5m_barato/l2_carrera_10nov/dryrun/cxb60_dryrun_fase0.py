#!/usr/bin/env python3
"""cxb60_dryrun_fase0.py -- DRY-RUN FORWARD de B-CXB60 v1 (5m ETH/SOL/XRP). SOLO SIMULA: no firma, no envia, no usa credenciales, no importa py-clob-client/requests. NO esta desplegado (ver PLAN_DESPLIEGUE en L_REAL_Y_DRYRUN_CXB60_11nov.md).
Entrada: lee en SOLO LECTURA los registros ms vivos `maker_ms_<D>_<pid>.csv.gz` del datalog (filas k = mercados, q = top del libro con ex y rx, t = trades con ex y rx; el resto se ignora). NO importa libro_estado_ws ni arranca el WS (duplicaria el escritor del
registro y podria interferir con su cerrojo): es un LECTOR del mismo fichero que ya escribe `observadores`. Un gz que crece se lee de forma incremental con zlib.decompressobj(31) y se reabre desde el principio al reiniciar.
Logica de decision/relleno: importada de cxb60_core.py (maquina incremental equivalente a run_var, probada contra el run_var ORIGINAL en test_cxb60_dryrun.py) y del motor v3 (engine/engine_v3/capt). Decisiones con RX; relleno/cancelacion con EX; l = {35,60,100,150} en paralelo;
CONTROL GEO1 (misma colocacion sin cancelar) y G0; PLACEBO PLC60_<semilla> de igual cobertura (20 semillas). Retraso de procesado SETTLE_MS=2 s (equivale a escribir con 2 s de latencia; NO mide el d_proc real de un ejecutor: ver microbench en test).
Salidas (datalogs, gz, FUERA de git; retencion --retencion-dias, 30 por defecto): OUT/dec_<D>.csv.gz (filas 'seg' = cada colocacion virtual con ms ex/rx, motivo de fin, cantidad y sello del relleno; filas 'nof' = motivos de no-colocacion por mercado/L/variante),
OUT/run_manifest.json, OUT/heartbeat.json, OUT/coverage_<D>.json, OUT/run_<ts>.log. El desenlace OFICIAL lo une cxb60_resolve.py (gmap del cron sa_r1), no este proceso. Idempotencia: un mercado cerrado se escribe en UN bloque gz anexado; al reiniciar se reconcilia con lo escrito
(tokens ya presentes se saltan; cola gz truncada se recorta al ultimo miembro valido) y los mercados abiertos se reprocesan desde el principio del fichero; los que empezaron antes del arranque sin datos completos se marcan `incompleto_arranque`.
Uso: python3 cxb60_dryrun_fase0.py [--out DIR] [--dir DIR] [--once --files f1 f2 ...] [--solo-dia YYYY-MM-DD]   (--once procesa los ficheros dados y termina: replay offline / pruebas)"""
import os, sys, io, gzip, zlib, json, time, glob, hashlib, argparse, datetime as dt, signal, resource, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_core as C

DL = '/root/polymarket-research-datalogs/'; UNIVERSE = {'ETH', 'SOL', 'XRP'}; VERSION = 'cxb60_dryrun_v1'
COLS = ['tipo', 'run_id', 'dia', 'tok', 'mid', 'coin', 'lado', 'fin', 'L', 'var', 'seg', 't_dec_rx', 't_arr', 't_end', 'motivo_fin', 'canc', 't_trig_rx', 't_trig_ex', 'q', 'tf', 'rem_antes', 'detalle', 't_wall_ms']


# ------------------------------------------------------------------------------------------------------------------------ lectura incremental de gz que crece
class GzTail:
    def __init__(self, path): self.path = path; self.fh = open(path, 'rb'); self.d = zlib.decompressobj(31); self.buf = b''; self.eof_member = False; self.n_bytes = 0

    def poll(self, maxbytes=1 << 22):
        """Devuelve la lista de lineas completas disponibles ahora (str). Tolera miembros gz concatenados y un final aun sin volcar."""
        data = self.fh.read(maxbytes)
        if not data: return []
        self.n_bytes += len(data); out = []
        while data:
            if self.d.eof: self.d = zlib.decompressobj(31)
            out.append(self.d.decompress(data)); data = self.d.unused_data if self.d.eof else b''
        txt = self.buf + b''.join(out); i = txt.rfind(b'\n')
        if i < 0: self.buf = txt; return []
        self.buf = txt[i + 1:]; return txt[:i].decode('utf-8', 'replace').split('\n')


def miembros_validos(path):
    """(texto, bytes_validos) de un gz de miembros anexados; recorta la cola corrupta/truncada (escritura interrumpida)."""
    if not os.path.exists(path): return '', 0
    raw = open(path, 'rb').read(); pos = 0; parts = []
    while pos < len(raw):
        d = zlib.decompressobj(31)
        try: parts.append(d.decompress(raw[pos:]))
        except zlib.error: break
        if not d.eof: break
        pos = len(raw) - len(d.unused_data)
    return b''.join(parts).decode('utf-8', 'replace'), pos


def append_gz(path, text):
    blob = gzip.compress(text.encode('utf-8'), 6)
    with open(path, 'ab') as f: f.write(blob); f.flush(); os.fsync(f.fileno())


def atomic_json(path, obj):
    tmp = path + '.tmp'; open(tmp, 'w').write(json.dumps(obj, indent=1, default=str)); os.replace(tmp, path)


def iso_epoch(s):
    return int(dt.datetime.fromisoformat(s.strip().replace(' ', 'T')).timestamp())


def fnum(x):
    try: return float(x) if x not in ('', 'None', 'nan') else float('nan')
    except ValueError: return float('nan')


# ------------------------------------------------------------------------------------------------------------------------ nucleo del proceso
class Run:
    def __init__(self, a):
        self.a = a; self.out = a.out; os.makedirs(self.out, exist_ok=True); self.run_id = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ') + f'_{os.getpid()}'
        self.logf = open(self.out + f'run_{self.run_id}.log', 'a'); self.meta = {}; self.by5 = {}; self.by15 = {}; self.bufs = {}; self.markets = {}; self.W = 0; self.W_first = None; self.cnt = dict(lineas=0, q=0, t=0, k=0, q_dup=0, parse_err=0, sin_buf=0)
        self.cov = {}; self.done = set(); self.specs = C.default_specs((35, 60, 100, 150), 20); self.cpu = []; self.t_start = time.time(); self.stop = False; self.last_hb = 0; self.skipped = {}
        self.closed_n = 0; self.pending_close = []; self.hash_ref = {f: hashlib.sha256(open(HERE + f, 'rb').read()).hexdigest()[:16] for f in ('cxb60_core.py', 'cxb60_dryrun_fase0.py')}
        for nm, pth in (('engine.py', C.P2 + 'escalera_B/engine.py'), ('engine_v3.py', C.HERE + 'engine_v3.py'), ('capt.py', C.P2 + 'capturabilidad_A_R1ws/capt.py'), ('engine_clock.py', C.HERE + 'engine_clock.py')):
            try: self.hash_ref[nm] = hashlib.sha256(open(pth, 'rb').read()).hexdigest()[:16]
            except OSError: self.hash_ref[nm] = 'no_encontrado'
        self.tails = {}; self.retencion()
        self.fill = C.make_live_fill(self.bufs_of, self.meta_of, a.c_print)

    def log(self, *x):
        s = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') + ' ' + ' '.join(str(i) for i in x); print(s, flush=True); self.logf.write(s + '\n'); self.logf.flush()

    def retencion(self):
        lim = time.time() - self.a.retencion_dias * 86400
        for f in glob.glob(self.out + 'dec_*.csv.gz') + glob.glob(self.out + 'run_*.log') + glob.glob(self.out + 'coverage_*.json'):
            try:
                if os.path.getmtime(f) < lim: os.remove(f); self.log('retencion: borrado', f)
            except OSError: pass

    # -------- reconciliacion con lo ya escrito (reinicio idempotente)
    def reconcilia(self, dia):
        p = self.out + f'dec_{dia}.csv.gz'; txt, ok = miembros_validos(p)
        if os.path.exists(p) and ok < os.path.getsize(p):
            self.log(f'RECONCILIA {p}: cola corrupta/truncada ({os.path.getsize(p) - ok} bytes) -> se recorta a {ok}'); os.truncate(p, ok)
        n = 0
        for ln in txt.split('\n')[1:]:
            if not ln: continue
            f = ln.split(',', 4)
            if len(f) > 3: self.done.add(f[3]); n += 1
        self.log(f'RECONCILIA {dia}: filas ya escritas {n}, mercados cerrados {len(self.done)}')

    def bufs_of(self, tok):
        c = self.by5.get((self.meta[tok]['mid'], 'NO' if self.meta[tok]['lado'] == 'YES' else 'YES')); return self.bufs[tok], self.bufs.get(c) or C.TokBuf()

    def meta_of(self, tok):
        m = self.meta[tok]; c = self.by5.get((m['mid'], 'NO' if m['lado'] == 'YES' else 'YES'))
        mc = self.meta[c] if c else dict(tok='sin_comp', mid=m['mid'], lado='NO' if m['lado'] == 'YES' else 'YES', coin=m['coin'], fin=m['fin']); return [m, mc]

    # -------- ingesta
    def feed(self, lines):
        for ln in lines:
            if not ln: continue
            self.cnt['lineas'] += 1; c0 = ln[0]
            if c0 == 'q':
                f = ln.split(',')
                if len(f) < 8: self.cnt['parse_err'] += 1; continue
                try: rx = int(f[7]); ex = int(f[1])
                except ValueError: self.cnt['parse_err'] += 1; continue
                if rx > self.W: self.W = rx
                if self.W_first is None: self.W_first = rx
                b = self.bufs.get(f[2])
                if b is None: continue
                row = (ex, rx, fnum(f[3]), fnum(f[4]), fnum(f[5]), fnum(f[6]))
                if len(b.qrx) and b.qrx[-1] == rx and b.qex[-1] == ex and (b.qbid[-1], b.qask[-1], b.qszb[-1], b.qsza[-1]) == row[2:]: self.cnt['q_dup'] += 1; continue
                b.add_q(*row); self.cnt['q'] += 1
            elif c0 == 't':
                f = ln.split(',')
                if len(f) < 7: self.cnt['parse_err'] += 1; continue
                try: rx = int(f[6]); ex = int(f[1])
                except ValueError: self.cnt['parse_err'] += 1; continue
                if rx > self.W: self.W = rx
                b = self.bufs.get(f[2])
                if b is None: continue
                b.add_t(ex, rx, fnum(f[3]), 1.0 if f[4] == 'BUY' else 0.0, fnum(f[5])); self.cnt['t'] += 1
            elif c0 == 'k':
                f = ln.split(',')
                if len(f) < 8 or f[2] in self.meta: continue
                try: fin = iso_epoch(f[6])
                except ValueError: self.cnt['parse_err'] += 1; continue
                coin, marco, lado = f[3], f[4], f[7].strip()
                if coin not in UNIVERSE or marco not in ('5min', '15min') or lado not in ('YES', 'NO'): continue
                self.cnt['k'] += 1; m = dict(tok=f[2], coin=coin, marco=marco, mid=f[5], fin=fin, lado=lado, t_k=int(f[1])); self.meta[f[2]] = m; self.bufs[f[2]] = C.TokBuf()
                (self.by5.__setitem__((m['mid'], lado), f[2]) if marco == '5min' else self.by15.__setitem__((coin, fin, lado), f[2]))
                if marco == '5min':
                    dia = dt.datetime.fromtimestamp(fin - 150, dt.timezone.utc).strftime('%Y-%m-%d'); self.cov.setdefault(dia, dict(esperados=0, procesados=0, saltados={}, duplicados_q=0, filas_invalidas=0))['esperados'] += 1

    # -------- ciclo de mercados
    def ciclo(self, final=False):
        tk = (10 ** 18) if final else self.W - C.SETTLE_MS; nuevos = 0
        for tok, m in list(self.meta.items()):
            if m['marco'] != '5min' or tok in self.markets or tok in self.done or tok in self.skipped: continue
            fin = m['fin']; dia = dt.datetime.fromtimestamp(fin - 150, dt.timezone.utc).strftime('%Y-%m-%d'); cv = self.cov[dia]
            if self.W < (fin - 300) * 1000 - 40000 and not final: continue                                    # aun no toca
            comp = self.by5.get((m['mid'], 'NO' if m['lado'] == 'YES' else 'YES')); f15 = int(math.ceil(fin / 900.0) * 900); t15 = self.by15.get((m['coin'], f15, m['lado']))
            why = None
            if comp is None: why = 'sin_comp'
            elif self.W_first is None or self.W_first > (fin - 300) * 1000 - 32000: why = 'incompleto_arranque'      # vol30/b300 necesitan >=31 s de datos antes de la rejilla
            elif t15 is None: why = 'sin_token_15m'
            elif tok not in self.bufs or comp not in self.bufs or t15 not in self.bufs: why = 'buffer_ausente'
            if why:
                self.skipped[tok] = why; cv['saltados'][why] = cv['saltados'].get(why, 0) + 1; continue
            self.markets[tok] = C.Market(tok, fin, m['coin'], m['lado'], m['mid'], comp, self.bufs[tok], self.bufs[comp], self.bufs[t15], self.specs); nuevos += 1
        for tok, mk in list(self.markets.items()):
            t0 = time.perf_counter(); out = mk.advance(tk if not final else 10 ** 18, self.fill); self.cpu.append((time.perf_counter() - t0) * 1e6)
            if out: self.pending_close.append((tok, out))
            if mk.closed: self.cierra(tok, mk, out)
        self.cpu = self.cpu[-5000:]
        self.gc()

    def cierra(self, tok, mk, last):
        m = self.meta[tok]; dia = dt.datetime.fromtimestamp(m['fin'] - 150, dt.timezone.utc).strftime('%Y-%m-%d'); recs = [r for t, o in self.pending_close if t == tok for r in o]
        self.pending_close = [x for x in self.pending_close if x[0] != tok]; rows = []; wall = int(time.time() * 1000)
        for r in recs:
            rows.append(['seg', self.run_id, dia, tok, m['mid'], m['coin'], m['lado'], m['fin'], r['L'], r['var'], r['seg'], r['t_dec_rx'], r['t_arr'], r['t_end'], r['motivo_fin'], r['canc'], r['t_trig_rx'] if r['t_trig_rx'] is not None else '', r['t_trig_ex'] if r['t_trig_ex'] is not None else '',
                         round(r['q'], 6), r['tf'], round(r['rem_antes'], 6), r['why'], wall])
        for ma in mk.M:
            rows.append(['nof', self.run_id, dia, tok, m['mid'], m['coin'], m['lado'], m['fin'], ma.L, ma.spec.name, ma.seg, '', '', '', '', '', '', '', '', '', '', json.dumps(ma.finalize_reasons(), separators=(',', ':')), wall])
        p = self.out + f'dec_{dia}.csv.gz'; head = '' if os.path.exists(p) and os.path.getsize(p) > 0 else ','.join(COLS) + '\n'
        append_gz(p, head + '\n'.join(','.join(str(x) if ',' not in str(x) else '"' + str(x).replace('"', '""') + '"' for x in r) for r in rows) + '\n')
        self.done.add(tok); del self.markets[tok]; self.closed_n += 1; self.cov[dia]['procesados'] += 1

    def gc(self):
        W = self.W; vivos = {t for mk in self.markets.values() for t in (mk.tok, mk.comp_tok)}
        for tok in list(self.bufs):
            m = self.meta[tok]
            if tok in vivos: continue
            if (W > m['fin'] * 1000 + (120000 if m['marco'] == '5min' else 400000) and (tok in self.done or tok in self.skipped or m['marco'] == '15min')) or W > (m['fin'] + 3600) * 1000:
                b = self.bufs.pop(tok); self.cnt['q_fuera_de_orden'] = self.cnt.get('q_fuera_de_orden', 0) + b.n_q_fuera_de_orden; self.cnt['t_fuera_de_orden'] = self.cnt.get('t_fuera_de_orden', 0) + b.n_t_fuera_de_orden

    def heartbeat(self, status='RUNNING'):
        cpu = np.asarray(self.cpu) if self.cpu else np.zeros(1); rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        hb = dict(run_id=self.run_id, status=status, wall=time.time(), W_ms=self.W, W_utc=dt.datetime.fromtimestamp(self.W / 1000, dt.timezone.utc).isoformat() if self.W else None, lag_s=round(time.time() - self.W / 1000, 1) if self.W else None, contadores=self.cnt,
                  mercados_activos=len(self.markets), cerrados=self.closed_n, saltados={k: sum(1 for v in self.skipped.values() if v == k) for k in set(self.skipped.values())}, rss_mb=round(rss, 0), cpu_advance_us=dict(p50=float(np.percentile(cpu, 50)), p90=float(np.percentile(cpu, 90)), p99=float(np.percentile(cpu, 99)), n=len(self.cpu)))
        atomic_json(self.out + 'heartbeat.json', hb); self.last_hb = time.time()

    def manifiesto(self, status, ficheros):
        man = dict(job=VERSION, run_id=self.run_id, status=status, modo='DRY_RUN (solo simula; 0 ordenes)', codigo=self.hash_ref, parametros=dict(niveles=C.LEVELS, tmin=C.TMIN, lat_post=C.LAT_POST, grid=C.GRID, size=C.SIZE, settle_ms=C.SETTLE_MS, c_print=self.a.c_print, l_ms=[35, 60, 100, 150], placebo_semillas=20, rebate=C.REB),
                   entradas=[dict(fichero=f, bytes=os.path.getsize(f) if os.path.exists(f) else None) for f in ficheros], inicio=self.t_start, fin=time.time() if status != 'RUNNING' else None, cobertura=self.cov, saltados=self.skipped, cmd=' '.join(sys.argv))
        atomic_json(self.out + 'run_manifest.json', man)
        for dia, cv in self.cov.items(): atomic_json(self.out + f'coverage_{dia}.json', dict(dia=dia, **cv))

    # -------- bucle
    def ficheros_vivos(self):
        if self.a.files: return self.a.files
        hoy = dt.datetime.now(dt.timezone.utc); dias = [(hoy - dt.timedelta(days=i)).strftime('%Y-%m-%d') for i in (1, 0)]; fs = []
        for d in dias:
            for f in sorted(glob.glob(self.a.dir + f'maker_ms_{d}_*.csv.gz')):
                if d == dias[0] and time.time() - os.path.getmtime(f) > 1800: continue
                fs.append(f)
        return fs

    def run(self):
        signal.signal(signal.SIGTERM, lambda *a: setattr(self, 'stop', True)); signal.signal(signal.SIGINT, lambda *a: setattr(self, 'stop', True))
        for d in {(dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=i)).strftime('%Y-%m-%d') for i in (0, 1)} | set(self.a.solo_dia or []): self.reconcilia(d)
        self.manifiesto('RUNNING', self.ficheros_vivos()); self.log('INICIO', VERSION, self.run_id, 'ficheros', self.ficheros_vivos()); estado = 'COMPLETE'
        try:
            while not self.stop:
                nuevo = False
                for f in self.ficheros_vivos():
                    if f not in self.tails:
                        try: self.tails[f] = GzTail(f); self.log('abre', f)
                        except OSError as e: self.log('no abre', f, e); continue
                    try: ls = self.tails[f].poll()
                    except zlib.error as e: self.log('gz ilegible', f, e); del self.tails[f]; continue
                    if ls: nuevo = True; self.feed(ls)
                if self.a.once:
                    if not nuevo: break
                    self.ciclo(); continue
                self.ciclo()
                if time.time() - self.last_hb > 30: self.heartbeat(); self.manifiesto('RUNNING', list(self.tails))
                if not nuevo: time.sleep(0.5)
        except Exception as e:
            estado = 'FAILED'; self.log('EXCEPCION', repr(e)); raise
        finally:
            if self.a.once: self.ciclo(final=True)
            elif self.stop: estado = 'PARTIAL'
            self.heartbeat('STOPPED_' + estado); self.manifiesto(estado, list(self.tails)); self.log('FIN', estado, 'cerrados', self.closed_n, 'activos', len(self.markets), self.cnt)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out', default=DL + 'cxb60_dryrun/'); ap.add_argument('--dir', default=DL); ap.add_argument('--files', nargs='*'); ap.add_argument('--once', action='store_true'); ap.add_argument('--solo-dia', nargs='*')
    ap.add_argument('--retencion-dias', type=int, default=30); ap.add_argument('--c-print', type=int, default=C.C_PRINT, help='sello de la cinta WS = ex - c_print - 1 (19 por defecto; 59 = escenario pesimista G7 del prereg; usar --out distinto)'); a = ap.parse_args(); a.out = a.out.rstrip('/') + '/'; a.dir = a.dir.rstrip('/') + '/'
    if a.once and not a.files: ap.error('--once requiere --files');
    Run(a).run()


if __name__ == '__main__': main()
