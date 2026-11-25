# Q11 barrido CORREGIDO (05-Nov, alpha-miner). TODO EXPLORATORIO
**Veredicto:** precursores del barrido = **REJECTED** para esta familia de datos (límite de datos declarado); puerta geométrica de colocación = **EXPLORATORY** (post hoc, pide prerregistro forward). No se toca producción ni prerregistros.
Base: escalera G (`escalera_B/engine.py` sin tocar; niveles 0,10/0,13/0,16/0,19, 5 acc, puerta A_R1ws), ETH/SOL/XRP 5m, **26-Oct..04-Nov (10 días ya gastados en Q11)**, cinta on-chain re-sincronizada idéntica a `esc_dec2.py`, reloj de recepción, EV = Σpnl/Σcoste con rebate, IC90 bootstrap por cierre (`fin`) y por día. Expediente: `experimentos/5m_barato/q11/barrido_corr/` (scripts, `out/*.log`, `HASHES.txt`, `DISENO_C.md`/`DISENO_C5.md` con sha escritos ANTES de cada paso).
**Reproducción:** G0 = dec2 exacto 10/10 días (2.938 rellenos, 2.074 eventos (k,tf), 635 cierres; src=bloque 16 = 0,5 %, excluidos). Fuente: `out/passA.log`, `out/ana_c1.log` §0.

## 1. Cruce de cotización vs fallback t_ws−63 ms (rellenos G0)
Cruce **55,3 %** (1.625/2.938; 55,1 % por €); fallback 44,7 %. Por tipo: S_nivel 98,6 % (n 346), «thru1» (un solo precio bajo L) 51,0 % (n 2.321), cola en L 37,3 % (n 271). ETH 58,7 / SOL 51,6 / XRP 53,0 %; por día 41,6-60,1 %. t_ws−tf con cruce: mediana 165 ms (p10 44, p90 349). Fuente `ana_c1.log` §1.

## 2. Etiquetas, EV y estimando (G0 sin bloque: n 2.922, EV −0,076 [−0,22, +0,07], 3/10 días, sin 2 mejores −0,177)
| etiqueta | P(S\|relleno) | eventos/cierres | EV\|S [IC90 cierre] [IC90 día] | días+ | sin 2 mejores | EV\|noS | dif [IC90 cierre], placebo p |
|---|---|---|---|---|---|---|---|
| S_wallet (nmk≥3) | 0,069 | 152/133 | +0,458 [+0,01, +0,92] [−0,02, +0,90] | 5/10 | +0,043 | −0,116 | +0,574 [+0,14, +1,02], 0,001 |
| S_orden (≥3 órdenes) | 0,077 | 171/146 | +0,489 [+0,07, +0,94] [+0,04, +0,86] | 7/10 | +0,109 | −0,124 | +0,613 [+0,20, +1,02], 0,001 |
| **S_nivel** (≥2 precios y pmin<L) | 0,118 | 244/201 | **+0,206 [−0,12, +0,55]** [−0,01, +0,43] | 7/10 | +0,067 | −0,114 | +0,320 [+0,01, +0,64], 0,008 |
| S_nivel, solo con cruce | 0,210 | 242/200 | +0,143 [−0,15, +0,46] | 7/10 | +0,046 | −0,051 | +0,194 [−0,12, +0,52], 0,17 |

S_nivel por moneda: ETH −0,113 (n 137), SOL +0,386 (135), XRP +0,468 (73). Descomposición: S_nivel∧S_wallet +0,528 (n 136, 5/10 d); S_nivel sin S_wallet −0,003 (209); **la pérdida de G0 es «thru1» −0,123 (n 2.308, −214 €)**: rellenos en que nuestro L está por encima del bid real.
**Estimando (oráculos con el futuro A PROPÓSITO, población completa con reposición, 10 días; `ana_c1.log` §3):**
| variante | rellenos | pnl € | EV [IC90 cierre] | días+ | sin 2 mejores | horas en libro |
|---|---|---|---|---|---|---|
| G0 | 2.938 | −166,9 | −0,076 [−0,22, +0,07] | 3/10 | −0,177 | 227 |
| ON1: cotizar solo si llega S_nivel en ≤1 s | 425 | +84,5 | +0,269 [−0,05, +0,60] | 7/10 | +0,024 | 0,1 |
| ON15 / ON60 | 1.027 / 1.591 | +48,6 / −289,3 | +0,064 / **−0,242 [−0,41, −0,07]** | 4 / 2 | −0,13 / −0,40 | 4,6 / 29 |
| OYD60 = saber la diana del hazard AUC 0,77 | 1.286 | −492,2 | **−0,522 [−0,65, −0,38]** | 0/10 | −0,628 | 45 |
| ANTI60: no estar 60 s antes de un S_nivel | 1.726 | +78,4 | +0,061 [−0,12, +0,24] | 6/10 | −0,099 | 194 |
**Estimando fijado: EVITAR, no colocarse delante.** Colocarse delante solo gana con precisión de ≤1 s y no es robusto. Con 60 s de antelación pierde, igual que R9-E1 en BTC (oráculo −0,43). Incluso con previsión perfecta, el techo de la evitación es +245 € en 10 días a 5 acc, con EV +0,061 no robusto.

## 3. g_* reconstruidos a tf−300 ms (03-Nov reconstruido, 04-Nov añadido; `ana_c1.log` §4)
Univariante S_nivel: bsz AUC 0,362 (p_max 0,003). Gradiente por retardo: 1 ms 0,345 → 300 ms 0,362 → 1 s 0,409, así que parte de la señal a 1 ms era fuga. HGB walk-forward (7 días OOS, 1.620 rellenos, 184 S_nivel):
- réplica antigua (rejilla 1 s): 0,542;
- a 1 ms: 0,606;
- **a 300 ms: 0,570 [0,528, 0,617]** frente a un placebo con media 0,504 y máximo 0,536 (p 0,11, el mínimo con 8 permutaciones);
- a 1 s: 0,546;
- solo T/L/moneda/lado: 0,538.

**Solo rellenos con cruce: 0,542 frente a placebo 0,527 (p 0,44) ≈ placebo.** Indicador NaN: AUC 0,48-0,51, sin fuga (sin filas NaN 0,562).

## 4. Otras familias, hazard de mercado y políticas
- **A tf−300 ms** (Binance propio 12 rasgos, cruzado 19, Chainlink 5, fase 2; sin flujo/conteos/bookTicker; `ana_c1b.log`): para S_nivel ninguna familia pasa alfa/4 (p_max mínimo 0,11); HGB OOS 0,49-0,54 ≈ placebo (p ≥0,14). S_wallet: B_r900 univariante 0,415 (p_max 0,003), pero el HGB cruzado da 0,502 OOS.
- **Hazard por segundo** (rejilla de decisión 500 ms, 2,21 M filas (k, L, t) con puerta G; etiqueta S_nivel(L) en (t+68 ms, t+60 s]; `C2_run.log`, `C2o_run.log`, `ana_c6.log`): AUC OOS 0,80-0,89 por día. **Pero solo T, L, bid−L, moneda y lado dan lo mismo.** Dentro de estratos de bid−L, libro+actividad menos solo-propios = −0,014 / −0,005 / −0,002 (mejor en 2-3 de 7 días). Los precursores no añaden nada a la geometría.
- **Políticas** (OOS walk-forward 29-Oct..04-Nov; G0 −71,5 €, EV −0,059, 1.630 rellenos; `ana_c3.log`, `ana_c5*.log`):

| política | rellenos | pnl € | EV | sin 2 mejores | ΔPnL vs G0 [IC90 cierre] | días Δ>0 |
|---|---|---|---|---|---|---|
| AVO_B70: cancelar al subir el hazard (principal de C) | 206 | −15,9 | −0,095 | −0,293 | +55,6 [−179, +264] | 6/7 |
| PG_B70: el score solo decide armar (principal de C5) | 1.082 | +18,4 | +0,022 | −0,053 | +90,0 [−24, +189] | 5/7 |
| PG_B50 | 624 | +117,6 | +0,245 | +0,135 | +189,2 [+43, +327], p 0,017 | 6/7 |
| **PG_O50 (solo T, L, bid−L, moneda, lado)** | 602 | +129,5 | +0,282 | +0,179 | +201,0 [+58, +336], p 0,014 | 6/7 |
| PGI_B50 (inversión) | 1.623 | −70,1 | −0,058 | −0,140 | +1,4 | 4/7 |
| 25 placebos (puntuación de otro token) | 863-943 | −105,4..+42,0 (media −28,5) | −0,155..+0,063 | | | |
| GEO6: armar solo si bid−L ≥6c (post hoc) | 1.240 | +2,3 | +0,002 | | | |

- AVO degenera en no operar: el 30 % del tiempo con hazard más alto contiene ~90 % de los rellenos. **REJECTED.**
- PG_B50 queda por encima de los 25 placebos (p placebo 0,038).
- PG_O50 por moneda: ETH +75,9 € (n 370), SOL +40,8 € (157), XRP +12,8 € (75).
- Reglas simples en 10 días: GEO6 −2,7 € (EV −0,002; Δ +164 [+64, +261], 9/10 días) y GEO8 +14,2 € (EV +0,009). Neutralizan la pérdida, pero no generan EV.

## 5. Hallazgos adversariales
1. La puerta PG se eligió después de ver C3/C4 en los MISMOS días de prueba. Las dos reglas principales declaradas con sha antes de correr (DISENO_C/DISENO_C5; no son prerregistros formales) fallan: AVO_B70 y PG_B70. Con 8 contrastes (alfa/8 = 0,0125), ni PG_B50 (p 0,017) ni PG_O50 (p 0,014) pasan.
2. La ventaja no viene de anticipar el barrido: el modelo sin precursores (PG_O50) es igual o mejor que PG_B50. Las reglas geométricas simples se quedan en EV ≈0, así que el +0,28 restante puede ser sobreajuste a interacciones T×bid−L×moneda×lado.
3. Mecanismo del simulador: la puerta cambia QUÉ relleno ocupa cada hueco (k, L, 5 acc). G0 lo gasta pronto en rellenos «thru1» tóxicos; PG lo deja para rellenos posteriores. Esto depende del relleno BASE: un print por debajo de L cuenta como relleno completo y la cola es el tamaño visible. No se han medido aquí ni la brecha «solo-toque» de R9-E4 ni el auto-print.
4. Cobertura baja: 30-Oct, 01-Nov y 02-Nov tienen 218/240/428 tokens por moneda en hora_mala. La comparación es pareada sobre el mismo universo; la supervivencia por hora mala no es medible.
5. Recursos: la regla load5>4 es inalcanzable (0 de 200 muestras ≤4 en ~50 h; nproc 8). Apliqué load5/nproc ≤3 (CLAUDE.md raíz) y load <16 (misión), con nice 19, ionice 3, ulimit −v 3 GB y fuera de 06-09Z. Total ~20 min de CPU en pasadas de menos de 10 min cada una.

## 6. Límite de datos y siguiente experimento decisivo
**Límite:** con 10 días y las fuentes actuales, ninguna variable anticipa el barrido más allá de dónde y cuándo está la orden (T, L, bid−L). Fuentes: libro L1 WS, cinta on-chain, Binance spot, cruzado, Chainlink, fase y L2 por delante (H-SURF-L2, AUC 0,49).
Sin probar:
- L2 a 5 niveles en tiempo real: logger desde el 05-Nov; hacen falta ≥10-12 días (≈16-17-Nov).
- Perp aggTrade y liquidaciones a 1 s: solo forward, escala ≥5 s.
- Identidad del tomador: el on-chain llega ~2,4 s tarde, no sirve por debajo de 3 s.

**Siguiente:** prerregistro forward (lo revisa el validador) de **PG_O50 congelado** frente a G0 y GEO6:
- modelo OWN entrenado con 26-Oct..04-Nov y umbral c=0,5, ambos congelados;
- días desde el 06-Nov, mínimo 10;
- pasa si ΔPnL vs G0 >0 con IC90 por cierre >0, EV >0 con IC90 por cierre >0, sin los 2 mejores días >0, al menos 6/10 días, y además **supera a GEO6** (si no, la parte del modelo es ruido);
- coste ~1 min de CPU al día, con los insumos que ya genera forward_calma (tape/bad/x y ms_D.npz).

Si pasa, «escalera G con puerta geométrica» va a dry-run; si no, se cierra «anticipar/evitar barrido» en la escalera G hasta tener L2.

## 7. Reproducibilidad y agentes
`cd experimentos/5m_barato/q11/barrido_corr`. Secuencia de comandos:
1. `python3 -I passA.py 2026-10-28` (a mano) y `./run_A.sh` (resto de días). 29 y 30-Oct se rehicieron con `run_A2.sh` tras un MemoryError, ya corregido en `passA.py`. `passA2.py` (oráculos por horizonte de evitación) está preparado, no ejecutado.
2. `./run_ana1.sh`; `python3 -I ana_c1b.py`.
3. `./run_C1.sh`: genera C1_*.pkl (>100 MB, borrados; se regeneran en ~2,5 min).
4. `./run_C2.sh`, `./run_C3.sh`.
5. `python3 -I ana_c4.py`.
6. `./run_C5.sh`, `./run_C5b.sh`, `./run_C5c.sh`, `./run_C5d.sh`.
7. `python3 -I ana_c6.py`.

`out/*.pkl` está fuera de git (`.gitignore`); hashes en `HASHES.txt`.
Necesito que el chief lance, de uno en uno:
- **cheap5m-statistical-validator**: revisar §1-4 y redactar el prerregistro de PG_O50;
- **cheap5m-red-team-auditor**: atacar la puerta (post hoc, efecto hueco, fidelidad del relleno BASE, auto-print);
- **cheap5m-execution-engineer**: evaluador forward, solo si el chief lo aprueba.
