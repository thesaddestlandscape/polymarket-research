#!/usr/bin/env python3
"""audit_final.py -- cierre de EXP-1: estados por fase, dias COMPLETE/FAILED/PENDING, duraciones del log y sha256 de scripts y salidas -> anexa un bloque a ../MANIFEST.txt (solo con --escribir). Solo lectura de exp1/."""
import os, sys, glob, json, hashlib, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popdata import *
sh = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
L = [f'## EXP-1 CIERRE ({pd.Timestamp.utcnow().strftime("%FT%TZ")}); addendum {ADD_SHA[:8]}']
S = json.load(open(EXP + 'STATUS.json')) if os.path.exists(EXP + 'STATUS.json') else {}
L.append('Fases (STATUS.json): ' + '; '.join(f"{k}: {v.get('estado')} ({v.get('t')})" for k, v in S.items()))
est = estado_dias(); cobL, por = resumen_cobertura(est); L += cobL
log = open(EXP + 'run_exp1.log').read().splitlines() if os.path.exists(EXP + 'run_exp1.log') else []
ini = {}; dur = {}
for ln in log:
    m = re.match(r'(\S+) (INICIO|FIN) (\S+)', ln)
    if m:
        t = pd.Timestamp(m.group(1))
        if m.group(2) == 'INICIO': ini[m.group(3)] = t
        elif m.group(3) in ini: dur[m.group(3)] = (t - ini[m.group(3)]).total_seconds()
L.append(f"Duracion total del job: {(pd.Timestamp(log[-1].split()[0]) - pd.Timestamp(log[0].split()[0])).total_seconds() / 60:.1f} min; E2 por dia: media {np.mean([v for k, v in dur.items() if k.startswith('E2_')]):.0f} s; fases: " + ', '.join(f'{k} {v:.0f} s' for k, v in dur.items() if not k.startswith('E2_')) if log and dur else 'sin log')
L.append('Log final: ' + (log[-1] if log else 'n/d'))
fl = sorted(glob.glob(EXP + '*.py')) + [EXP + 'run_exp1.sh'] + sorted(glob.glob(EXP + 'E*_*.txt')) + sorted(glob.glob(EXP + 'E*_*.json')) + [EXP + 'B_fills_v3.pkl', EXP + 'STATUS.json']
for p in fl:
    if os.path.exists(p): L.append(f'{sh(p)}  exp1/{os.path.basename(p)}')
L.append('manifiestos de poblacion por dia: ' + hashlib.sha256(''.join(sh(p) for p in sorted(glob.glob(CACHE + 'pob_2026-*.json'))).encode()).hexdigest() + f'  ({len(glob.glob(CACHE + "pob_2026-*.json"))} ficheros)')
print('\n'.join(L))
if '--escribir' in sys.argv: open(AQ + 'MANIFEST.txt', 'a').write('\n' + '\n'.join(L) + '\n'); print('anexado a MANIFEST.txt')
