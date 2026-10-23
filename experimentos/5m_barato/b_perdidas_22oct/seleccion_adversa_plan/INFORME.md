# Selección adversa de B: mapa de palancas y análisis E1 (cancelar en ms antes del relleno). 22-Oct-2026, ~15:50Z
Estado: **EXPLORATORY**. Ninguna palanca convierte a B en EV positivo fuera del nicho R2/R3. Todo el trabajo es en solo lectura: no se ha tocado B (`experimento_maker_h47.py`, sha c82f5dc5f304b8a6), el supervisor, los procesos, los crons, la config ni las órdenes. Ejecución con `nice -n 19 ionice -c3 ulimit -v 3 GB`, RSS máximo 0,5 GB, unos 10 s por día.

## 0. Respuesta corta (honesta)
- **Eliminar del todo la selección adversa no es alcanzable con las señales disponibles.** En el simulador a ms (6 días, 4.408 mercados, 3.123 rellenos), los rellenos aciertan el 15,8-18,4 % y las pujas no rellenadas el 43,7-52,2 %. La brecha de 0,24-0,26 €/€ ya estaba medida.
- El **55 % del coste rellenado** no tiene ninguna señal de Binance en los 10 s previos al relleno, o no tiene ninguna señal. Aun así su EV es de −0,14/−0,16. Esa pérdida es invisible antes del relleno con el top del libro, la cinta y Binance. Es la parte **estructural**.
- La parte **atacable** tiene dos trozos que se solapan:
  - **(i) R2/R3 (nivel del bid15).** Ya está en forward. Aquí, los rellenos con R2 verdadero dan EV −0,070 frente a −0,244 sin R2, y son el 28 % de los rellenos.
  - **(ii) S1, nueva: retirar la puja 2 s cuando Binance se mueve ≥2 bps en contra.** Da +0,03/+0,04 € por € de coste base, es decir, recupera un 13-16 % de la brecha. Ese valor está **solo fuera de R2**: dentro de R2 suma +0,002 €/€. Las dos ven la misma información.

## 1. Mapa de palancas (prioridad = EV incremental × evidencia ÷ coste de prueba)
| # | Palanca | EV incremental (€/€ del coste base) | € al año a escala B (~42 €/día de coste) | Evidencia | Coste de prueba | Estado |
|---|---|---|---|---|---|---|
| 1 | **R2/R3: no pujar si el bid15 del mismo lado queda >3c por encima de la puja (+ vol30, + hora ≥4)** | población +0,114 (IC90 días +0,079..+0,155); sim ms aquí: rellenos R2 −0,07 frente a −0,24 | ~0,3 k€ (retiene ~19 %); el techo del nicho son 15-25 k€ con K×5 | PROMISING, forward 02-Nov | 0 (ya en marcha) | seguir |
| 2 | **S1: cancelar 2 s tras ≥2 bps de Binance en contra (E1, nueva)** | +0,032 DESC / +0,042 TEST; fuera de R2 +0,052; dentro de R2 +0,002 | 0,5-0,6 k€ (B actual, sin R2); 0 si B pasa a R3 | EXPLORATORY post-hoc, 6/6 días, inversión ≈0, B real coherente | extraer el registro ms cada día (lo hace el chief) | preregistro E1b congelado |
| 3 | **Rebate maker del 20 %** | +0,011 esperado (2,15 $ en 180 posiciones) | ~0,17 k€ | **0 $ recibidos on-chain** hasta 22-Oct 15:06Z: falta, no es 0 | 0 (verificar cómo y cuándo se paga) | verificar |
| 4 | R1 (actividad <26 acc en 30 s; noche 00-04) | ~12 % de la brecha | ~0,2 k€ | PROMISING débil, forward | 0 (cron) | seguir |
| 5 | Correlación (B = una sola apuesta direccional) | **0 en EV** | 0 | `tandas`: 1 por cierre, info +0,009 (IC90 cruza 0) | — | solo palanca de varianza/capital (decisión de Javi) |
| 6 | Recompensas de liquidez | 0 a 5 acc (el mínimo son 50) | 0 | — | — | ligado a H45 (escalar K hace crecer la selección adversa) |
| — | REJECTED (no repetir) | V9, V3, salida tras el relleno (40 reglas), tandas/topes/rachas/stop diario, profundidad k, puja estática, spread, tamaño del top, imbalance, confirmación previa, cancelar por bid15, cobertura con el lado contrario, logit, tomadoras informadas, BTC con R2; **S2 (flujo tomador en contra ≤2 s) y S3 (barrido en otra moneda ≤2 s) en E1** | | | | |

**Lo que se ve ANTES y lo que solo se ve DESPUÉS.**
- Antes: Binance en contra en 0,1-2 s (21 % del coste rellenado; EV −0,23 frente a −0,14 de los rellenos sin señal en 10 s) y el nivel del bid15 (R2).
- Solo después: el barrido ≥3,5c, Binance a +30 s, Δbid a +5..60 s (AUC hasta 0,87) y el racimo multimoneda. Nada de eso se puede usar.
- Un 8 % del coste tiene su señal a menos de 100 ms del relleno: demasiado tarde para cancelar.

## 2. E1, ejecutado con preregistro (`PREREG_E1_CANCELAR_MS.md`, sha256 31d09a9f…f666, congelado antes de calcular)
- **Instrumento.** Simulador nuevo a ms, `scripts/e1_sim.py`. Usa el registro ms de 17-22 Oct (el 22 hasta 14:40Z), con libro, operaciones del WS y aggTrade de Binance, todo por recepción.
  - La puja es tipo B: top −k ticks, asentado de 1,5 s, banda 0,10-0,30, T 298-65 s.
  - Relleno CONS por print que atraviesa: SELL propio < puja, o BUY opuesto > 1−puja, con la puja viva 50 ms antes. Incluye contrafactual: tras el enfriamiento la puja vuelve y puede rellenarse después.
  - Desenlace oficial: 6 mercados del 22-Oct sin desenlace, excluidos y contados.
  - **Fidelidad** frente a B real: relleno 70-72 % (B 61-72 %); acierto de rellenos frente a no rellenos 15,8/43,7 % (B 21,7/37,6 %); precio 0,21 (B 0,209). El simulador es más duro que B, así que solo cuentan los efectos relativos.
- **Familia de 7 reglas.**
  - S1 = Binance de la misma moneda ≤ −2/−4 bps en 0,5/2 s.
  - S2 = ≥20 acc tomadoras contra nuestro lado en 0,5/2 s.
  - S3 = ≥20 acc contra el mismo sentido en las otras 2 monedas del cierre en 2 s.
  - Parámetros comunes: retirada a +100 ms (estrés 250 ms), vuelta a los 2.068 ms.
  - Controles: inversión (la señal a favor) y 8 desplazamientos temporales de ±1-4 min.

**Resultado del gate preregistrado.**
- En DESC (17-19) se eligió **S3**: +0,040 €/€, IC90 por cierre (+0,017, +0,060), p familiar 0,11 (con 8 desplazamientos no puede bajar de 0,11).
- En TEST (20-22) da **−0,003 €/€**, IC90 por cierre (−0,032, +0,024), días +12,1/−5,2/−10,8. Falla G1-G4. **S3 queda REJECTED.**
- **S2 queda REJECTED**: TEST −0,010 €/€ en sus dos ventanas.

| Regla (D=100 ms) | DESC €/€ (IC90 por cierre) | TEST €/€ (IC90 por cierre) | días + | inversión D/T | placebo máx. D/T | D250 D/T | retiene coste |
|---|---|---|---|---|---|---|---|
| S1 −2 bps, 2 s | **+0,032** (+0,001, +0,059) | **+0,042** (+0,010, +0,073) | 3/3 y 3/3 | +0,002/+0,003 | +0,015/+0,012 | +0,024/+0,049 | 0,87/0,83 |
| S1 −2 bps, 0,5 s | +0,014 (−0,008, +0,034) | +0,028 (+0,001, +0,053) | 3/3 y 3/3 | 0,001/−0,001 | +0,011/+0,009 | | |
| S1 −4 bps, 2 s | +0,002 | +0,014 | | | | | |
| S3 (elegida) | +0,040 (+0,017, +0,060) | −0,003 (−0,032, +0,024) | 3/3 y 1/3 | +0,006/+0,009 | +0,026/+0,007 | | |

**POST-HOC, no gate (`scripts/e1_posthoc.py`): S1 −2 bps, 2 s.**
- Positiva en las 3 monedas de ambos periodos (ETH +17,5/+26,3 €, SOL +25,5/+11,7 €, XRP +12,8/+24,3 €) y robusta a 250 ms de latencia.
- Inversión y placebos ≈0. Retienen el 97-100 % del coste, frente al 83-87 % de S1. **Los rellenos se concentran justo después de un movimiento de Binance en contra**: es el mecanismo, no un recorte de volumen.
- Las quitadas tienen EV −0,224 (acierto 15,8 %) y las retenidas −0,167.
- **El 51 % de lo quitado vuelve a rellenarse 2 s después**, con EV −0,20: el barrido sigue. Eso se come la mitad del ahorro bruto.
- **B real** (144 de 166 rellenos con print WS; 22 sin print, missing):
  - Con señal antes del print: n=20, acierto 15 %, EV −0,44, −9,75 $.
  - Sin señal: n=124, EV +0,15, +21,3 $.
  - Son 3 días y es descriptivo.
- **Solape con R2:**

  | Subconjunto | Rellenos | EV base | Efecto de S1 |
  |---|---|---|---|
  | R2 verdadero | 880 | −0,070 | +0,002 €/€ |
  | R2 falso | 2.112 | −0,244 | **+0,052 €/€** (DESC +48,9 €, TEST +64,1 €) |

  S1 complementa a la B actual (sin R2) y **no suma nada si B pasa a R3** (canibaliza).
- **Por qué no es la regla elegida.** Es 1 de 7 reglas vistas en los dos periodos, así que es una hipótesis post-hoc. Su confirmación está congelada en **`PREREG_E1b_CONFIRMACION_S1.md`** (sha256 b39021f8…be95), con días ≥23-Oct, gate ≥5 días con IC90 por día y por cierre >0 y R2-falso >0, y primera lectura el 28-Oct.
- **Viabilidad de latencia.**
  - La cancelación maker tarda 60 ms y no paga el taker delay. El efecto se mantiene a 250 ms.
  - Hay entre 1,5 y 2,7 mil episodios al día por moneda y lado. Mientras hay puja viva, la puja queda fuera el 6-10 % del tiempo.
  - Habría que añadir a la variante un WS aggTrade de Binance (ETH, SOL, XRP) y comprobar el ritmo de órdenes (riesgo de 429).

## 3. Qué es estructural y qué es atacable (números del simulador ms, 6 días)
- **Estructural, ~70-85 % de la brecha fuera del nicho.**
  - Rellenos sin precursor visible en 10 s: 55 % del coste, EV −0,14/−0,16.
  - Rellenos con la señal a menos de 0,1 s: 8 %, demasiado tarde.
  - Barridos de tamaño que solo se ven al casar.
  - Para ir más allá haría falta L2 o la posición en cola, que están DATA_BLOCKED (el registro solo guarda el top), o no cotizar.
- **Atacable.**
  - R2/R3 mueve el volumen al 19-28 % donde la brecha casi se cierra (población +0,114; aquí −0,07).
  - S1 recupera +0,03/+0,04 €/€ en el resto, aunque la sustitución se come la mitad.
  - Rebate: +0,011 si llega a pagarse.
- **Potenciar lo que gana.** B lleva hasta hoy 179 posiciones liquidadas: EV +0,0076, PnL +1,49 $, +0,0185 contando el rebate esperado (`contabilidad_wallet_dedicada/posiciones.csv`, 15:06Z).
  - El nicho que gana es R3 y su escalado (H45, K×5), que dependen del forward del 02-Nov.
  - La hora 04-08 y ETH/SOL **no replican en la población** (`tandas` §1, `anatomia` §3): no se proponen como corte.

## 4. Siguientes experimentos (máx. 3), elegido y valor de la información
1. **E1b, forward de S1 (ELEGIDO).** Coste: correr a diario `../salida/scripts/extraer.py D` y `desenlaces.py D` antes de que rote el registro ms (~4-5 d), y después `e1_sim.py`/`e1_eval.py` adaptados a los días forward (el chief decide el cron). Hay una probabilidad grande de resolver la duda en 5-10 días (6/6 días previos coherentes; el efecto es de 1-2 € al día en el simulador universal). Aporta poco al hueco de 200 k: unos 0,5 k€/año a escala B y unos 7 k€/año de pérdida evitada si se cotizara en todos los mercados a 5 acc. **Reduce pérdidas, no crea edge**, y no se suma a R3.
2. **Verificar el rebate.** Coste 0: leer las reglas de pago del programa y esperar los movimientos on-chain. Si se paga, aporta +0,011 €/€ a todo el maker, y cada línea maker debe sumarlo a su EV.
3. **R3 forward (ya en marcha).** Es la única palanca que crea EV positivo en un nicho: techo de 15-25 k€/año con escala. Decide el diseño de B tras N=500.

Nada de esto cierra el hueco hacia los 200 k: el límite es la capacidad del bote maker de las alts y BTC, que no tiene un conductor de selección adversa propio (H63).

## 5. Variante de diseño (no implementada; solo tras E1b CONFIRMADA + N=500 + `/code-review` + OK de Javi)
B_S1 sería un fichero nuevo que importa B:
- **Entrada:** WS aggTrade de Binance por moneda.
- **Disparo:** retorno firmado en 2 s ≤ −2 bps → DELETE de la puja viva de esa moneda y bloqueo de 2.068 ms.
- **Fail-closed:** si Binance lleva más de 2 s sin datos → no cotizar.
- **Ledger:** cada `cancela_s1` lleva retorno, ventana, hora de recepción y edad del dato.
- **Si B pasa a R3:** no apilar S1 salvo que E1b muestre un incremento >0 dentro de R2.

## 6. Reproducir y ficheros
Todo en `/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/seleccion_adversa_plan/`:
- Preregistros (en solo lectura): `PREREG_E1_CANCELAR_MS.md` + `.sha256` y `PREREG_E1b_CONFIRMACION_S1.md` + `.sha256`.
- Comandos: `scripts/e1_sim.py DIA…` → `datos/e1_D.csv.gz`; `scripts/e1_eval.py` → `datos/e1_eval.txt`, `datos/e1_resultados.json`; `scripts/e1_posthoc.py` → `datos/e1_posthoc.txt`. Hashes en `HASHES_E1.txt`.
- Entradas, sin modificar: `../salida/datos/ms_2026-10-17..22.npz`, `unidades_b.csv`, `desenlaces_extra.json`, `/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json`.

**Límites.**
- Simulador CONS sin cola, más duro que B.
- Binance solo de la misma moneda (BTC no está en el npz).
- El 22-Oct es parcial.
- p familiar con resolución mínima de 0,11.
- B real es descriptivo (3 días, n=144).
- Los días de E1 se solapan con los que eligieron R2: el solape S1×R2 es descriptivo.
