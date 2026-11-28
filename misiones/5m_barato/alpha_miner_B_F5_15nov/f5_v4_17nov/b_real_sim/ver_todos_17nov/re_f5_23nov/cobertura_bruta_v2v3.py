#!/usr/bin/env python3
"""cobertura_bruta_v2v3.py DIA [DIA ...]  (28-Nov, ADENDA_V2V3_rf5.md; ANEXO2 §3). WRAPPER NUEVO de cobertura_bruta.py (SELLADO en HASHES_rf5.txt: este wrapper lo IMPORTA sin modificarlo). Unica diferencia: la lectura de onchain_fills.
cobertura_bruta.calcula(x, keep=DIR) lee `DIR/onchain_fills_{x}*.csv.gz`; el wrapper prepara un DIR de symlinks en datalogs/exp5bis_27nov/paso3/keep_v2v3/x/ con:
  - dias <= 22-Nov (solo V2): EXACTAMENTE los ficheros que leia el sello (keep_onchain_re_as_b/onchain_fills_x*.csv.gz) => la salida es identica bit a bit a out_rf5_ciego/cobertura_bruta_x.json (test de identidad `--identidad DIA`);
  - dias >= 23-Nov: la cadena V2 de cadena_v2v3.rutas_cadena(x) + la V3 como onchain_fills_x_v3.csv.gz (si falta V3 FileNotFoundError: fail-loud, nunca solo V2).
Sello doble: la salida lleva `codigo_sha` (el de cobertura_bruta.py, sin cambios) + `adenda_v2v3` {sha16 cadena_v2v3, sha16 wrapper, versiones, ficheros}. Cache en out_rf5_ciego_v2v3/ (NO escribe en out_rf5_ciego/): no se mezclan muestras V2-solo y doble sello.
Pesado (cadena de un dia + libro5_tx x-1..x+1): por scripts/cron_pesado.sh con ulimit -v 3000000; fuera de 22:00-02:45Z. 0 ordenes, 0 red."""
import os, sys, glob, json, hashlib
sys.dont_write_bytecode = True
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, HV)
import cobertura_bruta as CB
EX = '/root/polymarket-research/experimentos/5m_barato/exp5bis_27nov'
sys.path.append(EX)
import cadena_v2v3 as CV
KEEP_V2 = CB.DL + 'keep_onchain_re_as_b/'
KEEP_BASE = CB.DL + 'exp5bis_27nov/paso3/keep_v2v3/'
OUT = os.environ.get('RF5_OUT_V2V3', HV + 'out_rf5_ciego_v2v3/')
V3_DESDE = '2026-11-23'


def sha16(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]


def prepara_keep(x, keep_v2=KEEP_V2, base=KEEP_BASE, rutas=None):
    """-> (dir con slash, [(version, ruta real)]). Limpia SOLO symlinks de ejecuciones anteriores de ESE dia."""
    d = base + x + '/'; os.makedirs(d, exist_ok=True)
    for f in glob.glob(d + '*'):
        if os.path.islink(f): os.unlink(f)
    usados = []
    sellados = sorted(glob.glob(keep_v2 + f'onchain_fills_{x}*.csv.gz'))
    if x < V3_DESDE and sellados:                                     # V2 solo: los MISMOS ficheros del sello
        for f in sellados: os.symlink(f, d + os.path.basename(f)); usados.append(('v2', f))
        return d, usados
    for ver, p in (rutas if rutas is not None else CV.rutas_cadena(x)):
        os.symlink(p, d + (f'onchain_fills_{x}.csv.gz' if ver == 'v2' else f'onchain_fills_{x}_v3.csv.gz')); usados.append((ver, p))
    return d, usados


def calcula_v2v3(x, **kw):
    d, usados = prepara_keep(x)
    r = CB.calcula(x, keep=d, **kw)
    if r is None: return None
    r['adenda_v2v3'] = dict(sha16_cadena_v2v3=sha16(EX + '/cadena_v2v3.py'), sha16_wrapper=sha16(os.path.abspath(__file__)), versiones=sorted({v for v, _ in usados}), ficheros=[p for _, p in usados])
    return r


def obtener_v2v3(x, out=None, **kw):
    out = out or OUT; os.makedirs(out, exist_ok=True); p = out + f'cobertura_bruta_v2v3_{x}.json'
    me = (CB.sha(os.path.abspath(CB.__file__)), sha16(os.path.abspath(__file__)), sha16(EX + '/cadena_v2v3.py'))
    if os.path.exists(p):
        try:
            j = json.load(open(p)); a = j.get('adenda_v2v3', {})
            if (j.get('codigo_sha'), a.get('sha16_wrapper'), a.get('sha16_cadena_v2v3')) == me: return j
        except (OSError, ValueError): pass
    r = calcula_v2v3(x, **kw)
    if r is None: return None
    json.dump(r, open(p + '.tmp', 'w'), indent=1); os.replace(p + '.tmp', p); return r


def identidad(x, sellado=None):
    """Dia <= 22-Nov: la salida del wrapper (sin la clave 'adenda_v2v3') debe ser IDENTICA a la sellada. -> (ok, motivo)."""
    if x >= V3_DESDE: return False, 'BLOCKED: la identidad solo se prueba en dias <= 22-Nov (solo V2)'
    sp = sellado or (CB.OUT + f'cobertura_bruta_{x}.json')
    if not os.path.exists(sp): return False, f'BLOCKED: no hay salida sellada {sp}'
    ref = json.load(open(sp)); r = calcula_v2v3(x)
    if r is None: return False, 'BLOCKED: faltan fuentes'
    r.pop('adenda_v2v3', None)
    # `codigo_sha` es el hash del modulo que genero la salida: la salida sellada de 18-Nov se genero con una version ANTERIOR de cobertura_bruta.py (1d13b10a...; HASHES_rf5 lista hoy 103b5d50...). Se compara TODO lo demas y se declara la diferencia de sha.
    sha_r, sha_ref = r.pop('codigo_sha', None), ref.pop('codigo_sha', None)
    a, b = json.dumps(r, sort_keys=True), json.dumps(ref, sort_keys=True)
    nota = '' if sha_r == sha_ref else f' (codigo_sha distinto, declarado: wrapper {str(sha_r)[:8]} vs sellada {str(sha_ref)[:8]})'
    return a == b, (('IDENTICA bit a bit en todos los campos' + nota) if a == b else 'BLOCKED: la salida difiere de la sellada')


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--identidad':
        ok, m = identidad(sys.argv[2]); print('IDENTIDAD', sys.argv[2], ok, m); sys.exit(0 if ok else 3)
    for d in sys.argv[1:]:
        r = obtener_v2v3(d); print(d, 'SIN_FUENTE' if r is None else dict(units=r['units'], con_tx=r['con_tx'], cov=r['cov'], versiones=r['adenda_v2v3']['versiones']))
