# CONTRATO R1v2 + GATILLO F5_t (bajo/medio) — measurement_id R1V2-F5-B-19NOV-v2
Autor: polymarket-data-integrity-authority, 19-Nov-2026 ~09:00Z. Sustituye a v1 (CONTRATO_R1v2_19nov.md, que queda como historial). Solo lectura: 0 EV medido.
Etiqueta obligatoria de todo resultado: «RELLENOS VISIBLES + ESTRES SOLO/NONE», no es EV de B real. Decisiones de Javi vigentes: prueba REAL obligatoria antes de recargar dinero en B; hi BLOQUEADO (no validado); cortafuegos CXB (R-CXB-1..6 de v1 sec.2 siguen en vigor, sin cambios).
ESTADO GLOBAL: AMBER (diseno certificable; ningun EV autorizado hasta cumplir sec.9).

## 1. Fidelidad (C1)
Declarado: la fidelidad del replay de B FALLA hoy (sensibilidad 0,416 frente a >=0,75 exigido; EV sim −56 % vs real). Poblacion simulada = «rellenos visibles» (88/202 con print/nivel). Sin ancla de relleno real en noviembre. Medir error de tiempo de relleno de los TP (p50/p90 |t_sim − t_real|) y comparar con L_cancel (paquete_l B2/B3/B5, 13-Nov): si p90 > L_cancel, la efectividad de cancelar a tiempo no es evaluable y se reporta INSUFFICIENT. La condicion (a) de v1 sec.3 pasa a «informativa»: ningun resultado es confirmatorio mientras sens<0,75.
## 2. Puerta 0 (C2, C3)
Poblacion: ORDENES B SIMULADAS 03-09 Nov con hora de colocacion y de cada repegado conocidas (no rellenos publicos). F5_t = log1p(tamano del ask de nuestro token, ultimo estado con rx<=t, <=30 s; invalido = no operar). Cortes C0=3,526360511779785, C1=4,717426776885986 congelados.
Se reporta EV incondicional (no relleno=0), P(relleno), EV|relleno, ponderado por € (Σpnl/Σcoste).
CRITERIO: EV_€(bajo∪medio) − EV_€(alto) > 0 con IC90 por DIAS (bootstrap por dia/cierre) Y EV_€(alto) <= 0. El orden bajo>medio solo descriptivo. Cambio de tercil F5_t vs F5 <=35 %. Fallo => F5_t AMBER-exploratorio.
## 3. Inversion y placebo (C4, C11)
Inversion = cancelar los de MAYOR mu con el MISMO numero de cancelaciones por orden. Placebo = permutar puntuaciones entre puntos (orden,t) dentro de dia×moneda×suelo×nivel×tramo T, misma tasa de cancelacion por orden, K=1000, semilla 20261119. Sin ventanas ±30 s.
## 4. Suelo (C5)
Rasgo de suelo SOLO con filas rx<=t (5 min previos). Clase de ventana completa (lo<=28 ms / hi>=33 ms / indet) solo como ESTRATO, nunca como rasgo. Dia valido: n_lo/(n_lo+n_hi+n_indet)>=0,5 con >=N=24 ventanas clasificadas por dia×moneda (N fijado ahora). Primario = lo; hi «no validado». Fecha de juicio = cuando haya >=10 dias lo validos.
## 5. Unidad y estimador (C6, C7)
Unidad = punto (orden,t) en rejilla fija 250 ms desde colocacion hasta T_STOP + cada repegado; peso 1 por orden (cada orden suma 1, no por numero de puntos). Bootstrap por dia/cierre. EV y ΔPnL incondicionales por €. Censura: IPW con hazard v11 (v11_hazard.json), truncado de pesos declarado (p99) y sensibilidad sin IPW. v1/DISENO se corrigen para coincidir: el diseno que habla de «1.er relleno por token-lado» queda para el reporte de EV por unidad, no para el entrenamiento.
Efectividad (tambien F5 en vida): una cancelacion cuenta como a tiempo solo si rx + t_proc + L_cancel <= casado − 20 ms. PRIMARIA = F5_t solo al colocar; cancelar en vida = variante exploratoria.
## 6. Antiguedad y validez de F5_t (C8)
Antiguedad = la del stream del token (sin hueco de seq), no la de cualquier mensaje. Reportar % invalido por tercil y moneda; EV de B-sin-filtro en las invalidas (para ver si el invalido censura). Equivalencia de q: maker_ms ↔ libro5_ms demostrada (mismo nivel/tamano en 100 muestras) antes de usar ambos.
## 7. Particiones y ceguera (C9)
10-17 Nov NO ciegos (F5 y rasgos conocidos). SOLO >=18-Nov confirma. Hash de rasgos y codigo ANTES de abrir >=18-Nov. libro5 parado (hoy PAUSA desde 03:18Z-19) = DATA_BLOCKED para esos dias. Resto de lista de dias de v1 sec.5 sin cambios.
## 8. Exito y multiplicidad (C10)
Familia = 4 (primaria + 3 secundarias de v1). EXITO = criterios 1-9 del diseno Y p_max<0,05 por max-statistic sobre las 4. tau: se ELIMINA (R1v2 es regla de valor esperado mu_ucb<−c; no hay tau). H-F5 = test aparte con su propio alfa. PROHIBIDO promocionar exploratorias tras ver el HOLD.
## 9. Datos auxiliares (C12, C13)
20-23 Oct: restar del L2 el tamano vivo de nuestras ordenes (ordenes_b.csv) y quitar prints con f_own>0. Chainlink/TWAP por rx, filtrando source (pyth/chainlink/fallback). mu_ucb = ucb90 bootstrap por dias del TRAIN. Sensibilidad con rebate=0 (el rebate real es 0,2 del fee). Confirmar grabador 26-28 Oct (cobertura por fichero). Medir falsos emparejamientos on-chain↔L2 (union hoy 49 %).
## 10. Reverse-engineer (RE-B-SOLO-OBSERVABLE)
(a) Censo de rellenos simulados por canal (print en nivel / TT / bloqueo) con cordura en octubre (≈0 eventos de bloqueo con la orden real viva salvo dt≈0). (b) Estres NONE OBLIGATORIO y UNIFORME en los 3 terciles: tasa 1,7-1,9 % de ordenes, EV −0,115, pesimista −0,176; no contar dos veces los TT (14, ya visibles). (c) % de ordenes y P(relleno) por tercil F5_t. (d) Reportar CON y SIN 23-Oct (11/11 perdedoras sin L2). (e) PROHIBIDO afirmar «SOLO = la AS» (J, no demostrado) y «F5_t evita la NONE» (E-SO-2 inconcluso, 87-89 % de NONE en bajo+medio). (f) Verificar unidades tk_sz/tk_rem (acciones vs USDC) antes de cualquier cifra. (g) E-SO-3 es PUERTA de R1v2: R1v2+F5_t congelados (entrenados en dias publicos) aplicados a las 3.796 ordenes de octubre; pasa si (cancelacion a tiempo NONE − TP) >=0,15 con p<0,10 por permutacion dentro de dia y ΔPnL € >0 sobre los 202. Si no pasa: se reporta «visibles + estres NONE uniforme» y R1v2 no se promociona.
## 11. Condiciones antes de medir EV (todas)
1 prereg+hash R1v2/F5_t/parametros; 2 Puerta 0 (sec.2) pasada; 3 error de tiempo de TP medido (sec.1); 4 tabla de suelo por ventana firmada; 5 test de fuga NaN (rasgo NaN-si-no-hay-datos = fuga; AUC≈0,5 por dia); 6 E-SO-3 pasada; 7 recursos (>=12Z, RAM libre >5 GB, cola_pesado) y R-CXB aceptadas.
