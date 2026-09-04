# Hipótesis automáticas — 2026-09-04 18:44 UTC
_Generado por shadow_postmortem.py sobre 284833 resoluciones (PNL=+27958.82€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.465` → IC=-0.170 (n=113)

  - _Acción_: SKIP cuando `py_entrada` < 0.465
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=345)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.392 (n=81)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=294)

- **PATRÓN** `py_entrada` > `0.465` → IC=+0.252 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.465 (IC base=+0.148)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.154 (n=316)

  - _Acción_: Kelly boost +0.77€ cuando `n_ballena_banda` > 19.0 (IC base=+0.148)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.240 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.148)

- **PATRÓN** `banda_hit_calibrado` > `0.6183` → IC=+0.246 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6183 (IC base=+0.148)

- **PATRÓN** `banda_z` > `11.589` → IC=+0.269 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.589 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.147 (n=327)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 16.0 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=358)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3140.839` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3140.839 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.135 (n=294)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.130 (n=79)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 125.0 (IC base=+0.020)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=167)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=192)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.280 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.175)

- **PATRÓN** `n_ballena_banda` > `18.0` → IC=+0.181 (n=252)

  - _Acción_: Kelly boost +0.91€ cuando `n_ballena_banda` > 18.0 (IC base=+0.175)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.241 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.175)

- **PATRÓN** `banda_hit_calibrado` > `0.7976` → IC=+0.272 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7976 (IC base=+0.175)

- **PATRÓN** `banda_z` > `11.678` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.678 (IC base=+0.175)

- **PATRÓN** `ballenas_wallet_edge_medio` > `3.265` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `ballenas_wallet_edge_medio` > 3.265 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=279)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `3000.0061` → IC=+0.183 (n=165)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3000.0061 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.127 (n=167)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 96.0 (IC base=+0.007)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=93)

- **FILTRO** `banda_hit_calibrado` < `0.6329` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6329
  - _Potencial_: sin este filtro IC_bueno=+0.238 (n=82)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=97)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=69)

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.085)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.085)

- **PATRÓN** `banda_z` > `8.441` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.441 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `147.45` → IC=-0.299 (n=3834)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.45
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=11505)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.02` → IC=-0.307 (n=505)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.02
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1518)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `626.37` → IC=-0.149 (n=329)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 626.37
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=644)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.04` → IC=-0.406 (n=511)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.04
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=1535)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `144.24` → IC=-0.314 (n=851)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.24
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=2556)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `158.1` → IC=-0.379 (n=923)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.1
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=1876)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=8149)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=2072)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2371.8003` → IC=+0.169 (n=1986)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2371.8003 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=5654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=6751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.254 (n=5070)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=3969)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `1946.1748` → IC=+0.175 (n=3388)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1946.1748 (IC base=+0.140)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=906)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.389 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `13169.0911` → IC=+0.221 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13169.0911 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=945)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.259 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=1202)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `12563.1974` → IC=+0.206 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.1974 (IC base=+0.189)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.121 (n=576)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 15.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` > `0.595` → IC=+0.164 (n=296)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` > 0.595 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `4800.0243` → IC=+0.151 (n=216)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4800.0243 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.180 (n=339)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.41 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4142.7901` → IC=+0.152 (n=323)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4142.7901 (IC base=+0.131)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=96)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=1421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.311 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.264 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.262 (n=737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` < `0.2` → IC=+0.404 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.2 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.260 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `2217.7203` → IC=+0.269 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2217.7203 (IC base=+0.257)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.136 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.142 (n=350)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.66` → IC=+0.258 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.66 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=470)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `1535.0309` → IC=+0.155 (n=389)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1535.0309 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.164 (n=144)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.426 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.210 (n=378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.348 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.211 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `930.4194` → IC=+0.213 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 930.4194 (IC base=+0.205)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.335 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=172)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `3436.2112` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3436.2112 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.226 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=295)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **FILTRO** `libro_liquidez` < `11360.7096` → IC=-0.266 (n=143)

  - _Acción_: SKIP cuando `libro_liquidez` < 11360.7096
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=6320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=5372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.202 (n=3007)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `3258.7888` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3258.7888 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=1563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.180 (n=1627)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.165)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.317)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.317)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.176 (n=1524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.178 (n=1355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.174 (n=1632)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.74 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.182 (n=1081)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.72 (IC base=+0.170)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.238 (n=1221)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.315 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.237)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `18.0` → IC=-0.217 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.250 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=1553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=1326)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.189 (n=805)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.7 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.183 (n=661)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.73 (IC base=+0.183)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.450 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.442 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.481 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.441 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `3434.6605` → IC=+0.452 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3434.6605 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.450 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.942` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.942 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `10987.7492` → IC=+0.463 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10987.7492 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.448 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `2106.7117` → IC=+0.450 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2106.7117 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.424 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.462 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.432 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `libro_liquidez` < `6196.1698` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 6196.1698
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=17764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.208 (n=18004)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.189)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=3687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.151 (n=3146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 15.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.180 (n=2664)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.72 (IC base=+0.150)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=3114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=1157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.272 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=3056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.163 (n=2419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 12.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=3117)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.163)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=1574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=1180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.271 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=1236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.238 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=1267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=2361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.230 (n=1525)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.204 (n=2553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.131)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.143 (n=2399)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` < 4.01 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.158 (n=2398)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.94 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.148 (n=3517)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `3.87` → IC=+0.158 (n=2392)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 3.87 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.209 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.137)

- **PATRÓN** `restante_min` < `3.96` → IC=+0.150 (n=1203)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` < 3.96 (IC base=+0.137)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.149 (n=1658)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.88 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.160 (n=1735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 8.0 (IC base=+0.137)

- **PATRÓN** `lag_apertura_s` < `6.88` → IC=+0.148 (n=1568)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 6.88 (IC base=+0.137)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.126)

- **PATRÓN** `restante_min` < `4.44` → IC=+0.132 (n=1592)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.44 (IC base=+0.126)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.168 (n=1216)

  - _Acción_: Kelly boost +0.84€ cuando `restante_min` > 4.95 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=3617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.135 (n=1782)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.126)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.169 (n=1205)

  - _Acción_: Kelly boost +0.84€ cuando `lag_apertura_s` < 3.28 (IC base=+0.126)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.315 (n=646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.368 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1758.8943` → IC=+0.294 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1758.8943 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.298 (n=280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.277 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5522.4076` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5522.4076 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.338 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.377 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1569.8406` → IC=+0.320 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1569.8406 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.338 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.330)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.348 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.330)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.367 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.330)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `687.7728` → IC=+0.373 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 687.7728 (IC base=+0.330)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.433 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.428 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.424 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `2007.6359` → IC=+0.436 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2007.6359 (IC base=+0.423)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.432 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.422 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.421)

- **PATRÓN** `libro_liquidez` > `5459.2656` → IC=+0.460 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5459.2656 (IC base=+0.421)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.434 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.424 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.426 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `1979.4391` → IC=+0.459 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.4391 (IC base=+0.427)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `py_entrada` > `0.93` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.365)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.411 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.278 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1046.7727` → IC=+0.277 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1046.7727 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.411 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.278 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1046.7727` → IC=+0.277 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1046.7727 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.36` → IC=+0.129 (n=3813)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.36 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.2661` → IC=+0.223 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2661 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.4566` → IC=+0.222 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4566 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.633` → IC=+0.150 (n=1448)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 5.633 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.6936` → IC=+0.227 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6936 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.242 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1707` → IC=+0.184 (n=654)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1707 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `2.8454` → IC=+0.177 (n=2298)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.8454 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` > `1.4725` → IC=+0.174 (n=2298)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4725 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.4016` → IC=+0.128 (n=3664)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.4016 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.3361` → IC=+0.144 (n=1355)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.3361 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.6867` → IC=+0.145 (n=575)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6867 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.0473` → IC=+0.144 (n=593)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0473 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.3034` → IC=+0.240 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3034 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.8143` → IC=+0.212 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8143 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.209 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.042)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.185 (n=284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.2868` → IC=+0.157 (n=849)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2868 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=308)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.673` → IC=+0.296 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.673 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.228 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.6489` → IC=+0.141 (n=751)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.6489 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.442` → IC=+0.145 (n=751)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.442 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=694)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.188 (n=498)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 64.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.263 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.271 (n=518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.0819` → IC=+0.321 (n=194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0819 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.261 (n=526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.266 (n=587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.4058` → IC=+0.280 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4058 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.205` → IC=+0.273 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.205 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0688` → IC=+0.257 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0688 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `1.5851` → IC=+0.283 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5851 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.266 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1709.5178` → IC=+0.280 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1709.5178 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.259 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=+0.256)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.256 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.224 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.098` → IC=+0.247 (n=223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.098 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9278` → IC=+0.241 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9278 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1813` → IC=+0.218 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1813 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.4771` → IC=+0.219 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4771 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.257` → IC=+0.230 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.257 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.07` → IC=+0.216 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.07 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `0.6988` → IC=+0.230 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6988 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.228 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.218 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.4797` → IC=+0.245 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4797 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `11045.5521` → IC=+0.237 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11045.5521 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.148 (n=487)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0041 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.145 (n=651)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.003 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.1769` → IC=+0.145 (n=486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1769 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.141 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.141 (n=769)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 18.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6604` → IC=+0.164 (n=729)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.6604 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1424` → IC=+0.162 (n=614)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1424 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.224 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6178` → IC=+0.173 (n=243)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6178 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1491` → IC=+0.219 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1491 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.7226` → IC=+0.159 (n=414)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7226 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.3957` → IC=+0.153 (n=621)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.3957 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=940)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12702.6869` → IC=+0.154 (n=486)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 12702.6869 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.174 (n=182)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 214.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.175 (n=804)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0059 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.197 (n=391)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 8.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.256 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.358` → IC=+0.274 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.358 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.160 (n=662)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `3.8745` → IC=+0.158 (n=718)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 3.8745 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.6803` → IC=+0.174 (n=717)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.6803 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.188 (n=835)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.192 (n=488)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 47.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.247 (n=658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.5051` → IC=+0.236 (n=658)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5051 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.244 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=303)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0315` → IC=+0.297 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0315 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.768` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.768 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3755` → IC=+0.291 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3755 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7033` → IC=+0.257 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7033 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `3.1107` → IC=+0.222 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1107 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.232 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.236)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.137 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=560)

- **FILTRO** `ibs_20min` > `0.8241` → IC=-0.180 (n=298)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8241
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=897)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=72)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1123)

- **PATRÓN** `dist_vwap_pct` < `0.2121` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2121 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` < `0.6119` → IC=+0.367 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6119 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` > `1.1956` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1956 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.1153` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1153 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.435` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.435 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.9064` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9064 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `178.0` → IC=+0.267 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 178.0 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.2862` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2862 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.8023` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8023 (IC base=-0.040)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=145)

- **FILTRO** `ibs_20min` < `0.1818` → IC=-0.202 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1818
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=140)

- **FILTRO** `sigma_h` > `0.0109` → IC=-0.131 (n=451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1357)

- **FILTRO** `sigma_ewma_delta_pct` > `8.368` → IC=-0.189 (n=207)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.368
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=1601)

- **FILTRO** `volumen_pendiente_norm` < `0.1097` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1097
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=26)

- **FILTRO** `volumen_spike_ratio` > `1.4181` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4181
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=16)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.141 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0066 (IC base=+0.035)

- **PATRÓN** `ibs_20min` > `0.2791` → IC=+0.135 (n=124)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.2791 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.7744` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7744 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.6091` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6091 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4181` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4181 (IC base=-0.058)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5186` → IC=-0.166 (n=363)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5186
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=706)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=127)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=942)

- **FILTRO** `ibs_20min` > `0.7885` → IC=-0.192 (n=426)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7885
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1281)

- **FILTRO** `sigma_ewma_delta_pct` > `8.99` → IC=-0.135 (n=198)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.99
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1509)

- **PATRÓN** `dist_vwap_pct` > `0.5816` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5816 (IC base=-0.101)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.209 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2197 (IC base=-0.101)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.0617` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0617 (IC base=-0.101)

- **PATRÓN** `volumen_spike_ratio` < `1.4974` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4974 (IC base=-0.101)

- **PATRÓN** `volumen_spike_ratio` > `2.4097` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4097 (IC base=-0.101)

- **PATRÓN** `dist_vwap_pct` < `0.242` → IC=+0.218 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.242 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` > `1.295` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.295 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2526` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2526 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.3135` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.3135 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` > `1.8841` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8841 (IC base=-0.046)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 21.0 (IC base=-0.046)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.174 (n=1566)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0094 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.2963` → IC=+0.143 (n=4696)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.2963 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `1.2207` → IC=+0.295 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2207 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.472` → IC=+0.122 (n=2485)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 2.472 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `0.6809` → IC=+0.218 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6809 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` < `0.1143` → IC=+0.216 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1143 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2516` → IC=+0.242 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2516 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.4852` → IC=+0.232 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4852 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.8039` → IC=+0.216 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8039 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.295 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5816` → IC=+0.132 (n=4543)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5816 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.7799` → IC=+0.248 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7799 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.1662` → IC=+0.221 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1662 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.7079` → IC=+0.223 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7079 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2256` → IC=+0.249 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2256 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2561` → IC=+0.343 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2561 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.4031` → IC=+0.277 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4031 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.268 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 67.0 (IC base=+0.053)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3021` → IC=-0.150 (n=392)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3021
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=797)

- **FILTRO** `sigma_ewma_delta_pct` > `2.449` → IC=-0.158 (n=346)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.449
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=751)

- **PATRÓN** `ibs_20min` > `0.8315` → IC=+0.220 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8315 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.072` → IC=+0.124 (n=448)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.072 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.8924` → IC=+0.239 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8924 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4729` → IC=+0.224 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4729 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.342 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.025)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8608` → IC=-0.161 (n=393)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8608
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1180)

- **PATRÓN** `volumen_spike_ratio` < `2.0448` → IC=+0.125 (n=305)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.0448 (IC base=-0.010)

- **PATRÓN** `ballena_activa_n` < `261.0` → IC=+0.149 (n=112)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 261.0 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` < `0.1223` → IC=+0.158 (n=179)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1223 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.5828` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.5828 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.1078` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.1078 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.0627` → IC=+0.143 (n=141)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.0627 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2157` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2157 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.9512` → IC=+0.195 (n=126)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.9512 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.148 (n=143)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.3908 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 263.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.270 (n=506)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1246` → IC=+0.228 (n=333)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1246 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.254 (n=364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.7083` → IC=+0.261 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7083 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.36` → IC=+0.303 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.36 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` < `0.1095` → IC=+0.239 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1095 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.7205` → IC=+0.234 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7205 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.323 (n=541)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.332 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` < `0.3299` → IC=+0.316 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3299 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.688` → IC=+0.339 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.688 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.331 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` < `3.4422` → IC=+0.300 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.4422 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `2.3438` → IC=+0.314 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3438 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `1665.1432` → IC=+0.308 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1665.1432 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.300 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.306)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.147 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=522)

- **FILTRO** `ibs_20min` < `0.5574` → IC=-0.167 (n=379)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5574
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=379)

- **FILTRO** `ibs_20min` > `0.7335` → IC=-0.145 (n=421)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7335
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=818)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.135 (n=83)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1156)

- **PATRÓN** `dist_vwap_pct` > `1.7158` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.7158 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` < `0.8742` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8742 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1716` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1716 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` < `2.2497` → IC=+0.228 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2497 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `1.3689` → IC=+0.212 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3689 (IC base=-0.057)

- **PATRÓN** `ballena_activa_n` < `212.0` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 212.0 (IC base=-0.057)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.8158` → IC=-0.141 (n=669)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8158
  - _Potencial_: sin este filtro IC_bueno=+0.293 (n=346)

- **FILTRO** `ibs_20min` > `0.7561` → IC=-0.230 (n=291)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7561
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=874)

- **FILTRO** `sigma_ewma_delta_pct` > `4.709` → IC=-0.148 (n=296)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.709
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=869)

- **PATRÓN** `ibs_20min` > `0.8158` → IC=+0.293 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8158 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `1.2158` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2158 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.8618` → IC=+0.257 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8618 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.1564` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1564 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` < `0.1162` → IC=+0.257 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1162 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.4502` → IC=+0.298 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4502 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.3531` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3531 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.299 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.4292` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.4292 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `1.2143` → IC=+0.130 (n=117)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2143 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.3913` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.3913 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.338 (n=504)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.262 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.9` → IC=+0.328 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9 (IC base=+0.254)

- **PATRÓN** `dist_vwap_pct` > `0.1627` → IC=+0.315 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1627 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.175` → IC=+0.292 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.175 (IC base=+0.254)

- **PATRÓN** `volumen_regimen` > `0.839` → IC=+0.292 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.839 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.296 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5706` → IC=+0.262 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5706 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `1.832` → IC=+0.259 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.832 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.257 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `2469.6086` → IC=+0.261 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2469.6086 (IC base=+0.254)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.277 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.024` → IC=+0.303 (n=272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.024 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.3231` → IC=+0.279 (n=545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3231 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.289 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.316 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.5366` → IC=+0.281 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5366 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` < `0.2061` → IC=+0.281 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2061 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.432` → IC=+0.297 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.432 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` > `1.2676` → IC=+0.307 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2676 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.2891` → IC=+0.388 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2891 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.1847` → IC=+0.295 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1847 (IC base=+0.277)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.205 (n=1321)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3434` → IC=+0.169 (n=3484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3434 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.281 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.7889` → IC=+0.234 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7889 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.726` → IC=+0.235 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.726 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.162 (n=2678)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6285 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1049` → IC=+0.185 (n=1479)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1049 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `2.3154` → IC=+0.162 (n=3248)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.3154 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.164 (n=4052)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.03 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3958.3691` → IC=+0.173 (n=1320)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3958.3691 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.178 (n=2872)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 144.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.187 (n=3258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0084 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.210 (n=1234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=1774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.182 (n=1700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 7.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.438` → IC=+0.227 (n=3702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.438 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.2257` → IC=+0.171 (n=2802)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2257 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.028` → IC=+0.211 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.028 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1724` → IC=+0.165 (n=2791)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1724 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6221` → IC=+0.160 (n=2792)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6221 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.244 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6536` → IC=+0.201 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6536 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.177 (n=2662)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 158.0 (IC base=+0.177)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.180 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.205 (n=303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.2919` → IC=+0.199 (n=665)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.2919 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.234 (n=250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.545` → IC=+0.291 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.545 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.258 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.6366` → IC=+0.166 (n=582)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.6366 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.4557` → IC=+0.168 (n=582)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4557 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.207 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.193 (n=346)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 59.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.265 (n=376)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1635` → IC=+0.309 (n=281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1635 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.261 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.2712` → IC=+0.264 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2712 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.691` → IC=+0.252 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.691 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0672` → IC=+0.228 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0672 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2471` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2471 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.9187` → IC=+0.235 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9187 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.250 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.252 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1701.1448` → IC=+0.277 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1701.1448 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.244 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.227 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.4094` → IC=+0.172 (n=587)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4094 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4744` → IC=+0.208 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4744 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.222 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.986` → IC=+0.238 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.986 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.6395` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6395 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.172 (n=266)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.0731 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4783` → IC=+0.202 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4783 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `11364.2884` → IC=+0.188 (n=524)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 11364.2884 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.178 (n=681)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0061 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.0622` → IC=+0.210 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0622 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.4833` → IC=+0.191 (n=678)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.4833 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.1993` → IC=+0.172 (n=683)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1993 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.232` → IC=+0.239 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.232 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6996` → IC=+0.221 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6996 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.158` → IC=+0.223 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.158 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.7228` → IC=+0.160 (n=380)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.7228 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.3935` → IC=+0.161 (n=570)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.3935 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.159 (n=162)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 239.0 (IC base=+0.154)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.211 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1776` → IC=+0.196 (n=412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1776 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.177 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 16.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.188 (n=283)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.632` → IC=+0.314 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.632 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.183 (n=244)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `3.1497` → IC=+0.164 (n=489)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 3.1497 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.7067` → IC=+0.166 (n=555)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7067 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=630)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.190 (n=127)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 18.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.248 (n=490)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.2281` → IC=+0.248 (n=327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2281 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.250 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.374` → IC=+0.266 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.374 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.768` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.768 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.3671` → IC=+0.268 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3671 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.9298` → IC=+0.224 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9298 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `3.0796` → IC=+0.217 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0796 (IC base=+0.230)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.202 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3674` → IC=+0.162 (n=524)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3674 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.169 (n=606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.436` → IC=+0.199 (n=595)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.436 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1538` → IC=+0.184 (n=416)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1538 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.391` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.391 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.212` → IC=+0.211 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.212 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.3003` → IC=+0.223 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3003 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6117` → IC=+0.203 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6117 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=666)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `8808.1502` → IC=+0.187 (n=397)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 8808.1502 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.143 (n=354)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 136.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.211 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3801` → IC=+0.147 (n=664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3801 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.146 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.5401` → IC=+0.179 (n=664)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5401 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.3473` → IC=+0.141 (n=730)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3473 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.371` → IC=+0.207 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.371 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.1582` → IC=+0.137 (n=664)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1582 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.135 (n=664)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6129 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.168 (n=224)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8371` → IC=+0.140 (n=370)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8371 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.5127` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5127 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `5188.5595` → IC=+0.138 (n=443)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 5188.5595 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `181.0` → IC=+0.123 (n=420)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 181.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.147 (n=664)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=780)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5313` → IC=+0.187 (n=743)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5313 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.1473` → IC=+0.250 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1473 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.270 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.120 (n=743)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` > 0.6285 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` < `0.1692` → IC=+0.127 (n=744)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1692 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.143 (n=236)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=565)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `3204.5735` → IC=+0.216 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3204.5735 (IC base=+0.111)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.144 (n=310)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0094 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0993` → IC=+0.152 (n=228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0993 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.4681` → IC=+0.221 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4681 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.2471` → IC=+0.143 (n=650)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2471 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.282` → IC=+0.162 (n=270)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.282 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.1714` → IC=+0.145 (n=682)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1714 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.8536` → IC=+0.140 (n=454)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8536 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2708` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2708 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.1049` → IC=+0.196 (n=248)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.1049 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `1446.3615` → IC=+0.150 (n=609)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1446.3615 (IC base=+0.131)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.216 (n=502)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.213 (n=332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.8873` → IC=+0.270 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8873 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1712` → IC=+0.224 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1712 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.182` → IC=+0.240 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.182 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` > `0.686` → IC=+0.210 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.686 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.0834` → IC=+0.254 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0834 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `2.5204` → IC=+0.209 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5204 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.5152` → IC=+0.198 (n=638)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.5152 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.193 (n=861)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.265 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0158` → IC=+0.211 (n=513)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0158 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.6533` → IC=+0.220 (n=769)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6533 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.4102` → IC=+0.256 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4102 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.5074` → IC=+0.216 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5074 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.869` → IC=+0.266 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.869 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.237 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.332 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.6536` → IC=+0.235 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6536 (IC base=+0.211)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.165 (n=386)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.008 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.141 (n=750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.202 (n=431)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.170 (n=852)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.4444 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.9611` → IC=+0.227 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9611 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.597` → IC=+0.178 (n=392)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.597 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8708` → IC=+0.160 (n=460)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8708 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.164` → IC=+0.147 (n=230)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.164 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1727` → IC=+0.178 (n=234)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1727 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4503` → IC=+0.157 (n=266)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4503 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.823` → IC=+0.147 (n=531)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.823 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=890)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `9026.9243` → IC=+0.185 (n=284)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 9026.9243 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.176 (n=211)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 13.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.305` → IC=+0.126 (n=584)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.305 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.97` → IC=+0.133 (n=178)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 7.97 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.1737` → IC=+0.164 (n=215)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1737 (IC base=+0.072)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.152 (n=326)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 22.0 (IC base=+0.072)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.151 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0036 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.178 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 10.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.9306` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9306 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.9611` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9611 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.469` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.469 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6895 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `11253.359` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11253.359 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 160.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.6256` → IC=+0.142 (n=255)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.6256 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.945` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 8.945 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.237 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.285 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.329 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.296 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` > `0.93` → IC=+0.325 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.93 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.292 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.247` → IC=+0.312 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.247 (IC base=+0.258)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.275 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.258)

- **PATRÓN** `volumen_regimen` > `1.145` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.145 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.0968` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0968 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.3651` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3651 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.0296` → IC=+0.332 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0296 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1322` → IC=+0.136 (n=75)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1322 (IC base=+0.042)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.8462` → IC=-0.123 (n=120)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8462
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=123)

- **FILTRO** `ibs_20min` > `0.4375` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4375
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=104)

- **FILTRO** `dist_vwap_pct` > `0.2318` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2318
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=136)

- **FILTRO** `volumen_pendiente_norm` > `0.2195` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2195
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=118)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.170 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 14.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` > `0.8462` → IC=+0.172 (n=123)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8462 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.6872` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6872 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.165` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.165 (IC base=+0.026)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0226` → IC=+0.146 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0226 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.31` → IC=+0.161 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.31 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.4 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.2912` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2912 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.434` → IC=+0.140 (n=159)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.434 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.9833` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.9833 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6571 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.2154` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2154 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.899` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.899 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.213 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.141 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 10.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.0588 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.9736` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9736 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.507` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.507 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6197 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.5677` → IC=+0.138 (n=136)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5677 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2567.2585` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2567.2585 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 16.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.199 (n=2167)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0087 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=4794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1634)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `1.0684` → IC=+0.218 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0684 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.639` → IC=+0.223 (n=2662)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.639 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8833` → IC=+0.159 (n=2203)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8833 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1678` → IC=+0.194 (n=1291)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1678 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8689` → IC=+0.172 (n=2966)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8689 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.167 (n=4524)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3876.3881` → IC=+0.183 (n=1593)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3876.3881 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.211 (n=2275)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.194 (n=4412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0109 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4837` → IC=+0.195 (n=4411)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.4837 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=2127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=1984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5597` → IC=+0.239 (n=4411)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5597 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.4448` → IC=+0.170 (n=3122)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.4448 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.693` → IC=+0.214 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.693 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.7` → IC=+0.189 (n=4128)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.7 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.169 (n=1044)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6225 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `1.197` → IC=+0.162 (n=1043)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.197 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.237` → IC=+0.243 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.237 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.298` → IC=+0.202 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.298 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.182 (n=3285)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 143.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.238 (n=357)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.83` → IC=+0.307 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.83 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2211` → IC=+0.263 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2211 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.5882` → IC=+0.185 (n=309)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5882 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.8895` → IC=+0.174 (n=468)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.8895 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.242 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.274 (n=520)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.274 (n=587)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.299 (n=392)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.276 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.276 (n=601)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.4087` → IC=+0.301 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4087 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.577` → IC=+0.284 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.577 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.299` → IC=+0.324 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.299 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `1.5233` → IC=+0.286 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5233 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.272 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `1477.6104` → IC=+0.280 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1477.6104 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.270 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.268)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.176 (n=347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0035 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.0966` → IC=+0.171 (n=262)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0966 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3271` → IC=+0.204 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3271 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.2345` → IC=+0.215 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2345 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.807` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.807 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.396` → IC=+0.168 (n=688)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 4.396 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.168 (n=785)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2653 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.099` → IC=+0.159 (n=356)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.099 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` < `0.0709` → IC=+0.170 (n=664)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.0709 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2078` → IC=+0.190 (n=156)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2078 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.3899` → IC=+0.177 (n=736)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.3899 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.7227` → IC=+0.177 (n=490)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.7227 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `10774.9458` → IC=+0.183 (n=701)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 10774.9458 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `471.0` → IC=+0.176 (n=582)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 471.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.170 (n=713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0062 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.167 (n=637)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.003 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2731` → IC=+0.178 (n=628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2731 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.169 (n=713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 17.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.6191` → IC=+0.201 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6191 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.1465` → IC=+0.178 (n=617)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1465 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.763` → IC=+0.205 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.763 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6181` → IC=+0.229 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6181 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.141` → IC=+0.235 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.141 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.3983` → IC=+0.197 (n=206)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.3983 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.0427` → IC=+0.192 (n=280)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.0427 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=920)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.169 (n=173)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 291.0 (IC base=+0.163)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.229 (n=460)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.244 (n=330)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.6809` → IC=+0.254 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6809 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.701` → IC=+0.333 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.701 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.2205` → IC=+0.211 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2205 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `3.9028` → IC=+0.204 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.9028 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.4544` → IC=+0.209 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4544 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `1456.9184` → IC=+0.211 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1456.9184 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.259 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.295 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.248 (n=315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.272 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.289 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.47` → IC=+0.288 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.47 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.357` → IC=+0.277 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.357 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `3.0387` → IC=+0.245 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0387 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.3266` → IC=+0.223 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3266 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.224 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.157 (n=697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.156 (n=714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.7337` → IC=+0.240 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7337 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.3732` → IC=+0.185 (n=316)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3732 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.047` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 12.047 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8989` → IC=+0.167 (n=529)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8989 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.2073` → IC=+0.154 (n=264)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2073 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `2.1443` → IC=+0.195 (n=342)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.1443 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=865)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `9553.6554` → IC=+0.235 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9553.6554 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.151 (n=557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0072 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4486` → IC=+0.149 (n=631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4486 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.171 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6809` → IC=+0.175 (n=631)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6809 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.219` → IC=+0.128 (n=264)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.219 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.4068` → IC=+0.131 (n=635)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4068 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.341` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.341 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.22` → IC=+0.131 (n=592)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.22 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.5978` → IC=+0.129 (n=211)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.5978 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.1367` → IC=+0.160 (n=210)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.1367 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5127` → IC=+0.167 (n=190)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5127 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `11624.4939` → IC=+0.184 (n=210)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 11624.4939 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `194.0` → IC=+0.143 (n=488)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 194.0 (IC base=+0.127)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.146 (n=552)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0084 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.135 (n=552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.4762` → IC=+0.177 (n=825)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.4762 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.8706` → IC=+0.187 (n=215)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.8706 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.355` → IC=+0.217 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.355 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=576)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2968.0736` → IC=+0.247 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.0736 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.156 (n=210)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 33.0 (IC base=+0.093)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.173 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0059 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1316` → IC=+0.177 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1316 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=304)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.200 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5915 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.5096` → IC=+0.140 (n=764)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.5096 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.222` → IC=+0.135 (n=779)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.222 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.8623` → IC=+0.140 (n=528)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8623 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.167 (n=265)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5571` → IC=+0.139 (n=283)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5571 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.1793` → IC=+0.138 (n=291)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.1793 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2670.0384` → IC=+0.162 (n=359)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2670.0384 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.028` → IC=+0.249 (n=301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.028 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=948)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.9321` → IC=+0.291 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9321 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.1701` → IC=+0.249 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1701 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.141` → IC=+0.246 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.141 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2248` → IC=+0.229 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2248 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.243 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.8195` → IC=+0.210 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8195 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.275 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0254` → IC=+0.228 (n=332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0254 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.5271` → IC=+0.212 (n=876)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5271 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.211 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.215 (n=1056)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.4964` → IC=+0.263 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4964 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.1806` → IC=+0.220 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1806 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.295` → IC=+0.283 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.295 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.225 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.308 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4567` → IC=+0.202 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4567 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.184 (n=711)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 34.0 (IC base=+0.210)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=1772)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.134 (n=1363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.01 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.2819` → IC=+0.139 (n=1032)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2819 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.9237` → IC=+0.191 (n=516)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.9237 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.472` → IC=+0.138 (n=244)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.472 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.792` → IC=+0.122 (n=1345)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 2.792 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.1741` → IC=+0.155 (n=418)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1741 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4565` → IC=+0.141 (n=511)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4565 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.8939` → IC=+0.141 (n=1021)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8939 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `8972.466` → IC=+0.138 (n=702)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 8972.466 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.165 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0039 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5064` → IC=+0.146 (n=1341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.5064 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.155 (n=447)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.1983` → IC=+0.154 (n=590)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1983 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.4784` → IC=+0.128 (n=361)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.4784 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.342` → IC=+0.137 (n=1338)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 6.342 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1015` → IC=+0.138 (n=1138)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.1015 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1484` → IC=+0.127 (n=1341)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1484 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.144 (n=633)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.4775` → IC=+0.134 (n=1327)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.4775 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.7958` → IC=+0.132 (n=884)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.7958 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=1772)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `4318.7906` → IC=+0.132 (n=1341)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 4318.7906 (IC base=+0.125)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.554` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.554
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.136 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.2159` → IC=+0.125 (n=102)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.2159 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.554` → IC=+0.147 (n=182)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.554 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `0.7903` → IC=+0.123 (n=104)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.7903 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `2.2086` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.2086 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `12617.0993` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 12617.0993 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.170 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0035 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.143 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.1703` → IC=+0.159 (n=274)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1703 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.6448` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6448 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.138 (n=620)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.8701` → IC=+0.147 (n=415)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8701 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.0635` → IC=+0.151 (n=293)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0635 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.143 (n=208)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.112)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.203 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.175 (n=161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0106 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.434` → IC=+0.151 (n=313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.434 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.189 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.9545` → IC=+0.248 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9545 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.295` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.295 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.653` → IC=+0.144 (n=304)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.653 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2159` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2159 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.6778` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.6778 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.4212` → IC=+0.155 (n=236)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4212 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `1738.202` → IC=+0.150 (n=355)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1738.202 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.340 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.256)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.163 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0052 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3932` → IC=+0.141 (n=500)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3932 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.144 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.185` → IC=+0.147 (n=568)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.185 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `1.0394` → IC=+0.172 (n=129)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 1.0394 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.4266` → IC=+0.144 (n=537)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4266 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.989` → IC=+0.146 (n=571)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.989 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1165` → IC=+0.147 (n=500)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1165 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1749` → IC=+0.157 (n=170)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1749 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.172 (n=187)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.8023` → IC=+0.137 (n=373)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.8023 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=493)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8385.7236` → IC=+0.146 (n=568)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8385.7236 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.167 (n=421)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0088 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4106` → IC=+0.205 (n=371)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4106 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.159 (n=288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 10.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3985` → IC=+0.171 (n=281)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.3985 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.7273` → IC=+0.157 (n=467)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.7273 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.927` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.927 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2231` → IC=+0.167 (n=421)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2231 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.7364` → IC=+0.148 (n=376)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7364 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.1489` → IC=+0.155 (n=430)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1489 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.0698` → IC=+0.163 (n=185)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0698 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1791` → IC=+0.172 (n=364)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1791 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.165 (n=413)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `8241.8258` → IC=+0.164 (n=421)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 8241.8258 (IC base=+0.148)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `ibs_20min` < `0.425` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.425
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=78)

- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.008)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0104` → IC=-0.297 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0104
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=189)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.215 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=137)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.233 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6383` → IC=+0.221 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6383 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.8392` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8392 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.248 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.8208` → IC=+0.159 (n=180)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8208 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.1039` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.1039 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1454` → IC=+0.171 (n=168)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1454 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2652` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2652 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.4829` → IC=+0.188 (n=152)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4829 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=224)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `1229.6844` → IC=+0.171 (n=220)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1229.6844 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.0875` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0875 (IC base=-0.124)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.225 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.7892` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7892 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.325` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.325 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.414` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.414 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `1.1089` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1089 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` < `0.0651` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0651 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2127` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2127 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `2.0892` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0892 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` > `1.8765` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8765 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=88)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.687` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.687 (IC base=-0.036)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.364 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=61)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.238 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **FILTRO** `ibs_20min` > `0.6442` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6442
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=35)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.201 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.294 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.7468` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7468 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1621` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1621 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.218` → IC=+0.345 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.218 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.791 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.5821` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.5821 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1359` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1359 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3908 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `1227.4818` → IC=+0.216 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1227.4818 (IC base=+0.123)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0159` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0159
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=67)

- **FILTRO** `volumen_regimen` > `0.8518` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8518
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=24)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.038)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.6744 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.9351` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9351 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.144` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.144 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `1.083` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.083 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0896` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0896 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.1854` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.1854 (IC base=+0.038)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.04 (IC base=+0.038)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1312` → IC=-0.368 (n=36)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1312
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=70)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.463 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=83)

- **FILTRO** `volumen_pendiente_norm` < `0.137` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.137
  - _Potencial_: sin este filtro IC_bueno=-0.333 (n=10)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0038` → IC=-0.250 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `ibs_20min` < `0.6047` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6047
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `volumen_regimen` > `1.0011` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0011
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7335` → IC=-0.464 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7335
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0086` → IC=-0.231 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `volumen_regimen` < `1.0152` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0152
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0084` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `dist_vwap_pct` < `0.2118` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2118
  - _Potencial_: sin este filtro IC_bueno=-0.312 (n=14)

- **FILTRO** `volumen_regimen` < `1.1255` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1255
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.6331` → IC=-0.246 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6331
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=171)

- **PATRÓN** `ibs_20min` > `0.6331` → IC=+0.124 (n=171)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.6331 (IC base=+0.030)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.251 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.672` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 5.672 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0662` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0662 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `2923.7123` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2923.7123 (IC base=+0.051)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=60)

- **FILTRO** `volumen_regimen` < `0.7102` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7102
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.258 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1622 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.501` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 14.501 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.5658` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5658 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.6024` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.6024 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3671.9914` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3671.9914 (IC base=+0.109)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=39)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.057)

- **PATRÓN** `drift_60min` |x|≤ `0.2013` → IC=+0.134 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.2013 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.8029` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.8029 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.1039` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1039 (IC base=+0.057)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2339.7005` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2339.7005 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 19.0 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `2418.7992` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2418.7992 (IC base=+0.038)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_spike_ratio` > `1.5494` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5494
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=8)

- **FILTRO** `dist_vwap_pct` > `0.1588` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1588
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

- **FILTRO** `volumen_regimen` < `1.0195` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0195
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.140 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0047 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.791 (IC base=+0.076)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.076)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2535.3936` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2535.3936 (IC base=+0.096)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=151)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2611.4379` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2611.4379 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2535.3936` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2535.3936 (IC base=+0.096)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.121 (n=151)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.5 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2611.4379` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2611.4379 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=64)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=109)

- **FILTRO** `libro_liquidez` < `2306.3177` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 2306.3177
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=94)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=171)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=157)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `libro_liquidez` < `11811.9773` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 11811.9773
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `libro_liquidez` < `14445.5423` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 14445.5423
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1064)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=47)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=79)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=47)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **PATRÓN** `liq_usd_total` > `58893.21` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `liq_usd_total` > 58893.21 (IC base=+0.004)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.004)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9534` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9534
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=76)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=366)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=404)

- **FILTRO** `liq_n` < `8.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_n` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.7365` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.7365
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=159)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=159)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=131)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=121)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=121)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=90)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=41)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=48)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.3878` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.3878
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=127)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=353)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=744)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=810)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.45` → IC=-0.185 (n=1433)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=4645)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.184 (n=1539)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=4794)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.229 (n=234)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=714)

- **FILTRO** `ibs_20min` < `0.7368` → IC=-0.211 (n=237)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=711)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.163 (n=274)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=834)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.183 (n=244)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=755)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.145 (n=249)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=750)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=964)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.194 (n=328)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=673)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.214 (n=250)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=828)

- **FILTRO** `ibs_20min` > `0.712` → IC=-0.197 (n=269)

  - _Acción_: SKIP cuando `ibs_20min` > 0.712
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=809)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=255)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=766)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.167 (n=247)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=767)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.173 (n=249)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=765)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.149 (n=274)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=750)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.164 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=801)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.200 (n=231)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=722)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=938)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.192 (n=258)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=815)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `15.0` → IC=-0.357 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=139)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=150)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=497)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=503)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=57)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.0752` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0752
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `drift_20min_pct` |x|> `0.1568` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1568
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=90)

- **FILTRO** `ibs_20min` > `0.9979` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9979
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=90)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=56)

- **FILTRO** `ibs_20min` > `0.8837` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8837
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 16.0 (IC base=+0.033)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `py_entrada` < `0.35` → IC=-0.281 (n=3626)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=11180)

- **FILTRO** `ibs_7min` < `0.7133` → IC=-0.241 (n=3701)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7133
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=11105)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.169 (n=5028)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=9778)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.221 (n=4582)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=14119)

- **FILTRO** `ibs_7min` > `0.7143` → IC=-0.173 (n=4654)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=14047)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.157 (n=643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=1520)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=531)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=1632)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.255 (n=712)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=1451)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.221 (n=532)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=1631)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.236 (n=809)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2441)

- **FILTRO** `drift_7min_pct` |x|> `0.1143` → IC=-0.129 (n=1103)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2147)

- **FILTRO** `ibs_7min` > `0.8362` → IC=-0.194 (n=812)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8362
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2438)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.133 (n=603)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=2148)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.259 (n=665)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2086)

- **FILTRO** `ibs_7min` < `0.7701` → IC=-0.192 (n=687)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7701
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2064)

- **FILTRO** `ballena_activa_n` > `168.0` → IC=-0.177 (n=685)

  - _Acción_: SKIP cuando `ballena_activa_n` > 168.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=2066)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.240 (n=651)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2114)

- **FILTRO** `ballena_activa_n` > `108.0` → IC=-0.172 (n=939)

  - _Acción_: SKIP cuando `ballena_activa_n` > 108.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1826)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.187 (n=694)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=1491)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.309 (n=696)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=1489)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.293 (n=545)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1640)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.237 (n=535)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=1650)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.223 (n=785)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2581)

- **FILTRO** `ibs_7min` > `0.794` → IC=-0.170 (n=841)

  - _Acción_: SKIP cuando `ibs_7min` > 0.794
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2525)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=762)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=1747)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.261 (n=604)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=1905)

- **FILTRO** `ibs_7min` < `0.7527` → IC=-0.196 (n=626)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7527
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=1883)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.177 (n=832)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1677)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.234 (n=830)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1692)

- **FILTRO** `ibs_7min` > `0.2764` → IC=-0.179 (n=630)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2764
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=1892)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.185 (n=618)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1904)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.245 (n=665)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2103)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.206 (n=689)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2079)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.186 (n=683)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2085)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.179 (n=836)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2681)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.290 (n=593)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1837)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.238 (n=602)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1828)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.228 (n=590)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1840)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.210 (n=813)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=2468)

- **FILTRO** `ibs_7min` > `0.7692` → IC=-0.163 (n=820)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2461)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=38)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=478)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3986` → IC=+0.146 (n=523)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3986 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `456.268` → IC=+0.163 (n=167)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 456.268 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=244)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3344.3586` → IC=+0.155 (n=204)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3344.3586 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.131 (n=367)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 64.0 (IC base=+0.131)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.264 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.118)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.130 (n=90)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.090)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4128` → IC=+0.195 (n=57)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4128 (IC base=+0.109)

- **PATRÓN** `total_vol_5m` < `498.822` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 498.822 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `7409.4986` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 7409.4986 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.145 (n=74)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 136.0 (IC base=+0.109)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4038` → IC=+0.216 (n=79)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4038 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.257 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.192)

- **PATRÓN** `total_vol_5m` < `6013.826` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 6013.826 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3096.9147` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3096.9147 (IC base=+0.192)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.159 (n=80)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `374733.9` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 374733.9 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `3424.0673` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3424.0673 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.128)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `3.488` → IC=-0.389 (n=61)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.488
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=120)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.363 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=25)

- **FILTRO** `T_h` > `39.9952` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `T_h` > 39.9952
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.132)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `291.9853` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` < 291.9853
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.208 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0092` → IC=-0.178 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0092
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=50)

- **FILTRO** `T_h` > `135.9952` → IC=-0.167 (n=49)

  - _Acción_: SKIP cuando `T_h` > 135.9952
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=151)

- **FILTRO** `T_h` > `145.6762` → IC=-0.360 (n=55)

  - _Acción_: SKIP cuando `T_h` > 145.6762
  - _Potencial_: sin este filtro IC_bueno=-0.307 (n=112)

- **FILTRO** `pct_vs_K` |x|> `4.4208` → IC=-0.448 (n=56)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4208
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=111)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `87.9866` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `T_h` > 87.9866
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **FILTRO** `pct_vs_K` |x|> `3.6199` → IC=-0.444 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.6199
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=59)

- **FILTRO** `sigma_h` < `0.0072` → IC=-0.330 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

- **FILTRO** `T_h` > `144.6172` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=41)

- **PATRÓN** `T_h` < `87.9866` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9866 (IC base=-0.058)

- **PATRÓN** `pct_vs_K` |x|≤ `1.2308` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.2308 (IC base=-0.058)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.005` → IC=-0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=27)

- **FILTRO** `T_h` > `111.9956` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 111.9956
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=36)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=39)

- **FILTRO** `T_h` > `145.5703` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `T_h` > 145.5703
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=31)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0161` → IC=-0.447 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0161
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=6)

- **FILTRO** `T_h` > `135.2296` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `T_h` > 135.2296
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2412` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2412 (IC base=+0.383)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.383)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.419 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.383)

- **PATRÓN** `dist_50` > `0.4092` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4092 (IC base=+0.383)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.383)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.447 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.479)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `7.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=67)

- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=74)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=128)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.038)

- **PATRÓN** `streak_estiramiento` < `0.3698` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3698 (IC base=+0.029)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.144 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=155)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=175)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=177)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=187)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=283)

- **PATRÓN** `streak_estiramiento` < `0.2913` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `streak_estiramiento` < 0.2913 (IC base=+0.038)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=560)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=291)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=370)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=1615)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=893)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=901)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.168 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0073 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1669` → IC=+0.136 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1669 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0597` → IC=+0.133 (n=562)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0597 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.133 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 4.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.5904` → IC=+0.213 (n=562)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5904 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.4266` → IC=+0.152 (n=139)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.4266 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.5508` → IC=+0.129 (n=591)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.5508 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.496` → IC=+0.232 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.496 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=577)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `10043.6494` → IC=+0.179 (n=188)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 10043.6494 (IC base=+0.131)

### UPDOWN_GBM#5min
- **FILTRO** `sigma_ewma_delta_pct` > `7.938` → IC=-0.198 (n=41)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.938
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=952)

### UPDOWN_GBM#60min
- **FILTRO** `ibs_15` < `0.2426` → IC=-0.143 (n=40)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2426
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=82)

- **FILTRO** `sigma_ewma_delta_pct` > `16.462` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.462
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=79)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.130 (n=71)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=145)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.194 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0034 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.167 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0046 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.189 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.167)

- **PATRÓN** `drift_15min` |x|≤ `0.625` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `drift_15min` |x|≤ 0.625 (IC base=+0.167)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3525` → IC=+0.208 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3525 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.191 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 4.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.167 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.287 (n=106)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.3054` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3054 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.1221` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1221 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.216 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.598` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 18.598 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `14955.5892` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14955.5892 (IC base=+0.167)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` > `0.0048` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=59)

- **FILTRO** `ibs_15` < `0.1693` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1693
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=59)

- **FILTRO** `libro_liquidez` < `13319.0258` → IC=-0.123 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 13319.0258
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=141)

- **FILTRO** `ibs_15` < `0.6608` → IC=-0.189 (n=43)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6608
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=129)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.351` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 20.351 (IC base=+0.003)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.2632` → IC=+0.173 (n=47)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2632 (IC base=+0.093)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2299` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2299 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.6381` → IC=+0.192 (n=141)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.6381 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.1005` → IC=+0.140 (n=98)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1005 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.638` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 14.638 (IC base=+0.093)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=74)

- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=86)

- **FILTRO** `libro_liquidez` < `8064.8076` → IC=-0.123 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 8064.8076
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=51)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `libro_spread` > `0.03` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=163)

- **FILTRO** `drift_15min` |x|> `0.3805` → IC=-0.182 (n=20)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3805
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `ibs_15` > `0.2345` → IC=-0.147 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2345
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.246 (n=61)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.260 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.129 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.109)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1406` → IC=+0.138 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.1406 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.109)

- **PATRÓN** `ibs_15` > `0.94` → IC=+0.420 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.94 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.576` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.576 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=59)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3038.6807` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3038.6807 (IC base=+0.109)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=105)

- **FILTRO** `ibs_15` < `0.4922` → IC=-0.189 (n=43)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4922
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=89)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=66)

- **FILTRO** `sigma_ewma_delta_pct` < `8.524` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.524
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=12)

- **PATRÓN** `dist_vwap_pct` < `0.3805` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3805 (IC base=+0.005)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0501` → IC=+0.158 (n=147)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0501 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.176 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.116)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.191 (n=147)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.5 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.4287` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4287 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.517` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.517 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 32.0 (IC base=+0.116)

- **PATRÓN** `ibs_15` < `0.119` → IC=+0.169 (n=176)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.84€ cuando `ibs_15` < 0.119 (IC base=+0.033)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.326 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.320)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.383 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.320)

- **PATRÓN** `drift_60min` |x|≤ `0.1153` → IC=+0.348 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1153 (IC base=+0.320)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.325 (n=135)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.320)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.338 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.320)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.385 (n=181)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.320)

- **PATRÓN** `dist_vwap_pct` > `0.2966` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2966 (IC base=+0.320)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.538` → IC=+0.332 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.538 (IC base=+0.320)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.888` → IC=+0.330 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.888 (IC base=+0.320)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.326 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.320)

- **PATRÓN** `libro_liquidez` > `8557.9163` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8557.9163 (IC base=+0.320)

- **PATRÓN** `ballena_activa_n` < `522.0` → IC=+0.364 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 522.0 (IC base=+0.320)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.197` → IC=+0.319 (n=103)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.197 (IC base=+0.310)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.309 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.310)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.354 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.310)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.329 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.310)

- **PATRÓN** `drift_15min` |x|≤ `0.4155` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4155 (IC base=+0.310)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1497` → IC=+0.312 (n=78)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1497 (IC base=+0.310)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.340 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.310)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.349 (n=117)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.310)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.509` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.509 (IC base=+0.310)

- **PATRÓN** `libro_liquidez` > `11439.5159` → IC=+0.339 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11439.5159 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `626.0` → IC=+0.415 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 626.0 (IC base=+0.310)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.325 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.328)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.378 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.328)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.367 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.328)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.341 (n=86)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.328)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2105` → IC=+0.333 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2105 (IC base=+0.328)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.332 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.328)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.329 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.328)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.398 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.328)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.328)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.328)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.994` → IC=+0.325 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.994 (IC base=+0.328)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `2812.5928` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2812.5928 (IC base=+0.328)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.011` → IC=-0.210 (n=350)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1052)

- **FILTRO** `ibs_15` < `0.5762` → IC=-0.187 (n=161)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5762
  - _Potencial_: sin este filtro IC_bueno=+0.223 (n=327)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.146 (n=360)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1042)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.174 (n=179)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=-0.069)

- **PATRÓN** `ibs_15` > `0.5762` → IC=+0.223 (n=327)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5762 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1779` → IC=+0.123 (n=221)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1779 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1248` → IC=+0.230 (n=328)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1248 (IC base=-0.061)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1081` → IC=+0.247 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1081 (IC base=-0.061)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.274 (n=493)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` < `0.4505` → IC=+0.222 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4505 (IC base=-0.061)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.226 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=-0.061)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.235 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=700)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.231 (n=307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=625)

- **FILTRO** `sigma_ewma_delta_pct` > `19.475` → IC=-0.247 (n=168)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.475
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=764)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1611` → IC=+0.180 (n=23)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1611 (IC base=+0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1156` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1156 (IC base=+0.022)

- **PATRÓN** `ibs_15` > `0.5837` → IC=+0.274 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5837 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.1823` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1823 (IC base=+0.022)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6371` → IC=-0.256 (n=76)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6371
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=156)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=215)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.209 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.086)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2769` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2769 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.6371` → IC=+0.253 (n=156)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6371 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `10832.5702` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10832.5702 (IC base=+0.086)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.249 (n=241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4431` → IC=+0.220 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4431 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0913` → IC=+0.226 (n=217)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0913 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.288 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.278 (n=241)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.2343` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2343 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.4044` → IC=+0.212 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4044 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.178` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.178 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.415` → IC=+0.230 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.415 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `3621.1646` → IC=+0.212 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3621.1646 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.213 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.212)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.203 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=174)

- **FILTRO** `drift_15min` |x|> `0.8686` → IC=-0.261 (n=86)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8686
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=261)

- **PATRÓN** `ibs_15` > `0.8214` → IC=+0.289 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8214 (IC base=-0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.124` → IC=+0.171 (n=71)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.124 (IC base=-0.045)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.189` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.189 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3926` → IC=+0.225 (n=107)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3926 (IC base=-0.045)

- **PATRÓN** `ibs_15` > `0.0714` → IC=+0.167 (n=97)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` > 0.0714 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` < `0.5028` → IC=+0.193 (n=112)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.5028 (IC base=-0.045)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0175` → IC=-0.257 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0175
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0927` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0927 (IC base=-0.057)

- **PATRÓN** `ibs_15` < `0.3448` → IC=+0.287 (n=125)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3448 (IC base=-0.057)

- **PATRÓN** `ibs_15` > `0.0784` → IC=+0.281 (n=112)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.0784 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `0.5602` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5602 (IC base=-0.057)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.206 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.4465` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4465 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.2576` → IC=+0.208 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2576 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `12949.2689` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12949.2689 (IC base=+0.100)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.206 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.4465` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4465 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.2576` → IC=+0.208 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2576 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `12949.2689` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12949.2689 (IC base=+0.100)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.287 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.292 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.339 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.303 (n=231)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8343` → IC=+0.319 (n=346)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8343 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.3029` → IC=+0.321 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3029 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.732` → IC=+0.285 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.732 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.246` → IC=+0.286 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.246 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.289 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13887.9508` → IC=+0.331 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13887.9508 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.304 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.280 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.0808` → IC=+0.309 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0808 (IC base=+0.280)

- **PATRÓN** `drift_15min` |x|≤ `0.7282` → IC=+0.278 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7282 (IC base=+0.280)

- **PATRÓN** `delta_ratio_macro` |x|> `0.128` → IC=+0.320 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.128 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.280)

- **PATRÓN** `ibs_15` > `0.8592` → IC=+0.308 (n=175)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8592 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.3131` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3131 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.666` → IC=+0.282 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.666 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `11875.3868` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11875.3868 (IC base=+0.280)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.293 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.287 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0682` → IC=+0.341 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0682 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0545` → IC=+0.296 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0545 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.323 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.322 (n=150)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2966` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2966 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` < `0.4822` → IC=+0.288 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4822 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.734` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.734 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.332` → IC=+0.296 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.332 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.302 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `12232.3596` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12232.3596 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `190.0` → IC=+0.292 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 190.0 (IC base=+0.287)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0808` → IC=-0.247 (n=73)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0808
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=142)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.174` → IC=-0.129 (n=60)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.174
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=61)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `drift_60min` |x|> `0.0858` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0858
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.1352` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1352
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9922` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.115)

- **PATRÓN** `T_h` > `145.965` → IC=+0.419 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.965 (IC base=+0.343)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.343)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.973` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.096)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.282)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `59.2591` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 59.2591 (IC base=+0.163)

- **PATRÓN** `ratio` < `0.9624` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9624 (IC base=+0.163)

- **PATRÓN** `T_h` > `87.996` → IC=+0.329 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.996 (IC base=+0.315)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.315)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `127.3918` → IC=+0.425 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 127.3918 (IC base=+0.409)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5904 sube el IC de +0.131 a +0.213 en UPDOWN_GBM#15min (n=562). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.167 a +0.287 en UPDOWN_GBM#BTC#15min (n=106). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6381 sube el IC de +0.093 a +0.192 en UPDOWN_GBM#ETH#15min (n=141). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.94 sube el IC de +0.109 a +0.420 en UPDOWN_GBM#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.116 a +0.191 en UPDOWN_GBM#XRP#15min (n=147). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.119 sube el IC de +0.033 a +0.169 en UPDOWN_GBM#XRP#15min (n=176). Ya aplicado como kelly_boost=+0.84€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5762 sube el IC de -0.069 a +0.223 en UPDOWN_GBM_15M_TARDIO (n=327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.061 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=493). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.5837 sube el IC de +0.022 a +0.274 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6371 sube el IC de +0.086 a +0.253 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=156). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.212 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=241). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8214 sube el IC de -0.130 a +0.289 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3926 sube el IC de -0.045 a +0.225 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=107). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS > 0.0714 sube el IC de -0.045 a +0.167 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=97). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3448 sube el IC de -0.057 a +0.287 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=125). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.0784 sube el IC de -0.057 a +0.281 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=112). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7 (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8343 sube el IC de +0.284 a +0.319 en UPDOWN_GBM_IBS_ALTO (n=346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8592 sube el IC de +0.280 a +0.308 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=175). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.287 a +0.322 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=150). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.320 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=181). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.310 a +0.349 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=117). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.328 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.365 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.365 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP#15min` — IC=+0.150 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `BALLENAS_CONFIRMADAS_15M#XRP` — IC=+0.150 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min` — IC=+0.094 n=30. Faltan ~10 resoluciones para umbral n≥40. ETA: ~7h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC` — IC=+0.094 n=30. Faltan ~10 resoluciones para umbral n≥40. ETA: ~7h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 833 | +0.090 | +56.87€ | 2 | 12 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 833 | +0.090 | +56.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 24 | +0.077 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 24 | +0.077 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 549 | +0.108 | +44.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 549 | +0.108 | +44.31€ | 2 | 12 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 38 | +0.150 | +11.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 38 | +0.150 | +11.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 15339 | -0.115 | -2578.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 973 | -0.013 | -142.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 14366 | -0.122 | -2435.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 2023 | -0.101 | -459.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 2023 | -0.101 | -459.43€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 973 | -0.013 | -142.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 973 | -0.013 | -142.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 2046 | -0.175 | -572.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 2046 | -0.175 | -572.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 4091 | -0.052 | -380.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 4091 | -0.052 | -380.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 3407 | -0.128 | -272.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 3407 | -0.128 | -272.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2799 | -0.193 | -751.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2799 | -0.193 | -751.09€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 4504 | -0.074 | +1912.59€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 1284 | -0.010 | +966.45€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 3220 | -0.100 | +946.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 4504 | -0.074 | +1912.59€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 1284 | -0.010 | +966.45€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 3220 | -0.100 | +946.14€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 96 | -0.031 | -8.28€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 96 | -0.031 | -8.28€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 96 | -0.031 | -8.28€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 96 | -0.031 | -8.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 49193 | +0.114 | -3012.95€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 8196 | +0.184 | -274.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 169 | -0.102 | -52.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 37026 | +0.099 | -2604.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3802 | +0.116 | -81.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 6215 | +0.084 | -799.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 27 | -0.121 | +3.75€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 6173 | +0.086 | -791.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 9847 | +0.131 | -233.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2415 | +0.198 | -118.96€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 6117 | +0.108 | -138.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1273 | +0.124 | +46.01€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 6233 | +0.084 | -762.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 29 | +0.016 | +3.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#240min | 11 | -0.148 | -7.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 6193 | +0.085 | -758.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 10642 | +0.126 | -163.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 3063 | +0.172 | -18.16€ | 1 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 6158 | +0.112 | -90.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1409 | +0.095 | -45.88€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 10043 | +0.124 | -635.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2641 | +0.192 | -146.23€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 83 | -0.006 | -1.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 6199 | +0.095 | -406.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1120 | +0.132 | -81.15€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 6213 | +0.105 | -418.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 21 | -0.022 | +1.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 6 | +0.000 | -0.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 6186 | +0.106 | -419.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 8121 | +0.178 | -627.50€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 8121 | +0.178 | -627.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2072 | +0.165 | -232.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2072 | +0.165 | -232.38€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 149 | -0.136 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 149 | -0.136 | -0.83€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2025 | +0.170 | -211.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2025 | +0.170 | -211.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1816 | +0.237 | -39.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1816 | +0.237 | -39.81€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1980 | +0.183 | -157.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1980 | +0.183 | -157.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 409 | +0.442 | -0.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 409 | +0.442 | -0.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 155 | +0.443 | +1.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 155 | +0.443 | +1.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 157 | +0.437 | -0.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 157 | +0.437 | -0.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 93 | +0.426 | -1.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 93 | +0.426 | -1.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 26288 | +0.189 | -2443.36€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 26288 | +0.189 | -2443.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 4673 | +0.150 | -727.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 4673 | +0.150 | -727.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 4106 | +0.225 | -146.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 4106 | +0.225 | -146.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 4545 | +0.163 | -615.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 4545 | +0.163 | -615.35€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 4190 | +0.218 | -172.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 4190 | +0.218 | -172.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 4350 | +0.199 | -323.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 4350 | +0.199 | -323.40€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 4424 | +0.184 | -458.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 4424 | +0.184 | -458.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 9559 | +0.131 | +334.49€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 9559 | +0.131 | +334.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 4744 | +0.137 | +211.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 4744 | +0.137 | +211.09€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 4815 | +0.126 | +123.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 4815 | +0.126 | +123.40€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 963 | +0.292 | -12.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 963 | +0.292 | -12.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 416 | +0.278 | -12.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 416 | +0.278 | -12.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 455 | +0.294 | +1.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 455 | +0.294 | +1.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 92 | +0.330 | -0.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 92 | +0.330 | -0.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 415 | +0.423 | -10.94€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 415 | +0.423 | -10.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 189 | +0.421 | -5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 189 | +0.421 | -5.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 191 | +0.427 | -4.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 191 | +0.427 | -4.53€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 35 | +0.365 | -0.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 35 | +0.365 | -0.68€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 489 | +0.091 | -7.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 166 | +0.077 | -9.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 323 | +0.097 | +1.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 30 | +0.094 | +0.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 30 | +0.094 | +0.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 385 | +0.102 | +4.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 62 | +0.125 | +2.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 323 | +0.097 | +1.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 74 | +0.026 | -12.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 74 | +0.026 | -12.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 14598 | +0.094 | -559.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1305 | +0.072 | -32.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 13293 | +0.096 | -527.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 8750 | +0.097 | -205.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1305 | +0.072 | -32.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 7445 | +0.101 | -173.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 1876 | +0.116 | +30.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 1876 | +0.116 | +30.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 3972 | +0.078 | -383.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 3972 | +0.078 | -383.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 571 | +0.259 | -70.27€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 571 | +0.259 | -70.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 571 | +0.259 | -70.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 571 | +0.259 | -70.27€ | 0 | 4 |
| ✅ GBM_LATE_15M | 12409 | +0.059 | +5315.03€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 12409 | +0.059 | +5315.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1900 | +0.196 | +1393.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1900 | +0.196 | +1393.95€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 1861 | +0.175 | +1270.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1861 | +0.175 | +1270.46€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 1944 | +0.197 | +1425.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1944 | +0.197 | +1425.88€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 1935 | -0.036 | +123.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1935 | -0.036 | +123.95€ | 3 | 11 |
| ✅ GBM_LATE_15M#SOL | 1993 | -0.049 | +483.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1993 | -0.049 | +483.64€ | 6 | 6 |
| ✅ GBM_LATE_15M#XRP | 2776 | -0.068 | +617.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2776 | -0.068 | +617.14€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 13143 | +0.064 | +6883.36€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 13143 | +0.064 | +6883.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 2286 | -0.002 | +1710.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 2286 | -0.002 | +1710.86€ | 2 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2857 | -0.019 | +435.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2857 | -0.019 | +435.96€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1728 | +0.260 | +1725.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1728 | +0.260 | +1725.61€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1997 | -0.047 | +66.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1997 | -0.047 | +66.01€ | 7 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2180 | -0.011 | +794.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2180 | -0.011 | +794.09€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2095 | +0.266 | +2150.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2095 | +0.266 | +2150.83€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 10213 | +0.169 | +7258.02€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 10213 | +0.169 | +7258.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1447 | +0.201 | +1114.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1447 | +0.201 | +1114.18€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1685 | +0.159 | +1220.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1685 | +0.159 | +1220.90€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1476 | +0.198 | +1117.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1476 | +0.198 | +1117.91€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1678 | +0.141 | +1017.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1678 | +0.141 | +1017.55€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1898 | +0.120 | +1191.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1898 | +0.120 | +1191.04€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2029 | +0.202 | +1596.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2029 | +0.202 | +1596.45€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 2302 | +0.105 | +764.51€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 2302 | +0.105 | +764.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 90 | +0.120 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 90 | +0.120 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 574 | +0.082 | +168.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 574 | +0.082 | +168.73€ | 0 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 328 | +0.145 | +158.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 328 | +0.145 | +158.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 523 | +0.165 | +223.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 523 | +0.165 | +223.84€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 400 | +0.000 | +21.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 400 | +0.000 | +21.82€ | 4 | 4 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 12249 | +0.175 | +8869.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#15min | 12249 | +0.175 | +8869.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1827 | +0.221 | +1545.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1827 | +0.221 | +1545.54€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1996 | +0.161 | +1430.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1996 | +0.161 | +1430.89€ | 0 | 29 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1845 | +0.224 | +1581.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1845 | +0.224 | +1581.64€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1896 | +0.135 | +1136.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1896 | +0.135 | +1136.34€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2155 | +0.105 | +1187.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2155 | +0.105 | +1187.15€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2530 | +0.206 | +1988.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2530 | +0.206 | +1988.16€ | 0 | 22 |
| ✅ GBM_LATE_5M | 3850 | +0.122 | +1775.33€ | 1 | 24 |
| ✅ GBM_LATE_5M#5min | 3850 | +0.122 | +1775.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 235 | +0.171 | +149.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 235 | +0.171 | +149.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1036 | +0.109 | +498.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1036 | +0.109 | +498.21€ | 1 | 16 |
| ✅ GBM_LATE_5M#DOGE | 512 | +0.154 | +287.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 512 | +0.154 | +287.42€ | 0 | 13 |
| ✅ GBM_LATE_5M#ETH | 1318 | +0.141 | +659.19€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1318 | +0.141 | +659.19€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 167 | -0.009 | +4.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 167 | -0.009 | +4.71€ | 2 | 1 |
| ✅ GBM_LATE_5M#XRP | 582 | +0.094 | +175.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 582 | +0.094 | +175.81€ | 0 | 0 |
| ✅ GBM_LATE_60M | 732 | +0.020 | +206.04€ | 3 | 13 |
| ✅ GBM_LATE_60M#60min | 732 | +0.020 | +206.04€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 244 | +0.061 | +57.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 244 | +0.061 | +57.80€ | 2 | 12 |
| ✅ GBM_LATE_60M#ETH | 270 | +0.048 | +106.20€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 270 | +0.048 | +106.20€ | 3 | 13 |
| ✅ GBM_LATE_60M#SOL | 218 | -0.059 | +42.05€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 218 | -0.059 | +42.05€ | 2 | 8 |
| 🚫 GBM_LATE_60M_FADE | 220 | -0.297 | -34.35€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 220 | -0.297 | -34.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 86 | -0.250 | -8.73€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 86 | -0.250 | -8.73€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 72 | -0.351 | -21.15€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 72 | -0.351 | -21.15€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 62 | -0.281 | -4.47€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 62 | -0.281 | -4.47€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 453 | +0.041 | +44.95€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 453 | +0.041 | +44.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 187 | +0.045 | +25.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 187 | +0.045 | +25.52€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 122 | +0.048 | -3.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 122 | +0.048 | -3.59€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 144 | +0.027 | +23.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 144 | +0.027 | +23.02€ | 3 | 3 |
| ✅ LATE_WINDOW_5MIN | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 600 | +0.100 | +144.63€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 600 | +0.100 | +144.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 600 | +0.100 | +144.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 600 | +0.100 | +144.63€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 317 | -0.099 | -37.91€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 317 | -0.099 | -37.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 73 | -0.113 | -10.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 73 | -0.113 | -10.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 97 | -0.025 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 97 | -0.025 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 1260 | -0.009 | -18.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1260 | -0.009 | -18.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 70 | -0.014 | -3.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 70 | -0.014 | -3.67€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 148 | -0.033 | -4.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 148 | -0.033 | -4.86€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 96 | -0.061 | -6.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 96 | -0.061 | -6.98€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 412 | +0.019 | +10.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 412 | +0.019 | +10.58€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 444 | -0.004 | -7.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 444 | -0.004 | -7.56€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 90 | -0.065 | -5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 90 | -0.065 | -5.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 646 | -0.018 | -3.11€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 646 | -0.018 | -3.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 192 | -0.036 | -9.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 192 | -0.036 | -9.23€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 196 | +0.005 | +4.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 196 | +0.005 | +4.34€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 258 | -0.023 | +1.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 258 | -0.023 | +1.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 7615 | -0.003 | -98.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 7615 | -0.003 | -98.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 547 | -0.005 | +2.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 547 | -0.005 | +2.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 752 | -0.016 | -15.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 752 | -0.016 | -15.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1790 | +0.008 | -16.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1790 | +0.008 | -16.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1585 | +0.001 | +1.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1585 | +0.001 | +1.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 1464 | -0.011 | -38.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 1464 | -0.011 | -38.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1477 | -0.006 | -32.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1477 | -0.006 | -32.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 12411 | -0.031 | +606.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 12411 | -0.031 | +606.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 2056 | -0.021 | +314.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 2056 | -0.021 | +314.66€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 2130 | -0.031 | -14.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 2130 | -0.031 | -14.10€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 2079 | -0.030 | +190.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 2079 | -0.030 | +190.56€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 2035 | -0.043 | -34.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 2035 | -0.043 | -34.17€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 2085 | -0.037 | +68.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 2085 | -0.037 | +68.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 2026 | -0.025 | +80.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 2026 | -0.025 | +80.89€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 697 | -0.094 | -49.37€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 697 | -0.094 | -49.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 105 | -0.033 | -4.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 105 | -0.033 | -4.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 115 | -0.141 | -12.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 115 | -0.141 | -12.47€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 150 | -0.165 | -17.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 150 | -0.165 | -17.80€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 190 | -0.062 | -2.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 190 | -0.062 | -2.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1386 | +0.006 | -1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1386 | +0.006 | -1.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 33507 | -0.076 | +646.88€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 33507 | -0.076 | +646.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 5413 | -0.087 | +459.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 5413 | -0.087 | +459.45€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 5516 | -0.078 | -111.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 5516 | -0.078 | -111.77€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 5551 | -0.082 | +166.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 5551 | -0.082 | +166.33€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 5031 | -0.100 | -267.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 5031 | -0.100 | -267.51€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 6285 | -0.053 | +112.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 6285 | -0.053 | +112.76€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 5711 | -0.065 | +287.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 5711 | -0.065 | +287.62€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6242 | -0.013 | -109.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6242 | -0.013 | -109.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 994 | -0.018 | -21.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 994 | -0.018 | -21.35€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1314 | -0.008 | -12.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1314 | -0.008 | -12.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1355 | -0.004 | -9.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1355 | -0.004 | -9.11€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 841 | -0.017 | -12.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 841 | -0.017 | -12.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 735 | +0.115 | +250.45€ | 1 | 6 |
| ✅ ORDER_FLOW_5M#5min | 599 | +0.127 | +237.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 142 | +0.118 | +58.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 142 | +0.118 | +58.54€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 120 | +0.090 | +25.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 120 | +0.090 | +25.09€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 113 | +0.109 | +40.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 113 | +0.109 | +40.23€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 105 | +0.192 | +70.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 105 | +0.192 | +70.55€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 119 | +0.128 | +43.45€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 119 | +0.128 | +43.45€ | 0 | 6 |
| ✅ PRICE_TARGET_GBM | 346 | -0.129 | -14.35€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 152 | -0.201 | -37.26€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 122 | -0.258 | -39.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 30 | +0.031 | +1.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 130 | -0.106 | +2.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 93 | -0.132 | -5.01€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 37 | -0.038 | +7.13€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 64 | +0.000 | +20.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 47 | -0.031 | +13.70€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 17 | +0.067 | +7.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 262 | -0.174 | -30.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 84 | +0.012 | +15.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 367 | -0.213 | -12.47€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 159 | -0.177 | -12.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 135 | -0.164 | -11.63€ | 4 | 2 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 24 | -0.231 | -1.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 133 | -0.263 | -18.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 111 | -0.279 | -22.51€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 22 | -0.167 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 75 | -0.188 | +18.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 62 | -0.188 | +14.99€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 13 | -0.108 | +3.57€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 308 | -0.213 | -19.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 59 | -0.205 | +6.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 107 | +0.362 | +44.37€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#BTC | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 62 | +0.484 | +42.77€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 62 | +0.484 | +42.77€ | 0 | 1 |
| ✅ RESOLUTION_SNIPER#sniper | 107 | +0.362 | +44.37€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 240 | +0.033 | +0.32€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 240 | +0.033 | +0.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 107 | +0.051 | +1.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 107 | +0.051 | +1.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 89 | +0.017 | -0.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 89 | +0.017 | -0.88€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1912 | -0.023 | -83.84€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1912 | -0.023 | -83.84€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 800 | -0.018 | -25.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 800 | -0.018 | -25.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 553 | -0.026 | -25.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 553 | -0.026 | -25.13€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 141 | -0.038 | -12.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 141 | -0.038 | -12.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 418 | -0.024 | -19.83€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 418 | -0.024 | -19.83€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 3977 | +0.022 | +62.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 3977 | +0.022 | +62.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1295 | +0.024 | +14.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1295 | +0.024 | +14.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 804 | +0.043 | +37.21€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 804 | +0.043 | +37.21€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 1175 | +0.011 | -2.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1175 | +0.011 | -2.41€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 703 | +0.015 | +12.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 703 | +0.015 | +12.53€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 4247 | +0.012 | -25.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 4247 | +0.012 | -25.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1634 | +0.011 | -12.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1634 | +0.011 | -12.55€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1688 | +0.021 | +5.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1688 | +0.021 | +5.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 925 | -0.005 | -18.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 925 | -0.005 | -18.70€ | 2 | 0 |
| ✅ UPDOWN_GBM | 10381 | +0.011 | +317.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3643 | +0.040 | +368.26€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 438 | +0.009 | +5.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 5593 | -0.005 | -49.03€ | 1 | 0 |
| ✅ UPDOWN_GBM#60min | 655 | -0.005 | -6.15€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 418 | +0.067 | +48.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 185 | +0.120 | +45.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 10 | -0.042 | -1.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 223 | +0.029 | +3.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1969 | +0.015 | +106.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 427 | +0.066 | +80.30€ | 1 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 131 | +0.049 | +7.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1143 | -0.002 | +17.94€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 248 | +0.004 | -1.58€ | 2 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 20 | -0.136 | +1.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 1179 | +0.004 | +4.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 129 | +0.088 | +27.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 10 | +0.042 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 1040 | -0.008 | -24.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 2141 | +0.001 | +18.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1053 | +0.028 | +44.89€ | 0 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 123 | +0.028 | +7.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 676 | -0.035 | -29.82€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 272 | -0.015 | -4.02€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 17 | -0.157 | +0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 2992 | +0.005 | +14.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 951 | +0.008 | +16.65€ | 1 | 8 |
| ✅ UPDOWN_GBM#SOL#240min | 117 | -0.004 | -2.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1776 | +0.006 | +2.39€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 135 | -0.004 | -0.55€ | 2 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 13 | -0.152 | -0.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1680 | +0.019 | +127.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 898 | +0.051 | +152.52€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 47 | -0.112 | -6.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 735 | -0.011 | -19.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 50 | -0.192 | +0.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 270 | +0.320 | +61.81€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 270 | +0.320 | +61.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 156 | +0.310 | +28.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 156 | +0.310 | +28.08€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 114 | +0.328 | +33.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 114 | +0.328 | +33.73€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 5815 | -0.063 | +1320.11€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 5815 | -0.063 | +1320.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 309 | -0.050 | +341.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 309 | -0.050 | +341.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1200 | -0.150 | -55.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1200 | -0.150 | -55.43€ | 3 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 553 | +0.160 | +269.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 553 | +0.160 | +269.13€ | 2 | 15 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1887 | -0.061 | +384.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1887 | -0.061 | +384.39€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1785 | -0.083 | +371.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1785 | -0.083 | +371.76€ | 1 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 57 | +0.059 | +3.08€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 57 | +0.059 | +3.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 57 | +0.059 | +3.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 57 | +0.059 | +3.08€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 461 | +0.284 | +365.88€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 461 | +0.284 | +365.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 261 | +0.280 | +203.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 261 | +0.280 | +203.83€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 200 | +0.287 | +162.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 200 | +0.287 | +162.06€ | 0 | 14 |
| ✅ UPDOWN_OU_5M | 641 | -0.099 | -73.22€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#5min | 641 | -0.099 | -73.22€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 310 | -0.077 | -35.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 310 | -0.077 | -35.00€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 159 | -0.047 | -8.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 159 | -0.047 | -8.23€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 54 | -0.161 | -8.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 54 | -0.161 | -8.04€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 51 | -0.179 | -7.91€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 51 | -0.179 | -7.91€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1424 | +0.294 | +625.49€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 458 | +0.226 | +22.35€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 472 | +0.276 | +139.65€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 494 | +0.373 | +463.49€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.082) — sin ventaja clara. oversold(IBS<0.3): IC=+0.029 n=3722 | neutral: IC=+0.006 n=4036 | overbought(IBS>0.7): IC=+0.087 n=4039
  - _Datos_: n=12251 IC=+0.042 PNL=+1284.01€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 199 celda(s) pasan gate riguroso completo de 1372 evaluadas (n>=40) y 2496 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.008 < 0.08 — monitorear
  - _Datos_: n=951 IC=+0.008 PNL=+16.65€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=472/15 IC=+0.276 PNL=+139.65€ | BTC: n=458/15 IC=+0.226 PNL=+22.35€ | SOL: n=494/15 IC=+0.373 PNL=+463.49€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 23 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 10319 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.051 n=67/60 | contraria IC=+0.130 n=44 | gap=-0.080 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=152, boost estimado=+0.006. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 105 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=272/40 IC=-0.015 PNL=-4.02€ | BTC#60min: n=248/40 IC=+0.004 PNL=-1.58€ | SOL#60min: n=135/40 IC=-0.004 PNL=-0.55€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.065 n=159165 | tras_1loss IC=+0.052 n=125401 | tras_2loss IC=+0.016 n=56138/40 | gap=+0.049 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.002 n=955 | contrario_BTC IC=-0.008 n=847/40 | gap=-0.006 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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

**🟡 H-24H-GBM-BUYYES-MADRUGADA** — GBM BUY_YES en madrugada europea (05-07h UTC) — señal alcista
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona en horas 05-07h UTC (7-9h Madrid). IC=+0.087 n=14 a las 06h, +0.063 n=11 a las 05h, +0.067 n=17 a las 07h. Hipótesis: apertura europea genera momentum alcista que el GBM captura. La dirección dominante cambia de BUY_NO (madrugada americana 13h) a BUY_YES (apertura europea). Objetivo: cubrir franja horaria 05-07h UTC en el camino hacia operación 24h.
  - _Umbral_: n≥40 en franja 05-07h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → añadir GBM BUY_YES a subtypes_permitidos_live para horas 05-07h UTC
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.188 > 0.08 con n=107 PNL=+67.05€
  - _Datos_: n=107 IC=+0.188 PNL=+67.05€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.08 con n=135 PNL=+54.86€
  - _Datos_: n=135 IC=+0.157 PNL=+54.86€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 24/25 ops en el filtro definido (IC actual=+0.269 PNL=+19.70€)
  - _Datos_: n=24 IC=+0.269 PNL=+19.70€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.336 > 0.1 con n=1202 PNL=+626.80€
  - _Datos_: n=1202 IC=+0.336 PNL=+626.80€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=87 IC=+0.039 PNL=+13.95€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=87 IC=+0.039 PNL=+13.95€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=30 IC=+0.219 PNL=+23.04€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=30 IC=+0.219 PNL=+23.04€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=10104 IC=+0.008 PNL=+264.16€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=10104 IC=+0.008 PNL=+264.16€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 2/15 ops en el filtro definido (IC actual=+0.025 PNL=+3.18€)
  - _Datos_: n=2 IC=+0.025 PNL=+3.18€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=519 IC=+0.001 PNL=-3.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=519 IC=+0.001 PNL=-3.52€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=136 IC=-0.029 PNL=-2.63€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=136 IC=-0.029 PNL=-2.63€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=185 IC=-0.035 PNL=+2.91€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=185 IC=-0.035 PNL=+2.91€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.1 con n=749 PNL=+245.11€
  - _Datos_: n=749 IC=+0.131 PNL=+245.11€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=194 IC=+0.076 PNL=+41.53€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=194 IC=+0.076 PNL=+41.53€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=427 IC=+0.066 PNL=+80.30€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=427 IC=+0.066 PNL=+80.30€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=2123 IC=+0.035 PNL=+206.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2123 IC=+0.035 PNL=+206.90€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=52 IC=-0.259 PNL=-9.58€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=52 IC=-0.259 PNL=-9.58€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=113 IC=-0.013 PNL=+8.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=113 IC=-0.013 PNL=+8.43€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=155 IC=+0.029 PNL=+9.66€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=155 IC=+0.029 PNL=+9.66€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 11/15 ops en el filtro definido (IC actual=+0.064 PNL=+1.63€)
  - _Datos_: n=11 IC=+0.064 PNL=+1.63€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2659 IC=-0.016 PNL=-42.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2659 IC=-0.016 PNL=-42.97€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=38 PNL=+9.28€
  - _Datos_: n=38 IC=+0.175 PNL=+9.28€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.217 n=44) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=44 IC=+0.217 PNL=+18.24€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=2702 IC=+0.017 PNL=+117.91€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2702 IC=+0.017 PNL=+117.91€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=746 IC=+0.031 PNL=+18.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=746 IC=+0.031 PNL=+18.41€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=216 PNL=+64.27€
  - _Datos_: n=216 IC=+0.115 PNL=+64.27€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=188 PNL=+16.65€
  - _Datos_: n=188 IC=+0.111 PNL=+16.65€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.08 con n=169 PNL=+57.77€
  - _Datos_: n=169 IC=+0.132 PNL=+57.77€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=27110 IC=+0.102 PNL=+8520.42€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=27110 IC=+0.102 PNL=+8520.42€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=1792 IC=+0.109 PNL=+195.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=1792 IC=+0.109 PNL=+195.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=1438 IC=+0.030 PNL=+78.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1438 IC=+0.030 PNL=+78.19€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.02 con n=408 PNL=+152.77€
  - _Datos_: n=408 IC=+0.129 PNL=+152.77€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=127 IC=-0.043 PNL=+34.76€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=127 IC=-0.043 PNL=+34.76€

**〰️ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: n=81 IC=-0.030 PNL=+3.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=81 IC=-0.030 PNL=+3.88€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.445 > 0.1 con n=740 PNL=+659.46€
  - _Datos_: n=740 IC=+0.445 PNL=+659.46€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=2562 IC=+0.032 PNL=+210.80€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=2562 IC=+0.032 PNL=+210.80€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=1118 PNL=+434.56€
  - _Datos_: n=1118 IC=+0.166 PNL=+434.56€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.187 < -0.1 con n=65 PNL=+1.03€
  - _Datos_: n=65 IC=-0.187 PNL=+1.03€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=702 IC=+0.033 PNL=+74.32€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=702 IC=+0.033 PNL=+74.32€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=32 IC=-0.147 PNL=+4.20€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=32 IC=-0.147 PNL=+4.20€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.104 > 0.1 con n=137 PNL=+30.56€
  - _Datos_: n=137 IC=+0.104 PNL=+30.56€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 4/20 ops en el filtro definido (IC actual=-0.067 PNL=-2.04€)
  - _Datos_: n=4 IC=-0.067 PNL=-2.04€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=8052 IC=-0.140 PNL=+455.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8052 IC=-0.140 PNL=+455.88€

**⏳ H-CUSTOM-LATE15-PHOTO-FINISH** — GBM_LATE_15M photo finish — entrar pegado al strike es moneda al aire cobrada como favorito
  - _Hipótesis_: Detectado 2026-07-05 validando contra nuestros datos la única idea aprovechable de un artículo-anuncio de copy-bot: GBM_LATE_15M con |drift_ventana_pct|<0.02 tenía IC=-0.145 n=181 (win 35%, -9.70€), estable en ambas mitades temporales (-0.163/-0.127), monótono con la distancia (0.02-0.05: IC=+0.061; ≥0.05: IC=+0.14..0.19) y consistente en crudo y normalizado por sigma (|d_gbm|<0.1 IC=-0.081 n=244). BTC (IC=-0.163 n=90) y ETH (-0.130 n=79) concentraban el daño; SOL/XRP apenas entran en esa zona. Mecanismo: sin distancia real al strike el resultado es ~50/50 pero py_entrada ya cobra favorito. Filtro GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict el 2026-07-05. Esta hipótesis trackea la zona filtrada: si vuelven a aparecer ops aquí, el filtro se ha roto.
  - _Umbral_: 200
  - _Acción_: Si aparecen ops nuevas en la zona → el filtro está roto, revisar shadow_predict. Si el buffer [0.02,0.05) se vuelve negativo con n≥60 forward → subir el corte a 0.05.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict.py desde 2026-07-05 -- bloquea la generación de la zona que esta hipótesis mide. Se mantiene como vigilancia pasiva (si vuelven a aparecer ops en la zona, el filtro se rompió), no como 'acumulando' (26-Ago)

**⏳ H-CUSTOM-PHOTO-FINISH-SNIPER** — Photo finish sniper — comprar el lado rezagado a 1-3c en los últimos segundos (estilo egig)
  - _Hipótesis_: 2026-07-05: wallet 'egig' verificada on-chain (leaderboard oficial +$41k all-time; flujo 23h: -$729 compras / +$2,140 redeems). Forense de 497 trades: compra a 1-3c (mediana 2c) el lado rezagado a mediana 2s del cierre, exclusivamente en photo finishes (dist spot-strike mediana 0.027%). Mecanismo: el mercado cobra los finales de foto como decididos cuando son ~moneda al aire — es el espejo del filtro photo finish que aplicamos a GBM_LATE el mismo día. Win rate implícito ~6% con breakeven 2% (~3x por ticket). photo_finish_logger.py (screen pfinish) acumula dataset en data/shadow/photo_finish_YYYY-MM-DD.csv: libro del lado rezagado a T-10s + outcome oficial vía outcomePrices. CAVEATS a medir: profundidad real del ask a 1-3c (egig compite por asks rancios), frecuencia del setup, y que nuestro T-10s no es su T-2s.
  - _Umbral_: 200
  - _Acción_: Si EV>2x sostenido con n≥200 → proponer watcher de ejecución dedicado (decisión de Javi: toca dinero real y requiere loop sub-5s). Si win rate ≈ ask (mercado calibrado también aquí) → archivar.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: REFUTADA_28JUL_TRACKING_SEPARADO: ya evaluada a mano 28-Jul con data/shadow/photo_finish_YYYY-MM-DD.csv directo (ver CLAUDE.md punto 13 protocolo arranque / memoria hipotesis_auto.md) -- este filtro genérico busca strategy='PHOTO_FINISH_SNIPER' en results.csv, pero photo_finish_logger.py escribe a un CSV propio con schema distinto y JAMÁS escribe ahí, así que n=0 estructuralmente para siempre por este motor. No repetir la evaluación por aquí; si se reabre, hacerlo contra el CSV propio como el 28-Jul.

**〰️ H-CUSTOM-LATE15-BTC-BUYNO-COINFLIP** — GBM_LATE_15M BTC#BUY_NO es moneda al aire — candidata a quitar del motor estrella
  - _Hipótesis_: Detectado 2026-07-06 desglosando la estrategia que carga el bankroll shadow (GBM_LATE_15M, +364€): por par×dirección, BTC#BUY_NO es la única tupla sin edge — 90/182 (49.5%) PNL=+8.92€, prácticamente coinflip, arrastrando a la baja el IC medio del subtipo. Contraste con las estrellas del mismo motor: SOL#BUY_NO 66.1% (+86.70€), XRP#BUY_YES 67.4% (+80.35€), SOL#BUY_YES 64.4% (+77.08€). ETH#BUY_NO (53.6%) es débil pero positivo; BTC#BUY_YES (57.8%) sí funciona. Hipótesis: el edge de entrada tardía en 15min es fuerte en SOL/XRP, medio en ETH/BTC alcista, y NULO en BTC bajista (BTC es el par más eficiente/arbitrado). Quitar BTC#BUY_NO sube el IC del subtipo sin perder PNL real. NO afecta live (la whitelist live es SOL/XRP BUY_NO + ETH BUY_YES, BTC no está).
  - _Umbral_: n≥150 y IC<+0.03 (n=182 ya disponible al crearla)
  - _Acción_: Si IC<+0.03 con n≥150 → filtro causal skip GBM_LATE_15M BTC#BUY_NO en shadow_predict (deja de diluir el subtipo). Si IC sube >+0.08 → mantener.
  - _Estado_: n=971 IC=+0.139 PNL=+517.17€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=971 IC=+0.139 PNL=+517.17€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.133 > 0.08 con n=711 PNL=+230.75€
  - _Datos_: n=711 IC=+0.133 PNL=+230.75€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=1038 IC=+0.004 PNL=+12.21€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1038 IC=+0.004 PNL=+12.21€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=975 PNL=+588.11€
  - _Datos_: n=975 IC=+0.086 PNL=+588.11€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.08 con n=210 PNL=+80.38€
  - _Datos_: n=210 IC=+0.165 PNL=+80.38€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=888 PNL=-115.31€
  - _Datos_: n=888 IC=-0.238 PNL=-115.31€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=2290 IC=+0.140 PNL=+1344.23€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=2290 IC=+0.140 PNL=+1344.23€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=48 PNL=+14.93€
  - _Datos_: n=48 IC=+0.100 PNL=+14.93€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=979 IC=-0.003 PNL=+111.86€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=979 IC=-0.003 PNL=+111.86€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=883 PNL=+600.18€
  - _Datos_: n=883 IC=+0.184 PNL=+600.18€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1464 IC=-0.058 PNL=+320.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1464 IC=-0.058 PNL=+320.84€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.08 con n=319 PNL=-31.66€
  - _Datos_: n=319 IC=+0.117 PNL=-31.66€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.226 > 0.08 con n=2066 PNL=-218.07€
  - _Datos_: n=2066 IC=+0.226 PNL=-218.07€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 19/40 ops en el filtro definido (IC actual=-0.068 PNL=+3.27€)
  - _Datos_: n=19 IC=-0.068 PNL=+3.27€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=330) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=330 IC=+0.102 PNL=+84.83€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.321 > 0.08 con n=110 PNL=+57.48€
  - _Datos_: n=110 IC=+0.321 PNL=+57.48€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.422 n=292) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=292 IC=+0.422 PNL=+403.70€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=4673 IC=+0.150 PNL=-727.77€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=4673 IC=+0.150 PNL=-727.77€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.250 > 0.1 con n=62 PNL=+44.39€
  - _Datos_: n=62 IC=+0.250 PNL=+44.39€
