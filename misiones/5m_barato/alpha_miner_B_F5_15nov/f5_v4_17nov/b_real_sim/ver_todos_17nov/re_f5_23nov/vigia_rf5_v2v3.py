#!/usr/bin/env python3
"""vigia_rf5_v2v3.py [--telegram] [...]  (28-Nov, ADENDA_V2V3_rf5.md; ANEXO2 §3). WRAPPER NUEVO de vigia_rf5.py (SELLADO: se IMPORTA, no se modifica). Mismo comportamiento y mismos avisos R1-R10 + R11 nuevo y una linea por dia de la cadena on-chain POR MONEDA (cadena_v2v3):
R11: dia >= 23-Nov con manifest RF5 COMPLETE cuya cadena para ETH/SOL/XRP no es COMPLETE en estado_monedas_DIA.json (p.ej. V3 sin indexar): la muestra de ese dia no puede mezclar V2-solo con doble sello. Firma estable (dia, moneda), sin valores recalculados.
Los dias <= 22-Nov (solo V2) quedan exactamente como en el vigia sellado. No se programa en cron: lo decide el chief tras firmar la adenda."""
import os, sys, json
sys.dont_write_bytecode = True
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, HV)
import vigia_rf5 as V
ESTADO = '/root/polymarket-research-datalogs/exp5bis_27nov/estado_monedas_%s.json'
MONEDAS = ('eth', 'sol', 'xrp')
DESDE_V3 = '2026-11-23'


def estado_cadena(d, ruta=None):
    try: j = json.load(open((ruta or ESTADO) % d))
    except (OSError, ValueError): return None
    return {c: (j.get(c) or {}).get('estado') for c in MONEDAS}


_resumen0, _avisos0 = V.resumen_texto, V.avisos


def resumen_v2v3(est, hoy_=None):
    base = _resumen0(est, hoy_); extra = []
    for d in V.dias_calendario(hasta=hoy_):
        if d < DESDE_V3: continue
        e = estado_cadena(d); extra.append(f'  {d}: cadena on-chain V2+V3 ' + ('SIN estado_monedas' if e is None else ', '.join(f'{c}={e[c]}' for c in MONEDAS)))
    return base + ('\nCadena V2+V3 por moneda (cadena_v2v3):\n' + '\n'.join(extra) if extra else '')


def avisos_v2v3(est, hb, libre_gb, hoy_=None, ahora=None, fuentes=None):
    A = _avisos0(est, hb, libre_gb, hoy_, ahora, fuentes)
    for d in V.dias_calendario(hasta=hoy_):
        m = est.get(d)
        if d < DESDE_V3 or not m or m.get('status') != 'COMPLETE': continue
        e = estado_cadena(d)
        for c in MONEDAS:
            if e is None or e.get(c) != 'COMPLETE': A.append((f'R11_cadena_{d}_{c}', f"RF5: dia {d} COMPLETE pero la cadena on-chain de {c.upper()} no es COMPLETE ({None if e is None else e.get(c)}): no mezclar V2-solo con doble sello."))
    return A


V.resumen_texto, V.avisos = resumen_v2v3, avisos_v2v3

if __name__ == '__main__':
    sys.exit(V.main(sys.argv[1:]))
