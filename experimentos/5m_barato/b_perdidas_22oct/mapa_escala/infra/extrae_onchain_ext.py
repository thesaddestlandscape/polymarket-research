#!/usr/bin/env python3
"""extrae_onchain_ext.py - re-extraccion/extension diaria de rellenos on-chain por marco (5min,15min,60min,240min,24h) REUTILIZANDO
extraer_onchain_15m.extraer() del repo (no se reescribe: se importa y se le inyecta un mapa de tokens robusto, ver tokmap.py).
Causa raiz del hueco 22-Oct: el mapa de tokens salia del m15_registro del dia, que quedo en .tmp truncado (extraer_registro_15m no captura
zlib.error en un maker_ms corrupto) -> 3.550 de ~7.000 tokens 5m -> m5_onchain_22 de 2 MB en vez de ~125 MB.
Uso: extrae_onchain_ext.py DIA [DIA ...] [--marcos 5min,15min,...] [--forzar]   (idempotente: solo rehace lo que falta o esta truncado)
Salida: volumen/{m5,m15}_onchain (existentes, 60 d por archivo_volumen), volumen/agentes_datos/mapa_infra/{m60,m240,m24h}_onchain (nuevos, retencion propia 60 d).
Manifest: datalogs/mapa_infra/runs/extract_<DIA>.json. Codigos de salida: 0 todo COMPLETE/ya existia; 3 algun PARTIAL/BLOCKED; 1 fallo."""
import sys, io, re, os, json, contextlib, statistics, argparse, datetime as dt
sys.path.insert(0, '/root/polymarket-research')
from pathlib import Path
import infra_lib as L, tokmap as T
MARCOS = ['5min', '15min', '60min', '240min', '24h']
ESPERADO = {'5min': 6500, '15min': 2200}   # tokens/dia observados 6.986-7.022 y 2.348-2.364 (18..21-Oct)
FRAC_TRUNC = 0.6        # fichero 5m/15m < 60 % de la mediana de los 7 dias previos = truncado
def carpeta(m): return L.VOL / f'{L.PREF[m]}_onchain' if m in ('5min', '15min') else L.AGENT / 'mapa_infra' / f'{L.PREF[m]}_onchain'   # 5m/15m: carpetas existentes del volumen
def destino(m, d): return carpeta(m) / f'{L.PREF[m]}_onchain_{d}.csv.gz'
def estado_previo(m, d):
    """None si falta; 'ok' si existe y plausible; 'truncado' si es <60 % de la mediana de los 7 dias previos (solo 5m/15m)."""
    f = destino(m, d)
    if not f.exists(): return None
    if m not in ('5min', '15min'): return 'ok'
    d0 = dt.date.fromisoformat(d); prev = []
    for k in range(1, 8):
        g = destino(m, (d0 - dt.timedelta(days=k)).isoformat())
        if g.exists(): prev.append(g.stat().st_size)
    if len(prev) >= 3 and f.stat().st_size < FRAC_TRUNC * statistics.median(prev): return 'truncado'
    return 'ok'
def retencion(m, dias=60):
    lim = (dt.date.today() - dt.timedelta(days=dias)).isoformat()
    if m in ('5min', '15min'): return           # las gestiona archivo_volumen.py
    for f in carpeta(m).glob('*.csv.gz'):
        r = re.search(r'(\d{4}-\d{2}-\d{2})', f.name)
        if r and r.group(1) < lim: f.unlink()
def extrae_dia(d, marcos, forzar=False):
    import extraer_onchain_15m as EO
    src = L.ROOT / f'onchain_fills_{d}.csv.gz'
    man = dict(dia=d, inicio=L.now(), marcos={}, fuente_onchain=str(src), estado='RUNNING')
    if not src.exists():
        man.update(estado='BLOCKED', motivo='sin onchain_fills (rotado o no generado)'); L.atomic_json(L.INFRA / 'runs' / f'extract_{d}.json', man); return man
    man['fuente_sha16'] = L.sha_file(src); man['fuente_bytes'] = src.stat().st_size
    toks, info = T.tokens_dia(d, [m for m in marcos if m in ('5min', '15min', '60min')]); man['tokens_info'] = info
    gam = None
    for m in marcos:
        prev = estado_previo(m, d); r = dict(previo=prev)
        if prev == 'ok' and not forzar: r['estado'] = 'COMPLETE(ya existia)'; man['marcos'][m] = r; continue
        if m in ('240min', '24h'):
            if gam is None:
                try: gam, gmeta = T.gamma_dia(d); man['gamma'] = {k: v for k, v in gmeta.items() if k != 'tokens'}
                except Exception as e: gam = False; man['gamma_error'] = f'{type(e).__name__}: {e}'
            if gam is False: r['estado'] = 'BLOCKED'; r['motivo'] = 'gamma no disponible'; man['marcos'][m] = r; continue
            ids = {t for t, v in gam.items() if v[1] == m}
        else:
            ids = set(toks.get(m, {}))
        r['n_tokens'] = len(ids)
        if not ids: r['estado'] = 'BLOCKED'; r['motivo'] = 'mapa de tokens vacio (fail-closed)'; man['marcos'][m] = r; continue
        EO.DL = L.ROOT; EO.MARCO, EO.PREF, EO.OUT = m, L.PREF[m], carpeta(m); EO.tokens_15m = lambda dia, _i=ids: _i      # inyeccion del mapa
        carpeta(m).mkdir(parents=True, exist_ok=True)
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf): EO.extraer(d, forzar=True)
        except Exception as e:
            r['estado'] = 'FAILED'; r['motivo'] = f'{type(e).__name__}: {e}'; man['marcos'][m] = r
            tmp = destino(m, d).with_suffix('.tmp')
            if tmp.exists(): tmp.unlink()
            continue
        out = buf.getvalue().strip(); r['extractor'] = out; mm = re.search(r'([\d,]+) filas -> ([\d,]+)', out)
        if not mm or not destino(m, d).exists(): r['estado'] = 'FAILED'; r['motivo'] = 'el extractor no genero fichero'; man['marcos'][m] = r; continue
        n_in, n_out = int(mm.group(1).replace(',', '')), int(mm.group(2).replace(',', ''))
        r.update(n_in=n_in, n_out=n_out, bytes=destino(m, d).stat().st_size, sha16=L.sha_file(destino(m, d)))
        # cobertura: filas leidas del on-chain vs mediana de los dias previos; tokens truncados -> PARTIAL
        hist = [x for x in (L.read_json(L.INFRA / 'runs' / f'extract_{(dt.date.fromisoformat(d) - dt.timedelta(days=k)).isoformat()}.json', {}).get('marcos', {}).get(m, {}).get('n_in') for k in range(1, 8)) if x]
        r['n_in_mediana_previos'] = statistics.median(hist) if len(hist) >= 3 else None
        if r['n_in_mediana_previos'] and n_in < 0.85 * r['n_in_mediana_previos']: r['estado'] = 'PARTIAL'; r['motivo'] = 'on-chain de origen con menos filas que lo habitual'
        elif m in ESPERADO and len(ids) < ESPERADO[m]: r['estado'] = 'PARTIAL'; r['motivo'] = f'mapa de tokens incompleto ({len(ids)} < {ESPERADO[m]} esperados)'
        elif m in toks and info['truncados']: r['estado'] = 'PARTIAL'; r['motivo'] = f"maker_ms corrupto(s) {info['truncados']}: mapa de tokens posiblemente incompleto"
        elif n_out == 0: r['estado'] = 'PARTIAL'; r['motivo'] = '0 filas de salida'
        else: r['estado'] = 'COMPLETE'
        man['marcos'][m] = r
    for m in marcos: retencion(m)
    man['fin'] = L.now()
    peor = [r['estado'] for r in man['marcos'].values()]
    man['estado'] = 'FAILED' if 'FAILED' in peor else ('PARTIAL' if any(s in ('PARTIAL', 'BLOCKED') for s in peor) else 'COMPLETE')
    L.atomic_json(L.INFRA / 'runs' / f'extract_{d}.json', man)
    return man
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('dias', nargs='+'); ap.add_argument('--marcos', default=','.join(MARCOS)); ap.add_argument('--forzar', action='store_true')
    a = ap.parse_args(); rc = 0
    for d in a.dias:
        m = extrae_dia(d, a.marcos.split(','), a.forzar)
        L.log(f"{d}: {m['estado']} " + ' '.join(f"{k}={v['estado']}({v.get('n_out','-')})" for k, v in m['marcos'].items()))
        rc = max(rc, {'COMPLETE': 0, 'PARTIAL': 3, 'BLOCKED': 3, 'FAILED': 1}.get(m['estado'], 1))
    sys.exit(rc)
