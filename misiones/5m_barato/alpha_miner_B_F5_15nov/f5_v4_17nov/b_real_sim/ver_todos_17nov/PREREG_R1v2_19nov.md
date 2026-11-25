# PREREG R1v2 + F5_t (bajo/medio) — measurement_id R1V2-F5-B-19NOV-v2 — 19-Nov-2026
Congela ANTES de cualquier lectura de EV. Contrato vinculante: CONTRATO_R1v2_19nov_v2.md sha256 6bda3605c0bf480deb5a928e1734640d18ffe1f9a0f6dccd99ab9f2f668fca81. Diseño: R1v2_DISENO_19nov.md sha256 fed21d8c9d3757b7d18b2428400b9cea8c3ac4cb039a85c1e4847d915007edde (secciones 1-7). Etiqueta de todo resultado: «RELLENOS VISIBLES + ESTRES NONE»; no es EV de B real. Estado: AMBER, 0 EV medido.
## 1. Parámetros congelados
- Gatillo F5_t = log1p(tamaño del ask de nuestro token, último estado con rx<=t, antigüedad<=30 s del stream del token; inválido = no operar). Cortes C0=3,526360511779785 (bajo/medio), C1=4,717426776885986 (medio/alto). Cambio de tercil F5_t vs F5 <=35 %.
- Regla: cancelar si mu_ucb(x_t) < −c, mu_ucb = ucb90 bootstrap por días del TRAIN. Sin tau. Primaria = F5_t solo al colocar; cancelar en vida = exploratoria.
- Unidad: punto (orden,t), rejilla 250 ms desde colocación a T_STOP + cada repegado; peso 1 por orden; IPW hazard v11 (v11_hazard.json), pesos truncados p99, sensibilidad sin IPW. EV/ΔPnL incondicionales, ponderados por € (Σpnl/Σcoste), bootstrap por día/cierre.
- Efectividad: a tiempo si rx + t_proc + L_cancel <= casado − 20 ms. L_cancel solo paquete_l B2/B3/B5 (13-Nov); sensibilidad 74/111/147.
- Estrés NONE uniforme (1,7-1,9 % órdenes; EV −0,115, pesimista −0,176), sin doble conteo TT; con y sin 23-Oct; canal bloqueo con cordura de octubre (diseño sec. 7).
- Rebate: real 0,2 del fee; sensibilidad rebate=0.
## 2. Familia confirmatoria = 4 y criterio
Primaria: E1 logística L2, c=0,02, κ=T_STOP, μ_ucb<−c, F5_t al colocar. Secundarias: c=0; c=0,05; regla μ̂<−c. Fuera de familia: E2/GBM, κ=1000, cancelar en vida, ablaciones. EXITO = criterios 1-9 del diseño sec. 4 Y p_max<0,05 por max-statistic (permutación) sobre las 4. H-F5 = test aparte con su alfa. Prohibido promocionar exploratorias tras ver el HOLD.
## 3. Placebo / inversión
Placebo C11: permutar puntuaciones entre puntos (orden,t) dentro de día×moneda×suelo×nivel×tramo T, misma tasa de cancelación por orden, K=1000, semilla 20261119, sin ±30 s. Inversión: cancelar los de MAYOR μ con el mismo nº de cancelaciones por orden.
## 4. Puerta 0 (C3)
Órdenes B simuladas 03-09 Nov: EV_€(bajo∪medio) − EV_€(alto) > 0 con IC90 por DÍAS Y EV_€(alto) <= 0. Reportar EV incondicional, P(relleno), EV|relleno, % inválido por tercil/moneda. Fallo ⇒ F5_t AMBER-exploratorio.
## 5. E-SO-3 (puerta de R1v2)
R1v2+F5_t congelados (entrenados en días públicos) aplicados a las 3.796 órdenes de octubre. Pasa si (tasa cancelación a tiempo NONE − TP) >= 0,15 con p<0,10 por permutación dentro de día Y ΔPnL € >0 sobre los 202. Si no: se reporta «visibles + estrés NONE uniforme», R1v2 no se promociona. Prohibido afirmar «SOLO = la AS» y «F5_t evita la NONE».
## 6. Particiones y ceguera
TRAIN 26-28 Oct + 03-06 Nov; CALIB 07-Nov; SELECCIÓN (diagnóstico) 08-09 Nov; 20-23 Oct solo consistencia descriptiva. 10-17 Nov NO ciegos (F5/rasgos conocidos; una lectura de EV por versión hasheada, R-CXB-5). SOLO >=18-Nov confirma; hash de rasgos y código ANTES de abrirlo. libro5 parado (19-Nov desde 03:18Z) = DATA_BLOCKED. Suelo: rasgo solo con filas rx<=t (5 min previos); clase lo(<=28 ms)/hi(>=33 ms)/indet solo estrato. Día válido: n_lo/(n_lo+n_hi+n_indet)>=0,5 con N=24 ventanas clasificadas por día×moneda. Primario = lo; hi BLOQUEADO (no validado). Juicio con >=10 días lo válidos.
## 7. Cortafuegos CXB
R-CXB-1..6 de CONTRATO_R1v2_19nov.md sec. 2 en vigor sin cambios: solo lectura; no tocar dryrun/HASHES_CONGELADOS.json, forward_gates.py, engine_v4/stamp_v3, gmap, GEO1; nada de R1v2 en >=10-Nov cambia CXB60; combinación CXB60+F5/B solo tras mirada 1 CXB (>=22-Nov) y con prereg propio; RSS<3.000 MB en cola_pesado.
## 8. Condiciones antes de EV y obligación real
Contrato sec. 11 (prereg+hash, Puerta 0, error de tiempo de TP, tabla de suelo firmada, test de fuga NaN AUC≈0,5 por día, E-SO-3, recursos >=12Z/RAM>5 GB). Prueba REAL obligatoria antes de recargar dinero en B.
## 9. Variantes y registro
Familia 4 + exploratorias listadas arriba; cualquier cambio posterior = versión nueva y cuenta. Clave k15 = floor(s5/900)*900+900; rasgos con rx<=t; Binance rx<=t−1000.
