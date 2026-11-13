#!/usr/bin/env python3
"""juez_calma_v3_dia.py [DIA] [--desde 2026-11-02] [--out DIR] [--run-dias RUTA] [--dev-out DIR] [--libro5 DIR] [--forzar] -- juez forward Calma-T1 con SELLO v3, EN PARALELO al forward actual (forward_calma_diario.sh -> esc_dec2.py, dev, NO se modifica).
Para DIA (por defecto ayer UTC): 1) exige que el forward original ya haya dejado dev out/dec2_<D>.pkl y dec3s100_<D>.pkl (si no: BLOCKED, no se calcula nada); 2) chequeo_libro5tx.py (gz abren, cobertura 24 h, huecos > 1 min: los huecos se REGISTRAN
(`libro5tx.ok_cobertura_24h`) y solo un gz con error o 0 eventos bloquea -- ver nota estructural en el manifiesto); 3) run_dias.sh <D> (idempotente: esc_dec2_v3 sale si el pkl existe; calcula dec2v3 y dec3v3s100); 4) ana_dec_v3_b.py (compara vs G0 sobre los dias comunes desde --desde)
-> out/resumen_fwd_v3_<D>.txt con `sello_print=v3`; 5) out/manifest_juez_v3_<D>.json (estado COMPLETE|PARTIAL|FAILED|BLOCKED, codigo hasheado, entradas, cobertura de dias esperados/procesados/faltan, tabla G0/T1 parseada).
rc: 0 COMPLETE, 1 FAILED/PARTIAL, 4 BLOCKED (forward original sin terminar), 5 BLOCKED (libro5_tx ilegible/vacio). Solo lectura de datalogs; 0 ordenes; sin red. Pesado: lanzar via scripts/cron_pesado.sh, fuera de 06-09Z (run_dias.sh usa guard_rss)."""
import os, sys, re, json, glob, time, hashlib, argparse, subprocess, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
import chequeo_libro5tx as CK
L2 = os.path.dirname(os.path.dirname(HERE.rstrip('/'))) + '/'
DEVDC = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/'
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16] if os.path.exists(p) else None
NOTA_HUECOS = ('Los libro5_tx reales (11 y 12-Nov) tienen ~5 min sin eventos alrededor de xx:55 de las horas 04/08/12/16/20/24 UTC (cierre de mercados 4 h): con el umbral de 1 min el check estricto sale ok=false TODOS los dias; '
               'se registra (n_huecos, gap_max) pero no bloquea el calculo. No se ha investigado si es ausencia de prints (periodo sin mercado) o perdida de captura.')


def parse_tabla(txt, etiqueta):
    """Filas de la seccion `===== sello <etiqueta>` de ana_dec_v3_b: {variante: dict(rellenos, EUR, EV, dEUR_vs_G0)}."""
    i = txt.find(f'===== sello {etiqueta}'); out = {}
    if i < 0: return out
    for ln in txt[i:].split('\n')[1:]:
        if ln.startswith('=====') and out: break
        t = ln.split()
        if len(t) >= 5 and re.match(r'^[A-Za-z]', t[0]) and t[0] != 'variante':
            try: out[t[0]] = dict(rellenos=int(t[1]), EUR=float(t[2]), EV=float(t[3]), dEUR_vs_G0=float(t[4]))
            except ValueError: continue
    return out


def dias_rango(d0, d1): a = dt.date.fromisoformat(d0); b = dt.date.fromisoformat(d1); return [(a + dt.timedelta(i)).isoformat() for i in range((b - a).days + 1)]


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument('dia', nargs='?'); ap.add_argument('--desde', default='2026-11-02'); ap.add_argument('--out', default=HERE + 'out/'); ap.add_argument('--run-dias', default=HERE + 'run_dias.sh')
    ap.add_argument('--dev-out', default=DEVDC + 'out/'); ap.add_argument('--libro5', default=CK.DIR); ap.add_argument('--forzar', action='store_true', help='calcula aunque libro5_tx no pase el check de lectura (queda anotado)')
    ap.add_argument('--ana', default=HERE + 'ana_dec_v3_b.py'); ap.add_argument('--reintentos', type=int, default=6); ap.add_argument('--sin-subprocesos', action='store_true', help='solo tests: no lanza run_dias ni ana'); a = ap.parse_args(argv)
    dia = a.dia or (dt.datetime.now(dt.timezone.utc).date() - dt.timedelta(days=1)).isoformat(); out = a.out.rstrip('/') + '/'; dev = a.dev_out.rstrip('/') + '/'; os.makedirs(out, exist_ok=True)
    mf = out + f'manifest_juez_v3_{dia}.json'; t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    man = dict(job='juez_calma_v3_dia', dia=dia, sello_print='v3', estado='RUNNING', inicio=t0, desde=a.desde, parametros=dict(out=out, dev_out=dev, run_dias=a.run_dias, libro5=a.libro5, forzar=a.forzar),
               codigo={n: sha(p) for n, p in [('run_dias.sh', HERE + 'run_dias.sh'), ('esc_dec2_v3.py', L2 + 'calma_v3/esc_dec2_v3.py'), ('esc_dec2.py(dev)', DEVDC + 'esc_dec2.py'), ('stamp_v3.py', L2 + 'stamp_v3.py'),
                                                          ('ana_dec_v3_b.py', HERE + 'ana_dec_v3_b.py'), ('ana_dec.py(dev)', DEVDC + 'ana_dec.py'), ('chequeo_libro5tx.py', HERE + 'chequeo_libro5tx.py'), ('juez_calma_v3_dia.py', HERE + 'juez_calma_v3_dia.py')]},
               comando=' '.join(['python3', '-I', HERE + 'juez_calma_v3_dia.py', dia, '--desde', a.desde]))
    def fin(estado, rc, **kw):
        man.update(estado=estado, fin=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rc=rc, **kw); json.dump(man, open(mf + '.tmp', 'w'), indent=1, default=str); os.replace(mf + '.tmp', mf)
        print(json.dumps(dict(dia=dia, estado=estado, rc=rc, **{k: v for k, v in kw.items() if k in ('motivo', 'cobertura_dias')}), default=str)); return rc
    # 1) forward original terminado
    falta = [f for f in (f'dec2_{dia}.pkl', f'dec3s100_{dia}.pkl') if not os.path.exists(dev + f)]
    if falta: return fin('BLOCKED', 4, motivo=f'el forward original (forward_calma_diario.sh) aun no dejo {falta} en {dev}')
    # 2) entrada libro5_tx
    ck = CK.chequeo(dia, a.libro5); man['libro5tx'] = dict(ok_cobertura_24h=ck['ok'], gap_max_ms=ck.get('gap_max_ms'), n_huecos=ck.get('n_huecos'), eventos=ck['eventos_en_dia'], ficheros_gz=ck['ficheros_gz'], ficheros_con_error=ck['ficheros_con_error'], huecos=ck.get('huecos'), nota=NOTA_HUECOS)
    if (ck['ficheros_con_error'] or ck['eventos_en_dia'] == 0) and not a.forzar: return fin('BLOCKED', 5, motivo=f"libro5_tx ilegible o vacio: {ck['ficheros_con_error'] or 'sin eventos'}")
    # 3) calculo v3 (idempotente)
    pk = [out + f'dec2v3_{dia}.pkl', out + f'dec3v3s100_{dia}.pkl']
    if not a.sin_subprocesos and not all(os.path.exists(p) for p in pk):
        # run_dias.sh usa guard_rss (espera <=5 min a load5<6 y MemAvailable>=2500 MB) y su propio `rc=$?` del log siempre sale 0: se REINTENTA mientras falten pkl (idempotente) y se verifica por existencia de salidas
        man['run_dias_intentos'] = 0
        for _ in range(a.reintentos):
            if all(os.path.exists(p) for p in pk): break
            r = subprocess.run(['bash', a.run_dias, dia], capture_output=True, text=True, timeout=7200); man['run_dias_rc'] = r.returncode; man['run_dias_intentos'] += 1
    man['salidas'] = {os.path.basename(p): (os.path.getsize(p) if os.path.exists(p) else None) for p in pk}
    if not all(os.path.exists(p) and os.path.getsize(p) > 0 for p in pk): return fin('FAILED', 1, motivo=f'faltan salidas v3 {[os.path.basename(p) for p in pk if not os.path.exists(p)]} (ver out/run_*.log de run_dias.sh)')
    # 4) resumen vs G0
    txt = {}
    if not a.sin_subprocesos:
        for tn, tv in (('dec2v3', 'dec2'), ('dec3v3s100', 'dec3s100')):
            r = subprocess.run(['nice', '-n', '19', sys.executable, '-I', a.ana, tn, tv, a.desde, dia], capture_output=True, text=True, timeout=1800, cwd=HERE); txt[tn] = r.stdout if r.returncode == 0 else f'ERROR rc={r.returncode}\n{r.stderr[-800:]}'
        cab = f'sello_print=v3 (stamp_v3; engine legacy sin dedupe) | dia={dia} | desde={a.desde} | generado={t0}\n'
        open(out + f'resumen_fwd_v3_{dia}.txt', 'w').write(cab + '\n'.join(f'#### {k} (vs sello VIEJO del forward original)\n{v}' for k, v in txt.items()))
        man['resumen'] = out + f'resumen_fwd_v3_{dia}.txt'; man['tabla_dec2v3'] = parse_tabla(txt['dec2v3'], 'V3'); man['tabla_dec2_viejo'] = parse_tabla(txt['dec2v3'], 'VIEJO')
        man['tabla_dec3v3s100'] = parse_tabla(txt['dec3v3s100'], 'V3')
        if any(v.startswith('ERROR') for v in txt.values()) or not man['tabla_dec2v3']: return fin('PARTIAL', 1, motivo='ana_dec_v3_b fallo o tabla vacia (ver resumen)')
    esp = dias_rango(a.desde, dia); ok = [d for d in esp if os.path.exists(out + f'dec2v3_{d}.pkl') and os.path.exists(out + f'dec3v3s100_{d}.pkl') and os.path.exists(dev + f'dec2_{d}.pkl')]
    cov = dict(esperados=len(esp), procesados=len(ok), faltan=[d for d in esp if d not in ok], nota='dias comunes v3 + forward original; 02-Nov = dia 0; CONFIRMA exige >=10 dias (PREREG_CALMA_T1)')
    return fin('COMPLETE' if not cov['faltan'] else 'PARTIAL', 0 if not cov['faltan'] else 1, cobertura_dias=cov, motivo=None if not cov['faltan'] else f"faltan dias {cov['faltan']} (calma v3 de dias previos sin recalcular)")


if __name__ == '__main__': sys.exit(main())
