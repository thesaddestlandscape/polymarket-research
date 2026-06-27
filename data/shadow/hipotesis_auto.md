# Hipótesis automáticas — 2026-06-27 11:34 UTC
_Generado por shadow_postmortem.py sobre 1185 resoluciones (PNL=-24.91€)_

## Patrones causales activos

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0502` → IC=+0.132 (n=17)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.66€ cuando `pct_spot_vs_ref` |x|≤ 0.0502 (IC base=+0.029)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.132 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0107 (IC base=+0.036)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.2212` → IC=-0.132 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2212
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

_Sin sugerencias automáticas con datos actuales. Ampliar n por estrategia._

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ ORDER_FLOW_5M | 782 | +0.011 | +6.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#5min | 646 | +0.002 | -5.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 63 | +0.038 | +1.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 63 | +0.038 | +1.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC | 128 | +0.008 | -0.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 128 | +0.008 | -0.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 82 | -0.012 | -1.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 82 | -0.012 | -1.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 112 | -0.026 | -4.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 112 | -0.026 | -4.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 145 | +0.017 | +1.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 145 | +0.017 | +1.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 116 | -0.009 | -2.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 116 | -0.009 | -2.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 16 | +0.000 | -1.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 7 | -0.019 | -0.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 7 | -0.019 | -0.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 6 | +0.000 | -1.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 6 | +0.000 | -1.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 16 | +0.000 | -1.53€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 20 | -0.273 | -9.86€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 6 | -0.037 | -1.69€ | 0 | 0 |
| ✅ UPDOWN_GBM | 289 | -0.005 | -2.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 164 | +0.036 | +7.19€ | 0 | 0 |
| 🚫 UPDOWN_GBM#240min | 12 | -0.171 | -4.82€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 56 | -0.155 | -16.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 50 | +0.096 | +5.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 90 | +0.000 | -3.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 49 | +0.029 | -0.44€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#240min | 5 | -0.089 | -2.96€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BTC#5min | 16 | -0.133 | -6.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 18 | +0.135 | +3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 106 | +0.018 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 67 | +0.036 | +1.43€ | 0 | 1 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 12 | -0.086 | -3.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 20 | +0.091 | +1.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 66 | -0.029 | +1.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 34 | +0.028 | +4.02€ | 1 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 17 | -0.112 | -4.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 12 | +0.000 | +1.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 22 | -0.042 | -0.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 13 | +0.022 | +1.37€ | 0 | 0 |
| 🚫 UPDOWN_GBM#XRP#5min | 9 | -0.061 | -1.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 5 | +0.054 | +7.49€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 21 | +0.022 | -3.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE#BTC | 6 | -0.037 | -2.73€ | 0 | 0 |
| ✅ WEEKLY_PRICE#ETH | 8 | +0.000 | -2.41€ | 0 | 0 |
| ✅ WEEKLY_PRICE#SOL | 7 | +0.058 | +1.36€ | 0 | 0 |
## Hipótesis pendientes — tracking automático


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 2 ops más en GBM@18h (IC actual=-0.108)
  - _Datos_: n=13 IC=-0.108 PNL=-1.93€

**⏳ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: 40
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Solo 3 ops con ibs_15 (feature añadida 2026-06-27). Esperar n≥40.
  - _Datos_: n=3 IC=-0.015 PNL=-1.91€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: 20
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: Solo 3 ops GBM con hora_utc en features. Esperar n≥20 para patrones.

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=17, boost estimado=+0.019. Necesita 3 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 72 ops con delta_ratio | SOL: 84 ops con delta_ratio

**⏳ H-KELLY-HORA** — Kelly boost ×1.2 en horas top (15/17/19h UTC)
  - _Umbral_: n≥40 por hora con IC estable ≥+0.10 confirmado en forward
  - _Acción_: Añadir HORA_BOOST = {13: 1.2, 15: 1.2, 17: 1.2, 19: 1.2} en shadow_predict.py
  - _Estado_: H=13h UTC: IC=-0.083 n=82/40 PNL=-4.35€ | H=15h UTC: IC=+0.025 n=57/40 PNL=+3.23€ | H=17h UTC: IC=+0.204 n=25/40 PNL=+7.08€ | H=19h UTC: IC=-0.029 n=32/40 PNL=-0.97€

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=20/40 IC=+0.091 PNL=+1.25€ | BTC#60min: n=18/40 IC=+0.135 PNL=+3.18€ | SOL#60min: n=12/40 IC=+0.000 PNL=+1.27€

**⏳ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n=34/40 IC=+0.028 PNL=+4.02€ (ETA: 6 ops)
  - _Datos_: n=34 IC=+0.028 PNL=+4.02€

**⏳ H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=8/15 IC=+0.000 PNL=-2.41€ | BTC: n=6/15 IC=-0.037 PNL=-2.73€ | SOL: n=7/15 IC=+0.058 PNL=+1.36€

**⏳ H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: Máximo n actual en GBM: 289/200. Esperar 3+ subtypes con n≥200.
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
  - _Estado_: 0/15 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=36 IC=+0.000 PNL=-0.18€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=36 IC=+0.000 PNL=-0.18€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=190 IC=+0.016 PNL=+2.72€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=190 IC=+0.016 PNL=+2.72€

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

**🟡 H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=36 PNL=+6.11€
  - _Datos_: n=36 IC=+0.105 PNL=+6.11€

**⏳ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: 30
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: 14/30 ops en el filtro definido (IC actual=+0.044 PNL=-0.41€)
  - _Datos_: n=14 IC=+0.044 PNL=-0.41€

**⏳ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: 15
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: 13/15 ops en el filtro definido (IC actual=-0.108 PNL=-1.93€)
  - _Datos_: n=13 IC=-0.108 PNL=-1.93€

**〰️ H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40.
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Si IC<0 con n≥30 → revisar umbral drift_60min (0.5% puede ser demasiado estrecho)
  - _Estado_: n=123 IC=+0.004 PNL=-4.33€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=123 IC=+0.004 PNL=-4.33€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0008/h) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? sigma_h<0.0008 equivale a volatilidad diaria <0.8%.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0008
  - _Estado_: 2/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.01€)
  - _Datos_: n=2 IC=+0.000 PNL=+0.01€

**⏳ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo.
  - _Umbral_: 50
  - _Acción_: Si IC<0.02 con n≥50 → desactivar BTC#15min (el edge ha muerto); si sube a >0.08 → candidato live
  - _Estado_: 49/50 ops en el filtro definido (IC actual=+0.029 PNL=-0.44€)
  - _Datos_: n=49 IC=+0.029 PNL=-0.44€
