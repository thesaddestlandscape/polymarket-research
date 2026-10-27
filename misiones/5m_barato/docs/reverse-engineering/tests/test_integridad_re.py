#!/usr/bin/env python3
"""Integridad del protocolo cheap5m-reverse-engineer: ficheros, frontmatter, estados, límites de seguridad."""
import os, re, sys
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..'))
D = os.path.join(R, 'misiones/5m_barato/docs/reverse-engineering')
A = os.path.join(R, '.claude/agents/cheap5m-reverse-engineer.md')
err = []
def ok(c, m):
    if not c: err.append(m)
for f in ['README.md','CASE_TEMPLATE.md','HYPOTHESIS_LEDGER.md','EXPERIMENT_LEDGER.md','FAILED_ATTEMPTS.md','DECISION_LOG.md','PROGRESS.md']:
    ok(os.path.isfile(os.path.join(D, f)), f'falta {f}')
t = open(A).read() if os.path.isfile(A) else ''
ok(t.startswith('---\nname: cheap5m-reverse-engineer\n'), 'frontmatter name')
m = re.search(r'^tools: (.*)$', t, re.M); tools = [x.strip() for x in m.group(1).split(',')] if m else []
ok(set(tools) <= {'Read','Grep','Glob','Bash','Edit','Write'}, f'tools fuera de lo permitido: {tools}')
ok('Agent' not in tools and 'WebFetch' not in tools, 'no debe lanzar agentes ni web')
for s in ['SOLVED','PARTIALLY_SOLVED','EVIDENCE_INSUFFICIENT','HYPOTHESIS_REFUTED','BLOCKED','NO_ECONOMIC_EDGE_DETECTED']:
    ok(s in t, f'estado {s} ausente en el agente')
for s in ['validación INDEPENDIENTE','.env','órdenes reales','77a75859ae5cf22e','hipótesis nula|la nula']:
    ok(re.search(s, t), f'falta regla: {s}')
for f in ['CASE_TEMPLATE.md','FAILED_ATTEMPTS.md']:
    p = os.path.join(D, f); ok(f=='CASE_TEMPLATE.md' or (os.path.isfile(p) and '|' in open(p).read()), f'{f} sin tabla')
cp = os.path.join(D,'CASE_TEMPLATE.md')
if os.path.isfile(cp):
    for s in ['Reproducción','Hechos','Refutación intentada','validación independiente','Siguiente paso']:
        ok(s in open(cp).read(), f'plantilla sin {s}')
# cada caso cerrado debe tener estado válido
for c in (os.listdir(os.path.join(D,'casos')) if os.path.isdir(os.path.join(D,'casos')) else []):
    e = os.path.join(D,'casos',c,'EXPEDIENTE.md')
    if os.path.isfile(e):
        ok(re.search(r'Estado de cierre: (SOLVED|PARTIALLY_SOLVED|EVIDENCE_INSUFFICIENT|HYPOTHESIS_REFUTED|BLOCKED|NO_ECONOMIC_EDGE_DETECTED)', open(e).read()), f'{c}: estado de cierre inválido')
        if 'Estado de cierre: SOLVED' in open(e).read():
            ok('validación independiente' in open(e).read().lower() and 'pendiente' not in open(e).read().lower().split('validación independiente')[1][:200], f'{c}: SOLVED sin validación independiente')
# cada PREREG*/ADENDA* de un caso debe tener su .sha256 y verificar
import hashlib, glob
for p in glob.glob(os.path.join(D,'casos','*','PREREG*.md'))+glob.glob(os.path.join(D,'casos','*','ADENDA*.md')):
    h=p[:-3]+'.sha256'
    if not os.path.isfile(h): err.append(f'{os.path.relpath(p,D)} sin .sha256'); continue
    ok(open(h).read().split()[0]==hashlib.sha256(open(p,'rb').read()).hexdigest(), f'{os.path.relpath(p,D)}: sha256 no coincide')
# cada expediente con tabla de reproducción
for e in glob.glob(os.path.join(D,'casos','*','EXPEDIENTE.md')):
    ok(re.search(r'REPRODUCIDA|NO_REPRODUCIDA|NO_LOCALIZADA', open(e).read()), f'{os.path.relpath(e,D)}: sin estados de reproducción')
print('FALLOS:' if err else 'OK', *err, sep='\n')
sys.exit(1 if err else 0)
