# Expediente RE-B-SOLO-OBSERVABLE — 19-Nov-2026 (reverse-engineer, 08:40-08:55Z, solo trabajo ligero <150 MB RSS)
Estado de cierre: PARTIALLY_SOLVED · Bloqueo dominante: A (información: la parte NONE de la clase 1 no deja huella pública) · Secundarios: G (estadístico: 4 días, sin IC por días; 23-Oct sin L2), B (medición: el motor no usa el canal de «bloqueo» del L2), J (la premisa «SOLO = la AS» no está demostrada).
Código, datos y salidas: `misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/solo_observable_19nov/` (prereg, adendas, scripts con .sha256 y .pkl de filas).

## 1. Fenómeno
Bloqueo del red-team 19-Nov: el replay de B (passT_v4) ve 88/202 rellenos reales de 20-23 Oct; la clase 1 (n=98: 72 SOLO, 24 SOLO_ARRIBA, 2 DEBAJO; EV −0,176 €/€) no tiene ningún print ajeno ≤L en su tx. En noviembre no hay órdenes propias. Pregunta: ¿se puede hacer observable o acotar con rigor, para medir si F5_t o R1v2 la evitan?

## 2. Realidad observada
| cifra | origen | estado |
|---|---|---|
| 98 clase 1, EV −0,176 (pnl −17,52 €) | ver_todos_17nov/tomador_202.pkl (causa) | REPRODUCIDA |
| TP 84, EV real −0,111 | ídem | REPRODUCIDA |
| B total −0,0724 €/€ (n=202) | ídem | REPRODUCIDA |
Relojes: real_tm3 = sello exchange del print (stamp v3); L2 `cola_vs_cruce/mk` = recepción ms (bids de AMBOS tokens; no guarda vendedores reales del token); t_dec = decisión de la 1.ª colocación (s). Cobertura L2: 20-Oct..22-Oct 16:15Z, ETH/SOL/XRP; 23-Oct sin L2 (85/98 clase 1 con L2).
Hechos estructurales (motor `escalera_B/engine.py::fill_segment` l.42): un print < L rellena la orden virtual completa (trade-through). El motor NO usa el L2 del complementario.

## 3. Física: qué hace el tomador de un SOLO en un mundo sin nuestra orden
TT: si su límite pasa de L y le queda tamaño, casa bids en [tk_eq, L) → print público < L → el motor YA lo rellena en noviembre. REST: si es GTC, queda en reposo (bid del complementario a 1−tk_eq) y cruza nuestra puja virtual → visible en L2, el motor no lo usa. NONE: FAK/FOK o tomador reactivo → no existe sin nosotros → no observable por construcción.

## 4. Experimentos (prereg con sha antes de calcular)
- E-SO-1a (PREREG_SO1 16543fc6…): tras el casado, ¿sube el bid del complementario a 1−tk_eq? Clase 1 con remanente 0,745 (n=47) frente a placebo ±10-30 s 0,319. El control (i) sin remanente da 0,500 (n=30) > 0,433 → NO ACEPTA; INCONCLUSO (hay recotización genérica tras el casado).
- E-SO-1a' (ADENDA_SO1_01 f664bfad…, post hoc; ancla = Δ igual al tamaño del remanente ±2 %): 0,191 (9/47) frente a control (i) 0,052 y placebo 0,021; diferencia 0,139 < 0,15 → REFUTA el canal REST como mayoritario. Con límite exacto en L: 0,296 (8/27), placebo 0.
- E-SO-1b (descriptivo): con límite más allá de L y remanente ≤1 %, había bids en [tk_eq, L−1c] ≥ 0,5·q en 14/20 (TT).
- Partición de la clase 1 (98): TT 14 (EV −0,054), REST exacto 10 (+0,265), NONE con L2 61 (−0,115; pnl −7,79 €), sin L2 13 (−1,000; −12,47 €; 11 son del 23-Oct).
- E-SO-2 (PREREG_SO2 83f46a06…), F5_t en la colocación (proxy: tamaño del mejor bid del complementario): 3.193 órdenes válidas. Terciles: bajo 56 %, medio 35 %, alto 9,5 %. Tasa NONE/orden: alto 2,30 % (7/304), bajo+medio 1,66 % (48/2.889), ratio 0,72, p=0,37 → INCONCLUSO. Con definición estricta (TT solo con remanente ≤1 %): 1,87 %, ratio 0,81, p=0,47. El 87-89 % de las NONE caen en bajo+medio.
- E-SO-2b (ADENDA_SO2_01, post hoc; sha refrescado a52b412a… tras añadir UNA línea que declara una corrección de agrupación; el sha original no se imprimió): F5_t en real_tm3−150 ms. NONE en alto 11/55 válidas (20 %); resto de rellenos 27-28 %. EV de los rellenos por tercil dinámico: alto −0,144 (n=48), bajo −0,040 (61), medio +0,095 (74).
- Contraste C1 frente a TP (post hoc, permutación dentro de día, 5.000, semilla 20261119): −0,176 frente a −0,111, p(C1 peor)=0,64; sin 23-Oct, −0,081 frente a −0,085 (p=0,64).

## 5. Qué se puede sostener / qué NO
SÍ: (1) la clase 1 no es homogénea: ~24 % deja huella pública (TT, que el motor de noviembre ya rellena, y REST, que el motor ignora); ~72 % (NONE) no la deja. (2) F5_t no reduce la tasa NONE de forma detectable, ni en la colocación ni en la versión dinámica: la NONE se concentra en bajo/medio. (3) La EV de la clase 1 depende del 23-Oct (11/11 perdedoras, sin L2).
NO: «SOLO = la selección adversa» como hecho. Sobre 20-23 Oct la clase 1 no es más adversa que los rellenos visibles (p=0,64). La AS de B es general. Tampoco «R1v2/F5_t evitan la AS»: no medido.

## 6. Hipótesis (HYPOTHESIS_LEDGER H-SO-0..5)
H1 SOLO sintético público → NO VIABLE para la NONE (un tx público con un maker solo implica que había maker; esos ya entran en el motor como print). La sub-variante «francotirador de cotización nueva y sola» (límite = L, tamaño = el nuestro; 16 casos, EV −1,00) queda en FALTA INFORMACIÓN. H2 estrés → SOLUCIONABLE como cota. H3 fallo del motor → PARCIAL: 19/118 FN son de motor (y ganadores); de la clase 1, 14 TT ya entran en noviembre y 10 REST piden el canal «bloqueo». H4 canal de bloqueo (nueva) → minoritaria. H5 nula: la observabilidad no informa de la EV → compatible.

## 7. Solución experimental
No hay código en producción. Se propone: (a) canal «relleno por bloqueo» en el motor de noviembre (bid del complementario ≥ 1−L o ask propio ≤ L mientras la puja virtual vive), con la cordura de octubre: ≈0 eventos con la orden real viva, salvo dt≈0 tras el relleno; (b) estrés NONE uniforme por tercil.

## 8. Refutación intentada
Controles sin remanente, placebos temporales, ancla de tamaño, definición estricta frente a la prerregistrada, sin 23-Oct, permutación dentro de día. Pendiente: validación independiente (statistical-validator, red-team); verificar las unidades de tk_sz/tk_rem (acciones frente a USDC).

## 9. Veredicto y economía
PARTIALLY_SOLVED: la clase 1 queda descompuesta y acotada; la NONE no es observable sin órdenes propias. Validado 0 €. Exploratorio: estrés NONE ≈ 1,7-1,9 % de las órdenes colocadas en bajo+medio, con EV −0,115 (rango −0,176 pesimista). Nada de esto es EV de B.

## 10. Siguiente paso exacto
E-SO-3 (antes de cualquier EV de R1v2): congelar R1v2+F5_t entrenados en días públicos y aplicarlos a las 3.796 órdenes de octubre. Acepta «evita la NONE» si la tasa de cancelación a tiempo de NONE menos la de TP es ≥ 0,15, con permutación dentro de día p<0,10, y ΔPnL en € sobre los 202 rellenos reales > 0. Si no, se reporta «visibles + estrés NONE uniforme». Reabriría el caso: órdenes reales en régimen lo (prueba real ya obligatoria según Javi), L2 del 23-Oct o un feed de órdenes FAK no casadas.
