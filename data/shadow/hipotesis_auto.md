# Hipótesis automáticas — 2026-09-16 01:47 UTC
_Generado por shadow_postmortem.py sobre 459686 resoluciones (PNL=+49384.65€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.249 (n=432)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=409)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.249 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `77.0` → IC=+0.208 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 77.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.8036` → IC=+0.259 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8036 (IC base=+0.121)

- **PATRÓN** `banda_z` > `10.308` → IC=+0.221 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.308 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.138 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=505)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2783.5427` → IC=+0.130 (n=317)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2783.5427 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.120 (n=409)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.037)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=332)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.258 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.129)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.213 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.129)

- **PATRÓN** `banda_hit_calibrado` > `0.7988` → IC=+0.271 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7988 (IC base=+0.129)

- **PATRÓN** `banda_z` > `11.425` → IC=+0.246 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.425 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=420)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2596.553` → IC=+0.131 (n=331)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2596.553 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 88.0 (IC base=+0.034)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=86)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=86)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=85)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=96)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=-0.018)

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
- **FILTRO** `restante_s_al_confirmar` < `145.94` → IC=-0.254 (n=5714)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.94
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=17148)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `139.02` → IC=-0.288 (n=786)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.02
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=2359)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `485.84` → IC=-0.162 (n=309)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 485.84
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=929)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `136.32` → IC=-0.280 (n=710)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.32
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2130)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `141.37` → IC=-0.151 (n=1472)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.37
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=4416)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.32` → IC=-0.252 (n=1351)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.32
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=4056)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.39` → IC=-0.329 (n=1433)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.39
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=2911)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.241 (n=230)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=247)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.294 (n=61)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=197)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.51` → IC=-0.253 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.51
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=30)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=61)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=65)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.195 (n=11597)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.69 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=2887)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5249.0643` → IC=+0.167 (n=1842)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5249.0643 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=9030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=10625)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.246 (n=7891)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=5704)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7178.5823` → IC=+0.178 (n=1803)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7178.5823 (IC base=+0.136)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.347 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `11012.9062` → IC=+0.200 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11012.9062 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=1355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.273 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `14404.1026` → IC=+0.212 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14404.1026 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.179 (n=272)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.62 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=286)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `4643.6334` → IC=+0.147 (n=230)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4643.6334 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.168 (n=564)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` < 0.425 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=542)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `3846.6396` → IC=+0.158 (n=419)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3846.6396 (IC base=+0.134)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=1976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.327 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.301 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.244 (n=1212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `3129.4031` → IC=+0.241 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3129.4031 (IC base=+0.239)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.134 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.132 (n=542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 17.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.221 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=633)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `1940.1614` → IC=+0.160 (n=360)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1940.1614 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.082)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.219 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=1073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.423 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.268 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.180 (n=1112)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.03 (IC base=+0.175)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.170 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 13.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.338 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3418.4493` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3418.4493 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.232 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=326)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.127)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=9069)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=8672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.219 (n=3219)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `5296.2198` → IC=+0.343 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5296.2198 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=2162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.180 (n=2251)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.169)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.316 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.283)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.283 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.343 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.283)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=2234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.180 (n=2129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=1904)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.321 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.236)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=2162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=1849)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.194 (n=1552)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.438 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.433 (n=372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `2048.1399` → IC=+0.444 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.1399 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.437 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.443 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.454 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `11846.5589` → IC=+0.452 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11846.5589 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.452 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.463 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.441 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `3923.6329` → IC=+0.444 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3923.6329 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.412 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.403)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.403)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=26898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.237 (n=10235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=5486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.175 (n=4624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=4934)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.169)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=4785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=4757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.271 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=4905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4941)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.169)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=4448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.255 (n=2252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=4510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=3585)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.248 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=4092)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.132 (n=3731)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.07 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.146 (n=4198)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.94 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.136 (n=5510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 8.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.150 (n=3735)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.31 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.130)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.135 (n=1857)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.01 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.146 (n=1991)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.93 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.146 (n=2724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `4.08` → IC=+0.150 (n=1851)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 4.08 (IC base=+0.130)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=2031)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.125 (n=2491)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.48 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.146 (n=1910)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.127 (n=2786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `4.36` → IC=+0.144 (n=2481)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 4.36 (IC base=+0.119)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1614.3793` → IC=+0.297 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1614.3793 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.300 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.273)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.337 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `5072.5083` → IC=+0.291 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5072.5083 (IC base=+0.273)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.328 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.291 (n=444)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.382 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1493.0973` → IC=+0.314 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1493.0973 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.338 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.332)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.359 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.332)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.375 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.332)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.370 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.332)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.437 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.432 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `1860.5823` → IC=+0.438 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.5823 (IC base=+0.430)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.433 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.430)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.447 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.434 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `2131.4162` → IC=+0.455 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2131.4162 (IC base=+0.433)

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
- **PATRÓN** `ibs_20min` > `0.9778` → IC=+0.231 (n=2034)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9778 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.1524` → IC=+0.242 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1524 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.716` → IC=+0.154 (n=3334)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.716 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6095` → IC=+0.254 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6095 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.0652` → IC=+0.242 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0652 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.0812` → IC=+0.192 (n=3609)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0812 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.3097` → IC=+0.202 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3097 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.9334` → IC=+0.198 (n=2666)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.9334 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.5687` → IC=+0.130 (n=7494)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.5687 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.5905` → IC=+0.181 (n=443)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.5905 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.3518` → IC=+0.168 (n=2575)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3518 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.170 (n=1068)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6973 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.8691` → IC=+0.173 (n=1617)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8691 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2462` → IC=+0.222 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2462 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `1.4654` → IC=+0.198 (n=4039)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4654 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.207 (n=3807)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 157.0 (IC base=+0.059)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.185 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0049 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.189 (n=458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0076 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3228` → IC=+0.167 (n=1369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3228 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.189 (n=673)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 8.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.067` → IC=+0.277 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.067 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.198 (n=177)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `2.6298` → IC=+0.155 (n=1262)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.6298 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.167 (n=1262)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.189 (n=1257)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=918)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1937` → IC=+0.275 (n=683)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1937 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.251 (n=706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0538` → IC=+0.286 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0538 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.213` → IC=+0.244 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.213 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0926` → IC=+0.233 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0926 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.267 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.7379` → IC=+0.267 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7379 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1584.11` → IC=+0.250 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1584.11 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.234 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.239 (n=457)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=1037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9222` → IC=+0.254 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9222 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.2132` → IC=+0.219 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2132 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.774` → IC=+0.234 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.774 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `1.2608` → IC=+0.220 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2608 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `0.8708` → IC=+0.213 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8708 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.215 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4939` → IC=+0.220 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4939 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.3839` → IC=+0.217 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3839 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `10916.3675` → IC=+0.221 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10916.3675 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.160 (n=984)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0049 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0766` → IC=+0.168 (n=372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0766 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.168 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6723` → IC=+0.176 (n=1114)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6723 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.155 (n=1011)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.516` → IC=+0.179 (n=191)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.516 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.151 (n=1114)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.204 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6842` → IC=+0.141 (n=995)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6842 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.185 (n=303)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4376` → IC=+0.155 (n=1006)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4376 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `13242.8486` → IC=+0.156 (n=743)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 13242.8486 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.162 (n=312)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 216.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.187 (n=1341)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0057 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.471` → IC=+0.224 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.471 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.182 (n=1136)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.3768` → IC=+0.182 (n=174)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.3768 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `3.043` → IC=+0.197 (n=568)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 3.043 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.188 (n=1530)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.222 (n=1160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.248 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.3796` → IC=+0.231 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3796 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.564` → IC=+0.233 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.564 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.388` → IC=+0.215 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.388 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3652` → IC=+0.265 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3652 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.8432` → IC=+0.205 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8432 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.2947` → IC=+0.222 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2947 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1887.161` → IC=+0.230 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.161 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.216 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.214)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1690)

- **PATRÓN** `ibs_20min` > `0.9299` → IC=+0.166 (n=285)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9299 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.3371` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3371 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` < `0.4917` → IC=+0.334 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4917 (IC base=+0.006)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.258` → IC=+0.135 (n=532)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 4.258 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6461` → IC=+0.378 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6461 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.1808` → IC=+0.353 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1808 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.4916` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4916 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1278` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1278 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.346 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 167.0 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.1655` → IC=+0.190 (n=185)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1655 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` < `0.8572` → IC=+0.150 (n=361)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8572 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.1639` → IC=+0.143 (n=180)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1639 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2708` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2708 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.5064` → IC=+0.176 (n=437)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5064 (IC base=+0.001)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=243)

- **FILTRO** `ibs_20min` < `0.3714` → IC=-0.173 (n=96)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3714
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=197)

- **FILTRO** `ibs_20min` > `0.2727` → IC=-0.128 (n=1724)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=860)

- **FILTRO** `sigma_ewma_delta_pct` > `8.613` → IC=-0.196 (n=281)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.613
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2303)

- **PATRÓN** `ibs_20min` > `0.7547` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7547 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `1.3203` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3203 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` < `0.5093` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5093 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.5788` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5788 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `3.0245` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0245 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.323 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7708` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7708 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` < `1.1044` → IC=+0.206 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1044 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.2029` → IC=+0.208 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2029 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.1481` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1481 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.4885` → IC=+0.239 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4885 (IC base=-0.046)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.247 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=-0.046)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6568` → IC=-0.190 (n=427)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1285)

- **FILTRO** `ibs_20min` < `0.7817` → IC=-0.140 (n=1284)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7817
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=428)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.199 (n=377)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1335)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.201 (n=647)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1948)

- **PATRÓN** `dist_vwap_pct` > `0.9754` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9754 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` < `0.2591` → IC=+0.303 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2591 (IC base=-0.083)

- **PATRÓN** `volumen_regimen` < `1.0034` → IC=+0.273 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0034 (IC base=-0.083)

- **PATRÓN** `volumen_regimen` > `0.6119` → IC=+0.289 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6119 (IC base=-0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.276 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=-0.083)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.281 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` > `1.0236` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0236 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` < `0.2666` → IC=+0.239 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2666 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` < `0.7344` → IC=+0.241 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7344 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` > `1.094` → IC=+0.286 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.094 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1065` → IC=+0.265 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1065 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.2351` → IC=+0.255 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2351 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.4734` → IC=+0.236 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4734 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.239 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.173 (n=2546)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0091 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.9835` → IC=+0.290 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9835 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `1.0247` → IC=+0.284 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0247 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.509` → IC=+0.142 (n=3604)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.509 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.6744` → IC=+0.233 (n=2315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6744 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2486` → IC=+0.255 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2486 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.4784` → IC=+0.237 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4784 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.7806` → IC=+0.235 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7806 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.276 (n=3606)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.140 (n=2597)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0084 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.150 (n=6845)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5556 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6975` → IC=+0.243 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6975 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1687` → IC=+0.230 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1687 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.7107` → IC=+0.231 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7107 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `1.1996` → IC=+0.251 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1996 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2529` → IC=+0.319 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2529 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.6251` → IC=+0.253 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6251 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `2.3723` → IC=+0.255 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3723 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.254 (n=2603)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.412` → IC=-0.164 (n=388)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.412
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1299)

- **PATRÓN** `ibs_20min` > `0.8645` → IC=+0.251 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8645 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.29` → IC=+0.146 (n=702)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.29 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2262` → IC=+0.282 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2262 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.8555` → IC=+0.198 (n=355)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.8555 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.6662` → IC=+0.194 (n=178)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6662 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` < `0.1791` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1791 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4112` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4112 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8269` → IC=-0.149 (n=573)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8269
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1724)

- **PATRÓN** `dist_vwap_pct` > `0.3061` → IC=+0.137 (n=246)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.3061 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.6495` → IC=+0.135 (n=592)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.6495 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.159 (n=215)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.182 (n=212)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 235.0 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.1622` → IC=+0.215 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1622 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.1336` → IC=+0.220 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1336 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.8012` → IC=+0.217 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8012 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1657` → IC=+0.236 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1657 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `243.0` → IC=+0.218 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 243.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.264 (n=1084)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0966` → IC=+0.247 (n=405)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0966 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.238 (n=612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.252 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.268 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.1109` → IC=+0.253 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1109 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.8779` → IC=+0.237 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8779 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `3.6311` → IC=+0.251 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6311 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.252 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.294 (n=970)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.317 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.285 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.885` → IC=+0.296 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.885 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.3474` → IC=+0.297 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3474 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` < `1.6254` → IC=+0.282 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6254 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.2257` → IC=+0.281 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2257 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `1877.2368` → IC=+0.300 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.2368 (IC base=+0.277)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.275 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.277)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2437` → IC=-0.213 (n=347)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2437
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1042)

- **FILTRO** `ibs_20min` > `0.8097` → IC=-0.185 (n=455)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8097
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1366)

- **PATRÓN** `ibs_20min` > `0.8031` → IC=+0.142 (n=473)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.8031 (IC base=-0.016)

- **PATRÓN** `dist_vwap_pct` > `0.3052` → IC=+0.226 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3052 (IC base=-0.016)

- **PATRÓN** `volumen_regimen` < `0.9407` → IC=+0.214 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9407 (IC base=-0.016)

- **PATRÓN** `volumen_regimen` > `0.6109` → IC=+0.190 (n=282)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6109 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` < `0.1084` → IC=+0.217 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1084 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.4909` → IC=+0.256 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4909 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `1.7478` → IC=+0.219 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7478 (IC base=-0.016)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.253 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=-0.016)

- **PATRÓN** `dist_vwap_pct` > `0.1692` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1692 (IC base=-0.019)

- **PATRÓN** `dist_vwap_pct` < `0.2862` → IC=+0.165 (n=231)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2862 (IC base=-0.019)

- **PATRÓN** `volumen_regimen` < `0.9712` → IC=+0.168 (n=197)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.9712 (IC base=-0.019)

- **PATRÓN** `volumen_regimen` > `0.7126` → IC=+0.173 (n=200)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.7126 (IC base=-0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.1528` → IC=+0.315 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1528 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` > `2.4157` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4157 (IC base=-0.019)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.237 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=-0.019)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.207 (n=824)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=837)

- **FILTRO** `ibs_20min` > `0.7143` → IC=-0.236 (n=438)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1318)

- **FILTRO** `sigma_ewma_delta_pct` > `4.704` → IC=-0.170 (n=410)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.704
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1346)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.255 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7795` → IC=+0.340 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7795 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.294 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8605 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.7191` → IC=+0.276 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7191 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1084` → IC=+0.279 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1084 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4442` → IC=+0.318 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4442 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.324 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.128 (n=883)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.4 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` > `0.7857` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7857 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` < `0.1875` → IC=+0.186 (n=323)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1875 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.7148` → IC=+0.247 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7148 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.182 (n=322)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2213` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2213 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.629` → IC=+0.200 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.629 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.5045` → IC=+0.182 (n=331)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.5045 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.216 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.322 (n=695)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.284 (n=488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.345 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.2672` → IC=+0.316 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2672 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.372` → IC=+0.297 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.372 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `0.6815` → IC=+0.285 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6815 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2364` → IC=+0.300 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2364 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.5484` → IC=+0.273 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5484 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `1.4429` → IC=+0.272 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4429 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `2584.4484` → IC=+0.276 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2584.4484 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.272 (n=380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0071 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0142` → IC=+0.294 (n=759)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0142 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.284 (n=573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.3925` → IC=+0.304 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3925 (IC base=+0.268)

- **PATRÓN** `dist_vwap_pct` > `0.5529` → IC=+0.285 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5529 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.415` → IC=+0.290 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.415 (IC base=+0.268)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.311 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.243` → IC=+0.362 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.243 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `2.5387` → IC=+0.265 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5387 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.17` → IC=+0.266 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.17 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.268 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `2331.9466` → IC=+0.274 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2331.9466 (IC base=+0.268)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.177 (n=2020)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.202 (n=2015)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3345` → IC=+0.173 (n=5302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3345 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=6294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6944` → IC=+0.229 (n=5383)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6944 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9633` → IC=+0.225 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9633 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.218` → IC=+0.248 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.218 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.163 (n=4017)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2155 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6205` → IC=+0.159 (n=4017)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6205 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.107` → IC=+0.186 (n=2359)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.107 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5664` → IC=+0.172 (n=2520)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5664 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6687` → IC=+0.168 (n=1908)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.6687 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3822.4537` → IC=+0.171 (n=2008)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3822.4537 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.184 (n=4941)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 123.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.188 (n=3906)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0063 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.205 (n=1952)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.202 (n=2835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4595` → IC=+0.226 (n=5856)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4595 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2257` → IC=+0.162 (n=4358)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2257 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.195 (n=1014)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1891` → IC=+0.157 (n=4276)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1891 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6241` → IC=+0.151 (n=4275)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6241 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2926` → IC=+0.227 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2926 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5745` → IC=+0.172 (n=2287)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5745 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6529` → IC=+0.178 (n=1733)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6529 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.171 (n=4813)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 125.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.223 (n=341)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.204 (n=461)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.314` → IC=+0.205 (n=1016)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.314 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.215 (n=503)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.097` → IC=+0.307 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.097 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.239 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.5529` → IC=+0.183 (n=923)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.5529 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.429` → IC=+0.184 (n=924)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.429 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.242 (n=653)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.262 (n=246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1823` → IC=+0.296 (n=493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1823 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.243 (n=776)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.1053` → IC=+0.272 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1053 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.095` → IC=+0.251 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.095 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.096` → IC=+0.234 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.096 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.262 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4302` → IC=+0.256 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4302 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.679` → IC=+0.245 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.679 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1595.0002` → IC=+0.254 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1595.0002 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.246 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.181 (n=293)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4303` → IC=+0.221 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4303 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2181` → IC=+0.214 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2181 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.669` → IC=+0.227 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.669 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.175 (n=877)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.2653 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2326` → IC=+0.189 (n=191)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2326 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.197 (n=282)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `9847.9824` → IC=+0.180 (n=877)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9847.9824 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.181 (n=879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0049 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0583` → IC=+0.199 (n=333)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0583 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.165 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 7.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.5289` → IC=+0.192 (n=997)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5289 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1401` → IC=+0.168 (n=1012)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1401 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.047` → IC=+0.214 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.047 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2096` → IC=+0.166 (n=997)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2096 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.178 (n=309)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.163 (n=887)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.157 (n=269)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 230.0 (IC base=+0.150)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.197 (n=994)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0058 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1938` → IC=+0.196 (n=662)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1938 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.618` → IC=+0.264 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.618 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.185 (n=816)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.184 (n=384)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.681` → IC=+0.188 (n=309)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.681 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `3.6503` → IC=+0.204 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6503 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.228 (n=281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0922` → IC=+0.246 (n=281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0922 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.269 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.3448` → IC=+0.250 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3448 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.269 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3606` → IC=+0.267 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3606 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `3.5269` → IC=+0.246 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5269 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1887.4151` → IC=+0.234 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.4151 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.210 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.179 (n=835)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0065 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4222` → IC=+0.166 (n=949)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4222 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.165 (n=955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.4079` → IC=+0.202 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4079 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1355` → IC=+0.195 (n=618)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1355 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.181` → IC=+0.240 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.181 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.158 (n=633)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8577 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1952` → IC=+0.177 (n=317)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.1952 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.215 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4007` → IC=+0.169 (n=309)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4007 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.5292` → IC=+0.185 (n=309)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5292 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7277.355` → IC=+0.190 (n=633)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7277.355 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.159 (n=780)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 152.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.163 (n=1025)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0071 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3788` → IC=+0.145 (n=1025)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3788 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6027` → IC=+0.179 (n=1025)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6027 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.3418` → IC=+0.140 (n=1128)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3418 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.037` → IC=+0.190 (n=201)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 12.037 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8596` → IC=+0.141 (n=684)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8596 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.609` → IC=+0.130 (n=1025)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.609 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.195 (n=149)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.7931` → IC=+0.136 (n=607)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.7931 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4834` → IC=+0.143 (n=303)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4834 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.151 (n=465)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.148 (n=750)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0077 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.195 (n=1134)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0185` → IC=+0.230 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0185 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.465` → IC=+0.253 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.465 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.122 (n=1123)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2203 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.131 (n=361)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1157)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2895.2022` → IC=+0.195 (n=509)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2895.2022 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.136 (n=821)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.150 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0058 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5435` → IC=+0.207 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5435 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.7133` → IC=+0.145 (n=198)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.7133 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.1929` → IC=+0.135 (n=1043)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1929 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.375` → IC=+0.160 (n=239)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 7.375 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.041` → IC=+0.129 (n=986)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.041 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4646` → IC=+0.131 (n=326)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4646 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.1743` → IC=+0.138 (n=443)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.1743 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3081.0348` → IC=+0.160 (n=374)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3081.0348 (IC base=+0.113)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` < `0.0271` → IC=+0.202 (n=1069)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0271 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0179` → IC=+0.213 (n=712)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0179 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.1668` → IC=+0.218 (n=470)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1668 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.725` → IC=+0.257 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.725 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `1.2484` → IC=+0.236 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2484 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.346` → IC=+0.243 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.346 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.207 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2075 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.6083` → IC=+0.211 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6083 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.261 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1841` → IC=+0.217 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1841 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.203 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2558.1816` → IC=+0.203 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2558.1816 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.235 (n=379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0163` → IC=+0.212 (n=756)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0163 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0922` → IC=+0.216 (n=379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0922 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=517)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.438` → IC=+0.241 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.438 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1626` → IC=+0.228 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1626 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2686` → IC=+0.204 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2686 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.304` → IC=+0.240 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.304 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6289` → IC=+0.218 (n=1134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6289 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.287 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2444` → IC=+0.197 (n=878)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2444 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4611` → IC=+0.193 (n=998)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4611 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2528.7202` → IC=+0.214 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2528.7202 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.147 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0038 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.151 (n=485)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0088 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.149 (n=483)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=732)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.3875` → IC=+0.166 (n=1449)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3875 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.8478` → IC=+0.168 (n=197)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.8478 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.696` → IC=+0.164 (n=659)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.696 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8626` → IC=+0.153 (n=831)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8626 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.164 (n=397)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.147 (n=462)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.5669` → IC=+0.157 (n=462)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5669 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=1601)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8121.9037` → IC=+0.155 (n=657)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8121.9037 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.157 (n=1230)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 156.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.139 (n=1016)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=1543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.4783` → IC=+0.156 (n=1341)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4783 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.985` → IC=+0.134 (n=452)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 5.985 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2242` → IC=+0.122 (n=1345)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2242 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.142 (n=395)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.2373` → IC=+0.133 (n=1280)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2373 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.125 (n=616)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 27.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1032` → IC=+0.146 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1032 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.142 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.2855` → IC=+0.139 (n=322)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.2855 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.140 (n=98)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.31` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.31 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.160 (n=142)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6895 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.0904` → IC=+0.128 (n=119)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.0904 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `9742.4663` → IC=+0.139 (n=322)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 9742.4663 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 151.0 (IC base=+0.101)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.216 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3449` → IC=+0.150 (n=472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3449 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.3451` → IC=+0.207 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3451 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1865` → IC=+0.145 (n=474)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1865 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.406` → IC=+0.136 (n=193)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 4.406 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.159` → IC=+0.126 (n=533)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 9.159 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.131 (n=472)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1917 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0609 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.1128` → IC=+0.157 (n=406)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1128 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.160 (n=148)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 159.0 (IC base=+0.125)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.260 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.205 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.213 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.229 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.2663` → IC=+0.227 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2663 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.217 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.219 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.8293` → IC=+0.194 (n=295)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8293 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2479` → IC=+0.315 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2479 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.3716` → IC=+0.214 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3716 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.3827` → IC=+0.255 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3827 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `12367.2302` → IC=+0.211 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12367.2302 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.134 (n=389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0066 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.138 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 11.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.2923` → IC=+0.159 (n=259)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.2923 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.51` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.51 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.2304` → IC=+0.123 (n=388)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2304 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.8232` → IC=+0.132 (n=245)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.8232 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3958` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3958
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=366)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.176 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `2982.5482` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2982.5482 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.4545` → IC=+0.163 (n=286)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.4545 (IC base=+0.082)

- **PATRÓN** `volumen_regimen` < `0.7151` → IC=+0.156 (n=126)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7151 (IC base=+0.082)

- **PATRÓN** `volumen_spike_ratio` < `2.513` → IC=+0.121 (n=262)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.513 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.126 (n=233)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 44.0 (IC base=+0.082)

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
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.192 (n=3462)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0086 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=7976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4721` → IC=+0.213 (n=7621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4721 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.9157` → IC=+0.205 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9157 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.222 (n=3734)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8815` → IC=+0.165 (n=3424)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8815 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2401` → IC=+0.186 (n=1444)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2401 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.6398` → IC=+0.182 (n=2420)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6398 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3784.1723` → IC=+0.170 (n=2541)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3784.1723 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.194 (n=5502)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 94.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.196 (n=4686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0067 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.4795` → IC=+0.184 (n=7015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4795 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=2714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.239 (n=7015)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5556 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2357` → IC=+0.164 (n=4442)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2357 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.852` → IC=+0.201 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.852 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.6259` → IC=+0.161 (n=1615)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6259 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.2027` → IC=+0.161 (n=1615)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.2027 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.249 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.3005` → IC=+0.190 (n=2848)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.3005 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.188 (n=2020)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 26.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.216 (n=428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.229 (n=581)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=860)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.317 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.865` → IC=+0.314 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.865 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.240 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `1.564` → IC=+0.186 (n=526)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.564 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.273` → IC=+0.197 (n=542)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.273 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.262 (n=674)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.267 (n=903)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.2023` → IC=+0.280 (n=672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2023 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.3404` → IC=+0.284 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3404 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.61` → IC=+0.264 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.61 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.226` → IC=+0.295 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.226 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `1.8995` → IC=+0.281 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8995 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1585.8448` → IC=+0.268 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1585.8448 (IC base=+0.255)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.192 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0027 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1827` → IC=+0.152 (n=806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1827 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6905` → IC=+0.243 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6905 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.3479` → IC=+0.198 (n=462)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3479 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.163 (n=283)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.374` → IC=+0.152 (n=1073)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.374 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6911` → IC=+0.182 (n=532)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6911 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.183 (n=329)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4203` → IC=+0.156 (n=1155)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4203 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7574` → IC=+0.159 (n=770)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7574 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `10762.5448` → IC=+0.168 (n=1079)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10762.5448 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `494.0` → IC=+0.159 (n=1084)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 494.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.170 (n=1083)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0057 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.2618` → IC=+0.171 (n=953)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2618 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.178 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.6376` → IC=+0.207 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6376 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.5435` → IC=+0.164 (n=215)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.5435 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.167 (n=996)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.258` → IC=+0.174 (n=535)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.258 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.167 (n=1083)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1913 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1504` → IC=+0.208 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1504 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.4156` → IC=+0.172 (n=985)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.4156 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `12168.9034` → IC=+0.158 (n=722)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12168.9034 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `309.0` → IC=+0.166 (n=393)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 309.0 (IC base=+0.157)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.224 (n=1206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.214 (n=1219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.6739` → IC=+0.247 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6739 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.541` → IC=+0.293 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.541 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.2179` → IC=+0.215 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2179 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `3.0052` → IC=+0.234 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0052 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=1372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.237 (n=1165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.3651` → IC=+0.267 (n=1024)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3651 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.713` → IC=+0.275 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.713 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.3595` → IC=+0.293 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3595 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.7916` → IC=+0.226 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7916 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.2372` → IC=+0.227 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2372 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `1891.5784` → IC=+0.233 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1891.5784 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.243 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.230)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.168 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4318` → IC=+0.137 (n=1292)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.4318 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=1356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.704` → IC=+0.232 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.704 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.3551` → IC=+0.183 (n=481)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.3551 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.274` → IC=+0.164 (n=551)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.274 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8785` → IC=+0.159 (n=862)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8785 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.229 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.5068` → IC=+0.145 (n=547)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5068 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.4694` → IC=+0.161 (n=414)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4694 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8750.1763` → IC=+0.230 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8750.1763 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.162 (n=388)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 89.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.156 (n=1039)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.154 (n=1037)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.3284` → IC=+0.231 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3284 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2052` → IC=+0.145 (n=969)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2052 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.104` → IC=+0.207 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.104 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8599` → IC=+0.143 (n=692)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8599 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1808` → IC=+0.152 (n=346)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1808 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.266 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.557` → IC=+0.152 (n=426)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.557 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.472` → IC=+0.171 (n=323)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.472 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10973.4331` → IC=+0.190 (n=346)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 10973.4331 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `194.0` → IC=+0.144 (n=958)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 194.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.121 (n=1350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 5.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.179 (n=1314)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4667 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `1.0143` → IC=+0.193 (n=223)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 1.0143 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.414` → IC=+0.221 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.414 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=916)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2900.261` → IC=+0.241 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2900.261 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.129 (n=971)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 53.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.171 (n=560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0061 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1241` → IC=+0.152 (n=423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1241 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.209 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.625 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.4769` → IC=+0.128 (n=1253)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.4769 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.437` → IC=+0.124 (n=1222)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.437 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.7176` → IC=+0.155 (n=558)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7176 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2197` → IC=+0.173 (n=194)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2197 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4623` → IC=+0.140 (n=370)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4623 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.225` → IC=+0.126 (n=503)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.225 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2913.9614` → IC=+0.168 (n=422)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2913.9614 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0181` → IC=+0.213 (n=883)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0181 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.205 (n=1174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.314 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1858` → IC=+0.235 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1858 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.346` → IC=+0.247 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.346 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2434` → IC=+0.207 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2434 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6263` → IC=+0.208 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6263 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.225 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.5768` → IC=+0.237 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5768 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2566.5304` → IC=+0.210 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2566.5304 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.233 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0254` → IC=+0.226 (n=487)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0254 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.505` → IC=+0.255 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.505 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.2739` → IC=+0.205 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2739 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.01` → IC=+0.263 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.01 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.240 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.257 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.2225` → IC=+0.196 (n=1126)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2225 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4422` → IC=+0.197 (n=1280)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4422 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2541.9388` → IC=+0.202 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2541.9388 (IC base=+0.201)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=2568)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.155 (n=2220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0094 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5293` → IC=+0.155 (n=2523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5293 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.160 (n=877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9375` → IC=+0.212 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9375 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1891` → IC=+0.155 (n=821)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1891 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.736` → IC=+0.167 (n=811)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.736 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.9065` → IC=+0.152 (n=1023)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9065 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1741` → IC=+0.173 (n=687)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1741 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4629` → IC=+0.161 (n=833)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4629 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.9089` → IC=+0.157 (n=1664)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9089 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8197.4544` → IC=+0.153 (n=1144)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8197.4544 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.188 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.154 (n=1938)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.163 (n=647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1794` → IC=+0.161 (n=853)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1794 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.7081` → IC=+0.147 (n=344)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7081 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.27` → IC=+0.145 (n=1921)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.27 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1133` → IC=+0.144 (n=1618)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1133 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.151 (n=913)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.5724` → IC=+0.141 (n=1918)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5724 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.149 (n=1279)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=2568)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7754.4674` → IC=+0.150 (n=1731)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7754.4674 (IC base=+0.136)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.170 (n=277)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0034 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.179 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.162 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.5254` → IC=+0.199 (n=207)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5254 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.2354` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2354 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.25` → IC=+0.166 (n=393)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 8.25 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.2448` → IC=+0.160 (n=310)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2448 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.8235` → IC=+0.192 (n=206)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.8235 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2313` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2313 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.217 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.7581` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.7581 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `12593.9941` → IC=+0.203 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12593.9941 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.205 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.145 (n=866)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.171 (n=314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.1527` → IC=+0.163 (n=381)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1527 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.6103` → IC=+0.143 (n=393)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6103 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.6015` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6015 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.228` → IC=+0.134 (n=893)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.228 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.025` → IC=+0.149 (n=947)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 9.025 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.176 (n=578)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8847 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.161 (n=411)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.5735` → IC=+0.142 (n=863)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5735 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.148 (n=575)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `12053.6057` → IC=+0.146 (n=774)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 12053.6057 (IC base=+0.133)

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
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.151 (n=746)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0088 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.149 (n=747)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0045 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.5048` → IC=+0.152 (n=746)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.5048 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.152 (n=271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 4.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.5403` → IC=+0.144 (n=498)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5403 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.1834` → IC=+0.154 (n=747)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.1834 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.9756` → IC=+0.179 (n=163)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.9756 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.4255` → IC=+0.150 (n=712)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.4255 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.152 (n=746)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.9097` → IC=+0.148 (n=498)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.9097 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.2712` → IC=+0.153 (n=249)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2712 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.1172` → IC=+0.143 (n=688)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1172 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.164 (n=221)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.168 (n=245)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=708)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `8268.5946` → IC=+0.151 (n=746)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8268.5946 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.164 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0071 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.512` → IC=+0.181 (n=613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.512 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.156 (n=428)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 11.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.163 (n=612)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.1001 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1574` → IC=+0.176 (n=273)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1574 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.4034` → IC=+0.150 (n=630)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.4034 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.802` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.802 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6505` → IC=+0.181 (n=205)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6505 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.7326` → IC=+0.154 (n=547)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7326 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.1527` → IC=+0.153 (n=630)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1527 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.175 (n=263)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.164 (n=530)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4508` → IC=+0.163 (n=601)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4508 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `8201.961` → IC=+0.173 (n=612)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8201.961 (IC base=+0.149)

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

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.140 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0113 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 22.0 (IC base=+0.053)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6429` → IC=-0.172 (n=184)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6429
  - _Potencial_: sin este filtro IC_bueno=+0.213 (n=553)

- **FILTRO** `sigma_h` > `0.008` → IC=-0.258 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.008
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=282)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=294)

- **FILTRO** `dist_vwap_pct` > `0.1621` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1621
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=217)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.178 (n=430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0051 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.213 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6429 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.136` → IC=+0.166 (n=285)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.136 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.128` → IC=+0.212 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.128 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.116` → IC=+0.161 (n=393)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.116 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=448)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.0688` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0688 (IC base=-0.020)

- **PATRÓN** `dist_vwap_pct` < `0.1621` → IC=+0.130 (n=217)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1621 (IC base=-0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.931` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.931 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.0857` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0857 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.6357` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.6357 (IC base=-0.020)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=155)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=-0.020)

- **PATRÓN** `libro_liquidez` > `2976.1916` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2976.1916 (IC base=-0.020)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5857` → IC=-0.177 (n=63)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5857
  - _Potencial_: sin este filtro IC_bueno=+0.208 (n=190)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.173 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.006 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.5857` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5857 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.739` → IC=+0.131 (n=120)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.739 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.0504` → IC=+0.127 (n=167)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0504 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.152 (n=133)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2602` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2602 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.0198` → IC=+0.191 (n=134)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.0198 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2835.039` → IC=+0.126 (n=177)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2835.039 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.0426` → IC=+0.241 (n=25)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0426 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.4946` → IC=+0.220 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4946 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.9536` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.9536 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.0796` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0796 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.4111` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4111 (IC base=+0.049)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.300 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=79)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.175 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0049 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.144 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.649` → IC=+0.242 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.649 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.5504` → IC=+0.200 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5504 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.789` → IC=+0.164 (n=129)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.789 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.144 (n=172)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6214 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.7434` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.7434 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.3826` → IC=+0.148 (n=143)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.3826 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=201)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `1077.2861` → IC=+0.188 (n=168)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1077.2861 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1021` → IC=+0.194 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1021 (IC base=-0.052)

- **PATRÓN** `ibs_20min` < `0.2452` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2452 (IC base=-0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.257` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.257 (IC base=-0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.1056` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1056 (IC base=-0.052)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.052)

- **PATRÓN** `libro_liquidez` > `1005.653` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1005.653 (IC base=-0.052)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` < `0.6757` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6757
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=171)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.238 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=60)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.321 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.291 (n=41)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.074)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.128 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 14.0 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.199 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6757 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.1756` → IC=+0.133 (n=96)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.1756 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.655` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 3.655 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0643 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `2.5513` → IC=+0.158 (n=153)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.5513 (IC base=+0.074)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.143 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.006 (IC base=-0.070)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.291 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=-0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.174` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 2.174 (IC base=-0.070)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1406` → IC=-0.346 (n=37)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1406
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=113)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.400 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=104)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.340 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=94)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=123)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=112)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=42)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.6687` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6687
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=39)

- **FILTRO** `drift_60min` |x|> `0.1035` → IC=-0.293 (n=27)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1035
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=29)

- **FILTRO** `sigma_ewma_delta_pct` > `3.572` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.572
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=34)

- **FILTRO** `volumen_regimen` > `0.9045` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9045
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8396` → IC=-0.429 (n=40)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8396
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.333 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.326 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

- **FILTRO** `dist_vwap_pct` > `0.1871` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.326 (n=21)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.3298` → IC=-0.158 (n=74)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3298
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=225)

- **FILTRO** `dist_vwap_pct` > `0.4337` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4337
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=266)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7391 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.2365` → IC=+0.130 (n=198)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2365 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `3844.2308` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3844.2308 (IC base=+0.042)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=77)

- **FILTRO** `ibs_20min` < `0.5499` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5499
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=70)

- **FILTRO** `volumen_regimen` < `0.758` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.758
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=70)

- **FILTRO** `volumen_spike_ratio` < `1.4594` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4594
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=49)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.207 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1524 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.096)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=57)

- **FILTRO** `ibs_20min` < `0.7272` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7272
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=57)

- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=73)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.144 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0042 (IC base=+0.058)

- **PATRÓN** `drift_60min` |x|≤ `0.2768` → IC=+0.127 (n=57)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.2768 (IC base=+0.058)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.7272` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.7272 (IC base=+0.058)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.26` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.26 (IC base=+0.015)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2459` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2459
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.161 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.3838` → IC=+0.148 (n=86)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3838 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.155 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.7143` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.7143 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.7692 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1961` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1961 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.5494` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5494 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `514.5372` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 514.5372 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.0984` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0984 (IC base=-0.029)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.127 (n=459)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2824.2811` → IC=+0.171 (n=162)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2824.2811 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2306.5744` → IC=+0.129 (n=535)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2306.5744 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.127 (n=459)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2824.2811` → IC=+0.171 (n=162)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2824.2811 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2306.5744` → IC=+0.129 (n=535)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2306.5744 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=70)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=123)

- **FILTRO** `libro_liquidez` < `2404.4298` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 2404.4298
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=105)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=191)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=177)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

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

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1322)

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
- **FILTRO** `liq_usd_total` < `59480.98` → IC=-0.123 (n=67)

  - _Acción_: SKIP cuando `liq_usd_total` < 59480.98
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=67)

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
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=564)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=419)

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
- **FILTRO** `py_entrada` < `0.435` → IC=-0.132 (n=188)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=439)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=252)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=252)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9975` → IC=-0.132 (n=66)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9975
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=201)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=158)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=158)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=131)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=74)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=160)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=55)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=59)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=89)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.125 (n=1014)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=5431)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6212)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=1034)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1310)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.180 (n=2621)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=7949)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.171 (n=2702)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=8331)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.220 (n=430)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=1348)

- **FILTRO** `ibs_20min` < `0.7475` → IC=-0.182 (n=444)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7475
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=1334)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.162 (n=451)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1514)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.201 (n=449)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=1380)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.213 (n=462)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=1477)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.164 (n=483)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1456)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.201 (n=433)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=1322)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.193 (n=484)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1458)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2389)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2398)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2404)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=283)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.7252` → IC=-0.200 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7252
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=118)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=156)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=617)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=7557)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=17326)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.283 (n=5786)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=19097)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.242 (n=6218)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=18665)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.161 (n=8252)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=16631)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.224 (n=7732)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=23438)

- **FILTRO** `ibs_7min` > `0.2963` → IC=-0.177 (n=7785)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2963
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=23385)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=939)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3046)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.259 (n=1314)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2671)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.194 (n=956)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3029)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.148 (n=3631)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1797)

- **FILTRO** `ibs_7min` > `0.7976` → IC=-0.206 (n=1356)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7976
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=4072)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=996)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=3354)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.256 (n=1011)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3339)

- **FILTRO** `ibs_7min` < `0.7589` → IC=-0.187 (n=1087)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7589
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3263)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.173 (n=1081)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3269)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.255 (n=1030)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3381)

- **FILTRO** `ibs_7min` > `0.2509` → IC=-0.168 (n=1102)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2509
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3309)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.176 (n=1098)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3313)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.181 (n=907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=2832)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.322 (n=898)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=2841)

- **FILTRO** `drift_7min_pct` |x|> `0.1813` → IC=-0.131 (n=1271)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1813
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=2468)

- **FILTRO** `ibs_7min` < `0.2026` → IC=-0.275 (n=934)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2026
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2805)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.220 (n=899)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=2840)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.235 (n=1336)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=4362)

- **FILTRO** `ibs_7min` > `0.2632` → IC=-0.157 (n=1937)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2632
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3761)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=1286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=2804)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.254 (n=990)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3100)

- **FILTRO** `ibs_7min` < `0.7451` → IC=-0.194 (n=1022)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7451
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3068)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.183 (n=1019)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3071)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.259 (n=1024)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3167)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.174 (n=1047)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3144)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.179 (n=1042)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3149)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.254 (n=1054)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3458)

- **FILTRO** `ibs_7min` < `0.7222` → IC=-0.216 (n=1118)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7222
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3394)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.176 (n=1416)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4482)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.281 (n=1012)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3195)

- **FILTRO** `ibs_7min` < `0.7315` → IC=-0.230 (n=1051)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7315
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=3156)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.207 (n=1038)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3169)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.205 (n=1315)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=4229)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=955)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=480)

- **FILTRO** `libro_liquidez` < `10498.4421` → IC=-0.159 (n=130)

  - _Acción_: SKIP cuando `libro_liquidez` < 10498.4421
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=393)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=526)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3986` → IC=+0.136 (n=627)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3986 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.135 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.154 (n=209)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 459.6089 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.133 (n=265)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 27.0 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.140 (n=48)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.137)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.413` → IC=+0.178 (n=85)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.413 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 16.0 (IC base=+0.099)

- **PATRÓN** `total_vol_5m` < `672.2721` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 672.2721 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `7894.6804` → IC=+0.121 (n=114)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 7894.6804 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 81.0 (IC base=+0.099)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.196 (n=113)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.151)

- **PATRÓN** `total_vol_5m` < `6013.826` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 6013.826 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `3200.0566` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3200.0566 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 37.0 (IC base=+0.151)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.164 (n=108)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.142 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 13.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.117)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0078` → IC=-0.335 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=186)

- **FILTRO** `T_h` > `52.6662` → IC=-0.232 (n=188)

  - _Acción_: SKIP cuando `T_h` > 52.6662
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=93)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.171 (n=71)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0038 (IC base=-0.143)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `56.3892` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `T_h` > 56.3892
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=45)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.219 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.144)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.184 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.225 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=74)

- **FILTRO** `T_h` > `71.8388` → IC=-0.185 (n=217)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=73)

- **FILTRO** `pct_vs_K` |x|> `4.4208` → IC=-0.450 (n=58)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4208
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=177)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0037` → IC=-0.286 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=80)

- **FILTRO** `T_h` > `63.9952` → IC=-0.204 (n=79)

  - _Acción_: SKIP cuando `T_h` > 63.9952
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=62)

- **FILTRO** `pct_vs_K` |x|> `3.0033` → IC=-0.426 (n=25)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0033
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=57)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.267 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

- **FILTRO** `T_h` < `87.9808` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `T_h` < 87.9808
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=55)

- **FILTRO** `sigma_h` > `0.01` → IC=-0.250 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=62)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.357 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **FILTRO** `T_h` > `69.2345` → IC=-0.336 (n=59)

  - _Acción_: SKIP cuando `T_h` > 69.2345
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.235 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `T_h` > `71.8388` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `sigma_h` < `0.0103` → IC=-0.370 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0103
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

- **FILTRO** `T_h` > `87.8036` → IC=-0.400 (n=28)

  - _Acción_: SKIP cuando `T_h` > 87.8036
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1526` → IC=+0.444 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1526 (IC base=+0.371)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.463 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.371)

- **PATRÓN** `T_h` > `0.8157` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8157 (IC base=+0.371)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.464 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.371)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.462 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.371)

- **PATRÓN** `edge` > `0.1023` → IC=+0.450 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.407)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.463 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.407)

- **PATRÓN** `T_h` > `0.8157` → IC=+0.431 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8157 (IC base=+0.407)

- **PATRÓN** `dist_50` > `0.4092` → IC=+0.486 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4092 (IC base=+0.407)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.417 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.407)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.474)

- **PATRÓN** `edge` > `0.2135` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2135 (IC base=+0.476)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.474 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.476)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.464 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.476)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.476)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.480 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.476)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.462 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.476)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.468 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.476)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=125)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=219)

- **PATRÓN** `streak_estiramiento` < `0.4429` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.4429 (IC base=+0.035)

- **PATRÓN** `streak_estiramiento` < `0.5577` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.5577 (IC base=+0.029)

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
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=519)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=525)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=301)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=456)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=922)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=533)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=565)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2316)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1190)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1198)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.185 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0039 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.198 (n=482)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0072 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.180 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.174 (n=1063)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3415` → IC=+0.210 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3415 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.178 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 11.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.184 (n=507)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.619` → IC=+0.243 (n=1062)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.619 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1084` → IC=+0.174 (n=709)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1084 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.769` → IC=+0.236 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.769 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `5059.1554` → IC=+0.184 (n=482)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 5059.1554 (IC base=+0.172)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=347)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.218 (n=179)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.214 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.0604` → IC=+0.261 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0604 (IC base=+0.196)

- **PATRÓN** `drift_15min` |x|≤ `0.3766` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3766 (IC base=+0.196)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.203 (n=89)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.196)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1124` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1124 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.213 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.196)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.294 (n=178)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.4066` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4066 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.205 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.68` → IC=+0.248 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.68 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `8803.312` → IC=+0.218 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8803.312 (IC base=+0.196)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `20.351` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 20.351 (IC base=-0.006)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.182 (n=86)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0032 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.136 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0056 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.147 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1411` → IC=+0.157 (n=170)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1411 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.266` → IC=+0.169 (n=164)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.266 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.142 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.228 (n=255)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.5482` → IC=+0.145 (n=294)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.5482 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.210 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `10076.1613` → IC=+0.136 (n=116)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 10076.1613 (IC base=+0.135)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `4.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `ibs_15` > `0.2168` → IC=-0.231 (n=24)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2168
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=48)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.587` → IC=-0.180 (n=48)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.587
  - _Potencial_: sin este filtro IC_bueno=+0.238 (n=147)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.142 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.005 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.181 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0076 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1368` → IC=+0.172 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1368 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0638` → IC=+0.164 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.0638 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.170 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.587` → IC=+0.238 (n=147)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.587 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.5591` → IC=+0.146 (n=173)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.5591 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3002.1997` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3002.1997 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 34.0 (IC base=+0.135)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5885` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5885
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=590)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.0714` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0714
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=51)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.334` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.334 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.015` → IC=+0.256 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.206 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.181)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0648` → IC=+0.195 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.0648 (IC base=+0.181)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.229 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.181)

- **PATRÓN** `ibs_15` > `0.5385` → IC=+0.275 (n=305)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5385 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1729` → IC=+0.199 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1729 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.3078` → IC=+0.183 (n=291)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.3078 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.93` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.93 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.409` → IC=+0.181 (n=271)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 7.409 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.181 (n=330)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.03 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `2716.8736` → IC=+0.238 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2716.8736 (IC base=+0.181)

- **PATRÓN** `ibs_15` < `0.1087` → IC=+0.177 (n=336)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` < 0.1087 (IC base=+0.048)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.373 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.341 (n=269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.339 (n=203)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2966` → IC=+0.369 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2966 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.352 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.376 (n=305)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.424` → IC=+0.371 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.424 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.340 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.018` → IC=+0.333 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.018 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.341 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3425.1488` → IC=+0.347 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3425.1488 (IC base=+0.333)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1204` → IC=+0.344 (n=75)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1204 (IC base=+0.334)

- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.353 (n=114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0032 (IC base=+0.334)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.342 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.334)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1021` → IC=+0.339 (n=153)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1021 (IC base=+0.334)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.406 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.334)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.359 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.334)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.333 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.334)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.367 (n=171)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.334)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.384 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.347 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.334)

- **PATRÓN** `libro_liquidez` > `9160.5319` → IC=+0.353 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9160.5319 (IC base=+0.334)

- **PATRÓN** `ballena_activa_n` < `552.0` → IC=+0.390 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 552.0 (IC base=+0.334)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.339 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0035 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1549` → IC=+0.335 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1549 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.339 (n=135)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.391 (n=135)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` > `0.1414` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1414 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.0995` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0995 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.371 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.348 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `3558.8831` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3558.8831 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.331 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 148.0 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0125` → IC=-0.201 (n=530)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0125
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1592)

- **FILTRO** `ibs_15` < `0.6071` → IC=-0.182 (n=177)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6071
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=531)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.207 (n=247)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1875)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.236 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.058)

- **PATRÓN** `ibs_15` > `0.6071` → IC=+0.252 (n=531)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6071 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` < `0.1122` → IC=+0.179 (n=328)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1122 (IC base=-0.058)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1192` → IC=+0.238 (n=740)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1192 (IC base=-0.046)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1822` → IC=+0.239 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1822 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.356` → IC=+0.279 (n=1110)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.356 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `0.6684` → IC=+0.274 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6684 (IC base=-0.046)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.202 (n=317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=952)

- **FILTRO** `sigma_h` < `0.0032` → IC=-0.234 (n=317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=952)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.210 (n=812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=457)

- **FILTRO** `sigma_ewma_delta_pct` > `19.944` → IC=-0.248 (n=228)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.944
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1041)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.161 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0026 (IC base=+0.070)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.070)

- **PATRÓN** `ibs_15` > `0.8109` → IC=+0.341 (n=105)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8109 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.267 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.070)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6515` → IC=-0.239 (n=86)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6515
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=259)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=328)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.140 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0065 (IC base=+0.131)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.158 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0039 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.215 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.131)

- **PATRÓN** `drift_15min` |x|≤ `0.4193` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.4193 (IC base=+0.131)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.228 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.6515` → IC=+0.255 (n=259)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6515 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.177 (n=187)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.822` → IC=+0.138 (n=277)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 18.822 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=328)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.192 (n=118)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.251 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.3595` → IC=+0.231 (n=411)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3595 (IC base=+0.224)

- **PATRÓN** `drift_15min` |x|≤ `0.7675` → IC=+0.229 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7675 (IC base=+0.224)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2064` → IC=+0.257 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2064 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.245 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.224)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.270 (n=467)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.3857` → IC=+0.245 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3857 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.223` → IC=+0.233 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.223 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.182` → IC=+0.228 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.182 (IC base=+0.224)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.182 (n=385)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=129)

- **FILTRO** `drift_60min` |x|> `0.1644` → IC=-0.210 (n=174)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1644
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=340)

- **FILTRO** `drift_15min` |x|> `0.8398` → IC=-0.231 (n=128)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8398
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=386)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0701` → IC=+0.211 (n=206)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0701 (IC base=-0.043)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.247 (n=231)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` < `0.1738` → IC=+0.205 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1738 (IC base=-0.043)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.019` → IC=-0.253 (n=318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.019
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=320)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=464)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.353 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=-0.047)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.299 (n=327)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` > `1.1104` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1104 (IC base=-0.047)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.133 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0071 (IC base=+0.077)

- **PATRÓN** `drift_60min` |x|≤ `0.0996` → IC=+0.227 (n=20)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0996 (IC base=+0.077)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.077)

- **PATRÓN** `ibs_15` > `0.1457` → IC=+0.123 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` > 0.1457 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1495` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1495 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.077)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.133 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0071 (IC base=+0.077)

- **PATRÓN** `drift_60min` |x|≤ `0.0996` → IC=+0.227 (n=20)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0996 (IC base=+0.077)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.077)

- **PATRÓN** `ibs_15` > `0.1457` → IC=+0.123 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` > 0.1457 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1495` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1495 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.077)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.291 (n=347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.283 (n=519)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.057` → IC=+0.312 (n=174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.057 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1417` → IC=+0.290 (n=346)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1417 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.301` → IC=+0.308 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.301 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8374` → IC=+0.323 (n=519)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8374 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.324 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.314 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.287 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `12445.3624` → IC=+0.302 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12445.3624 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.286 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.282 (n=131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.308 (n=97)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.3849` → IC=+0.288 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3849 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.246` → IC=+0.288 (n=97)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.246 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3724` → IC=+0.294 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3724 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.335 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.8242` → IC=+0.297 (n=289)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8242 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.865` → IC=+0.333 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.865 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `11995.5068` → IC=+0.300 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11995.5068 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.307 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.298 (n=231)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0502` → IC=+0.310 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0502 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1898` → IC=+0.313 (n=105)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1898 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.334 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.321 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.337 (n=231)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.309 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` < `0.454` → IC=+0.299 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.454 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.72` → IC=+0.316 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.72 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.304 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.297 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.085` → IC=-0.273 (n=64)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.085
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=193)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.253 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=170)

- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.197 (n=64)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=193)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1851` → IC=-0.127 (n=73)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1851
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=73)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2412` → IC=-0.138 (n=67)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2412
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=69)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2312` → IC=-0.204 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2312
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

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
- **PATRÓN** `T_h` > `87.9922` → IC=+0.149 (n=192)

  - _Acción_: Kelly boost +0.75€ cuando `T_h` > 87.9922 (IC base=+0.138)

- **PATRÓN** `ratio` < `0.9771` → IC=+0.462 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9771 (IC base=+0.138)

- **PATRÓN** `T_h` > `145.8422` → IC=+0.409 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8422 (IC base=+0.348)

- **PATRÓN** `ratio` > `1.01` → IC=+0.376 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.348)

### WEEKLY_PRICE#BTC
- **FILTRO** `ratio` > `0.9933` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `ratio` > 0.9933
  - _Potencial_: sin este filtro IC_bueno=+0.292 (n=70)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.097)

- **PATRÓN** `T_h` > `87.9957` → IC=+0.306 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.302)

- **PATRÓN** `ratio` > `1.041` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.041 (IC base=+0.302)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9836` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.196)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.409 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.196)

- **PATRÓN** `T_h` > `87.996` → IC=+0.346 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.996 (IC base=+0.327)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.369 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.327)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.405)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.619 sube el IC de +0.172 a +0.243 en UPDOWN_GBM#15min (n=1062). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.196 a +0.294 en UPDOWN_GBM#BTC#15min (n=178). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.135 a +0.228 en UPDOWN_GBM#ETH#15min (n=255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.587 sube el IC de +0.135 a +0.238 en UPDOWN_GBM#SOL#15min (n=147). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5385 sube el IC de +0.181 a +0.275 en UPDOWN_GBM#XRP#15min (n=305). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1087 sube el IC de +0.048 a +0.177 en UPDOWN_GBM#XRP#15min (n=336). Ya aplicado como kelly_boost=+0.89€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6071 sube el IC de -0.058 a +0.252 en UPDOWN_GBM_15M_TARDIO (n=531). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.356 sube el IC de -0.046 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1110). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8109 sube el IC de +0.070 a +0.341 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=105). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6515 sube el IC de +0.131 a +0.255 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=259). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.361 sube el IC de +0.224 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=467). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.147 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.043 a +0.247 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=231). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.047 a +0.299 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8374 sube el IC de +0.284 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=519). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8242 sube el IC de +0.275 a +0.297 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=289). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.293 a +0.337 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=231). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.333 a +0.376 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=305). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.334 a +0.367 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=171). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.329 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=135). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1155 | +0.083 | +138.07€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1155 | +0.083 | +138.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 835 | +0.090 | +115.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 835 | +0.090 | +115.08€ | 3 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 240 | +0.045 | +4.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 240 | +0.045 | +4.23€ | 4 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 54 | +0.161 | +20.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 54 | +0.161 | +20.25€ | 0 | 5 |
| ✅ BALLENAS_TARDIAS | 20396 | -0.103 | -2908.86€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1238 | -0.045 | -183.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 19158 | -0.107 | -2725.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3145 | -0.121 | -558.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3145 | -0.121 | -558.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1238 | -0.045 | -183.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1238 | -0.045 | -183.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5888 | -0.049 | -585.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5888 | -0.049 | -585.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5407 | -0.113 | -434.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5407 | -0.113 | -434.55€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4344 | -0.163 | -985.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4344 | -0.163 | -985.95€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 12069 | -0.042 | +4247.64€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3245 | -0.007 | +1852.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 8824 | -0.055 | +2395.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 12069 | -0.042 | +4247.64€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3245 | -0.007 | +1852.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 8824 | -0.055 | +2395.14€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 928 | -0.103 | -139.29€ | 1 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 59 | -0.090 | -12.04€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 869 | -0.104 | -127.25€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 533 | -0.078 | -69.60€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 41 | -0.081 | -7.02€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 492 | -0.077 | -62.57€ | 1 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 257 | -0.160 | -58.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 18 | -0.090 | -5.02€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 239 | -0.164 | -53.62€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 77 | -0.057 | -10.92€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 77 | -0.057 | -10.92€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 73956 | +0.113 | -3815.16€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 11583 | +0.182 | -367.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 285 | -0.117 | -46.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 56969 | +0.100 | -3298.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5119 | +0.116 | -102.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 9495 | +0.097 | -879.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 38 | -0.150 | -1.48€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 9442 | +0.099 | -865.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 14946 | +0.131 | -317.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3533 | +0.201 | -118.86€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 9439 | +0.109 | -192.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1932 | +0.116 | +16.23€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 9534 | +0.089 | -932.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 45 | -0.053 | -1.73€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 9474 | +0.090 | -919.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 15839 | +0.125 | -299.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4468 | +0.171 | -75.69€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 9519 | +0.108 | -169.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1840 | +0.100 | -45.49€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 14633 | +0.116 | -821.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3461 | +0.185 | -180.77€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 188 | -0.074 | +7.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 9637 | +0.092 | -575.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1347 | +0.138 | -72.83€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#XRP | 9509 | +0.103 | -565.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 38 | +0.000 | +10.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 9458 | +0.103 | -575.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 11688 | +0.189 | -807.81€ | 3 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 11688 | +0.189 | -807.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2874 | +0.169 | -307.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2874 | +0.169 | -307.41€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 616 | +0.180 | +4.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 616 | +0.180 | +4.87€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2820 | +0.176 | -266.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2820 | +0.176 | -266.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2535 | +0.236 | -77.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2535 | +0.236 | -77.85€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2764 | +0.191 | -175.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2764 | +0.191 | -175.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 541 | +0.434 | -10.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 541 | +0.434 | -10.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 206 | +0.438 | -1.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 206 | +0.438 | -1.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 205 | +0.442 | +1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 205 | +0.442 | +1.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 122 | +0.403 | -8.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 122 | +0.403 | -8.55€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 39917 | +0.195 | -3345.33€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 39917 | +0.195 | -3345.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6953 | +0.169 | -883.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6953 | +0.169 | -883.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6331 | +0.223 | -242.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6331 | +0.223 | -242.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6915 | +0.169 | -881.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6915 | +0.169 | -881.79€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6422 | +0.217 | -269.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6422 | +0.217 | -269.99€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6587 | +0.203 | -446.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6587 | +0.203 | -446.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6709 | +0.191 | -620.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6709 | +0.191 | -620.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 14904 | +0.124 | +288.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 14904 | +0.124 | +288.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7392 | +0.130 | +205.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7392 | +0.130 | +205.99€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7512 | +0.119 | +82.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7512 | +0.119 | +82.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1234 | +0.288 | -22.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1234 | +0.288 | -22.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 545 | +0.273 | -19.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 545 | +0.273 | -19.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 590 | +0.292 | -2.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 590 | +0.292 | -2.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 99 | +0.332 | -1.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 99 | +0.332 | -1.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 545 | +0.430 | -8.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 545 | +0.430 | -8.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 254 | +0.430 | -4.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 254 | +0.430 | -4.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 252 | +0.433 | -3.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 252 | +0.433 | -3.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 39 | +0.378 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 39 | +0.378 | -0.28€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 846 | +0.065 | -49.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 301 | +0.048 | -30.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 545 | +0.074 | -19.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 53 | +0.118 | +2.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 53 | +0.118 | +2.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 659 | +0.075 | -22.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 114 | +0.078 | -3.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 545 | +0.074 | -19.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 134 | -0.007 | -29.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 134 | -0.007 | -29.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 26294 | +0.098 | -799.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2216 | +0.094 | +32.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 24078 | +0.099 | -832.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 15012 | +0.102 | -235.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2216 | +0.094 | +32.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 12796 | +0.103 | -268.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4564 | +0.115 | +32.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4564 | +0.115 | +32.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6718 | +0.079 | -596.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6718 | +0.079 | -596.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 719 | +0.253 | -94.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 719 | +0.253 | -94.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 719 | +0.253 | -94.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 719 | +0.253 | -94.01€ | 0 | 4 |
| ✅ GBM_LATE_15M | 19488 | +0.075 | +8750.69€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 19488 | +0.075 | +8750.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3190 | +0.196 | +2346.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3190 | +0.196 | +2346.20€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 2867 | +0.174 | +1926.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2867 | +0.174 | +1926.01€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 3331 | +0.193 | +2409.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3331 | +0.193 | +2409.13€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 2916 | +0.003 | +437.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2916 | +0.003 | +437.49€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 2877 | -0.038 | +622.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2877 | -0.038 | +622.64€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 4307 | -0.050 | +1009.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4307 | -0.050 | +1009.22€ | 4 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 20554 | +0.076 | +10213.70€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 20554 | +0.076 | +10213.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3771 | +0.011 | +1943.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3771 | +0.011 | +1943.53€ | 1 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4340 | +0.005 | +813.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4340 | +0.005 | +813.25€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2908 | +0.254 | +2835.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2908 | +0.254 | +2835.08€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3210 | -0.018 | +392.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3210 | -0.018 | +392.91€ | 2 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3417 | +0.014 | +1209.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3417 | +0.014 | +1209.58€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2908 | +0.268 | +3019.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2908 | +0.268 | +3019.36€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 15836 | +0.169 | +11602.93€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 15836 | +0.169 | +11602.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2338 | +0.209 | +1878.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2338 | +0.209 | +1878.24€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2498 | +0.156 | +1811.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2498 | +0.156 | +1811.98€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2443 | +0.203 | +1898.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2443 | +0.203 | +1898.71€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2631 | +0.140 | +1758.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2631 | +0.140 | +1758.39€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2990 | +0.112 | +1933.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2990 | +0.112 | +1933.50€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2936 | +0.203 | +2322.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2936 | +0.203 | +2322.11€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3962 | +0.124 | +1572.29€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3962 | +0.124 | +1572.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 141 | +0.115 | +56.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 141 | +0.115 | +56.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1057 | +0.116 | +410.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1057 | +0.116 | +410.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1104 | +0.151 | +503.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1104 | +0.151 | +503.33€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 789 | +0.079 | +201.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 789 | +0.079 | +201.18€ | 1 | 8 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 19514 | +0.173 | +14077.20€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 19514 | +0.173 | +14077.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3051 | +0.221 | +2572.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3051 | +0.221 | +2572.56€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3053 | +0.152 | +2005.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3053 | +0.152 | +2005.76€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3158 | +0.219 | +2644.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3158 | +0.219 | +2644.27€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3104 | +0.137 | +2003.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3104 | +0.137 | +2003.41€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3437 | +0.106 | +1958.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3437 | +0.106 | +1958.57€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3711 | +0.203 | +2892.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3711 | +0.203 | +2892.63€ | 0 | 24 |
| ✅ GBM_LATE_5M | 5946 | +0.141 | +3233.42€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5946 | +0.141 | +3233.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1566 | +0.139 | +954.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1566 | +0.139 | +954.85€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1810 | +0.146 | +987.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1810 | +0.146 | +987.83€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 314 | +0.038 | +45.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 314 | +0.038 | +45.08€ | 2 | 6 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1234 | +0.064 | +467.13€ | 4 | 16 |
| ✅ GBM_LATE_60M#60min | 1234 | +0.064 | +467.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 436 | +0.087 | +163.50€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 436 | +0.087 | +163.50€ | 1 | 15 |
| ✅ GBM_LATE_60M#ETH | 411 | +0.071 | +192.52€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 411 | +0.071 | +192.52€ | 2 | 18 |
| ✅ GBM_LATE_60M#SOL | 387 | +0.030 | +111.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 387 | +0.030 | +111.11€ | 3 | 10 |
| 🚫 GBM_LATE_60M_FADE | 294 | -0.270 | -28.11€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 294 | -0.270 | -28.11€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 110 | -0.223 | -8.42€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 110 | -0.223 | -8.42€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 100 | -0.304 | -15.89€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 100 | -0.304 | -15.89€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 84 | -0.279 | -3.80€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 84 | -0.279 | -3.80€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 581 | +0.051 | +98.00€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 581 | +0.051 | +98.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 227 | +0.037 | +27.96€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 227 | +0.037 | +27.96€ | 4 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 172 | +0.035 | +0.39€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 172 | +0.035 | +0.39€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 182 | +0.082 | +69.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 182 | +0.082 | +69.65€ | 1 | 15 |
| ✅ LATE_WINDOW_5MIN | 66 | +0.250 | +42.94€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 66 | +0.250 | +42.94€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 66 | +0.250 | +42.94€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 66 | +0.250 | +42.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1359 | +0.105 | +394.24€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1359 | +0.105 | +394.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1359 | +0.105 | +394.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1359 | +0.105 | +394.24€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 351 | -0.084 | -34.00€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 351 | -0.084 | -34.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 86 | -0.080 | -6.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 86 | -0.080 | -6.87€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 118 | -0.017 | -3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 118 | -0.017 | -3.33€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1520 | -0.005 | -9.83€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1520 | -0.005 | -9.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 168 | -0.018 | +2.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 168 | -0.018 | +2.40€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 611 | +0.020 | +14.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 611 | +0.020 | +14.26€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 459 | -0.008 | -8.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 459 | -0.008 | -8.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 105 | -0.061 | -6.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 105 | -0.061 | -6.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 894 | -0.048 | -27.76€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 894 | -0.048 | -27.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 262 | -0.053 | -14.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 262 | -0.053 | -14.64€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 284 | -0.042 | -6.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 284 | -0.042 | -6.29€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 348 | -0.049 | -6.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 348 | -0.049 | -6.84€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 12898 | -0.011 | -179.94€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 12898 | -0.011 | -179.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2349 | -0.022 | -47.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2349 | -0.022 | -47.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2595 | -0.017 | -21.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2595 | -0.017 | -21.86€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3136 | -0.017 | -59.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3136 | -0.017 | -59.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 21603 | -0.012 | +960.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 21603 | -0.012 | +960.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3743 | +0.009 | +480.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3743 | +0.009 | +480.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3503 | -0.026 | -33.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3503 | -0.026 | -33.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3768 | +0.003 | +308.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3768 | +0.003 | +308.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3279 | -0.043 | -72.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3279 | -0.043 | -72.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3613 | -0.016 | +148.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3613 | -0.016 | +148.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3697 | -0.003 | +129.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3697 | -0.003 | +129.11€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4888 | -0.037 | -105.53€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4888 | -0.037 | -105.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1026 | -0.041 | -18.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1026 | -0.041 | -18.97€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 442 | -0.119 | -18.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 442 | -0.119 | -18.15€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1331 | -0.050 | -21.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1331 | -0.050 | -21.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3304 | +0.005 | +1.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3304 | +0.005 | +1.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 186 | +0.011 | -0.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 186 | +0.011 | -0.87€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1279 | +0.010 | +10.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1279 | +0.010 | +10.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 56053 | -0.073 | +1084.93€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 56053 | -0.073 | +1084.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 9413 | -0.081 | +560.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 9413 | -0.081 | +560.77€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 8761 | -0.087 | -293.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 8761 | -0.087 | -293.95€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 9437 | -0.072 | +414.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 9437 | -0.072 | +414.94€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8281 | -0.093 | -231.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8281 | -0.093 | -231.20€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 10410 | -0.048 | +295.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 10410 | -0.048 | +295.93€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 9751 | -0.064 | +338.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 9751 | -0.064 | +338.45€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6702 | -0.021 | -104.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6702 | -0.021 | -104.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1493 | -0.020 | -9.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1493 | -0.020 | -9.89€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1481 | -0.014 | -7.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1481 | -0.014 | -7.67€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 993 | -0.035 | -12.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 993 | -0.035 | -12.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 971 | +0.113 | +338.36€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 835 | +0.121 | +325.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 191 | +0.137 | +94.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 191 | +0.137 | +94.37€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 164 | +0.096 | +39.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 164 | +0.096 | +39.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 170 | +0.099 | +56.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 170 | +0.099 | +56.75€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 150 | +0.151 | +79.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 150 | +0.151 | +79.51€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 160 | +0.117 | +55.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 160 | +0.117 | +55.60€ | 0 | 3 |
| ✅ PRICE_TARGET_GBM | 459 | -0.088 | -11.96€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 203 | -0.129 | -33.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 161 | -0.169 | -36.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 164 | -0.078 | +4.06€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 122 | -0.089 | -2.50€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 92 | -0.011 | +17.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 72 | -0.027 | +11.86€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 355 | -0.113 | -27.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 525 | -0.221 | -42.79€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 220 | -0.203 | -32.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 188 | -0.195 | -30.60€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 185 | -0.243 | -22.54€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 158 | -0.256 | -26.63€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 120 | -0.213 | +12.64€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 106 | -0.213 | +9.58€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 452 | -0.223 | -47.64€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 187 | +0.400 | +139.33€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 45 | +0.351 | +38.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 45 | +0.351 | +38.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 119 | +0.483 | +103.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 119 | +0.483 | +103.58€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#sniper | 187 | +0.400 | +139.33€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 382 | +0.031 | +9.88€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 382 | +0.031 | +9.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 168 | +0.035 | +2.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 168 | +0.035 | +2.52€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 44 | -0.022 | -4.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 44 | -0.022 | -4.10€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 145 | +0.031 | +8.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 145 | +0.031 | +8.17€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 2398 | -0.024 | -105.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2398 | -0.024 | -105.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 562 | -0.023 | -23.39€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 562 | -0.023 | -23.39€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 152 | -0.045 | -14.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 152 | -0.045 | -14.43€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 880 | -0.026 | -40.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 880 | -0.026 | -40.30€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 57 | -0.042 | -3.50€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 57 | -0.042 | -3.50€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 22 | +0.042 | +0.45€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 22 | +0.042 | +0.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6355 | +0.022 | +88.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6355 | +0.022 | +88.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2031 | +0.020 | +18.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2031 | +0.020 | +18.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1325 | +0.029 | +33.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1325 | +0.029 | +33.03€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1859 | +0.014 | +4.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1859 | +0.014 | +4.79€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1140 | +0.030 | +31.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1140 | +0.030 | +31.53€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5897 | +0.012 | -33.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5897 | +0.012 | -33.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2335 | +0.019 | +1.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2335 | +0.019 | +1.26€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2340 | +0.014 | -9.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2340 | +0.014 | -9.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1222 | -0.006 | -25.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1222 | -0.006 | -25.62€ | 2 | 0 |
| ✅ UPDOWN_GBM | 25021 | +0.029 | +1386.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 6687 | +0.058 | +1064.74€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 939 | +0.005 | +9.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 15800 | +0.023 | +319.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1492 | -0.006 | -10.76€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2186 | +0.073 | +213.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 273 | +0.122 | +84.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1894 | +0.067 | +129.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4460 | +0.032 | +299.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 801 | +0.084 | +189.54€ | 0 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 267 | +0.024 | +7.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2692 | +0.027 | +97.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 661 | -0.001 | +3.43€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 39 | -0.110 | +1.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2974 | +0.032 | +93.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 229 | +0.106 | +55.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2729 | +0.026 | +39.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 5072 | +0.016 | +202.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1841 | +0.044 | +197.28€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 254 | +0.008 | +8.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2407 | +0.004 | +1.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 536 | -0.011 | -9.18€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 34 | -0.139 | +4.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6527 | +0.016 | +149.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1797 | +0.023 | +103.31€ | 1 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 248 | -0.008 | -2.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4159 | +0.017 | +53.40€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 295 | -0.008 | -5.01€ | 1 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 28 | -0.133 | -0.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3800 | +0.041 | +430.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1746 | +0.080 | +434.88€ | 0 | 13 |
| ✅ UPDOWN_GBM#XRP#240min | 135 | -0.011 | -3.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1919 | +0.010 | -1.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 101 | -0.131 | +6.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 406 | +0.333 | +112.43€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 406 | +0.333 | +112.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 227 | +0.334 | +57.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 227 | +0.334 | +57.71€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 179 | +0.329 | +54.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 179 | +0.329 | +54.72€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 8919 | -0.049 | +1845.38€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 8919 | -0.049 | +1845.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 403 | -0.053 | +344.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 403 | -0.053 | +344.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1707 | -0.130 | -11.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1707 | -0.130 | -11.12€ | 4 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 967 | +0.191 | +544.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 967 | +0.191 | +544.36€ | 2 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2865 | -0.062 | +446.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2865 | -0.062 | +446.18€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2838 | -0.077 | +466.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2838 | -0.077 | +466.65€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 97 | +0.056 | +8.36€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 97 | +0.056 | +8.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 97 | +0.056 | +8.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 97 | +0.056 | +8.36€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 692 | +0.284 | +554.16€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 692 | +0.284 | +554.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 385 | +0.275 | +291.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 385 | +0.275 | +291.93€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 307 | +0.293 | +262.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 307 | +0.293 | +262.23€ | 0 | 12 |
| ✅ UPDOWN_OU_5M | 686 | -0.109 | -80.31€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 686 | -0.109 | -80.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 184 | -0.070 | -12.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 184 | -0.070 | -12.11€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 66 | -0.176 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 66 | -0.176 | -10.12€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1900 | +0.303 | +968.74€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 633 | +0.246 | +100.73€ | 1 | 3 |
| ✅ WEEKLY_PRICE#ETH | 677 | +0.292 | +271.01€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 590 | +0.375 | +597.00€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.028 n=360 — no justifica filtro, seguir monitorizando
  - _Datos_: n=360 IC=+0.028 PNL=+22.59€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 451 celda(s) pasan gate riguroso completo de 2040 evaluadas (n>=40) y 3000 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.023 < 0.08 — monitorear
  - _Datos_: n=1796 IC=+0.023 PNL=+103.87€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=677/15 IC=+0.292 PNL=+271.01€ | BTC: n=633/15 IC=+0.246 PNL=+100.73€ | SOL: n=590/15 IC=+0.375 PNL=+597.00€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.097 n=179/60 | contraria IC=+0.123 n=160 | gap=-0.027 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=237, boost estimado=+0.005. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=536/40 IC=-0.011 PNL=-9.18€ | BTC#60min: n=661/40 IC=-0.001 PNL=+3.43€ | SOL#60min: n=295/40 IC=-0.008 PNL=-5.01€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.053 n=257773 | tras_1loss IC=+0.071 n=201557 | tras_2loss IC=+0.039 n=86398/40 | gap=+0.014 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.195 > 0.08 con n=195 PNL=+141.78€
  - _Datos_: n=195 IC=+0.195 PNL=+141.78€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.08 con n=261 PNL=+169.82€
  - _Datos_: n=261 IC=+0.200 PNL=+169.82€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.342 > 0.1 con n=1591 PNL=+956.85€
  - _Datos_: n=1591 IC=+0.342 PNL=+956.85€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=189 IC=+0.076 PNL=+25.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=189 IC=+0.076 PNL=+25.67€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=44 IC=+0.196 PNL=+30.53€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=44 IC=+0.196 PNL=+30.53€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=1091 IC=-0.006 PNL=-16.17€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1091 IC=-0.006 PNL=-16.17€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=401 IC=-0.006 PNL=+5.41€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=401 IC=-0.006 PNL=+5.41€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=360 IC=+0.028 PNL=+22.59€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=360 IC=+0.028 PNL=+22.59€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.1 con n=1414 PNL=+799.40€
  - _Datos_: n=1414 IC=+0.172 PNL=+799.40€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=801 IC=+0.084 PNL=+189.54€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=801 IC=+0.084 PNL=+189.54€

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
  - _Estado_: n=375 IC=+0.017 PNL=+29.14€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=375 IC=+0.017 PNL=+29.14€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=26 IC=+0.000 PNL=-0.58€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=26 IC=+0.000 PNL=-0.58€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.250 n=66) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=66 IC=+0.250 PNL=+42.94€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=555 PNL=+224.02€
  - _Datos_: n=555 IC=+0.128 PNL=+224.02€

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
  - _Estado_: n=8087 IC=+0.049 PNL=+915.99€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=8087 IC=+0.049 PNL=+915.99€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.153 < -0.1 con n=148 PNL=+12.69€
  - _Datos_: n=148 IC=-0.153 PNL=+12.69€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1339 IC=+0.049 PNL=+161.87€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1339 IC=+0.049 PNL=+161.87€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.1 con n=257 PNL=+83.67€
  - _Datos_: n=257 IC=+0.141 PNL=+83.67€

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
  - _Estado_: n=13395 IC=-0.143 PNL=+612.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13395 IC=-0.143 PNL=+612.04€

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
  - _Estado_: n=1485 IC=+0.141 PNL=+806.49€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1485 IC=+0.141 PNL=+806.49€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2540 IC=+0.015 PNL=+61.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2540 IC=+0.015 PNL=+61.82€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.082 > 0.08 con n=1541 PNL=+800.36€
  - _Datos_: n=1541 IC=+0.082 PNL=+800.36€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.240 < -0.1 con n=1360 PNL=-177.57€
  - _Datos_: n=1360 IC=-0.240 PNL=-177.57€

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
  - _Estado_: 27/40 ops en el filtro definido (IC actual=+0.017 PNL=+6.66€)
  - _Datos_: n=27 IC=+0.017 PNL=+6.66€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=713) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=713 IC=+0.099 PNL=+186.32€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=380) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=380 IC=+0.414 PNL=+531.98€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=6952 IC=+0.170 PNL=-882.65€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6952 IC=+0.170 PNL=-882.65€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.1 con n=105 PNL=+68.10€
  - _Datos_: n=105 IC=+0.220 PNL=+68.10€
