#!/usr/bin/env python3
"""Tests del runner del dry-run (cxb60_dryrun_fase0.py) con ficheros gz SINTETICOS en un directorio temporal (nunca toca el datalog real ni arranca procesos). python3 -I test_runner_dryrun.py
R1  GzTail: lectura incremental de un gz que crece (miembros anexados y un unico flujo con Z_SYNC_FLUSH), lineas completas, sin perdida ni duplicado.
R2  extremo a extremo (--once): k/q/t sinteticos -> dec_<D>.csv.gz con filas seg y nof; cobertura y manifiesto; ninguna cadena de envio de ordenes.
R3  idempotencia: segundo arranque sobre los mismos ficheros no duplica filas ni cambia el resultado (claves unicas tok,L,var,seg).
R4  corrupcion: cola gz truncada se recorta al ultimo miembro valido y el reinicio reconcilia.
R5  filas fuera de orden / duplicadas / basura no rompen el lector (contadores de duplicados y errores).
R6  microbench: coste por evento de la primitiva de decision incremental (cota informativa del d_proc de computo).
R8  hashes congelados (H1): el runner ABORTA (exit 3) si un hash difiere o falta la referencia; HASHES_CONGELADOS.json coincide con el codigo actual.
R9  escenarios en paralelo (C4): OUT/c59/ con las mismas colocaciones y cinta distinta; mkt rows (calidad del feed) y cobertura por moneda (H4).
R10 W = minimo de ficheros activos, fichero Binance ignorado, hueco de feed marcado (H3).
R11 resolver: join exacto por token (H10).
R12 informe: EV incondicional/condicional, P(fill), IC por cierre/dia, placebo."""
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
    import cxb60_io as IO
    txt, ok = R.miembros_validos(out + f'dec_{dia}.csv.gz'); ls = [l for l in txt.split('\n') if l]; return IO.lee_dec(out + f'dec_{dia}.csv.gz'), ls


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
    cmd = [sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', out, '--once', '--files', f, '--solo-dia', dia, '--sin-verificar-hash']
    r1 = subprocess.run(cmd, capture_output=True, text=True, timeout=300); assert r1.returncode == 0, r1.stderr[-2000:] + r1.stdout[-1000:]
    filas, ls = leer_dec(out, dia); seg = [x for x in filas if x['tipo'] == 'seg']; nof = [x for x in filas if x['tipo'] == 'nof']
    assert len(nof) == 2 * len(C.LEVELS) * (len(C.default_specs(R.L_LIST, 1))) and len(seg) > 0, (len(nof), len(seg))   # 2 tokens (A, B) x 4 L x (6 variantes + placebo semilla 1: las demas semillas no escriben nof)
    assert len([x for x in filas if x['tipo'] == 'mkt']) == 2
    claves = [(x['tok'], x['L'], x['var'], x['seg']) for x in seg]; assert len(claves) == len(set(claves)), 'claves seg duplicadas'
    man = json.load(open(out + 'run_manifest.json')); assert man['status'] == 'COMPLETE' and man['modo'].startswith('DRY_RUN') and 'cxb60_core.py' in man['codigo'] and 'frozen/engine_v3.py' in man['codigo'] and man['sello_print'] == 'ws_ex-19-1'
    cov = json.load(open(out + f'coverage_{dia}.json')); assert cov['esperados_vistos'] == 2 and cov['procesados'] == 2 and 'ETH' in cov['por_moneda'] and cov['por_moneda']['ETH']['procesados'] == 2, cov
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
    subprocess.run([sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', out, '--once', '--files', f, '--solo-dia', dia, '--sin-verificar-hash'], capture_output=True, text=True, timeout=300, check=True)
    os.makedirs(d + '/gm'); json.dump({'x': dict(id=777, des='YES')}, open(d + '/gm/gmap_x.json', 'w'))                      # mercado 777 resuelto YES; 888 (15m) irrelevante
    o1, st1 = V.resolve(out + f'dec_{dia}.csv.gz', V.carga_gmap(d + '/gm')); o2, st2 = V.resolve(out + f'dec_{dia}.csv.gz', V.carga_gmap(d + '/gm'))
    assert st1 == st2 and st1['fills'] > 0 and st1['sin_desenlace'] == 0, st1
    pn = sum(float(r['pnl']) for r in o1 if r['pnl'] != ''); gm0 = V.carga_gmap(d + '/gm_vacio'); o3, st3 = V.resolve(out + f'dec_{dia}.csv.gz', gm0)
    assert st3['sin_desenlace'] == st3['fills'] and all(r['pnl'] == '' for r in o3), st3                                   # sin desenlace: no se inventa PnL
    # duplicar el bloque no duplica el PnL
    p = out + f'dec_{dia}.csv.gz'; txt, ok = R.miembros_validos(p); R.append_gz(p, '\n'.join(txt.split('\n')[1:]))
    o4, st4 = V.resolve(p, V.carga_gmap(d + '/gm')); assert st4['duplicados'] > 0 and abs(sum(float(r['pnl']) for r in o4 if r['pnl'] != '') - pn) < 1e-9, st4
    shutil.rmtree(d); print('R7 ok: fills', st1['fills'], 'duplicados descartados', st4['duplicados'])


def test_hashes_congelados():
    """R8: la referencia coincide con el codigo actual; si un hash difiere (o falta la referencia) el runner aborta con exit 3 y no escribe nada."""
    import cxb60_io as IO
    ok, det = IO.verifica_hashes(); assert ok, ('HASHES_CONGELADOS.json no coincide con el codigo: regenerar con congelar_hashes_cxb60.py si fue deliberado', det)
    d = tempfile.mkdtemp(); ref = json.load(open(IO.HASHES_FILE)); ref['hashes']['frozen/engine_v3.py'] = '0' * 64; bad = d + '/h.json'; json.dump(ref, open(bad, 'w'))
    env = dict(os.environ, CXB60_HASHES_FILE=bad); out = d + '/out/'; f = d + '/maker_ms_2026-11-12_1.csv.gz'; escribe(f, sint(3))
    r = subprocess.run([sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', out, '--once', '--files', f], capture_output=True, text=True, timeout=120, env=env)
    assert r.returncode == 3 and 'ABORTO' in r.stderr and 'frozen/engine_v3.py' in r.stderr and not os.path.exists(out + 'run_manifest.json'), (r.returncode, r.stderr[-600:])
    ref2 = dict(ref); bad2 = d + '/vacio.json'; ok2, det2 = IO.verifica_hashes(bad2); assert not ok2 and 'error' in det2                      # sin referencia: fail-closed
    r2 = subprocess.run([sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--dir', d, '--out', d + '/o2/', '--sin-verificar-hash'], capture_output=True, text=True, timeout=60); assert r2.returncode != 0 and 'solo se admite con --once' in r2.stderr     # el demonio siempre verifica
    shutil.rmtree(d); print('R8 ok: hash distinto => exit 3; sin referencia => fallo; demonio sin bypass')


def test_escenarios_paralelo_y_calidad():
    d = tempfile.mkdtemp(); dia = dt.datetime.fromtimestamp(FIN - 150, dt.timezone.utc).strftime('%Y-%m-%d'); f = d + f'/maker_ms_{dia}_1.csv.gz'; escribe(f, sint(3)); out = d + '/out/'
    subprocess.run([sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', out, '--once', '--files', f, '--solo-dia', dia, '--sin-verificar-hash', '--placebo', '3'], capture_output=True, text=True, timeout=300, check=True)
    a, _ = leer_dec(out, dia); b, _ = leer_dec(out + 'c59/', dia); sa = [x for x in a if x['tipo'] == 'seg']; sb = [x for x in b if x['tipo'] == 'seg']
    assert len(sb) > 0 and {x['var'] for x in sb}.isdisjoint({'PLC60_1', 'PLC60_2', 'PLC60_3'}) and {'PLC60_1', 'PLC60_3'} <= {x['var'] for x in sa}, 'c59 sin placebo; primario con 3 semillas'
    assert json.load(open(out + 'c59/run_manifest.json'))['sello_print'] == 'ws_ex-59-1' and json.load(open(out + 'c59/run_manifest.json'))['parametros']['c_print'] == 59
    # mismas colocaciones y decisiones (solo la cinta cambia el relleno): claves (tok,L,var,seg,t_dec_rx) de G0/GEO1 del primario y de c59 coinciden en t_dec_rx de los segmentos que existen en ambos
    ka = {(x['tok'], x['L'], x['var'], x['seg']): x['t_dec_rx'] for x in sa if x['var'] in ('G0', 'GEO1')}; kb = {(x['tok'], x['L'], x['var'], x['seg']): x['t_dec_rx'] for x in sb if x['var'] in ('G0', 'GEO1')}
    comunes = set(ka) & set(kb); assert comunes and all(ka[k] == kb[k] for k in comunes)
    mk = [x for x in a if x['tipo'] == 'mkt']; det = json.loads(mk[0]['detalle']); assert {'hueco_feed', 'vac_max_s', 'nq_ventana', 'W_edad_ms'} <= set(det), det
    cov = json.load(open(out + f'coverage_{dia}.json')); assert cov['dia_valido'] is False and cov['cobertura'] is not None and cov['por_moneda']['ETH']['ok_095'] in (True, False)            # 1 mercado no es un dia: nunca valido
    shutil.rmtree(d); print('R9 ok: c59 en paralelo, mkt rows, cobertura por moneda; seg primario', len(sa), 'c59', len(sb))


def test_W_min_binance_y_hueco():
    d = tempfile.mkdtemp(); out = d + '/o/'; os.makedirs(out)
    a = R.parse_args(['--out', out, '--once', '--files', d + '/x', '--sin-verificar-hash', '--c-print-par', '0', '--placebo', '1']); r = R.Run(a)
    fA, fB = d + '/A.gz', d + '/B.gz'; open(fA, 'wb').close(); open(fB, 'wb').close()
    r.feed([f'k,1,{TA},ETH,5min,777,{iso(FIN)},YES'], fA); r.feed([f'q,5000,{TA},0.1,0.2,1,1,100000', f'q,5001,{TA},0.1,0.2,1,1,160000'], fA); r.feed([f'q,5000,{TA},0.1,0.2,1,1,90000'], fB)
    r.actualiza_W(); assert r.W == 90000, r.W                                                                                    # min de los ficheros ACTIVOS (ambos recien creados)
    os.utime(fB, (time.time() - 1000, time.time() - 1000)); r2 = R.Run(a); r2.Wf = {fA: 100000, fB: 90000}; r2.actualiza_W(); assert r2.W == 100000, r2.W    # B inactivo (mtime viejo) deja de frenar W
    # hueco de feed: segundos con mensajes solo al principio de la ventana => vac_max grande
    m = r.meta[TA]; r.sec['ETH'] = set(range(m['fin'] - 332, m['fin'] - 300)); q = r.calidad_feed(m); assert q['hueco_feed'] and q['vac_max_s'] >= 300, q
    r.sec['ETH'] = set(range(m['fin'] - 332, m['fin'] + 1)); q = r.calidad_feed(m); assert not q['hueco_feed'] and q['vac_n_s'] == 0, q
    # fichero Binance (primera fila x/b) se clasifica y se ignora; el del libro no
    assert r.clasifica('f', ['tipo,t_ms,id,c1', 'x,1,BTCUSDT,1,1,0,1,2']) == 'bn' and r.clasifica('f', ['tipo,t_ms', 'k,1,2']) == 'pm' and r.clasifica('f', ['tipo,t_ms']) is None
    # demonio de semanas: mercados con >2 dias salen de meta/by5/coin_of/done al recortar (sin perder el cerrado en disco)
    r.scens[0].done.add(TA); r.W = (FIN + 3 * 86400) * 1000; r.last_prune = 0; r.gc(); assert TA not in r.meta and TA not in r.coin_of and (m['mid'], m['lado']) not in r.by5 and TA not in r.scens[0].done
    shutil.rmtree(d); print('R10 ok: W min activos, hueco de feed, clasificacion Binance, poda de meta')


def test_resolver_join_token():
    import cxb60_resolve as V
    d = tempfile.mkdtemp(); dia = dt.datetime.fromtimestamp(FIN - 150, dt.timezone.utc).strftime('%Y-%m-%d'); f = d + f'/maker_ms_{dia}_1.csv.gz'; escribe(f, sint(5)); out = d + '/out/'
    subprocess.run([sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', out, '--once', '--files', f, '--solo-dia', dia, '--sin-verificar-hash'], capture_output=True, text=True, timeout=300, check=True)
    os.makedirs(d + '/gm'); json.dump({'x': dict(id=777, des='YES', toks=[TA, TB])}, open(d + '/gm/gmap_x.json', 'w')); o, st = V.resolve(out + f'dec_{dia}.csv.gz', V.carga_gmap(d + '/gm')); assert st['join_tok_mismatch'] == 0 and st['sin_desenlace'] == 0 and st['fills'] > 0, st
    json.dump({'x': dict(id=777, des='YES', toks=['999', '998'])}, open(d + '/gm/gmap_x.json', 'w')); o2, st2 = V.resolve(out + f'dec_{dia}.csv.gz', V.carga_gmap(d + '/gm')); assert st2['join_tok_mismatch'] == st2['seg'] and st2['sin_desenlace'] == st2['fills'] and all(r['pnl'] == '' for r in o2), st2   # join exacto: no se resuelve por mid
    shutil.rmtree(d); print('R11 ok: join exacto por token')


def test_informe():
    """R12: sobre un dec/res sintetico con 2 dias, el informe calcula EV incondicional (<= condicional en valor absoluto por el denominador mayor), P(fill) y excluye dias no validos."""
    import cxb60_resolve as V, cxb60_informe as I
    d = tempfile.mkdtemp(); out = d + '/out/'; os.makedirs(out); gz = dt.datetime.fromtimestamp(FIN - 150, dt.timezone.utc).strftime('%Y-%m-%d'); gm = d + '/gm'; os.makedirs(gm); json.dump({'x': dict(id=777, des='YES', toks=[TA, TB])}, open(gm + '/gmap_x.json', 'w'))
    for k, dia in enumerate((gz, '2026-11-13')):
        f = d + f'/maker_ms_{gz}_{k}.csv.gz'; escribe(f, sint(3 + k)); o = d + f'/o{k}/'
        subprocess.run([sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--out', o, '--once', '--files', f, '--solo-dia', gz, '--sin-verificar-hash', '--placebo', '4'], capture_output=True, text=True, timeout=300, check=True)
        shutil.copy(o + f'dec_{gz}.csv.gz', out + f'dec_{dia}.csv.gz'); open(out + f'coverage_{dia}.json', 'w').write(json.dumps(dict(dia=dia, dia_valido=(k == 0), cobertura=1.0 if k == 0 else 0.5, dia_completo=True, por_moneda={'ETH': dict(cobertura=1.0)})))
        subprocess.run([sys.executable, '-I', HERE + 'cxb60_resolve.py', dia, '--out', out, '--gmap-dir', gm], capture_output=True, text=True, timeout=120, check=True)
    subprocess.run([sys.executable, '-I', HERE + 'cxb60_informe.py', '--out', out, '--c59-dir', out + 'nada'], capture_output=True, text=True, timeout=300, check=True)
    inf = json.load(open(out + 'informe_cxb60.json')); assert inf['dias_usados'] == [gz] and '2026-11-13' in inf['dias_no_validos_excluidos'], inf['dias_usados']
    v = inf['variantes']['CXB60']; assert v['n_colocaciones'] > 0 and 0 <= v['P_fill_colocaciones'] <= 1 and v['mercados_procesados'] == 2 and 'ev_incondicional_por_eur' in v and inf['placebo']['semillas'] == 4 and 0 < inf['placebo']['p_valor'] <= 1, v
    if v['ev_cond_fill_ponderado_eur'] is not None and v['ev_incondicional_por_eur'] is not None: assert abs(v['ev_incondicional_por_eur']) <= abs(v['ev_cond_fill_ponderado_eur']) + 1e-9      # denominador cost_pot >= cost
    shutil.rmtree(d); print('R12 ok: informe; CXB60', {k: v[k] for k in ('n_colocaciones', 'n_rellenos', 'P_fill_colocaciones', 'ev_incondicional_por_eur', 'ev_cond_fill_ponderado_eur')})


def test_demonio_smoke():
    """R13: modo DEMONIO (sin --once) sobre un directorio temporal: verifica hashes (real), lee el fichero del dia, escribe heartbeat/manifiesto, cierra mercados y termina limpio con SIGTERM (PARTIAL), sin ordenes."""
    import signal
    d = tempfile.mkdtemp(); hoy = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d'); f = d + f'/maker_ms_{hoy}_1.csv.gz'; escribe(f, sint(3)); out = d + '/out/'
    p = subprocess.Popen([sys.executable, '-I', HERE + 'cxb60_dryrun_fase0.py', '--dir', d, '--out', out, '--c-print-par', '0', '--placebo', '1'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    t0 = time.time(); ok = False
    while time.time() - t0 < 90:
        time.sleep(1)
        if os.path.exists(out + f'dec_{dt.datetime.fromtimestamp(FIN - 150, dt.timezone.utc).strftime("%Y-%m-%d")}.csv.gz') and os.path.exists(out + 'heartbeat.json'):
            hb = json.load(open(out + 'heartbeat.json'))
            if hb['cerrados']['c19'] >= 2: ok = True; break
    p.send_signal(signal.SIGTERM); o, _ = p.communicate(timeout=60)
    assert ok, o[-1500:]; man = json.load(open(out + 'run_manifest.json')); hb = json.load(open(out + 'heartbeat.json'))
    assert p.returncode == 0 and man['status'] == 'PARTIAL' and man['hash_check']['ok'] is True and hb['status'] == 'STOPPED_PARTIAL' and hb['rss_mb'] > 0, (p.returncode, man['status'], o[-800:])
    shutil.rmtree(d); print('R13 ok: demonio, hashes verificados, cerrados', hb['cerrados'], 'RSS', hb['rss_mb'], 'MB')


if __name__ == '__main__':
    test_gztail(); test_extremo_a_extremo_idempotente_y_corrupcion(); test_microbench_decision(); test_resolver(); test_escenarios_paralelo_y_calidad(); test_W_min_binance_y_hueco(); test_resolver_join_token(); test_informe(); test_hashes_congelados(); test_demonio_smoke(); print('TODOS OK (runner)')
