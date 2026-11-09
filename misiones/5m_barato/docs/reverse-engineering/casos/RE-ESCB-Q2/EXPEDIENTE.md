# Expediente RE-ESCB-Q2 — 2026-11-04 (reverse-engineer, Q2)
Estado de cierre: NO_ECONOMIC_EDGE_DETECTED (escalera_B) + candidata v2 prerregistrada (forward pendiente) · Bloqueo dominante: G (estadístico: EV>0 depende de 2 días) · Secundarios: F (AS residual ≈0 tras calma), E (latencia ≤100 ms y fills reales no medidos)
## 1. Fenómeno
escalera_B modo G (pujas 5 acc 0,10/0,13/0,16/0,19, lado barato 5m ETH/SOL/XRP, gate A_R1ws, A3 2 bps SOL+XRP), BASE, cinta re-sincronizada sa_ms, cancel 60 ms, 26-Oct..01-Nov (7 días GASTADOS).
## 2. Reproducción
| cifra | artefacto | reproducida |
| G −0,024 €/€, 797 unidades, 1.599 € | A3_guarda/ret_cinta_corregida/out/esc_resumen.txt (ret60 BASE) | REPRODUCIDA: G compuesto = dec2 T2 (SOL/XRP) + G0 (ETH) → −0,024, 2.149 rellenos, 797 unidades, 1.599,4 € (/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/escalera_B_q2/out_descomp_q2.txt) |
| T1 sin 0,19 +0,149 | calma_exec/out_profundidad_vs_latencia.txt | REPRODUCIDA (/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/escalera_B_q2/out_ana_v2_repro_gastados.txt) |
Relojes: libro y Binance = recepción (sa_ms, x_ c[7]); relleno = cotización sa_ms que cruza a bid≤pmin del tx en [t_ws−400, t_ws] (si no, t_ws−63). "barrido" = nmk≥3 makers en el tx (ex post, NO observable antes). "mov" = relleno de G que la variante T1 (calma 1 bps) elimina (definición por la política, no por un rasgo NaN).
## 3. Dónde está el −0,024 y dónde el dinero (EV ponderado por €, IC90 bootstrap por cierre / por día) — /root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/escalera_B_q2/out_descomp_q2.txt
- Total G: −37,8 € (n=2.149, 506 cierres), IC cierre [−0,19;+0,16], días [−0,18;+0,14], sin 2 mejores −0,172, 2/7 días +.
- Barridos: +91,4 € (n=158, 7 %), EV +0,762 IC cierre [+0,21;+1,32], día [+0,33;+1,17], 6/7 d. No barrido: −129,3 € (n=1.991), −0,087.
- Movimiento Binance (1 bps): −100,4 € (n=724), −0,184; de ello mov×no-barrido −123,8 € (n=677), −0,244, IC cierre [−0,43;−0,03], día [−0,44;−0,06], 1/7 d  ← TODA la pérdida y más.
- Calma×no-barrido −5,4 € (n=1.314) EV −0,006 [−0,19;+0,19]; calma×barrido +68,0 € (n=111) +0,819 [+0,22;+1,45] 6/7 d.
- Nivel: 0,19 −50,9 € (−0,083; en calma −0,100, n=423); 0,13 calma +0,231 (n=337), 0,16 calma +0,175 (n=369), 0,10 calma +0,007. SOL 0,19 calma −64,2 € (−0,556, IC<0, 1/7 d) es la celda peor (24 celdas miradas: multiplicidad).
- Tiempo desde apertura: 180-239 s −72,4 € (−0,145; en mov −0,244, en calma −0,106); 120-180 s×mov −0,438 IC<0.
- Edad de la orden: <1 s −0,188, 5-30 s −0,206 (−152 €), >30 s +0,230 (+124 €, 5/7 d). En T1: no-barrido <1 s −0,348 (n=149) = rearmes que se rellenan enseguida.
- Último salto ≥2 bps adverso <1 s antes: −0,511 (n=167, IC<0) (sobre todo ETH, sin A3 en G).
## 4. Diagnóstico: qué le falta EXACTAMENTE
(a) Quitar los 677 rellenos no-barrido durante movimiento adverso de Binance (−124 €): la calma 1 bps lo hace (INV −0,25..−0,38, IC90 cierre <0 en todas las variantes; dEUR vs G0 7/7 días) — hecho robusto, exige cancelar ≤100 ms (−100 ms aún +; c300 cae a +0,013).
(b) Lo que queda NO es edge: no-barrido en calma ≈0 (−0,006; en T1 +0,007) y su PnL lo ponen 2 días (26-Oct +87,8 €, 01-Nov +46,5; los otros 5 negativos) = dirección del día. El dinero estable es solo el barrido (8 % de rellenos, +0,8/€, no observable ex ante: línea cerrada 03-Nov).
(c) Por eso TODA variante (T1, T05, sin 0,19, 0,13/0,16, ap<180, rearme 2 s) tiene EV sin 2 mejores días <0 (−0,006..−0,149) (/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/escalera_B_q2/out_v2_explora.txt). EV>0 robusto exigiría que el no-barrido en calma fuese >0 sin los días de dirección, o subir la fracción de barridos: ninguna palanca observable lo consigue con estos datos.
No responder con: más filtros de colocación (450 reglas sin supervivientes), backtest idealizado (R11: simulador optimista en B, real −0,072 vs estricto +0,040).
## 5. Hipótesis (ver HYPOTHESIS_LEDGER): H-ESCQ2-1 AS = rellenos durante movimiento (sostenida, robusta); H-ESCQ2-2 residual calma = dirección del día (sostenida in-sample); H-ESCQ2-0 nula (V2 no tiene edge fuera de muestra: prior favorable).
## 6. Experimentos
- E-ESCQ2-DESC (descomposición, exploratorio, días gastados) y E-ESCQ2-V2 (prereg /root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/escalera_B_q2/PREREG_ESC_V2.md sha 3bfcb173…; juez ana_v2.py sha 1dedabb6…; forward ≥03-Nov sobre las salidas del cron 11:45Z forward_calma_diario.sh; NO EJECUTADO en forward: 03-Nov BLOCKED sin ms/x).
- Identidad: filtrar L en el pkl = quitar el nivel (niveles simulados independientes, rem=5 por nivel en esc_dec2.py).
## 7. Solución experimental: política v2 = T1 sin 0,19 (tamaño 5 acc igual por nivel; armar con A_R1ws ∧ calma; desarmar al caer gate o movimiento adverso ≥1 bps +60 ms; rearmar tras 1 s). Código: solo juez de lectura; ejecución = calma_exec (Q3), sin tocar engine congelado.
## 8. Refutación intentada: sin 2 mejores días (FALLA en muestra); placebo (V2 +0,149 vs PLA +0,012, 5/7 d); inversión (−0,329, IC sup −0,118); −100 ms (+0,093); c300 (+0,069); rearme 0/2 s (peor); concentración por día del no-barrido (2 días). Validación independiente: NO hecha.
## 9. Economía: validada 0 €. Exploratoria (gastados): V2 +115,9 €/7 d sobre 778 € (≈+16 €/día BASE, sin 2 mejores negativo) — NO extrapolar. Contrafactual: quitar mov = +100 €/7 d sobre G. Capacidad: 5 acc/nivel, ~170 rellenos/día. Contribución incremental: no sumar con T1 ni A3v11 (mismos eventos).
## 10. Siguiente: Q4 market-data (desbloquear ms_D/x_D para 03-Nov+ y cobertura on-chain 83 %); correr ana_v2.py 2026-11-03 <D> cuando haya ≥10 días (~14-Nov); reabre escalera_B solo si V2 pasa sin2>0 fuera de muestra o aparece un observable ex ante del barrido. Pista exploratoria (no prerregistrada): edad de orden >30 s +0,23 vs rearmes <1 s −0,35 → "no rearmar rápido / órdenes que reposan"; solo con días nuevos.
