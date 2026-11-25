#!/usr/bin/env python3
"""reeval_manifest.py [DIA...] -- (CONTRATO_CXB60_REEVAL_PASST_V4_v2_23nov sec.5b y C9 (c)) manifest por dia de la REEVAL passT_v4 de CXB60: clase del dia, estado, sha de entradas (dec_/res_/coverage_) y cobertura (SOLO claves de conteo/cobertura de coverage_D.json; nunca res_/pnl/EV).
Clases: 13..17-Nov = EXPLORATORIO (tabla aparte, descriptiva); >=18-Nov = CONFIRMATORIO (ciego: este script NO abre res_ ni dec_ de esos dias, solo hashea ficheros y lee coverage). Firma chief 23-Nov: 19..22-Nov INCOMPLETE para la reeval (passT_v4 lee libro5_tx como fallback; cobertura libro5_tx 19-Nov 0,719).
El reproceso passT_v4 en si (adaptador dec_/maker_ms -> b_policy_sim) NO esta implementado: estado PENDIENTE_REPROCESO. Escribe out_reeval/manifest_reeval_D.json (atomico). 0 ordenes, 0 red."""
import os, sys, json, hashlib, time
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
DL = os.environ.get('CXB60_DL', '/root/polymarket-research-datalogs/cxb60_dryrun/'); OUT = os.environ.get('REEVAL_OUT', HERE + 'out_reeval/')
EXPLORATORIOS = ('2026-11-13', '2026-11-14', '2026-11-15', '2026-11-16', '2026-11-17'); INCOMPLETOS_LIBRO5TX = ('2026-11-19', '2026-11-20', '2026-11-21', '2026-11-22')
CLAVES_COBERTURA = ('dia', 'procesados', 'esperados_teoricos', 'esperados_vistos', 'cobertura', 'dia_valido', 'dia_valido_btc', 'dia_valido_4monedas', 'dia_completo', 'por_moneda', 'saltados')

def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def clase_dia(d): return 'EXPLORATORIO' if d in EXPLORATORIOS else ('CONFIRMATORIO' if d >= '2026-11-18' else 'FUERA_DE_RANGO')

def manifest_dia(d, dl=None):
    dl = dl or DL; cl = clase_dia(d); m = dict(dia=d, clase=cl, t=time.strftime('%FT%TZ', time.gmtime()), contrato='CONTRATO_CXB60_REEVAL_PASST_V4_v2_23nov')
    ins = {}
    for n in (f'dec_{d}.csv.gz', f'res_{d}.csv.gz', f'coverage_{d}.json'):
        p = dl + n; ins[n] = dict(existe=os.path.exists(p), bytes=(os.path.getsize(p) if os.path.exists(p) else None), sha256=(sha(p) if os.path.exists(p) else None))     # solo hash: no se abre el contenido de dec_/res_
    m['inputs'] = ins; cp = dl + f'coverage_{d}.json'
    if os.path.exists(cp):
        try: c = json.load(open(cp)); m['cobertura'] = {k: c[k] for k in CLAVES_COBERTURA if k in c}
        except Exception as ex: m['cobertura'] = dict(error=repr(ex))
    if cl == 'FUERA_DE_RANGO': m.update(estado='FUERA_DE_RANGO', motivo='dec_ pre-12-Nov no existen; la reeval cubre 13-Nov en adelante')
    elif d in INCOMPLETOS_LIBRO5TX: m.update(estado='INCOMPLETE', motivo='firma chief 23-Nov: passT_v4 lee libro5_tx (fallback del sello de relleno) y libro5_tx estuvo en pausa 19-23 Nov (cobertura 19-Nov 0,719)')
    elif not all(v['existe'] for v in ins.values()): m.update(estado='PENDING', motivo='faltan entradas del dia')
    else: m.update(estado='PENDIENTE_REPROCESO', motivo='adaptador passT_v4 (dec_/maker_ms -> b_policy_sim) no implementado')
    return m

def escribe(d, dl=None, out=None):
    out = out or OUT; os.makedirs(out, exist_ok=True); m = manifest_dia(d, dl); p = out + f'manifest_reeval_{d}.json'
    with open(p + '.tmp', 'w') as f: json.dump(m, f, indent=1)
    os.replace(p + '.tmp', p); return m

if __name__ == '__main__':
    for d in (sys.argv[1:] or [f'2026-11-{x:02d}' for x in range(13, 23)]): m = escribe(d); print(d, m['clase'], m['estado'])
