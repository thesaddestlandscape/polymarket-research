# RESUMEN H-Q11-SOL013 (generado 2026-11-24T12:50:04Z)
Prereg PREREG_Q11_SOL013.md + ADDENDUM2/3 (no modificar). Rango: 2026-11-06..9999-12-31. Fuente: /root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/

Dias validos (dec2+dec3s100): 10 2026-11-06..2026-11-15; con rellenos T1: 10; nd_validos(T1,PLA_T1)=10; nd_validos(T1,G0)=10
AVISO: dias con dec2 sin dec3s100 (o al reves) en la ventana, NO cuentan (no es error): ['2026-11-16']
T1 SOL L=0,13: n=122 rellenos, mercados=122, cierres=122, coste=76.5 EUR, pnl=-6.28
EV ponderado por EUR (sum pnl/sum coste): T1 -0.082 | -100 ms -0.115 (n=128) | sin 2 mejores dias -0.324 | IC90 por cierre (-0.461, +0.288)
EV por unidad (media pnl/coste): -0.042; dias +: 5/10
Comparadores: PLA_T1 n=173 EV -0.173 (sin2 -0.471) | G0 n=287 EV -0.315 (sin2 -0.515)
Victorias estrictas por dia comparable: T1>PLA_T1 5/10 | T1>G0 7/10
Muestra b (solo D_T1PLA): T1 n=122 EV -0.082 sin2 -0.324 IC90 inf -0.461 | PLA_T1 EV -0.173 | G0 EV -0.315
DIAGNOSTICO barrido (nmk>=3): 9 rellenos EV -0.988; resto 113 EV -0.007 (no es regla de decision)

## CONFIRMA (sec. 3): a) todos los dias validos
- [ ] EV>0
- [ ] EV(-100ms)>0
- [ ] EV sin 2 mejores dias>0
- [ ] IC90 cierre inf>0
- [x] EV(T1)>EV(PLA_T1) agregado
- [x] EV(T1)>EV(G0) agregado
- [x] n>=40 rellenos T1
b) solo dias de D_T1PLA
- [ ] EV>0
- [ ] EV sin 2 mejores dias>0
- [ ] IC90 cierre inf>0
- [x] EV(T1)>EV(PLA_T1)
- [x] EV(T1)>EV(G0)
- [x] n>=40 rellenos T1
c) dias comparables
- [ ] nd(T1,PLA_T1)>=10 y >=60 % victorias (5/10)
- [x] nd(T1,G0)>=10 y >=60 % victorias (7/10)
=> sec. 3 cumplida: False | racha 0/3 (last_nd=10) | REFUTA (ADDENDUM4): R1=si R2=si R3=no (EV(T1)=-0.082 IC90 sup cierre=+0.288 dia=(-0.403,+0.227); n=122) => no

PROMOCION (alfa/4): NO | seguimiento=INSUFFICIENT | IC cierre T1 [1,25%;98,75%] B=4000 todos los dias=(-0.570,+0.464) req inf>0: no | dias comparables T1-PLA_T1=(-0.570,+0.464) req inf>0: no | placebo: no aplica

## VEREDICTO: INSUFFICIENT (nd=10: CONFIRMA y REFUTA no cumplidas (REFUTA incluye NaN/minimos no alcanzados) y nd<20)
Aviso prereg: si el EV viene igual de PLA_T1, el mecanismo es "SOL a 0,13" y no la calma.
Exploratorio; no autoriza nada live. Rellenos sin barrido NO se filtran (clasificacion ex post).
