# RESUMEN H-Q11-SOL013 (generado 2026-11-09T12:50:02Z)
Prereg PREREG_Q11_SOL013.md + ADDENDUM2/3 (no modificar). Rango: 2026-11-06..9999-12-31. Fuente: /root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/

Dias validos (dec2+dec3s100): 3 2026-11-06..2026-11-08; con rellenos T1: 3; nd_validos(T1,PLA_T1)=3; nd_validos(T1,G0)=3
T1 SOL L=0,13: n=43 rellenos, mercados=43, cierres=43, coste=26.6 EUR, pnl=-6.95
EV ponderado por EUR (sum pnl/sum coste): T1 -0.262 | -100 ms -0.466 (n=47) | sin 2 mejores dias -0.481 | IC90 por cierre (-0.794, +0.343)
EV por unidad (media pnl/coste): -0.093; dias +: 1/3
Comparadores: PLA_T1 n=57 EV -0.579 (sin2 -0.653) | G0 n=95 EV -0.433 (sin2 -0.808)
Victorias estrictas por dia comparable: T1>PLA_T1 2/3 | T1>G0 2/3
Muestra b (solo D_T1PLA): T1 n=43 EV -0.262 sin2 -0.481 IC90 inf -0.794 | PLA_T1 EV -0.579 | G0 EV -0.433
DIAGNOSTICO barrido (nmk>=3): 5 rellenos EV -0.988; resto 38 EV -0.160 (no es regla de decision)

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
- [ ] nd(T1,PLA_T1)>=10 y >=60 % victorias (2/3)
- [ ] nd(T1,G0)>=10 y >=60 % victorias (2/3)
=> sec. 3 cumplida: False | racha 0/3 (last_nd=3) | refuta_def=True refuta=True

PROMOCION (alfa/4): NO | seguimiento=INSUFFICIENT | IC cierre T1 [1,25%;98,75%] B=4000 todos los dias=(-0.844,+0.599) req inf>0: no | dias comparables T1-PLA_T1=(-0.844,+0.599) req inf>0: no | placebo: no aplica

## VEREDICTO: INSUFFICIENT (nd=3<10 (REFUTA/REFUTED no disponibles))
Aviso prereg: si el EV viene igual de PLA_T1, el mecanismo es "SOL a 0,13" y no la calma.
Exploratorio; no autoriza nada live. Rellenos sin barrido NO se filtran (clasificacion ex post).
