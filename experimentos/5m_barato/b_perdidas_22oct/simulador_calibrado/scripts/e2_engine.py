#!/usr/bin/env python3
"""e2_engine.py -- PREREG_E2_ORDEN_DECIDIR (sha 86ffe92c...). Motor MOCK: ejecuta el decidir() REAL de experimento_maker_h47.py (sin editar) sobre el libro5
grabado con reloj virtual. NO crea cliente CLOB, NO firma, NO lee .env, NO escribe en ningun ledger. Solo lectura de produccion."""
import os, sys, json, bisect, hashlib, random, bisect
sys.dont_write_bytecode = True
os.environ['E1Q_FASE'] = 'MEDIR'
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_E2_ORDEN_DECIDIR.md'), 'rb').read()).hexdigest().startswith('86ffe92c14e58312')
CV = os.path.join(AQ, '../../cola_vs_cruce/scripts'); sys.path.insert(0, CV)
import numpy as np
import e1q_sim as S
DEV = '/root/polymarket-research-dev'; sys.path.insert(0, DEV)
import experimento_maker_h47 as H
H_SHA = hashlib.sha256(open(H.__file__, 'rb').read()).hexdigest()
assert H_SHA.startswith('c82f5dc5f304b8a6'), H_SHA


class FakeTime:
    now = 0.0
    def time(self): return FakeTime.now
    def sleep(self, s): raise RuntimeError('sleep en mock')
H.time = FakeTime()
H.X.leer_ledger = lambda *a, **k: []          # decidir() lo llama alrededor del POST; el mock no toca ningun ledger
LAT_POST, LAT_CAN = 0.085, 0.055
OPP = S.OPP


class Mkt:
    def __init__(self, act, mid, fin):
        ev = S.load(S.SRC + f'mk/{act}_{mid}.gz')
        self.act, self.mid, self.fin = act, mid, fin
        self.TT, self.TV, self.lvl, self.NT, self.roto = S.prepara(ev, fin) if ev else (None, None, None, None, True)
        self.lvt = {k: ([x[0] for x in h], [x[1] for x in h]) for k, h in (self.lvl or {}).items()}
        self.w = S.DES.get(mid)

    def nivel(self, L, q, t):
        h = self.lvt.get((L, q))
        if not h: return 0.0
        i = bisect.bisect_right(h[0], t) - 1
        return h[1][i] if i >= 0 else 0.0


class FakeLib:
    tick_cambiado = False
    def __init__(self, mk, dobs_ms):
        self.mk, self.dobs = mk, dobs_ms
    def _t(self): return int(round(FakeTime.now * 1000)) - self.dobs
    def top(self, tok):
        t = self._t(); b = S.top_at(self.mk.TT, self.mk.TV, tok, t); bo = S.top_at(self.mk.TT, self.mk.TV, OPP[tok], t)
        bid = (b / 1000.0, self.mk.nivel(tok, b, t)) if b > 0 else None
        ask = ((1000 - bo) / 1000.0, 0.0) if bo > 0 else None
        return bid, ask
    def tamano_nivel(self, tok, precio): return float(self.mk.nivel(tok, H.mils(precio), self._t()))
    def mejor_bid_ajeno(self, tok, *a, **k):
        t = self._t(); b = S.top_at(self.mk.TT, self.mk.TV, tok, t); return b / 1000.0 if b > 0 else None
    def fresco(self): return True


class MockExp(H.Exp47):
    kill = None            # sombrea la propiedad de X.Exp
    senal = False
    def __init__(self, alloc='prop', budget=None):
        self.real = False; self.escalon = 'B'; self.t_stop = H.T_STOP_DEF; self.size = 5; self.min_nocional = 1.0; self.max_vivas = H.MAX_VIVAS
        self.n_max = 500; self.vivas = {}; self.canceladas = {}; self.enfriar_tok = {}; self.slugs_usados = set(); self.parada = False
        self.n_ordenes_total = 0; self.ctxs = {}; self.recs = []; self.rec = {}; self.mkts = {}; self.alloc = alloc; self.budget = budget; self.nblk = 0
        self._est = {}
    # ---- E/S sustituida
    def _log47(self, ev): pass
    def _bloqueo(self, *a, **k): pass
    def _libro5(self, lib, tok): return {'bids': [], 'asks': []}
    def parar(self, motivo): self.parada = True
    def liquidar(self, *a, **k): return None
    def puede_enviar(self, coste):
        if self.budget is None: return True
        comp = sum(float(o['size']) * float(o['precio']) for o in list(self.vivas.values()) + list(self.canceladas.values()))
        ok = self.budget(FakeTime.now) - comp - coste >= -1e-9
        if not ok: self.nblk += 1
        return ok
    def post(self, slug, tok, lado, precio, size, cola, lib=None, ajeno_dec=None, ask_dec=None, fin=None):
        now = FakeTime.now; mk = self.mkts[slug]; self.n_ordenes_total += 1
        h = f'o{len(self.recs)}'; t_live = now + LAT_POST
        res = S.vida_orden(mk.lvl, mk.NT, tok, H.mils(precio), int(round(t_live * 1000)), int((fin - self.t_stop + 3) * 1000), size, self.alloc)
        rec = dict(h=h, slug=slug, tok=tok, precio=precio, size=size, t_dec=now, t_live=t_live, fill=res, t_cancel=None, t_can_eff=None, filled=False)
        self.recs.append(rec); self.rec[h] = rec
        self.vivas[h] = {'tok': tok, 'lado': lado, 'precio': precio, 'size': size, 't_post': now + 0.137, 'cola': cola, 'slug': slug, 'visto': False}
        return h
    def cancelar(self, h):
        o = self.vivas.pop(h, None)
        if o is None: return False
        now = FakeTime.now; rec = self.rec[h]; rec['t_cancel'] = now; rec['t_can_eff'] = now + LAT_CAN; o['t_cancel'] = now
        self.canceladas[h] = o; return True
    # ---- bucle por mercado (lo que paso() hace alrededor de decidir)
    def _relleno(self, c, h, tras_cancel):
        rec = self.rec[h]; e = c.estado[rec['tok']]; acc = rec['fill'][1]
        e['llenas'] += acc; e['coste'] += acc * rec['precio']
        e['rellenos'].append({'oid': h, 'acc': acc, 'precio': rec['precio'], 'tras_cancel': tras_cancel}); rec['filled'] = True
    def detectar(self, c, now):
        for h, o in list(self.vivas.items()):
            if o['slug'] != c.mk['slug']: continue
            f = self.rec[h]['fill']
            if f is not None and f[0] / 1000.0 <= now:
                self._relleno(c, h, False); del self.vivas[h]
    def asentar(self, c, now):
        for h, o in list(self.canceladas.items()):
            if o['slug'] != c.mk['slug'] or now - o['t_cancel'] < H.X.ASENTAR_S: continue
            f = self.rec[h]['fill']
            if f is not None and f[0] / 1000.0 < self.rec[h]['t_can_eff']: self._relleno(c, h, True)
            del self.canceladas[h]
    def tick(self, c, now):
        T = c.mk['fin'] - now
        if c.fase == 'previa':
            if T > H.T_INI: return
            c.fase = 'activa'
        if c.fase == 'activa':
            if T <= self.t_stop:
                c.fase, c.t_cierre = 'asentando', now; return
            if now - c.ult_poll >= H.POLL_S:
                c.ult_poll = now; self.detectar(c, now); self.asentar(c, now)
            elif now - c.ult_poll_can >= 0.15:
                c.ult_poll_can = now; self.asentar(c, now)
            self.decidir(c, T, now)
        elif c.fase == 'asentando':
            for h in [h for h, o in self.vivas.items() if o['slug'] == c.mk['slug']]:
                f = self.rec[h]['fill']
                if f is not None and f[0] / 1000.0 <= now: self._relleno(c, h, False); del self.vivas[h]
                else: self.cancelar(h)
            self.asentar(c, now)
            if not [1 for o in list(self.vivas.values()) + list(self.canceladas.values()) if o['slug'] == c.mk['slug']]: c.fase = 'fin'


def run_slot(mkts, cad, dobs_ms, budget, alloc, seed):
    """mkts: {act: Mkt} del mismo cierre. Devuelve (filas de ordenes, filas de pujas)."""
    fin = next(iter(mkts.values())).fin
    ex = MockExp(alloc=alloc, budget=budget); ctxs = {}
    for act in sorted(mkts):
        mk = mkts[act]; slug = f"{act.lower()}-updown-5m-{fin - 300}"
        ex.mkts[slug] = mk
        m = {'slug': slug, 'id': mk.mid, 'toks': {'Up': 'Y', 'Down': 'N'}, 'fin': fin, 'min_size': None}
        c = H.Ctx(act.lower(), m, FakeLib(mk, dobs_ms), H.K_POR_MONEDA[act.lower()]); ctxs[act] = c; ex.ctxs[act] = c
    rng = random.Random(f'{seed}-{fin}-{cad}'); now = fin - H.T_INI - 1 + rng.random() * cad
    while now < fin + 20 and any(c.fase != 'fin' for c in ctxs.values()):
        FakeTime.now = now
        for act in sorted(ctxs):
            if ctxs[act].fase != 'fin': ex.tick(ctxs[act], now)
        now += cad
    orders, pujas = [], []
    for act, c in ctxs.items():
        mk = mkts[act]; recs = [r for r in ex.recs if r['slug'] == c.mk['slug']]
        for i, r in enumerate(recs):
            end = r['t_can_eff'] if r['t_can_eff'] is not None else (r['fill'][0] / 1000.0 if r['fill'] else np.nan)
            orders.append(dict(act=act, mid=mk.mid, fin=fin, n=i + 1, tok=r['tok'], precio=r['precio'], size=r['size'], t_dec=r['t_dec'], t_live=r['t_live'],
                               t_cancel=r['t_cancel'], t_can_eff=r['t_can_eff'], fill_r=(r['fill'][0] if r['fill'] else np.nan),
                               fill_acc=(r['fill'][1] if r['fill'] else np.nan), fill_tipo=(r['fill'][2] if r['fill'] else ''), filled=int(r['filled'])))
        if not recs: continue
        L = c.tok; fl = [r for r in recs if r['filled']]
        w = mk.w; gana = int((w == 'YES') == (L == 'Y')) if w is not None else -1
        row = dict(act=act, mid=mk.mid, fin=fin, lado_sim=L, n_ord=len(recs), fill=int(bool(fl)), gana=gana, nblk=ex.nblk, fin_puja='relleno' if fl else 't_stop')
        if fl:
            r = fl[0]; row.update(p=r['precio'], acc=r['fill'][1], r=r['fill'][0], tl=r['t_live'] * 1000.0, tipo=r['fill'][2], clase=clase_u(mk.NT, L, r['fill'][0], H.mils(r['precio']), r['fill'][2]))
        pujas.append(row)
    return orders, pujas


def clase_u(NT, L, r, o, tipo, tau1=25):
    """Clase del relleno simulado con la definicion on-chain a partir de prints L2: C1 = print mas hondo (q<o) dentro de [r, r+tau1]; C2 = en (r+tau1, r+2000]; C3 = resto."""
    if tipo == 'X': return 'C1'
    arr = NT[L]; i = bisect.bisect_left(arr, (r, -1, 0))
    c2 = False
    for (rr, q, acc) in arr[i:]:
        if rr > r + 2000: break
        if q < o:
            if rr <= r + tau1: return 'C1'
            c2 = True
    return 'C2' if c2 else 'C3'


def make_budget():
    """H(t): ultima observacion del ledger real (suelo_fijado/subido: saldo-suelo; bloqueo: saldo-minimo); 5.0 antes de la primera."""
    import datetime
    obs = []
    for l in open('/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'):
        try: d = json.loads(l)
        except Exception: continue
        if not d.get('real'): continue
        t = d.get('tipo')
        if t in ('suelo_fijado', 'suelo_subido'): h = d['saldo'] - d['suelo']
        elif t == 'bloqueo_suelo_saldo': h = d['saldo'] - d['minimo']
        else: continue
        obs.append((datetime.datetime.fromisoformat(d['ts']).timestamp(), h))
    obs.sort(); ts = [o[0] for o in obs]; hs = [o[1] for o in obs]
    def f(t):
        i = bisect.bisect_right(ts, t) - 1
        return hs[i] if i >= 0 else 5.0
    return f, len(obs)
