#!/usr/bin/env python3
"""cxb60_dryrun_fase0.py -- DRY-RUN FORWARD de B-CXB60 v1 (5m ETH/SOL/XRP + BTC como subvariante; MULTIVARIANTE v3: CXB35/45/60/100/150 + CXBEMP). SOLO SIMULA: no firma, no envia, no usa credenciales, no importa py-clob-client/requests. NO esta desplegado (ver PLAN_DESPLIEGUE en CXB60_CONDICIONES_L_CALMA_12nov.md §C6).
Entrada: lee en SOLO LECTURA los registros ms vivos `maker_ms_<D>_<pid>.csv.gz` del datalog (filas k = mercados, q = top del libro con ex y rx, t = trades con ex y rx; el resto se ignora; los ficheros cuyo primer dato es x/b = Binance se descartan). NO importa
libro_estado_ws ni arranca el WS: es un LECTOR del mismo fichero que ya escribe `observadores`. Un gz que crece se lee de forma incremental con zlib.decompressobj(31) y se reabre desde el principio al reiniciar.
Logica de decision/relleno: importada de cxb60_core.py (maquina incremental equivalente a run_var, probada contra el run_var ORIGINAL en test_cxb60_dryrun.py) y del motor v3 CONGELADO en frozen/ (engine/engine_v3/capt/relojes/engine_clock: copia de dev).
INTEGRIDAD DE CODIGO (H1): al arrancar (salvo --once --sin-verificar-hash, solo desarrollo) compara sha256 de frozen/*, cxb60_core.py, cxb60_io.py y de ESTE fichero con HASHES_CONGELADOS.json y ABORTA con exit 3 si difieren o falta la referencia.
Decisiones con RX; relleno/cancelacion con EX; l = {35,45,60,100,150} + CXBEMP (l empirico: 3 ms + pool de 1.453 anclas) en paralelo; CONTROL GEO1 (misma colocacion sin cancelar) y G0; PLACEBO PLC60_<semilla> de igual cobertura (100 semillas por defecto, --placebo).
ESCENARIOS EN PARALELO (C4): el escenario primario usa sello de cinta WS = ex - c_print - 1 (c_print=19) y escribe en OUT/; el escenario pesimista (c_print=59, G7 del prereg) se calcula EN EL MISMO PROCESO sobre los mismos buffers (sin placebo) y escribe en OUT/c59/.
RELOJ DE FLUJO W (H3): W = MINIMO del rx maximo de los ficheros ACTIVOS (mtime < 120 s); sin ficheros activos, el maximo. Retraso de procesado SETTLE_MS=2 s (NO mide el d_proc real de un ejecutor).
Salidas (datalogs, gz, FUERA de git; retencion --retencion-dias, 30): OUT/dec_<D>.csv.gz con filas 'seg' (cada colocacion virtual), 'nof' (motivos de no-colocacion por mercado/L/variante; placebo solo semilla 1) y 'mkt' (una por mercado cerrado:
calidad del feed: huecos de >=5 s sin ningun mensaje de la moneda en la ventana [fin-332 s, fin], edad de W, n de filas), OUT/run_manifest.json, OUT/heartbeat.json, OUT/coverage_<D>.json (cobertura = mercados procesados / esperados TEORICOS
(288 mercados 5m x 2 tokens por moneda y dia), por moneda; dia valido solo si todas las monedas >= 0,95: H4), OUT/run_<ts>.log. El desenlace OFICIAL lo une cxb60_resolve.py. Idempotencia: un mercado cerrado se escribe en UN bloque gz; al reiniciar
se reconcilia con lo escrito y los mercados abiertos se reprocesan desde el principio del fichero; los que empezaron antes del arranque sin datos completos se marcan `incompleto_arranque`.
Uso: python3 cxb60_dryrun_fase0.py [--out DIR] [--dir DIR] [--once --files f1 f2 ...] [--solo-dia YYYY-MM-DD] [--placebo N] [--c-print-par 59|0] [--max-rss-mb N]"""
import os, sys, io, gzip, zlib, json, time, glob, bisect, argparse, datetime as dt, signal, resource, math, re
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_io as IO
import cxb60_core as C
from cxb60_io import COLS, miembros_validos, append_gz, atomic_json          # reexportados (tests y resolvedor antiguos)

DL = '/root/polymarket-research-datalogs/'; UNIVERSE = {'ETH', 'SOL', 'XRP', 'BTC'}; UNIVERSE_PRIM = {'ETH', 'SOL', 'XRP'}; VERSION = 'cxb60_dryrun_v3'          # BTC = subvariante (hipotesis aparte): procesada y reportada, pero NO cuenta en dia_valido ni en el agregado primario
GAP_S = 5                  # un hueco de >= GAP_S segundos consecutivos sin NINGUN mensaje de la moneda dentro de la ventana del mercado marca `hueco_feed`
VENT_PRE_S = 332           # 300 s de mercado + 32 s de calentamiento (vol30/b300)
SLOTS_DIA = 288; COBERTURA_MIN = 0.95
L_LIST = (35, 45, 60, 100, 150)          # + CXBEMP (l empirico, ver cxb60_core.l_emp); CXB100/150 = control de dosis-respuesta, no candidatos


def iso_epoch(s):
    return int(dt.datetime.fromisoformat(s.strip().replace(' ', 'T')).timestamp())


def fnum(x):
    try: return float(x) if x not in ('', 'None', 'nan') else float('nan')
    except ValueError: return float('nan')


def dia_de(fin): return dt.datetime.fromtimestamp(fin - 150, dt.timezone.utc).strftime('%Y-%m-%d')


def rss_mb():
    try: return int(open('/proc/self/statm').read().split()[1]) * os.sysconf('SC_PAGE_SIZE') / 1048576.0
    except (OSError, ValueError, IndexError): return -1.0


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


# ------------------------------------------------------------------------------------------------------------------------ escenario (sello de cinta) y nucleo
class Scen:
    """Un escenario de simulacion: mismo flujo/buffers/features que los demas, distinto sello de cinta WS (c_print) y directorio de salida."""
    def __init__(self, name, out, c_print, specs):
        self.name, self.out, self.c_print, self.specs = name, out, c_print, specs; os.makedirs(out, exist_ok=True)
        self.markets = {}; self.done = set(); self.pending_close = []; self.closed_n = 0; self.fill = None; self.proc = {}          # proc[dia][coin] = set(tok) ya cerrados (reconciliado + nuevos)


class Run:
    def __init__(self, a):
        self.a = a; self.out = a.out; os.makedirs(self.out, exist_ok=True); self.run_id = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ') + f'_{os.getpid()}'
        self.logf = open(self.out + f'run_{self.run_id}.log', 'a'); self.meta = {}; self.by5 = {}; self.by15 = {}; self.bufs = {}; self.W = 0; self.W_first = None; self.Wf = {}
        self.cnt = dict(lineas=0, q=0, t=0, k=0, q_dup=0, parse_err=0, sin_buf=0, ficheros_binance_ignorados=0)
        self.sec = {c: set() for c in UNIVERSE}; self.coin_of = {}; self.esperados_vistos = {}; self.skipped = {}; self.sk_cov = {}; self.cpu = []; self.t_start = time.time(); self.stop = False; self.last_hb = 0; self.last_prune = 0; self.last_rss = 0
        self.fkind = {}; self.tails = {}; self.hash_check = None
        self.scens = [Scen(f'c{a.c_print}', self.out, a.c_print, C.default_specs(L_LIST, a.placebo))]
        if a.c_print_par and a.c_print_par != a.c_print: self.scens.append(Scen(f'c{a.c_print_par}', self.out + f'c{a.c_print_par}/', a.c_print_par, C.default_specs(L_LIST, 0)))
        for s in self.scens: s.fill = C.make_live_fill(self.bufs_of, self.meta_of, s.c_print)
        self.hash_ref = IO.hashes_actuales(); self.retencion()

    def log(self, *x):
        s = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ') + ' ' + ' '.join(str(i) for i in x); print(s, flush=True); self.logf.write(s + '\n'); self.logf.flush()

    def retencion(self):
        """Borra por FECHA DEL NOMBRE (no por mtime: un dec_ re-escrito en un reinicio no renueva la edad). res_*/run_manifest nunca se borran."""
        lim = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=self.a.retencion_dias)).strftime('%Y-%m-%d')
        for s in self.scens:
            for f in glob.glob(s.out + 'dec_*.csv.gz') + glob.glob(s.out + 'coverage_*.json'):
                m = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(f))
                if m and m.group(1) < lim:
                    try: os.remove(f); self.log('retencion: borrado', f)
                    except OSError: pass
        for f in glob.glob(self.out + 'run_*.log'):
            try:
                if os.path.getmtime(f) < time.time() - self.a.retencion_dias * 86400: os.remove(f)
            except OSError: pass

    # -------- reconciliacion con lo ya escrito (reinicio idempotente)
    def reconcilia(self, dia):
        for s in self.scens:
            p = s.out + f'dec_{dia}.csv.gz'; txt, ok = miembros_validos(p)
            if os.path.exists(p) and ok < os.path.getsize(p):
                self.log(f'RECONCILIA {p}: cola corrupta/truncada ({os.path.getsize(p) - ok} bytes) -> se recorta a {ok}'); os.truncate(p, ok)
            n = 0
            for ln in txt.split('\n')[1:]:
                if not ln: continue
                f = ln.split(',', 6)
                if len(f) > 5:
                    s.done.add(f[3]); n += 1
                    if f[0] == 'mkt': s.proc.setdefault(f[2], {}).setdefault(f[5], set()).add(f[3])
            self.log(f'RECONCILIA [{s.name}] {dia}: filas ya escritas {n}, mercados cerrados {len(s.done)}')

    def bufs_of(self, tok):
        c = self.by5.get((self.meta[tok]['mid'], 'NO' if self.meta[tok]['lado'] == 'YES' else 'YES')); return self.bufs[tok], self.bufs.get(c) or C.TokBuf()

    def meta_of(self, tok):
        m = self.meta[tok]; c = self.by5.get((m['mid'], 'NO' if m['lado'] == 'YES' else 'YES'))
        mc = self.meta[c] if c else dict(tok='sin_comp', mid=m['mid'], lado='NO' if m['lado'] == 'YES' else 'YES', coin=m['coin'], fin=m['fin']); return [m, mc]

    # -------- ingesta
    def feed(self, lines, fid):
        sec = self.sec; coin_of = self.coin_of
        for ln in lines:
            if not ln: continue
            c0 = ln[0]
            if c0 == 'q':
                self.cnt['lineas'] += 1; f = ln.split(',')
                if len(f) < 8: self.cnt['parse_err'] += 1; continue
                try: rx = int(f[7]); ex = int(f[1])
                except ValueError: self.cnt['parse_err'] += 1; continue
                if self.Wf.get(fid, 0) < rx: self.Wf[fid] = rx
                if self.W_first is None: self.W_first = rx
                b = self.bufs.get(f[2])
                if b is None: continue
                sec[coin_of[f[2]]].add(rx // 1000)
                row = (ex, rx, fnum(f[3]), fnum(f[4]), fnum(f[5]), fnum(f[6]))
                if len(b.qrx) and b.qrx[-1] == rx and b.qex[-1] == ex and (b.qbid[-1], b.qask[-1], b.qszb[-1], b.qsza[-1]) == row[2:]: self.cnt['q_dup'] += 1; continue
                b.add_q(*row); self.cnt['q'] += 1
            elif c0 == 't':
                if ln.startswith('tipo,'): continue                                                                   # cabecera del fichero
                self.cnt['lineas'] += 1; f = ln.split(',')
                if len(f) < 7: self.cnt['parse_err'] += 1; continue
                try: rx = int(f[6]); ex = int(f[1])
                except ValueError: self.cnt['parse_err'] += 1; continue
                if self.Wf.get(fid, 0) < rx: self.Wf[fid] = rx
                b = self.bufs.get(f[2])
                if b is None: continue
                sec[coin_of[f[2]]].add(rx // 1000)
                b.add_t(ex, rx, fnum(f[3]), 1.0 if f[4] == 'BUY' else 0.0, fnum(f[5])); self.cnt['t'] += 1
            elif c0 == 'k':
                self.cnt['lineas'] += 1; f = ln.split(',')
                if len(f) < 8 or f[2] in self.meta: continue
                try: fin = iso_epoch(f[6])
                except ValueError: self.cnt['parse_err'] += 1; continue
                coin, marco, lado = f[3], f[4], f[7].strip()
                if coin not in UNIVERSE or marco not in ('5min', '15min') or lado not in ('YES', 'NO'): continue
                self.cnt['k'] += 1; m = dict(tok=f[2], coin=coin, marco=marco, mid=f[5], fin=fin, lado=lado, t_k=int(f[1])); self.meta[f[2]] = m; self.bufs[f[2]] = C.TokBuf(); coin_of[f[2]] = coin
                (self.by5.__setitem__((m['mid'], lado), f[2]) if marco == '5min' else self.by15.__setitem__((coin, fin, lado), f[2]))
                if marco == '5min': self.esperados_vistos.setdefault(dia_de(fin), {}).setdefault(coin, set()).add(f[2])
            else: self.cnt['lineas'] += 1

    def actualiza_W(self):
        """H3: W = min del rx maximo de los ficheros ACTIVOS (mtime < 120 s: el escritor aun anexa); sin activos, el maximo. Monotono."""
        now = time.time(); act = []
        for f, w in self.Wf.items():
            try:
                if now - os.path.getmtime(f) < 120: act.append(w)
            except OSError: pass
        cand = min(act) if act else (max(self.Wf.values()) if self.Wf else 0)
        if cand > self.W: self.W = cand

    # -------- calidad del feed por mercado (H3)
    def calidad_feed(self, m):
        fin = m['fin']; s0, s1 = fin - VENT_PRE_S, fin; S = self.sec[m['coin']]; run = best = 0; vac = 0
        for s in range(s0, s1 + 1):
            if s in S: run = 0
            else: run += 1; vac += 1; best = max(best, run)
        b = self.bufs.get(m['tok']); lo, hi = s0 * 1000, s1 * 1000
        nq = (bisect.bisect_right(b.qrx, hi) - bisect.bisect_left(b.qrx, lo)) if b is not None else -1; nt = (bisect.bisect_right(b.trx, hi) - bisect.bisect_left(b.trx, lo)) if b is not None else -1
        return dict(hueco_feed=best >= GAP_S, vac_max_s=best, vac_n_s=vac, nq_ventana=nq, nt_ventana=nt, W_edad_ms=int(self.W - fin * 1000), n_q_fuera_orden=(b.n_q_fuera_de_orden if b is not None else -1))

    # -------- ciclo de mercados
    def ciclo(self, final=False):
        tk = (10 ** 18) if final else self.W - C.SETTLE_MS
        for tok, m in list(self.meta.items()):
            if m['marco'] != '5min' or tok in self.skipped: continue
            falta = [s for s in self.scens if tok not in s.markets and tok not in s.done]
            if not falta: continue
            fin = m['fin']; dia = dia_de(fin)
            if self.W < (fin - 300) * 1000 - 40000 and not final: continue                                    # aun no toca
            comp = self.by5.get((m['mid'], 'NO' if m['lado'] == 'YES' else 'YES')); f15 = int(math.ceil(fin / 900.0) * 900); t15 = self.by15.get((m['coin'], f15, m['lado']))
            why = None
            if comp is None: why = 'sin_comp'
            elif self.W_first is None or self.W_first > (fin - 300) * 1000 - 32000: why = 'incompleto_arranque'      # vol30/b300 necesitan >=31 s de datos antes de la rejilla
            elif t15 is None: why = 'sin_token_15m'
            elif tok not in self.bufs or comp not in self.bufs or t15 not in self.bufs: why = 'buffer_ausente'
            if why:
                self.skipped[tok] = why; d = self.sk_cov.setdefault(dia, {}).setdefault(m['coin'], {}); d[why] = d.get(why, 0) + 1; continue
            F = next((s.markets[tok].F for s in self.scens if tok in s.markets), None)                         # features compartidas entre escenarios (no dependen de c_print)
            for s in falta:
                s.markets[tok] = C.Market(tok, fin, m['coin'], m['lado'], m['mid'], comp, self.bufs[tok], self.bufs[comp], self.bufs[t15], s.specs, F=F); F = s.markets[tok].F
        for s in self.scens:
            for tok, mk in list(s.markets.items()):
                t0 = time.perf_counter(); out = mk.advance(tk if not final else 10 ** 18, s.fill); self.cpu.append((time.perf_counter() - t0) * 1e6)
                if out: s.pending_close.append((tok, out))
                if mk.closed: self.cierra(s, tok, mk)
        self.cpu = self.cpu[-5000:]
        self.gc()

    def cierra(self, s, tok, mk):
        m = self.meta[tok]; dia = dia_de(m['fin']); recs = [r for t, o in s.pending_close if t == tok for r in o]
        s.pending_close = [x for x in s.pending_close if x[0] != tok]; rows = []; wall = int(time.time() * 1000)
        for r in recs:
            rows.append(['seg', self.run_id, dia, tok, m['mid'], m['coin'], m['lado'], m['fin'], r['L'], r['var'], r['seg'], r['t_dec_rx'], r['t_arr'], r['t_end'], r['motivo_fin'], r['canc'], r['t_trig_rx'] if r['t_trig_rx'] is not None else '', r['t_trig_ex'] if r['t_trig_ex'] is not None else '',
                         round(r['q'], 6), r['tf'], round(r['rem_antes'], 6), r['why'], wall])
        for ma in mk.M:
            if ma.spec.kind == 'PLC' and ma.spec.seed != 1: continue                                          # los motivos de no-colocacion del placebo son identicos a los de CXB60: una semilla basta
            rows.append(['nof', self.run_id, dia, tok, m['mid'], m['coin'], m['lado'], m['fin'], ma.L, ma.spec.name, ma.seg, '', '', '', '', '', '', '', '', '', '', json.dumps(ma.finalize_reasons(), separators=(',', ':')), wall])
        rows.append(['mkt', self.run_id, dia, tok, m['mid'], m['coin'], m['lado'], m['fin'], '', '', '', '', '', '', '', '', '', '', '', '', '', json.dumps(self.calidad_feed(m), separators=(',', ':')), wall])
        p = s.out + f'dec_{dia}.csv.gz'; head = None if os.path.exists(p) and os.path.getsize(p) > 0 else COLS
        append_gz(p, IO.csv_text(rows, head))
        s.done.add(tok); del s.markets[tok]; s.closed_n += 1; s.proc.setdefault(dia, {}).setdefault(m['coin'], set()).add(tok)

    def gc(self):
        W = self.W; vivos = {t for s in self.scens for mk in s.markets.values() for t in (mk.tok, mk.comp_tok)}
        for tok in list(self.bufs):
            m = self.meta[tok]
            if tok in vivos: continue
            todos_done = all(tok in s.done for s in self.scens)
            if (W > m['fin'] * 1000 + (120000 if m['marco'] == '5min' else 400000) and (todos_done or tok in self.skipped or m['marco'] == '15min')) or W > (m['fin'] + 3600) * 1000:
                b = self.bufs.pop(tok); self.cnt['q_fuera_de_orden'] = self.cnt.get('q_fuera_de_orden', 0) + b.n_q_fuera_de_orden; self.cnt['t_fuera_de_orden'] = self.cnt.get('t_fuera_de_orden', 0) + b.n_t_fuera_de_orden
        if time.time() - self.last_prune > 300 and W:
            self.last_prune = time.time(); lim = W // 1000 - 7200
            for c in self.sec: self.sec[c] = {x for x in self.sec[c] if x >= lim}
            cut = W // 1000 - 2 * 86400                                                                          # demonio de semanas: se olvidan los mercados con >2 dias (los datos ya estan en dec_<D>.csv.gz)
            for t in [t for t, m in self.meta.items() if m['fin'] < cut and not any(t in sc.markets for sc in self.scens)]:
                m = self.meta.pop(t); self.coin_of.pop(t, None); self.skipped.pop(t, None); self.bufs.pop(t, None)
                (self.by5.pop((m['mid'], m['lado']), None) if m['marco'] == '5min' else self.by15.pop((m['coin'], m['fin'], m['lado']), None))
                for sc in self.scens: sc.done.discard(t)

    # -------- cobertura (H4)
    def cobertura(self, dia):
        s = self.scens[0]; d0 = int(dt.datetime.strptime(dia, '%Y-%m-%d').replace(tzinfo=dt.timezone.utc).timestamp()); fin_max = self.W // 1000 - C.SETTLE_MS // 1000
        slots = int(min(SLOTS_DIA, max(0, (fin_max - d0) // 300)))                                       # mercados 5m del dia con fin = d0+300k (k=1..288) ya cerrados segun W
        pm = {}; tot_p = tot_e = 0; ok = True
        for coin in sorted(UNIVERSE):
            p = len(s.proc.get(dia, {}).get(coin, ())); e = slots * 2; cob = (p / e) if e else None; sk = self.sk_cov.get(dia, {}).get(coin, {})
            pm[coin] = dict(procesados=p, esperados_teoricos=e, cobertura=round(cob, 4) if cob is not None else None, ok_095=bool(cob is not None and cob >= COBERTURA_MIN), saltados=sk, esperados_vistos_k=len(self.esperados_vistos.get(dia, {}).get(coin, ())))
            if coin in UNIVERSE_PRIM: tot_p += p; tot_e += e; ok = ok and pm[coin]['ok_095']
        dia_completo = (d0 + 86400) <= fin_max
        return dict(dia=dia, procesados=tot_p, esperados_teoricos=tot_e, esperados_vistos=sum(len(v) for v in self.esperados_vistos.get(dia, {}).values()), cobertura=round(tot_p / tot_e, 4) if tot_e else None, dia_valido=bool(ok and dia_completo), dia_valido_btc=bool(pm['BTC']['ok_095'] and dia_completo), dia_valido_4monedas=bool(ok and pm['BTC']['ok_095'] and dia_completo), dia_completo=bool(dia_completo),
                    por_moneda=pm, regla='cobertura = mercados(token) procesados / esperados teoricos (288 mercados 5m x 2 tokens por moneda y dia, hasta W); valido = dia completo y ETH,SOL,XRP >= 0,95 (BTC aparte: dia_valido_btc)', saltados={k: sum(1 for v in self.skipped.values() if v == k) for k in set(self.skipped.values())})

    def heartbeat(self, status='RUNNING'):
        cpu = np.asarray(self.cpu) if self.cpu else np.zeros(1); rss = rss_mb()
        hb = dict(run_id=self.run_id, status=status, wall=time.time(), W_ms=self.W, W_utc=dt.datetime.fromtimestamp(self.W / 1000, dt.timezone.utc).isoformat() if self.W else None, lag_s=round(time.time() - self.W / 1000, 1) if self.W else None, contadores=self.cnt,
                  mercados_activos={s.name: len(s.markets) for s in self.scens}, cerrados={s.name: s.closed_n for s in self.scens}, saltados={k: sum(1 for v in self.skipped.values() if v == k) for k in set(self.skipped.values())}, rss_mb=round(rss, 0), rss_pico_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 0),
                  hash_check=self.hash_check, cpu_advance_us=dict(p50=float(np.percentile(cpu, 50)), p90=float(np.percentile(cpu, 90)), p99=float(np.percentile(cpu, 99)), n=len(self.cpu)))
        for s in self.scens: atomic_json(s.out + 'heartbeat.json', hb)
        self.last_hb = time.time()

    def manifiesto(self, status, ficheros):
        dias = sorted({dia_de(m['fin']) for m in self.meta.values() if m['marco'] == '5min'})[-3:]
        for s in self.scens:
            man = dict(job=VERSION, run_id=self.run_id, escenario=s.name, status=status, modo='DRY_RUN (solo simula; 0 ordenes)', codigo=self.hash_ref, hash_check=self.hash_check, sello_print=f'ws_ex-{s.c_print}-1',
                       parametros=dict(niveles=C.LEVELS, tmin=C.TMIN, lat_post=C.LAT_POST, grid=C.GRID, size=C.SIZE, settle_ms=C.SETTLE_MS, c_print=s.c_print, l_ms=list(L_LIST), placebo_semillas=sum(1 for x in s.specs if x.kind == 'PLC'), rebate=C.REB, gap_s=GAP_S, cobertura_min=COBERTURA_MIN),
                       entradas=[dict(fichero=f, bytes=os.path.getsize(f) if os.path.exists(f) else None) for f in ficheros], inicio=self.t_start, fin=time.time() if status != 'RUNNING' else None, saltados=self.skipped, cmd=' '.join(sys.argv))
            atomic_json(s.out + 'run_manifest.json', man)
            for dia in dias: atomic_json(s.out + f'coverage_{dia}.json', self.cobertura(dia))

    # -------- bucle
    def ficheros_vivos(self):
        if self.a.files: return list(self.a.files)
        hoy = dt.datetime.now(dt.timezone.utc); dias = [(hoy - dt.timedelta(days=i)).strftime('%Y-%m-%d') for i in (1, 0)]; fs = []
        for d in dias:
            for f in glob.glob(self.a.dir + f'maker_ms_{d}_*.csv.gz'):
                try: mt = os.path.getmtime(f)
                except OSError: continue
                if d == dias[0] and time.time() - mt > 1800 and hoy.hour >= 1: continue                       # ayer solo si aun crecia o estamos en la primera hora UTC (mercados que cierran 00:0x tras un reinicio)
                if f in self.fkind and self.fkind[f] == 'bn': continue
                fs.append((mt, f))
        return [f for mt, f in sorted(fs)]                                                                     # orden cronologico (mtime), no alfabetico por pid

    def clasifica(self, f, ls):
        """Decide 'pm' (k/q/t del libro de Polymarket) o 'bn' (Binance x/b: se descarta) por la primera fila de datos."""
        for l in ls:
            if not l or l.startswith('tipo,'): continue
            return 'bn' if l[0] in ('x', 'b') else 'pm'
        return None

    def run(self):
        signal.signal(signal.SIGTERM, lambda *a: setattr(self, 'stop', True)); signal.signal(signal.SIGINT, lambda *a: setattr(self, 'stop', True))
        for d in {(dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=i)).strftime('%Y-%m-%d') for i in (0, 1)} | set(self.a.solo_dia or []): self.reconcilia(d)
        self.manifiesto('RUNNING', self.ficheros_vivos()); self.log('INICIO', VERSION, self.run_id, 'escenarios', [(s.name, s.out) for s in self.scens], 'ficheros', self.ficheros_vivos(), 'hash_check', (self.hash_check or {}).get('ok')); estado = 'COMPLETE'
        try:
            while not self.stop:
                nuevo = False
                vivos = self.ficheros_vivos()
                for f in [f for f in self.tails if f not in vivos and not self.a.files]:                       # ficheros que ya no se vigilan: cerrar el manejador
                    try: self.tails.pop(f).fh.close()
                    except OSError: pass
                    self.Wf.pop(f, None)
                for f in vivos:
                    if f not in self.tails:
                        try: self.tails[f] = GzTail(f); self.log('abre', f)
                        except OSError as e: self.log('no abre', f, e); continue
                    try: ls = self.tails[f].poll()
                    except zlib.error as e: self.log('gz ilegible', f, e); del self.tails[f]; continue
                    if not ls: continue
                    if f not in self.fkind:
                        k = self.clasifica(f, ls)
                        if k is None: continue
                        self.fkind[f] = k
                        if k == 'bn': self.cnt['ficheros_binance_ignorados'] += 1; self.log('fichero Binance (x/b), se ignora', f); del self.tails[f]; continue
                    nuevo = True; self.feed(ls, f)
                self.actualiza_W()
                if self.a.once:
                    if not nuevo: break
                    self.ciclo(); continue
                self.ciclo()
                if time.time() - self.last_hb > 30: self.heartbeat(); self.manifiesto('RUNNING', list(self.tails))
                if time.time() - self.last_rss > 5:
                    self.last_rss = time.time(); r = rss_mb()
                    if self.a.max_rss_mb and r > self.a.max_rss_mb: estado = 'FAILED'; self.log(f'RSS {r:.0f} MB > tope {self.a.max_rss_mb}: salgo (los mercados abiertos se reprocesan al reiniciar)'); self.stop = True; self.exit_code = 4
                if not nuevo: time.sleep(0.5)
        except Exception as e:
            estado = 'FAILED'; self.log('EXCEPCION', repr(e)); raise
        finally:
            if self.a.once: self.ciclo(final=True)
            elif self.stop and estado != 'FAILED': estado = 'PARTIAL'
            self.heartbeat('STOPPED_' + estado); self.manifiesto(estado, list(self.tails)); self.log('FIN', estado, 'cerrados', {s.name: s.closed_n for s in self.scens}, 'activos', {s.name: len(s.markets) for s in self.scens}, self.cnt)
        return getattr(self, 'exit_code', 0)


def parse_args(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument('--out', default=DL + 'cxb60_dryrun/'); ap.add_argument('--dir', default=DL); ap.add_argument('--files', nargs='*'); ap.add_argument('--once', action='store_true'); ap.add_argument('--solo-dia', nargs='*')
    ap.add_argument('--retencion-dias', type=int, default=30); ap.add_argument('--c-print', type=int, default=C.C_PRINT, help='sello de la cinta WS del escenario primario = ex - c_print - 1 (19 por defecto)')
    ap.add_argument('--c-print-par', type=int, default=59, help='segundo escenario EN PARALELO (G7 del prereg, sello pesimista) -> OUT/c<N>/ ; 0 lo desactiva')
    ap.add_argument('--placebo', type=int, default=100, help='semillas de placebo PLC60 en el escenario primario (prereg: >=100)'); ap.add_argument('--max-rss-mb', type=int, default=3000, help='sale (exit 4) si el RSS actual lo supera; 0 = sin tope')
    ap.add_argument('--sin-verificar-hash', action='store_true', help='SOLO desarrollo/tests y solo con --once: no comprueba HASHES_CONGELADOS.json')
    a = ap.parse_args(argv); a.out = a.out.rstrip('/') + '/'; a.dir = a.dir.rstrip('/') + '/'
    if a.once and not a.files: ap.error('--once requiere --files')
    if a.sin_verificar_hash and not a.once: ap.error('--sin-verificar-hash solo se admite con --once (el demonio SIEMPRE verifica)')
    return a


def main():
    a = parse_args(); hc = None
    if not a.sin_verificar_hash:
        ok, det = IO.verifica_hashes(); hc = dict(ok=ok, **det)
        if not ok: print('ABORTO (exit 3): hashes de codigo distintos de los congelados / referencia ausente:', json.dumps(det, indent=1), file=sys.stderr, flush=True); sys.exit(3)
    else: hc = dict(ok=None, nota='SIN_VERIFICAR (--sin-verificar-hash, solo desarrollo)')
    r = Run(a); r.hash_check = hc; code = r.run(); sys.exit(code or 0)


if __name__ == '__main__': main()
