#!/usr/bin/env python3
"""vendorizar_sdk.py -- ACCION EXPLICITA y OFFLINE (nunca la carga el envio): registra en VENDOR_HASHES.json el sha256 de `mercado_version.py` y de CADA fichero de vendor/sdk122/ (py_clob_client_v2 1.2.2, aislado del venv de produccion, 26-Nov).
Origen del SDK: wheel PyPI py_clob_client_v2-1.2.2-py3-none-any.whl, sha256 c7291a450b77cb04a7531865edb5a1adfb1cc528a4514a94dd5f25a665024e8f (coincide con el digest publicado por PyPI y con el RECORD de la wheel). No toca el resto de entradas.
Uso:  python3 -I vendorizar_sdk.py          (reescribe SOLO las entradas sdk122/* y mercado_version.py)       python3 -I vendorizar_sdk.py --verificar"""
import os, sys, json, hashlib, time
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
WHEEL_SHA = 'c7291a450b77cb04a7531865edb5a1adfb1cc528a4514a94dd5f25a665024e8f'
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()


def ficheros():
    out = []
    for d, _, fs in os.walk(HERE + 'sdk122'):
        if '__pycache__' in d: continue
        out += [os.path.relpath(os.path.join(d, f), HERE) for f in fs if not f.endswith('.pyc')]
    return sorted(out)


def main():
    h = json.load(open(HERE + 'VENDOR_HASHES.json'))
    if '--verificar' in sys.argv:
        mal = [f for f in ficheros() + ['mercado_version.py'] if h['copias'].get(f, {}).get('sha256_copia') != sha(HERE + f)]; falta = [f for f in h['copias'] if f.startswith('sdk122/') and not os.path.exists(HERE + f)]
        print(json.dumps(dict(ok=not mal and not falta, alteradas=mal, ausentes=falta))); sys.exit(0 if not mal and not falta else 1)
    for k in [k for k in h['copias'] if k.startswith('sdk122/')]: del h['copias'][k]
    for f in ficheros(): h['copias'][f] = dict(origen=f'PyPI py_clob_client_v2 1.2.2 wheel sha256 {WHEEL_SHA}', sha256_copia=sha(HERE + f))
    h['copias']['mercado_version.py'] = dict(origen='escrito para el paquete (selector de version por mercado + carga aislada del SDK); copia identica en b-k', sha256_copia=sha(HERE + 'mercado_version.py'))
    h['sdk122_actualizado_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    json.dump(h, open(HERE + 'VENDOR_HASHES.json', 'w'), indent=1); print('ok', len(ficheros()), 'ficheros del SDK + mercado_version.py')


if __name__ == '__main__': main()
