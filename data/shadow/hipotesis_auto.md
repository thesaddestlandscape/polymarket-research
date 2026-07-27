# Hipótesis automáticas — 2026-07-27 04:00 UTC
_Generado por shadow_postmortem.py sobre 37703 resoluciones (PNL=+7833.48€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.200 (n=2180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.194 (n=1174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.331 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=2677)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.187 (n=1174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.334 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=2854)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.170)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.217 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.209 (n=547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.266 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.217 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.357 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=734)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.193)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.244 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.635 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `8687.1649` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8687.1649 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.266 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `5976.8472` → IC=+0.183 (n=159)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 5976.8472 (IC base=+0.168)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.219 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.351 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.193)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.575 (IC base=+0.148)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.575 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.184 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 8.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.405 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.42` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.42 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4203.8302` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4203.8302 (IC base=+0.140)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.240 (n=198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.221 (n=242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.322 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.221 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2374.2498` → IC=+0.229 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2374.2498 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.211 (n=575)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.37` → IC=+0.266 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `1581.0777` → IC=+0.208 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1581.0777 (IC base=+0.203)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.224 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.191 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` < `0.64` → IC=+0.204 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.64 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.191 (n=147)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.575 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `3436.2112` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3436.2112 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.123 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 12.0 (IC base=+0.109)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.156 (n=152)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.109)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=2397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.447` → IC=+0.140 (n=331)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.447 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.025` → IC=+0.183 (n=768)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.025 (IC base=+0.116)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.124 (n=1469)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` > 0.0103 (IC base=+0.094)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.151 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0045 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.4306` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.4306 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.1011` → IC=+0.149 (n=266)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1011 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.702` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.702 (IC base=+0.111)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.169 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0042 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.3858` → IC=+0.172 (n=62)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3858 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.1506` → IC=+0.147 (n=117)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1506 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.167` → IC=+0.188 (n=126)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 7.167 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.602` → IC=+0.142 (n=146)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.602 (IC base=+0.067)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.217` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.217
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=592)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.374` → IC=+0.227 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.374 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.144 (n=400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 8.0 (IC base=+0.094)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.161 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0101 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0208` → IC=+0.151 (n=330)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0208 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.6221` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6221 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1078` → IC=+0.131 (n=356)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1078 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.54` → IC=+0.259 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.54 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.149 (n=915)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0083 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.161 (n=340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3403` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.3403 (IC base=+0.139)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.192 (n=1119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0075 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=1578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.197 (n=483)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.548` → IC=+0.242 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.548 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.157 (n=1343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0067 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.131 (n=1403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 12.0 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.9408` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.9408 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.6879` → IC=+0.120 (n=2124)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.6879 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.258` → IC=+0.139 (n=297)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.258 (IC base=+0.121)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.137 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0047 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.163 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 7.0 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.4476` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4476 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.045` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.045 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.456` → IC=+0.145 (n=187)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 4.456 (IC base=+0.092)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.192 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0075 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.155 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 12.0 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1126` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1126 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.301` → IC=+0.198 (n=114)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 7.301 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.483` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.483 (IC base=+0.091)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.203 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.148 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.1796` → IC=+0.156 (n=161)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1796 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.665` → IC=+0.275 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.665 (IC base=+0.117)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0179` → IC=+0.260 (n=394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0179 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.237 (n=393)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.256 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.4345` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4345 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.003` → IC=+0.362 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.003 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.243 (n=520)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1883` → IC=+0.319 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1883 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.52` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.52 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.425` → IC=+0.204 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.425 (IC base=+0.211)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.146 (n=541)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0126 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=1498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.4497` → IC=+0.152 (n=326)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.4497 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.34` → IC=+0.258 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.34 (IC base=+0.106)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.145 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.004 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.142 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.4428` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4428 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.986` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.986 (IC base=+0.099)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.152 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0037 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.728` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.728 (IC base=+0.066)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `7.784` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.784
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=471)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.386` → IC=+0.238 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.386 (IC base=+0.061)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0204` → IC=+0.183 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0204 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0143` → IC=+0.178 (n=333)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0143 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.175 (n=447)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.2413` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2413 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.065` → IC=+0.287 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.065 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.179 (n=636)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0076 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.175 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 12.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.165 (n=222)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.3421` → IC=+0.226 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3421 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.52` → IC=+0.157 (n=651)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 9.52 (IC base=+0.159)

### GBM_LATE_60M
- **FILTRO** `sigma_ewma_delta_pct` < `14.633` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 14.633
  - _Potencial_: sin este filtro IC_bueno=+0.206 (n=15)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.173 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0044 (IC base=-0.008)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.633` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.633 (IC base=-0.008)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0034` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `sigma_h` < `0.008` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.159 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.005 (IC base=+0.026)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0084` → IC=-0.333 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=32)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=33)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.294 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.333 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` < `0.0135` → IC=-0.258 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0135
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=17)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `sigma_h` > `0.0103` → IC=-0.271 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.202 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.261 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

### LEADLAG_BTC_XRP_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=156)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=156)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=153)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `total_vol_5m` < `197.886` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 197.886 (IC base=+0.031)

### ORDER_FLOW_5M#BTC#5min
- **FILTRO** `delta_ratio` |x|≤ `0.3925` → IC=-0.180 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.3925
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

### ORDER_FLOW_5M#DOGE#5min
- **FILTRO** `total_vol_5m` > `1108292.0` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `total_vol_5m` > 1108292.0
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=61)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `hora_utc` < `4.0` → IC=+0.129 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 4.0 (IC base=+0.067)

### ORDER_FLOW_5M#XRP#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4307` → IC=-0.136 (n=20)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4307
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0105` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `sigma_h` > `0.0062` → IC=-0.365 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **FILTRO** `T_h` < `145.8988` → IC=-0.423 (n=50)

  - _Acción_: SKIP cuando `T_h` < 145.8988
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `pct_vs_K` |x|> `2.6724` → IC=-0.481 (n=50)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6724
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.433 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `T_h` > `111.9936` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `T_h` > 111.9936
  - _Potencial_: sin este filtro IC_bueno=-0.400 (n=8)

- **FILTRO** `T_h` < `145.9348` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `T_h` < 145.9348
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.409 (n=9)

### STREAK_FADE_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=93)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.196 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.069)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `streak_len` < `4.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `streak_len` < 4.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.485 (IC base=+0.112)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.167 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 9.0 (IC base=+0.079)

- **PATRÓN** `volumen_racha` < `497480.0` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 497480.0 (IC base=+0.079)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

- **FILTRO** `streak_len` > `4.0` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=47)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `6441.4408` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 6441.4408
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### STREAK_MOM_5M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `streak_len` > `4.0` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=120)

- **FILTRO** `libro_liquidez` < `3352.7321` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 3352.7321
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=103)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=149)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=85)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `libro_liquidez` < `8045.5084` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 8045.5084
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=30)

- **FILTRO** `libro_liquidez` < `3331.5444` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3331.5444
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=33)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.203 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `streak_len` > `3.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

- **FILTRO** `libro_liquidez` < `3688.8474` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 3688.8474
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=23)

### UPDOWN_GBM#15min
- **PATRÓN** `ibs_15` > `0.7554` → IC=+0.221 (n=457)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7554 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1647` → IC=+0.170 (n=222)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1647 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.207` → IC=+0.150 (n=204)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 7.207 (IC base=+0.054)

### UPDOWN_GBM#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.01` → IC=-0.300 (n=28)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `sigma_h` > `0.0024` → IC=-0.333 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0024
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.03` → IC=-0.167 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.143 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_h` < `0.0058` → IC=-0.208 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `ibs_15` > `0.1935` → IC=-0.175 (n=38)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1935
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `ibs_15` < `0.5186` → IC=-0.204 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5186
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` < `19.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `ibs_15` < `0.7622` → IC=-0.182 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7622
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.1169` → IC=-0.182 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1169
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=40)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.124 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0047 (IC base=+0.099)

- **PATRÓN** `drift_60min` |x|≤ `0.2204` → IC=+0.140 (n=301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2204 (IC base=+0.099)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0647` → IC=+0.122 (n=302)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.61€ cuando `delta_ratio_macro` |x|> 0.0647 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.140 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 19.0 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.149 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.099)

- **PATRÓN** `ibs_15` > `0.7248` → IC=+0.241 (n=234)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7248 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1435` → IC=+0.222 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1435 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.773` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 20.773 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.986` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 5.986 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.190 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0061 (IC base=+0.024)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.67` → IC=+0.192 (n=199)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.67 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.232` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.232 (IC base=+0.042)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.157 (n=132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0056 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.4501` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.4501 (IC base=+0.063)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `sigma_h` > `0.0204` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0204
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `sigma_h` < `0.0133` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=35)

- **FILTRO** `drift_15min` |x|> `0.3058` → IC=-0.136 (n=31)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3058
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1932` → IC=-0.167 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1932
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0549` → IC=-0.192 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0549
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

- **FILTRO** `sigma_h` > `0.0086` → IC=-0.154 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0086
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `drift_15min` |x|> `0.4751` → IC=-0.237 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4751
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `ibs_15` < `0.0526` → IC=+0.130 (n=79)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` < 0.0526 (IC base=+0.075)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.8242` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 144.8242
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

- **PATRÓN** `T_h` > `146.1132` → IC=+0.428 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.333)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.8515` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.8515 (IC base=+0.263)

- **PATRÓN** `pct_dist` |x|≤ `0.836` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.836 (IC base=+0.263)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9965` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9965 (IC base=+0.263)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1426` → IC=+0.398 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1426 (IC base=+0.402)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.419 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.7554 sube el IC de +0.054 a +0.221 en UPDOWN_GBM#15min (n=457). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7248 sube el IC de +0.099 a +0.241 en UPDOWN_GBM#BTC#15min (n=234). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.67 sube el IC de +0.042 a +0.192 en UPDOWN_GBM#ETH#15min (n=199). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#XRP` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1348 | +0.104 | +36.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1348 | +0.104 | +36.47€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 530 | +0.098 | +1.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 530 | +0.098 | +1.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 501 | +0.126 | +13.64€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 501 | +0.126 | +13.64€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 298 | +0.080 | +21.24€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 298 | +0.080 | +21.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 45 | +0.394 | +5.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 45 | +0.394 | +5.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 45 | +0.394 | +5.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 45 | +0.394 | +5.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 6666 | +0.179 | -23.92€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 4396 | +0.203 | -30.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 294 | +0.057 | -17.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 802 | +0.123 | -67.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1174 | +0.159 | +91.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1960 | +0.186 | +8.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1461 | +0.199 | -44.37€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 97 | +0.045 | -10.89€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 392 | +0.183 | +67.03€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 8 | +0.120 | +5.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 7 | +0.097 | +4.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 2342 | +0.168 | -48.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1447 | +0.198 | -14.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 97 | -0.025 | -22.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 406 | +0.125 | -32.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 392 | +0.145 | +21.03€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL | 2317 | +0.185 | +8.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1448 | +0.212 | +24.14€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 98 | +0.150 | +16.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 381 | +0.127 | -35.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 390 | +0.148 | +3.34€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#XRP | 35 | +0.149 | +1.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 29 | +0.113 | -2.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 411 | +0.306 | +11.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 411 | +0.306 | +11.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 411 | +0.306 | +11.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 411 | +0.306 | +11.51€ | 0 | 0 |
| ✅ GBM_LATE_15M | 8165 | +0.094 | +2470.71€ | 0 | 4 |
| ✅ GBM_LATE_15M#15min | 8165 | +0.094 | +2470.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1976 | +0.073 | +349.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1976 | +0.073 | +349.82€ | 0 | 5 |
| ✅ GBM_LATE_15M#ETH | 1801 | +0.075 | +305.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1801 | +0.075 | +305.74€ | 0 | 6 |
| ✅ GBM_LATE_15M#SOL | 2197 | +0.083 | +747.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2197 | +0.083 | +747.70€ | 1 | 3 |
| ✅ GBM_LATE_15M#XRP | 2191 | +0.141 | +1067.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2191 | +0.141 | +1067.45€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5396 | +0.117 | +2547.08€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5396 | +0.117 | +2547.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1415 | +0.086 | +502.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1415 | +0.086 | +502.03€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1414 | +0.090 | +492.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1414 | +0.090 | +492.06€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1350 | +0.085 | +521.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1350 | +0.085 | +521.17€ | 0 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1217 | +0.222 | +1031.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1217 | +0.222 | +1031.82€ | 0 | 10 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 278 | +0.071 | +104.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 278 | +0.071 | +104.34€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 117 | -0.055 | +7.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 117 | -0.055 | +7.77€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 5386 | +0.069 | +1454.25€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#15min | 5386 | +0.069 | +1454.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1287 | +0.038 | +173.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1287 | +0.038 | +173.67€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1315 | +0.026 | +105.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1315 | +0.026 | +105.72€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1267 | +0.029 | +236.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1267 | +0.029 | +236.28€ | 1 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1517 | +0.166 | +938.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1517 | +0.166 | +938.58€ | 0 | 11 |
| ✅ GBM_LATE_5M | 808 | -0.031 | -1.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 808 | -0.031 | -1.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 171 | -0.038 | -11.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 171 | -0.038 | -11.21€ | 0 | 0 |
| 🚫 GBM_LATE_5M#ETH | 82 | -0.202 | -15.93€ | 0 | 0 |
| 🚫 GBM_LATE_5M#ETH#5min | 82 | -0.202 | -15.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 291 | -0.050 | +9.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 291 | -0.050 | +9.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 264 | +0.049 | +16.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 264 | +0.049 | +16.12€ | 0 | 0 |
| ✅ GBM_LATE_60M | 341 | -0.106 | +7.13€ | 3 | 2 |
| ✅ GBM_LATE_60M#60min | 341 | -0.106 | +7.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 122 | -0.040 | +2.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 122 | -0.040 | +2.22€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 109 | -0.131 | -6.35€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 109 | -0.131 | -6.35€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 354 | -0.056 | -5.08€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 354 | -0.056 | -5.08€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 354 | -0.056 | -5.08€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 354 | -0.056 | -5.08€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 294 | +0.010 | +9.53€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 294 | +0.010 | +9.53€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 294 | +0.010 | +9.53€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 294 | +0.010 | +9.53€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1684 | +0.011 | +9.99€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1548 | +0.006 | -2.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 217 | +0.034 | +4.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 217 | +0.034 | +4.59€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 226 | +0.000 | -2.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 226 | +0.000 | -2.22€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 269 | -0.017 | -8.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 269 | -0.017 | -8.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 331 | +0.043 | +14.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 331 | +0.043 | +14.36€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#XRP | 214 | -0.009 | -6.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 214 | -0.009 | -6.01€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 150 | -0.171 | -4.78€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 58 | -0.183 | -0.24€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#ETH#atexpiry | 52 | -0.204 | -3.53€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 6 | +0.000 | +3.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 30 | +0.031 | +13.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 28 | +0.033 | +13.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 136 | -0.188 | -7.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 14 | +0.000 | +2.83€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 13 | +0.195 | +3.10€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 6 | +0.113 | +1.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 6 | +0.113 | +1.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 13 | +0.195 | +3.10€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 295 | +0.069 | +23.47€ | 1 | 1 |
| ✅ STREAK_FADE_15M#15min | 295 | +0.069 | +23.47€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | +0.038 | -2.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | +0.038 | -2.53€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 88 | +0.122 | +20.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 88 | +0.122 | +20.43€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 144 | +0.048 | +5.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 144 | +0.048 | +5.58€ | 0 | 2 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 0 | 0 |
| 🚫 STREAK_MOM_5M | 320 | -0.059 | -26.41€ | 5 | 0 |
| ✅ STREAK_MOM_5M#5min | 320 | -0.059 | -26.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 107 | -0.060 | -7.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 107 | -0.060 | -7.33€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 115 | -0.013 | -5.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 115 | -0.013 | -5.74€ | 2 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 2760 | +0.034 | +244.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2497 | +0.051 | +282.99€ | 0 | 3 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 130 | -0.061 | -11.21€ | 6 | 0 |
| ✅ UPDOWN_GBM#BNB | 290 | +0.055 | +55.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 290 | +0.055 | +55.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 578 | +0.053 | +68.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 494 | +0.087 | +83.14€ | 1 | 10 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 234 | +0.017 | +13.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 231 | +0.019 | +13.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1073 | +0.040 | +73.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 979 | +0.053 | +85.33€ | 0 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 285 | -0.040 | -0.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 216 | -0.014 | +5.84€ | 4 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 32 | -0.088 | -1.46€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 298 | +0.043 | +36.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 287 | +0.054 | +39.42€ | 4 | 1 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 183 | +0.305 | +35.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 183 | +0.305 | +35.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 84 | +0.314 | +18.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 84 | +0.314 | +18.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 99 | +0.292 | +17.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 99 | +0.292 | +17.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1993 | +0.155 | +904.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1993 | +0.155 | +904.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 192 | +0.211 | +124.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 192 | +0.211 | +124.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 208 | +0.114 | +37.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 208 | +0.114 | +37.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 179 | +0.224 | +130.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 179 | +0.224 | +130.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 386 | +0.165 | +150.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 386 | +0.165 | +150.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 475 | +0.087 | +122.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 475 | +0.087 | +122.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 553 | +0.176 | +339.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 553 | +0.176 | +339.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 17 | +0.022 | +0.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 17 | +0.022 | +0.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 17 | +0.022 | +0.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 17 | +0.022 | +0.10€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M | 84 | -0.209 | -18.89€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#5min | 84 | -0.209 | -18.89€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB | 13 | -0.195 | -5.11€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB#5min | 13 | -0.195 | -5.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 14 | -0.087 | -1.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 14 | -0.087 | -1.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 13 | -0.108 | -2.68€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 13 | -0.108 | -2.68€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH | 18 | -0.225 | -4.88€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH#5min | 18 | -0.225 | -4.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 13 | -0.065 | -1.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 13 | -0.065 | -1.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 13 | -0.108 | -2.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 13 | -0.108 | -2.67€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 407 | +0.216 | +92.16€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 116 | +0.144 | -10.31€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 116 | +0.161 | -5.67€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 175 | +0.297 | +108.13€ | 0 | 2 |