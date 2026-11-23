#!/usr/bin/env python3
"""t_proc_cronometro.py [DIA<=17-Nov] -- ESPEC E3: cronometra el tramo de DETECCION del camino de cancelacion por Binance (V5/V6): t_proc = t_send - t_rx_tick, con
t_rx_tick = time.time_ns() al recibir el mensaje WS crudo de Binance; parseo (misma logica que libro_estado_ws.py::_binance_registro: json.loads(raw).get("data") + comprobaciones + extraccion de campos) ->
detector de salto STREAMING con las reglas V5/V6 (variantes_b.V5/V6; equivalencia bit a bit con variantes_b.saltos verificada en test) -> comprobacion de estado (ordenes vivas armadas del lado adverso) -> t_decision ->
t_send = justo antes de la llamada de cancelacion, que aqui es un STUB que NO envia (dry-run/shadow: sin firmar, sin red, sin ordenes). No existe hoy un ejecutor de produccion con disparo por Binance: se declara como equivalente shadow.
Ticks: aggTrade grabados (m5_registro del dia, FB.carga_binance; recepcion rx) reconstruidos como mensaje WS crudo. Dos modos: 'rafaga' (cache caliente, cota inferior) y 'ritmado' (pausa entre eventos = camino mas frio). Registro por medicion en datalogs
(gz, retencion 30 d, fuera de git) y resumen p50/p90/p99 y n por modo. Si p90 > 37 ms => K INSUFFICIENT (contrato). Solo tiempos: 0 EV."""
import sys, os, json, time, gzip, bisect, collections, random, glob
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
DLOG = '/root/polymarket-research-datalogs/rf5_t_proc/'; STALE_MS = 15000
VARS = dict(V5=dict(w_ms=1000, thr_bps=3.0), V6=dict(w_ms=2000, thr_bps=2.0))       # = variantes_b.V5 / V6 (la equivalencia se verifica en test)

def parsea_tick(raw):
    """mensaje WS crudo (bytes/str) -> (simbolo, T_ms, precio) o None. Mismo flujo que libro_estado_ws._binance_registro: json.loads(raw).get('data'); no dict => ignorar; aggTrade => campos s,p,T."""
    try: d = json.loads(raw).get("data")
    except Exception: d = None
    if not isinstance(d, dict): return None
    if d.get("e") == "aggTrade": return d.get("s"), int(d.get("T")), float(d.get("p"))
    return None

class DetectorSalto:
    """V5/V6 streaming por simbolo: en cada tick (instante t = RECEPCION, precio p) devuelve el retorno en bps contra el ultimo tick <= t-w; salto adverso si ret >= +thr (up) o <= -thr (dn) (inclusivo), con tick rancio (>15 s) => sin senal.
    = variantes_b.ret_bps/saltos para ticks ordenados por recepcion (test: equivalencia bit a bit)."""
    def __init__(self, w_ms, thr_bps): self.w = w_ms; self.thr = thr_bps; self.t = collections.deque(); self.p = collections.deque(); self.j0 = None
    def tick(self, t, p):
        self.t.append(t); self.p.append(p)
        lim = t - self.w; ref = None
        while len(self.t) >= 2 and self.t[1] <= lim: self.t.popleft(); self.p.popleft()           # conserva el ultimo tick <= t-w en la cabeza
        if self.t[0] <= lim: ref = self.p[0]
        if ref is None: return None
        r = (p / ref - 1) * 1e4
        return 'up' if r >= self.thr - 1e-12 else ('dn' if r <= -self.thr + 1e-12 else None)

class Estado:
    """ordenes vivas armadas por simbolo y lado (YES: adverso 'dn'; NO: adverso 'up'). cancela() es un STUB: registra la intencion, NO envia."""
    def __init__(self): self.vivas = collections.defaultdict(list); self.intenciones = 0
    def arma(self, sym, lado, oid): self.vivas[(sym, lado)].append(oid)
    def decide(self, sym, direccion):
        lado = 'YES' if direccion == 'dn' else 'NO'; return list(self.vivas.get((sym, lado), ()))
    def cancela_stub(self, oids): self.intenciones += len(oids); return None                       # sin red, sin firma, sin orden

def procesa(raw, dets, estado, t_ms=None):
    """un tick: t_rx -> parseo -> detectores V5/V6 -> estado -> t_dec -> t_send (justo antes del stub). Devuelve None (sin disparo) o (t_rx, t_dec, t_send, {var})."""
    t_rx = time.time_ns()                                   # cronometro: SIEMPRE el reloj real al recibir; t_ms (opcional) = instante de recepcion GRABADO para la logica del detector en el replay
    pt = parsea_tick(raw)
    if pt is None: return None
    sym, T, p = pt; trg = {}; tms = (t_rx // 1_000_000) if t_ms is None else int(t_ms)
    for v, det in dets[sym].items():
        dr = det.tick(tms, p)
        if dr is not None: trg[v] = dr
    if not trg: return None
    oids = []
    for v, dr in trg.items(): oids += estado.decide(sym, dr)
    t_dec = time.time_ns(); t_send = time.time_ns(); estado.cancela_stub(oids); return t_rx, t_dec, t_send, trg

def mensaje(sym, t_ms, p):
    return ('{"stream":"%s@aggTrade","data":{"e":"aggTrade","E":%d,"s":"%s","a":1,"p":"%s","q":"1.0","T":%d,"m":false}}' % (sym.lower(), t_ms, sym, repr(float(p)), t_ms)).encode()

def pct(a, q):
    a = sorted(a); return a[min(len(a) - 1, int(q / 100 * len(a)))] if a else None

def mide(dia, n_eventos=400, seed=20261124, max_ticks=None):
    sys.path.insert(0, HV); import rf5_run as RR
    bs = RR.FB.carga_binance(dia); sims = {'eth': 'ETHUSDT', 'sol': 'SOLUSDT', 'xrp': 'XRPUSDT'}
    ev = []                                                         # (t, sym, p) global ordenado por recepcion
    for c, (t, p) in bs.items(): ev += [(int(a), sims[c], float(b)) for a, b in zip(t, p)]
    ev.sort(); ev = ev[:max_ticks] if max_ticks else ev
    msgs = [(t, mensaje(s, t, p)) for t, s, p in ev]; filas = []; rng = random.Random(seed)
    for modo in ('rafaga', 'ritmado'):
        dets = {s: {v: DetectorSalto(**VARS[v]) for v in VARS} for s in sims.values()}; est = Estado()
        for s in sims.values(): est.arma(s, 'YES', f'{s}-Y1'); est.arma(s, 'NO', f'{s}-N1')
        pausas = 0
        for i, (t, raw) in enumerate(msgs):
            if modo == 'ritmado' and i % 40 == 0: time.sleep(0.002); pausas += 1      # pausa 2 ms cada 40 ticks: camino mas frio (cache/planificador)
            r = procesa(raw, dets, est, t_ms=t)
            if r is not None:
                t_rx, t_dec, t_send, trg = r; filas.append((modo, int(t_rx), int(t_dec), int(t_send), int(t_send - t_rx), '+'.join(sorted(trg)), time.gmtime(t_rx / 1e9).tm_hour, _memavail(), _load1()))
                if modo == 'ritmado' and rng.random() < 0.5: time.sleep(0.003)
    return filas, len(msgs)

def _memavail():
    for l in open('/proc/meminfo'):
        if l.startswith('MemAvailable'): return int(l.split()[1]) // 1024
def _load1(): return float(open('/proc/loadavg').read().split()[0])

def resumen(filas, n_msgs):
    out = dict(n_ticks=n_msgs)
    for modo in ('rafaga', 'ritmado'):
        a = [f[4] for f in filas if f[0] == modo]
        out[modo] = dict(n=len(a), p50_ms=(pct(a, 50) / 1e6 if a else None), p90_ms=(pct(a, 90) / 1e6 if a else None), p99_ms=(pct(a, 99) / 1e6 if a else None), max_ms=(max(a) / 1e6 if a else None))
    return out

if __name__ == '__main__':
    dia = sys.argv[1] if len(sys.argv) > 1 else '2026-11-17'
    if dia >= '2026-11-18': raise SystemExit('dia ciego: prohibido')
    mt = int(sys.argv[2]) if len(sys.argv) > 2 else 500000                  # tope de ticks (RAM): los primeros mt de la rejilla ordenada por recepcion
    filas, n = mide(dia, max_ticks=mt); os.makedirs(DLOG, exist_ok=True)
    nom = DLOG + 't_proc_%s.csv.gz' % time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())
    with gzip.open(nom, 'wt') as f:
        f.write('modo,t_rx_ns,t_dec_ns,t_send_ns,t_proc_ns,var,hora_utc,memavail_mb,load1\n')
        for r in filas: f.write(','.join(map(str, r)) + '\n')
    for old in glob.glob(DLOG + 't_proc_*.csv.gz'):                       # retencion 30 d
        if time.time() - os.path.getmtime(old) > 30 * 86400: os.remove(old)
    r = resumen(filas, n); r.update(dia_ticks=dia, fichero=nom, python=sys.version.split()[0], cpus=os.cpu_count(), load1_inicio=_load1(), p90_gate_ms=37.0, nota='t_proc = t_send - t_rx_tick (parseo + deteccion V5/V6 + estado); cancelacion = STUB sin envio. Computo CPU: no depende de la clase de suelo rx-ex.')
    print(json.dumps(r, indent=1))
