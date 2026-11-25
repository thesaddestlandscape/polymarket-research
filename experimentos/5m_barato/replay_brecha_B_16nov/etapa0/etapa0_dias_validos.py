#!/usr/bin/env python3
"""etapa0_dias_validos.py -- Etapa 0 del PREREG_REPLAY_BRECHA_B_16nov + ADDENDUM1 (B-1, B-3). SOLO LECTURA.
No importa el motor, no lee ms2, no calcula ni imprime pnl/EV/rellenos (de SEGT solo se usan act, fin y dia).
HOLD 10-14 Nov: no se abre nada salvo la columna recv de libro5_tx del 10-Nov, filas con recv del 09-Nov (ADDENDUM1 B-1.4).
Uso: nice -n 19 ionice -c3 /usr/bin/python3 -I etapa0_dias_validos.py   (ulimit -v 3000000)
Escribe en este directorio: dias_validos_E0.json y tabla_dias_E0.tsv (el .sha256 se escribe fuera con sha256sum)."""
import os, json, glob, hashlib, time, resource, collections, datetime as dt
import numpy as np, pandas as pd

H = os.path.dirname(os.path.abspath(__file__)) + '/'
R = '/root/polymarket-research/'
L2 = R + 'experimentos/5m_barato/l2_carrera_10nov/'
MIS = R + 'misiones/5m_barato/alpha_miner_B_F5_15nov/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'
DL = '/root/polymarket-research-datalogs/'
TXD = '/mnt/HC_Volume_106538179/libro5_tx/'
HF = L2 + 'calma_v3/huecos_fix_13nov/out/'
DIAS = [d.strftime('%Y-%m-%d') for d in pd.date_range('2026-10-26', '2026-11-09')]
PRIM = DIAS[2:]                                   # 28-Oct..09-Nov (13)
COINS = ('ETH', 'SOL', 'XRP')
HOLD = ['2026-11-%02d' % i for i in range(10, 32)] + ['2026-12']   # 10-14 Nov HOLD y >= 15-Nov (forward CXB)
APA = {  # Apendice A del prereg: sha256 (16 hex) de CX_v3dd y SEGT_v3dd
    '2026-10-26': ('7a85cdb5c689a5c9', 'bcb2928495edc0cc'), '2026-10-27': ('774ca0666ecf997d', 'b96caee382a3de27'),
    '2026-10-28': ('a66d1ecc375352ef', 'a3fff3eef8dab3df'), '2026-10-29': ('0e14cb1b04b5df48', '1968741ddce2dfc8'),
    '2026-10-30': ('4e500ec40d4c6a90', 'cfde4f68146b1b9c'), '2026-10-31': ('007af78af73b1cfc', 'b652829447d938d1'),
    '2026-11-01': ('0d6a2a447ae854e6', 'a70a05c5ddee6af2'), '2026-11-02': ('74c9e95e028127ff', '90a12182d397cfcd'),
    '2026-11-03': ('4e1cb1d338f4ae1d', 'c6b9b4e0a0298312'), '2026-11-04': ('b1b57697e5d0c2d7', 'b7afc381c2c17572'),
    '2026-11-05': ('5cc7b4af954aac9a', '4a791df788fa5942'), '2026-11-06': ('9657382cea87ec34', '4b7e4301bf919bc7'),
    '2026-11-07': ('0b396e0de768257a', '78dace8a127e7937'), '2026-11-08': ('aa8ae756db1686d6', 'f2a64e67a1a429cb'),
    '2026-11-09': ('67b436c7c478946e', 'a66323ad6287cccb')}


def guard(path, recv_only=False):
    b = os.path.basename(path)
    if any(h in b for h in HOLD):
        assert recv_only and b.startswith('libro5_tx_2026-11-10_'), ('HOLD/forward: prohibido abrir', path)
    return path


def sha16(p):
    h = hashlib.sha256()
    with open(guard(p), 'rb') as f:
        for ch in iter(lambda: f.read(1 << 20), b''): h.update(ch)
    return h.hexdigest()[:16]


def e0(d): return int(pd.Timestamp(d, tz='UTC').timestamp())
def dsh(d, n): return (pd.Timestamp(d) + pd.Timedelta(days=n)).strftime('%Y-%m-%d')
def fins(d): return [e0(d) + 4 * 3600 + 300 * (i + 1) for i in range(240)]          # cierres 04:05..24:00Z (s)
def hkey(ts): t = dt.datetime.fromtimestamp(ts, dt.timezone.utc); return (t.strftime('%Y-%m-%d'), t.hour)


def clase_p5(v):
    if v is None or not np.isfinite(v): return 'indet'
    if abs(v - 19.25) <= 5: return 'lo'
    if abs(v - 39.5) <= 5: return 'hi'
    return 'indet'


# ---------------------------------------------------------------- hole60: recv unicos de libro5_tx (D-1, D, D+1), una lectura por fecha
def leer_rx(f, objetivos, contrib, ficheros):
    """Lee la columna recv de todos los libro5_tx_<f>_*.csv.gz y reparte los recv por dia objetivo (solo [d0, d1) de cada objetivo)."""
    rng = {t: (e0(t) * 1000, (e0(t) + 86400) * 1000) for t in objetivos}
    for p in sorted(glob.glob(TXD + f'libro5_tx_{f}_*.csv.gz')):
        guard(p, recv_only=True); st = os.stat(p); ficheros.append(dict(f=os.path.basename(p), bytes=st.st_size, mtime=int(st.st_mtime)))
        for c in pd.read_csv(p, header=None, names=['t_ev', 'token', 'tx', 'recv'], usecols=['recv'], on_bad_lines='skip', chunksize=2_000_000):
            v = pd.to_numeric(c['recv'], errors='coerce').to_numpy(dtype='float64'); v = v[np.isfinite(v)].astype(np.int64)
            for t, (a, b) in rng.items():
                m = (v >= a) & (v < b)
                if m.any(): contrib[t].append(np.unique(v[m]))


def huecos(d, arrs):
    d0 = e0(d) * 1000
    rx = np.unique(np.concatenate(arrs)) if arrs else np.array([], dtype=np.int64)
    e = np.concatenate([[d0], rx, [d0 + 86400000]]); g = np.diff(e); ix = np.where(g > 60000)[0]
    return [(int(e[i]), int(e[i + 1])) for i in ix], int(len(rx))


def main():
    t_ini = time.time(); out = dict(job='etapa0_dias_validos', prereg_sha256=open(MIS + 'PREREG_REPLAY_BRECHA_B_16nov.sha256').read().split()[0],
                                     addendum1_sha256=open(MIS + 'ADDENDUM1_PREREG_REPLAY_BRECHA_B_16nov.sha256').read().split()[0],
                                     codigo_sha256=hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(), inicio_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    # hole60 primero (lectura secuencial 25-Oct..10-Nov; el 10-Nov solo recv con recv del 09-Nov)
    contrib = collections.defaultdict(list); ficheros = []; H60 = {}
    fechas = [dsh(DIAS[0], -1)] + DIAS + [dsh(DIAS[-1], 1)]
    for f in fechas:
        objetivos = [t for t in (dsh(f, -1), f, dsh(f, 1)) if t in DIAS]
        leer_rx(f, objetivos, contrib, ficheros)
        t = dsh(f, -1)
        if t in DIAS: H60[t] = huecos(t, contrib.pop(t, []))
    out['libro5_tx_leidos'] = ficheros
    filas = []; dias = {}
    for d in DIAS:
        bad = {tuple(x) for x in json.load(open(guard(P2 + f'bad_{d}.json')))['bad']}
        F = fins(d); okp = [f for f in F if not (hkey(f - 300) in bad or hkey(f) in bad)]   # engine.sane: horas de t0 y de fin
        holes, n_rx = H60[d]; exc = [(a - 60000, b + 60000) for a, b in holes]
        okh = [f for f in F if not any((f - 300) * 1000 < hb and f * 1000 > ha for ha, hb in exc)]
        # gmap D-1, D, D+1 (sin HOLD)
        GM = {}; conf = 0; gfiles = []
        for g in (dsh(d, -1), d, dsh(d, 1)):
            p = DL + f'sa_r1/gmap_{g}.json'
            if any(h in os.path.basename(p) for h in HOLD) or not os.path.exists(p): continue
            gfiles.append((os.path.basename(p), sha16(p)))
            for s, v in json.load(open(guard(p))).items():
                des = v.get('des')
                if s in GM and GM[s] in ('YES', 'NO') and des in ('YES', 'NO') and GM[s] != des: conf += 1
                if des in ('YES', 'NO') or s not in GM: GM[s] = des
        def cov(lista):
            r = {}
            for m in COINS:
                n = len(lista); c = sum(1 for f in lista if GM.get(f'{m.lower()}-updown-5m-{f - 300}') in ('YES', 'NO'))
                r[m] = (n, c)
            n = sum(v[0] for v in r.values()); c = sum(v[1] for v in r.values())
            return r, (c / n if n else None), n - c
        covp, cp, faltp = cov(okp); covh, ch, falth = cov(okh)
        # SEGT subset N_ok (solo act, fin, dia)
        sp = L2 + f'out_v3/SEGT_v3dd_{d}.pkl'; cp_ = L2 + f'out_v3/CX_v3dd_{d}.pkl'
        s = pd.read_pickle(guard(sp))[['dia', 'act', 'fin']]; dia_ok = bool((s['dia'] == d).all())
        mk = set(zip(s['act'].astype(str), s['fin'].astype(np.int64))); del s
        okset = set(okp); viol = sorted((a, int(f)) for a, f in mk if a not in COINS or f not in okset)
        sha_cx, sha_sg = sha16(cp_), sha16(sp)
        # clase (ADD3, solo lectura de ficheros COMPLETE)
        pa = MIS + f'exp1/cache/pob_add3_{d}.json'; cl = dict(estado='PENDIENTE_ADD3')
        if os.path.exists(pa):
            j = json.load(open(guard(pa)))
            if j.get('estado') == 'COMPLETE':
                pf = j['C3_suelo_rx_menos_ex']['perfil_p5_10min']; lab = [clase_p5(None if v is None else float(v)) for v in pf]
                gob = collections.Counter(lab[23:143]); tot = collections.Counter(lab)
                vpc = j['C3_suelo_rx_menos_ex'].get('ventanas_por_clase', {})
                cl = dict(estado='COMPLETE', n_ventanas=len(pf), gob_lo=gob['lo'], gob_hi=gob['hi'], gob_indet=gob['indet'],
                          lo_puro=bool(gob['hi'] == 0 and gob['indet'] <= 6), indet_gt20=bool(gob['indet'] > 24),
                          cuenta_G_INT=bool(gob['indet'] <= 24 and gob['lo'] >= 60),
                          reproduce_ventanas_por_clase_144=bool(all(tot[k] == vpc.get(k, 0) for k in ('lo', 'hi', 'indet'))))
            else: cl = dict(estado='ADD3_' + str(j.get('estado')))
        frac_p = len(okp) * 3 / 720; frac_h = len(okh) * 3 / 720
        if viol: est_p = 'PENDIENTE_SEGT'
        else: est_p = 'VALIDO' if (frac_p >= 0.5 and cp is not None and cp >= 0.995) else 'NO_VALIDO'
        est_h = 'VALIDO' if (frac_h >= 0.5 and ch is not None and ch >= 0.995) else 'NO_VALIDO'
        horas_malas = sorted(h for dd, h in bad if dd == d)
        dias[d] = dict(primario=d in PRIM, horas_malas=horas_malas, N_cal_por_moneda=240,
                       primaria=dict(N_ok_por_moneda=len(okp), retenido=round(frac_p, 4), cov_des=cp, sin_desenlace=faltp, cov_por_moneda={m: covp[m] for m in COINS}, estado=est_p),
                       hole60=dict(n_huecos=len(holes), huecos=holes, recv_unicos=n_rx, N_ok_por_moneda=len(okh), retenido=round(frac_h, 4), cov_des=ch, sin_desenlace=falth, cov_por_moneda={m: covh[m] for m in COINS}, estado=est_h),
                       segt=dict(mercados=len(mk), fuera_de_N_ok=len(viol), ejemplos=viol[:5], dia_ok=dia_ok),
                       sha16=dict(CX=sha_cx, SEGT=sha_sg, CX_ok=sha_cx == APA[d][0], SEGT_ok=sha_sg == APA[d][1], bad=sha16(P2 + f'bad_{d}.json'), gmap=gfiles, gmap_conflictos=conf),
                       clase=cl)
        filas.append([d, 'P' if d in PRIM else '-', ','.join(map(str, horas_malas)) or '-', len(okp), f'{frac_p:.3f}', f'{cp:.4f}' if cp is not None else 'NA', est_p,
                      len(holes), len(okh), f'{frac_h:.3f}', f'{ch:.4f}' if ch is not None else 'NA', est_h, len(viol), cl.get('estado'),
                      '%s/%s/%s' % (cl.get('gob_lo', '-'), cl.get('gob_hi', '-'), cl.get('gob_indet', '-'))])
    # control cruzado hole60 vs meta2 (02..09-Nov)
    x = {}
    for d in DIAS:
        p = HF + f'meta2_{d}.json'
        if os.path.exists(p): m2 = [tuple(h) for h in json.load(open(guard(p)))['holes']]; x[d] = dict(igual=m2 == dias[d]['hole60']['huecos'], n_meta2=len(m2), n_recalc=len(dias[d]['hole60']['huecos']))
    vp = [d for d in PRIM if dias[d]['primaria']['estado'] == 'VALIDO']; vh = [d for d in PRIM if dias[d]['hole60']['estado'] == 'VALIDO']
    pend_cl = [d for d in vp if dias[d]['clase']['estado'] != 'COMPLETE']; lo_cnt = [d for d in vp if dias[d]['clase'].get('cuenta_G_INT')]
    out.update(dias=dias, control_hole60_vs_meta2=x,
               dias_validos_primaria=vp, dias_validos_hole60=vh,
               dias_26_27_oct=dict((d, dict(primaria=dias[d]['primaria']['estado'], hole60=dias[d]['hole60']['estado'])) for d in DIAS[:2]),
               puerta_etapa0=dict(n_validos_primarios=len(vp), umbral=10, dias=('PASA' if len(vp) >= 10 else 'NO_PASA'),
                                  clase=('PENDIENTE_ADD3: ' + ','.join(pend_cl)) if pend_cl else ('PASA' if len(lo_cnt) >= 10 else 'NO_PASA'),
                                  dias_LO_que_cuentan_G_INT=lo_cnt, sha_entradas_ok=all(dias[d]['sha16']['CX_ok'] and dias[d]['sha16']['SEGT_ok'] for d in DIAS),
                                  identidades_y_paridad_lectura='NO EJECUTADAS (van despues de fijar esta lista; ADDENDUM1 B-1.2)'),
               recursos=dict(cpu_s=round(time.process_time(), 1), pared_s=round(time.time() - t_ini, 1), maxrss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1)),
               fin_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    tmp = H + 'dias_validos_E0.json.tmp'; json.dump(out, open(tmp, 'w'), indent=1, default=str); os.replace(tmp, H + 'dias_validos_E0.json')
    cab = ['dia', 'prim', 'horas_malas', 'N_ok_mon', 'ret', 'cov_des', 'estado', 'h60_huecos', 'h60_N_ok_mon', 'h60_ret', 'h60_cov', 'h60_estado', 'segt_fuera', 'clase', 'gob_lo/hi/indet']
    with open(H + 'tabla_dias_E0.tsv.tmp', 'w') as g: g.write('\t'.join(cab) + '\n' + '\n'.join('\t'.join(map(str, r)) for r in filas) + '\n')
    os.replace(H + 'tabla_dias_E0.tsv.tmp', H + 'tabla_dias_E0.tsv')
    print(json.dumps(dict(validos_primaria=vp, validos_hole60=vh, puerta=out['puerta_etapa0'], control_meta2={d: v['igual'] for d, v in x.items()}, recursos=out['recursos']), default=str))


if __name__ == '__main__':
    main()
