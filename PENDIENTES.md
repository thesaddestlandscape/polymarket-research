# Pendientes — por orden

- [x] Kelly compuesto (en curso)
- [x] Resolution Sniper — p_modelo≥0.92 con mercado en 0.80, última 1-2h antes de vencimiento
- [x] OU Process 5min — shadow strategy paralela UPDOWN_OU_5M, θ=30, calibrar con n≥200
- [x] Ventanas horarias con más edge — ORDER_FLOW blacklist 22 UTC (IC=-0.115 n=37)
- [ ] [LARGO PLAZO] Grinold-Kahn: ampliar breadth con mercados no-cripto — cuando modelo crypto esté funcionando perfectamente. Tipos candidatos: tiempo meteorológico, política, macro, deportes. Correlación ≈0 con BTC/ETH → BR_efectivo se dobla → IR ×√2 sin cambiar el modelo.
- [ ] Grinold-Kahn: alpha decay monitor automático — si IC_rolling_30 < 0.5×IC_histórico → Telegram alert. Ya tenemos datos, falta el trigger.
- [ ] Grinold-Kahn: stake explícito por IC — #60min (IC=0.105) debería apostar ×1.5 vs #15min (IC=0.070). Actualmente Kelly lo aproxima pero no explícitamente.
- [ ] Dataset Jon-Becker — descarga selectiva + procesamiento en streaming
- [ ] ORDER_FLOW BUY_YES: desactivar cuando CLV_BUY_YES < -0.030 con n≥400 O 3 bloques consecutivos de 30 ops con CLV < -0.020. Actualmente: n=284, CLV=-0.007 (no significativo). Umbral ~116 ops más. Una línea: `if dec == 'BUY_YES': return None` en s_order_flow_5m.
- [ ] MAE/MFE tracking: cruzar historial precios con posiciones abiertas → si precio_yes ≥ prob_modelo×0.9 antes de expirar → señal de salida anticipada (especialmente para WEEKLY_PRICE y PRICE_TARGET)
- [ ] UPDOWN_OU_5M: probar umbral pct mínimo más alto (|pct|>0.15%) para señales de mayor RR — menos ops, mayor edge por op. Validar cuando n≥100.
- [ ] Random Forest sobre features (pct, sigma, drift, delta_ratio) → requiere Jon-Becker n≥5000
- [ ] Feature velocidad_precio_yes: pct_change del precio YES en últimos 5min de historial → añadir a features de UPDOWN_GBM para detectar herd behavior (mispricings cuando crowd pierde independencia)
- [ ] Grid search de parámetros (THETA_OU, REGIME_THRESHOLD, DELTA_MAX...) sobre Jon-Becker — cuando tengamos los datos. Inspirado en AlphaEvolve (arxiv 2506.13131) pero con scipy.optimize, no LLMs.
