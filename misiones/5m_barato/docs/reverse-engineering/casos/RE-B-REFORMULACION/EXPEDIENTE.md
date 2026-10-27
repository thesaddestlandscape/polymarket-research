# Expediente RE-B-REFORMULACION — 26-Oct-2026 (cheap5m-reverse-engineer)
Estado de cierre: PARTIALLY_SOLVED · Bloqueo dominante (A-K): H (económico: la AS bien medida se come más que todo el margen del nivel y, quitándola, B queda en ≈0) · Secundarios: J (formulación previa), B (unidad orden vs puja en la «etiqueta virtual»), E (mecanismo del barrido sin reloj de exchange), G (n de B = 195 rellenos, 4 días), K (load5 5-7 >4: E03 no ejecutado)
PARTIALLY_SOLVED = formulación corregida, descomposición reproducible y prerregistrada, inventario hecho; la palanca NO está resuelta y nada está validado de forma independiente.

## 1. Fenómeno
B (H47-B, wallet dedicada 0x659a…297f, maker 5 acc 1-2c bajo el mejor bid, ETH k=2 / SOL,XRP k=1, pc 0,11-0,29, 20-23 Oct) pierde: −16,02 € sobre 221,30 € (posiciones, EV −0,072) y −13,05 € sobre 213,3 € (órdenes corregidas, EV −0,061). La pregunta: ¿qué partes de lo hecho en B dependían de la formulación «AS = brecha rellena − no rellena (−18..−28 pp)», y cuál es el problema económico correcto?

## 2. Reproducción y datos
| conclusión citada | artefacto → crudo | cifra reproducida | estado |
|---|---|---|---|
| P(fill) real 5,1 % | etiquetado_B 20-23 → ledger | 0,0514 por ORDEN (3.796) | REPRODUCIDA |
| «etiqueta virtual 52,8 % vs real 5,1 %» (RT_26OCT §2, mitigar_as M0) | F8 vida 60 s vs B orden | **B por PUJA (mercado-lado, 10,4 órdenes/puja): 0,536 (n=364; por día 0,68/0,55/0,49/0,46)** | NO_REPRODUCIDA como discrepancia: es comparación de unidades |
| EV B −0,072 / −0,030 | posiciones.csv / b_vs_poblacion | −0,0724 (n=202); órdenes corregidas −0,0612 (n=195; diferencia 0,011 ≤0,02: Q3 OK) | REPRODUCIDA |
| «AS por relleno −0,14/−0,08/−0,07/−0,04» (q_techo §6) | relleno − bid NO condicionado | no recomputado; por definición es contra un contrafactual no capturable | NO_REPRODUCIDA (no aplica como premio) |
- Código: `scripts/e01_descomp.py`, `scripts/e02l_markout.py` (hashes `HASHES.txt`); salidas `e01_salida.txt`, `e02l_salida.txt`. Ligeros (<1 s), solo lectura.
- Relojes: m_arm = mid del libro en `puja_post` (t_dec, decisión); m_det = `puja_fin.rellenos.mid0` = mid en la DETECCIÓN del relleno (recepción; verificado en `polymarket-research-dev/experimento_pares_cola_15m.py:1103`, `lib.mid_en(tok, t_r)`); mid_5s/30s/120s desde t_det. Sin hora de exchange del relleno (E03).
- Desenlace oficial 3.796/3.796 órdenes (100 %), 195/195 rellenos.
- **Discrepancia propia**: PREREG_E02L suponía mid0 = mid al armar; es mid en la detección. La regla R1 de E02L queda NO DECISORIA tal como se escribió; se usa solo como perfil post-detección (marcado).

## 3. Reformulación económica correcta (por € de relleno, ponderado por €, maker fee 0)
EV_f = SPREAD + SEL + COND (identidad contable; E01, 195 rellenos, 129 cierres, IC90 bootstrap por cierre):
| componente | qué es | valor €/€ | IC90 | pp a p=0,205 | ajustable con |
|---|---|---|---|---|---|
| SPREAD | m_arm − pc (nivel 1-2c bajo el bid) | **+0,107** | (+0,102,+0,113) | +2,2 | nivel de armado (k) |
| SEL | gana − m_arm NO condicionado (1 por puja, 364) escalado a los rellenos | +0,048 (U=+0,036) | (−0,21,+0,31) | +1,0 | dónde/cuándo pujar (R0/R1/régimen) |
| COND | condicionamiento al relleno (deriva m_arm→relleno) | **−0,216** | (−0,43,−0,016) | −4,4 | ejecución: anticipar/cancelar |
| EV_f | | −0,061 | (−0,32,+0,21) | −1,25 (=M_f) | |
| Rebate 20 % | 0,2·0,07·(1−p) | +0,011 si cobra | — | — | volumen ≥89 €/día (B 17-83 €/día: hoy 0) |
Perfil (E02L, 153 rellenos con las 3 marcas): m_det − pc = −0,097 €/€ (el mid YA está ~2c por debajo del precio al detectar el relleno); después D5 −0,002 (IC −0,035,+0,032), D30 +0,038, D120 +0,043, gana − m_det −0,034 (IC −0,31,+0,24). ⇒ casi todo COND ocurre ANTES/EN el relleno (≈ −0,20 entre armar y detectar, con espera mediana ~1,9 s); tras la detección el mid es ≈ insesgado. Es MICROESTRUCTURA (barrido), no información direccional posterior [inferencia; no identificable sin hora de exchange].
- `tras_cancel` (orden ya cancelada al detectar el relleno): 60,6 % del €, EV −0,212 (n=92) vs resto −0,007 (n=61) [punto, sin IC de la diferencia]. Probable marcador de barrido (B repega/cancela cuando el bid cae), no prueba de palanca de latencia → E03.
- Nivel (POST-HOC, confundido con moneda: k=2 solo ETH): 1c bajo bid EV_f −0,111 (127 €), 2c +0,047 (83 €); P(fill) por orden 4,9 % vs 5,4 %.
**Lectura**: la AS correctamente medida (COND, frente al mid al armar) NO es ≈0: vale ≈ −0,22 €/€ (−4,4 pp), el doble del margen de nivel. El «M_f ≈ −1 pp / techo ≈0» del piloto la neteaba con SPREAD. Pero aun eliminando todos los rellenos barridos (proxy tras_cancel), el resto da −0,007 con el 39 % del volumen: **mitigar la AS lleva B a ≈0, no a positivo**; el margen positivo tendría que venir de SPREAD/nivel, SEL o rebate, y ninguno está demostrado.

## 4. Inventario (matriz) — ¿dependía de la formulación errónea?
INVALIDADA_POR_FORMULACIÓN = la conclusión (o su cota/premio) se apoya en la brecha rellena−no rellena, en el «52,8 vs 5,1» o en un contrafactual no capturable. NO_AFECTADA = mide PnL de rellenos/política con desenlace oficial. REQUIERE_REMEDIR = cifra útil pero con un término mal definido.
| línea | métrica/evidencia | clasificación | motivo |
|---|---|---|---|
| «AS −18..−33 pp» (memoria 24-Oct, PLAN_AGENTES «ahorran») | brecha anatomia 21,7 vs 37,6 %; vpv | INVALIDADA_POR_FORMULACIÓN | identidad condicionada (RE-AS-B) |
| detector_ex_ante | AUC 0,513 en rellenos; «premio máximo −18 pp / q_techo 0.3» | AUC NO_AFECTADA; premio INVALIDADA | ΔPnL = −Σpnl banderados es correcto; la cota no |
| q_techo | G-Q1/G-Q2 a pc real: REJECTED | NO_AFECTADA; §0.3/§6 «AS por relleno» INVALIDADA | relleno − bid no condicionado |
| capacidad_diseno §5, f1_huella (escala «−18 pp»), seleccion_adversa_plan («S1 13-16 %», «R1 ~12 % de la brecha 0,24-0,26») | % de la brecha | REQUIERE_REMEDIR | los ΔPnL €/€ valen; el % de brecha no |
| f2_menos_as «ninguna celda 5m barata sin AS» | brecha −20..−27 pp en 6 monedas | INVALIDADA_POR_FORMULACIÓN (esa conclusión); EV de celdas NO_AFECTADA | la brecha aparece en cualquier celda por construcción |
| F8 estructura | REJECTED: retenidas −0,10 €/€, regla trivial = modelo, placebo +1 | veredicto NO_AFECTADA; motivo «52,8 % vs 5,1 %» INVALIDADA | P(fill) por puja 53,6 % ≈ virtual; transferencia REQUIERE_REMEDIR por puja |
| mitigar_as M0 / calibracion_etiqueta (hipótesis 51 vs 5,1) | prerrequisito | REQUIERE_REMEDIR | la calibración debe hacerse por puja y nivel (enmienda 1 ya lo apunta) |
| A1/F5 (100 ms tamaño en ask) | ΔPnL población, RT: EXPLORATORY | NO_AFECTADA | coherente con COND microestructural |
| E1c (0/7), BN_W300 (REJECTED pob.), E1D R1 (PROMISING, B +17,85 € en 183 rellenos) | ΔPnL de rellenos | NO_AFECTADA | forward ≥10 d (~03-Nov) |
| R0/R2 (P-REAL) | taker al ask real, no condicionado: Δ −0,234, 16/17 d | NO_AFECTADA (como tomador) ; su valor para B REQUIERE_REMEDIR | en B, SEL ≈ +0,05 (IC cruza 0): poco espacio por selección; R0 actuaría vía COND |
| skip025 (precio_025) | exceso B −0,52 vs pob. (fill) + dosis-respuesta «AS rellena−no» | REQUIERE_REMEDIR | la parte de brecha no vale; el exceso fill-based sí, 1 periodo |
| b_sin_flujo_minorista / R8 | cuota DES+NUEVO 9,9 vs 26,2 % | NO_AFECTADA | EXPLORATORY |
| cola_posicion, control_misma_edad, cola_vs_cruce, r3 (cola +0,19 vs cruce −0,09) | mecánica de cola | NO_AFECTADA | apoya COND = barrido |
| X-SALIDA | ΔPnL = EV·Δvolumen | NO_AFECTADA | teorema; robusto |
| mapa_escala, tintero, PLAN_MAESTRO (estrés «brecha B−pob. −0,053») | −0,072 vs −0,019 de periodos distintos | REQUIERE_REMEDIR | mismo periodo B −0,030 ≈ P −0,045 (b_vs_poblacion) |
| r3_escalado (capacidad 136 €/día K5; K20 ×2,3; techo 0/1,5/11 k€) | sim + B | NO_AFECTADA | capacidad medida |
| F7, cosechar v3, fav 60m puja propia, F3 carry, huérfana ex-ante, pares_huecos, salida, tandas, b_regimen, D-FUERTE, W1 tendencia, contrapunto, as_tomador, f6, ganadoras persistentes, rebate_ganadores, post_25_27 | PnL de rellenos o de política / dirección / roster | NO_AFECTADA | cementerio vigente (F3 usa rellenos virtuales: fidelidad, no formulación) |
| PSA (pata_suelta_activa), fav_60m_4h, replica_ganadora, r8_emparejado | sin INFORME | NO_LOCALIZADA (resultado) | no clasificables sin informe |
| RE-AS-B (piloto): «techo AS ≈0, ≲1,5 k€/año» | |M_f|·volumen | REQUIERE_REMEDIR (corregido aquí) | |M_f| no es cota; la AS es −0,22 €/€, pero quitarla deja B ≈0 |
| r1 «EV rellenas −0,0016» | acc doble | invalidada por bug (FA-003) | implementación |

## 5. Hipótesis (HYPOTHESIS_LEDGER H-BR-0..4)
H-BR-0 nula: B = maker de margen ≈0 en un nicho con EV poblacional ≈0 (−0,045..+0,069 según régimen); ninguna palanca lo hace positivo · H-BR-1 COND evitable con latencia de cancelación (E03) · H-BR-2 COND solo evitable con anticipación ≥100 ms (A1/F5/R1) · H-BR-3 nivel más profundo (2c) da EV_f >0 (post-hoc, confundido con ETH) · H-BR-4 rebate a escala (≥89 €/día) suma +0,011.

## 6. Experimentos
- E-RE-BR-01 `PREREG_E01.md` sha256 b648d34d…62e9 (mtime 09:08:14Z; salida 09:08:53Z). Q1: P(fill) puja 0,536 ∈ [0,38-0,68] ⇒ «52,8 vs 5,1» INVALIDADO como motivo. Q2: |COND| 0,216 > |U| 0,036, COND IC90<0 ⇒ palanca de EJECUCIÓN. Q3 OK. Q4: rebate 0 a la escala de B.
- E-RE-BR-02L `PREREG_E02L.md` sha256 942e095d…af17 (mtime 09:11:34Z; salida 09:11:55Z). R1 NO DECISORIA (mid0 mal supuesto, ver §2); R2: share 0,606 ≥0,25 y diferencia 0,205 >0,10 ⇒ cumple en punto, pero no identifica latencia vs anticipación. R3: 195 rellenos = E01.
- E-RE-BR-03 `PREREG_E03.md` sha256 85db9250…32f0: NO EJECUTADO (load5 7,3, 09:13Z).
- Chequeo de identidades: SPREAD+SEL+COND = EV_f por construcción (COND es residuo): no decide nada por sí sola; lo informativo es que SPREAD (IC estrecho) y m_det − pc (medido directamente, independiente del residuo) cuadran con COND ≈ −0,2.

## 7. Solución experimental
Ninguna: la evidencia no justifica política nueva. Justifica cambiar la pregunta (sec. 9) y E03.

## 8. Refutación intentada
1. COND es residuo → contrastado con medida directa independiente (m_det − pc = −0,097 vs SPREAD +0,107 ⇒ deriva ≈ −0,20): cuadra. 2. Parte de la caída del mid al detectar es MECÁNICA (desaparecen los niveles ≥pc, ~1,2c del 2c): es el contenido económico del barrido, no un artefacto, pero no toda es «información». 3. Días: COND +0,10 / −0,22 / −0,44 / +0,00 (2/4 negativos): depende de 21-22 Oct; sin 2 peores días ≈0 → frágil (G). 4. Unidad: por puja vs por orden cambia P(fill) ×10; EV por € no cambia. 5. tras_cancel puede ser simple retraso de detección del relleno (no latencia) → E03. 6. «resto −0,007»: selección por resultado del propio mecanismo de B (las órdenes no canceladas son las que el precio no barrió); no es una política ejecutable. 7. Validación independiente: PENDIENTE.

## 9. Veredicto y economía (camino B→200 k€)
Validada: 0 €. Exploratoria: B hoy −0,061..−0,072 €/€ × ~65 €/día ≈ −1,5 k€/año. Contrafactual/capacidad, palanca a palanca, SIN sumar solapadas (las de cancelación se toman como máximo, no suma):
| # | palanca | evidencia | €/€ | volumen €/día | k€/año (contraf.) | hueco |
|---|---|---|---|---|---|---|
| 0 | B tal cual | E01/posiciones, 4 d | −0,06 | 65 | −1,5 | 201,5 |
| 1 | COND: anticipar/cancelar (R1 E1D o A1/F5, máx., no suma) | R1 +0,14 en B (descr.), A1 +0,028 pob.; techo: quitar barridos ⇒ resto −0,007 | → 0..+0,08 | 40-65 | 0..+1,9 | ~198 |
| 2 | escala K 5→20, 3 alts, 24 h | r3: 136 €/día K5, ×2,3 K20, EV −0,017 | +0,06 | ~310 | ≈+7 | ~193 |
| 3 | rebate (solo con ≥89 €/día) | rebate_ganadores | +0,011 | 310 | +1,2 | ~192 |
| 4 | nivel 2c (H-BR-3) | post-hoc confundido | ? | — | no cuantificable | — |
| 5 | nichos no explotados (15m ETH favoritos, otra mecánica) | mapa_escala, únicos BH q=0,024 | +0,025 | 1-5 % de ~30 k €/día | 6-29 | ~163-186 |
| — | 0,30-0,50, BTC, BNB/DOGE | R3 −0,19; BTC REJECTED; <1 k | — | — | 0 | — |
Techo medido honesto de B (palancas 1-3): **≈0-11 k€/año** (r3_escalado optimista ~11 k), con 5: ≲40 k€. Capital NO es el límite (posiciones resuelven en ≤5 min; para P(DD)≤10 % a K=25 y 1.000 rellenos bastan 430-680 $); con EV≤0 el Kelly es 0 y la reinversión no escala nada. **Para 200 k€ desde B tendría que ser verdad**: EV_f ≥ +0,10 €/€ sobre ≥5,5 k€/día de rellenos (16 % del flujo maker del nicho 33,9 k€/día, ~40× la capacidad R3 a K20) o +0,05 sobre 11 k€/día (32 %); es decir, eliminar ~90 % de COND SIN perder volumen ni SPREAD y ganar cuota de cola frente a ~119 makers/día. No hay evidencia de ninguna de las tres.

## 10. Siguiente paso exacto y qué reabriría
1) E03 (tras 09:30Z con load5<4): hora de exchange de los rellenos tras_cancel vs intención de cancelar ⇒ decide latencia vs anticipación. 2) Remedición priorizada (sec. 11). 3) No citar más «AS −18 pp» ni «52,8 vs 5,1»: citar COND (−0,22 €/€) y P(fill) por puja (0,54). Reabre H-BR-0: una política con EV_f ≥ +0,05 ponderado por €, ≥10 días forward, IC90 días >0, sin 2 mejores días, o un nivel/selección que dé SPREAD+SEL > |COND| en A/B aleatorizado.

## 11. Re-medir / reabrir (solo con mecanismo o predicción nueva)
| prio | línea | por qué ahora | experimento mínimo | coste | prereg |
|---|---|---|---|---|---|
| 1 | E03 latencia vs anticipación | COND microestructural; tras_cancel 61 % del € | PREREG_E03 | bajo (zcat|grep, <2 min CPU) | 85db9250… |
| 2 | F8/mitigar_as transferencia por PUJA | el motivo de no-transferencia era de unidades | P(fill) y EV_f por puja virtual (vida = cadena) vs B 0,536 | medio | a escribir por calibracion_etiqueta (ya en enmienda) |
| 3 | nivel 1c vs 2c (H-BR-3) | SPREAD es el único componente positivo con IC estrecho | población on-chain × libro5_bajos: EV_f por distancia al top en el relleno, estratificado moneda×día | medio | pendiente |
| 4 | R1/A1 forward | ya preregistrados | leer forward ~03/04-Nov | 0 | existentes |
| 5 | estrés «−0,053» en mapa_escala/tintero | periodos distintos | recalcular escenarios con B≈P mismo periodo | bajo | — |

## 12. CORRECCIONES por validación independiente (casos/VALIDACION_INDEPENDIENTE_26OCT.md) — mandan sobre las secciones anteriores; no citar las cifras previas
1. Verdad de B = on-chain por order_hash: 202 rellenos, 221,30 €, EV −0,0724, IC90 por cierre −0,31..+0,20 (por día +0,070/+0,166/−0,267/−0,584). Mi E01 (195 rellenos, −0,061) usaba etiquetado_pasivo_B, al que le faltan 7 rellenos (−2,97 €): sesgo de +0,011.
2. On-chain: SPREAD +0,106, SEL +0,048 (cruza 0), COND −0,227 (−0,44..−0,01). COND es un RESIDUO acoplado mecánicamente a SPREAD: para rellenarse a pc, el mid tiene que caer. NO es una palanca independiente. Su significación depende del 22-Oct: sin ese día, EV +0,045 y COND −0,079 (n=125). Medida directa m_det − pc = −0,092 (n=193).
3. «Sin barridos −0,007» es SELECCIÓN: exige mid_120s y excluye 50 rellenos con EV +0,104. Con los 202: tras_cancel −0,116 frente a resto +0,005; diferencia IC90 −0,38..+0,60, y el marcador es inestable. Retiro la frase «mitigar la AS lleva B a ≈0».
4. P(fill): 5,32 % por orden y 55,5 % por puja. Que la puja de B se parezca al 52,8 % virtual NO es calibración: es coincidencia entre unidades distintas. FA-004 queda como cruce de unidades, no como prueba de transferencia.
5. El margen frente al precio, ponderado por €, NO es pequeño: virtual opt −0,100 (nicho de B −0,134); B real −0,072 €/€ = −1,49 pp por acción.
6. Techo: «≲40 k€» y «0-11 k€» NO son defendibles. El 15m ETH es otra mecánica (FAV-15M-ETH, misión 15m v5). «40×» es ~18× frente a K20. Las palancas 1 y 2 solapan. La 2 suponía EV +0,06 frente al R3 medido −0,041. **Valor central de B ≈ −1,5 k€/año.** Lo único sostenible: 200 k = 0,10 × 5.479 €/día × 365 = 0,05 × 11 k€/día × 365.
7. Nivel 1c −0,130 (SOL/XRP) frente a 2c +0,043 (todo ETH): confundido con la moneda; no identificable.
