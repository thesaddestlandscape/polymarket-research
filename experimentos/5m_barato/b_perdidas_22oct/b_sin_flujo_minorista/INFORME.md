# B sin flujo minorista (25-Oct-2026) — EXPLORATORY (4 días de B; ≤21). Solo lectura, nice 19, ulimit 3 GB, nada a real, sin crons/procesos.
Prereg `PREREG.md` (sha256 666f40ea…) y `PREREG_R8.md` (cdb6bc83…) escritos antes de calcular. Salidas `datos/s8_salida.txt`, `s9_salida.txt`, `s11_r8_salida.txt`, `s11b_r8_cheap_salida.txt`; scripts `scripts/l0,s5..s11b`; datos pesados en `agentes_datos/b_sin_flujo/`.

## 1. ¿Persiste el déficit? Sí en lo medido, pero NO hay más n de B
- **B solo existe el 20-23 Oct** (ledger: 24 y 25-Oct solo `mercado_inicio/fin`, 0 órdenes; 23-Oct parcial desde 06:30Z). 17-19: B no operaba. Días de B: 4 (112 cierres); faltan 6 días de B operando para ≥10. Lo único que se extendió fue la población (24-Oct, 3.7 k mercados; cobertura desenlace 100 %).
- Fill-level (n=215, 112 cierres): cuota € DES+NUEVO de B 9,9 % vs 26,2 % esperado (coin×día×banda de la población); dif −0,163 IC90 cierre (−0,195, −0,131); por día −0,118/−0,208/−0,159/−0,092 (4/4 negativos; sin el mejor día −0,162).
- Población 24-Oct: cuota DES+NUEVO 34,1 % (sube), EV −0,20 (todas las clases ≤0): el déficit de B no es porque la población haya cambiado.

## 2. Mecanismo (lo que dicen los datos; replay FIFO BLOQUEADO)
- **B arma y cancela en 0,58 s de mediana** (3.796 órdenes armadas, vida p90 2,8 s; las rellenadas viven 1,8 s; espera armado→relleno mediana 1,9 s, p90 5,7 s, n=178 emparejados). Siguen el top en ~0,2 s (cola_vs_cruce).
- Por clase (n=178 emparejados): MIX 134 (146 €), INF 21, NUEVO 13, DES 10. Espera mediana MIX 1,96 s, INF 2,08, DES 1,54, NUEVO 0,74; T medio al relleno 98 s (MIX), 97 (INF), 128 (NUEVO), 139 (DES) desde apertura. Sin diferencia fiable de espera por clase (n=10-21).
- Flujo de OTROS que cruza el NIVEL EXACTO de B durante su vida (±1,4 s, 171 de 3.796 órdenes): cuota DES+NUEVO 33,6 % vs 28,0 % esperada (dif +0,056, IC90 cierre −0,027..+0,142). **O sea: el flujo no informado SÍ llega al nivel de B mientras está armado; a B no le rellena, le rellenan casi solo MIX (78-80 % del €).** Orientación: prioridad/cola o tamaño, no ausencia de flujo. Relleno de B con flujo de otros en el nivel 21,6 % vs 4,6 % sin él.
- **Los DES+NUEVO llegan más tarde que la vida de B**: cuota DES+NUEVO en (vida, 12 s] tras cancelar = 41,6 % vs 33,6 % durante la vida (dif pareada +0,129 IC90 cierre +0,017..+0,244, 72 cierres; placebo +60 s: 48,5 %, n pequeño). M1 se cumple, EXPLORATORY.
- **Replay FIFO de la cola: BLOQUEADO** (prereg): reloj on-chain con resolución ±1,4 s (block time; offset medio 1,69 s) frente a vidas de 0,6 s; solo ~37 de 202 rellenos reales tienen flujo ajeno visible en la ventana → recall <20 % (<60 % exigido). Las políticas sólo pueden darse como COTA OPTIMISTA (B primero en la cola, 5 acc), no como simulación.

## 3. Políticas (cota optimista; unidad cierre; 4 días; sin tope de precio; reloj corregido; IC90 cierre)
| política | fills añad. (n / €) | EV añad. €-pond. | %DES+NUEVO añadido | Δ EV de B | IC90 cierre | placebo p | BH q |
|---|---|---|---|---|---|---|---|
| Base B real (215, 221 €) | | −0,072 (IC −0,315..+0,199) | | | | | |
| P1 mantener 3 s | 77 / 65 | +0,135 | 44 % | +0,047 | (−0,074, +0,182) | 0,42 | 0,58 |
| P1 mantener 6 s | 172 / 145 | +0,049 | 39 % | +0,048 | (−0,114, +0,221) | 0,46 | 0,58 |
| P1 mantener 12 s | 300 / 253 | +0,002 | 36 % | +0,040 | (−0,157, +0,238) | 0,63 | 0,63 |
| P3 top−1c vida real | 105 / 79 | +0,062 | 23 % | +0,035 | (−0,077, +0,163) | 0,44 | 0,58 |
| P3 top−1c mantener 6 s | 236 / 190 | +0,090 | 25 % | +0,075 | (−0,097, +0,257) | 0,39 | 0,58 |
- Ninguna con señal (IC cruza 0, placebo p≥0,39, BH q≥0,58; Δ por día cambia de signo: p. ej. hold 6 s −0,24/−0,03/+0,36/−0,06). P2 «armar tarde» (T restante ≤150 s) sobre fills reales: 46 fills, EV +0,007 vs −0,127 (n=132) — descriptivo, no simulación. Mantener la orden sí trae más DES+NUEVO (36-44 % del añadido) pero ese flujo extra no es rentable por sí solo.
- **€/año honesto: validado 0 €.** Cota optimista (P1 3 s, +8,8 € por ~4 días a ~60 €/día rellenos) ≈ 0,8 k€/año, IC cruza 0, placebo p=0,42. Lejos de 200 k€.

## 4. R8 (coordinador): tras el primer fill de una PERDEDORA (roster solo días previos, z≤−2), vender el lado barato en +5..+60 s
- 13 días (12-24 Oct), 14.839 eventos (mercado-lado), roster 360-461 wallets/día. EV de vender s (maker, sin rebate) en W: **+0,0017 IC90 cierre (−0,009,+0,012), n=3.738 cierres** (IC por día igual): ≈0.
- Pareado con el mismo mercado-lado en [+65,+120]: +0,0595 IC90 (0,049, 0,071), 13/13 días — pero el «después» (−0,004) es peor por el T (flujo informado cerca del cierre), no por la perdedora: no es control de evento. Control de mercados sin evento (mismos segundos): dif +0,039, permutación p=0,002, 11/13 días, sin 2 mejores días +0,027, pero NO emparejado por banda de precio de mercado (cap de control 25× menor) → no concluyente. Control con todos los precios (s10/s11) descartado por inválido (−0,71).
- Gate R8 (EV_W − control con IC90 cierre>0 y placebo) NO cumplido de forma limpia; absoluto ≈0. Hilo: replicar con control emparejado por mercado-lado-banda y libro ms (no solo on-chain). EXPLORATORY.

## 5. Siguiente
1. Reactivar B (decisión de Javi) ≥6 días más para el gate de exposición (obs−esp < −0,05 IC90 por cierre; hoy −0,163 con 4 días).
2. Medir cola/prioridad con libro5_ms (ms; rellenos de B y flujo con clase vía tx): único modo de desbloquear el replay; no hecho por carga (libro5 3,5 GB/día).
3. A/B aleatorizado (mantener 3 s vs vida actual) dentro de B ya propuesto en b_vs_poblacion; el prerrequisito es que la clase de quien rellena se lea on-chain a posteriori.
## Limitaciones
4 días de B; 11 tomadores INF; clase por wallet; ventana ±1,4 s infla flujo en vidas de 0,6 s; cota optimista sin cola; ts on-chain en bloque; 24-Oct solo población.
