# Pendientes — por orden

- [x] Kelly compuesto (en curso)
- [x] Resolution Sniper — p_modelo≥0.92 con mercado en 0.80, última 1-2h antes de vencimiento
- [x] OU Process 5min — shadow strategy paralela UPDOWN_OU_5M, θ=30, calibrar con n≥200
- [x] Ventanas horarias con más edge — ORDER_FLOW blacklist 22 UTC (IC=-0.115 n=37)
- [ ] Dataset Jon-Becker — descarga selectiva + procesamiento en streaming
- [ ] MAE/MFE tracking: cruzar historial precios con posiciones abiertas → si precio_yes ≥ prob_modelo×0.9 antes de expirar → señal de salida anticipada (especialmente para WEEKLY_PRICE y PRICE_TARGET)
- [ ] Random Forest sobre features (pct, sigma, drift, delta_ratio) → requiere Jon-Becker n≥5000
- [ ] Feature velocidad_precio_yes: pct_change del precio YES en últimos 5min de historial → añadir a features de UPDOWN_GBM para detectar herd behavior (mispricings cuando crowd pierde independencia)
- [ ] Grid search de parámetros (THETA_OU, REGIME_THRESHOLD, DELTA_MAX...) sobre Jon-Becker — cuando tengamos los datos. Inspirado en AlphaEvolve (arxiv 2506.13131) pero con scipy.optimize, no LLMs.
