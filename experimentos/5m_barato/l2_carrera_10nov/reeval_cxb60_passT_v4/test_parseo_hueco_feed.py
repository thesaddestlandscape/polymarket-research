"""test_parseo_hueco_feed.py -- ESPEC E8(c): el parseo del 'hueco_feed' acepta las dos formas JSON (con y sin espacio tras los dos puntos). El informe congelado (dryrun/cxb60_informe.py:38) solo acepta la forma sin espacio."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_informe_reeval as RI

def test_acepta_ambas_formas_y_rechaza_falso():
    assert RI.tiene_hueco_feed('{"hueco_feed":true,"vac_max_s":55}') and RI.tiene_hueco_feed('{"hueco_feed": true, "vac_max_s": 55}') and RI.tiene_hueco_feed('{"vac_max_s":1,"hueco_feed" :  true}')
    assert not RI.tiene_hueco_feed('{"hueco_feed":false}') and not RI.tiene_hueco_feed('{"hueco_feed": false}') and not RI.tiene_hueco_feed('') and not RI.tiene_hueco_feed(None) and not RI.tiene_hueco_feed('{"otro_hueco_feed_x": true}')
    for d in ({'hueco_feed': True}, {'hueco_feed': False}): assert RI.tiene_hueco_feed(json.dumps(d)) == d['hueco_feed'] and RI.tiene_hueco_feed(json.dumps(d, separators=(',', ':'))) == d['hueco_feed']

def test_el_congelado_sigue_intacto_y_tiene_el_defecto():
    src = open(HERE + '../dryrun/cxb60_informe.py').read(); assert '\'"hueco_feed":true\' in r[21]' in src            # documentado: el original NO se toca
    h = json.load(open(HERE + '../dryrun/HASHES_CONGELADOS.json')); import hashlib
    assert hashlib.sha256(open(HERE + '../dryrun/cxb60_informe.py', 'rb').read()).hexdigest() == h['hashes']['cxb60_informe.py']
