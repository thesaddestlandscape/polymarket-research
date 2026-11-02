#!/usr/bin/env python3
"""etiquetador_mid_ventana_5m.py (D-FUERTE ronda 3, 24-Oct) - guarda el mid y el bid/ask del token YES (Up) de cada mercado 5min y 15min a T=60/120/180/240 s de CADA ventana 5m
(el 15m se anota en los 3 slots de 5 min que contiene), con la hora de RECEPCION (ms) de la ultima cotizacion <= checkpoint. PASIVO: lee los registros ms que ya existen
(m5_registro_D y m15_registro_D del volumen, escritos por extraer_registro_*; ninguna conexion nueva, no toca observadores_fase0). Salida:
/root/polymarket-research-datalogs/mid_ventana_5m/mid_ventana_5m_D.csv.gz (~0,5 MB/dia, fuera de git). Un checkpoint sin cotizacion en los LB_S s previos sale con bid/ask vacios (missing, NO 0).
Uso: etiquetador_mid_ventana_5m.py [--dia YYYY-MM-DD] [--force]   (defecto: ayer UTC). Cron propuesto: 25 4 * * * (tras extraer_registro 03:45/04:00)."""
import sys, os, gzip, subprocess, datetime as dt, tempfile, csv, collections
VOL = '/mnt/HC_Volume_106538179'; OUT = '/root/polymarket-research-datalogs/mid_ventana_5m'; TS = (60, 120, 180, 240); LB_S = 120
def _num(x):
    try: float(x); return True
    except ValueError: return False
def main():
    a = sys.argv[1:]; force = '--force' in a
    dia = a[a.index('--dia') + 1] if '--dia' in a else (dt.datetime.now(dt.timezone.utc).date() - dt.timedelta(days=1)).isoformat()
    os.makedirs(OUT, exist_ok=True); dst = f'{OUT}/mid_ventana_5m_{dia}.csv.gz'
    if os.path.exists(dst) and not force: print('ya existe', dst); return 0
    files = [f'{VOL}/m5_registro/m5_registro_{dia}.csv.gz', f'{VOL}/m15_registro/m15_registro_{dia}.csv.gz']; files = [f for f in files if os.path.exists(f)]
    if not files: print('FALTAN registros de', dia); return 2
    tok = {}
    for f in files:
        p = subprocess.run(['bash', '-c', "zcat '%s' | awk -F, '$1==\"k\" && ($5==\"5min\"||$5==\"15min\") && $8==\"YES\"{print $3\",\"$4\",\"$5\",\"substr($7,1,19)}'" % f], capture_output=True, text=True)
        for l in p.stdout.splitlines():
            t, c, tf, e = l.split(','); tok[t] = (c, tf, int(dt.datetime.strptime(e, '%Y-%m-%d %H:%M:%S').replace(tzinfo=dt.timezone.utc).timestamp()))
    if not tok: print('sin tokens k'); return 3
    tmp = tempfile.NamedTemporaryFile('w', dir=OUT, suffix='.map', delete=False); [tmp.write(f'{t},{tf},{e}\n') for t, (c, tf, e) in tok.items()]; tmp.close()
    awk = r'''BEGIN{FS=","} NR==FNR{ tf[$1]=$2; en[$1]=$3; next }
$1=="q" && ($3 in tf){ r=$8; x=(r/1000)%300; if (x>=240+1) next; e=en[$3]; n=(tf[$3]=="5min")?1:3
  for(j=0;j<n;j++){ s=(tf[$3]=="5min")?e-300:e-900+300*j; for(i=1;i<=4;i++){ T=60*i; cp=(s+T)*1000; if(r<=cp && r>cp-LB*1000){ k=$3","s","T; if(r>br[k]){br[k]=r; bb[k]=$4; ba[k]=$5} } } } }
END{ for(k in br) print k","br[k]","bb[k]","ba[k] }'''
    best = {}
    for f in files:
        sc = tempfile.NamedTemporaryFile('w', dir=OUT, suffix='.awk', delete=False); sc.write(awk); sc.close()
        p = subprocess.run(['bash', '-c', "zcat '%s' | nice -n 19 awk -v LB=%d -f '%s' '%s' -" % (f, LB_S, sc.name, tmp.name)], capture_output=True, text=True); os.unlink(sc.name)
        if p.returncode != 0: print('awk fallo', f, p.stderr[:300]); os.unlink(tmp.name); return 4
        for l in p.stdout.splitlines():
            t, s, T, r, b, ask = l.split(','); k = (t, int(s), int(T))
            if k not in best or int(r) > best[k][0]: best[k] = (int(r), b, ask)
    os.unlink(tmp.name); n_ok = n_all = 0; rows = []
    for t, (c, tf, e) in tok.items():
        for s in ([e - 300] if tf == '5min' else [e - 900 + 300 * j for j in range(3)]):
            if not (dia + 'T00:00:00' <= dt.datetime.fromtimestamp(s, dt.timezone.utc).isoformat()[:19] < (dt.date.fromisoformat(dia) + dt.timedelta(days=1)).isoformat() + 'T00:00:00'): continue
            for T in TS:
                n_all += 1; v = best.get((t, s, T)); cp = (s + T) * 1000
                if v: n_ok += 1; ok2 = _num(v[1]) and _num(v[2]); mid = '%.4f' % ((float(v[1]) + float(v[2])) / 2) if ok2 else ''; rows.append((dia, c, tf, e, s, (s // 300 % 3) if tf == '15min' else '', T, v[0], cp - v[0], v[1] if _num(v[1]) else '', v[2] if _num(v[2]) else '', mid))
                else: rows.append((dia, c, tf, e, s, (s // 300 % 3) if tf == '15min' else '', T, '', '', '', '', ''))
    rows.sort(key=lambda r: (r[4], r[1], r[2], r[6]))
    with gzip.open(dst + '.tmp', 'wt', newline='') as fh:
        w = csv.writer(fh, lineterminator='\n'); w.writerow(['dia','coin','tf','fin_mercado_s','slot_inicio_s','slot15','T_s','recv_ms','edad_ms','bid_yes','ask_yes','mid_yes']); w.writerows(rows)
    os.replace(dst + '.tmp', dst); print(f'{dia}: checkpoints {n_all}, con cotizacion {n_ok} ({100*n_ok/max(n_all,1):.1f} %), tokens {len(tok)} -> {dst}'); return 0
if __name__ == '__main__': sys.exit(main())
