#!/usr/bin/env python3
"""Casos sinteticos de aceptacion del evaluador (sin datos reales). Uso: python3 -I test_l2eval.py -> imprime PASS/FAIL por caso y sale !=0 si alguno falla."""
import sys, os, json, tempfile, numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l2eval as E

COINS = ['ETH', 'SOL', 'XRP']; LS = [0.10, 0.13, 0.16, 0.19]
def synth(seed, ndias=20, tox_gap=0.12, n_per=8):
    rng = np.random.default_rng(seed); rows = []
    for di in range(ndias):
        d = f'2026-10-{1 + di:02d}'
        for c in COINS:
            for L in LS:
                for j in range(n_per):
                    tox = rng.random() < 0.30
                    p = max(0.01, L - (tox_gap if tox else -0.02))     # toxicas pierden; el resto gana algo sobre el precio
                    g = float(rng.random() < p); rows.append(dict(dia=d, act=c, L=L, fin=di * 100 + j, q=5.0, gana=g, tox=tox))
    U = pd.DataFrame(rows); U['cost'] = U.q * U.L
    for rb, nm in ((0.0, '0'), (0.2, '2')): U['pnl' + nm] = E.pnl_maker(U.gana, U.q, U.L, rb); U['pot' + nm] = -U['pnl' + nm]
    return U
def aplicar(U, aff):
    U = U.copy(); U['aff'] = aff; U['aff_inv'] = ~aff; return U
R = []
def chk(nm, ok, det=''): R.append(ok); print(('PASS' if ok else 'FAIL'), nm, det)

dias = [f'2026-10-{1 + i:02d}' for i in range(20)]
# 1) efecto nulo: quita aleatoria independiente del resultado -> NO PROMISING en 10 semillas, nunca por debajo de 'rechazo' del placebo
prom = 0; rej = 0
for s in range(10):
    U = synth(100 + s); rng = np.random.default_rng(s); U = aplicar(U, rng.random(len(U)) < 0.25)
    r = E.gate(U, dias, 'nulo', B=2000, look=20); prom += r['PROMISING_candidato']; rej += r['REJECTED']
chk('nulo: 0/10 PROMISING', prom == 0, f'promising={prom} rejected={rej}')
# 2) efecto inyectado: quitar 85 % de las toxicas (y ninguna otra) -> debe pasar G1-G10 con rb 0 y 0,2
U = synth(1); rng = np.random.default_rng(5); U = aplicar(U, U.tox.values & (rng.random(len(U)) < 0.85))
r = E.gate(U, dias, 'inyectado', B=4000, look=20)
chk('inyectado: PROMISING', r['PROMISING_candidato'], json.dumps({k: (v['sum_delta'], v['placebo_p'], v['delta_inv'], v['cobertura_coste']) for k, v in r['rb'].items()}))
chk('inyectado: Delta>0 y inversion<0 (rb0 y rb0,2)', all(v['sum_delta'] > 0 and v['delta_inv'] < 0 for v in r['rb'].values()))
# 3) inversion: quitar las NO toxicas (lo contrario) -> Delta<0 y REJECTED
Ui = U.copy(); Ui['aff'] = ~U['aff'] & ~U.tox; Ui['aff_inv'] = U['aff']
ri = E.gate(Ui, dias, 'inversion', B=2000, look=20)
chk('inversion: Delta<0 y REJECTED', ri['rb']['0.0']['sum_delta'] < 0 and ri['REJECTED'])
# 4) veto >=85 % del coste base: quitar casi todo con efecto positivo -> no PROMISING aunque Delta>0
Uv = synth(2); Uv = aplicar(Uv, (Uv.tox.values | (np.random.default_rng(9).random(len(Uv)) < 0.95)))
rv = E.gate(Uv, dias, 'veto', B=2000, look=20)
chk('veto cobertura >=85 %', rv['rb']['0.0']['veto'] and not rv['PROMISING_candidato'], f"cob={rv['rb']['0.0']['cobertura_coste']}")
# 5) un solo dia gordo (PnL concentrado) no debe pasar G4/G5
Uc = synth(3); rng = np.random.default_rng(3); aff = np.zeros(len(Uc), bool); d0 = (Uc.dia == dias[0]).values
aff[d0] = Uc.tox.values[d0]; Uc.loc[d0 & Uc.tox.values, 'pot0'] += 60; Uc.loc[d0 & Uc.tox.values, 'pot2'] += 60; Uc['aff'] = aff; Uc['aff_inv'] = ~aff
rc = E.gate(Uc, dias, 'un_dia', B=2000, look=20)
chk('un solo dia: no PROMISING (G4/G5)', not rc['PROMISING_candidato'] and not rc['rb']['0.0']['gates']['G4'])
# 6) adicion (N3/B1/H-VIDA): unidades con EV>0 pasan; con EV<0 no; n<40 no pasa G7
Ua = synth(4, tox_gap=-0.05); Ua['aff'] = True; Ua['aff_inv'] = False; Ua['pot0'] = Ua.pnl0; Ua['pot2'] = Ua.pnl2
ra = E.gate(Ua, dias, 'adicion+', tipo='adicion', B=2000, look=20, aplica_G6=True)
Un = synth(4, tox_gap=0.12); Un['aff'] = True; Un['aff_inv'] = False; Un['pot0'] = Un.pnl0; Un['pot2'] = Un.pnl2
rn = E.gate(Un, dias, 'adicion-', tipo='adicion', B=2000, look=20)
chk('adicion EV>0: G1-G2 pasan; EV<0: REJECTED', ra['rb']['0.0']['gates']['G1'] and ra['rb']['0.0']['gates']['G2'] and rn['REJECTED'])
# 7) < 10 dias: no PROMISING (G9)
r5 = E.gate(U[U.dia.isin(dias[:6])].reset_index(drop=True), dias[:6], 'pocos', B=2000, look=10)
chk('<10 dias: no PROMISING', not r5['PROMISING_candidato'] and not r5['rb']['0.0']['gates']['G9'])
# 8) rb: Delta con rb=0,2 > rb=0 en quita de perdedoras (el rebate reduce la perdida evitada) -> comprobar formula
chk('formula rb: pnl2-pnl0 = q*0,07*L(1-L)*0,2', np.allclose(U.pnl2 - U.pnl0, U.q * 0.2 * 0.07 * U.L * (1 - U.L)))
# 9) guard HOLD + log append-only + hash
with tempfile.TemporaryDirectory() as td:
    lg = td + '/log.jsonl'
    try: E.guard_dias(['2026-11-09', '2026-11-10'], 'x', hold=False, log=lg); ok = False
    except PermissionError: ok = True
    chk('guard bloquea HOLD', ok and not os.path.exists(lg))
    E.guard_dias(['2026-11-08', '2026-11-09'], 'x', log=lg); E.guard_dias(['2026-11-03'], 'y', log=lg)
    chk('log append-only (2 lineas)', len(open(lg).read().splitlines()) == 2)
chk('hash PREREG congelado', E.sha_ok())
# 10) determinismo: misma entrada -> mismo resultado
a = E.gate(U, dias, 'd', B=2000, look=20); b = E.gate(U, dias, 'd', B=2000, look=20)
chk('determinismo', json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True))
# 11) validez de dia: faltan b40 / sa_ms / pocas horas
with tempfile.TemporaryDirectory() as td:
    os.makedirs(td + '/bad'); os.makedirs(td + '/b40'); os.makedirs(td + '/sa')
    json.dump(dict(bad=[['2026-10-01', h] for h in range(14)]), open(td + '/bad/bad_2026-10-01.json', 'w'))
    v = E.valida_dia('2026-10-01', td + '/bad/', td + '/b40/', td + '/sa/')
    chk('dia invalido: 10 h sanas, sin b40, sin sa_ms', (not v['valido']) and len(v['motivos']) == 3, str(v['motivos']))
sys.exit(0 if all(R) else 1)
