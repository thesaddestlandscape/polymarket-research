#!/usr/bin/env python3
"""l2_rasgos.py -- R1v2 FASE B, E1 con L2/prints/15m (CONTRATO_RASGOS_E1_L2_19nov.md). 0 ordenes, 0 red, solo lectura de ficheros locales; nada de esto mide EV.
Grupos: A5 (huecos de niveles mejores que el nuestro, GREEN), F (prints en nuestro nivel, ultimos 10 s, GREEN), D1 (cambio del bid del 15m en <=1 s, GREEN), A3 (masa que sale de NUESTRO nivel sin imprimir) y A4 (masa que sale de los niveles MEJORES),
ambos AMBER con la regla de 400 ms, y D2 (TWAP-apertura vs spot; rasgo NORMAL en TRAIN/SELECCION/HOLD: chainlink 26-28 Oct recuperado de git por el chief, ver CL_DIRS; dia ausente = fail-closed, nunca se imputa).
Reglas (contrato sec.0/1): reloj = RECEPCION (rx) siempre; orden (rx, pid, seq) sin mezclar seq entre PIDs (todos los ficheros PID del dia, dedupe por (token,tipo,rx,seq,c1,c2,c3)); una pasada en streaming por dia
(`materializa`), solo tokens de interes; mapa de huecos por (dia, token) y por fichero (seq perdidos, fuera de orden, truncado). Rasgo no evaluable -> NaN (la fila se EXCLUYE, nunca 0): libro desconocido (sin B tras baja/arranque),
o sin stream vivo = ningun B/d del token en (t-30 s, t] SALVO que el latido global (algun d de OTRO token en (t-1 s, t], solo causal) pruebe que el grabador vive y el mercado esta quieto. La MISMA funcion (`Libro.query`) en TRAIN/SELECCION/HOLD.
Regla de 400 ms (A3/A4): una baja de d se clasifica 'cancel' solo si no hay T del mismo token/precio con tamano compatible en [rx_d-400, rx_d+400] Y ya ha pasado ese margen (rx_d <= t-400); las bajas de los ultimos 400 ms
son masa 'ambigua' (rasgo aparte, JAMAS cancelacion): las ventanas [t-300,t-150) y [t-150,t] solo aportan masa ambigua. Se excluye d propio (en replay no existe orden real en el L2).
DECLARADO: tick 0,01; A5 = n de niveles VACIOS de bid entre nuestro L (excl.) y el mejor bid (libro valido sin bids o L >= mejor bid: 0); F cuenta prints a precio == L de cualquier lado (contrato: sin identidad ni flujo tomador); latido global causal (t-1 s, t] en vez de +-1 s."""
import os, re, sys, glob, json, time, heapq, subprocess, pickle, calendar
from array import array
from collections import deque
import numpy as np

ROOT = '/mnt/HC_Volume_106538179/'
DIRS_L5 = [ROOT + 'libro5_ms_prot/', ROOT + 'keep_libro5_ms_prot_permanente/', ROOT + 'keep_libro5_ms_03_05nov/', ROOT + 'archivo_libro5_raw/', ROOT + 'libro5_ms/']
M15 = ROOT + 'm15_registro/m15_registro_%s.csv.gz'
CL_DIR = '/root/polymarket-research/data/prices/'
TICK = 0.01; AMB_MS = 400; VIVO_MS = 30000; HB_MS = 1000; MAX_EDAD_MS = 120000; F_MS = 10000; BUF_MS = 2000; PRE_ROLL_S = 1800; MAX_EVENTOS = 80_000_000
GRUPOS = {'A5': ['a5_huecos'], 'F': ['f_n10', 'f_tam10'], 'A3': ['a3_cf1', 'a3_amb1', 'a3_amb2', 'a3_amb3', 'a3_sal'], 'A4': ['a4_cf1', 'a4_amb1', 'a4_amb2', 'a4_amb3'], 'D1': ['d1_dbid15', 'd1_sin_cambio'], 'D2': ['d2_dist_bps']}
G_BOOK = ('A5', 'F', 'A3', 'A4')
NAN = float('nan')

# ------------------------------------------------------------------ lectura: ficheros PID del dia, streaming, orden (rx, pid, seq)
def rutas_dia(dia, dirs=None):
    """[(pid, ruta)] de TODOS los ficheros libro5_ms del dia (.gz/.zst) en los directorios del contrato; el mismo fichero (mismo nombre) duplicado en otro directorio cuenta una vez (primera ruta). Orden por pid."""
    vistos = {}
    for dd in (dirs or DIRS_L5):
        for p in sorted(glob.glob(f'{dd}libro5_ms_{dia}_*')):
            b = os.path.basename(p)
            if not re.search(r'\.(gz|zst)$', b): continue
            vistos.setdefault(re.sub(r'\.(csv\.)?(gz|zst)$', '', b), p)
    return [(re.sub(r'^libro5_ms_%s_' % dia, '', s), p) for s, p in sorted(vistos.items())]

def abre(p, tokfile):
    """(iterador de lineas, finalizador()->(rc, stderr)). zcat|awk: se filtra por tokens de interes (y todas las G). pipefail: un gz truncado da rc != 0."""
    cat = 'zstdcat' if p.endswith('.zst') else 'zcat'
    cmd = f"set -o pipefail; {cat} '{p}' | awk -F, 'BEGIN{{while((getline l < \"{tokfile}\")>0) t[l]}} NR>1{{n++; s=$8+0; if(n==1||s<mn)mn=s; if(s>mx)mx=s}} $1==\"G\" || ($3 in t){{print}} END{{print \"#SEQ,\" mn \",\" mx \",\" n+0}}'"
    pr = subprocess.Popen(['bash', '-c', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1 << 20)
    def fin():
        err = pr.stderr.read(); rc = pr.wait(); return rc, err
    return pr.stdout, fin

def parse(l):
    f = l.rstrip('\n').split(',')
    if len(f) < 8: return None
    try: return (int(f[6]), int(f[7]), f[0], f[2], f[3], f[4], f[5])        # rx, seq, tipo, token, c1, c2, c3
    except ValueError: return None

def lineas(opener, p, tokfile, rank, info):
    it, fin = opener(p, tokfile); ult = None
    for l in it:
        if l.startswith('#SEQ'):                                   # resumen del stream SIN filtrar (min, max, n de seq): perdidos = (max-min+1) - n
            try: _, mn, mx, n = l.strip().split(','); info['seq_perdidos'] = max(0, int(mx) - int(mn) + 1 - int(n)) if int(n) > 0 else 0
            except ValueError: info['seq_perdidos'] = None
            continue
        e = parse(l)
        if e is None: continue
        info['n_lineas'] += 1; rx, seq = e[0], e[1]
        if ult is not None and seq <= ult: info['retrocesos_seq'] += 1
        ult = seq; yield (rx, rank, seq) + e[2:]
    rc, err = fin(); info['rc'] = rc; info['truncado'] = bool(rc) or ('unexpected end' in (err or ''))

def ordena_buffer(it, buf_ms, info):
    """reordena por (rx, rank, seq) dentro de un buffer de buf_ms; lo que llega mas tarde que el buffer se emite igualmente y se cuenta como fuera_de_orden."""
    h = []; mx = -1; ult = -1
    for e in it:
        if e[0] < ult: info['fuera_de_orden'] += 1
        heapq.heappush(h, e); mx = max(mx, e[0])
        while h and h[0][0] < mx - buf_ms: x = heapq.heappop(h); ult = max(ult, x[0]); yield x
    while h: yield heapq.heappop(h)

def p_niveles(s):
    out = []
    for z in s.split(';'):
        if ':' in z:
            a, b = z.split(':', 1)
            try: out.append((round(float(a), 4), float(b)))
            except ValueError: pass
    return out

TIPO = {'B': 0, 'd': 1, 'T': 2, 'G': 3}

def materializa(dia, ventanas, rutas, opener=abre, tmpdir='/tmp', max_eventos=MAX_EVENTOS):
    """UNA pasada por dia sobre todos los ficheros PID. ventanas {token: (ini_ms, fin_ms[, conexion])} (solo se guardan los eventos con ini <= rx <= fin; el pre-roll lo da el llamador; conexion = coin#marco del grabador, para el latido).
    Devuelve (ev, huecos): ev = arrays compactos por token, ORDENADOS por token y luego por (rx, pid, seq) (np.lexsort tras materializar: el desorden del stream no llega al cursor); rx int64, tipo int8 (0 B, 1 d, 2 T, 3 G), lado int8 (d 0 bid/1 ask, T 0 BUY/1 SELL, G 0 baja/1 arranque),
    precio f32, valor f32 (d nuevo total, T tamano, B indice en snaps), ini/fin por token, conn, win; huecos = mapa por (dia, token) y por fichero (seq_perdidos del stream SIN filtrar). Fichero truncado (rc != 0) declarado: el llamador decide."""
    if len(rutas) > 120: raise ValueError('demasiados ficheros PID (rank int8)')
    toks = sorted(ventanas); ti = {t: i for i, t in enumerate(toks)}; tokfile = os.path.join(tmpdir, f'l2_toks_{dia}.txt')
    with open(tokfile, 'w') as f: f.write('\n'.join(toks) + '\n')
    rx = array('q'); tk = array('i'); tp = array('b'); sd = array('b'); pr = array('f'); vl = array('f'); rk = array('b'); sq = array('q'); snaps = []; infos = {}; gens = []
    def put(r, i, ty, s_, p_, v_, rank, seq): rx.append(r); tk.append(i); tp.append(ty); sd.append(s_); pr.append(p_); vl.append(v_); rk.append(rank); sq.append(seq)
    for rank, (pid, p) in enumerate(rutas):
        info = dict(pid=pid, ruta=p, n_lineas=0, seq_perdidos=0, retrocesos_seq=0, fuera_de_orden=0, rc=None, truncado=False); infos[pid] = info
        gens.append(ordena_buffer(lineas(opener, p, tokfile, rank, info), BUF_MS, info))
    H = {t: dict(n_B=0, n_d=0, n_T=0, n_baja=0, first_rx=None, last_rx=None, max_gap_ms=0, _prev=None) for t in toks}; seen = set(); seen_rx = None; dups = 0; n_ev = 0
    for (r, rank, seq, tipo, tok, c1, c2, c3) in heapq.merge(*gens):
        if r != seen_rx: seen.clear(); seen_rx = r
        key = (tok, tipo, r, seq, c1, c2, c3)
        if key in seen: dups += 1; continue
        seen.add(key)
        if tipo == 'G':
            code = 0 if c1 == 'baja' else (1 if c1 == 'arranque' else None)
            if code is None: continue
            for t in (toks if tok == '*' else ([tok] if tok in ti else [])):
                w = ventanas[t]
                if w[0] <= r <= w[1]: put(r, ti[t], 3, code, 0.0, 0.0, rank, seq); n_ev += 1
                H[t]['n_baja'] += 1 if code == 0 else 0
        elif tok in ti:
            w = ventanas[tok]
            if r < w[0] or r > w[1]: continue                    # fuera de la ventana (pre-roll incluido): no se guarda
            h = H[tok]
            if tipo in ('B', 'd'):
                if h['first_rx'] is None: h['first_rx'] = r
                if h['_prev'] is not None: h['max_gap_ms'] = max(h['max_gap_ms'], r - h['_prev'])
                h['_prev'] = r; h['last_rx'] = r; h['n_B' if tipo == 'B' else 'n_d'] += 1
            if tipo == 'T': h['n_T'] += 1
            if tipo == 'B': snaps.append((p_niveles(c1), p_niveles(c2))); put(r, ti[tok], 0, 0, 0.0, float(len(snaps) - 1), rank, seq)
            elif tipo == 'd':
                try: s_, p_, v_ = (0 if c1 == 'B' else 1), round(float(c2), 4), float(c3)
                except ValueError: continue
                put(r, ti[tok], 1, s_, p_, v_, rank, seq)
            elif tipo == 'T':
                try: s_, p_, v_ = (0 if c2 == 'BUY' else 1), round(float(c1), 4), float(c3)
                except ValueError: continue
                put(r, ti[tok], 2, s_, p_, v_, rank, seq)
            else: continue
            n_ev += 1
        if n_ev > max_eventos: raise MemoryError(f'materializa: >{max_eventos} eventos (guarda de RAM): reducir ventanas')
    rxa = np.frombuffer(rx, dtype=np.int64); tka = np.frombuffer(tk, dtype=np.int32); o = np.lexsort((np.frombuffer(sq, dtype=np.int64), np.frombuffer(rk, dtype=np.int8), rxa, tka))
    ev = dict(toks=toks, rx=rxa[o], tipo=np.frombuffer(tp, dtype=np.int8)[o], lado=np.frombuffer(sd, dtype=np.int8)[o], precio=np.frombuffer(pr, dtype=np.float32)[o], valor=np.frombuffer(vl, dtype=np.float32)[o], snaps=snaps,
              conn=[(ventanas[t][2] if len(ventanas[t]) > 2 else '') for t in toks], win=np.array([[ventanas[t][0], ventanas[t][1]] for t in toks], dtype=np.int64).reshape(-1, 2))
    tks = tka[o]; ev['ini'] = np.searchsorted(tks, np.arange(len(toks)), 'left'); ev['fin'] = np.searchsorted(tks, np.arange(len(toks)), 'right'); del tks, o
    for t in toks: H[t].pop('_prev')
    return ev, dict(dia=dia, ficheros=infos, tokens=H, duplicadas=dups, n_eventos=int(len(rxa)), truncado=any(i['truncado'] for i in infos.values()))

# ------------------------------------------------------------------ libro por token y rasgos (una unica funcion para TRAIN/SELECCION/HOLD)
def clasifica(decs, Ts, t):
    """decs: [(rx, precio, masa)] bajas ordenadas por rx; Ts: [[rx, precio, tam]] prints. -> [(rx, cancel, amb)]: 'cancel' solo si rx <= t-AMB_MS y la masa no la explican T del mismo precio en [rx-400, rx+400] (cada T se consume una vez)."""
    out = []
    for rx, p, m in decs:
        if rx > t - AMB_MS: out.append((rx, 0.0, m)); continue
        c = m
        for T in Ts:
            if T[2] > 0 and abs(T[1] - p) < 1e-6 and rx - AMB_MS <= T[0] <= rx + AMB_MS:
                u = min(T[2], c); T[2] -= u; c -= u
                if c <= 0: break
        out.append((rx, max(c, 0.0), 0.0))
    return out

class Libro:
    def __init__(self): self.reset()
    def reset(self): self.bid = {}; self.ask = {}; self.valido = False; self.last = -10 ** 18; self.dq = deque(); self.tq = deque()
    def baja(self): self.valido = False; self.bid = {}; self.ask = {}; self.dq.clear()
    def _poda(self, rx):
        while self.dq and self.dq[0][0] < rx - 2 * (1000 + AMB_MS): self.dq.popleft()
    def snapshot(self, rx, bids, asks):
        """un B NO borra la historia reciente de d (llega cada pocos segundos): si el libro ya era valido, la diferencia snapshot - libro actual entra en dq como cambios de nivel con el rx del B; solo baja/arranque vacian dq."""
        nb, na = dict(bids), dict(asks)
        if self.valido:
            for lado, old, new in ((0, self.bid, nb), (1, self.ask, na)):
                for p in set(old) | set(new):
                    a, b = old.get(p, 0.0), new.get(p, 0.0)
                    if abs(a - b) > 1e-5 * max(1.0, a, b): self.dq.append((rx, lado, p, a, b))
            self._poda(rx)
        else: self.dq.clear()
        self.bid = nb; self.ask = na; self.valido = True; self.last = rx
    def delta(self, rx, lado, p, new):
        if not self.valido: return                              # antes del primer B tras baja/arranque: estado desconocido, no 'vacio'
        D = self.bid if lado == 0 else self.ask; prev = D.get(p, 0.0)
        if new <= 0: D.pop(p, None)
        else: D[p] = new
        self.dq.append((rx, lado, p, prev, max(new, 0.0))); self.last = rx; self._poda(rx)
    def print_(self, rx, p, s):
        self.tq.append((rx, p, s))
        while self.tq and self.tq[0][0] < rx - F_MS - 2000: self.tq.popleft()
    def query(self, t, L, hb_ok):
        """hb_ok = latido de OTRO token de la MISMA conexion en (t-1 s, t]. Vivo = ultimo B/d propio en (t-30 s, t], o (mercado quieto) latido de la conexion Y ultimo B/d propio a <= MAX_EDAD_MS: un libro congelado no se valida por el latido de otras monedas."""
        out = {k: NAN for g in G_BOOK for k in GRUPOS[g]}; ed = t - self.last
        if not self.valido or not (ed <= VIVO_MS or (hb_ok and ed <= MAX_EDAD_MS)): return out
        L = round(float(L), 4)
        bb = max(self.bid) if self.bid else None; n = 0 if bb is None else min(int(round((bb - L) / TICK)), 100); out['a5_huecos'] = 0.0 if n <= 0 else float(sum(1 for i in range(1, n + 1) if self.bid.get(round(L + i * TICK, 4), 0.0) <= 0))
        pf = [x for x in self.tq if t - F_MS < x[0] <= t and abs(x[1] - L) < 1e-6]; out['f_n10'] = float(len(pf)); out['f_tam10'] = float(sum(x[2] for x in pf))
        evs = [e for e in self.dq if e[0] <= t]; Ts = [[x[0], x[1], x[2]] for x in self.tq if x[0] >= t - 1000 - 2 * AMB_MS and x[0] <= t]
        wins = ((t - 1000, t - 300), (t - 300, t - 150), (t - 150, t + 1))
        for g, sel, now in (('a3', lambda e: e[1] == 0 and abs(e[2] - L) < 1e-6, self.bid.get(L, 0.0)), ('a4', lambda e: e[1] == 0 and e[2] > L + 1e-6, sum(s for p, s in self.bid.items() if p > L + 1e-6))):
            es = [e for e in evs if sel(e)]; sal = 0.0; dec = [(e[0], e[2], e[3] - e[4], e[4]) for e in es if e[3] > e[4]]
            cls = clasifica([(a_, b_, c_) for a_, b_, c_, _ in dec], [list(x) for x in Ts], t)         # alineado por INDICE de evento (dos bajas con el mismo rx y precio no se pisan)
            for j, (lo, hi) in enumerate(wins, 1):
                q0 = now + sum(e[3] - e[4] for e in es if e[0] >= lo); cn = 0.0; am = 0.0
                for (r_, p_, m_, nw), c in zip(dec, cls):
                    if not (lo <= r_ < hi): continue
                    if j == 1:
                        cn += c[1]; am += c[2]
                        if g == 'a3' and c[1] > 0 and nw <= 0: sal = 1.0
                    else: am += m_
                fr = lambda x: float(min(1.0, x / q0)) if q0 > 0 else (0.0 if x <= 0 else 1.0)
                if j == 1: out[g + '_cf1'] = fr(cn)
                out[f'{g}_amb{j}'] = fr(am)
            if g == 'a3': out['a3_sal'] = sal
        return out

class L2Dia:
    """consulta causal de los rasgos L2/15m/D2 de un dia: cursores por token sobre SLICES numpy de los eventos materializados (sin copias en listas); el cursor se desaloja al pasar el fin del mercado (rewind si se vuelve a consultar un t anterior al del cursor)."""
    def __init__(self, ev, m15=None, cl=None, bsrc=None):
        self.ev = ev; self.ti = {t: i for i, t in enumerate(ev['toks'])}; self.cur = {}; self.m15 = m15 or {'tok': {}, 'q': {}}; self.cl = cl; self.bsrc = bsrc or {}; self.n_rewind = 0
        d = ev['tipo'] == 1; tk = np.repeat(np.arange(len(ev['toks'])), ev['fin'] - ev['ini']); o = np.argsort(ev['rx'][d], kind='stable'); self.d_rx = ev['rx'][d][o]; self.d_tok = tk[d][o]; del tk
        cn = ev.get('conn') or [''] * len(ev['toks']); ids = {c: i for i, c in enumerate(sorted(set(cn)))}; self.conn = np.array([ids[c] for c in cn], dtype=np.int32); self.d_conn = self.conn[self.d_tok] if len(self.d_tok) else self.d_tok
        self.win_fin = ev['win'][:, 1] if 'win' in ev and len(ev['win']) else None
    def libera(self, tok): self.cur.pop(self.ti.get(tok), None)
    def _cursor(self, tok):
        i = self.ti[tok]
        if i not in self.cur: self.cur[i] = dict(L=Libro(), pos=0, t=-10 ** 18, a=int(self.ev['ini'][i]), n=int(self.ev['fin'][i] - self.ev['ini'][i]))
        return i, self.cur[i]
    def _avanza(self, tok, t):
        i, c = self._cursor(tok)
        if t < c['t']: c['L'].reset(); c['pos'] = 0; self.n_rewind += 1
        e = self.ev; L = c['L']; j = c['pos']; n = c['n']; a = c['a']; rx = e['rx']
        while j < n and rx[a + j] <= t:
            k = a + j; ty = int(e['tipo'][k]); r = int(rx[k])
            if ty == 0: bids, asks = e['snaps'][int(e['valor'][k])]; L.snapshot(r, bids, asks)
            elif ty == 1: L.delta(r, int(e['lado'][k]), round(float(e['precio'][k]), 4), float(e['valor'][k]))
            elif ty == 2: L.print_(r, round(float(e['precio'][k]), 4), float(e['valor'][k]))
            else: L.baja()
            j += 1
        c['pos'] = j; c['t'] = t; return i, L
    def latido(self, i, t):
        """algun d de OTRO token de la MISMA conexion (coin#marco) en (t-1 s, t] (causal)."""
        j = int(np.searchsorted(self.d_rx, t, 'right')); n = 0; ci = self.conn[i]
        while j > 0 and n < 400:
            j -= 1; n += 1
            if self.d_rx[j] <= t - HB_MS: return False
            if self.d_tok[j] != i and self.d_conn[j] == ci: return True
        return False
    def libro(self, tok, t, L):
        if tok not in self.ti: return {k: NAN for g in G_BOOK for k in GRUPOS[g]}
        i, lb = self._avanza(tok, int(t)); r = lb.query(int(t), L, self.latido(i, int(t)))
        if self.win_fin is not None and int(t) > self.win_fin[i]: self.cur.pop(i, None)         # mercado cerrado: se libera el cursor
        return r
    # --- D1: bid del 15m con el mismo lado y fin15 = floor((fin-300)/900)*900+900 (k15 correcto; NO el 15m previo: fuga 29-Oct)
    def tok15(self, coin, fin, lado):
        f15 = (int(fin) - 300) // 900 * 900 + 900; return self.m15['tok'].get((str(coin).upper(), f15, lado))
    def d1(self, tok15, t):
        out = {'d1_dbid15': NAN, 'd1_sin_cambio': NAN}; q = self.m15['q'].get(tok15)
        if q is None: return out
        rx, bid, ask = q; i = int(np.searchsorted(rx, t, 'right')) - 1; j = int(np.searchsorted(rx, t - 1000, 'right')) - 1
        if i < 0 or j < 0 or t - rx[i] > VIVO_MS or (t - 1000) - rx[j] > VIVO_MS: return out
        if not all(np.isfinite(x) for x in (bid[i], ask[i], bid[j], ask[j])) or bid[i] > ask[i] or bid[j] > ask[j]: return out       # bid vacio = NaN; libro cruzado (bid>ask) en CUALQUIERA de los dos estados: descartado
        out['d1_dbid15'] = float(bid[i] - bid[j]); out['d1_sin_cambio'] = float(rx[i] <= t - 1000); return out
    # --- D2: (spot Binance rx<=t-1000 - TWAP60 de apertura)/TWAP * 1e4, signo a favor del lado. Las filas source=='chainlink' YA son medias RTDS [s-32, s-3] (ws = s): el TWAP60 oficial de apertura e0 = media de ticks [e0-62, e0-3]
    # se aproxima por (fila ws=e0 + fila ws=e0-30 s)/2, disponible SOLO si la fila ws=e0 tiene recepcion (timestamp_utc) <= t (antes: NaN por diseno, misma regla en todos los dias). Contraste con el twap60 oficial de PolyBolt en test_d2_contraste_polybolt.
    def d2(self, coin, fin, t, lado):
        c = str(coin).lower()
        if self.cl is None or c not in self.cl or c not in self.bsrc: return NAN
        ws, rxx, px = self.cl[c]; e0 = (int(fin) - 300) * 1000; m = []
        for s_ in (e0, e0 - 30000):
            lo = int(np.searchsorted(ws, s_, 'left')); hi = int(np.searchsorted(ws, s_, 'right')); sel = rxx[lo:hi] <= t
            if not sel.any(): return NAN
            m.append(float(px[lo:hi][sel].mean()))
        tw = (m[0] + m[1]) / 2.0; tb, pb = self.bsrc[c]; j = int(np.searchsorted(tb, t - 1000, 'right')) - 1
        if j < 0 or t - 1000 - tb[j] > VIVO_MS: return NAN
        return float((1.0 if lado == 'YES' else -1.0) * (pb[j] - tw) / tw * 1e4)
    def rasgos(self, tok, t, L, lado, coin, fin, d2=True):
        f = self.libro(tok, t, L); f.update(self.d1(self.tok15(coin, fin, lado), int(t)))
        if d2: f['d2_dist_bps'] = self.d2(coin, fin, int(t), lado)
        return f

# ------------------------------------------------------------------ cargas auxiliares (15m y chainlink) con streaming
def carga_m15(path, ts_ini_ms=None):
    """{'tok': {(COIN, fin_epoch_s, 'YES'|'NO'): token}, 'q': {token: (rx, bid, ask)}} de m15_registro del dia: k con tf=='15min'; q solo de esos tokens; ordenado por recepcion (c5)."""
    tok = {}
    for l in subprocess.run(['bash', '-c', f"set -o pipefail; zcat '{path}' | awk -F, '$1==\"k\" && $5==\"15min\"'"], capture_output=True, text=True, timeout=1800, check=True).stdout.splitlines():
        f = l.split(',')
        try: fin = calendar.timegm(time.strptime(f[6][:19], '%Y-%m-%d %H:%M:%S'))
        except ValueError: continue
        tok[(f[3].upper(), fin, f[7].strip())] = f[2]
    S = set(tok.values()); rows = {}
    p = subprocess.Popen(['bash', '-c', f"set -o pipefail; zcat '{path}' | awk -F, '$1==\"q\"'"], stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
    for l in p.stdout:
        f = l.split(',')
        if len(f) >= 8 and f[2] in S:
            try: rows.setdefault(f[2], []).append((int(f[7]), float(f[3]) if f[3] != '' else NAN, float(f[4]) if f[4] != '' else NAN))      # bid/ask vacio = NaN (la fila NO se descarta: el estado anterior no queda como bid fantasma)
            except ValueError: pass
    if p.wait() != 0: raise RuntimeError(f'm15_registro truncado/ilegible: {path}')
    q = {}
    for k, v in rows.items(): a = np.array(sorted(v)); q[k] = (a[:, 0].astype(np.int64), a[:, 1], a[:, 2])
    return dict(tok=tok, q=q)

CL_DIRS = (CL_DIR, '/root/polymarket-research-datalogs/chainlink_recuperado_git/')
def carga_chainlink(dia, dirs=CL_DIRS):
    """{coin_min: (ws_ms, rx_ms, px)} solo source=='chainlink' (media 30 s; polybolt_fallback = Pyth, excluido); reloj rx = timestamp_utc (recepcion). 26-28 Oct: recuperados de git en chainlink_recuperado_git (19-Nov, chief).
    FAIL-CLOSED: si el dia no existe en ninguna ruta -> FileNotFoundError (no se imputa ni se sustituye por NaN silencioso)."""
    import pandas as pd
    for d in dirs:
        for ext in ('.csv', '.csv.gz'):
            p = f'{d}chainlink_{dia}{ext}'
            if not os.path.exists(p): continue
            comp = 'gzip' if open(p, 'rb').read(2) == b'\x1f\x8b' else None
            df = pd.read_csv(p, usecols=['timestamp_utc', 'asset', 'price_usd', 'ws_timestamp_ms', 'source'], compression=comp); df = df[df.source == 'chainlink']
            rxs = ((pd.to_datetime(df.timestamp_utc, utc=True, format='mixed') - pd.Timestamp('1970-01-01', tz='UTC')) // pd.Timedelta(milliseconds=1)).values.astype(np.int64); out = {}      # independiente de la resolucion (ns/us) de pandas
            for a, g in df.assign(_rx=rxs).groupby(df.asset.str.lower().str[:3]):
                g = g.sort_values('ws_timestamp_ms'); out[a] = (g.ws_timestamp_ms.values.astype(np.int64), g._rx.values.astype(np.int64), g.price_usd.values.astype(float))
            return out
    raise FileNotFoundError(f'chainlink {dia} no existe en {dirs} (fail-closed: D2 no se imputa)')

def ventanas_m5(m5_path, pre_s=PRE_ROLL_S, coins=('ETH', 'SOL', 'XRP')):
    """{token: (ini_ms, fin_ms, 'COIN#5min')} de los mercados 5min de m5_registro (filas k) con pre-roll de pre_s; fin = fin del mercado + 5 s."""
    out = {}
    for l in subprocess.run(['bash', '-c', f"set -o pipefail; zcat '{m5_path}' | awk -F, '$1==\"k\" && $5==\"5min\"'"], capture_output=True, text=True, timeout=1800, check=True).stdout.splitlines():
        f = l.split(',')
        if f[3].upper() not in coins: continue
        try: fin = calendar.timegm(time.strptime(f[6][:19], '%Y-%m-%d %H:%M:%S'))
        except ValueError: continue
        out[f[2]] = ((fin - 300 - pre_s) * 1000, (fin + 5) * 1000, f[3].upper() + '#5min')      # conexion del grabador = coin#marco
    return out

def guarda(path, obj):
    with open(path + '.tmp', 'wb') as f: pickle.dump(obj, f, protocol=4)
    os.replace(path + '.tmp', path)
