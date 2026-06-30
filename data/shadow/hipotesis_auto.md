# Hipótesis automáticas — 2026-06-30 02:10 UTC
_Generado por shadow_postmortem.py sobre 1349 resoluciones (PNL=-47.54€)_

## Patrones causales activos

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1022` → IC=+0.125 (n=22)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.62€ cuando `pct_spot_vs_ref` |x|≤ 0.1022 (IC base=+0.037)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.3147` → IC=-0.147 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.3147
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

_Sin sugerencias automáticas con datos actuales. Ampliar n por estrategia._

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ ORDER_FLOW_5M | 785 | +0.012 | +7.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#5min | 649 | +0.002 | -5.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 63 | +0.038 | +1.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 63 | +0.038 | +1.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC | 129 | +0.011 | +0.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 129 | +0.011 | +0.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 82 | -0.012 | -1.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 82 | -0.012 | -1.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 112 | -0.026 | -4.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 112 | -0.026 | -4.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 147 | +0.017 | +1.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 147 | +0.017 | +1.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 116 | -0.009 | -2.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 116 | -0.009 | -2.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 50 | -0.058 | -10.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 25 | -0.093 | -5.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 24 | -0.115 | -5.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 19 | +0.023 | -2.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 18 | +0.000 | -2.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 6 | -0.037 | -2.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 6 | -0.037 | -2.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 48 | -0.080 | -10.87€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 23 | -0.260 | -10.63€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 9 | -0.061 | -2.46€ | 0 | 0 |
| ✅ UPDOWN_GBM | 377 | -0.007 | -6.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 222 | +0.031 | +3.85€ | 0 | 0 |
| 🚫 UPDOWN_GBM#240min | 12 | -0.171 | -4.82€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 56 | -0.155 | -16.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 74 | +0.053 | +4.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 119 | +0.004 | -5.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 65 | +0.037 | -2.12€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#240min | 5 | -0.089 | -2.96€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BTC#5min | 16 | -0.133 | -6.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 29 | +0.081 | +1.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 148 | +0.027 | +2.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 98 | +0.040 | +1.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 12 | -0.086 | -3.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 29 | +0.081 | +3.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 77 | -0.057 | -0.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 39 | +0.012 | +3.45€ | 1 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 17 | -0.112 | -4.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 16 | -0.044 | +0.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 28 | -0.067 | -1.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 19 | -0.023 | +0.37€ | 0 | 0 |
| 🚫 UPDOWN_GBM#XRP#5min | 9 | -0.061 | -1.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 11 | +0.021 | +8.10€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M | 57 | -0.229 | -13.76€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#5min | 57 | -0.229 | -13.76€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB | 8 | -0.160 | -4.56€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB#5min | 8 | -0.160 | -4.56€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BTC | 9 | -0.102 | -2.57€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BTC#5min | 9 | -0.102 | -2.57€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 7 | -0.058 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 7 | -0.058 | -1.11€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH | 12 | -0.129 | -2.82€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH#5min | 12 | -0.129 | -2.82€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 10 | -0.042 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 10 | -0.042 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 11 | -0.064 | -1.65€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 11 | -0.064 | -1.65€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 57 | +0.009 | -13.43€ | 0 | 0 |
| ✅ WEEKLY_PRICE#BTC | 18 | -0.045 | -6.60€ | 0 | 0 |
| ✅ WEEKLY_PRICE#ETH | 21 | +0.022 | -5.16€ | 0 | 0 |
| ✅ WEEKLY_PRICE#SOL | 18 | +0.045 | -1.67€ | 0 | 0 |
## Hipótesis pendientes — tracking automático


### 🔴 Listas para implementar YA

**🔴 H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Confirma: IC=-0.133 n=16 PNL=-2.48€ → añadir 18 a GBM_BLACKLIST_HOURS
  - _Datos_: n=16 IC=-0.133 PNL=-2.48€


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.033) — sin ventaja clara. oversold(IBS<0.3): IC=-0.033 n=28 | neutral: IC=+0.000 n=24 | overbought(IBS>0.7): IC=-0.028 n=34
  - _Datos_: n=88 IC=-0.022 PNL=-7.70€


### ⏳ Acumulando datos

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 88 ops, 15 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=17, boost estimado=+0.014. Necesita 3 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 73 ops con delta_ratio | SOL: 86 ops con delta_ratio

**⏳ H-KELLY-HORA** — Kelly boost ×1.2 en horas top (15/17/19h UTC)
  - _Umbral_: n≥40 por hora con IC estable ≥+0.10 confirmado en forward
  - _Acción_: Añadir HORA_BOOST = {13: 1.2, 15: 1.2, 17: 1.2, 19: 1.2} en shadow_predict.py
  - _Estado_: H=13h UTC: IC=-0.051 n=87/40 PNL=+0.29€ | H=15h UTC: IC=-0.011 n=92/40 PNL=-5.07€ | H=17h UTC: IC=+0.271 n=33/40 PNL=+13.52€ | H=19h UTC: IC=+0.048 n=40/40 PNL=+2.97€

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=29/40 IC=+0.081 PNL=+3.23€ | BTC#60min: n=29/40 IC=+0.081 PNL=+1.25€ | SOL#60min: n=16/40 IC=-0.044 PNL=+0.30€

**⏳ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n=39/40 IC=+0.012 PNL=+3.45€ (ETA: 1 ops)
  - _Datos_: n=39 IC=+0.012 PNL=+3.45€

**⏳ H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=21/15 IC=+0.022 PNL=-5.16€ | BTC: n=18/15 IC=-0.045 PNL=-6.60€ | SOL: n=18/15 IC=+0.045 PNL=-1.67€

**⏳ H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: Máximo n actual en GBM: 377/200. Esperar 3+ subtypes con n≥200.
  - _Bloqueante_: N_INSUFICIENTE


### 🔒 Bloqueadas (requieren dataset/API)

**🔒 H-OBI** — Orderbook Imbalance como señal
  - _Umbral_: Dataset Jon-Becker + API CLOB con orderbook histórico
  - _Acción_: Implementar s_obi en shadow_predict.py usando L2 orderbook
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Analizar spread bid/ask e imbalance por mercado en 60min previos a resolución.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-OU-THETA** — Calibrar theta OU con datos históricos
  - _Umbral_: Dataset Jon-Becker con series de precios históricos suficientes
  - _Acción_: Ajustar THETA_OU por par en strategy_params.json (BTC/ETH/SOL independientes)
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Fit OU sobre series históricas por par y estimar theta por MLE.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-HMM-REGIME** — HMM para régimen de mercado
  - _Umbral_: n≥200 ops GBM forward con hora_utc/ibs_15, o dataset Jon-Becker
  - _Acción_: Implementar hmmlearn sobre features GBM; condicionar estrategia al régimen detectado
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Entrenar HMM 3-estado sobre (drift_60min, sigma_h) histórico. Validar en forward.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-CROSS-ARB** — Arbitraje Polymarket vs Kalshi
  - _Umbral_: API Kalshi activa + credenciales Polymarket live
  - _Acción_: Extender arb_scanner.py con endpoints Kalshi; comparar mismo evento cross-plataforma
  - _Estado_: Requiere acceso API Kalshi + credenciales Polymarket live
  - _Bloqueante_: API_KALSHI


### 🧪 Hipótesis custom (editables en hipotesis_custom.json)

**⏳ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: 15
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.067 PNL=+2.98€)
  - _Datos_: n=4 IC=+0.067 PNL=+2.98€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=38 IC=+0.000 PNL=-0.21€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=38 IC=+0.000 PNL=-0.21€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=278 IC=+0.007 PNL=-0.94€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=278 IC=+0.007 PNL=-0.94€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 5/15 ops en el filtro definido (IC actual=+0.054 PNL=+1.49€)
  - _Datos_: n=5 IC=+0.054 PNL=+1.49€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 12/20 ops en el filtro definido (IC actual=+0.043 PNL=+0.95€)
  - _Datos_: n=12 IC=+0.043 PNL=+0.95€

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=59 IC=+0.041 PNL=+3.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=59 IC=+0.041 PNL=+3.82€

**⏳ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: 30
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: 15/30 ops en el filtro definido (IC actual=+0.066 PNL=+0.96€)
  - _Datos_: n=15 IC=+0.066 PNL=+0.96€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.157 < -0.08 con n=17 PNL=-4.08€
  - _Datos_: n=17 IC=-0.157 PNL=-4.08€

**〰️ H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40.
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Si IC<0 con n≥30 → revisar umbral drift_60min (0.5% puede ser demasiado estrecho)
  - _Estado_: n=167 IC=-0.003 PNL=-12.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=167 IC=-0.003 PNL=-12.71€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0008/h) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? sigma_h<0.0008 equivale a volatilidad diaria <0.8%.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0008
  - _Estado_: 2/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.01€)
  - _Datos_: n=2 IC=+0.000 PNL=+0.01€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo.
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: Si IC<0.02 con n≥50 → desactivar BTC#15min (el edge ha muerto); si sube a >0.08 → candidato live
  - _Estado_: n=65 IC=+0.037 PNL=-2.12€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=65 IC=+0.037 PNL=-2.12€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 31/50 ops en el filtro definido (IC actual=-0.015 PNL=-0.41€)
  - _Datos_: n=31 IC=-0.015 PNL=-0.41€

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=86 IC=+0.080 PNL=+0.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=86 IC=+0.080 PNL=+0.80€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 8/30 ops en el filtro definido (IC actual=-0.040 PNL=+0.39€)
  - _Datos_: n=8 IC=-0.040 PNL=+0.39€

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 19/20 ops en el filtro definido (IC actual=+0.158 PNL=+5.18€)
  - _Datos_: n=19 IC=+0.158 PNL=+5.18€

**⏳ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: 25
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: 15/25 ops en el filtro definido (IC actual=-0.110 PNL=-8.44€)
  - _Datos_: n=15 IC=-0.110 PNL=-8.44€

**🔴 H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.158 < -0.08 con n=19 PNL=-8.08€
  - _Datos_: n=19 IC=-0.158 PNL=-8.08€

**⏳ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: 40
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
