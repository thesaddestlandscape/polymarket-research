# PREREG VER_TODOS v2 — 18-Nov-2026 ~09:45Z (reverse-engineer). Escrito ANTES de ejecutar cualquier variante nueva.
Vinculante: CONTRATO_VALIDACION_18nov.md (sha f85b1bb4f17f65bb…, RED). Este prereg aplica sus puntos 7 y C1-C8. Solo lectura, 0 órdenes.

## Universo y motor (sin cambios)
3.796 órdenes reales de B, 20/21/22/23-Oct (únicos días con órdenes reales; no hay OOS independiente). 202 rellenos reales (198 token-lados).
Motor engine_v4 + stamp_v3 'v3d' (passT_v4), ARR = t_call0 + EXA, CANC = t_cancel_int + EXC; sin cancelación: (cie−60)·1000 + EXC.
Copia generada: v9_verif_v2.py (de v4_verif_dem.py) + dem_hook_v2.py. La base v3d_BASE debe reproducir 88/84/4/118 con EXA=35/EXC=33; si no, PARA.
Entradas permitidas de ordenes_b.csv: oid, tok, lado, precio, size, cola, t_dec, t_call0, t_cancel_int, cie (+ fill/acc_llena/gana_lado SOLO como etiqueta, nunca como entrada del motor).
Excepción declarada (replay de órdenes reales, contrato C3): COLA_viva y L2Q restan de la fila del libro el tamaño VIVO de NUESTRA orden real (size − rellenos propios con sello < t). Es contabilidad del libro observado, no información para decidir; se marca y se audita (test: 0 rescates con dt=0 y relleno propio en el tx).
Prohibido: TRAIN 26-Oct..09-Nov para ajustar, HOLD 10-14-Nov, cualquier dato ≥15-Nov; DEMall/DEMr_COLA no son evidencia; variantes nuevas sin adenda con sha previa.

## Variantes (todas por orden, mismo motor/sello)
- BASE = v3d_BASE (referencia de reproducción).  COLA = la de la adenda 1 (resta constante; solo referencia del defecto 2c).
- **COLA_viva** (C3) = COLA pero restando el tamaño vivo. **Referencia de TODOS los incrementos.**
- DEMe_COLAv (C2) = COLA_viva + print sintético con residual S_T − f_aj (tamaño de ORDEN), solo tx con ≥1 maker ajeno y SIN filas nuestras (f_own = 0).
- **DEMt_COLAv** (C1+C2, primaria DEM) = COLA_viva + residual = S_T·(takerFillAmount/makerAmount) − f_aj − f_own, solo tx sin filas nuestras, residual > 1e-3.
- Placebos de DEMt_COLAv (C4): _p30 / _m30 (eventos ±30 s) y _rnd (20 semillas fijas 0..19: por semilla y token, todos los eventos elegibles desplazados un offset U([−30,−5]∪[5,30]) s). Todos CON COLA_viva.
- **L2Q_COLAv** (paso 2a, primaria cola): cola delante = tamaño del nivel L en el L2 por nivel (cola_vs_cruce/mk, recepción ms, 20-22 Oct) en t_arr; cada cambio del nivel L en (t_arr, t_end] es una fila de cola con v = nivel − tamaño vivo propio (desde la aparición de nuestra alta en el L2: primer aumento ≈ size ±0,02 en [t_arr−60, t_arr+300] ms; si no se encuentra, t_arr, contado). Reloj: t_ex = rx − 38 ms (suelo hi). Semántica del motor (pesimista: las cancelaciones salen de detrás primero: ahead = min(ahead, v)). Órdenes sin L2 → igual que COLA_viva (contado).
- L2Q20 (sensibilidad de reloj, rx − 20 ms); L2Q_opt (cota optimista: las bajadas no casadas con prints restan de delante; puede contar doble: solo cota, no evidencia); placebos L2Q_p30 / L2Q_m30 (serie del nivel desplazada ±30 s).
- Combinación DEMt+L2Q: solo se calcula si AMBAS pasan por separado (no se espera).

## Sensibilidades (no confirmatorias; se reportan siempre)
- C5 ventana endógena: te_cap = min(te, t_arr + CAP), CAP = p50 (605 ms) y p90 (2.675 ms) de la vida de las órdenes NO rellenadas (medido en los pkl V5_DEM antes de este prereg); aplicado a BASE y COLA_viva de todas las órdenes.
- C6 latencia: corridas completas con (EXA,EXC) = (147,33), (35,74), (35,111), (147,111). Clase de suelo declarada: días 20-23 Oct 94 % hi / 6 % amb / 0 lo (ledger, contrato p.3); la latencia 35/33 es del pool lo → la (147,111) es la referencia pesimista hi. Sin medición hi: todo «no validado».
- C7: métricas sobre el subconjunto de órdenes sin eventos de cinta 'sinev'/'amb' en [t_arr, t_end] y con relleno real fuera de esas ramas.

## Métricas (por orden; también por día y leave-one-day-out)
TP = sim ∧ real ∧ q_sim ≥ 0,5·q_real (estricto; los sim∧real con q_sim < 0,5 q_real se cuentan aparte como TP_parcial); FP = sim ∧ ¬real; FN = real ∧ ¬TP.
Incremento sobre COLA_viva: ΔTP, ΔFP, neto = ΔTP − ΔFP (y lo mismo para cada placebo; rnd: máximo y p95 sobre 20 semillas).
recall q-ponderado = Σ min(q_sim, q_real) / Σ q_real. % TP con |tf − real_tm3| ≤ 50 ms. Rescates con dt = 0 y f_own > 0 (debe ser 0).
EV ponderado por € (Σpnl/Σcoste) y por unidad (media de pnl/coste), 1.er relleno por token-lado, desenlace oficial (gana): TP motor vs real, FP, FN, por día y sin el mejor día. Sin IC por días (n = 4 días ⇒ INSUFFICIENT para EV).
C8: «invisible» ⇒ «no identificable ex ante». EV real por clase de FN (98/11/8/1 base; recalculado sobre FN de COLA_viva) para reconciliar el −0,235 (hipótesis previa: es el FN de DEMr_COLA, variante circular).

## Criterio (confirmatorio, por variante primaria DEMt_COLAv y L2Q_COLAv, cada una contra COLA_viva)
ACEPTA si TODO: ΔTP ≥ 5; ΔFP ≤ ΔTP/3; neto > 0; máx. placebo (±30 s y rnd-máx) en ΔTP y en neto ≤ 1/3 del real; 0 rescates con dt = 0 y f_own > 0;
signo de neto > 0 en ≥ 3 de 4 días (L2Q: ≥ 2 de 3 días con L2) y neto > 0 en cada leave-one-day-out.
REFUTA si ΔTP ≤ máx. placebo ΔTP o neto ≤ 0. Resto: INCONCLUSO. Si el residual correcto de DEMt es ~0 (esperado): REFUTADO («sin información pública ex ante en la cinta»).
Incluso ACEPTA = mecanismo de visibilidad, no EV: el EV de B sigue sin validar (4 días, latencia lo en días hi).

## Paso 2b — modelo de llegada de tomadores (hazard), prerregistrado
Unidad: intervalos de 250 ms de cada orden desde t_arr hasta min(t_end, 1.er relleno real). y = 1 si el 1.er relleno real (sello v3) cae en el intervalo.
Rasgos SOLO con datos ≤ t (inicio del intervalo): libro sa_ms en t − 40 ms (distancia bid−L en ticks, spread, log1p tamaño top), log1p(cola de B en t_dec), T a cierre, lado (YES/NO), moneda;
Binance bookTicker (recepción, último valor ≤ t, forward-fill; sin dato en el día ⇒ orden excluida, no NaN-como-rasgo): retorno 1 s, 5 s, 30 s FIRMADO a favor de nuestro token y |ret 5 s|. Régimen lo/hi: constante en estos días (94 % hi) ⇒ no se usa.
Modelo: regresión logística L2 (C=1, estandarizada), leave-one-day-out (entrena 3 días, predice el 4.º). Sin ajuste de hiperparámetros.
Reporta: Brier vs Brier de la tasa base del día de entrenamiento; fiabilidad por decil; AUC por intervalos; separación perdedores/ganadores = AUC de la hazard predicha en el intervalo del relleno entre rellenos perdedores (gana=0) y ganadores;
EV real de rellenos por tercil de hazard. ÚTIL si Brier skill > 0 en ≥ 3 de 4 días Y AUC ≥ 0,60; separa AS si AUC perdedor/ganador ≥ 0,60 con signo estable en ≥ 3 días. Si no: no se usa para imputar en fase 2.
Uso F5: F5 cancela fuera de lo; en estos días ~94 % hi ⇒ se reporta la fracción de FN no identificables en ventanas hi como cota; la medida exacta requiere el estado del detector por orden (fuera de alcance aquí).
