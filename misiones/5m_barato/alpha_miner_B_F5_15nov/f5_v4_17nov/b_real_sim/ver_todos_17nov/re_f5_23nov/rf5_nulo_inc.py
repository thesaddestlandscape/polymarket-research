#!/usr/bin/env python3
"""rf5_nulo_inc.py -- NULO INCREMENTAL de RF5E-COMB-23NOV-v1 (ADENDA_RF5_NULO_INCREMENTAL_24nov, sha 99b0cf26).
Las replicas del nulo se calculan POR DIA en cuanto el dia queda COMPLETE (cron propio con lanza_pesado; no dependen de la mirada), con la permutacion determinista por (dia, j) de rf5_nulo.rng_perm (semilla 20261124) y los
desplazamientos de rf5_nulo.delta_perm. Cada replica es una SIMULACION COMPLETA del dia (acople real busy/MAXV; ver rf5_nulo_run). Salida PRECINTADA: nulo_inc/{FAM}_{DIA}.jsonl guarda SOLO el estadistico por replica
({pol: Delta_dia}); NO guarda ni el observado ni EV/PnL agregado; nadie lo lee hasta decide_mirada (`agrega` exige exactamente los dias de la mirada y que esten TODAS las replicas j < K_max de cada dia: si falta alguna la mirada ESPERA, no se baja K_max
ni se mira con menos). El estado legible (nulo_inc/nulo_inc_estado.json) es solo CONTEOS (replicas hechas por familia y dia).
FAMILIAS Y K_max (adenda sec.3; rf5_fronteras.K_MAX): K = K1..K4 (max-statistic, 250), K6 (1100), A = F1,F2,F3,U13 (500) [enmienda Javi 24-Nov v3.1]. Orden de computo: K, K6, A. SOLO K y K6 bloquean la mirada; A NO bloquea (si A se calcula tarde con ya 10 dias validos, su mirada 1 se salta y se usa el umbral final).
K6 (placebo de Calma, ADENDA_RF5_K6_CALMA_v2 C5; DECLARADO AQUI): estadistico por dia Delta_d = (PnL_K6,d - PnL_K1,d) / Coste_base,d (unidades de primer relleno, mismo criterio que K1..K4; T = media/ee por dias). Replica j = K6 con la fuente Binance de CALMA SOLA
con los TIEMPOS de sus saltos desplazados circularmente delta_perm(dia, j) >= 60 s dentro del dia [d0, d0+24h) (C1: los eventos se calculan UNA vez sobre la serie original, ver rf5_nulo.desplaza_eventos; misma tasa de disparos; V5/V6 y F3 siguen observados); K1 es la replica directa observada del dia. Bajo el nulo la senal de Calma no esta alineada con el mercado.
BC (Besag-Clifford h=20; si no para, p=(1+#)/(K_max+1)) se aplica en `agrega` sobre la secuencia agregada j=0,1,...: calcular replicas de mas no cambia el p. Test: agregado incremental == bloque (rf5_nulo.nulo_K_run con sim_bloque) bit a bit.
NOTA RAM (24-Nov 11:11Z): `--workers N>1` hace fork del proceso con el motor (~3,3 GB) y las paginas se duplican al tocarlas: con la maquina a ~4 GB libres el kernel mato el job (OOM). El defecto es 1 (serie); N>1 solo con >10 GB libres.
C3 (DECLARADO): el nulo de K6 se AGREGA sobre los dias de K6 = rf5_k6.dias_k6 (interseccion de dias validos RF5 con Calma EVALUABLE segun manifest_rf5K6_D.json), los MISMOS que el Delta observado; su mirada es el 6.o / 10.o dia VALIDO DE K6 (`mirada_k6`), no el de RF5. Las replicas se calculan en todos los dias COMPLETE (no se sabe antes de su K6 si es evaluable).
C2 (DECLARADO): cada linea de replica lleva `sello` (hash del codigo del nulo: SELLO_FICH + fuentes externas) y `K_max`; el estado tambien; `lee_replicas`/`agrega_replicas`/`lee_nulo` RECHAZAN (ValueError / None) cualquier sello o K_max distinto; reanudar sobre un fichero con otro sello => BLOCKED (nada se mezcla). verifica_registro (HASHES_rf5.txt) fail-closed al arrancar cola/dia/equiv/corre. workers = 1 FIJO.
Uso:  rf5_nulo_inc.py cola [--fam K|K6|A]                   replicas de TODOS los dias COMPLETE >= 2026-11-24 pendientes (K, K6, A), parando al entrar en 06:00-09:15Z o 22:15-22:30Z (reanudable)
      rf5_nulo_inc.py dia FAM DIA [--K n] [--prueba]  un dia (prueba: solo dias <= 17-Nov, fichero prueba_*, sin manifest)
      rf5_nulo_inc.py equiv FAM DIA [--K 3]                     prueba incremental == bloque, dia <= 17-Nov
      rf5_nulo_inc.py ident FAM DIA                              identidad: replica con delta=0 (PASANDO por el desplazamiento de eventos) == directa bit a bit, K | K6; + eventos de la replica == observados (C1)
      rf5_nulo_inc.py corre FAM [--h 20]                       agrega en la mirada (decide_mirada; RF5_NULO_AUTORIZADO=1 + replicas completas) -> nulo_FAM_resultado.json
0 ordenes, 0 red."""
import sys, os, json, time
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import numpy as np, pandas as pd
import rf5_run as RR, rf5_core as K5, rf5_nulo as NU, rf5_fronteras as FR, rf5_nulo_run as NR

DESDE = '2026-11-24'; ORDEN = ('K', 'K6', 'A'); BLOQUE = 8
SELLO_FICH = ('rf5_core.py', 'rf5_run.py', 'rf5_nulo.py', 'rf5_nulo_run.py', 'rf5_nulo_inc.py', 'rf5_rapido.py', 'calma_hook.py', 'calma_gate.py', 'rf5_fronteras.py', 'rf5_k6.py', 'rf5_cortes.json', 'rf5_t_proc_ms.txt')
_SELLO = {}
def sello():
    """C2: sello de codigo de las replicas = sha256 de {fichero: sha} de SELLO_FICH + todo lo externo/del motor de code_hashes() (no rf5/*: eval, vigia, etc. no cambian las replicas). Cambiar el codigo del nulo => otro sello => las replicas anteriores se rechazan."""
    if 'x' not in _SELLO:
        import hashlib; H = RR.code_hashes(); k = {n: v for n, v in H.items() if not n.startswith('rf5/') or n[4:] in SELLO_FICH}
        _SELLO['x'] = hashlib.sha256(json.dumps(k, sort_keys=True).encode()).hexdigest()[:16]
    return _SELLO['x']
def registro_ok():
    """C2: fail-closed: HASHES_rf5.txt debe cubrir y coincidir con el disco (incluye rf5_nulo_inc.py, run_nulo_inc.sh, cron_nulo_inc.txt)."""
    p = RR.verifica_registro()
    if p: raise SystemExit('BLOCKED registro (HASHES_rf5.txt): ' + '; '.join(p[:5]))
def lee_sellado(path, kmax):
    """{(dia, j): Delta} del fichero de replicas; ValueError si ALGUNA linea valida lleva sello/K_max distinto del vigente (o ninguno). Lineas corruptas/duplicadas: como NU._lee_ckpt."""
    h = {}
    if os.path.exists(path):
        for ln in open(path):
            try: r = json.loads(ln); k = (r['dia'], int(r['j'])); v = r['d']
            except Exception: continue
            if r.get('sello') != sello() or int(r.get('K_max', -1)) != int(kmax): raise ValueError(f"SELLO_O_KMAX_DISTINTO en {os.path.basename(path)}: linea sello={r.get('sello')} K_max={r.get('K_max')} vs vigente sello={sello()} K_max={kmax}")
            h.setdefault(k, v)
    return h
def dir_inc(): return RR.OUT + 'nulo_inc/'
def ruta(fam, d, prueba=False): return dir_inc() + (f'prueba_{fam}_{d}.jsonl' if prueba else f'{fam}_{d}.jsonl')
def ruta_estado(): return dir_inc() + 'nulo_inc_estado.json'

def ventana_ok(hhmm=None):
    """fuera de 06:00-09:15Z y de 22:15-22:30Z."""
    h = int(time.strftime('%H%M', time.gmtime())) if hhmm is None else int(hhmm)
    return (h < 600 or h >= 915) and (h < 2215 or h >= 2230)

class SimK6:
    """placebo de Calma (ver docstring del modulo). Misma interfaz que NR.SimNulo: estado_dia / una / pols."""
    pols = ('K6',)
    def __init__(self, cortes, tp): self.cortes = cortes; self.tp = tp
    def pols_nulo(self): return list(self.pols)
    def estado_dia(self, d, pre):
        import calendar
        E, P, W, ctx = pre; bsrc = RR.FB.carga_binance(d)
        if not bsrc: raise RuntimeError('DATA_BLOCKED: sin m5_registro Binance para %s' % d)
        Rb, c, HK = RR._replay(d, P, W, ctx, 'base', K5.POLITICAS_A, None, self.cortes, None, None); base = NR.unidades_dia(Rb)
        R1, c, HK = RR._replay(d, P, W, ctx, 'K1', K5.POLITICAS_K, bsrc, self.cortes, self.tp, None); k1 = NR.unidades_dia(R1)
        return dict(d=d, P=P, W=W, ctx=ctx, bsrc=bsrc, d0=calendar.timegm(time.strptime(d, '%Y-%m-%d')) * 1000, base=base, k1=k1)
    def __call__(self, d, lista, pre):
        """camino en BLOQUE (referencia de la prueba de equivalencia): estado del dia + todas las replicas de la lista."""
        with RR.desenlace_con_marcador():
            st = self.estado_dia(d, pre); return {j: self.una(st, j, delta) for j, delta in lista}
    def una(self, st, j, delta):
        R, c, HK = RR._replay(st['d'], st['P'], st['W'], st['ctx'], 'K6', K5.POLITICAS_K6, st['bsrc'], self.cortes, self.tp, None, ev_shift=(st['d0'], delta, ('calma',)))     # C1: solo se desplazan los TIEMPOS de los saltos de Calma (serie original); pn, co = NR.unidades_dia(R)
        return {'K6': NR.delta_dia(pn, co, st['k1'][0], st['base'][1])}

def escribe_estado(fam, d, n, kmax, estado):
    """SOLO conteos (replicas hechas / K_max): lo lee el vigia."""
    p = ruta_estado(); e = {}
    try: e = json.load(open(p))
    except Exception: pass
    e.setdefault(fam, {})[d] = dict(n=int(n), K_max=int(kmax), estado=estado, sello=sello(), t=RR.ts()); RR.atomic_json(p, e)

def prepara(fam, d):
    """motor del dia (UNA vez), simulador de la familia y estado compartido por las replicas; debe llamarse dentro de RR.desenlace_con_marcador(). (None si falta t_proc)."""
    import b_policy_sim as BS, eng_v5 as EV
    cortes = K5.lee_cortes(); tp = RR.t_proc()
    if tp is None: return None
    E, info = EV.build(d); P = BS.params(); W = RR.motor(E, False); ctx = dict(W=W, serie=W._serie); pre = (E, P, W, ctx)
    if fam == 'K6': sim = SimK6(cortes, tp)
    else:
        M, base_dia, Rb = NR.prepara_dia(d, E, P, W, ctx, cortes); sim = NR.SimNulo(fam, base_dia, M, cortes, tp)
    return sim, sim.estado_dia(d, pre), pre

def ejecuta(sim, st, d, fam, kmax, path, prueba=False, bloque=BLOQUE):
    """escribe las replicas pendientes j<K_max en `path` (linea JSON con sello + K_max + fsync por replica, reanudable). workers = 1 FIJO (C2; el fork OOM-mato el job). Devuelve 'COMPLETO' | 'PARCIAL'. ValueError si el fichero trae otro sello/K_max."""
    hechos = lee_sellado(path, kmax); pend = [j for j in range(kmax) if (d, j) not in hechos]; n = len(hechos); estado = 'COMPLETO'; sl = sello()
    with open(path, 'a') as fh:
        for i in range(0, len(pend), bloque):
            if not prueba and not ventana_ok(): estado = 'PARCIAL'; break
            for j in pend[i:i + bloque]:
                r = sim.una(st, j, NU.delta_perm(d, j)); fh.write(json.dumps(dict(dia=d, j=j, d=r, sello=sl, K_max=int(kmax))) + '\n'); fh.flush(); os.fsync(fh.fileno()); n += 1
            if not prueba: escribe_estado(fam, d, n, kmax, 'PARCIAL')
    return estado

def calcula_dia(fam, d, kmax=None, prueba=False, bloque=BLOQUE, sufijo=''):
    """replicas j=0..K_max-1 del dia (reanudable: se saltan las hechas). Devuelve 'COMPLETO' | 'PARCIAL' (ventana) | 'NO_APLICA' | 'BLOCKED'."""
    kmax = int(kmax or FR.K_MAX[fam])
    if prueba:
        if d >= '2026-11-18': raise SystemExit('dia ciego: prohibido')
    else:
        m = RR.lee_dia(d)
        if d < DESDE or not m or m.get('status') != 'COMPLETE': return 'NO_APLICA'
    os.makedirs(dir_inc(), exist_ok=True); path = ruta(fam, d, prueba) + sufijo
    try: hechos = lee_sellado(path, kmax)
    except ValueError as ex:
        if not prueba: escribe_estado(fam, d, 0, kmax, 'BLOCKED: ' + str(ex)[:140])
        print(RR.ts(), 'BLOCKED', fam, d, ex); return 'BLOCKED'
    if all((d, j) in hechos for j in range(kmax)):
        if not prueba: escribe_estado(fam, d, kmax, kmax, 'COMPLETO')
        return 'COMPLETO'
    try:
        with RR.desenlace_con_marcador():
            pr = prepara(fam, d)
            if pr is None: return 'BLOCKED'
            sim, st, pre = pr; estado = ejecuta(sim, st, d, fam, kmax, path, prueba, bloque)
    except RuntimeError as ex:
        if not prueba: escribe_estado(fam, d, len(hechos), kmax, 'BLOCKED: ' + str(ex)[:120])
        print(RR.ts(), 'BLOCKED', fam, d, ex); return 'BLOCKED'
    if not prueba: escribe_estado(fam, d, len(lee_sellado(path, kmax)), kmax, estado)
    return estado

def equiv(fam, d, K=3):
    """PRUEBA (dia <= 17-Nov): las replicas j<K por el camino incremental (serie) y por el camino EN BLOQUE de siempre (SimNulo/SimK6.__call__) deben ser IGUALES bit a bit. Un solo motor en memoria. Escribe solo igualdades y conteos (sin EV). workers=1 fijo."""
    if d >= '2026-11-18': raise SystemExit('dia ciego: prohibido')
    registro_ok(); os.makedirs(dir_inc(), exist_ok=True)
    with RR.desenlace_con_marcador():
        pr = prepara(fam, d)
        if pr is None: raise SystemExit('BLOCKED_T_PROC')
        sim, st, pre = pr; pth = ruta(fam, d, True) + '.serie'
        if os.path.exists(pth): os.remove(pth)
        ejecuta(sim, st, d, fam, K, pth, True, 2); ser = lee_sellado(pth, K)
        out = sim(d, [(j, NU.delta_perm(d, j)) for j in range(K)], pre); blo = {(d, j): out[j] for j in range(K)}
    r = dict(dia=d, familia=fam, K=K, workers=1, sello=sello(), n_serie=len(ser), n_bloque=len(blo), serie_igual_bloque=bool(ser == blo), todo_igual=bool(ser == blo and len(blo) == K))
    json.dump(r, open(RR.OUT + f'nulo_inc_equiv_{fam}_{d}.json', 'w'), indent=1); print(json.dumps(r)); return r

def ident(fam, d):
    """C1 (tests a, b, c sobre un dia REAL <= 17-Nov). (a) identidad: la replica con delta=0 PASANDO por el desplazamiento de eventos == la politica directa, BIT A BIT (K: K1..K4 via SimNulo.identidad; K6: replay directo con bsrc_calma=None vs ev_shift delta=0).
    (b)+(c) para delta_perm(d, j) j<5: el desplazamiento es una ROTACION del dia (mismos tiempos tras ordenar el desfase inverso) y el NUMERO de eventos de Calma (K6) / V5 / V6 (K) de la replica == el observado, EXACTO."""
    if d >= '2026-11-18': raise SystemExit('dia ciego: prohibido')
    registro_ok(); os.makedirs(dir_inc(), exist_ok=True); r = dict(dia=d, familia=fam, sello=sello())
    with RR.desenlace_con_marcador():
        pr = prepara(fam, d)
        if pr is None: raise SystemExit('BLOCKED_T_PROC')
        sim, st, pre = pr
        if fam == 'K6':
            R0, c, HK0 = RR._replay(d, st['P'], st['W'], st['ctx'], 'K6', K5.POLITICAS_K6, st['bsrc'], sim.cortes, sim.tp, None)
            R1, c, HK1 = RR._replay(d, st['P'], st['W'], st['ctx'], 'K6', K5.POLITICAS_K6, st['bsrc'], sim.cortes, sim.tp, None, ev_shift=(st['d0'], 0, ('calma',)))
            r['a_identidad_delta0_bit_a_bit'] = bool(NR.igual(R1, R0)); r['ordenes_directa'] = int(len(R0)); r['ordenes_delta0'] = int(len(R1))
        else:
            r['a_identidad_delta0'] = sim.identidad(d, pre)
        # (b)+(c) sobre los hooks (eventos): se construye el hook con la serie observada y se compara J original vs desplazada
        evs = {}
        for nombre, mk in (('calma', lambda: K5.construye_hook('K6', K5.POLITICAS_K6, st['W']._serie, st['bsrc'], sim.cortes, sim.tp, lambda: []).calma), ('v5', lambda: K5.construye_hook('K1', K5.POLITICAS_K, st['W']._serie, st['bsrc'], sim.cortes, sim.tp, lambda: []).v5), ('v6', lambda: K5.construye_hook('K2', K5.POLITICAS_K, st['W']._serie, st['bsrc'], sim.cortes, sim.tp, lambda: []).v6)):
            if (fam == 'K6') != (nombre == 'calma'): continue
            h = mk(); J = h.J; n0 = {c: len(v['up']) + len(v['dn']) for c, v in J.items()}; filas = []
            for j in range(5):
                dl = NU.delta_perm(d, j); S = NU.desplaza_eventos(J, st['d0'], dl); n1 = {c: len(v['up']) + len(v['dn']) for c, v in S.items()}; rot = True
                d0 = st['d0']
                for c, v in J.items():
                    for k in ('up', 'dn'):
                        t = np.asarray(v[k]); en = (t >= d0) & (t < d0 + 86400000); u = np.asarray(S[c][k]); dia = (u >= d0) & (u < d0 + 86400000)
                        back = np.sort(np.concatenate([u[~dia], d0 + (u[dia] - d0 - dl) % 86400000]))                    # desplazamiento inverso == serie original de eventos
                        rot &= bool(np.array_equal(back, np.sort(t)) and int(en.sum()) == int(dia.sum()))
                filas.append(dict(j=j, delta_s=dl / 1000, eventos_observados=n0, eventos_replica=n1, numero_igual=(n0 == n1), rotacion_ok=rot))
            evs[nombre] = dict(eventos_observados=n0, replicas=filas, todo_ok=all(f['numero_igual'] and f['rotacion_ok'] for f in filas))
        r['bc_eventos'] = evs
    r['verde'] = bool((r.get('a_identidad_delta0_bit_a_bit') if fam == 'K6' else all(v['igual'] for v in r['a_identidad_delta0'].values())) and all(v['todo_ok'] for v in r['bc_eventos'].values()))
    json.dump(r, open(RR.OUT + f'nulo_inc_ident_{fam}_{d}.json', 'w'), indent=1, default=str); print(json.dumps(r, default=str)[:3000]); return r

def dias_pendientes():
    est = RR.estado(); return sorted(d for d, m in est.items() if d >= DESDE and m.get('status') == 'COMPLETE')

def cola(fams=ORDEN):
    """familias en el orden K, K6, A; dentro de cada una, dias en orden. Para al cerrarse la ventana."""
    registro_ok(); rc = 'COMPLETO'
    for fam in fams:
        for d in dias_pendientes():
            if not ventana_ok(): return 'PARCIAL'
            r = calcula_dia(fam, d); print(RR.ts(), 'nulo_inc', fam, d, r, flush=True)
            if r == 'PARCIAL': return 'PARCIAL'
            if r == 'BLOCKED': rc = 'BLOQUEADOS_ALGUNOS'
    return rc

# ------------------------------------------------------------------ agregacion (SOLO en la mirada)
def lee_replicas(fam, dias, kmax=None):
    """{(dia, j): {pol: Delta}} de las replicas j<K_max de TODOS los dias; (None, faltan) si falta alguna. Unico lector de las replicas precintadas. ValueError (C2) si algun fichero trae otro sello de codigo o K_max."""
    kmax = int(kmax or FR.K_MAX[fam]); out = {}; faltan = {}
    for d in dias:
        h = lee_sellado(ruta(fam, d), kmax); mis = [j for j in range(kmax) if (d, j) not in h]
        if mis: faltan[d] = len(mis)
        for j in range(kmax):
            if (d, j) in h: out[(d, j)] = h[(d, j)]
    return (None, faltan) if faltan else (out, {})

def agrega_replicas(fam, dias, Tobs, kmax=None, h=FR.H_BC, hechos=None):
    """BC sobre la secuencia agregada. Si falta alguna replica => dict(estado='ESPERA_REPLICAS', faltan). Reutiliza NU.nulo_K_run (el calculo en bloque) con las replicas ya hechas: la unica via de calculo del p."""
    kmax = int(kmax or FR.K_MAX[fam]); faltan = {}
    if hechos is None: hechos, faltan = lee_replicas(fam, dias, kmax)
    if hechos is None: return dict(estado='ESPERA_REPLICAS', faltan=faltan, K_max=kmax)
    tmp = dir_inc() + f'_agrega_{fam}.jsonl'; os.makedirs(dir_inc(), exist_ok=True)
    with open(tmp, 'w') as f:
        for (d, j), v in sorted(hechos.items()): f.write(json.dumps(dict(dia=d, j=j, d=v)) + '\n')
    def nunca(d, lista): raise RuntimeError('agregacion: falta una replica que no deberia faltar')
    try: r = NU.nulo_K_run(list(dias), Tobs, None, tmp, K=kmax, h=h, sim_bloque=nunca, bloque=kmax)
    finally: os.path.exists(tmp) and os.remove(tmp)
    return r

def observado(fam, dias):
    """T observado de la mirada (familias A/K: max-statistic de Tobs_max; K6: T de Delta_d = (PnL_K6 - PnL_K1)/Coste_base). Lee los pkl de los dias de la mirada: SOLO desde `corre`."""
    RA = pd.concat([pd.read_pickle(RR.OUT + f'rf5A_{d}.pkl') for d in dias], ignore_index=True); Rb = RA[(RA.bloq == 0) & (RA.pol == 'base')]
    if fam == 'A': return NR.Tobs_max('A', Rb, RA, NR.FAM['A'][1])
    RK = pd.concat([pd.read_pickle(RR.OUT + f'rf5K_{d}.pkl') for d in dias], ignore_index=True)
    if fam == 'K': return NR.Tobs_max('K', Rb, RK, NR.FAM['K'][1])
    R6 = pd.concat([pd.read_pickle(RR.OUT + f'rf5K6_{d}.pkl') for d in dias], ignore_index=True); dd = []
    for d in dias:
        b = NR.unidades_dia(Rb[Rb.dia == d]); k1 = NR.unidades_dia(RK[(RK.pol == 'K1') & (RK.bloq == 0) & (RK.dia == d)]); k6 = NR.unidades_dia(R6[(R6.pol == 'K6') & (R6.bloq == 0) & (R6.dia == d)]); dd.append(NR.delta_dia(k6[0], k6[1], k1[0], b[1]))
    return dict(Tmax=float(NU.T_stat(dd)), por_politica=dict(K6=dict(T=NU.T_stat(dd), delta_dias=dd)), dias=list(dias))

def dias_calma_ok(dias):
    """dias con manifest_rf5K6_D.json COMPLETE y Calma EVALUABLE (solo lee el manifest, nunca el pkl)."""
    ok = []
    for d in dias:
        try: m = json.load(open(RR.OUT + f'manifest_rf5K6_{d}.json'))
        except Exception: continue
        if m.get('status') == 'COMPLETE' and (m.get('cobertura') or {}).get('calma_evaluable', {}).get('estado') == 'EVALUABLE': ok.append(d)
    return ok

def estado_k6(estado):
    """C3: pseudo-estado para decide_mirada de K6: dia RF5 valido con K6 sin manifest terminal => PENDING (espera); K6 COMPLETE no evaluable => fuera (no cuenta ni espera); evaluable => valido. Asi la mirada de K6 = 6.o / 10.o dia VALIDO DE K6."""
    ok = set(dias_calma_ok([d for d, m in estado.items() if FR.es_valido(m)])); out = {}
    for d, m in estado.items():
        if not FR.es_valido(m): out[d] = m; continue
        if d in ok: out[d] = m; continue
        try: k = json.load(open(RR.OUT + f'manifest_rf5K6_{d}.json')); term = k.get('status') == 'COMPLETE'
        except Exception: term = False
        out[d] = dict(status='NO_EVALUABLE_K6') if term else dict(status='PENDING')
    return out

def mirada_k6(estado):
    """decide_mirada de K6 sobre sus propios dias validos + regla del 20 % de no evaluables (rf5_k6.dias_k6). Devuelve la misma estructura que FR.decide_mirada (mirada 0 si INSUFFICIENT)."""
    import rf5_k6 as K6
    dec = FR.decide_mirada(estado_k6(estado))
    if dec['mirada'] == 0: return dec
    dv = sorted(d for d, m in estado.items() if FR.es_valido(m) and d <= dec['dias'][-1]); r = K6.dias_k6(dv, dias_calma_ok(dv))
    if r['estado'] != 'OK': return dict(mirada=0, nombre='K6_INSUFFICIENT', dias=[], espera=[], motivo=f"{len(r['no_evaluables'])}/{len(dv)} dias no evaluables > 20 %")
    return dec

def decide_fam(fam, estado):
    return mirada_k6(estado) if fam == 'K6' else FR.decide_mirada(estado)

def main_corre(argv):
    if os.environ.get('RF5_NULO_AUTORIZADO') != '1': raise SystemExit('BLOQUEADO: el nulo agregado escribe p_max (EV): solo en la mirada con autorizacion del chief (RF5_NULO_AUTORIZADO=1)')
    registro_ok(); fam = argv[0]; h = int(argv[argv.index('--h') + 1]) if '--h' in argv else FR.H_BC; K = FR.k_max(fam)
    dec = decide_fam(fam, RR.estado())          # dias EXACTOS de la mirada (6 primeros validos | 10 primeros): nunca por argumento
    if dec['mirada'] == 0 or min(dec['dias']) < DESDE: raise SystemExit(f"BLOQUEADO: sin mirada habilitada ({dec['nombre']}: {dec['motivo']})")
    dias = dec['dias']; fk = {'K': 'K1_K4', 'A': 'A', 'K6': 'K6'}[fam]
    if not FR.resolucion_ok(fk, dec['mirada'], 0.01 if fam == 'K6' else None, k=K): raise SystemExit(f'BLOQUEADO: K_max={K} < 5/umbral de la mirada {dec["mirada"]} ({fk})')
    hechos, faltan = lee_replicas(fam, dias, K)
    if hechos is None:
        r = dict(estado='ESPERA_REPLICAS', faltan=faltan, K_max=K, dias=dias, mirada=dec['mirada'], familia=fam); print(json.dumps(r)); return 0          # la mirada ESPERA (no se baja K_max)
    obs = observado(fam, dias); r = agrega_replicas(fam, dias, obs['Tmax'], K, h, hechos)
    r.update(familia=fam, T_max_obs=obs['Tmax'], dias=dias, mirada=dec['mirada'], K_max=K, sello=sello(), umbral_p=(FR.umbral_p(fk, dec['mirada'], 0.01) if fam == 'K6' else FR.umbral_p(fk, dec['mirada'])), estado='NULO_RESIMULADO_EXACTO', origen='incremental (ADENDA_RF5_NULO_INCREMENTAL_24nov)')
    json.dump(r, open(RR.OUT + f'nulo_{fam}_resultado.json', 'w'), indent=1, default=str); print(json.dumps(r, default=str)); return 0

def main(argv):
    modo = argv[0] if argv else ''
    if '--workers' in argv and int(argv[argv.index('--workers') + 1]) != 1: raise SystemExit('workers = 1 FIJO (el fork duplica ~3,3 GB y el kernel mata el job)')
    if modo == 'cola':
        fams = (argv[argv.index('--fam') + 1],) if '--fam' in argv else ORDEN; r = cola(fams); print(RR.ts(), 'cola', r); return 0 if r in ('COMPLETO', 'PARCIAL') else 2
    if modo == 'dia':
        fam, d = argv[1], argv[2]; K = int(argv[argv.index('--K') + 1]) if '--K' in argv else None; registro_ok(); r = calcula_dia(fam, d, K, prueba=('--prueba' in argv)); print(RR.ts(), 'dia', fam, d, r); return 0 if r in ('COMPLETO', 'PARCIAL', 'NO_APLICA') else 2
    if modo == 'equiv':
        fam, d = argv[1], argv[2]; K = int(argv[argv.index('--K') + 1]) if '--K' in argv else 3; r = equiv(fam, d, K); return 0 if r['todo_igual'] else 2
    if modo == 'ident':
        r = ident(argv[1], argv[2]); return 0 if r['verde'] else 2
    if modo == 'corre': return main_corre(argv[1:])
    raise SystemExit(__doc__)

if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
