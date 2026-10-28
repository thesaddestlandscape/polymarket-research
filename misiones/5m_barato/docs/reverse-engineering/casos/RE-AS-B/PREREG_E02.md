# PREREG E-RE-AS-B-02 (27-Oct-2026) — escrito ANTES de calcular nada sobre vpv_2026-10-26 ni sobre EV ponderado por € / barrido por moneda x bucket
Ya visto antes (no ciego): E01 sobre vpv 24-25 (M_f opt -0,022; EVw opt -0,100, pes -0,383 por validación independiente; post-hoc p01 pes+barrido -8,4 pp vs sin barrido +0,0 pp, no ponderado por €). NO visto: vpv_2026-10-26 (día OOS), nada por moneda x bucket ponderado por €.
Pregunta: ¿existe una política de mitigación de la AS de B (maker barato 5m b in [0,10-0,30]) con EV ponderado por € > 0 que cumpla el gate (n>=40 rellenos, >=10 días, IC90 por días > 0)?
## Datos
`/root/polymarket-research-datalogs/vida_puja_virtual/vpv_2026-10-2{4,5,6}.csv.gz`; `gana` = (maker_ms_desenlaces_cache.json[mercado]==lado) (como ADENDA E01); evaluables: gana no-missing, ba>b. Unidad vida. Pnl por vida rellena = 5*(gana-b) (sin comisión ni rebate: maker; rebate 20% de comisión taker ignorado => cota pesimista leve). Bootstrap por CIERRE (2000, semilla 2711).
EVw(S) = suma pnl / suma coste (5*b) sobre las vidas rellenas de S. Rellenos: opt y pes por separado.
## Preguntas y reglas (fijadas antes)
Q1 EVw(opt) y EVw(pes) agregado, por día, por moneda, por bucket de b (0,10-0,15,0,15-0,20,0,20-0,25,0,25-0,30) y moneda x bucket. R1 «margen de relleno negativo confirmado» si IC90 por cierre de EVw < 0 agregado en ambos y el día 26 (OOS) tiene el mismo signo.
Q2 (H2, replica OOS): entre rellenos pes, EVw(barrido=1) - EVw(barrido=0), agregado y por día. R2 «H2 apoyada» si IC90 de la diferencia < 0 y signo igual en 3/3 días; si solo 24-25 lo cumplen y 26 no => refutada como patrón estable.
Q3 (techo contrafactual, NO ejecutable ex-ante): EVw de los rellenos pes con barrido=0 (política «cancelar justo antes de un barrido» con previsión perfecta). Gate G: n>=40 rellenos, >=10 días, IC90 por días > 0. Con 3 días el gate de días NO es alcanzable: el resultado máximo posible es «EVIDENCE_INSUFFICIENT/exploratorio». Se reporta además P(fill) retenido y € por día.
Q4 Placebo: quitar al azar, dentro de día x moneda, el mismo nº de rellenos pes que son barrido=1 (1000 réplicas): ¿EVw del resto de la política supera el percentil 95 del placebo? Inversión: EVw de los rellenos barrido=1 (lo que la política aparta). Si placebo ~ política => no ordena nada.
Q5 Robustez: leave-one-day-out de Q3; EV de Q3 sin el mejor día; mejor celda moneda x bucket con n>=40 contrastada con max-statistic (bootstrap del máximo sobre todas las celdas con n>=40, sin centrar => se compara con la distribución del máximo bajo permutación de gana dentro de moneda x bucket x día, 500 perm).
Q6 Cruce real: posiciones.csv H47-B (202 posiciones on-chain, 20-23 Oct): EVw real por día y moneda (pnl_realizado/coste) para contrastar con la virtual. Solo descriptivo.
## Decisión
- Si Q3 EVw IC90 por cierre > 0 Y Q4 supera placebo p95 Y Q2 consistente 3/3 días: «mitigación por evitar barridos tiene techo positivo exploratorio»; falta (i) ex-ante, (ii) >=10 días. Siguiente paso = E02-real on-chain x libro5_ms.
- Si Q3 <= 0 o no supera placebo: «ni con previsión perfecta de barrido hay EV>0 en vpv»: NO_ECONOMIC_EDGE_DETECTED para esa palanca.
- Cualquier celda moneda x bucket positiva se declara exploratoria (multiplicidad: n celdas = las evaluadas).
