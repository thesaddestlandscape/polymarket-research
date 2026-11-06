# Expediente RE-Q11 (toxicidad del relleno y mecanismo de PG_O50) — 2026-11-05
Estado de cierre: EVIDENCE_INSUFFICIENT · Bloqueo dominante (A-K): F (selección adversa de colocación) · Secundarios: G (días gastados, post hoc, multiplicidad), B (realismo del relleno "rancio" en simulación), C (régimen de dirección no separable).
Informe: `misiones/5m_barato/informes/Q11_toxicidad_fill_RE_05nov.md`. Código y datos: `experimentos/5m_barato/q11/toxicidad_re/` (DISENO_TOX.md sha 07bde82a8c3b7defc804081982c9511444c7bc600959ea6d576f8f3d532081e5, HASHES.txt). Los prerregistros congelados de esta carpeta (PISTAS, GIRO, SOL013 y addenda) NO se tocaron.

## 1. Fenómeno
Escalera G0 (niveles 0,10/0,13/0,16/0,19, 5 acc, puerta A_R1ws), ETH/SOL/XRP 5m, 26-Oct..04-Nov: −166,9 €, EV −0,076. La puerta geométrica PG_O50 (post hoc) da +129,5 € frente a −71,5 € de G0 en 7 días. Pregunta: ¿qué hace tóxico un relleno y por qué funciona PG_O50?

## 2. Realidad observada
- Datos: `barrido_corr/out/A_all.pkl`, que reproduce dec2 G0 10/10 días; dec2_D.pkl (`edad`, `lagj`; unión 2.938/2.938); RC5c/RC5d; libro D del motor escalera_B, solo leído, para mid a tf−300 y markouts. Desenlace capt_outcome: cobertura 100 % de los tokens 'ok' (los demás se excluyen en origen). Hora mala excluida en origen (30-Oct, 01 y 02-Nov con cobertura baja).
- Reproducción:

| cifra citada | artefacto → crudo | reproducida | estado |
|---|---|---|---|
| G0 −166,9 € / EV −0,076 (sin bloque n 2.922) | A_all.pkl ← passA.py | −166,9 / −0,076 (n 2.922, −165,6) | REPRODUCIDA |
| GEO6 ΔPnL +164,2 € (10 d) | RC5d ← passC5d.py | +164,9 (quitados − añadidos) | REPRODUCIDA (±0,7 € por emparejamiento) |
| PG_O50 +129,5 €, 602 rellenos, Δ +201,0 | RC5c ← passC5c.py | +129,5, 602, Δ +199,3 (base G0 sin bloque) | REPRODUCIDA (±1,7 €) |
| «thru1» −0,123, n 2.308 | ana_c1.log | no recomputada (categorías propias por rel) | NO_REPRODUCIDA (no necesaria) |

- Relojes: tf = hora re-sincronizada, ~100 ms tarde de mediana en el 45 % con fallback, según la auditoría AMBER. Por eso todos los rasgos del libro van a tf−300. `edad` = tf − t_arr de la propia orden. `lagj` = recepción de Binance hasta tf: es la condición del instante del relleno, no un precursor. P-C usa Chainlink `source=chainlink` por recepción (x_cl_*).
- Hechos: tablas del informe §1-3. Inferencias (marcadas): «AS de colocación» como mecanismo, y que la parte extra de PG_O50 sobre GEO6 sea colocación y no régimen.

## 3. Qué se puede sostener / qué NO
- SÍ (exploratorio): la pérdida que quitan PG/GEO es ~75 % información y ~25 % descuento. Sale de rellenos quitados, no del efecto hueco. Los rellenos tras un salto adverso ≤3 s son AS pura (información −0,33).
- NO: que la posición respecto al bid en el instante del relleno identifique la AS (K1: es precio de entrada). Que PG anticipe barridos. Que P-C sea un filtro de microestructura (es dirección). Que T1 con calma de 3 s mejore a T1 (techo +19 € en 10 días; 2 s ya pierde).

## 4. Diagnóstico
Bloqueo F (AS de colocación) con G (sin días limpios). Ni más rasgos ni un modelo mayor resuelven G: la herramienta es el forward congelado. Un backtest idealizado tampoco resuelve B (realismo del relleno rancio): hace falta red-team o rellenos reales.

## 5. Árbol de hipótesis
H-TOX-0..7 en HYPOTHESIS_LEDGER (la nula, H-TOX-0, sigue abierta).

## 6. Experimentos
E-RE-Q11-TOX1 (diseño con sha previo; los 4 contrastes no pasan alfa/4). TOX2-TOX4: descriptivos post hoc. Detalle en EXPERIMENT_LEDGER.
- Chequeo de identidades: la descomposición descuento + información + rebate = EV es contable; no decide por sí misma. Se usa solo para comparar grupos.
- Hora del diseño: mtime de DISENO_TOX.md, 2026-11-05T14:01Z, con su sha. Lo NO EJECUTADO: inversión explícita por contraste (redundante con el signo de la diferencia), markouts por día.

## 7. Solución experimental
Ninguna implementada. Propuestas de diseño: añadidos al prerregistro forward de PG_O50 (descomposición, control de régimen por lado y día, markouts); T1_r3000 en dry-run con valor de la información bajo; evaluación descriptiva de P-C con markouts.

## 8. Refutación intentada
- Efecto hueco: refutado (los añadidos restan).
- Tamaño BASE optimista: el signo se mantiene al capar q a sh_tx.
- Régimen: ΔPnL positiva en ambos lados y en el 31-Oct; aun así, no identificable.
- Dependencia de días: GEO6 sin 2 mejores días +77,6 €, 9/10.
- Placebo de contrastes: hecho.
- Pendiente: realismo del relleno rancio (red-team).
- Validación independiente: pendiente (statistical-validator / red-team, a petición del chief).

## 9. Veredicto y economía
- Validado: 0 €.
- Exploratorio: GEO6 deja EV ≈0 (−2,7 € en 10 días); PG_O50 +129,5 € en 7 días, post hoc.
- Contrafactual: techo de la calma de 3 s ≈ +19 € en 10 días.
- Capacidad: no medida.
- Contribución incremental: sin estimar.

## 10. Siguiente paso exacto / qué lo reabre
1. El validador incorpora (a)-(c) del informe §5 al prerregistro forward de PG_O50 antes del 06-Nov.
2. Red-team sobre el relleno rancio.
3. Se reabre con ≥10 días forward (en especial días en que el NO gane en G0), con L2 (≈16-17-Nov) o con rellenos reales.
