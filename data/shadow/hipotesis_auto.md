# Hipótesis automáticas — 2026-09-16 20:24 UTC
_Generado por shadow_postmortem.py sobre 471352 resoluciones (PNL=+50703.41€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=439)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=410)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.248 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.213 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.803` → IC=+0.262 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.803 (IC base=+0.122)

- **PATRÓN** `banda_z` > `10.241` → IC=+0.224 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.241 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.139 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=511)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2807.4678` → IC=+0.132 (n=321)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2807.4678 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=339)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.257 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.217 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.271 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.130)

- **PATRÓN** `banda_z` > `11.377` → IC=+0.250 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.377 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=426)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2641.4924` → IC=+0.133 (n=336)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2641.4924 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 88.0 (IC base=+0.034)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=86)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.250 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.100)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.100)

- **PATRÓN** `banda_z` > `6.169` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 6.169 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `1358.622` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1358.622 (IC base=+0.100)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.174)

- **PATRÓN** `n_total_lado` > `39.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 39.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `2707.1913` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2707.1913 (IC base=+0.174)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `144.29` → IC=-0.252 (n=5825)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.29
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=17477)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `139.07` → IC=-0.277 (n=799)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.07
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=2398)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `486.3` → IC=-0.164 (n=313)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 486.3
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=942)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `135.58` → IC=-0.281 (n=712)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.58
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2136)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.0` → IC=-0.251 (n=1386)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=4158)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `119.88` → IC=-0.362 (n=1120)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.88
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=3362)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.245 (n=257)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=275)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.140 (n=123)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=398)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.146 (n=125)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=396)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.259 (n=131)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=154)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.150 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=209)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.256 (n=80)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.180 (n=48)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=98)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.196 (n=11807)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.69 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=2945)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5280.0735` → IC=+0.169 (n=1876)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 5280.0735 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=9159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=10886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.247 (n=8064)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=5793)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7223.6182` → IC=+0.177 (n=1832)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7223.6182 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.348 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15001.7036` → IC=+0.211 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15001.7036 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=1388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.264 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `13207.9317` → IC=+0.214 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13207.9317 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.183 (n=276)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.62 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=286)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `4641.025` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4641.025 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.185 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.167 (n=574)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.425 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=544)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3855.8996` → IC=+0.155 (n=421)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3855.8996 (IC base=+0.131)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=2367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.328 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=1063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.301 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.246 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `3755.7636` → IC=+0.244 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3755.7636 (IC base=+0.239)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.133 (n=551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 17.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.224 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=464)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `1928.4642` → IC=+0.158 (n=366)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1928.4642 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.081)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.425 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.268 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.180 (n=1124)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.03 (IC base=+0.175)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.172 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 13.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.743` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.743 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.142 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.222 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=328)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **FILTRO** `libro_liquidez` < `11311.3585` → IC=-0.260 (n=144)

  - _Acción_: SKIP cuando `libro_liquidez` < 11311.3585
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=49)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=9285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=8899)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.221 (n=3286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=2211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=2294)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `py_entrada` < `0.775` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.321 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.282)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.287 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.333 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.282)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=2154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=1937)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=2037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.321 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=1891)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.195 (n=1589)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.432 (n=365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `2062.8229` → IC=+0.440 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2062.8229 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.434 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.437 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `12146.257` → IC=+0.444 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12146.257 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.453 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.413 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.398 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.404)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=27522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.238 (n=10446)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4747)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=5062)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.170)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=4903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=4893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.272 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=2653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=5057)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.169)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=1859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.269 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=4546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.255 (n=2309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=4614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=3678)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.250 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.205 (n=4191)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.132 (n=3820)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.07 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.154 (n=3829)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.95 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.137 (n=5654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.3` → IC=+0.154 (n=3833)

  - _Acción_: Kelly boost +0.77€ cuando `lag_apertura_s` < 3.3 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.209 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.129)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.135 (n=1903)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.01 (IC base=+0.129)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.149 (n=2044)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.93 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.146 (n=2795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.129)

- **PATRÓN** `lag_apertura_s` < `4.06` → IC=+0.153 (n=1895)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 4.06 (IC base=+0.129)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=2078)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.126 (n=2547)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.148 (n=1975)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.123 (n=2216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.129 (n=2859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.150 (n=1927)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 2.49 (IC base=+0.119)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.384 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1604.6829` → IC=+0.296 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.6829 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.299 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.272)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.338 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `5065.6943` → IC=+0.294 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5065.6943 (IC base=+0.272)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.328 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1491.7936` → IC=+0.314 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1491.7936 (IC base=+0.290)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.340 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.333)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.359 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.333)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.346 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.370 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.333)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.438 (n=368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.433 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `1860.5823` → IC=+0.438 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.5823 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.438 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.434 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.447 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.434 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `2127.0131` → IC=+0.455 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2127.0131 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.375 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.378)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.298 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.298 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9778` → IC=+0.229 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9778 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.2143` → IC=+0.244 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2143 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.876` → IC=+0.168 (n=2419)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.876 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.6095` → IC=+0.257 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6095 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `1.0679` → IC=+0.245 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0679 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.1746` → IC=+0.192 (n=4289)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1746 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.308` → IC=+0.203 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.308 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `1.9238` → IC=+0.198 (n=2753)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.9238 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.5687` → IC=+0.130 (n=7689)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.5687 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.5753` → IC=+0.185 (n=455)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5753 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.3459` → IC=+0.167 (n=2677)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3459 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.6997` → IC=+0.169 (n=1106)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6997 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.8714` → IC=+0.176 (n=1675)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8714 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1683` → IC=+0.220 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1683 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `1.4672` → IC=+0.197 (n=4182)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4672 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.209 (n=3954)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.059)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.180 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0049 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.185 (n=471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0077 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.186 (n=527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.069` → IC=+0.278 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.069 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.199 (n=184)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.4344` → IC=+0.164 (n=1301)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4344 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.186 (n=1312)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.04 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=941)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1937` → IC=+0.272 (n=701)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1937 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.251 (n=721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.290 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.39` → IC=+0.247 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.39 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0923` → IC=+0.232 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0923 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.272 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.7136` → IC=+0.261 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7136 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1740.63` → IC=+0.252 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1740.63 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.224 (n=940)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.212 (n=356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.239 (n=470)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=1068)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9179` → IC=+0.254 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9179 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1983` → IC=+0.220 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1983 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.845` → IC=+0.234 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.845 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2628` → IC=+0.223 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2628 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.0989` → IC=+0.221 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0989 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4957` → IC=+0.220 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4957 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.368` → IC=+0.222 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.368 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `10984.4814` → IC=+0.223 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10984.4814 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.155 (n=1008)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0049 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.157 (n=383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6717` → IC=+0.172 (n=1146)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6717 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1275` → IC=+0.150 (n=1044)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1275 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.49` → IC=+0.168 (n=194)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.49 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.144 (n=1146)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2085 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.8477` → IC=+0.140 (n=764)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8477 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.182 (n=309)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.153 (n=1037)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `13495.0655` → IC=+0.149 (n=764)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 13495.0655 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `423.0` → IC=+0.145 (n=952)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 423.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.177 (n=1214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0089 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.189 (n=1382)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0058 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=1381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.566` → IC=+0.213 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.566 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.1065` → IC=+0.183 (n=1173)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1065 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.3768` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.3768 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.6649` → IC=+0.182 (n=1292)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.6649 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=1581)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.194 (n=485)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 16.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.222 (n=1189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.216 (n=1067)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.3793` → IC=+0.231 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3793 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.564` → IC=+0.234 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.564 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.388` → IC=+0.217 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.388 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.266 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.8451` → IC=+0.206 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8451 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.3006` → IC=+0.224 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3006 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.227 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1886.9572` → IC=+0.234 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1886.9572 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.224 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1742)

- **PATRÓN** `ibs_20min` > `0.9324` → IC=+0.172 (n=288)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.9324 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.3351` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3351 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` < `0.491` → IC=+0.327 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.491 (IC base=+0.006)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.272` → IC=+0.135 (n=543)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 4.272 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6461` → IC=+0.372 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6461 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.1953` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1953 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.4862` → IC=+0.337 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4862 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1278` → IC=+0.342 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1278 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.343 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 165.0 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.1655` → IC=+0.189 (n=194)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1655 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.8602` → IC=+0.148 (n=382)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8602 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `1.1669` → IC=+0.148 (n=191)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1669 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2684` → IC=+0.233 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2684 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.5087` → IC=+0.186 (n=466)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.5087 (IC base=+0.003)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=250)

- **FILTRO** `ibs_20min` < `0.375` → IC=-0.170 (n=98)

  - _Acción_: SKIP cuando `ibs_20min` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=202)

- **FILTRO** `ibs_20min` > `0.2717` → IC=-0.127 (n=1769)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2717
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=872)

- **FILTRO** `sigma_ewma_delta_pct` > `8.632` → IC=-0.205 (n=290)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.632
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=2351)

- **PATRÓN** `ibs_20min` > `0.7576` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7576 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `1.221` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.221 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.5788` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5788 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `0.7668` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7668 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.8428` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8428 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.5081` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5081 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.329 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7352` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7352 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` < `1.1047` → IC=+0.214 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1047 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.1481` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1481 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.4885` → IC=+0.247 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4885 (IC base=-0.046)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6576` → IC=-0.193 (n=438)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6576
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1317)

- **FILTRO** `ibs_20min` < `0.7921` → IC=-0.140 (n=1316)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7921
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=439)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.201 (n=379)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1376)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.202 (n=665)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1998)

- **PATRÓN** `dist_vwap_pct` > `0.9852` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9852 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` < `0.2585` → IC=+0.302 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2585 (IC base=-0.085)

- **PATRÓN** `volumen_regimen` > `0.6119` → IC=+0.287 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6119 (IC base=-0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.0746` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0746 (IC base=-0.085)

- **PATRÓN** `volumen_spike_ratio` < `2.4964` → IC=+0.273 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4964 (IC base=-0.085)

- **PATRÓN** `volumen_spike_ratio` > `1.5988` → IC=+0.279 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5988 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` > `1.0236` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0236 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` < `0.2666` → IC=+0.245 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2666 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` > `1.0842` → IC=+0.293 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0842 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.1065` → IC=+0.276 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1065 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.224` → IC=+0.262 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.224 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.4747` → IC=+0.243 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4747 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.248 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.175 (n=2616)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0092 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.88` → IC=+0.264 (n=3561)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.88 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0161` → IC=+0.287 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0161 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.527` → IC=+0.144 (n=3710)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.527 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.236 (n=2383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6754 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` < `0.1131` → IC=+0.226 (n=4041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1131 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2478` → IC=+0.257 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2478 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `1.4768` → IC=+0.244 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4768 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.7743` → IC=+0.236 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7743 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.277 (n=3726)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.139 (n=2657)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0085 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.150 (n=7010)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5556 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6847` → IC=+0.246 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6847 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2317` → IC=+0.230 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2317 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.7151` → IC=+0.231 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7151 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.249 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2515` → IC=+0.320 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2515 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.4922` → IC=+0.255 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4922 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `2.37` → IC=+0.254 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.37 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.256 (n=2712)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2298` → IC=-0.141 (n=539)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2298
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=1618)

- **FILTRO** `sigma_ewma_delta_pct` > `4.415` → IC=-0.166 (n=393)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.415
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1313)

- **PATRÓN** `ibs_20min` > `0.8621` → IC=+0.247 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8621 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.295` → IC=+0.149 (n=728)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.295 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.291 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.201 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `2.6489` → IC=+0.196 (n=182)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6489 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8266` → IC=-0.150 (n=587)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8266
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1765)

- **PATRÓN** `dist_vwap_pct` > `0.299` → IC=+0.142 (n=252)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.299 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.131 (n=687)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2036 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` > `0.6498` → IC=+0.138 (n=614)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6498 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.175 (n=124)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.176 (n=223)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.188 (n=219)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 230.0 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.1603` → IC=+0.207 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1603 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `1.0364` → IC=+0.210 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0364 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.0717` → IC=+0.201 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0717 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.212 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.808 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.217 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=-0.000)

- **PATRÓN** `ballena_activa_n` < `243.0` → IC=+0.215 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 243.0 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.266 (n=1112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0966` → IC=+0.248 (n=415)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0966 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.253 (n=463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.534` → IC=+0.273 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.534 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1113` → IC=+0.254 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1113 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8816` → IC=+0.238 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8816 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `3.6393` → IC=+0.250 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6393 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.296 (n=996)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.315 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.3321` → IC=+0.284 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3321 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.795` → IC=+0.296 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.795 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.612` → IC=+0.278 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.612 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.301 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.6326` → IC=+0.285 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6326 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.2358` → IC=+0.279 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2358 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `1877.2368` → IC=+0.302 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.2368 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.271 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.278)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.245` → IC=-0.209 (n=359)

  - _Acción_: SKIP cuando `ibs_20min` < 0.245
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1079)

- **FILTRO** `ibs_20min` > `0.8086` → IC=-0.184 (n=469)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8086
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1410)

- **PATRÓN** `ibs_20min` > `0.806` → IC=+0.146 (n=489)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.806 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.4618` → IC=+0.218 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4618 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` < `0.9674` → IC=+0.214 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9674 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` > `0.6162` → IC=+0.194 (n=299)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.6162 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2663` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2663 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `2.0676` → IC=+0.243 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0676 (IC base=-0.013)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.244 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.1237` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1237 (IC base=-0.019)

- **PATRÓN** `dist_vwap_pct` < `0.2862` → IC=+0.172 (n=251)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2862 (IC base=-0.019)

- **PATRÓN** `volumen_regimen` < `1.1494` → IC=+0.171 (n=241)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1494 (IC base=-0.019)

- **PATRÓN** `volumen_regimen` > `0.7226` → IC=+0.179 (n=216)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.7226 (IC base=-0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` > `2.3824` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3824 (IC base=-0.019)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.243 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=-0.019)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6693` → IC=-0.207 (n=849)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6693
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=850)

- **FILTRO** `ibs_20min` > `0.7115` → IC=-0.234 (n=449)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7115
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1349)

- **FILTRO** `sigma_ewma_delta_pct` > `4.704` → IC=-0.175 (n=420)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.704
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=1378)

- **PATRÓN** `ibs_20min` > `0.6693` → IC=+0.258 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6693 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7667` → IC=+0.342 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7667 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.295 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.7198` → IC=+0.277 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7198 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.280 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4442` → IC=+0.319 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4442 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.321 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.1071` → IC=+0.195 (n=451)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1071 (IC base=+0.004)

- **PATRÓN** `dist_vwap_pct` > `0.5842` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5842 (IC base=+0.004)

- **PATRÓN** `dist_vwap_pct` < `0.1825` → IC=+0.197 (n=338)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.1825 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.7171` → IC=+0.252 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7171 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.188 (n=335)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2188` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2188 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.5876` → IC=+0.210 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5876 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4946` → IC=+0.186 (n=345)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4946 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.228 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0155` → IC=+0.323 (n=705)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0155 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.287 (n=495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` > `0.9024` → IC=+0.346 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9024 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.315 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.300 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `0.8543` → IC=+0.295 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8543 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.304 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `1.5484` → IC=+0.277 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5484 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.207` → IC=+0.277 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.207 (IC base=+0.271)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2590.751` → IC=+0.281 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2590.751 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.326 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.295 (n=777)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.284 (n=582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.3945` → IC=+0.305 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3945 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.5506` → IC=+0.285 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5506 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.44` → IC=+0.291 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.44 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `1.2464` → IC=+0.308 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2464 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.243` → IC=+0.365 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.243 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.5387` → IC=+0.264 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5387 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1688` → IC=+0.270 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1688 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `2350.7328` → IC=+0.274 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2350.7328 (IC base=+0.269)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.175 (n=2068)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0048 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.204 (n=2058)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3345` → IC=+0.172 (n=5433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3345 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=6449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5833` → IC=+0.215 (n=6176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5833 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9483` → IC=+0.222 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9483 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.233` → IC=+0.249 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.233 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2136` → IC=+0.163 (n=4108)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2136 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6204` → IC=+0.160 (n=4107)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6204 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1068` → IC=+0.186 (n=2412)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1068 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5656` → IC=+0.174 (n=2583)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5656 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6656` → IC=+0.168 (n=1956)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.6656 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3822.4537` → IC=+0.170 (n=2058)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3822.4537 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.184 (n=5089)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 122.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.187 (n=4012)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0064 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.203 (n=2004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.199 (n=2889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.462` → IC=+0.228 (n=6011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.462 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.223` → IC=+0.161 (n=4493)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.223 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.24` → IC=+0.195 (n=1037)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.24 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1902` → IC=+0.156 (n=4395)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1902 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6256` → IC=+0.151 (n=4395)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6256 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.228 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5745` → IC=+0.174 (n=2356)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5745 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.283` → IC=+0.174 (n=2427)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.283 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.173 (n=4970)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 123.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.224 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.212 (n=352)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3159` → IC=+0.202 (n=1046)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3159 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.211 (n=513)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.073` → IC=+0.308 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.073 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.240 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.542` → IC=+0.180 (n=952)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.542 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.4266` → IC=+0.180 (n=952)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4266 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.207 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.242 (n=669)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.250 (n=677)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1821` → IC=+0.291 (n=506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1821 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.242 (n=758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0984` → IC=+0.274 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0984 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.124` → IC=+0.253 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.124 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.235 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.266 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4356` → IC=+0.262 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4356 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6638` → IC=+0.240 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6638 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1741.1448` → IC=+0.260 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1741.1448 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.246 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.186 (n=301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.190 (n=813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4289` → IC=+0.223 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4289 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2093` → IC=+0.213 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2093 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.549` → IC=+0.223 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.549 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.175 (n=903)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.2629 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2311` → IC=+0.185 (n=198)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2311 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.199 (n=290)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10070.4177` → IC=+0.178 (n=903)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 10070.4177 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `403.0` → IC=+0.160 (n=725)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 403.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.174 (n=903)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0049 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.059` → IC=+0.196 (n=343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.059 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.161 (n=949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.5312` → IC=+0.190 (n=1026)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5312 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1347` → IC=+0.165 (n=1045)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1347 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.029` → IC=+0.214 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.029 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.160 (n=1026)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2145 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1586` → IC=+0.176 (n=316)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1586 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.158 (n=916)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.160 (n=277)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 228.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.199 (n=1023)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0059 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.196` → IC=+0.200 (n=681)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.196 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.672` → IC=+0.268 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.672 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.2175` → IC=+0.186 (n=980)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2175 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.186 (n=393)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.6731` → IC=+0.192 (n=319)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.6731 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.3436` → IC=+0.196 (n=637)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.3436 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.225 (n=573)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.223 (n=860)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.244 (n=287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.270 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.3448` → IC=+0.252 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3448 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.671` → IC=+0.272 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.671 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.3595` → IC=+0.273 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3595 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.8365` → IC=+0.214 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8365 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `3.5269` → IC=+0.249 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5269 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `1886.9572` → IC=+0.240 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1886.9572 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.218 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.223)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.178 (n=855)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0065 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4208` → IC=+0.168 (n=971)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4208 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.4076` → IC=+0.205 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4076 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1357` → IC=+0.195 (n=630)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1357 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.083` → IC=+0.247 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.083 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.858` → IC=+0.162 (n=648)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.858 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1924` → IC=+0.172 (n=324)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1924 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.208 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1672` → IC=+0.158 (n=834)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1672 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.179 (n=316)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7210.5304` → IC=+0.189 (n=647)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7210.5304 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.167 (n=610)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 120.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.165 (n=1054)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0071 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3796` → IC=+0.147 (n=1054)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3796 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6008` → IC=+0.180 (n=1054)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6008 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.15` → IC=+0.145 (n=1059)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.15 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.937` → IC=+0.189 (n=204)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.937 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.141 (n=703)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8585 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.6106` → IC=+0.133 (n=1054)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6106 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.193 (n=151)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.7931` → IC=+0.139 (n=626)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.7931 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.4806` → IC=+0.141 (n=313)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4806 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.158 (n=478)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.126 (n=868)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 177.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.148 (n=766)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0077 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.195 (n=1160)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0126` → IC=+0.234 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0126 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.458` → IC=+0.251 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.458 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.121 (n=1147)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2203 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.8007` → IC=+0.127 (n=735)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8007 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=1181)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2898.521` → IC=+0.192 (n=520)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2898.521 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.137 (n=835)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 48.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.148 (n=507)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0059 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5492` → IC=+0.209 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5492 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.6856` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.6856 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.135 (n=1070)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.383` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 7.383 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.1973` → IC=+0.125 (n=1154)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.1973 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.179 (n=138)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4623` → IC=+0.140 (n=337)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4623 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.177` → IC=+0.132 (n=457)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.177 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3082.5359` → IC=+0.163 (n=384)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3082.5359 (IC base=+0.114)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0181` → IC=+0.215 (n=725)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0181 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.1678` → IC=+0.212 (n=480)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1678 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=490)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7267` → IC=+0.255 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7267 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.2464` → IC=+0.237 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2464 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.371` → IC=+0.243 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.371 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.207 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2068 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6086` → IC=+0.211 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6086 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.262 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1918` → IC=+0.217 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1918 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.204 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2569.4014` → IC=+0.206 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2569.4014 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.235 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0222` → IC=+0.214 (n=529)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0222 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0909` → IC=+0.213 (n=388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0909 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=530)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.0272` → IC=+0.309 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0272 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.226 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2688` → IC=+0.205 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2688 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.244 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6291` → IC=+0.218 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6291 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.281 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2519` → IC=+0.198 (n=903)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.2519 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4614` → IC=+0.194 (n=1026)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4614 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2541.6579` → IC=+0.215 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2541.6579 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.149 (n=502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0038 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.164 (n=498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0088 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.151 (n=499)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.388` → IC=+0.167 (n=1495)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.388 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.8295` → IC=+0.170 (n=204)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.8295 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.043` → IC=+0.171 (n=521)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.043 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8639` → IC=+0.155 (n=859)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8639 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.167 (n=409)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.147 (n=477)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.5666` → IC=+0.158 (n=477)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5666 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=1659)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8408.3868` → IC=+0.151 (n=678)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8408.3868 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.158 (n=1274)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 156.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.135 (n=1060)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.3392` → IC=+0.128 (n=1398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3392 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=1610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.156 (n=1398)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4872 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2043` → IC=+0.122 (n=1417)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2043 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.996` → IC=+0.137 (n=466)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 5.996 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.2242` → IC=+0.121 (n=1408)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2242 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.1668` → IC=+0.141 (n=405)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1668 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `2.2271` → IC=+0.136 (n=1337)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2271 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.125 (n=630)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 25.0 (IC base=+0.115)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1073` → IC=+0.149 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1073 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.150 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 10.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.2836` → IC=+0.134 (n=337)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.2836 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.3004` → IC=+0.141 (n=104)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3004 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.256` → IC=+0.154 (n=157)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.256 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6971 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `9834.2432` → IC=+0.131 (n=337)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 9834.2432 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 151.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.205 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.148 (n=489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.3419` → IC=+0.201 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3419 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.137 (n=199)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.142` → IC=+0.127 (n=553)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 9.142 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.127 (n=489)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2044 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.0616` → IC=+0.170 (n=222)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0616 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.205 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.4085` → IC=+0.149 (n=479)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4085 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 159.0 (IC base=+0.126)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.260 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.199 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.219 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.241 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.2587` → IC=+0.227 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2587 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.367` → IC=+0.223 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.367 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.116` → IC=+0.228 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.116 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.8293` → IC=+0.201 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8293 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.212 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.247` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.247 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.374` → IC=+0.215 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.374 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.3704` → IC=+0.248 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3704 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `12351.8233` → IC=+0.212 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12351.8233 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.130 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0067 (IC base=+0.107)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.159 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.135 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.3025` → IC=+0.163 (n=271)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.3025 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.407` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.407 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `1.2304` → IC=+0.120 (n=406)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2304 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.1661` → IC=+0.170 (n=95)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1661 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` > `1.8165` → IC=+0.133 (n=257)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.8165 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.175 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.8966` → IC=+0.201 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8966 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.7744` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7744 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.329` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 5.329 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `3054.897` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3054.897 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.136 (n=105)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 21.0 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.4762` → IC=+0.156 (n=315)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4762 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.7177` → IC=+0.145 (n=139)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.7177 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `2.5598` → IC=+0.135 (n=291)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5598 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2922.7252` → IC=+0.135 (n=143)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2922.7252 (IC base=+0.087)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.56 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.8803` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8803 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.1233` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1233 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.177 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.022 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.08` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.08 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.0734` → IC=+0.126 (n=177)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0734 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6508` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6508 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.133 (n=178)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.6702` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.6702 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.0068` → IC=+0.127 (n=124)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.0068 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.196 (n=3547)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0086 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=8187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.214 (n=7820)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.9028` → IC=+0.203 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9028 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.589` → IC=+0.223 (n=3834)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.589 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8829` → IC=+0.168 (n=3507)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8829 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.189 (n=1479)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6361` → IC=+0.184 (n=2484)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6361 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3802.1817` → IC=+0.170 (n=2607)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3802.1817 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.195 (n=5672)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 93.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.196 (n=4802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0067 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4795` → IC=+0.183 (n=7200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4795 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5593` → IC=+0.239 (n=7201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5593 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2337` → IC=+0.162 (n=4587)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2337 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.847` → IC=+0.196 (n=1034)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.847 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.705` → IC=+0.183 (n=6958)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.705 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.159 (n=2193)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7044 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.2052` → IC=+0.158 (n=1660)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.2052 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.247 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.2995` → IC=+0.189 (n=2931)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.2995 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.178 (n=6082)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 125.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.209 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.235 (n=598)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.318 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.891` → IC=+0.313 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.891 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.241 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5559` → IC=+0.183 (n=541)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5559 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.5813` → IC=+0.199 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5813 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.264 (n=688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.265 (n=1031)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.2026` → IC=+0.281 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2026 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.3409` → IC=+0.285 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3409 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.466` → IC=+0.264 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.466 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.299 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6807` → IC=+0.294 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6807 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1592.8005` → IC=+0.270 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.8005 (IC base=+0.256)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.193 (n=415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1834` → IC=+0.155 (n=829)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1834 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3255` → IC=+0.199 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3255 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.3398` → IC=+0.198 (n=475)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3398 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.757` → IC=+0.162 (n=291)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.757 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.367` → IC=+0.154 (n=1106)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.367 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6939` → IC=+0.187 (n=547)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6939 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.154` → IC=+0.179 (n=341)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.154 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1158` → IC=+0.159 (n=1047)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1158 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7514` → IC=+0.157 (n=793)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7514 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `10850.867` → IC=+0.168 (n=1111)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10850.867 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `492.0` → IC=+0.161 (n=1121)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 492.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=1113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.26` → IC=+0.167 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.26 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.171 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.6377` → IC=+0.204 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6377 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.6991` → IC=+0.161 (n=169)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6991 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1302` → IC=+0.163 (n=1028)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1302 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.22` → IC=+0.164 (n=554)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.22 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2003` → IC=+0.161 (n=1113)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2003 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1509` → IC=+0.207 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1509 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4046` → IC=+0.167 (n=1015)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4046 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `371.0` → IC=+0.162 (n=614)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 371.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.226 (n=1242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=1308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.215 (n=1262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.6739` → IC=+0.250 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6739 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.577` → IC=+0.297 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.577 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.2176` → IC=+0.216 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2176 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.9996` → IC=+0.233 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9996 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.236 (n=1194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.233 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.3642` → IC=+0.267 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3642 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.718` → IC=+0.272 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.718 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.298 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.7946` → IC=+0.227 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7946 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.2488` → IC=+0.229 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2488 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `1891.307` → IC=+0.237 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1891.307 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.255 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.231)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.172 (n=584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0039 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4307` → IC=+0.140 (n=1324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4307 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=1390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.7033` → IC=+0.232 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7033 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3525` → IC=+0.182 (n=486)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3525 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.224` → IC=+0.161 (n=562)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.224 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8804` → IC=+0.160 (n=883)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8804 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2746` → IC=+0.223 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2746 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5052` → IC=+0.148 (n=561)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5052 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.4563` → IC=+0.158 (n=425)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4563 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8808.1502` → IC=+0.230 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8808.1502 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.172 (n=400)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 87.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.158 (n=1074)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0076 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.157 (n=1072)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6883` → IC=+0.193 (n=1072)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6883 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2051` → IC=+0.144 (n=1009)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2051 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.012` → IC=+0.198 (n=160)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.012 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.146 (n=472)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6958 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1921` → IC=+0.147 (n=358)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1921 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.266 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5573` → IC=+0.143 (n=441)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5573 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4663` → IC=+0.167 (n=334)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4663 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10929.1174` → IC=+0.194 (n=358)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 10929.1174 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `192.0` → IC=+0.144 (n=995)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 192.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.122 (n=893)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0076 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4673` → IC=+0.182 (n=1340)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.4673 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0029` → IC=+0.193 (n=229)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 1.0029 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.395` → IC=+0.219 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.395 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=932)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2917.745` → IC=+0.244 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2917.745 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.128 (n=1000)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 53.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.169 (n=572)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0062 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.154 (n=434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.148 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.208 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2689` → IC=+0.130 (n=1129)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.2689 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.449` → IC=+0.127 (n=1252)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.449 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.7205` → IC=+0.153 (n=572)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7205 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2225` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2225 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4615` → IC=+0.150 (n=381)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4615 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2904.4304` → IC=+0.164 (n=433)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2904.4304 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0241` → IC=+0.215 (n=615)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0241 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.5135` → IC=+0.245 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5135 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.1869` → IC=+0.235 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1869 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.355` → IC=+0.249 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.355 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2484` → IC=+0.210 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2484 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.627` → IC=+0.210 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.627 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2371` → IC=+0.235 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2371 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.5851` → IC=+0.238 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5851 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2574.954` → IC=+0.211 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2574.954 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.235 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.227 (n=499)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.254 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.2715` → IC=+0.206 (n=1395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2715 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.731` → IC=+0.262 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.731 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.240 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.254 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2322` → IC=+0.194 (n=1157)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2322 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4437` → IC=+0.197 (n=1315)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4437 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2550.1344` → IC=+0.202 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2550.1344 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=2580)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.156 (n=2227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0094 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5272` → IC=+0.156 (n=2531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5272 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.161 (n=879)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9387` → IC=+0.215 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9387 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1884` → IC=+0.157 (n=825)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1884 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.736` → IC=+0.169 (n=816)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.736 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.9082` → IC=+0.152 (n=1027)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9082 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1738` → IC=+0.174 (n=692)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1738 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4626` → IC=+0.162 (n=835)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4626 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.9083` → IC=+0.158 (n=1669)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9083 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8205.7154` → IC=+0.154 (n=1148)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8205.7154 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.189 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0037 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4875` → IC=+0.155 (n=1947)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4875 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.163 (n=650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.161 (n=857)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1814 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.7057` → IC=+0.145 (n=345)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.7057 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.274` → IC=+0.144 (n=1931)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.274 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1144` → IC=+0.144 (n=1626)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1144 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.152 (n=918)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.5724` → IC=+0.140 (n=1927)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5724 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.8251` → IC=+0.146 (n=1285)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8251 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=2580)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7727.9509` → IC=+0.151 (n=1739)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7727.9509 (IC base=+0.136)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.171 (n=281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0034 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0921` → IC=+0.192 (n=105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0921 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.165 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.198 (n=210)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5413 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2308` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2308 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.25` → IC=+0.167 (n=397)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 8.25 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.2448` → IC=+0.161 (n=314)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2448 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.8276` → IC=+0.197 (n=209)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.8276 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2313` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2313 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.210 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.7581` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7581 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `12617.0993` → IC=+0.207 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12617.0993 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.206 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.147 (n=870)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1546` → IC=+0.165 (n=383)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1546 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6117` → IC=+0.145 (n=395)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6117 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.723` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.723 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2277` → IC=+0.135 (n=897)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2277 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.265` → IC=+0.158 (n=849)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.265 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.179 (n=580)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8812 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.163 (n=413)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.5735` → IC=+0.143 (n=867)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5735 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.147 (n=578)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `11358.9394` → IC=+0.150 (n=870)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11358.9394 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `707.0` → IC=+0.138 (n=824)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 707.0 (IC base=+0.135)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.180 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.4174` → IC=+0.173 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4174 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.9934` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9934 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.404` → IC=+0.217 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.404 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.166 (n=621)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.197 (n=282)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.213` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.213 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.1037` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1037 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `3.6446` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6446 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `2463.7708` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2463.7708 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.153 (n=750)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0088 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.150 (n=750)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0045 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5046` → IC=+0.156 (n=750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5046 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.153 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.1834` → IC=+0.157 (n=752)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.1834 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.9678` → IC=+0.175 (n=164)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.9678 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.424` → IC=+0.154 (n=714)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.424 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.676` → IC=+0.153 (n=748)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.676 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.116` → IC=+0.148 (n=660)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.116 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `1.2702` → IC=+0.155 (n=250)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2702 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1777` → IC=+0.161 (n=222)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1777 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.169 (n=246)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=712)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8788.5542` → IC=+0.152 (n=670)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8788.5542 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.162 (n=540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0071 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.512` → IC=+0.180 (n=614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.512 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=429)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.161 (n=614)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.1001 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.174 (n=274)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.4008` → IC=+0.148 (n=631)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.4008 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.985` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 8.985 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.176 (n=205)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6473 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.7288` → IC=+0.153 (n=549)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7288 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.1527` → IC=+0.151 (n=632)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1527 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.175 (n=263)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.162 (n=531)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.4508` → IC=+0.161 (n=603)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4508 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `8178.431` → IC=+0.172 (n=614)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8178.431 (IC base=+0.148)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=137)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=160)

- **PATRÓN** `ibs_20min` > `0.9848` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.9848 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.125` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 7.125 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.156` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.156 (IC base=+0.025)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.128 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` > 0.0114 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.6223` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6223 (IC base=+0.041)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.255 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=289)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=289)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.210 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.171 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.649` → IC=+0.220 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.649 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1307` → IC=+0.173 (n=295)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1307 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.105` → IC=+0.217 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.105 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.0939` → IC=+0.128 (n=576)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0939 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.977` → IC=+0.124 (n=261)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.977 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.468` → IC=+0.160 (n=469)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.468 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.4086` → IC=+0.138 (n=468)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4086 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=466)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.159 (n=250)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.0688` → IC=+0.292 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0688 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` < `0.1599` → IC=+0.123 (n=226)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1599 (IC base=-0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.981` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.981 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0857` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0857 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.6098` → IC=+0.154 (n=154)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.6098 (IC base=-0.022)

- **PATRÓN** `libro_liquidez` > `2977.6678` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2977.6678 (IC base=-0.022)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5881` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5881
  - _Potencial_: sin este filtro IC_bueno=+0.210 (n=198)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.175 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0061 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.5881` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5881 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.535` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 13.535 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `1.2106` → IC=+0.135 (n=198)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2106 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.162 (n=140)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.2582` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2582 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `2.0118` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.0118 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2859.3011` → IC=+0.129 (n=184)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2859.3011 (IC base=+0.108)

- **PATRÓN** `drift_60min` |x|≤ `0.0426` → IC=+0.250 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0426 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.5693` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5693 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.9523` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.9523 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.0764` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0764 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `2.4035` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4035 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `3253.1204` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3253.1204 (IC base=+0.054)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.306 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=90)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.222 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=67)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.179 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.151 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 8.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.649` → IC=+0.247 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.649 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.1208` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1208 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.7962` → IC=+0.169 (n=134)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.7962 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6236` → IC=+0.146 (n=179)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6236 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.3845` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.3845 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=209)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `1101.9191` → IC=+0.189 (n=175)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 1101.9191 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.1021` → IC=+0.158 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1021 (IC base=-0.062)

- **PATRÓN** `ibs_20min` < `0.2452` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2452 (IC base=-0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.303` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.303 (IC base=-0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=-0.062)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.062)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=81)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.079)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.138 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 14.0 (IC base=+0.079)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.198 (n=180)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.6757 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.1731` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1731 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` > `1.0632` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0632 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `2.5485` → IC=+0.154 (n=160)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5485 (IC base=+0.079)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.143 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.006 (IC base=-0.074)

- **PATRÓN** `ibs_20min` < `0.1154` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1154 (IC base=-0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.012` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.012 (IC base=-0.074)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1406` → IC=-0.354 (n=39)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1406
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=124)

- **FILTRO** `dist_vwap_pct` > `0.2306` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2306
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=143)

- **FILTRO** `volumen_spike_ratio` > `1.4324` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=37)

- **FILTRO** `sigma_ewma_delta_pct` > `2.588` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.588
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=32)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=40)

- **FILTRO** `dist_vwap_pct` > `0.2409` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2409
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=42)

- **FILTRO** `sigma_ewma_delta_pct` > `3.572` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.572
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=35)

- **FILTRO** `volumen_regimen` > `0.8664` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8664
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7738` → IC=-0.447 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=33)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

- **FILTRO** `dist_vwap_pct` > `0.1871` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.326 (n=21)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.158 (n=77)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=233)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.151 (n=193)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.75 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.234` → IC=+0.133 (n=205)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.234 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.126` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 6.126 (IC base=+0.045)

- **PATRÓN** `libro_liquidez` > `3925.9695` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3925.9695 (IC base=+0.045)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=81)

- **FILTRO** `ibs_20min` < `0.5548` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5548
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=73)

- **FILTRO** `volumen_regimen` < `0.7777` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7777
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=73)

- **FILTRO** `volumen_spike_ratio` < `1.4652` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4652
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=52)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1435 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.100)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=58)

- **FILTRO** `ibs_20min` < `0.8327` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8327
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=51)

- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=74)

- **PATRÓN** `sigma_h` < `0.0015` → IC=+0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0015 (IC base=+0.064)

- **PATRÓN** `drift_60min` |x|≤ `0.111` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.111 (IC base=+0.064)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.8327` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.8327 (IC base=+0.064)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `1571.5815` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1571.5815 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.020)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.55` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=53)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.167 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3956` → IC=+0.152 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3956 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.167 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 12.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.156 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 18.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.7692 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.5856` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5856 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1961` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1961 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.5494` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5494 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0984` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0984 (IC base=-0.035)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=484)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2833.8623` → IC=+0.161 (n=169)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2833.8623 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2309.0554` → IC=+0.128 (n=554)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2309.0554 (IC base=+0.100)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=484)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2833.8623` → IC=+0.161 (n=169)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2833.8623 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2309.0554` → IC=+0.128 (n=554)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2309.0554 (IC base=+0.100)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=124)

- **FILTRO** `libro_liquidez` < `2415.4574` → IC=-0.284 (n=35)

  - _Acción_: SKIP cuando `libro_liquidez` < 2415.4574
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=105)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=191)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=177)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `libro_liquidez` < `15120.4031` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 15120.4031
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `liq_n` < `7.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `libro_liquidez` < `2892.3985` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2892.3985
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1338)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=49)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=81)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `33209.41` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `liq_usd_total` < 33209.41
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=90)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `569.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 569.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_usd_total` > `59480.98` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `liq_usd_total` > 59480.98 (IC base=+0.022)

- **PATRÓN** `libro_liquidez` > `16811.4722` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 16811.4722 (IC base=+0.022)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=579)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=420)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=76)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=424)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=261)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=261)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.200 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=228)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=160)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=160)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=97)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=74)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=163)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=95)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.123 (n=1053)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5509)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=6408)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=1052)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1368)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.179 (n=2698)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=8181)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.173 (n=2787)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=8573)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.220 (n=441)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=1396)

- **FILTRO** `ibs_20min` < `0.748` → IC=-0.180 (n=457)

  - _Acción_: SKIP cuando `ibs_20min` < 0.748
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1380)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.165 (n=470)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1556)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=1090)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.018)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.203 (n=462)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1423)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.219 (n=478)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1522)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.165 (n=497)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1503)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.201 (n=446)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1367)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.193 (n=497)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1504)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2422)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2462)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=2468)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=294)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.214 (n=61)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=185)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=163)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=629)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=223)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.038)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=7781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=17781)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.283 (n=5989)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=19573)

- **FILTRO** `ibs_7min` < `0.703` → IC=-0.242 (n=6387)

  - _Acción_: SKIP cuando `ibs_7min` < 0.703
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=19175)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.159 (n=8687)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=16875)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.224 (n=7968)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=24034)

- **FILTRO** `ibs_7min` > `0.2963` → IC=-0.177 (n=7989)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2963
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=24013)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=969)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3147)

- **FILTRO** `ibs_7min` < `0.7089` → IC=-0.256 (n=1357)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7089
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2759)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.195 (n=966)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3150)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.150 (n=3724)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1838)

- **FILTRO** `drift_7min_pct` |x|> `0.1368` → IC=-0.133 (n=1389)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1368
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=4173)

- **FILTRO** `ibs_7min` > `0.7992` → IC=-0.206 (n=1390)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7992
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=4172)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=3442)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.257 (n=1045)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3421)

- **FILTRO** `ibs_7min` < `0.7554` → IC=-0.188 (n=1116)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7554
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3350)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.173 (n=1112)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3354)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.256 (n=1064)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3454)

- **FILTRO** `ibs_7min` > `0.2534` → IC=-0.168 (n=1129)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2534
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3389)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.179 (n=1126)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3392)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.182 (n=937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=2915)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.322 (n=928)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2924)

- **FILTRO** `drift_7min_pct` |x|> `0.1811` → IC=-0.132 (n=1309)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1811
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=2543)

- **FILTRO** `ibs_7min` < `0.2031` → IC=-0.274 (n=963)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2031
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=2889)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.221 (n=907)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=2945)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.235 (n=1380)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=4478)

- **FILTRO** `ibs_7min` > `0.2623` → IC=-0.156 (n=1991)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2623
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3867)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=2882)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.253 (n=1025)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3181)

- **FILTRO** `ibs_7min` < `0.7429` → IC=-0.193 (n=1050)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3156)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.183 (n=1038)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3168)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1061)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3239)

- **FILTRO** `ibs_7min` > `0.274` → IC=-0.175 (n=1074)

  - _Acción_: SKIP cuando `ibs_7min` > 0.274
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3226)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.181 (n=1065)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3235)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.256 (n=1099)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3506)

- **FILTRO** `ibs_7min` < `0.7187` → IC=-0.222 (n=1148)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7187
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3457)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.170 (n=1459)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4603)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.282 (n=1052)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3265)

- **FILTRO** `ibs_7min` < `0.7264` → IC=-0.232 (n=1079)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7264
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3238)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.210 (n=1055)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3262)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.207 (n=1353)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=4349)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=961)

- **FILTRO** `libro_liquidez` < `10506.0977` → IC=-0.154 (n=131)

  - _Acción_: SKIP cuando `libro_liquidez` < 10506.0977
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=395)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=313)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=530)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.136 (n=638)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.156 (n=213)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 469.512 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.122 (n=289)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3728.089 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.134 (n=271)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 27.0 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.147 (n=49)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.136)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `libro_spread` < `0.02` → IC=+0.120 (n=106)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.02 (IC base=+0.100)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.178 (n=88)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.101)

- **PATRÓN** `total_vol_5m` < `672.2721` → IC=+0.172 (n=117)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 672.2721 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 80.0 (IC base=+0.101)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.190 (n=114)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.149)

- **PATRÓN** `total_vol_5m` < `7671.127` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 7671.127 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3218.4716` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3218.4716 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 37.0 (IC base=+0.149)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.154 (n=108)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.142 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 13.0 (IC base=+0.114)

- **PATRÓN** `total_vol_5m` < `353208.2` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 353208.2 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.114)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.320 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=193)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.167 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0039 (IC base=-0.125)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `54.5986` → IC=-0.372 (n=45)

  - _Acción_: SKIP cuando `T_h` > 54.5986
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=46)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.124)

- **PATRÓN** `T_h` < `54.5986` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `T_h` < 54.5986 (IC base=-0.124)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.150 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.236 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=75)

- **FILTRO** `T_h` > `71.8388` → IC=-0.195 (n=224)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=76)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.284 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=83)

- **FILTRO** `pct_vs_K` |x|> `4.4208` → IC=-0.452 (n=60)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4208
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=183)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=73)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=65)

- **FILTRO** `pct_vs_K` |x|> `3.0033` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0033
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=59)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.271 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `T_h` < `87.9808` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `T_h` < 87.9808
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

- **FILTRO** `sigma_h` > `0.01` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=64)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.364 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=63)

- **FILTRO** `T_h` > `63.9668` → IC=-0.328 (n=62)

  - _Acción_: SKIP cuando `T_h` > 63.9668
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.271 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

- **FILTRO** `T_h` > `71.8388` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.339 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `T_h` > `87.8036` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `T_h` > 87.8036
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.15` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.15 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.467 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.366)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.467 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.366)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.468 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.366)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.462 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.366)

- **PATRÓN** `edge` > `0.1015` → IC=+0.452 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1015 (IC base=+0.404)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.465 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.404)

- **PATRÓN** `T_h` > `0.8072` → IC=+0.421 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8072 (IC base=+0.404)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.487 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.436 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.404)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.475)

- **PATRÓN** `edge` > `0.2135` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2135 (IC base=+0.477)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.474 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.477)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.464 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.477)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.477)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.480 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.477)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.463 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.477)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.469 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.477)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=130)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=226)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `streak_estiramiento` < 0.4576 (IC base=+0.024)

- **PATRÓN** `streak_estiramiento` < `0.5577` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.5577 (IC base=+0.034)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `1171851.4` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `volumen_racha` > 1171851.4
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=24)

- **PATRÓN** `volumen_racha` < `1171851.4` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_racha` < 1171851.4 (IC base=+0.010)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=82)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=84)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=552)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=558)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=306)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `streak_len` < 4.0 (IC base=+0.029)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=467)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=944)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=556)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=578)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2364)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1211)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1219)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.184 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.004 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.207 (n=500)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.178 (n=485)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0585` → IC=+0.176 (n=1101)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0585 (IC base=+0.175)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.225 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.179 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.175)

- **PATRÓN** `ibs_15` > `0.6216` → IC=+0.246 (n=1101)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6216 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.2646` → IC=+0.170 (n=395)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.2646 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.178 (n=733)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.769` → IC=+0.241 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.769 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2633.3465` → IC=+0.178 (n=984)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2633.3465 (IC base=+0.175)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=373)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.220 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.205 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.268 (n=93)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.194)

- **PATRÓN** `drift_15min` |x|≤ `0.3762` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3762 (IC base=+0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.25` → IC=+0.195 (n=93)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.25 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1506` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1506 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.238 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.78` → IC=+0.264 (n=248)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.78 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.1` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.583` → IC=+0.250 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.583 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `14070.628` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14070.628 (IC base=+0.194)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `20.331` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 20.331 (IC base=-0.004)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.174 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.141 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0048 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.142 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1407` → IC=+0.163 (n=179)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.1407 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2725` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2725 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.161 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.6489` → IC=+0.230 (n=268)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6489 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1433` → IC=+0.165 (n=213)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1433 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.212 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `11704.6865` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11704.6865 (IC base=+0.141)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `4.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `ibs_15` > `0.1983` → IC=-0.250 (n=26)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1983
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=53)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.160 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=154)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.204 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1727` → IC=+0.167 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1727 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.186 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3347` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3347 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.178 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.244 (n=154)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.5519` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.5519 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=127)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3004.2322` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.2322 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 34.0 (IC base=+0.142)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5742` → IC=-0.147 (n=117)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5742
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=608)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=+0.020)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.252 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.198 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.183)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0648` → IC=+0.194 (n=279)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.0648 (IC base=+0.183)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.183)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.274 (n=312)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.1729` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1729 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.496` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.496 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.183 (n=339)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.03 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2813.2668` → IC=+0.245 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2813.2668 (IC base=+0.183)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.178 (n=349)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` < 0.1111 (IC base=+0.048)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.336 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.332)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.376 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.339 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.332)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.344 (n=210)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.332)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2203` → IC=+0.373 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2203 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.348 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.332)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.374 (n=315)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` > `0.4129` → IC=+0.374 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4129 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.333 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.332 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.332)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `3480.6224` → IC=+0.345 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3480.6224 (IC base=+0.332)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1211` → IC=+0.338 (n=78)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1211 (IC base=+0.331)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.329 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.331)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.369 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.342 (n=156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.342 (n=118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.411 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.344 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.366 (n=177)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` > `0.242` → IC=+0.389 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.242 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.597` → IC=+0.345 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.597 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `9173.8264` → IC=+0.342 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9173.8264 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `478.0` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 478.0 (IC base=+0.331)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.361 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.333 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.337 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.349 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.387 (n=139)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.337 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.0995` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0995 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.327 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.346 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `3558.8831` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3558.8831 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0126` → IC=-0.203 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0126
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1621)

- **FILTRO** `ibs_15` < `0.6078` → IC=-0.170 (n=180)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6078
  - _Potencial_: sin este filtro IC_bueno=+0.251 (n=543)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.175 (n=685)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1476)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2875` → IC=+0.224 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2875 (IC base=-0.059)

- **PATRÓN** `ibs_15` > `0.6078` → IC=+0.251 (n=543)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6078 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.175 (n=429)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.266 (IC base=-0.059)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2104` → IC=+0.242 (n=385)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2104 (IC base=-0.045)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1818` → IC=+0.239 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1818 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.356` → IC=+0.280 (n=1156)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.356 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` > `0.6583` → IC=+0.269 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6583 (IC base=-0.045)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.209 (n=325)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=976)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.229 (n=429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=872)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.209 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=470)

- **FILTRO** `sigma_ewma_delta_pct` > `19.873` → IC=-0.244 (n=232)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.873
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1069)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.170 (n=113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0026 (IC base=+0.071)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1156` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1156 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.330 (n=110)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.3434` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3434 (IC base=+0.071)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6537` → IC=-0.222 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6537
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=264)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=335)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.137 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0066 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.160 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.004 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0771` → IC=+0.214 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0771 (IC base=+0.133)

- **PATRÓN** `drift_15min` |x|≤ `0.4625` → IC=+0.147 (n=117)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.4625 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.234 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.252 (n=264)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.863` → IC=+0.138 (n=208)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.863 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=335)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.247 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.3563` → IC=+0.229 (n=430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3563 (IC base=+0.224)

- **PATRÓN** `drift_15min` |x|≤ `0.7675` → IC=+0.229 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7675 (IC base=+0.224)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2` → IC=+0.259 (n=222)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.224)

- **PATRÓN** `ibs_15` < `0.3657` → IC=+0.268 (n=489)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3657 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.3809` → IC=+0.248 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3809 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.263` → IC=+0.230 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.263 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.189` → IC=+0.229 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.189 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3578.3819` → IC=+0.225 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3578.3819 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.224 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.224)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.186 (n=390)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=131)

- **FILTRO** `drift_60min` |x|> `0.1609` → IC=-0.209 (n=177)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1609
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=344)

- **FILTRO** `drift_15min` |x|> `0.8398` → IC=-0.235 (n=130)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8398
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=391)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.150)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0711` → IC=+0.212 (n=210)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0711 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.247 (n=235)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.207 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0192` → IC=-0.257 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0192
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=325)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=474)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1081` → IC=+0.351 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1081 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.306 (n=338)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` > `1.111` → IC=+0.419 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.111 (IC base=-0.045)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.136 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0064 (IC base=+0.098)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.239 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.098)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.098)

- **PATRÓN** `ibs_15` > `0.269` → IC=+0.143 (n=40)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.71€ cuando `ibs_15` > 0.269 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1495` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1495 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.309` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.309 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.098)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.136 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0064 (IC base=+0.098)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.239 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.098)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.098)

- **PATRÓN** `ibs_15` > `0.269` → IC=+0.143 (n=40)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.71€ cuando `ibs_15` > 0.269 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1495` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1495 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.309` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.309 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.098)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.286 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0567` → IC=+0.312 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0567 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.288 (n=357)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.319 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.835` → IC=+0.323 (n=535)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.835 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.326 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.316 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.287 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `12693.7099` → IC=+0.300 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12693.7099 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.293 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.274)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.288 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.314 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.274)

- **PATRÓN** `drift_15min` |x|≤ `0.3849` → IC=+0.284 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3849 (IC base=+0.274)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2454` → IC=+0.284 (n=100)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2454 (IC base=+0.274)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3724` → IC=+0.289 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3724 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.326 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.274)

- **PATRÓN** `ibs_15` > `0.8213` → IC=+0.293 (n=298)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8213 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.2601` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2601 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.336 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `15587.8902` → IC=+0.304 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15587.8902 (IC base=+0.274)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.308 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.303 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.317 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1882` → IC=+0.311 (n=109)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1882 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.340 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.323 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.341 (n=237)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.315 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` < `0.4471` → IC=+0.300 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4471 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.317 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.305 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.298 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.085` → IC=-0.273 (n=64)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.085
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=193)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.253 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=170)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.161 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=322)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2171` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2171
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=66)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2412` → IC=-0.138 (n=67)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2412
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=69)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2179` → IC=-0.155 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2179
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2099` → IC=-0.389 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2099
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `87.9936` → IC=+0.140 (n=198)

  - _Acción_: Kelly boost +0.70€ cuando `T_h` > 87.9936 (IC base=+0.133)

- **PATRÓN** `ratio` < `0.9771` → IC=+0.464 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9771 (IC base=+0.133)

- **PATRÓN** `T_h` > `145.8408` → IC=+0.408 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8408 (IC base=+0.349)

- **PATRÓN** `ratio` > `1.0115` → IC=+0.381 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0115 (IC base=+0.349)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.091)

- **PATRÓN** `T_h` > `87.996` → IC=+0.309 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.996 (IC base=+0.305)

- **PATRÓN** `ratio` > `1.0413` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0413 (IC base=+0.305)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `145.6143` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.6143 (IC base=+0.190)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.392 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.190)

- **PATRÓN** `T_h` > `88.9194` → IC=+0.348 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 88.9194 (IC base=+0.330)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.378 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.330)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.405)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6216 sube el IC de +0.175 a +0.246 en UPDOWN_GBM#15min (n=1101). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.78 sube el IC de +0.194 a +0.264 en UPDOWN_GBM#BTC#15min (n=248). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6489 sube el IC de +0.141 a +0.230 en UPDOWN_GBM#ETH#15min (n=268). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.142 a +0.244 en UPDOWN_GBM#SOL#15min (n=154). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.183 a +0.274 en UPDOWN_GBM#XRP#15min (n=312). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.048 a +0.178 en UPDOWN_GBM#XRP#15min (n=349). Ya aplicado como kelly_boost=+0.89€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6078 sube el IC de -0.059 a +0.251 en UPDOWN_GBM_15M_TARDIO (n=543). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.356 sube el IC de -0.045 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1156). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.071 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=110). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.133 a +0.252 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=264). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3657 sube el IC de +0.224 a +0.268 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=489). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.150 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.042 a +0.247 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=235). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.045 a +0.306 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=338). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.835 sube el IC de +0.285 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=535). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8213 sube el IC de +0.274 a +0.293 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=298). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.296 a +0.341 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=237). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.332 a +0.374 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=315). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.331 a +0.366 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=177). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.329 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=139). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1163 | +0.084 | +141.54€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1163 | +0.084 | +141.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 842 | +0.091 | +119.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 842 | +0.091 | +119.69€ | 3 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 241 | +0.043 | +3.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 241 | +0.043 | +3.10€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 54 | +0.161 | +20.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 54 | +0.161 | +20.25€ | 0 | 5 |
| ✅ BALLENAS_TARDIAS | 20828 | -0.100 | -3017.02€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1255 | -0.046 | -181.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 19573 | -0.104 | -2835.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3197 | -0.114 | -557.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3197 | -0.114 | -557.17€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1255 | -0.046 | -181.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1255 | -0.046 | -181.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5976 | -0.044 | -588.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5976 | -0.044 | -588.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5544 | -0.109 | -475.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5544 | -0.109 | -475.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4482 | -0.167 | -1053.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4482 | -0.167 | -1053.45€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 12619 | -0.041 | +4220.45€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3386 | -0.006 | +1846.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 9233 | -0.053 | +2373.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 12619 | -0.041 | +4220.45€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3386 | -0.006 | +1846.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 9233 | -0.053 | +2373.73€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1053 | -0.106 | -155.59€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 73 | -0.087 | -14.55€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 980 | -0.107 | -141.04€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 601 | -0.085 | -75.08€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 49 | -0.088 | -9.33€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 552 | -0.085 | -65.75€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 295 | -0.150 | -64.00€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 271 | -0.156 | -58.78€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 96 | -0.071 | -16.38€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 96 | -0.071 | -16.38€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 75603 | +0.113 | -3883.86€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 11780 | +0.183 | -355.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 292 | -0.116 | -43.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 58330 | +0.100 | -3367.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5201 | +0.115 | -116.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 9719 | +0.096 | -901.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 38 | -0.150 | -1.48€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 9666 | +0.098 | -888.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 15282 | +0.131 | -312.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3611 | +0.202 | -113.19€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 9663 | +0.110 | -188.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1966 | +0.115 | +12.02€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 9758 | +0.089 | -948.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 45 | -0.053 | -1.73€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 9698 | +0.090 | -935.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 16180 | +0.125 | -297.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4547 | +0.173 | -71.75€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 9751 | +0.108 | -170.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1870 | +0.099 | -47.03€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 14931 | +0.115 | -855.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3501 | +0.186 | -178.07€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 195 | -0.074 | +10.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 9870 | +0.091 | -605.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1365 | +0.136 | -81.89€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 9733 | +0.103 | -568.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 38 | +0.000 | +10.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 9682 | +0.104 | -578.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 11952 | +0.190 | -811.87€ | 3 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 11952 | +0.190 | -811.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2931 | +0.168 | -315.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2931 | +0.168 | -315.83€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 669 | +0.187 | +8.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 669 | +0.187 | +8.51€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2873 | +0.178 | -264.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2873 | +0.178 | -264.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2581 | +0.238 | -75.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2581 | +0.238 | -75.45€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2819 | +0.191 | -178.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2819 | +0.191 | -178.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 552 | +0.431 | -12.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 552 | +0.431 | -12.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 211 | +0.434 | -3.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 211 | +0.434 | -3.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 210 | +0.439 | -0.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 210 | +0.439 | -0.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 123 | +0.404 | -8.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 123 | +0.404 | -8.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 40844 | +0.195 | -3409.02€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 40844 | +0.195 | -3409.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 7112 | +0.170 | -896.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 7112 | +0.170 | -896.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6484 | +0.223 | -240.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6484 | +0.223 | -240.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7076 | +0.169 | -900.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7076 | +0.169 | -900.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6575 | +0.217 | -275.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6575 | +0.217 | -275.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6735 | +0.202 | -459.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6735 | +0.202 | -459.65€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6862 | +0.191 | -635.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6862 | +0.191 | -635.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 15277 | +0.124 | +291.95€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 15277 | +0.124 | +291.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7578 | +0.129 | +204.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7578 | +0.129 | +204.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7699 | +0.119 | +87.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7699 | +0.119 | +87.80€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1253 | +0.286 | -27.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1253 | +0.286 | -27.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 554 | +0.272 | -21.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 554 | +0.272 | -21.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 599 | +0.290 | -5.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 599 | +0.290 | -5.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 100 | +0.333 | -0.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 100 | +0.333 | -0.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 551 | +0.431 | -7.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 551 | +0.431 | -7.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 258 | +0.431 | -3.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 258 | +0.431 | -3.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 254 | +0.434 | -3.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 254 | +0.434 | -3.14€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 39 | +0.378 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 39 | +0.378 | -0.28€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 873 | +0.067 | -48.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 313 | +0.052 | -29.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 560 | +0.075 | -19.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 679 | +0.076 | -23.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 119 | +0.079 | -3.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 560 | +0.075 | -19.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 139 | -0.004 | -29.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 139 | -0.004 | -29.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 27091 | +0.098 | -827.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2277 | +0.093 | +29.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 24814 | +0.099 | -856.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 15429 | +0.102 | -231.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2277 | +0.093 | +29.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 13152 | +0.104 | -261.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4748 | +0.115 | +35.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4748 | +0.115 | +35.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6914 | +0.077 | -630.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6914 | +0.077 | -630.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 726 | +0.249 | -93.57€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 726 | +0.249 | -93.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 726 | +0.249 | -93.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 726 | +0.249 | -93.57€ | 0 | 4 |
| ✅ GBM_LATE_15M | 19995 | +0.075 | +8975.96€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 19995 | +0.075 | +8975.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3280 | +0.194 | +2394.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3280 | +0.194 | +2394.54€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 2951 | +0.173 | +1961.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2951 | +0.173 | +1961.28€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 3421 | +0.195 | +2497.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3421 | +0.195 | +2497.11€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 2984 | +0.004 | +453.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2984 | +0.004 | +453.76€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 2941 | -0.037 | +633.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2941 | -0.037 | +633.55€ | 4 | 11 |
| ✅ GBM_LATE_15M#XRP | 4418 | -0.050 | +1035.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4418 | -0.050 | +1035.73€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 21075 | +0.077 | +10454.65€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 21075 | +0.077 | +10454.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3863 | +0.010 | +1941.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3863 | +0.010 | +1941.01€ | 2 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4449 | +0.006 | +839.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4449 | +0.006 | +839.46€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2985 | +0.255 | +2921.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2985 | +0.255 | +2921.58€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3317 | -0.016 | +415.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3317 | -0.016 | +415.24€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3497 | +0.014 | +1240.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3497 | +0.014 | +1240.35€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2964 | +0.270 | +3097.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2964 | +0.270 | +3097.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 16245 | +0.169 | +11920.95€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 16245 | +0.169 | +11920.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2404 | +0.209 | +1923.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2404 | +0.209 | +1923.89€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2570 | +0.154 | +1848.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2570 | +0.154 | +1848.35€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2506 | +0.205 | +1962.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2506 | +0.205 | +1962.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2699 | +0.141 | +1823.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2699 | +0.141 | +1823.78€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3065 | +0.113 | +1985.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3065 | +0.113 | +1985.11€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3001 | +0.204 | +2377.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3001 | +0.204 | +2377.67€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4109 | +0.125 | +1643.97€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4109 | +0.125 | +1643.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 147 | +0.117 | +60.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 147 | +0.117 | +60.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1100 | +0.115 | +427.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1100 | +0.115 | +427.25€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1142 | +0.150 | +519.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1142 | +0.150 | +519.28€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 849 | +0.086 | +235.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 849 | +0.086 | +235.89€ | 0 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 20024 | +0.173 | +14471.29€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 20024 | +0.173 | +14471.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3131 | +0.221 | +2637.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3131 | +0.221 | +2637.30€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3140 | +0.151 | +2052.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3140 | +0.151 | +2052.85€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3244 | +0.221 | +2736.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3244 | +0.221 | +2736.41€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3194 | +0.137 | +2058.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3194 | +0.137 | +2058.57€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3518 | +0.106 | +2021.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3518 | +0.106 | +2021.08€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3797 | +0.203 | +2965.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3797 | +0.203 | +2965.08€ | 0 | 23 |
| ✅ GBM_LATE_5M | 5969 | +0.141 | +3248.14€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5969 | +0.141 | +3248.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1577 | +0.141 | +974.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1577 | +0.141 | +974.04€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1817 | +0.146 | +985.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1817 | +0.146 | +985.72€ | 0 | 30 |
| ✅ GBM_LATE_5M#SOL | 319 | +0.033 | +42.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 319 | +0.033 | +42.71€ | 2 | 5 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1274 | +0.067 | +535.71€ | 2 | 18 |
| ✅ GBM_LATE_60M#60min | 1274 | +0.067 | +535.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 450 | +0.091 | +176.85€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 450 | +0.091 | +176.85€ | 1 | 16 |
| ✅ GBM_LATE_60M#ETH | 426 | +0.072 | +216.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 426 | +0.072 | +216.06€ | 2 | 17 |
| ✅ GBM_LATE_60M#SOL | 398 | +0.033 | +142.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 398 | +0.033 | +142.80€ | 1 | 11 |
| 🚫 GBM_LATE_60M_FADE | 303 | -0.267 | -23.86€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 303 | -0.267 | -23.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 113 | -0.222 | -7.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 113 | -0.222 | -7.68€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 103 | -0.300 | -13.97€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 103 | -0.300 | -13.97€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 87 | -0.275 | -2.21€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 87 | -0.275 | -2.21€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 598 | +0.055 | +115.10€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 598 | +0.055 | +115.10€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 240 | +0.045 | +38.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 240 | +0.045 | +38.86€ | 4 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 174 | +0.040 | +7.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 174 | +0.040 | +7.11€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 184 | +0.081 | +69.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 184 | +0.081 | +69.13€ | 2 | 13 |
| ✅ LATE_WINDOW_5MIN | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1411 | +0.105 | +408.91€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1411 | +0.105 | +408.91€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1411 | +0.105 | +408.91€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1411 | +0.105 | +408.91€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 352 | -0.085 | -34.51€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 352 | -0.085 | -34.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 87 | -0.084 | -7.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 87 | -0.084 | -7.38€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 118 | -0.017 | -3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 118 | -0.017 | -3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1536 | -0.005 | -8.85€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1536 | -0.005 | -8.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 168 | -0.018 | +2.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 168 | -0.018 | +2.40€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 626 | +0.021 | +14.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 626 | +0.021 | +14.72€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 460 | -0.006 | -8.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 460 | -0.006 | -8.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 105 | -0.061 | -6.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 105 | -0.061 | -6.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 908 | -0.048 | -28.49€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 908 | -0.048 | -28.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 264 | -0.053 | -14.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 264 | -0.053 | -14.59€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 290 | -0.038 | -5.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 290 | -0.038 | -5.01€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 354 | -0.053 | -8.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 354 | -0.053 | -8.89€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 13211 | -0.012 | -188.16€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 13211 | -0.012 | -188.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2439 | -0.024 | -52.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2439 | -0.024 | -52.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2708 | -0.016 | -22.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2708 | -0.016 | -22.04€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3246 | -0.018 | -62.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3246 | -0.018 | -62.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 22239 | -0.012 | +962.59€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 22239 | -0.012 | +962.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3863 | +0.010 | +496.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3863 | +0.010 | +496.00€ | 3 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3593 | -0.026 | -29.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3593 | -0.026 | -29.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3885 | +0.004 | +307.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3885 | +0.004 | +307.60€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3365 | -0.046 | -99.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3365 | -0.046 | -99.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3719 | -0.016 | +154.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3719 | -0.016 | +154.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3814 | -0.001 | +133.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3814 | -0.001 | +133.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4985 | -0.040 | -116.88€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4985 | -0.040 | -116.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1076 | -0.048 | -23.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1076 | -0.048 | -23.12€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 459 | -0.120 | -19.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 459 | -0.120 | -19.93€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1361 | -0.055 | -26.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1361 | -0.055 | -26.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3339 | +0.004 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3339 | +0.004 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 186 | +0.011 | -0.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 186 | +0.011 | -0.87€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1314 | +0.007 | +7.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1314 | +0.007 | +7.09€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 57564 | -0.073 | +1143.25€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 57564 | -0.073 | +1143.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 9678 | -0.081 | +559.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 9678 | -0.081 | +559.94€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 8984 | -0.089 | -339.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 8984 | -0.089 | -339.08€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 9710 | -0.071 | +461.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 9710 | -0.071 | +461.01€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8506 | -0.092 | -227.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8506 | -0.092 | -227.76€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 10667 | -0.048 | +331.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 10667 | -0.048 | +331.40€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 10019 | -0.064 | +357.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 10019 | -0.064 | +357.74€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6730 | -0.021 | -104.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6730 | -0.021 | -104.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1502 | -0.021 | -9.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1502 | -0.021 | -9.24€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1493 | -0.015 | -5.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1493 | -0.015 | -5.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1000 | -0.037 | -14.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1000 | -0.037 | -14.73€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 986 | +0.112 | +342.87€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 850 | +0.121 | +330.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 193 | +0.136 | +94.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 193 | +0.136 | +94.29€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 168 | +0.100 | +42.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 168 | +0.100 | +42.71€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 176 | +0.101 | +60.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 176 | +0.101 | +60.28€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 152 | +0.149 | +79.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 152 | +0.149 | +79.43€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 161 | +0.114 | +53.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 161 | +0.114 | +53.58€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 469 | -0.077 | -5.10€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 207 | -0.122 | -32.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 165 | -0.159 | -35.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 167 | -0.068 | +8.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 125 | -0.075 | +1.91€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 95 | +0.005 | +19.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 75 | -0.006 | +13.09€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 365 | -0.100 | -20.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 543 | -0.221 | -44.40€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 227 | -0.203 | -33.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 195 | -0.195 | -31.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 191 | -0.241 | -22.27€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 164 | -0.253 | -26.35€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 125 | -0.216 | +11.61€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 111 | -0.217 | +8.55€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 470 | -0.223 | -49.26€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 198 | +0.395 | +144.37€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 48 | +0.360 | +39.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 48 | +0.360 | +39.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 122 | +0.484 | +109.19€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 122 | +0.484 | +109.19€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#sniper | 198 | +0.395 | +144.37€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 394 | +0.030 | +10.41€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 394 | +0.030 | +10.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 175 | +0.025 | +0.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 175 | +0.025 | +0.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 45 | -0.011 | -3.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 45 | -0.011 | -3.64€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 149 | +0.036 | +9.81€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 149 | +0.036 | +9.81€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 2437 | -0.026 | -110.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2437 | -0.026 | -110.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 562 | -0.023 | -23.39€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 562 | -0.023 | -23.39€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 153 | -0.042 | -13.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 153 | -0.042 | -13.91€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 918 | -0.030 | -45.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 918 | -0.030 | -45.79€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 58 | -0.033 | -2.61€ | 2 | 1 |
| ✅ STREAK_FADE_60M#60min | 58 | -0.033 | -2.61€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 23 | +0.060 | +1.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 23 | +0.060 | +1.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6523 | +0.021 | +83.59€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6523 | +0.021 | +83.59€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2087 | +0.021 | +20.21€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2087 | +0.021 | +20.21€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1363 | +0.028 | +32.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1363 | +0.028 | +32.69€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1897 | +0.012 | +1.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1897 | +0.012 | +1.52€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1176 | +0.027 | +29.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1176 | +0.027 | +29.16€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6006 | +0.011 | -38.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6006 | +0.011 | -38.76€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2383 | +0.018 | -1.59€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2383 | +0.018 | -1.59€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2380 | +0.013 | -11.73€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2380 | +0.013 | -11.73€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1243 | -0.005 | -25.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1243 | -0.005 | -25.44€ | 2 | 0 |
| ✅ UPDOWN_GBM | 25907 | +0.029 | +1440.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 6943 | +0.059 | +1113.18€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 977 | +0.005 | +8.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 16312 | +0.023 | +321.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1569 | -0.002 | -5.00€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2262 | +0.071 | +218.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 277 | +0.127 | +90.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1966 | +0.064 | +129.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4666 | +0.031 | +305.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 849 | +0.081 | +192.81€ | 0 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 277 | +0.023 | +7.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2807 | +0.027 | +99.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 693 | -0.001 | +5.28€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 40 | -0.119 | +1.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3047 | +0.032 | +98.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 235 | +0.112 | +59.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2796 | +0.025 | +38.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 5319 | +0.016 | +214.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1910 | +0.045 | +213.31€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 264 | +0.007 | +8.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2549 | +0.002 | -4.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 561 | -0.006 | -7.18€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 35 | -0.149 | +3.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6703 | +0.017 | +160.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1862 | +0.024 | +110.14€ | 1 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 258 | -0.008 | -2.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4239 | +0.018 | +56.63€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 315 | +0.002 | -3.11€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 29 | -0.145 | -0.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3908 | +0.042 | +445.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1810 | +0.080 | +447.36€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 143 | -0.010 | -3.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1955 | +0.011 | +1.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 104 | -0.141 | +4.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 420 | +0.332 | +116.37€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 420 | +0.332 | +116.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 235 | +0.331 | +59.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 235 | +0.331 | +59.31€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 185 | +0.329 | +57.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 185 | +0.329 | +57.06€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 9136 | -0.048 | +1947.85€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 9136 | -0.048 | +1947.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 411 | -0.054 | +343.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 411 | -0.054 | +343.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1751 | -0.129 | +32.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1751 | -0.129 | +32.51€ | 4 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 144 | +0.123 | +60.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 144 | +0.123 | +60.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1003 | +0.193 | +561.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1003 | +0.193 | +561.77€ | 2 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2923 | -0.062 | +460.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2923 | -0.062 | +460.96€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2904 | -0.076 | +488.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2904 | -0.076 | +488.96€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 102 | +0.067 | +14.80€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 102 | +0.067 | +14.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 102 | +0.067 | +14.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 102 | +0.067 | +14.80€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 713 | +0.285 | +571.54€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 713 | +0.285 | +571.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 397 | +0.274 | +298.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 397 | +0.274 | +298.08€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 316 | +0.296 | +273.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 316 | +0.296 | +273.47€ | 0 | 12 |
| ✅ UPDOWN_OU_5M | 686 | -0.109 | -80.31€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 686 | -0.109 | -80.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 184 | -0.070 | -12.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 184 | -0.070 | -12.11€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 66 | -0.176 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 66 | -0.176 | -10.12€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1949 | +0.304 | +1002.88€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 650 | +0.248 | +104.58€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 700 | +0.293 | +287.86€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 599 | +0.375 | +610.45€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.016 n=372 — no justifica filtro, seguir monitorizando
  - _Datos_: n=372 IC=+0.016 PNL=+18.02€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 456 celda(s) pasan gate riguroso completo de 2050 evaluadas (n>=40) y 3017 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.025 < 0.08 — monitorear
  - _Datos_: n=1857 IC=+0.025 PNL=+108.70€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=700/15 IC=+0.293 PNL=+287.86€ | BTC: n=650/15 IC=+0.248 PNL=+104.58€ | SOL: n=599/15 IC=+0.375 PNL=+610.45€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 29 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: 40
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Solo 0 ops con ibs_15 (feature añadida 2026-06-27). Esperar n≥40.

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: 20
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: Solo 0 ops GBM con hora_utc en features. Esperar n≥20 para patrones.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.093 n=187/60 | contraria IC=+0.129 n=165 | gap=-0.036 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=245, boost estimado=+0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=560/40 IC=-0.007 PNL=-7.72€ | BTC#60min: n=691/40 IC=-0.001 PNL=+4.65€ | SOL#60min: n=314/40 IC=+0.000 PNL=-3.61€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.053 n=264089 | tras_1loss IC=+0.072 n=206499 | tras_2loss IC=+0.040 n=88377/40 | gap=+0.013 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.000 n=0 | contrario_BTC IC=+0.000 n=0/40 | gap=+0.000 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.08 con n=205 PNL=+146.10€
  - _Datos_: n=205 IC=+0.196 PNL=+146.10€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.192 > 0.08 con n=274 PNL=+169.13€
  - _Datos_: n=274 IC=+0.192 PNL=+169.13€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.235 > 0.08 con n=32 PNL=+22.88€
  - _Datos_: n=32 IC=+0.235 PNL=+22.88€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.344 > 0.1 con n=1630 PNL=+995.44€
  - _Datos_: n=1630 IC=+0.344 PNL=+995.44€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=201 IC=+0.076 PNL=+26.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=201 IC=+0.076 PNL=+26.64€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=45 IC=+0.202 PNL=+32.49€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=45 IC=+0.202 PNL=+32.49€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=1139 IC=-0.005 PNL=-15.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1139 IC=-0.005 PNL=-15.38€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=426 IC=+0.002 PNL=+8.70€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=426 IC=+0.002 PNL=+8.70€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=372 IC=+0.016 PNL=+18.02€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=372 IC=+0.016 PNL=+18.02€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.173 > 0.1 con n=1459 PNL=+824.84€
  - _Datos_: n=1459 IC=+0.173 PNL=+824.84€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=846 IC=+0.080 PNL=+189.69€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=846 IC=+0.080 PNL=+189.69€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**⏳ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: 40
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=393 IC=+0.014 PNL=+27.75€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=393 IC=+0.014 PNL=+27.75€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=29 IC=+0.048 PNL=+0.86€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=29 IC=+0.048 PNL=+0.86€

**⏳ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: 40
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: 30
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.257 n=68) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=68 IC=+0.257 PNL=+46.86€

**⏳ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: 40
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: 40
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: 200
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: 100
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: 40
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.02 con n=567 PNL=+230.73€
  - _Datos_: n=567 IC=+0.129 PNL=+230.73€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=140 IC=-0.056 PNL=+31.39€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=140 IC=-0.056 PNL=+31.39€

**⏳ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=8409 IC=+0.048 PNL=+940.17€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=8409 IC=+0.048 PNL=+940.17€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.161 < -0.1 con n=160 PNL=+11.60€
  - _Datos_: n=160 IC=-0.161 PNL=+11.60€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1393 IC=+0.049 PNL=+165.31€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1393 IC=+0.049 PNL=+165.31€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=56 IC=-0.086 PNL=+7.93€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=56 IC=-0.086 PNL=+7.93€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.138 > 0.1 con n=266 PNL=+83.65€
  - _Datos_: n=266 IC=+0.138 PNL=+83.65€

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
  - _Estado_: n=13786 IC=-0.144 PNL=+594.21€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13786 IC=-0.144 PNL=+594.21€

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
  - _Estado_: n=1526 IC=+0.137 PNL=+794.77€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1526 IC=+0.137 PNL=+794.77€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2669 IC=+0.016 PNL=+74.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2669 IC=+0.016 PNL=+74.27€

**〰️ H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: n=1597 IC=+0.079 PNL=+804.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1597 IC=+0.079 PNL=+804.82€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.244 < -0.1 con n=1390 PNL=-203.87€
  - _Datos_: n=1390 IC=-0.244 PNL=-203.87€

**⏳ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: 100
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: 40
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: 40
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 29/40 ops en el filtro definido (IC actual=-0.016 PNL=+5.59€)
  - _Datos_: n=29 IC=-0.016 PNL=+5.59€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.100 n=738) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=738 IC=+0.100 PNL=+196.85€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=389) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=389 IC=+0.413 PNL=+545.43€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=7105 IC=+0.170 PNL=-897.69€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=7105 IC=+0.170 PNL=-897.69€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.222 > 0.1 con n=106 PNL=+69.69€
  - _Datos_: n=106 IC=+0.222 PNL=+69.69€
