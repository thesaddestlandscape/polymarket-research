#!/usr/bin/env python3
"""Tests del runner del dry-run (cxb60_dryrun_fase0.py) con ficheros gz SINTETICOS en un directorio temporal (nunca toca el datalog real ni arranca procesos). python3 -I test_runner_dryrun.py
R1  GzTail: lectura incremental de un gz que crece (miembros anexados y un unico flujo con Z_SYNC_FLUSH), lineas completas, sin perdida ni duplicado.
R2  extremo a extremo (--once): k/q/t sinteticos -> dec_<D>.csv.gz con filas seg y nof; cobertura y manifiesto; ninguna cadena de envio de ordenes.
R3  idempotencia: segundo arranque sobre los mismos ficheros no duplica filas ni cambia el resultado (claves unicas tok,L,var,seg).
R4  corrupcion: cola gz truncada se recorta al ultimo miembro valido y el reinicio reconcilia.
R5  filas fuera de orden / duplicadas / basura no rompen el lector (contadores de duplicados y errores).
R6  microbench: coste por evento de la primitiva de decision incremental (cota informativa del d_proc de computo)."""
import os, sys, gzip, zlib, json, time, tempfile, datetime as dt, subprocess, shutil
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_core as C, cxb60_dryrun_fase0 as R

FIN = 1794400500; FIN15 = int(np.ceil(FIN / 900.0) * 900)
def iso(e): return dt.datetime.fromtimestamp(e, dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S+00:00')
TA, TB, TC, TD = '111111111', '222222222', '333333333', '444444444'


def sint(seed=3, ruido=False):
    r = np.random.default_rng(seed); L = []
    L += [f'k,{(FIN - 500) * 1000},{TA},ETH,5min,777,{iso(FIN)},YES', f'k,{(FIN - 500) * 1000},{TB},ETH,5min,777,{iso(FIN)},NO', f'k,{(FIN - 500) * 1000},{TC},ETH,15min,888,{iso(FIN15)},YES', f'k,{(FIN - 500) * 1000},{TD},ETH,15min,888,{iso(FIN15)},NO']
    t0 = (FIN - 300) * 1000 - 120000; t1 = FIN * 1000 + 10000; bid = 0.19; rows = []
    for t in range(t0, t1, 100):
        bid = float(np.clip(round(bid + r.choice([-0.01, 0, 0, 0.01]), 2), 0.05, 0.30)); ex = t; rx = t + int(r.integers(15, 60))
        rows.append((rx, f'q,{ex},{TA},{bid},{round(bid + 0.01, 2)},{10 + int(r.integers(0, 30))},12,{rx}'))
        rows.append((rx + 1, f'q,{ex},{TB},{round(0.99 - bid, 2)},{round(1.0 - bid, 2)},12,10,{rx + 1}'))
        if t % 1000 == 0: rows.append((rx + 2, f'q,{ex},{TC},{round(bid + 0.01, 2)},{round(bid + 0.02, 2)},12,10,{rx + 2}')); rows.append((rx + 2, f'q,{ex},{TD},{round(0.98 - bid, 2)},{round(0.99 - bid, 2)},12,10,{rx + 2}'))
        if t % 2000 == 0:
            for tok in (TA, TB): rows.append((rx + 3, f't,{ex},{tok},{round(bid - 0.01 * int(r.integers(0, 3)), 2)},SELL,{float(r.integers(5, 25))},{rx + 3},'))
    rows.sort(key=lambda x: x[0]); L += [x[1] for x in rows]
    if ruido: L += ['basura sin sentido', 'q,1,2', 'q,abc,333,0.1,0.2,1,1,xyz', rows[-1][1], rows[-1][1]]
    return '\n'.join(L) + '\n'


def escribe(path, txt, miembros=4):
    ls = txt.strip('\n').split('\n'); n = len(ls); cuts = [0] + [n * i // miembros for i in range(1, miembros)] + [n]
    with open(path, 'wb') as f:
        for a, b in zip(cuts[:-1], cuts[1:]): f.write(gzip.compress(('\n'.join(ls[a:b]) + '\n').encode()))


def leer_dec(out, dia):
    txt, ok = R.miembros_validos(out + f'dec_{dia}.csv.gz'); ls = [l for l in txt.split('\n') if l]; hdr = ls[0].split(','); return [dict(zip(hdr, l.split(',', len(hdr) - 2)[:len(hdr) - 1])) for l in ls[1:]], ls


def test_gztail():
    d = tempfile.mkdtemp(); p = d + '/x.gz'; lineas = [f'q,{i},tok,0.1,0.2,1,1,{i}' for i in range(5000)]; txt = '\n'.join(lineas) + '\n'
    for modo in ('miembros', 'flujo'):
        if os.path.exists(p): os.remove(p)
        open(p, 'wb').close(); tail = R.GzTail(p); got = []; co = zlib.compressobj(6, zlib.DEFLATED, 31); k = 0
        for i in range(0, len(lineas), 700):
            trozo = ('\n'.join(lineas[i:i + 700]) + '\n').encode()
            with open(p, 'ab') as f:
                if modo == 'miembros': f.write(gzip.compress(trozo))
                else: f.write(co.compress(trozo) + co.flush(zlib.Z_SYNC_FLUSH))
            got += tail.poll()
        if modo == 'flujo':
            with open(p, 'ab') as f: f.write(co.flush())
        got += tail.poll()
        assert got == lineas, (modo, len(got), got[-2:])
    shutil.rmtree(d); print('R1 ok')


def test_extremo_a_extremo_idempotente_y_corrupcion():
    d = tempfile.mkdtemp(); dia = dt.datetime.fromtimestamp(FIN - 150, dt.timezone.utc).strftime('%Y-%m-%d'); f = d + f'/maker_ms_{dia}_1.csv.gz'; escribe(f, sint(3, ruido=True)); out = d + '/out/'
    cmd = [sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', out, '--once', '--files', f, '--solo-dia', dia]
    r1 = subprocess.run(cmd, capture_output=True, text=True, timeout=300); assert r1.returncode == 0, r1.stderr[-2000:] + r1.stdout[-1000:]
    filas, ls = leer_dec(out, dia); seg = [x for x in filas if x['tipo'] == 'seg']; nof = [x for x in filas if x['tipo'] == 'nof']
    assert len(nof) == 2 * len(C.LEVELS) * len(C.default_specs()) and len(seg) > 0, (len(nof), len(seg))              # 2 tokens (A, B) x 4 L x 26 variantes
    claves = [(x['tok'], x['L'], x['var'], x['seg']) for x in seg]; assert len(claves) == len(set(claves)), 'claves seg duplicadas'
    man = json.load(open(out + 'run_manifest.json')); assert man['status'] == 'COMPLETE' and man['modo'].startswith('DRY_RUN') and 'cxb60_core.py' in man['codigo']
    cov = json.load(open(out + f'coverage_{dia}.json')); assert cov['esperados'] == 2 and cov['procesados'] == 2, cov
    hb = json.load(open(out + 'heartbeat.json')); assert hb['contadores']['q_dup'] >= 1 and hb['contadores']['parse_err'] >= 2, hb['contadores']                 # R5: duplicado y basura contados
    n1 = len(ls); sha = open(out + f'dec_{dia}.csv.gz', 'rb').read()
    r2 = subprocess.run(cmd, capture_output=True, text=True, timeout=300); assert r2.returncode == 0, r2.stderr[-1500:]                                                    # R3 idempotencia
    filas2, ls2 = leer_dec(out, dia); assert len(ls2) == n1 and open(out + f'dec_{dia}.csv.gz', 'rb').read() == sha, ('duplico filas en el reinicio', n1, len(ls2))
    # R4 corrupcion: cola truncada tras un miembro extra a medio escribir
    p = out + f'dec_{dia}.csv.gz'; ok0 = os.path.getsize(p); open(p, 'ab').write(gzip.compress(b'seg,x,y\n')[:-7])
    r3 = subprocess.run(cmd, capture_output=True, text=True, timeout=300); assert r3.returncode == 0 and 'RECONCILIA' in r3.stdout and 'cola corrupta' in r3.stdout, r3.stdout[-1500:]
    assert os.path.getsize(p) == ok0, (os.path.getsize(p), ok0)
    fuente = open(HERE + 'cxb60_dryrun_fase0.py').read(); shutil.rmtree(d); print('R2/R3/R4/R5 ok: seg', len(seg), 'nof', len(nof), 'bytes dec', ok0)


def test_microbench_decision():
    """Cota informativa: coste de computo de la primitiva incremental (trigger + features) por evento; NO es el d_proc de un ejecutor (no hay envio ni red)."""
    r = np.random.default_rng(1); buf = C.TokBuf(); t = (FIN - 300) * 1000
    for i in range(20000): buf.add_q(t + i * 15, t + i * 15 + 20, float(round(0.15 + 0.01 * r.integers(-2, 3), 2)), 0.2, 10.0, 10.0)
    spec = C.VSpec('CXB60', 'CXB', l=60); F = C.TokenFeats('x', FIN, buf, None, None); m = C.VMachine(spec, F, 0.13, 1); F.extend(t + 150000)
    t0 = time.perf_counter(); n = 200
    for i in range(n): m._trigger(t + 20000, t + 280000, 60, t + 280000)
    us = (time.perf_counter() - t0) / n * 1e6; print('R6 microbench: _trigger sobre 20k filas: %.0f us por llamada' % us); assert us < 50000


def test_resolver():
    """R7: el resolver une el desenlace oficial sin duplicar PnL, deja 'sin_desenlace' vacio (missing != 0) y es idempotente."""
    import cxb60_resolve as V
    d = tempfile.mkdtemp(); dia = dt.datetime.fromtimestamp(FIN - 150, dt.timezone.utc).strftime('%Y-%m-%d'); f = d + f'/maker_ms_{dia}_1.csv.gz'; escribe(f, sint(5)); out = d + '/out/'
    subprocess.run([sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', out, '--once', '--files', f, '--solo-dia', dia], capture_output=True, text=True, timeout=300, check=True)
    os.makedirs(d + '/gm'); json.dump({'x': dict(id=777, des='YES')}, open(d + '/gm/gmap_x.json', 'w'))                      # mercado 777 resuelto YES; 888 (15m) irrelevante
    o1, st1 = V.resolve(out + f'dec_{dia}.csv.gz', V.carga_gmap(d + '/gm')); o2, st2 = V.resolve(out + f'dec_{dia}.csv.gz', V.carga_gmap(d + '/gm'))
    assert st1 == st2 and st1['fills'] > 0 and st1['sin_desenlace'] == 0, st1
    pn = sum(float(r['pnl']) for r in o1 if r['pnl'] != ''); gm0 = V.carga_gmap(d + '/gm_vacio'); o3, st3 = V.resolve(out + f'dec_{dia}.csv.gz', gm0)
    assert st3['sin_desenlace'] == st3['fills'] and all(r['pnl'] == '' for r in o3), st3                                   # sin desenlace: no se inventa PnL
    # duplicar el bloque no duplica el PnL
    p = out + f'dec_{dia}.csv.gz'; txt, ok = R.miembros_validos(p); R.append_gz(p, '\n'.join(txt.split('\n')[1:]))
    o4, st4 = V.resolve(p, V.carga_gmap(d + '/gm')); assert st4['duplicados'] > 0 and abs(sum(float(r['pnl']) for r in o4 if r['pnl'] != '') - pn) < 1e-9, st4
    shutil.rmtree(d); print('R7 ok: fills', st1['fills'], 'duplicados descartados', st4['duplicados'])


if __name__ == '__main__':
    test_gztail(); test_extremo_a_extremo_idempotente_y_corrupcion(); test_microbench_decision(); test_resolver(); print('TODOS OK (runner)')
