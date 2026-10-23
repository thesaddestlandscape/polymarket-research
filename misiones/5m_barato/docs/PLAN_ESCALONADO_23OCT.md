# Plan escalonado de agentes — 23-Oct (Javi: no gastar la cuota de golpe)
Foco Javi: eliminar/mitigar selección adversa de B y detectar tendencia alcista/bajista para B; lo simple primero; usar wallets ganadoras de alts. Objetivo: B → 200 k€/año (con R3/BTC según PLAN_EQUIPO_22OCT).
Reglas: máx. 2 agentes simultáneos; cada uno con tope de tokens (~150 k) y de tiempo (~60 min), checkpoint + MD final corto; el siguiente arranca SOLO al entregar el anterior. Modelo sonnet salvo validación/red-team. Análisis pesado: nice 19 ionice -c3, fuera de 06-09Z, RAM>2,5 GB, disco raíz 92 % (no generar >1 GB). B parado (13,26 $): todo offline; cualquier cambio a B = variante + /code-review + OK Javi. H39b sigue en PAUSA.
- OLA 1 (ahora): [E1] execution-engineer: calibrar simulador maker con anclas on-chain (186 rellenos B, 0xf074dc84, 0x0ab01745) — cuello de botella de todo backtest. [W1] wallet-intelligence: tendencia/régimen + qué hacen las wallets ganadoras de alts según tendencia (lo más simple primero).
- OLA 2 (al terminar ola 1): [A1] alpha-researcher: predictor simple de tendencia → regla para B (lado/skip) probada en el simulador calibrado; [S1] statistical-validator: control de órdenes no rellenadas de misma edad (¿selección adversa o supervivencia?).
- OLA 3: [R1] red-team sobre lo que sobreviva; [O1] objetivo-200k actualiza libro con cifras.
- Tras reset de cuota (26-Oct 13:00Z): event-causality (C2 predicción), market-data, H39b si B masterizada.

## Aprobado por Javi 23-Oct (cola, se lanza al liberarse hueco; máx. 2 simultáneos)
- [W2] 0x21f4c1a1 (BTC): reconstruir Binance desde maker_ms y repetir el análisis de tendencia/wallet de W1 (tendencia_wallets/INFORME.md).
- [L1] Etiquetado PASIVO de rpre y r900 en cada orden de B (proceso aparte, solo lectura del ledger de B + Binance; NO toca experimento_maker_h47.py ni B); ≥10 días antes de cualquier regla. Hipótesis a refutar: «no pujar el lado a favor de la tendencia 15 min previos con |rpre|≥~7,7 bps».
- Orden: al terminar S1 o E2 → L1 primero (no se pierden días), luego W2; A1 espera a E2.

## Cola Q-TECHO (Javi 23-Oct): NO lanzar hasta que terminen P-REAL y D-FUERTE
Q-TECHO = techo de precio por orden con q calibrada al fill (debe batir al mid y a R3). Lanzado por error a las 08:05Z y detenido a las 08:10Z; relanzar al entregar P-REAL y D-FUERTE, reutilizando sus informes (detector_regimen/INFORME_PREAL.md e INFORME_DFUERTE.md). Salida: b_perdidas_22oct/q_techo/INFORME.md. Prompt guardado en la sesión del chief (volver a generarlo desde esta nota).

## Horario de carga 23-Oct (Javi: "ordénalos para que no consuman todos los tokens")
- 09:00Z: W2 runner (CPU, sin tokens) + P-REAL pesado. 09:30Z: D-FUERTE pesado. 09:37Z: retomar W2 (informe).
- X-SALIDA (salida a nivel de curva de saldo/tanda, cheap5m-risk-economics): EN COLA, se lanza al entregar P-REAL o D-FUERTE (el primero). Detenida a las 08:57Z antes de avanzar.
- Q-TECHO: en cola, al entregar los dos primeros.
- Máx. 2 agentes con tokens a la vez; los runners pesados no cuentan como agentes pero no se solapan más de 2.

## DECISIÓN Javi 23-Oct ~09:35Z: candidatas para B = R0, R2 y su COMBINACIÓN
- Se prueban las dos y una combinación. R0 = saltar CON (lado a favor de rpre, |rpre|≥7,7 bps) siempre; R2 = saltar CON solo en ventanas TREND o MIXTO (REVERT sigue pujando); combinación = por definir por Q-TECHO/D-FUERTE (p.ej. R0/R2 + techo de precio por q calibrada + r60 de W2).
- Evidencia al ask real (P-REAL, 17 d, ETH/SOL/XRP): Δ(CON−CONTRA) −0,234; R0 placebo p=0,000, 16/17 días; R2 placebo p=0,044 (no pasa Bonferroni ×3); R1 no pasa. BTC con signo contrario (B no opera BTC).
- Gate previo a variante de B: forward 10 días (L1/L1b/P-REAL, evaluable ~2-3 Nov) + /code-review + OK Javi. B sin dinero (3,41 $) hasta la recarga.
- Orden: PRIMERO masterizar B (R0/R2/combinación + AS + escalado a 200k); DESPUÉS H39b (sigue en pausa).
- X-SALIDA: ninguna regla de salida a nivel de curva crea EV (candidata = NINGUNA); B real EV −0,068/€, Kelly 0; hueco ≥189 k€/año; capital y EV son las palancas.
