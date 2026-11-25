# PREREG R1v2 — ADENDA 03 (19-Nov ~10:57Z, execution-engineer por encargo de chief; dictamen del statistical-validator y OK de Javi). Antes de ver ningún dato de V5.
Base NO editada: PREREG_R1v2_19nov.md (48fe638e…), ADENDA_01 (efd19654…), ADENDA_02 (73f90080…), CONTRATO_R1v2_19nov_v2.md (6bda3605…). Todo lo no mencionado aquí no cambia.

## B. Latencia de cancelación de V5 = L_cancel REAL vigente (anula los «+150 ms»)
1. V5 (= CXJ150 aplicada sobre la política REAL de B, ADENDA_02 §1) usa como latencia de cancelación **L_cancel de paquete_l 13-Nov** (`/root/polymarket-research-datalogs/paquete_l/ensayo_real_B2, _B3, _B5`; regla de Javi 16-Nov «solo datos reales vigentes»): **PRIMARIA = p90 74 ms**; sensibilidades **111 ms y 147 ms** (PREREG §1: «sensibilidad 74/111/147»; ADENDA_01: p50 33 / p90 74 / estrés 111), declaradas por clase de suelo lo/hi.
2. Condición de efectividad, sin cambio de forma: la cancelación llega a tiempo solo si `rx + t_proc + L_cancel ≤ casado − 20 ms` (rx = recepción del tick de Binance que dispara el salto; PREREG §1, ADENDA_01 A1). El relleno con t ≥ salto + L_cancel (no +150) se da por cancelado SOLO si cumple esa condición.
3. SE ANULAN: el «+150 ms» de CXJ150 (PREREG_Q11_THRU1_FWD.md línea 14, sha 68ca25a0…; aproximación anterior al paquete_l vigente) y la frase de ADENDA_02 §1 «la +150 ms de CXJ150 se mantiene como primaria; 74/111 ms como sensibilidad». Los 150 ms no se usan ni como sensibilidad (147 ya cubre esa zona con dato real).
4. Si p90 |t_sim − t_real| > L_cancel → INSUFFICIENT (contrato v2), sin cambio.

## C. «No armar» = cada colocación Y cada repegado de DEEP_PEG
1. En la política real de B (DEEP_PEG top−k con repegado; REGISTRO_HIPOTESIS H35), **cada alta y cada repegado cuenta como «armar»**: si hubo salto adverso ≥3 bps en 1 s en (t−3300, t−300] ms respecto al instante t de la alta/repegado, NO se coloca / NO se repega (la orden en reposo previa sigue su vida con la regla (ii) de cancelación).
2. Salto = `bnr(coin, t, 1000)` de **passT_v4 vigente** (`/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/passT_v4.py`, líneas 75-83, **sha256 85256bcc7872afdfdc7d18f9bf4cd3e27e46c0d4176aceb263d6821045bbf535**): hora = RECEPCIÓN del tick de Binance, retorno en bps entre t−w y t con el último tick ≤ t (rancio >15 s ⇒ NaN), umbral |r| ≥ 3 bps (`JUMP`, línea 83); adverso = contra el lado de la puja (Binance baja y la orden es Up, o sube y es Down). Si el texto y passT_v4 difieren, manda passT_v4 (regla del antecedente PREREG_Q11_THRU1_FWD línea 14). Sin dato Binance rx ≤ t no hay salto (NaN, igual que passT_v4): se publica el % de altas/repegados sin dato.
3. Se reporta SIEMPRE la fracción de altas/repegados bloqueados y la de vidas con ≥1 disparo, y P(fill) con/sin regla (ADENDA_01 A1, trampa de «cancelar para siempre»).
4. Antecedentes cruzados (no se inventan umbrales): CXJ150 de PREREG_Q11_THRU1_FWD.md (68ca25a0…, línea 14); DB1/DB1_150 (PREREG_DB1.md) y H-DB3, CXB_l como familia emparentada, ya citadas en ADENDA_02.

## D. Días excluidos del HOLD de R1v2
Los días **26-Oct … 04-Nov** (dPnL +128 sobre G0, donde CXJ150 se eligió post hoc entre 12 variantes, ADENDA_02 §2) quedan EXCLUIDOS del HOLD de R1v2 y de cualquier bloque de evidencia confirmatoria de V5 o de la familia (HOLD, SELECCIÓN, Puerta 0, E-SO-3, max-statistic); solo pueden aparecer en descripciones etiquetadas «POST HOC / días quemados». Esto endurece (no sustituye) PREREG §6, donde ya solo ≥18-Nov confirma; V5 es una regla fija, no se entrena, así que el solape con TRAIN 26-28 Oct no la afecta.

## E. Familia y resto
Familia = 5 variantes (ADENDA_01), V5 := CXJ150 con B y C de esta adenda. Rebate 0 primario, cortafuegos CXB R-CXB-1..6, particiones, ceguera, Puerta 0 y E-SO-3 sin cambio. Cualquier cambio posterior = versión nueva y cuenta.
