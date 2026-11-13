#!/usr/bin/env python3
"""Tests de verificar_codigo_cxb60.py (C1). python3 -I test_verificar_codigo.py  (sintetico en tmp; sin red ni Telegram; no toca el datalog real)
K1 sano: disco == referencia == codigo del manifiesto (primario y c59) -> ok.
K2 un fichero congelado editado en disco -> disco_distinto.
K3 el proceso arranco con codigo distinto del congelado (manifiesto) -> proceso_con_codigo_distinto; hash_check ausente/False -> arranque_sin_verificar.
K4 sin referencia o sin manifiesto -> fail-closed (no ok).
K5 deriva del origen dev: solo informativa (ok sigue True).
K6 main: avisa UNA vez por dia y firma (latch), rc 1; sano rc 0; CXB60_DIR invalido rc 2."""
import os, sys, json, shutil, tempfile, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE.rstrip('/')) + '/')
import cxb60_io as IO, verificar_codigo_cxb60 as V
os.environ['CXB60_SIN_TELEGRAM'] = '1'
TMP = tempfile.mkdtemp(prefix='t_verif_codigo_')
sha = lambda b: hashlib.sha256(b).hexdigest()


def montar(nombre):
    base = f'{TMP}/{nombre}/base/'; out = f'{TMP}/{nombre}/out/'; os.makedirs(base + 'frozen'); os.makedirs(out + 'c59')
    h = {}
    for f in IO.FICHEROS_CONGELADOS:
        c = f'contenido {f}'.encode(); open(base + f, 'wb').write(c); h[f] = sha(c)
    org = f'{TMP}/{nombre}/origen_engine.py'; open(org, 'w').write('x'); ref = dict(hashes=h, origen={'frozen/engine.py': dict(ruta=org, sha256=sha(b'x'))})
    hp = f'{TMP}/{nombre}/HASHES.json'; json.dump(ref, open(hp, 'w'))
    for d in (out, out + 'c59/'): json.dump(dict(escenario='c19', status='RUNNING', codigo=dict(h), hash_check=dict(ok=True)), open(d + 'run_manifest.json', 'w'))
    return base, out, hp, h, org


def tipos(r): return sorted(c for c, _ in r['problemas'])


def test_sano_y_deriva():
    base, out, hp, h, org = montar('a'); r = V.comprobar(out, hp, base); assert r['ok'] and not r['problemas'] and not r['info'], r
    open(base + 'cxb60_core.py', 'a').write(' # editado'); r = V.comprobar(out, hp, base); assert not r['ok'] and tipos(r) == ['disco_distinto'], r   # K2
    open(org, 'w').write('cambiado'); base2, out2, hp2, h2, org2 = montar('a2'); open(org2, 'w').write('otro'); r = V.comprobar(out2, hp2, base2)
    assert r['ok'] and len(r['info']) == 1, r                                                                                                        # K5 informativo


def test_proceso_distinto():
    base, out, hp, h, org = montar('b'); m = json.load(open(out + 'c59/run_manifest.json')); m['codigo']['frozen/engine_v3.py'] = 'a' * 64; json.dump(m, open(out + 'c59/run_manifest.json', 'w'))
    r = V.comprobar(out, hp, base); assert not r['ok'] and tipos(r) == ['proceso_con_codigo_distinto'] and 'c19' in r['problemas'][0][1], r                  # K3
    base, out, hp, h, org = montar('b2'); m = json.load(open(out + 'run_manifest.json')); m['hash_check'] = None; json.dump(m, open(out + 'run_manifest.json', 'w'))
    assert tipos(V.comprobar(out, hp, base)) == ['arranque_sin_verificar']
    m['hash_check'] = dict(ok=False); json.dump(m, open(out + 'run_manifest.json', 'w')); assert tipos(V.comprobar(out, hp, base)) == ['arranque_sin_verificar']


def test_fail_closed():
    base, out, hp, h, org = montar('c'); os.remove(hp); r = V.comprobar(out, hp, base); assert not r['ok'] and tipos(r) == ['sin_referencia']                  # K4
    base, out, hp, h, org = montar('c2'); os.remove(out + 'run_manifest.json'); os.remove(out + 'c59/run_manifest.json'); assert 'sin_manifiesto' in tipos(V.comprobar(out, hp, base))
    base, out, hp, h, org = montar('c3'); open(out + 'run_manifest.json', 'w').write('{no json'); assert 'manifiesto_ilegible' in tipos(V.comprobar(out, hp, base))


def test_main_latch():
    base, out, hp, h, org = montar('d'); os.environ['CXB60_DIR'] = out; os.environ['CXB60_HASHES_FILE'] = hp
    import io, contextlib
    V.DRY = base                                                                  # comprobar(base=None) usa DRY
    def run():
        b = io.StringIO()
        with contextlib.redirect_stdout(b): rc = V.main()
        return rc, b.getvalue()
    rc, s = run(); assert rc == 0, s                                              # K6 sano
    open(base + 'cxb60_io.py', 'a').write('#x'); rc, s = run(); assert rc == 1 and 'AVISO (seco' in s, s
    marcas = [f for f in os.listdir(out) if f.startswith('aviso_codigo_')]; assert len(marcas) == 1, marcas
    rc, s = run(); assert rc == 1 and 'AVISO (seco' not in s, s                   # misma firma/dia: no se repite
    os.environ['CXB60_DIR'] = TMP + '/no_existe'; assert V.main() == 2


if __name__ == '__main__':
    try: test_sano_y_deriva(); test_proceso_distinto(); test_fail_closed(); test_main_latch(); print('TODOS OK (verificar_codigo_cxb60)')
    finally: shutil.rmtree(TMP, ignore_errors=True)
