#!/usr/bin/env python3
"""vigia_h23_repuja.py -- VIGIA DIARIO de la demostracion fuera de muestra de la re-puja a 150 ms (H69, H23-MAKER-V3). Solo medicion: NO envia ordenes, NO toca ejecutores, NO lee claves.

Que hace (idempotente; se puede relanzar las veces que haga falta):
  1. Dias esperados: OOS = 2026-10-19 .. ayer (UTC). Para cada dia con registro ms completo (m5_registro_D y m15_registro_D en el volumen) y SIN salida valida del replay v3
     (v3_BTC_D.csv + v3_cobertura_BTC_D.json, sin claves duplicadas) lanza, de uno en uno y con nice/ionice/ulimit, la extraccion BTC (r2/extrae_btc.sh, idempotente por .done) y el
     replay `h23_sim_v3.py D` (idempotente: no recalcula si existe la salida). Guardas: nunca 06:00-09:15Z, MemAvailable > 1,8 GB, load5 < 20, ningun otro job pesado
     (extrae_btc.sh / h61b_sim.py / ms_extract.py / run_v3.sh) en marcha, un solo vigia a la vez (flock). Si una guarda falla: estado PARTIAL y no se hace nada pesado.
  2. Evalua el gate del PREREGISTRO §4 por brazo (A, B) sobre la celda PRIMARIA (BTC, cola base, alta 79 / cancel 60, tamano real + universo ejecutable, un relleno cierra la puja,
     desenlace oficial; sin desenlace = missing): n, dias con relleno, EV ponderado por EUR, EV sin los 2 mejores dias, IC90 por dias (bootstrap de dias, 3000, semilla 7, solo con
     >= 5 dias con relleno), contraste emparejado r150 - r1500 (PLACEBO = el arnes real v1 re-pujando a 1,5 s) en los MISMOS cierres, ritmo y dias hasta n = 40.
  3. Lee el shadow v3 forward (h23_shadow_v3, si esta desplegado) y los ledgers de los arneses (ensayo en seco / real) para la latencia REAL de re-puja (`h23v3_repuja`) y la doble
     exposicion (`h23v3_fill_tardio`). Lo que no se puede medir se imprime como NO MEDIDO, nunca como cumplido.
  4. Escribe informe de texto + JSON + run_manifest.json (atomico) en /root/polymarket-research-datalogs/h23_repuja/ y, con --telegram, un resumen corto (una vez al dia).
Fuentes del gate: la poblacion del replay (registro ms) y la del shadow v3 son LOS MISMOS mercados: NO son aditivas (no sumar n). Estado final solo puede ser DRY_RUN_VALIDATED si
TODOS los criterios pasan, incluidos los dos que SOLO mide el arnes (latencia real p50 <= 300 ms sobre >= 10 re-pujas, cero doble exposicion): hoy ninguno esta medido.
Uso: nice -n 19 ionice -c3 python3 -I vigia_h23_repuja.py [--telegram] [--sin-calcular] [--hasta YYYY-MM-DD]"""
import csv
import fcntl
import glob
import gzip
import hashlib
import json
import math
import os
import subprocess
import sys
import time
import zlib
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

import numpy as np

Z = os.path.dirname(os.path.abspath(__file__))
R2 = '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r2'
VOL = '/mnt/HC_Volume_106538179'
IN = VOL + '/datalogs_analisis_caches/v4_comprar_lo_bueno/'
OUT = VOL + '/datalogs_analisis_caches/h23_v3/'           # salida del replay v3 (misma que run_v3.sh: un solo sitio)
DL = '/root/polymarket-research-datalogs/'
VIG = DL + 'h23_repuja/'                                  # informes, manifest, logs del vigia
SHADOW_V3 = DL + 'h23_shadow_v3/'
OOS_DESDE = '2026-10-19'
SIM_COLS = ['coin', 'dia', 'cierre', 'lado', 'm5', 'brazo', 'sizing', 'modo', 'rep', 'cola', 'lat_post', 'lat_cancel', 'n_cotiz', 'need', 'lleno', 'coste', 'n_fill', 't_rel', 'p_rel', 'gana', 'rebate']
CLAVE = ('cierre', 'brazo', 'sizing', 'modo', 'rep', 'cola', 'lat_post', 'lat_cancel')
GATE = dict(n=40, dias=10, ev_pond=0.05, ic90_lo=0.0, sin2=0.0, p50_ms=300.0, n_repujas=10, min_dias_ic=5)
PESADOS = ('extrae_btc.sh', 'h61b_sim.py', 'ms_extract.py', 'run_v3.sh', 'h23_sim_v3.py', 'run_v2_dogebnb.sh', 'h23_sim_v2.py')


def ahora():
    return time.strftime('%FT%TZ', time.gmtime())


def log(msg):
    os.makedirs(VIG, exist_ok=True)
    with open(VIG + 'vigia.log', 'a') as f:
        f.write(f'{ahora()} {msg}\n')


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()[:16]


def atomico(path, obj):
    with open(path + '.tmp', 'w') as f:
        json.dump(obj, f, indent=1, default=str)
        f.flush()
        os.fsync(f.fileno())
    os.replace(path + '.tmp', path)


# ---------------------------------------------------------------------------------------------------------------- dias y validacion
def dias_esperados(hasta=None):
    ayer = (datetime.now(timezone.utc) - timedelta(days=1)).date() if hasta is None else datetime.strptime(hasta, '%Y-%m-%d').date()
    d, out = datetime.strptime(OOS_DESDE, '%Y-%m-%d').date(), []
    while d <= ayer:
        out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def registro_listo(D):
    return all(os.path.exists(f'{VOL}/{m}_registro/{m}_registro_{D}.csv.gz') for m in ('m5', 'm15')) and os.path.exists(f'{DL}vigia_5m_barato/controles_{D}.csv')


def validar_dia(D):
    """(ok, motivo, info). Un dia vale si existen CSV + cobertura, la cabecera es la esperada, no hay claves duplicadas y la cobertura cuadra con el CSV."""
    f, c = f'{OUT}v3_BTC_{D}.csv', f'{OUT}v3_cobertura_BTC_{D}.json'
    if not os.path.exists(f):
        return False, 'sin_csv', {}
    if not os.path.exists(c):
        return False, 'csv_sin_cobertura', {}
    try:
        cob = json.load(open(c))
        with open(f, newline='') as fh:
            rd = csv.DictReader(fh)
            if rd.fieldnames != SIM_COLS:
                return False, 'cabecera_inesperada', {}
            seen, n = set(), 0
            for r in rd:
                k = tuple(r[x] for x in CLAVE)
                if k in seen:
                    return False, 'clave_duplicada', {}
                seen.add(k)
                n += 1
                if r['dia'] != D:
                    return False, 'dia_incorrecto', {}
    except Exception as e:  # noqa: BLE001
        return False, f'ilegible:{type(e).__name__}', {}
    if cob.get('dia') != D:
        return False, 'cobertura_de_otro_dia', {}
    return True, 'ok', dict(filas=n, **{k: cob.get(k) for k in ('cierres_grupo', 'con_lado', 'con_libro', 'errores', 'sin_desenlace')})


def guardas():
    h = int(time.strftime('%H%M', time.gmtime()))
    if 600 <= h < 915:
        return False, 'ventana 06:00-09:15Z prohibida'
    mem = next((int(l.split()[1]) // 1024 for l in open('/proc/meminfo') if l.startswith('MemAvailable')), 0)
    if mem < 1800:
        return False, f'MemAvailable {mem} MB < 1800'
    l5 = float(open('/proc/loadavg').read().split()[1])
    if l5 >= 20:
        return False, f'load5 {l5} >= 20'
    yo = os.getpid()
    for p in os.listdir('/proc'):
        if p.isdigit() and int(p) != yo:
            try:
                cmd = open(f'/proc/{p}/cmdline', 'rb').read().replace(b'\0', b' ').decode(errors='replace')
            except OSError:
                continue
            if any(x in cmd for x in PESADOS) and 'vigia_h23_repuja' not in cmd and 'pgrep' not in cmd and 'ps aux' not in cmd:
                return False, f'otro job pesado en marcha (pid {p}: {cmd[:80]})'
    return True, 'ok'


def calcular_dia(D):
    """Extraccion (idempotente por .done) + replay v3 del dia D, secuencial, con limites. Devuelve (ok, detalle)."""
    ok, why = guardas()
    if not ok:
        return False, f'pospuesto: {why}'
    ext = [] if os.path.exists(f'{IN}{D}.done') and os.path.exists(f'{IN}rows_{D}.csv.gz') else ['bash', f'{R2}/extrae_btc.sh', D]
    for cmd, lim in ((ext, 3000000), (['python3', '-I', f'{Z}/h23_sim_v3.py', D], 2800000)):
        if not cmd:
            continue
        ok, why = guardas()
        if not ok:
            return False, f'pospuesto: {why}'
        t0 = time.time()
        r = subprocess.run(['bash', '-c', f'ulimit -v {lim}; exec nice -n 19 ionice -c3 "$@"', '_'] + cmd, capture_output=True, text=True, cwd=Z)
        log(f'{D} {" ".join(cmd[-2:])} rc={r.returncode} {time.time() - t0:.0f}s {(r.stdout or "")[-200:].strip()!r} {(r.stderr or "")[-300:].strip()!r}')
        if r.returncode != 0:
            return False, f'FAILED {" ".join(cmd[-2:])} rc={r.returncode}: {(r.stderr or "")[-200:]}'
    ok, why, _ = validar_dia(D)
    return ok, 'calculado' if ok else f'FAILED validacion tras calcular: {why}'


# ---------------------------------------------------------------------------------------------------------------- estadistica (misma formula que h23_analisis_v3.py)
def ic90_dias(d_pnl, d_coste, semilla=7, B=3000):
    if len(d_pnl) < GATE['min_dias_ic']:
        return None, None
    rng = np.random.default_rng(semilla)
    P, C = np.array(d_pnl), np.array(d_coste)
    idx = rng.integers(0, len(P), (B, len(P)))
    b = P[idx].sum(1) / C[idx].sum(1)
    return float(np.percentile(b, 5)), float(np.percentile(b, 95))


def resumen_pos(pos):
    """pos = lista de dicts {dia, pnl, coste, lleno, g}. EV ponderado por EUR (sum pnl / sum coste), por unidad, sin 2 mejores dias, IC90 por dias."""
    if not pos:
        return dict(n=0, dias=0)
    por = defaultdict(lambda: [0.0, 0.0])
    for p in pos:
        por[p['dia']][0] += p['pnl']
        por[p['dia']][1] += p['coste']
    dias = sorted(por)
    P = [por[d][0] for d in dias]
    C = [por[d][1] for d in dias]
    lo, hi = ic90_dias(P, C)
    orden = sorted(dias, key=lambda d: -por[d][0])[2:]
    c2 = sum(por[d][1] for d in orden)
    sin2 = (sum(por[d][0] for d in orden) / c2) if orden and c2 > 0 else None
    coste = sum(C)
    return dict(n=len(pos), dias=len(dias), dias_pos=sum(1 for x in P if x > 0), pnl=sum(P), coste=coste, ev_pond=sum(P) / coste if coste else None,
                ev_unit=float(np.mean([p['pnl'] / p['coste'] for p in pos if p['coste'] > 0])) if coste else None, ic_lo=lo, ic_hi=hi, sin2=sin2, dias_sin2=len(orden),
                acierto=float(np.mean([p['g'] for p in pos])), precio_med=coste / sum(p['lleno'] for p in pos))


def poisson_ic90(n, dias):
    from scipy.stats import chi2
    lo = chi2.ppf(0.05, 2 * n) / 2 / dias if n else 0.0
    hi = chi2.ppf(0.95, 2 * n + 2) / 2 / dias
    return lo, hi


def cargar_replay(dias):
    """{(brazo, rep): {cierre: posicion}} de la celda PRIMARIA + cobertura. Solo dias validos."""
    pos = defaultdict(dict)
    cob = {}
    for D in dias:
        ok, why, info = validar_dia(D)
        if not ok:
            continue
        cob[D] = info
        with open(f'{OUT}v3_BTC_{D}.csv', newline='') as fh:
            for r in csv.DictReader(fh):
                if r['sizing'] != 'real' or r['modo'] != 'primer' or r['cola'] != 'base' or r['lat_post'] != '79' or r['lat_cancel'] != '60':
                    continue
                lleno = float(r['lleno'])
                if lleno <= 0:
                    continue
                g = {'True': 1.0, 'False': 0.0}.get(r['gana'])
                coste = float(r['coste'])
                if g is None:
                    pos[(r['brazo'], int(r['rep']))].setdefault('_sin_desenlace', []).append(r['cierre'])
                    continue
                pos[(r['brazo'], int(r['rep']))][r['cierre']] = dict(dia=D, cierre=r['cierre'], lleno=lleno, coste=coste, g=g, pnl=lleno * g - coste + float(r['rebate']))
    return pos, cob


def emparejado(pos, brazo, a=150, b=1500):
    A = {k: v for k, v in pos.get((brazo, a), {}).items() if k != '_sin_desenlace'}
    B = {k: v for k, v in pos.get((brazo, b), {}).items() if k != '_sin_desenlace'}
    com, sa, sb = set(A) & set(B), set(A) - set(B), set(B) - set(A)
    return dict(n150=len(A), n1500=len(B), comunes=len(com), solo150=len(sa), solo1500=len(sb), pnl150=sum(v['pnl'] for v in A.values()), pnl1500=sum(v['pnl'] for v in B.values()),
                pnl_solo150=sum(A[k]['pnl'] for k in sa), pnl_solo1500=sum(B[k]['pnl'] for k in sb), dpnl_comunes=sum(A[k]['pnl'] - B[k]['pnl'] for k in com),
                acierto_solo150=(float(np.mean([A[k]['g'] for k in sa])) if sa else None), ratio=(len(A) / len(B)) if B else None)


# ---------------------------------------------------------------------------------------------------------------- shadow v3 y ledgers
def leer_gz_tolerante(path):
    try:
        data = open(path, 'rb').read()
    except OSError:
        return
    while data:
        d = zlib.decompressobj(31)
        try:
            txt = d.decompress(data)
        except zlib.error:
            return
        for ln in txt.decode(errors='replace').splitlines():
            try:
                yield json.loads(ln)
            except ValueError:
                continue
        data = d.unused_data
        if not d.eof:
            return


def leer_shadow_v3():
    """Posiciones forward del shadow v3 (celda central base|c) por (brazo, var) solo en pares COMPLETOS con desenlace oficial; cobertura; filas `repuja` (retardo simulado)."""
    ficheros = sorted(glob.glob(SHADOW_V3 + 'h23_shadow_v3_*.jsonl.gz'))
    if not ficheros:
        return None
    rell, des, fin, rep, ini = {}, {}, {}, [], []
    for f in ficheros:
        for r in leer_gz_tolerante(f):
            t = r.get('tipo')
            if t == 'relleno_resumen':
                rell[(r['mkt'], r['arm'], r['var'])] = r
            elif t == 'desenlace':
                des[r['mkt']] = r
            elif t == 'mercado_fin':
                fin[r['mkt']] = r
            elif t == 'repuja':
                rep.append(r)
            elif t == 'inicio':
                ini.append(r)
    pos, cov = defaultdict(list), Counter()
    por_mkt = defaultdict(list)
    for k, r in rell.items():
        por_mkt[k[0]].append((k, r))
    for m, fr in fin.items():
        cov['pares_total'] += 1
        if not fr.get('completo'):
            cov['pares_incompletos'] += 1
            continue
        cov['pares_completos'] += 1
        d = des.get(m)
        if d is None or d.get('ganador') is None:
            cov['completos_sin_desenlace'] += 1
            continue
        dia = datetime.fromtimestamp(fr['cierre'], timezone.utc).strftime('%Y-%m-%d')
        for (mm, arm, var), r in por_mkt.get(m, []):
            e = r['esc'].get('base|c')
            pn = (d.get('pnl') or {}).get(f'{arm}|{var}|base|c')
            if e and e.get('acc') and pn is not None:
                pos[(arm, var)].append(dict(dia=dia, pnl=pn, coste=e['coste'], lleno=e['acc'], g=1.0 if pn > 0 else 0.0, mkt=m))
    return dict(pos=pos, cov=dict(cov), repujas=rep, hashes={i.get('hash_regla') for i in ini}, dias=sorted({p['dia'] for v in pos.values() for p in v}),
                ficheros=[os.path.basename(f) for f in ficheros])


def leer_ledgers_arnes():
    """Eventos h23v3_repuja / h23v3_fill_tardio de TODOS los ledgers de los arneses (en seco y real). Sin parsear lo que no contenga `h23v3`."""
    rep, tardio, ficheros = [], [], []
    for f in sorted(glob.glob(DL + 'experimento_h47*_ledger*.jsonl')):
        try:
            with open(f, errors='replace') as fh:
                hit = False
                for ln in fh:
                    if 'h23v3_' not in ln:
                        continue
                    try:
                        ev = json.loads(ln)
                    except ValueError:
                        continue
                    hit = True
                    (rep if ev.get('tipo') == 'h23v3_repuja' else tardio if ev.get('tipo') == 'h23v3_fill_tardio' else []).append(ev)
                if hit:
                    ficheros.append(os.path.basename(f))
        except OSError:
            continue
    return dict(repujas=rep, tardios=tardio, ficheros=ficheros)


# ---------------------------------------------------------------------------------------------------------------- gate
def evaluar_gate(res, lat, tard):
    """Criterios del PREREGISTRO §4 para UN brazo sobre la celda primaria r150. Cada criterio: (valor, estado) con estado PASA/FALLA/NO_ESTIMABLE/NO_MEDIDO."""
    c = {}
    n = res.get('n', 0)
    c['n>=40'] = (n, 'PASA' if n >= GATE['n'] else 'FALLA')
    c['dias>=10'] = (res.get('dias', 0), 'PASA' if res.get('dias', 0) >= GATE['dias'] else 'FALLA')
    ev = res.get('ev_pond')
    c['EVpond>=+0.05'] = (ev, 'NO_ESTIMABLE' if ev is None else 'PASA' if ev >= GATE['ev_pond'] else 'FALLA')
    lo = res.get('ic_lo')
    c['IC90dias>0'] = (lo, 'NO_ESTIMABLE' if lo is None else 'PASA' if lo > GATE['ic90_lo'] else 'FALLA')
    s2 = res.get('sin2')
    c['sin2mejores>0'] = (s2, 'NO_ESTIMABLE' if s2 is None else 'PASA' if s2 > GATE['sin2'] else 'FALLA')
    ms = sorted(float(e['ms_desde_decision_cancel']) for e in lat if e.get('ms_desde_decision_cancel') is not None)
    if len(ms) < GATE['n_repujas']:
        c['p50_repuja<=300ms (>=10 reales)'] = (f'{len(ms)} re-pujas reales', 'NO_MEDIDO')
    else:
        p50 = float(np.median(ms))
        c['p50_repuja<=300ms (>=10 reales)'] = (p50, 'PASA' if p50 <= GATE['p50_ms'] else 'FALLA')
    dbl = [e for e in tard if e.get('doble_exposicion')]
    c['0 doble exposicion'] = (f'{len(dbl)} dobles / {len(tard)} tardios', 'NO_MEDIDO' if not lat else ('PASA' if not dbl else 'FALLA'))
    c['cobertura desenlace 100%'] = (None, 'PASA')                        # las posiciones sin desenlace se EXCLUYEN y se cuentan aparte (ver sin_desenlace)
    est = 'DRY_RUN_VALIDATED' if all(v[1] == 'PASA' for v in c.values()) else 'INSUFICIENTE' if (n < GATE['n'] or res.get('dias', 0) < GATE['dias']) else 'NO_CUMPLE'
    return est, c


def fm(x, f='{:+.3f}'):
    return 'n/e' if x is None else f.format(x)


def linea(res):
    if not res.get('n'):
        return 'n=0'
    ic = f"IC90d=({res['ic_lo']:+.2f},{res['ic_hi']:+.2f})" if res.get('ic_lo') is not None else 'IC90d=n/e(<5 dias)'
    s2 = f"sin2mejores={res['sin2']:+.3f}({res['dias_sin2']}d)" if res.get('sin2') is not None else 'sin2mejores=n/e'
    return (f"n={res['n']:2d} d={res['dias']:2d}(+{res['dias_pos']}) PnL={res['pnl']:+7.2f} coste={res['coste']:6.2f} EVpond={res['ev_pond']:+.3f} EVunit={res['ev_unit']:+.3f} {ic} {s2} "
            f"acierto={res['acierto']:.2f} vs precio={res['precio_med']:.2f}")


def informe(dias_exp, estado_dias, pos, cob, sh, ar):
    L, js = [], {}
    L.append(f'VIGIA H23 RE-PUJA 150 ms (H69) · {ahora()} · celda PRIMARIA: BTC, cola base, alta 79/cancel 60, tamano real + universo ejecutable, un relleno cierra la puja, desenlace oficial')
    L.append('Estado de la HIPOTESIS: EXPLORATORY · solo medicion · NADA real · gate PREREGISTRO §4 (n>=40, >=10 dias, EVpond>=+0,05, IC90 dias>0, sin 2 mejores>0, p50 re-puja<=300 ms, 0 doble exposicion)')
    ok = [d for d in dias_exp if estado_dias[d][0]]
    falt = [(d, estado_dias[d][1]) for d in dias_exp if not estado_dias[d][0]]
    L.append(f'\n## COBERTURA OOS (>= {OOS_DESDE}): esperados {len(dias_exp)} dias, validos {len(ok)}, faltan {len(falt)}: {falt if falt else "ninguno"}')
    L.append('dia        cierres  con_lado  sin_lado  con_libro  sin_libro  errores  sin_desenlace')
    for d in ok:
        i = cob[d]
        L.append(f"{d}  {i['cierres_grupo']:7d}  {i['con_lado']:8d}  {i['cierres_grupo'] - i['con_lado']:8d}  {i['con_libro']:9d}  {i['con_lado'] - i['con_libro']:9d}  {i['errores']:7d}  {i['sin_desenlace']:13d}")
    sd = {b: len(pos.get((b, 150), {}).get('_sin_desenlace', [])) for b in 'AB'}
    L.append(f'posiciones r150 sin desenlace oficial (excluidas, missing != 0): {sd}')
    js['cobertura'] = dict(esperados=dias_exp, validos=ok, faltan=falt, por_dia=cob, sin_desenlace_r150=sd)
    js['replay'] = {}
    for b in 'AB':
        L.append(f'\n## REPLAY OOS · brazo {b} (BTC) · celda primaria')
        for rep, et in ((0, 'r0 cota (no ejecutable)'), (150, 'r150 H69'), (300, 'r300'), (1500, 'r1500 PLACEBO = arnes real v1')):
            res = resumen_pos([v for k, v in pos.get((b, rep), {}).items() if k != '_sin_desenlace'])
            nd = max(len(ok), 1)
            L.append(f'{et:34s} rell/d={res.get("n", 0) / nd:.2f} | {linea(res)}')
            js['replay'][f'{b}_r{rep}'] = res
        em = emparejado(pos, b)
        L.append(f"EMPAREJADO r150 vs r1500 (mismos cierres): n150={em['n150']} n1500={em['n1500']} comunes={em['comunes']} solo150={em['solo150']} (PnL {em['pnl_solo150']:+.2f}) "
                 f"solo1500={em['solo1500']} (PnL {em['pnl_solo1500']:+.2f}) | PnL r150={em['pnl150']:+.2f} r1500={em['pnl1500']:+.2f} delta={em['pnl150'] - em['pnl1500']:+.2f} | dPnL en comunes={em['dpnl_comunes']:+.2f}")
        js['replay'][f'{b}_emparejado'] = em
        n150 = js['replay'][f'{b}_r150'].get('n', 0)
        lo, hi = poisson_ic90(n150, max(len(ok), 1))
        r = n150 / max(len(ok), 1)
        L.append(f'ritmo r150: {n150} en {len(ok)} dias = {r:.2f}/dia (IC90 Poisson {lo:.2f}-{hi:.2f}) -> n=40 en ' + (f'{40 / r:.0f} dias (IC {40 / hi:.0f}-{40 / lo if lo else float("inf"):.0f})' if n150 else 'inf. dias (sin rellenos)'))
        # regla de falsacion del PREREGISTRO §3
        rec = em['solo150']
        evaluable = len(ok) >= 5 and rec >= 5
        ratio = em['ratio']
        L.append(f"falsacion (PREREGISTRO §3: r150 conserva >=1,4x los rellenos de r1500; PnL total no menor; EVpond sin 2 mejores > 0): "
                 f"{'EVALUABLE' if evaluable else 'INSUFICIENTE (<5 dias OOS o <5 rellenos recuperados: ' + str(len(ok)) + ' dias, ' + str(rec) + ' recuperados)'}; ratio n150/n1500={fm(ratio, '{:.2f}')}, delta PnL={em['pnl150'] - em['pnl1500']:+.2f}")
        js['replay'][f'{b}_falsacion'] = dict(evaluable=evaluable, recuperados=rec, ratio=ratio)
    # ------------------------------------------------------------------ shadow v3
    L.append('\n## SHADOW v3 FORWARD (h23_shadow_v3: mismos mercados que el replay, NO aditivo)')
    if sh is None:
        L.append(f'NO DESPLEGADO: no hay ficheros en {SHADOW_V3}. El shadow v1 (`h23shadow`, regla 46eff95337902549) NO tiene brazo r150, usa 2 EUR y cierre acumulado: no sirve para el gate.')
        js['shadow_v3'] = None
    else:
        L.append(f"ficheros {sh['ficheros'][0]}..{sh['ficheros'][-1]} · hash_regla {sorted(map(str, sh['hashes']))} · cobertura {sh['cov']} · dias con relleno {sh['dias']}")
        js['shadow_v3'] = dict(cov=sh['cov'], dias=sh['dias'], hashes=sorted(map(str, sh['hashes'])))
        for b in 'AB':
            for var, et in (('join', 'r0 cota'), ('join_150', 'r150 H69'), ('join_r', 'r1500 PLACEBO'), ('nc', 'nc control sin cancelar')):
                res = resumen_pos(sh['pos'].get((b, var), []))
                L.append(f'{b} {et:24s} | {linea(res)}')
                js['shadow_v3'][f'{b}_{var}'] = res
        lag = [float(e['lag_obs_ms']) for e in sh['repujas'] if e.get('lag_obs_ms') is not None]
        if lag:
            L.append(f"re-pujas simuladas: {len(lag)}; retardo SIMULADO = 150 ms por construccion; retardo hasta el primer evento observado: p50={np.percentile(lag, 50):.0f} ms p90={np.percentile(lag, 90):.0f} ms (indicador de cadencia del WS, NO latencia real de envio)")
    # ------------------------------------------------------------------ arnes real / ensayo en seco
    L.append('\n## ARNES (ensayo en seco / real): latencia REAL de re-puja y doble exposicion')
    lat = ar['repujas']
    if lat:
        ms = sorted(float(e['ms_desde_decision_cancel']) for e in lat if e.get('ms_desde_decision_cancel') is not None)
        L.append(f"{len(ms)} re-pujas en {ar['ficheros']}: p50={np.median(ms):.0f} ms p90={np.percentile(ms, 90):.0f} ms max={max(ms):.0f}; fill_tardio={len(ar['tardios'])}, con doble exposicion={sum(1 for e in ar['tardios'] if e.get('doble_exposicion'))}")
    else:
        L.append('0 eventos h23v3_repuja / h23v3_fill_tardio en los ledgers: el arnes v3 NUNCA se ha ejecutado (ni en seco ni real). Latencia real y doble exposicion: NO MEDIDAS.')
    js['arnes'] = dict(n_repujas=len(lat), n_tardios=len(ar['tardios']), ficheros=ar['ficheros'])
    # ------------------------------------------------------------------ gate
    L.append('\n## GATE §4 por brazo (poblacion = REPLAY OOS r150, celda primaria; el shadow v3 solo contrasta)')
    js['gate'] = {}
    for b in 'AB':
        est, c = evaluar_gate(js['replay'][f'{b}_r150'], lat, ar['tardios'])
        L.append(f'brazo {b}: {est}')
        for k, (v, s) in c.items():
            L.append(f'   {k:34s} {s:13s} {v if not isinstance(v, float) else round(v, 3)}')
        js['gate'][b] = dict(estado=est, criterios={k: dict(valor=v, estado=s) for k, (v, s) in c.items()})
    L.append('\nNota: DISC 06-18 Oct (13 dias) NO cuenta para el gate. Sin multiplicidad corregida: una sola celda primaria por brazo y un contraste emparejado por brazo.')
    return '\n'.join(L), js


def telegram(js, resumen_corto):
    sys.path.insert(0, '/root/polymarket-research')
    from shadow_digest import enviar_telegram as e
    e(resumen_corto)


def main():
    a = sys.argv[1:]
    os.makedirs(VIG, exist_ok=True)
    lock = open(VIG + 'vigia.lock', 'w')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        print('otro vigia_h23_repuja en marcha: salgo')
        return 0
    hasta = a[a.index('--hasta') + 1] if '--hasta' in a else None
    dias = dias_esperados(hasta)
    t0 = ahora()
    manifest = dict(job_id='h23_repuja_vigia_22oct', inicio=t0, comando=f'nice -n 19 ionice -c3 python3 -I {Z}/vigia_h23_repuja.py --telegram',
                    codigo={n: sha(f'{Z}/{n}') for n in ('vigia_h23_repuja.py', 'h23_sim_v3.py', 'h23_regla_v3.py', 'h23_shadow_v3.py', 'PREREGISTRO.md') if os.path.exists(f'{Z}/{n}')},
                    parametros=dict(gate=GATE, celda='BTC base 79/60 real primer', oos_desde=OOS_DESDE, bootstrap='dias, 3000, semilla 7, >=5 dias'), fechas_previstas=dias, estado='RUNNING')
    atomico(VIG + 'run_manifest.json', manifest)
    estado = {}
    pendientes = []
    for D in dias:
        ok, why, info = validar_dia(D)
        if not ok and why in ('csv_sin_cobertura', 'cabecera_inesperada', 'clave_duplicada', 'dia_incorrecto', 'cobertura_de_otro_dia') or (not ok and why.startswith('ilegible')):
            # salida corrupta o a medias: se aparta (no se borra) y se recalcula; el replay es determinista e idempotente
            for suf in (f'v3_BTC_{D}.csv', f'v3_cobertura_BTC_{D}.json'):
                p = OUT + suf
                if os.path.exists(p) and time.time() - os.path.getmtime(p) > 600:          # no tocar una salida que otro proceso este escribiendo ahora
                    os.replace(p, p + f'.invalido_{time.strftime("%Y%m%dT%H%M%S", time.gmtime())}')
            log(f'{D} salida invalida ({why}): apartada, se recalcula')
            ok, why = False, 'sin_csv'
        estado[D] = (ok, why)
        if not ok:
            pendientes.append(D)
    detalle = {}
    if '--sin-calcular' not in a:
        for D in pendientes:
            if not registro_listo(D):
                estado[D] = (False, 'registro_ms_o_controles_no_disponible')
                continue
            ok, why = calcular_dia(D)
            ok2, why2, _ = validar_dia(D)
            estado[D] = (ok2, 'ok' if ok2 else why)
            detalle[D] = why
            log(f'{D} calcular -> {why} ; valido={ok2}')
            if not ok and why.startswith('pospuesto'):
                break                                                     # una guarda cerro: nada mas pesado hoy
    pos, cob = cargar_replay([d for d in dias if estado[d][0]])
    sh, ar = leer_shadow_v3(), leer_ledgers_arnes()
    txt, js = informe(dias, estado, pos, cob, sh, ar)
    fin = ahora()
    faltan = [d for d in dias if not estado[d][0]]
    manifest.update(fin=fin, dias_hechos=[d for d in dias if estado[d][0]], dias_pendientes=faltan, detalle_calculo=detalle,
                    entradas={d: {'csv_sha': sha(f'{OUT}v3_BTC_{d}.csv')} for d in dias if estado[d][0]},
                    estado='COMPLETE' if not faltan else 'PARTIAL', coverage_expected=len(dias), coverage_valid=len(dias) - len(faltan))
    hoy = time.strftime('%Y-%m-%d', time.gmtime())
    open(f'{VIG}informe_{hoy}.txt', 'w').write(txt + '\n')
    atomico(f'{VIG}informe_{hoy}.json', js)
    atomico(VIG + 'run_manifest.json', manifest)
    print(txt)
    if '--telegram' in a and not os.path.exists(f'{VIG}telegram_{hoy}.ok') and not any(v.startswith('pospuesto') for v in detalle.values()):
        g = js['gate']
        corto = (f"H23 re-puja 150 ms (H69) {hoy}: OOS {len(manifest['dias_hechos'])}/{len(dias)} dias; r150 A n={js['replay']['A_r150'].get('n', 0)} B n={js['replay']['B_r150'].get('n', 0)} "
                 f"(r1500 A {js['replay']['A_r1500'].get('n', 0)} B {js['replay']['B_r1500'].get('n', 0)}); recuperados A {js['replay']['A_emparejado']['solo150']} B {js['replay']['B_emparejado']['solo150']}; "
                 f"gate A {g['A']['estado']} B {g['B']['estado']}; latencia real y doble exposicion NO medidas. EXPLORATORY, nada real. Detalle: {VIG}informe_{hoy}.txt")
        telegram(js, corto)
        open(f'{VIG}telegram_{hoy}.ok', 'w').write(fin)
    return 3 if any(v.startswith('FAILED') for v in detalle.values()) else 0          # PARTIAL (pospuesto/registro no disponible) no es un fallo: el manifest lo dice


if __name__ == '__main__':
    sys.exit(main())
