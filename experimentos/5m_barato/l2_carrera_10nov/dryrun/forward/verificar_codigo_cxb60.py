#!/usr/bin/env python3
"""verificar_codigo_cxb60.py -- C1 (INTEGRIDAD_CXB60_DRYRUN_12nov.md, H1): comprobacion de CODIGO del dry-run B-CXB60 SIN tocar el runner congelado. Solo lectura; 0 ordenes; sin red salvo Telegram.
ESTADO REAL (13-Nov, verificado): HASHES_CONGELADOS.json YA incluye engine/capt/relojes/engine_clock/engine_v3 como copias byte a byte en dryrun/frozen/ (+ cxb60_core/io/runner/l_pool), cxb60_core.py las importa de
frozen/ (con assert de procedencia) y el runner ABORTA (exit 3) en el arranque si algo difiere; lanzar_cxb60_dryrun.sh repite la comprobacion antes de lanzar. Lo que NO cubria nada: DERIVA EN CALIENTE (el
proceso vivo cargo un codigo y el disco ya es otro: el siguiente reinicio abortaria) y DERIVA DEL ORIGEN en dev (informativa: la copia frozen/ manda).
Comprueba: (1) disco vs HASHES_CONGELADOS (cxb60_io.verifica_hashes); (2) `codigo` de cada run_manifest.json VIVO (primario y c59: lo que el proceso hasheo al arrancar) vs referencia y vs disco;
(3) origen dev vs copia frozen (solo informativo, no es problema).  Salida: 0 sano, 1 problema (avisa por Telegram UNA vez por dia y firma), 2 uso. CXB60_DIR, CXB60_SIN_TELEGRAM, CXB60_TAG, CXB60_HASHES_FILE como el resto.
Activacion (NO instalada): ver docstring de cron_verificar_codigo en el informe; p. ej. `17 * * * * $PY -I .../verificar_codigo_cxb60.py` (ligero, <1 s)."""
import os, sys, json, time, hashlib

HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; DRY = os.path.dirname(HERE.rstrip('/')) + '/'
sys.path.insert(0, DRY)
import cxb60_io as IO


def manifiestos(out):
    """Rutas de run_manifest.json del escenario primario y de los subdirectorios de escenario (c59...)."""
    r = []
    for p in [out + 'run_manifest.json'] + sorted(os.path.join(out, d, 'run_manifest.json') for d in os.listdir(out) if os.path.isdir(os.path.join(out, d))):
        if os.path.exists(p): r.append(p)
    return r


def comprobar(out, hashes_path=None, base=None):
    """Devuelve dict(ok, problemas[(codigo, texto)], info[...]). `base` = directorio de los ficheros congelados (por defecto dryrun/)."""
    base = base or DRY; hashes_path = hashes_path or os.environ.get('CXB60_HASHES_FILE') or IO.HASHES_FILE
    prob, info = [], []
    if not os.path.exists(hashes_path): return dict(ok=False, problemas=[('sin_referencia', f'falta {hashes_path}')], info=[])
    ref = json.load(open(hashes_path)); refh = ref.get('hashes', {})
    for f in IO.FICHEROS_CONGELADOS:
        p = base + f; act = IO.sha256_file(p) if os.path.exists(p) else 'no_encontrado'
        if refh.get(f) != act: prob.append(('disco_distinto', f'{f}: congelado {str(refh.get(f))[:12]} != disco {act[:12]}'))
    mans = manifiestos(out)
    if not mans: prob.append(('sin_manifiesto', f'no hay run_manifest.json en {out}'))
    for mp in mans:
        try: m = json.load(open(mp))
        except (OSError, ValueError) as e: prob.append(('manifiesto_ilegible', f'{mp}: {e}')); continue
        cod = m.get('codigo') or {}; etiqueta = f"{m.get('escenario', '?')}/{m.get('status', '?')}"
        for f in IO.FICHEROS_CONGELADOS:
            if cod.get(f) != refh.get(f): prob.append(('proceso_con_codigo_distinto', f'{etiqueta} {f}: el proceso hasheo {str(cod.get(f))[:12]} != congelado {str(refh.get(f))[:12]} (arrancado con codigo no congelado)'))
        hc = m.get('hash_check')
        if not hc or hc.get('ok') is not True: prob.append(('arranque_sin_verificar', f'{etiqueta}: hash_check={hc}'))
    for f, o in (ref.get('origen') or {}).items():
        rp = o.get('ruta'); s = IO.sha256_file(rp) if rp and os.path.exists(rp) else None
        if s != o.get('sha256'): info.append(f'origen {f}: {rp} {"ausente" if s is None else "difiere"} de la copia congelada (informativo: el runner usa frozen/)')
    return dict(ok=not prob, problemas=prob, info=info, manifiestos=mans, referencia_sha256=IO.sha256_file(hashes_path))


def avisar(texto):
    if os.environ.get('CXB60_SIN_TELEGRAM'): print('AVISO (seco, sin Telegram): ' + texto); return True
    try: sys.path.insert(0, '/root/polymarket-research'); from shadow_digest import enviar_telegram; return enviar_telegram(texto) is True
    except Exception as e: print('Telegram fallo:', e, file=sys.stderr); return False


def main(argv=None):
    out = os.environ.get('CXB60_DIR', '/root/polymarket-research-datalogs/cxb60_dryrun').rstrip('/') + '/'
    if not os.path.isdir(out): print('CXB60_DIR invalido', out, file=sys.stderr); return 2
    r = comprobar(out); print(json.dumps(r, indent=1, default=str))
    if r['ok']: return 0
    firma = hashlib.sha256(json.dumps(sorted(c for c, _ in r['problemas'])).encode()).hexdigest()[:10]; marca = out + f'aviso_codigo_{time.strftime("%Y-%m-%d", time.gmtime())}_{firma}'
    if not os.path.exists(marca):
        tag = os.environ.get('CXB60_TAG', ''); txt = (tag + ' ' if tag else '') + 'cxb60 CODIGO: ' + '; '.join(t for _, t in r['problemas'][:4])
        if avisar(txt): open(marca, 'w').write(txt)
    return 1


if __name__ == '__main__': sys.exit(main())
