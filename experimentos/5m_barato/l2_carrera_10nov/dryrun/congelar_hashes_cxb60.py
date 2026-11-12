#!/usr/bin/env python3
"""congelar_hashes_cxb60.py -- ACCION EXPLICITA: escribe HASHES_CONGELADOS.json con el sha256 completo de los ficheros que ejecuta el dry-run (ver cxb60_io.FICHEROS_CONGELADOS) y, para las copias frozen/, el sha256 de su ORIGEN.
Ejecutar solo tras una edicion deliberada del codigo y re-congelar el prereg (el hash del dry-run forma parte de la congelacion). `--verificar` solo compara y sale 0/1. Sin red, sin datos."""
import os, sys, json, time
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import cxb60_io as IO
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'; L2 = os.path.dirname(HERE.rstrip('/')) + '/'
ORIGEN = {'frozen/engine.py': P2 + 'escalera_B/engine.py', 'frozen/capt.py': P2 + 'capturabilidad_A_R1ws/capt.py', 'frozen/relojes.py': L2 + 'relojes.py', 'frozen/engine_clock.py': L2 + 'engine_clock.py', 'frozen/engine_v3.py': L2 + 'engine_v3.py'}
if '--verificar' in sys.argv:
    ok, det = IO.verifica_hashes(); print(json.dumps(dict(ok=ok, **det), indent=1)); sys.exit(0 if ok else 1)
h = IO.hashes_actuales(); ref = dict(creado_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), hashes=h, origen={f: dict(ruta=p, sha256=IO.sha256_file(p) if os.path.exists(p) else None) for f, p in ORIGEN.items()},
                                     nota='frozen/* son copias byte a byte de ORIGEN en la fecha de creado_utc; el runner aborta si cualquiera de FICHEROS_CONGELADOS difiere')
json.dump(ref, open(IO.HASHES_FILE, 'w'), indent=1); print('escrito', IO.HASHES_FILE); [print(' ', k, v[:16]) for k, v in h.items()]
