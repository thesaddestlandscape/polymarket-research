#!/usr/bin/env python3
"""huecos_real.py DIA [DIA...] -- ESPEC E8(b) / contrato v2 (f); DECLARACION DE FEED Y RELOJ en huecos_cxb60.py (filas q/t de todos los tokens de la moneda, reloj de RECEPCION: q c[7], t recv; ventana unica 332 s): prueba del detector de huecos A NIVEL DE FICHERO maker_ms con datos reales (dias NO ciegos <=17-Nov). Lee maker_ms_DIA_*.csv.gz de datalogs (o del volumen maker_ms_crudo), construye los segundos con mensajes q/t por MONEDA (token->moneda
desde las filas k) y mide vac_max por mercado (las filas 'mkt' de dec_DIA.csv.gz: moneda, fin) con la misma ventana que el runner (332 s); compara con el vac_max_s que registro el runner. Aceptacion: p50 nuevo < 10 s (el del runner ~55 s). NO mira EV/PnL: solo huecos. Escribe out/huecos_real_DIA.json en rf5_btc? no: en el directorio de la reeval (out_reeval/). Se niega a dias >= 18-Nov.
Pesado en lectura (zcat de unos GB/dia): por cron_pesado, nice 19, ionice -c3; RAM baja (arrays de segundos por moneda)."""
import os, sys, glob, json, csv, subprocess, gzip
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE); sys.path.insert(0, HERE + '../dryrun/')
import huecos_cxb60 as H
DL = '/root/polymarket-research-datalogs/'; DEC = DL + 'cxb60_dryrun/'; OUT = HERE + 'out_reeval/'; VENT = H.PRE_S; CRUDO = '/mnt/HC_Volume_106538179/maker_ms_crudo/'; MIN_BYTES = 1024      # una sola ventana (332 s); ficheros < 1 KiB = cabecera vacia. OJO: los maker_ms_* de datalogs son ENLACES al volumen (ls -l muestra 73 B = longitud del enlace; getsize sigue el enlace)

def ficheros_dia(d, dl=None, crudo=None):
    """maker_ms_D_*.csv.gz REALES del dia: union de datalogs y del volumen crudo, deduplicada por nombre (gana el de mayor tamano) y SIN ficheros vacios (< 1 KiB) ni enlaces rotos (OSError)."""
    best = {}
    for base in (dl or DL, crudo or CRUDO):
        for f in glob.glob(base + f'maker_ms_{d}_*.csv.gz'):
            try: sz = os.path.getsize(f)
            except OSError: continue
            if sz >= MIN_BYTES and sz > best.get(os.path.basename(f), (0, None))[0]: best[os.path.basename(f)] = (sz, f)
    return [v[1] for _, v in sorted(best.items())]

def segundos_por_moneda(d):
    """{coin: bool array 86400+7200 (indice = segundo del dia UTC; d-1/d+1 recortados)} y n de filas por tipo. awk emite 'moneda,seg' para q (rx col 8) y t (recv col 7) de tokens conocidos (filas k: id,c1=coin)."""
    fs = ficheros_dia(d)
    if not fs: return None, {}
    import calendar, time; d0 = calendar.timegm(time.strptime(d, '%Y-%m-%d')); A = {}; n = {}
    for f in fs:
        awk = r"""BEGIN{FS=","} $1=="k"{c[$3]=$4; next} ($1=="q" && NF>=8){r=$8+0} ($1=="t" && NF>=7){r=$7+0} ($1=="q" || $1=="t"){ if (($3 in c) && r>0) print c[$3] "," int(r/1000) }"""
        p = subprocess.Popen(['bash', '-c', f"zcat '{f}' 2>/dev/null | awk '{awk}'"], stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
        for ln in p.stdout:
            c, s = ln.rstrip('\n').split(','); a = A.setdefault(c.lower(), np.zeros(86400 + 14400, bool)); i = int(s) - (d0 - 7200)
            if 0 <= i < len(a): a[i] = True; n[c] = n.get(c, 0) + 1
        p.wait()
    return (A, d0), n

def mercados_dec(d):
    import io
    p = DEC + f'dec_{d}.csv.gz'
    if not os.path.exists(p): return []
    out = []
    with gzip.open(p, 'rt', errors='replace') as fh:
        for ln in fh:
            if not ln.startswith('mkt,'): continue
            r = next(csv.reader([ln]))
            try: det = json.loads(r[21]); out.append(dict(coin=r[5].lower(), fin=int(r[7]), vac_runner=det.get('vac_max_s'), hueco_runner=det.get('hueco_feed')))
            except Exception: continue
    return out

def adaptador_mercados(d, por_mercado, out=None):
    """ADAPTADOR de la reevaluacion CXB60: escribe out_reeval/huecos_mercados_D.json = por mercado (moneda, fin) su vac_max_s medido en maker_ms y `excluir` (vac_max >= 5 s, huecos_cxb60.excluye_mercados) que el informe de la reeval usa en lugar del `hueco_feed` degenerado del runner. Atomico; sin EV/PnL."""
    out = out or OUT; os.makedirs(out, exist_ok=True); filas = [dict(m, excluir=bool(H.excluye_mercados({0: m['vac_max_s']}))) for m in por_mercado]
    p = out + f'huecos_mercados_{d}.json'; json.dump(dict(dia=d, pre_s=VENT, umbral_s=H.UMBRAL_S, n=len(filas), n_excluir=sum(f['excluir'] for f in filas), mercados=filas), open(p + '.tmp', 'w')); os.replace(p + '.tmp', p); return p

def main(d):
    if d >= '2026-11-18': raise SystemExit('dia ciego: prohibido')
    seg, n = segundos_por_moneda(d)
    if seg is None: return dict(dia=d, estado='SIN_MAKER_MS')
    A, d0 = seg; M = mercados_dec(d); nuevo = []; runner = []
    por_mercado = []; S = {}
    for m in M:
        a = A.get(m['coin'])
        if a is None or m['vac_runner'] is None: continue
        if m['coin'] not in S: S[m['coin']] = set((np.nonzero(a)[0] + (d0 - 7200)).tolist())
        v = H.vac_max_seg(S[m['coin']], m['fin'], VENT); nuevo.append(v); runner.append(m['vac_runner']); por_mercado.append(dict(coin=m['coin'], fin=m['fin'], vac_max_s=v))
    nuevo = np.array(nuevo); runner = np.array(runner, float); pc = lambda x, q: (float(np.percentile(x, q)) if len(x) else None)
    res = dict(dia=d, estado='OK', n_mercados=int(len(nuevo)), filas_por_moneda=n, vac_max_nuevo=dict(p50=pc(nuevo, 50), p90=pc(nuevo, 90), max=pc(nuevo, 100)), vac_max_runner=dict(p50=pc(runner, 50), p90=pc(runner, 90)), frac_hueco_ge5_nuevo=(float((nuevo >= 5).mean()) if len(nuevo) else None),
               frac_hueco_ge5_runner=(float((runner >= 5).mean()) if len(runner) else None), aceptacion_p50_menor_10s=bool(len(nuevo) and pc(nuevo, 50) < 10))
    res['ficheros_maker_ms'] = [dict(nombre=os.path.basename(f), bytes=os.path.getsize(f)) for f in ficheros_dia(d)]; res['pre_s'] = VENT; res['feed'] = 'filas q+t de todos los tokens de la moneda (k), reloj de recepcion'
    os.makedirs(OUT, exist_ok=True); json.dump(res, open(OUT + f'huecos_real_{d}.json', 'w'), indent=1)
    adaptador_mercados(d, por_mercado); return res

if __name__ == '__main__':
    for d in sys.argv[1:]: print(json.dumps(main(d)))
