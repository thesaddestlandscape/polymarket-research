#!/usr/bin/env python3
"""cxb60_io.py -- utilidades MINIMAS (sin numpy/motor) compartidas por el runner del dry-run B-CXB60, el resolvedor y el informe: columnas del dec_, gz con miembros anexados,
escritura atomica, y VERIFICACION DE HASHES CONGELADOS (H1 de INTEGRIDAD_CXB60_DRYRUN_12nov.md).
Hashes: HASHES_CONGELADOS.json (sha256 completo) lo escribe `congelar_hashes_cxb60.py` (accion explicita). El runner ABORTA (exit 3) en el arranque si alguno de los ficheros que ejecuta difiere:
  frozen/{engine,capt,relojes,engine_clock,engine_v3}.py (copia del motor v3 de dev), cxb60_core.py, cxb60_io.py, cxb60_dryrun_fase0.py.
Solo lectura de codigo; 0 ordenes; sin red."""
import os, io, csv, gzip, zlib, json, hashlib

HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
COLS = ['tipo', 'run_id', 'dia', 'tok', 'mid', 'coin', 'lado', 'fin', 'L', 'var', 'seg', 't_dec_rx', 't_arr', 't_end', 'motivo_fin', 'canc', 't_trig_rx', 't_trig_ex', 'q', 'tf', 'rem_antes', 'detalle', 't_wall_ms']
FICHEROS_CONGELADOS = ['frozen/engine.py', 'frozen/capt.py', 'frozen/relojes.py', 'frozen/engine_clock.py', 'frozen/engine_v3.py', 'cxb60_core.py', 'cxb60_io.py', 'cxb60_dryrun_fase0.py', 'l_pool_emp.json']
INFORMATIVOS = ['cxb60_resolve.py', 'cxb60_informe.py']                      # se hashean en el manifiesto pero no son parte del proceso que corre
HASHES_FILE = HERE + 'HASHES_CONGELADOS.json'


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()


def hashes_actuales(extra=()):
    out = {}
    for f in list(FICHEROS_CONGELADOS) + list(INFORMATIVOS) + list(extra):
        p = HERE + f
        out[f] = sha256_file(p) if os.path.exists(p) else 'no_encontrado'
    return out


def verifica_hashes(path=None):
    """(ok, detalle). ok False si falta la referencia, falta un fichero o algun hash difiere. NUNCA 'ok' por defecto: sin referencia = fallo (fail-closed)."""
    path = path or os.environ.get('CXB60_HASHES_FILE') or HASHES_FILE
    if not os.path.exists(path): return False, dict(error='sin fichero de hashes congelados', path=path)
    ref = json.load(open(path)); refh = ref.get('hashes', {}); dif = {}
    for f in FICHEROS_CONGELADOS:
        p = HERE + f; act = sha256_file(p) if os.path.exists(p) else 'no_encontrado'
        if refh.get(f) != act: dif[f] = dict(congelado=refh.get(f), actual=act)
    return (not dif), dict(path=path, sha256_referencia=sha256_file(path), diferencias=dif, ficheros=len(FICHEROS_CONGELADOS))


def miembros_validos(path):
    """(texto, bytes_validos) de un gz de miembros anexados; recorta la cola corrupta/truncada (escritura interrumpida)."""
    if not os.path.exists(path): return '', 0
    raw = open(path, 'rb').read(); pos = 0; parts = []
    while pos < len(raw):
        d = zlib.decompressobj(31)
        try: parts.append(d.decompress(raw[pos:]))
        except zlib.error: break
        if not d.eof: break
        pos = len(raw) - len(d.unused_data)
    return b''.join(parts).decode('utf-8', 'replace'), pos


def append_gz(path, text):
    blob = gzip.compress(text.encode('utf-8'), 6)
    with open(path, 'ab') as f: f.write(blob); f.flush(); os.fsync(f.fileno())


def atomic_json(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w') as f: f.write(json.dumps(obj, indent=1, default=str))
    os.replace(tmp, path)


def csv_text(rows, header=None):
    """Filas -> texto CSV con el quoting del modulo csv (H8: sin heuristicas; un '"' o ',' en `detalle` se escapa bien). \n como fin de linea."""
    b = io.StringIO(); w = csv.writer(b, lineterminator='\n')
    if header: w.writerow(header)
    w.writerows(rows); return b.getvalue()


def lee_dec(path):
    """Filas del dec_/res_ como lista de dict (csv.DictReader sobre miembros validos)."""
    txt, ok = miembros_validos(path); return list(csv.DictReader(io.StringIO(txt)))
