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
