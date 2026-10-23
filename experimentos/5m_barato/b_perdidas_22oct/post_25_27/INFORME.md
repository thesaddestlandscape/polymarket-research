# POST-25-27 - postmortem de las tandas r25-r27 de B como prueba fuera de muestra (23-Oct-2026, ~10:00Z)
Estado: **EXPLORATORY / DESCRIPTIVO (n=16 posiciones, 10 cierres, 1 dia).** Solo lectura: B, ejecutores, crons, config, modulos intactos; sin ordenes, claves ni commits. Prereg `PREREG_POST2527.md` (sha256 8e220e16..., `sha256sum -c PREREG_POST2527.sha256` OK) escrito y hasheado ANTES de calcular ninguna regla sobre las posiciones del 23-Oct. Lo POST-HOC va marcado. Scripts y hashes: `scripts/`, `datos/HASHES_scripts.txt`; salidas: `datos/a1..a8_*.txt`, `datos/pos_b.csv` (202 posiciones etiquetadas), `datos/gemelo_fills_23oct.csv`.
Nomenclatura: r25/r26/r27 = tandas "25/26/27" de Javi = tandas 26/27/28 de `contabilidad_wallet_dedicada` (ese numera por suelo_reiniciado: desfase +1). Aqui r25 06:30-07:50Z, r26 07:50-08:50Z, r27 08:50Z-.

## 0. Respuesta corta
1. **Contabilidad CUADRA** (reproducida a mano): saldo on-chain 3,412408 pUSD = suma de 260 movimientos = 19 + F1 (+0,587) + PnL B (-16,023) - 0,152 (una ganadora de polvo del 21-Oct sin redimir). PnL del 23-Oct = **-9,843** (r25 -4,780; r26 -1,013; r27 -4,051), 16 posiciones, **1 ganadora de 16** (ETH Down 0,16 x7: +5,88). No hay dinero sin explicar en el 23-Oct (0 discrepancias ledger/on-chain; las 4 de la contabilidad son de 20-22 Oct, 9 mercados sin `puja_fin`, 16,4 acc).
2. **Las predicciones congeladas NO se cumplieron ni se refutaron (n=16, 4 en h_w1=1).** L1 predecia PnL(h_w1=1)<0: salio **+3,30** (la unica ganadora es h_w1=1); saltar h_w1=1 habria costado -3,30 (RL0), RL2 -4,70, RL1 no salta nada (2 TREND). R3 (bid15-puja<=3c y vol30>=26): las 5 posiciones que pasan perdieron las 5 (0/5, -5,89); solo habria ahorrado +2,91 a costa de la ganadora. S1 (proxy): 1-2 posiciones, +1,10..+2,55. **Ninguna regla evita mas de ~2,9 $ de los 9,84 $ en el dia, salvo las reglas que solo existen a posteriori y que he formulado yo viendo el dia (no cotizar en REVERT +9,06; fuera de MIXTO +11,66), y la poblacion las REFUTA (ver 5).**
3. **Mercado vs B vs azar:** B no perdio mas que el maker medio de forma distinguible: nulo calibrado a la poblacion on-chain 17-22 (27.215 unidades) da PnL esperado -0,30 $ (sd 8,7); P(PnL<=-9,84)=0,14 (0,16 con ajuste por cluster); P(<=1 acierto de 16)=0,13. Pero **la ventana fue mala para TODOS los longshots**: con el bid 0,10-0,30 a T 150-210 s en los 27 cierres de la ventana de B, acierto 13,0 % (n=69) frente a 24,8 % (n=614) fuera de ella (escaneo de ventanas de igual duracion: 2,5 % de las ventanas igual o peor; post-hoc, ventanas solapadas). El gemelo simulado de B (r3shadow cons_x) en la misma ventana: 1 acierto de 14 (EV -0,64, IC90 cierre -1,00..-0,05). Descomposicion (escenarios, no puntos): observado -9,84 = nulo -0,30 + regimen de la ventana -5,3 + seleccion adversa (cota del gemelo, n=14) -5,1 + residuo +0,8.
4. **Quedan -9,85 $ en 3 h, y el gap a 200k NO se cierra con B:** la poblacion ENTERA de makers en la banda 0,10-0,30 de ETH/SOL/XRP 5m despliega ~4.715 EUR/dia (17-21 Oct); 200 k EUR/anio con EV +0,10/EUR exigiria 5.479 EUR/dia = 1,2x todo ese volumen, con EV +0,20 el 58 % de el. B desplego 16-83 EUR/dia (1,7 % del volumen el 21-Oct) con EV -0,072 (IC90 cierre -0,32..+0,20, n=202; sin las 2 mejores posiciones -0,154). Eso es aritmetica de capacidad, no prevision.
5. **Rechazado hoy:** (a) "no cotizar en REVERT" (mi hipotesis post-hoc: salva +9,06 el 23-Oct) -> la poblacion 17-22 da REVERT el MEJOR EV (+0,031 vs -0,041 MIXTO y -0,047 TREND) y saltarlo cuesta -277 EUR (placebo p=0,99): **REJECTED**; (b) "el relleno por orden lo predice h_w1": tasa de relleno por mercado-lado 0,538 (h_w1=1) vs 0,531 (=0): no hay firma en el relleno.

## 1. Contabilidad (parte 1)
Fuente: `contabilidad_wallet_dedicada/{movimientos,posiciones}.csv`, `estado_dashboard.json` (bloque 96027574, 09:12Z), ledger B. Reproducido en `scripts/a1_contab.py` -> `datos/a1_contab.txt`.
| Cuadre | Valor |
|---|---|
| Suma de 260 movimientos pUSD (DEPOSITO 19; COMPRA -; REDENCION +) | 3,412408 = saldo on-chain 3,412408 (dif 0) |
| 19 + F1 (+0,58725) + PnL B realizado (-16,0229) | 3,56432; saldo 3,41241; diferencia 0,15191 = ganadora SOL 1792584300 (21-Oct, payout 0,151909) NO redimida (polvo de 1,38 acc; 42 ganadoras en posiciones, 41 REDENCION) |
| Saldo antes de r25 / r26 / r27 / ahora | 13,2557 / 8,4757 / 7,4632 / 3,4124 |
| PnL por run (pos. liquidadas) | r25 -4,780 (4 pos, 0 gan) ; r26 -1,013 (8 pos, 1 gan; el pico de 11,76 $ que cita el supervisor coincide con la redencion de 7,00 $ de la ganadora a las 08:02Z; no recalculado) ; r27 -4,051 (4 pos, 0 gan) = **-9,843** |
| Ledger vs on-chain 23-Oct | 0 discrepancias (acciones por mercado iguales). Historico 20-22: 9 mercados on-chain sin `puja_fin` (16,4 acc; ya conocido) |
| Comisiones | maker 0 (B). Rebate NO cobrado ni verificable; **estimado** 20 % del fee taker 0,07 p(1-p): 0,185 $ el 23-Oct (1,1 pp de EV), 2,41 $ en B total (+0,011/EUR): no cambia el signo (-0,072 -> -0,061). El devengo anunciado (1,318 $ a 22-Oct 15:06Z) sigue sin pago observable en la wallet. |
Nada que no cuadre. A surfacear: (i) el proceso `h47B` (pid 437290, `--n 500`, "ya usadas 358") **sigue vivo a las 09:24Z pero no postea** (suelo de saldo; `mercado_fin posteado: False`); el supervisor dice "parado" (saldo 3,41 < 12). (ii) el cuadre llama "abierta" a la tanda 28 por construccion.

## 2. Por posicion (16 posiciones, 23-Oct)
Etiquetas: L1 (`etiquetado_B_2026-10-23`), R de `regimen_lib` recalculado para el 23-Oct con la misma funcion (sha 750a4ecf9a5d; barras de bookTicker; sandbox en scratchpad, NO escribe en datalogs), bid15/vol30 del brazo r3shadow (muestra <=6 s antes de t_dec), mov. Binance 2 s previos a la deteccion (S1p, + = a favor).
| run | mercado (cierre) | lado | precio x acc | PnL | h_w1 (rpre bps) | R | gap15 (mil) / R3 | S1p mov bps |
|---|---|---|---|---|---|---|---|---|
| r25 | xrp 06:40 | Up | 0,28 x5 | -1,40 | 0 (-19,6) | REVERT | +190 no | 0,0 |
| r25 | sol 06:40 | Up | 0,26 x5 | -1,30 | 0 (-16,2) | REVERT | +190 no | 0,0 |
| r25 | eth 06:40 | Up | 0,20 x5 | -1,00 | 0 (-12,5) | REVERT | +440 no | -1,2 |
| r25 | sol 06:45 | Down | 0,12 x9 | -1,08 | 0 (+6,7 <7,7) | REVERT | 0 pasa | 0,0 |
| r26 | xrp 07:55 | Up | 0,23 x5 | -1,15 | 0 (-24,9) | TREND | -70 pasa | 0,0 |
| r26 | **eth 08:00** | Down | 0,16 x7 | **+5,88** | **1 (+20,9)** | MIXTO | +780 no | -0,8 |
| r26 | xrp 08:05 | Up | 0,29 x5 | -1,45 | 0 (-14,3) | TREND | +80 no | **-2,3 (S1p)** |
| r26 | xrp 08:10 | Down | 0,14 x0,23 | -0,03 | 1 (+10,6) | MIXTO | +150 no | 0,0 |
| r26 | eth 08:10 | Down | 0,28 x5 | -1,40 | 1 (+8,4) | REVERT | -60 pasa | +0,2 |
| r26 | xrp 08:15 | Down | 0,16 x7 | -1,12 | 0 (-0,8) | MIXTO | -100 pasa | -0,8 |
| r26 | sol 08:15 | Down | 0,13 x8 | -1,04 | 0 (-19,2) | REVERT | sin muestra | 0,0 |
| r26 | sol 08:25 | Down | 0,14 x5 | -0,70 | 0 (-27,8) | REVERT | +50 no | 0,0 |
| r27 | sol 08:55 | Up | 0,23 x5 | -1,15 | 1 (+12,4) | MIXTO | +610 no | -1,0 |
| r27 | eth 08:55 | Up | 0,27 x2,45 | -0,66 | 0 (+0,5) | MIXTO | +250 no | 0,0 |
| r27 | xrp 09:00 | Up | 0,22 x5 | -1,10 | 0 (-2,3) | MIXTO | +650 no | **-2,3 (S1p)** |
| r27 | eth 09:00 | Up | 0,19 x6 | -1,14 | 0 (-14,5) | REVERT | -130 pasa | -1,5 |
Cortes (`datos/a3_reglas.txt`): lado YES 0/9 (-10,35), NO 1/7 (+0,51); en_contra 0/10 (-11,40), a_favor 1/6 (+1,56); moneda ETH +1,68 (1/5), SOL -5,27 (0/5), XRP -6,25 (0/6); precio 0,10-0,15 0/4, 0,15-0,20 1/3, 0,20-0,25 0/4, 0,25-0,30 0/5; hora 06Z -4,78, 07Z +4,73, 08Z -9,79 (10 posiciones). Tamano: 5 acc salvo parciales (0,23 y 2,45 acc). **Cola/barrido C1/C2/C3 y retirada L1b: DATA_BLOCKED para el 23-Oct** (`oc_2026-10-23` no extraido; la retirada D-1 corre el 24-Oct 12:50Z). Sustituto disponible: markout de los rellenos (ledger `puja_fin`): ponderado por coste, 23-Oct mk5 -0,126 / **mk30 -0,433** (n=14) frente a 20-22 mk5 -0,092 / mk30 +0,015 (n=162): el relleno fue seguido de caida del mid mas fuerte que la habitual (sintoma de regimen/AS; no distingue cual).
Ordenes (3.796 `puja_post` 20-23 Oct): el 23-Oct 524 ordenes en 35 mercados-lado (15 ordenes por mercado-lado; 7,6 el 20-Oct, 9,0, 11,5), 15 rellenos (43 % por mercado-lado frente a 68 %, 55 %, 49 %): mas recotizacion y menos relleno cada dia, descriptivo (n=4 dias).

## 3. Predicciones congeladas y gate de L1
(`datos/a3_reglas.txt`; dP = ahorro de PnL al saltar; p = permutacion de igual n, una cola; IC90 por cierre.)
| Regla (prereg) | Conjunto | evaluadas / saltadas | PnL saltadas | dP | ganancias perdidas | p perm | IC90 cierre dP |
|---|---|---|---|---|---|---|---|
| RL0 h_w1=1 (L1) | **23-Oct fwd** | 16 / 4 | +3,30 | **-3,30** | 5,88 | 0,95 | (-15,1, +4,6) |
| RL1 h_w1 & TREND | 23-Oct fwd | 16 / 0 | - | - | - | - | - |
| RL2 h_w1 & TREND/MIXTO | 23-Oct fwd | 16 / 3 | +4,70 | -4,70 | 5,88 | 0,99 | (-16,4, +2,4) |
| RB2 / RB3 (R3) | 23-Oct fwd | 15 / 10 | -2,91 | +2,91 | 5,88 | 0,87 | (-10,4, +13,9) |
| S1p [t-2,t] (proxy) | 23-Oct fwd | 16 / 2 | -2,55 | +2,55 | 0 | 0,13 | (0,0, +5,5) |
| RL0 | B 20-22 (VISTO por W1) | 183 / 60 | -24,41 | +24,41 | 32,11 | 0,049 | (-0,9, +48,5) |
| RL2 | B 20-22 (visto) | 183 / 42 | -19,97 | +19,97 | 20,43 | 0,064 | (+0,6, +39,3) |
| RL0 | B total 20-23 | 199 / 64 | -21,11 | +21,11 | 37,99 | 0,124 | (-7,3, +47,3) |
| RB2 / RB3 | 22-Oct pm + 23-Oct (29 pos.) | 29 / 21-22 | -7,23 / -8,26 | +7,23 / +8,26 | 11,76 | 0,92 / 0,93 | (-10,6, +23,4) |
Delta EV(h_w1=1)-EV(h_w1=0) en B: 23-Oct n1=4, n0=12: **+1,89** (sign contrario al de la hipotesis; IC sin sentido); B 20-22 visto -0,500 (IC90 cierre -0,954,-0,023); B total **-0,335 (-0,817,+0,154)**: el primer dia forward ha llevado el IC de B a cruzar 0. Multiplicidad: familia de 10 contrastes (6 prereg + 2 post-hoc RX + 2 variantes S1p-lag), Bonferroni p<0,005: nada pasa; el mejor p (S1p-lag 0,006, post-hoc) tampoco.
**Gate L1 (conteo):** dias forward con posiciones: **1 de 10** (23-Oct); posiciones forward 16 (h_w1=1: **4**, h_w1=0: 12); faltan 9 dias y 36 posiciones h_w1=1 (n<40 por clase = solo descriptivo). Ritmo de B corriendo: 37/72/77 posiciones por dia (h_w1=1: 14/28/18) -> 40 h_w1=1 en ~2 dias de B, pero el cuello es el reloj de 10 dias y el CAPITAL (3,41 $ < minimo 6 $): **el reloj de B esta parado**. El reloj util es el de la POBLACION (L1b/R-TEND/R3 forward): 23-Oct entra el 24-Oct (R1 10:40Z), 10 dias = 1-Nov, lectura 2-Nov. MDE de B solo: con n1=40/n0=80 el Delta minimo detectable (IC90 una cola) es 0,63 EUR/EUR (SD pnl/coste 1,8-2,3 por pago asimetrico); n1=100: 0,40. B no tendra potencia propia: la decision tiene que salir de la poblacion y del P-REAL.

## 4. Mercado vs B (parte 3)
- **M1 nulo calibrado a poblacion** (`datos/a4_nulo_gemelo.txt`; 27.215 unidades ETH/SOL/XRP 0,10-0,30, hit por cubo 0,05; poblacion EV -0,019, acierto 20,0 % a precio 20,6 %: el maker medio de la banda NO gana). rho entre monedas del mismo cierre 0,345 -> DEFF de B 1,21 (el DEFF 11 de la poblacion es por muchas wallets en un mismo mercado, no aplica a B). B 23-Oct: obs -9,84 vs nulo -0,30 (sd 8,7-9,5): p 0,13 / 0,16; r25 p 0,36/0,17; r26 0,48/0,45; r27 (4 perdidas) P(0 de 4)=0,41 (no es raro). B 20-22: -6,18 vs -3,61, p 0,47. B total: -16,02 vs -4,11, p 0,36/0,36. **Conclusion: B no pierde mas que el maker medio a su mismo precio de forma estadisticamente distinguible (ni el 23-Oct ni en total); tampoco gana.**
- **M3 regimen fill-independiente:** bid 0,10-0,30 a T 150-210 s, todos los mercados completos con desenlace oficial (r3shadow): 22-Oct pm n=399 acierto 23,6 % (EV@bid +0,18); 23-Oct dia n=284 23,6 % (+0,19); **ventana B n=69 13,0 % (EV@bid -0,31) vs fuera n=614 24,8 %**. El bid es un coste optimista (no es el relleno). Mercado Up 51 %: no fue un dia direccional.
- **M2 gemelo (cons_x, un relleno por puja):** dia n=56, acierto 19,6 %, EV -0,092 (IC90 cierre -0,50,+0,34); ventana B n=14 (1 acierto) EV -0,643 (-1,00,-0,05); cons_r ventana -0,596; opt_x (cota optimista) -0,752 (n=22). Por hora: horas 3, 5, 6 con EV positivo en el gemelo. Emparejado: el gemelo rellena solo 4 de las 16 posiciones de B (los 4: perdidas; B -3,72 vs gemelo -4,61): **el gemelo no es B** (rellena 4/16, ver su fidelidad propia en R3_PRODUCCION).
- **M4 sesgos de B (B 20-22, visto):** lado NO +0,281 (n=79) vs poblacion -0,016; YES -0,254 (n=107) vs -0,023: B es una apuesta direccional (77 % de pares coinciden) y la diferencia YES-NO (-0,53) es exposicion al signo del dia (el 23-Oct YES 0/9, NO 1/7), no una ventaja; moneda: XRP -0,124 (n=53) vs poblacion +0,010; ETH +0,014 vs -0,046. Sin n>=40 con IC90 por cierre que excluya 0 en ninguna celda: descriptivo.
- **Descomposicion del -9,84 (`a7`):** nulo -0,30; regimen de ventana -5,3; AS tipo gemelo -5,1 (cota basada en 1/14: IC enorme); residuo +0,8. P(<=1 acierto) bajo (a) 0,13, (b) 0,33, (c) 0,66: con el acierto de la ventana el resultado es **esperable**. No es identificable aqui cuanta AS hay: la AS entra por el relleno (el acierto de los rellenos 6-7 % frente al 13 % generico), pero con n=14-16.

## 5. Evitable por regla y coste de oportunidad (parte 4; PnL total, no EV)
En el 23-Oct (-9,84 $): RL0 -3,30 (cuesta); RL2 -4,70 (cuesta); RL1 0; R3 +2,91 (pero pierde la ganadora +5,88 y las 5 que pasan pierden -5,89); S1p +2,55 / +1,10 (lag 0,5 s); **no cotizar en REVERT +9,06** (8 posiciones, 0 ganadoras; p perm 0,096) y no fuera de MIXTO +11,66 (p 0,019, sin ganancias perdidas) - **ambas POST-HOC, mias, elegidas tras ver el dia**. Contra el resto: en B 20-22 REVERT-skip ahorra +11,80 pero pierde 55,5 de ganancias (p 0,25); en la **poblacion** (misma ventana temporal, 27.161 unidades) REVERT EV +0,031, MIXTO -0,041, TREND -0,047 y saltar REVERT = -277 EUR (placebo p 0,99). EV por dia x R en B cambia de signo cada dia (REVERT -0,59, +0,31, -0,26, -1,00). **REJECTED.**
Sobre 20-23 (n=199-202, visto salvo el 23-Oct): RL0 +21,1 (ganancias perdidas 38,0; IC90 cierre -7,3..+47,3), RL2 +15,3, S1p +26,1 (31-43 saltadas; hit saltadas 6,5-11,6 % vs 22 %; p 0,028 con [t-2,t], **0,006 con [t-2,5,t-0,5], 0,236 con [t-3,t-1]**: depende de la ventana, post-hoc, y el proxy usa `t_det` posterior al casado y NO modela re-puja). Ninguna sobrevive a Bonferroni 0,005. Lo que ahorra cada regla es siempre <= lo que cuesta en ganancias perdidas salvo S1p-lag (ganancias perdidas 4,84 con +27,7): la unica pista con mecanismo (relleno con Binance en contra = AS visible) y por eso sigue como EXPLORATORY.
Cota superior de "evitable" en el 23-Oct: una regla perfecta que salte solo perdedoras ahorra 15,72 $ (no existe). El 55 % del coste rellenado no tiene senal previa (anatomia, 22-Oct): el resto es regimen+azar.

## 6. Palancas contra la seleccion adversa, con TODO el ledger de B (parte 5)
Ledger B (28 tandas de la contabilidad, 202 posiciones/221,3 $/EV -0,072) + poblacion 17-22 + proxies. Etiquetas sin ambiguedad; ninguna autoriza dinero ni cambia B.
| # | Palanca | Evidencia (n efectivo) | Etiqueta | Que falta / como conseguir potencia YA |
|---|---|---|---|---|
| 1 | Saltar longshot A FAVOR de la tendencia 15 min (|rpre|>=7,7; L1/R-TEND) | proxy sin precios 5 muestras (129 d, 349 d 2025, 40 d oficial, 28 d bookTicker) Delta -0,08..-0,17, placebo p<=0,002; precios reales poblacion 17-22 -0,133 (IC90 cierre -0,275,+0,007, 1.614 cierres); B 20-22 -0,50 (visto); **23-Oct fwd contradice (n1=4)**; B total -0,335 cruza 0; el efecto es de pocos dias (PnL total solo mejora en 5/6 dias de pob.) | **EXPLORATORY/PROMISING** | gate poblacion 10 d fwd (2-Nov); P-REAL 17 d con ASK real (runner 09:00Z, leer); extraer 22-23 Oct de `maker_ms_*` crudo antes de que rote (~4 d) y el `m5_registro_2026-10-22` fallido (zlib); replica BTC/DOGE/BNB 5m y 15m (la proxy BTC da -0,055); Jon-Becker 40 d con precios = 36 GB en streaming (decide el chief) |
| 2 | Condicionar 1 al regimen de ventana TREND (R1) | I_R -0,073 (IC90 dias -0,127,-0,020) pero el bootstrap por dias es LIBERAL (D-FUERTE: 5 % nominal = 9-11 %): p efectivo ~0,05-0,06 sin x3; TREND = 2 posiciones el 23-Oct | EXPLORATORY (debil) | R-TEND/D-FUERTE forward; modelo de D-FUERTE aun sin leer; mas dias de pob. |
| 3 | R2/R3 (bid15 mismo lado - puja <=3c; vol30>=26; hora>=4) | simulador +0,253 p=0,003, recalibrado a B ~+0,07 (-0,19,+0,35); techo 0/1,5k/11k EUR/anio; 23-Oct 0/5 las que pasan; BTC REJECTED (n=36.407) | EXPLORATORY | r3shadow ya cubre ~864 mercados/dia (n grande): 10 d validos y >=200 flag-true -> lectura 2-Nov; ampliar a BTC/15m solo como replica |
| 4 | S1 / retirar puja si Binance en contra (E1b D250) | sustitucion +0,0216/EUR (IC90 cierre 0,018-0,025), eliminacion ~azar (p=0,81) ~0,3 k EUR/anio; mi proxy sobre fills reales de B: ver 5 (ventana-dependiente) | EXPLORATORY (techo bajo) | E1b forward 24-28 Oct; con el libro WS de B ms-resuelto; validar `t_det` vs hora de casado on-chain |
| 5 | Retirada de liquidez / cancelar con la senal (L1b, S1 control) | banda 0,10-0,30: retirada real pero <=300 ms; EV de los evitados +0,106 (se pierde dinero bueno) | **REJECTED** en banda 0,10-0,30; EXPLORATORY 0,30-0,70 (B no opera) | L1b retirada tau 200/250 forward (0/10 dias) por si cambia |
| 6 | Predecir/mitigar C2 (el mercado sigue casando por debajo tras el relleno) | C2 pob -0,110 (IC90 cierre -0,190,-0,027), pero es markout ex post; AUC previo 0,51-0,60; B ya recotiza en 0,2 s | REJECTED como predictor previo | markout propio: mk30 B 23-Oct -0,43; clasificar C1/C2/C3 del 23-Oct requiere `oc_2026-10-23` (DATA_BLOCKED hoy) |
| 7 | No cotizar en REVERT / fuera de MIXTO | post-hoc de este informe; poblacion al reves | **REJECTED** | - |
| 8 | Equilibrar lados / cubrir pares | pares_huecos Delta -0,11..-0,31 (10 politicas); B YES/NO es exposicion direccional | REJECTED (cobertura) | - |
| 9 | Menos recotizacion / mas relleno (7,6 -> 15 ordenes por mercado-lado, relleno 68 % -> 43 %) | 4 dias, descriptivo | DESCRIPTIVO | medir con ledger de `repega` x relleno x markout en n>=500; ya existe la telemetria |
**Potencia ya (orden de Javi):** la unica palanca con potencia propia es la POBLACION (4-9 k unidades/dia; 1.613 cierres en 6 d) y el brazo r3shadow (864 mercados/dia, gemelo de B, desenlace oficial): ahi se decide 1, 2, 3 y 4 hacia el 2-Nov. B real aporta n=16-80 posiciones/dia con SD enorme: sirve para contabilidad y para validar la traduccion al dinero, no para decidir palancas.

## 7. Limitaciones y sesgos
- n=16 posiciones/10 cierres/1 dia: todo contraste es descriptivo; los p son de permutacion con n pequeno; un solo ganador (+5,88) decide cada signo.
- La ventana de B (06:30-08:56Z) la fija el agotamiento de cada tanda: terminar al perder introduce sesgo de parada; el escaneo de ventanas es post-hoc y con ventanas solapadas.
- M3 usa el bid (optimista); el gemelo r3shadow (cons_x) rellena 4/16 de B: solo cota. Rebate no sumado. R/etiquetas del 23-Oct usan barras parciales de bookTicker (R no NA solo para el tramo 06:30-09:00; 3 posiciones del 22-Oct con R=NA excluidas en RL1/RL2).
- S1p usa `t_det` del ledger (posterior al casado), no el reloj de bloque, y no modela re-puja: SOBRESTIMA ahorros si la mudanza ocurre en el casado y no es accionable a 65 ms.
- Los dias 20-22 ya los vio W1: cualquier cifra de B 20-22 es descriptiva y no suma al reloj forward.
- No se verifico on-chain de nuevo (se uso la reconciliacion de la contabilidad, cuyo cuadre es internamente consistente); el rebate no se puede comprobar.
- P-REAL (ask real, 17 d) y D-FUERTE tienen resultados por leer (corren solos): este informe no los usa.

## 8. Reproducir
`cd scripts; nice -n 19 ionice -c3 python3 -I a1_contab.py | a2_unidades.py | a3_reglas.py | a4_nulo_gemelo.py | a5_extra.py | a6_post.py | a7_descomposicion.py` (todos con `ulimit -v 3000000`, ~1 min cada uno). `a2` necesita las etiquetas de regimen del 23-Oct recalculadas en el scratchpad (copia de `etiquetar_regimen.py` con OUT redirigido; `regimen_lib.py` sha 750a4ecf9a5d). Semilla 20261023.
