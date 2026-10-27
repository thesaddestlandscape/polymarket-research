import sys, os, json, gzip, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import reconstruir_puja_fin as R, markouts_desde_registro as M, reconstructor_diario_puja_fin as D


def test_pasada_unica_idempotente(tmp_path):
    ini = int(time.time()) - 86400 * 3; ini -= ini % 300; slug = f'eth-updown-5m-{ini}'
    dia = M.dt.datetime.utcfromtimestamp(ini).strftime('%Y-%m-%d'); fin_s = M.dt.datetime.utcfromtimestamp(ini + 300).strftime('%Y-%m-%d %H:%M:%S+00:00')
    iso = lambda t: M.dt.datetime.fromtimestamp(t, M.dt.timezone.utc).isoformat()
    led = [dict(tipo='puja_post', oid='o1', slug=slug, coin='eth', lado='YES', precio=0.25, k=1, ts=iso(ini + 50)),
           dict(tipo='lectura', oid='o1', f=5.0, precio=0.25, ts=iso(ini + 100), acc=5.0)]
    (tmp_path / 'led.jsonl').write_text('\n'.join(json.dumps(x) for x in led) + '\n')
    vol = tmp_path / 'v'; vol.mkdir()
    with gzip.open(vol / f'm5_registro_{dia}.csv.gz', 'wt') as f:
        f.write(f'k,1,TOK,ETH,5min,9,{fin_s},YES\n' + ''.join(f'q,{int((ini+t)*1000)},TOK,0.3,0.32,1,1,{int((ini+t)*1000)+9}\n' for t in range(0, 260, 20)))
    R.LEDGER, R.OUT, R.POSIC = str(tmp_path / 'led.jsonl'), str(tmp_path / 'rec.jsonl'), str(tmp_path / 'nada.csv')
    M.VOL, M.L5, M.DL, M.OUT = str(vol), str(tmp_path / 'l5'), str(tmp_path), str(tmp_path / 'mk.jsonl')
    a = D.correr(); b = D.correr()
    assert a['reconstruidos_nuevos'] == 1 and a['markouts']['escritas'] == 1
    assert b['reconstruidos_nuevos'] == 0 and b['markouts']['calculadas'] == 0 and b['markouts']['ya_hechos'] == 1
    assert len(open(M.OUT).read().splitlines()) == 1 and len(open(R.OUT).read().splitlines()) == 1
    # dia sin archivar -> aplazado, nada escrito
    os.remove(vol / f'm5_registro_{dia}.csv.gz'); os.remove(M.OUT)
    c = D.correr(); assert c['markouts']['esperan_archivo_dia'] == 1 and not os.path.exists(M.OUT)


def _led(ini, extra=(), intencion=True):
    iso = lambda t: M.dt.datetime.fromtimestamp(t, M.dt.timezone.utc).isoformat()
    slug = f'eth-updown-5m-{ini}'
    base = dict(oid='o1', slug=slug, tok='tU', lado='YES', precio=0.25, size=5, real=True)
    filas = [dict(base, tipo='intencion_post', ts=iso(ini + 40))] if intencion else []
    return slug, filas + [dict(base, tipo='puja_post', coin='eth', k=1, ts=iso(ini + 50)),
                          dict(tipo='lectura', oid='o1', f=2.0, precio=0.25, ts=iso(ini + 100), acc=2.0, real=True)] + list(extra)


def _prep(filas, ahora):
    p = D._robustez().preparar(filas, ahora)
    return p.permitidos, p.parciales, sorted(p.esperan + p.inmaduros)


def test_misma_logica_que_el_ejecutor_difiere_sin_verificar_y_recientes():
    import h47_robustez as H
    assert D._robustez() is H and H.fin_de is H.fin_de and H.__file__.startswith(D.PARCHE)
    ahora = time.time(); ini = int(ahora) - 86400; ini -= ini % 300
    slug, led = _led(ini)                                             # lectura 2 < size 5 y sin verificar -> espera
    assert _prep(led, ahora) == (set(), set(), [slug])
    verif = [dict(tipo='fuera_libro', oid='o1', ts=M.dt.datetime.fromtimestamp(ini + 110, M.dt.timezone.utc).isoformat(), real=True),
             dict(tipo='verificada', oid='o1', f=2.0, real=True, ts=M.dt.datetime.fromtimestamp(ini + 400, M.dt.timezone.utc).isoformat())]
    assert _prep(led + verif, ahora) == ({slug}, set(), [])
    reciente = int(ahora) - 100; reciente -= reciente % 300           # fin+35+60 s aun no paso (o recien pasado)
    s2, l2 = _led(reciente, [dict(tipo='lectura', oid='o1', f=5.0, real=True)])
    assert _prep(l2, reciente + 300 + 90) == (set(), set(), [s2]) and _prep(l2, reciente + 300 + 96)[0] == {s2}
    assert _prep(l2, reciente + 300 + 96)[2] == []


def test_intencion_sin_puja_post_anomalia_e_ilegible_se_difieren_y_completos_no_cuentan():
    ahora = time.time(); ini = int(ahora) - 86400; ini -= ini % 300
    s, l = _led(ini)
    solo_int = [d for d in l if d['tipo'] == 'intencion_post']          # intencion huerfana: sin puja_post ni lectura
    assert _prep(solo_int, ahora) == (set(), set(), [s])
    ilegible = [dict(d, size=None) if d['tipo'] == 'intencion_post' else d for d in l] + [dict(tipo='lectura', oid='o1', f=5.0, real=True)]
    assert _prep(ilegible, ahora)[2] == [s]
    anomala = l + [dict(tipo='lectura', oid='o1', f=9.0, real=True)]    # lectura > size -> anomalia
    assert _prep(anomala, ahora)[2] == [s]
    # hallazgo 2: con puja_fin COMPLETO el slug no es candidato ni 'espera'; el parcial si espera/reconstruye
    assert _prep(l + [dict(tipo='puja_fin', slug=s)], ahora) == (set(), set(), [])
    assert _prep(l + [dict(tipo='puja_fin', slug=s, interrumpida=True)], ahora)[1] == {s}


def test_parcial_interrumpido_se_reconstruye_marcado_y_un_puja_fin_completo_cierra(tmp_path):
    ahora = time.time(); ini = int(ahora) - 86400; ini -= ini % 300
    fuera = M.dt.datetime.fromtimestamp(ini + 110, M.dt.timezone.utc).isoformat()
    ver = M.dt.datetime.fromtimestamp(ini + 400, M.dt.timezone.utc).isoformat()
    slug, led = _led(ini, [dict(tipo='fuera_libro', oid='o1', ts=fuera, real=True), dict(tipo='verificada', oid='o1', f=2.0, ts=ver, real=True),
                           dict(tipo='puja_fin', slug=f'eth-updown-5m-{ini}', interrumpida=True)])
    perm, parc, esp = _prep(led, ahora)
    assert parc == {slug} and perm == {slug} and esp == []
    R.LEDGER, R.OUT, R.POSIC = str(tmp_path / 'l.jsonl'), str(tmp_path / 'r.jsonl'), str(tmp_path / 'n.csv')
    (tmp_path / 'l.jsonl').write_text(''.join(json.dumps(x) + '\n' for x in led))
    M.VOL, M.L5, M.DL, M.OUT = str(tmp_path / 'v'), str(tmp_path / 'l5'), str(tmp_path), str(tmp_path / 'mk.jsonl')
    D.correr()
    r = [json.loads(x) for x in open(R.OUT)]
    assert len(r) == 1 and r[0]['sustituye_puja_fin_parcial'] is True
    D.correr()
    assert len(open(R.OUT).read().splitlines()) == 1                  # idempotente por slug


def test_pins_hash_ruta_trackeada_y_fallo_ruidoso(tmp_path):
    import shutil
    H = D._robustez()
    assert sys.path[0] == D.PARCHE and D.PARCHE.startswith('/root/polymarket-research/experimentos/') and 'dev' not in D.PARCHE
    d = tmp_path / 'copia'; d.mkdir()
    for f in D.PINS: shutil.copy(os.path.join(D.PARCHE, f), d / f)
    with open(d / 'h47_robustez.py', 'a') as f: f.write('\n# cambio sin actualizar PINS\n')
    try: D._robustez(str(d)); assert False, 'debia fallar'
    except RuntimeError as e: assert 'h47_robustez.py' in str(e)
    sys.path[:] = [x for x in sys.path if x != str(d)]; D._robustez()      # restaura la ruta buena en sys.path[0]


def test_cron_salta_paso1_si_el_hilo_trabaja_y_no_cuenta_inmaduros_en_esperan(tmp_path):
    H = D._robustez()
    ahora = time.time(); ini = int(ahora) - 86400; ini -= ini % 300
    slug, led = _led(ini, [dict(tipo='fuera_libro', oid='o1', ts=M.dt.datetime.fromtimestamp(ini + 110, M.dt.timezone.utc).isoformat(), real=True),
                           dict(tipo='verificada', oid='o1', f=2.0, real=True, ts=M.dt.datetime.fromtimestamp(ini + 400, M.dt.timezone.utc).isoformat())])
    R.LEDGER, R.OUT, R.POSIC = str(tmp_path / 'l.jsonl'), str(tmp_path / 'r.jsonl'), str(tmp_path / 'n.csv')
    (tmp_path / 'l.jsonl').write_text(''.join(json.dumps(x) + '\n' for x in led))
    M.VOL, M.L5, M.DL, M.OUT = str(tmp_path / 'v'), str(tmp_path / 'l5'), str(tmp_path), str(tmp_path / 'mk.jsonl')
    with H.bloqueo_proceso(R.OUT) as b:                                # el hilo del ejecutor esta reconstruyendo
        assert b.ok
        r = D.correr()
    assert r['paso1_saltado_hilo_activo'] is True and r['reconstruidos_nuevos'] == 0 and not os.path.exists(R.OUT)
    r = D.correr()
    assert r['paso1_saltado_hilo_activo'] is False and r['reconstruidos_nuevos'] == 1 and r['esperan_verificacion'] == 0 and r['vencidos_sin_verificar'] == []
