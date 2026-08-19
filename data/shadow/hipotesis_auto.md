# Hipótesis automáticas — 2026-08-19 03:49 UTC
_Generado por shadow_postmortem.py sobre 71462 resoluciones (PNL=+7044.88€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.355` → IC=-0.143 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=149)

- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.181 (n=164)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=210)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.080)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.080)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.080)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.137 (n=210)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.016)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=82)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.338 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=109)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.091)

- **PATRÓN** `n_total_lado` > `94.0` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 94.0 (IC base=+0.091)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=109)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.007)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=84)

- **FILTRO** `banda_hit_calibrado` < `0.6267` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6267
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=74)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=85)

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

- **PATRÓN** `py_entrada` > `0.33` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.33 (IC base=+0.068)

- **PATRÓN** `banda_hit_calibrado` > `0.6267` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `banda_hit_calibrado` > 0.6267 (IC base=+0.068)

- **PATRÓN** `banda_z` > `8.673` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.673 (IC base=+0.068)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=85)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.068)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `154.57` → IC=-0.247 (n=957)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.57
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2874)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `119.48` → IC=-0.404 (n=102)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.48
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=307)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `641.37` → IC=-0.290 (n=117)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 641.37
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=353)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `13.79` → IC=-0.492 (n=127)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 13.79
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=259)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `concentracion_yes` < `1.0` → IC=-0.121 (n=64)

  - _Acción_: SKIP cuando `concentracion_yes` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=871)

- **FILTRO** `n_ballenas` < `4.0` → IC=-0.148 (n=225)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=710)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `177.08` → IC=-0.284 (n=248)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 177.08
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=506)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=2422)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.090)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=1177)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2373.5135` → IC=+0.168 (n=1138)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2373.5135 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.158 (n=4050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=2985)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=2047)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `4054.8773` → IC=+0.183 (n=833)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4054.8773 (IC base=+0.153)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.365 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.302 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.158 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 15.0 (IC base=+0.130)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.143 (n=427)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` > 0.555 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.203 (n=163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.222 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `5296.1268` → IC=+0.174 (n=210)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5296.1268 (IC base=+0.142)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.143 (n=471)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 11.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.297 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.315 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.402 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.301 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.299)

- **PATRÓN** `libro_liquidez` > `3334.5877` → IC=+0.356 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3334.5877 (IC base=+0.299)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.173 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 16.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.245 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=275)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2169.3562` → IC=+0.169 (n=273)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2169.3562 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.121 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `5700.7138` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5700.7138 (IC base=+0.099)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.397 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.276 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` < `0.31` → IC=+0.344 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.31 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `905.8814` → IC=+0.248 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 905.8814 (IC base=+0.231)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.256 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.197 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 13.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=258)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.114)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=65)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=96)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.195 (n=1206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.201 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.163 (n=609)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.173 (n=616)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.155)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=27)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.186 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 7.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.186 (n=234)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.7 (IC base=+0.157)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=407)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.320 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.217)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.199 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.187 (n=515)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.72 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.429 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.417 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.410)

- **PATRÓN** `libro_liquidez` > `3351.8902` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3351.8902 (IC base=+0.410)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.413 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.407 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.435 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.406)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.417 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.386)

- **PATRÓN** `py_entrada` < `0.91` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.91 (IC base=+0.386)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.386)

- **PATRÓN** `libro_liquidez` > `2004.8341` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2004.8341 (IC base=+0.386)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.411)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.411)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=1779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=3271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.225 (n=3399)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `py_entrada` > `0.73` → IC=+0.134 (n=446)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.73 (IC base=+0.094)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.298 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.325 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.243)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.171 (n=396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.224 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.155)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=777)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.298 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.256 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.280 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.244)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.189 (n=548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.241 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.225 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.148)

- **PATRÓN** `restante_min` < `3.8` → IC=+0.163 (n=580)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` < 3.8 (IC base=+0.148)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.208 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.154 (n=1592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.155 (n=1742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.148)

- **PATRÓN** `lag_apertura_s` < `5.53` → IC=+0.213 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.53 (IC base=+0.148)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.241 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.154)

- **PATRÓN** `restante_min` < `3.73` → IC=+0.169 (n=285)

  - _Acción_: Kelly boost +0.84€ cuando `restante_min` < 3.73 (IC base=+0.154)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.193 (n=311)

  - _Acción_: Kelly boost +0.97€ cuando `restante_min` > 4.88 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `lag_apertura_s` < `7.0` → IC=+0.197 (n=285)

  - _Acción_: Kelly boost +0.98€ cuando `lag_apertura_s` < 7.0 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.207 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.142)

- **PATRÓN** `restante_min` < `3.9` → IC=+0.150 (n=295)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` < 3.9 (IC base=+0.142)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.224 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=884)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.142)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.222 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.28 (IC base=+0.142)

- **PATRÓN** `profundidad_ratio_no` > `11.0` → IC=+0.153 (n=295)

  - _Acción_: Kelly boost +0.77€ cuando `profundidad_ratio_no` > 11.0 (IC base=+0.142)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.312 (n=434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.313 (n=426)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.386 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.288 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.275)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.280 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.275)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.287 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.275)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `5580.6846` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5580.6846 (IC base=+0.275)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.312 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.319 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.302)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.399 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.304 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `1873.4324` → IC=+0.314 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1873.4324 (IC base=+0.302)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.446 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.377)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.377)

- **PATRÓN** `libro_liquidez` > `909.4383` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 909.4383 (IC base=+0.377)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.410 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.433 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.413 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.430 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.407 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `1957.89` → IC=+0.420 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.89 (IC base=+0.409)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.402 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.405)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.417 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.405)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.420 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.405)

- **PATRÓN** `libro_liquidez` > `5849.2071` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5849.2071 (IC base=+0.405)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.414 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.417 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.414)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.415 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.414)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.429 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.414)

- **PATRÓN** `libro_liquidez` > `1965.9066` → IC=+0.444 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1965.9066 (IC base=+0.414)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.278 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.387 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1397.8324` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1397.8324 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.278 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.387 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1397.8324` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1397.8324 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.138 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.269 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.4219` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4219 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.694` → IC=+0.237 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.694 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.2802` → IC=+0.248 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2802 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.6468` → IC=+0.242 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6468 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.6642` → IC=+0.122 (n=2216)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6642 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.2421` → IC=+0.140 (n=586)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2421 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `1.3132` → IC=+0.138 (n=500)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.3132 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `0.6966` → IC=+0.139 (n=447)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6966 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.3324` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3324 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.5637` → IC=+0.259 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5637 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.8655` → IC=+0.233 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8655 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `244.0` → IC=+0.269 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 244.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.170 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.007 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.195 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.9216` → IC=+0.280 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9216 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.471` → IC=+0.347 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.471 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.157 (n=307)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.06 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.315 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.329 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1333` → IC=+0.344 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1333 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.288 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.296 (n=199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.5701` → IC=+0.331 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5701 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.2422` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2422 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.8119` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8119 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.335 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1915.807` → IC=+0.317 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.807 (IC base=+0.286)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.340 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.264)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.289 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.311 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` > `0.917` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.917 (IC base=+0.264)

- **PATRÓN** `dist_vwap_pct` > `0.1937` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1937 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.529` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.529 (IC base=+0.264)

- **PATRÓN** `volumen_regimen` < `1.3738` → IC=+0.289 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3738 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` < `0.1838` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1838 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `2.7035` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7035 (IC base=+0.264)

- **PATRÓN** `libro_liquidez` > `13015.3205` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13015.3205 (IC base=+0.264)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.174 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0018 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.149 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0029 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1881` → IC=+0.174 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1881 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.185 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 12.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.4755` → IC=+0.206 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4755 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1392` → IC=+0.163 (n=265)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1392 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.439` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.439 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.3019` → IC=+0.161 (n=246)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.3019 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6842` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6842 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.1879` → IC=+0.190 (n=143)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1879 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1063` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1063 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.6686` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6686 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.4754` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4754 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `12624.5033` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 12624.5033 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 235.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.167 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0075 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0628` → IC=+0.136 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.0628 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.207 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.924` → IC=+0.292 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.924 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.144 (n=419)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.06 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.345 (n=82)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.286 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.309 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.289 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.293 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.5011` → IC=+0.313 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5011 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.071` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.071 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.4259` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4259 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `4.6682` → IC=+0.272 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.6682 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.9495` → IC=+0.271 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9495 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.289 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.285)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.149 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.050)

- **PATRÓN** `ibs_20min` > `0.772` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.772 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.896` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.896 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.0972` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.0972 (IC base=-0.018)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` < `2.8678` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.8678
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.190 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0055 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `23.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 23.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.375` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.375 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2651.9196` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2651.9196 (IC base=+0.115)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.176` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 8.176 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1873` → IC=+0.224 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1873 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6986 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.1434` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1434 (IC base=+0.032)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.234 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.3584` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3584 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.215` → IC=+0.128 (n=1031)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.215 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.3377` → IC=+0.200 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3377 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.2069` → IC=+0.155 (n=453)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.2069 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.240 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.167 (n=879)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.4957` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4957 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `1.2602` → IC=+0.221 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2602 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.3516` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3516 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `3.7394` → IC=+0.315 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7394 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.308 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 68.0 (IC base=+0.050)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.003` → IC=-0.213 (n=106)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.003
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=540)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.382` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 3.382 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0503` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0503 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.3584` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.3584 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` < `0.0555` → IC=-0.156 (n=88)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0555
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=265)

- **PATRÓN** `volumen_regimen` < `1.164` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.164 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5727 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.1352` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1352 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.293 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0614` → IC=+0.213 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0614 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.248 (n=165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.958` → IC=+0.305 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.958 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` < `0.1441` → IC=+0.183 (n=257)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1441 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `3.8997` → IC=+0.203 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.8997 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.194 (n=390)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.06 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `1915.1184` → IC=+0.213 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.1184 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.411 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.370)

- **PATRÓN** `drift_60min` |x|≤ `0.1806` → IC=+0.376 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1806 (IC base=+0.370)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.397 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.370)

- **PATRÓN** `ibs_20min` < `0.3056` → IC=+0.381 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3056 (IC base=+0.370)

- **PATRÓN** `ibs_20min` > `0.0506` → IC=+0.367 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0506 (IC base=+0.370)

- **PATRÓN** `volumen_pendiente_norm` < `0.3211` → IC=+0.399 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3211 (IC base=+0.370)

- **PATRÓN** `volumen_spike_ratio` < `2.9702` → IC=+0.442 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9702 (IC base=+0.370)

- **PATRÓN** `libro_liquidez` > `1873.0784` → IC=+0.414 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1873.0784 (IC base=+0.370)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.6296` → IC=-0.126 (n=161)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6296
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=84)

- **FILTRO** `dist_vwap_pct` < `0.3632` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3632
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

- **FILTRO** `volumen_regimen` > `0.8629` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8629
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **FILTRO** `libro_liquidez` < `8612.4997` → IC=-0.214 (n=61)

  - _Acción_: SKIP cuando `libro_liquidez` < 8612.4997
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=184)

- **FILTRO** `volumen_regimen` > `0.7318` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.7318
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=708)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.45` → IC=-0.153 (n=148)

  - _Acción_: SKIP cuando `ibs_20min` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=149)

- **FILTRO** `dist_vwap_pct` > `0.1358` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1358
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **PATRÓN** `ibs_20min` > `0.45` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.45 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.1779` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1779 (IC base=-0.012)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.298 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1375` → IC=+0.150 (n=204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1375 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.212 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.227 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3235` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3235 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.128` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.128 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.5938` → IC=+0.151 (n=305)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.5938 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.3138` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3138 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.1451` → IC=+0.131 (n=166)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.1451 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=309)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2467.4755` → IC=+0.140 (n=273)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2467.4755 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.296 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.329 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.32` → IC=+0.331 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.32 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.5418` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5418 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.5` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.5 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.927` → IC=+0.286 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.927 (IC base=+0.283)

- **PATRÓN** `volumen_regimen` > `0.8948` → IC=+0.322 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8948 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `3.5418` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5418 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.283)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.158 (n=436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0047 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.192 (n=595)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0066 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0928` → IC=+0.141 (n=575)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.0928 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=443)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.9198` → IC=+0.254 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9198 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.153 (n=384)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.948` → IC=+0.269 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.948 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.1848` → IC=+0.145 (n=679)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1848 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.142 (n=679)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6297 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1112` → IC=+0.156 (n=443)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1112 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.146 (n=1473)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.06 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2708.1108` → IC=+0.178 (n=436)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2708.1108 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.218 (n=1276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.234` → IC=+0.219 (n=1123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.234 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.257 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.277 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.6` → IC=+0.236 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.6 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2517` → IC=+0.187 (n=988)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.2517 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8747` → IC=+0.197 (n=658)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.8747 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3231` → IC=+0.269 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3231 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.5489` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5489 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `3.1445` → IC=+0.244 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1445 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.266 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.212)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.161 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.207 (n=148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.230 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.8777` → IC=+0.285 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8777 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.572` → IC=+0.373 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.572 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1492` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.1492 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.186 (n=253)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.295 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.308 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.2156` → IC=+0.326 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2156 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.314 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.4177` → IC=+0.325 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4177 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.2061` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2061 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.9432` → IC=+0.382 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9432 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.376 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1962.999` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1962.999 (IC base=+0.290)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.002` → IC=+0.284 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.219)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.269 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.273 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.8703` → IC=+0.278 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8703 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1472` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1472 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.06` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.06 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.3738` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3738 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.9086` → IC=+0.230 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9086 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.4774` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4774 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.0183` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0183 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `11869.8733` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11869.8733 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.207 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.184 (n=213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.002 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1925` → IC=+0.206 (n=209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1925 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.301` → IC=+0.233 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.301 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.411` → IC=+0.259 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.411 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.6405` → IC=+0.232 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6405 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.1952` → IC=+0.202 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1952 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1417` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1417 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.6478` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6478 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `12480.3954` → IC=+0.216 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12480.3954 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.189 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0076 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1453` → IC=+0.154 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1453 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.207 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.2311` → IC=+0.127 (n=242)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.2311 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.0095` → IC=+0.206 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0095 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `3.8668` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 3.8668 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.174 (n=234)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.04 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `1970.881` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1970.881 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 27.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.333 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.308)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.308 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.308)

- **PATRÓN** `drift_60min` |x|≤ `0.1618` → IC=+0.349 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1618 (IC base=+0.308)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.321 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.308)

- **PATRÓN** `ibs_20min` < `0.3186` → IC=+0.328 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3186 (IC base=+0.308)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.476` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.476 (IC base=+0.308)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` < `3.1896` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.1896 (IC base=+0.308)

- **PATRÓN** `volumen_spike_ratio` > `1.9367` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9367 (IC base=+0.308)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.294 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.254 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.1718` → IC=+0.318 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1718 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.270 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `0.7234` → IC=+0.314 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7234 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` < `0.3636` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3636 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.807` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.807 (IC base=+0.250)

- **PATRÓN** `volumen_regimen` > `0.7651` → IC=+0.282 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7651 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.114` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.114 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.6992` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6992 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.4523` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4523 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `3088.7155` → IC=+0.247 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3088.7155 (IC base=+0.250)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.256 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1372` → IC=+0.199 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1372 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.227 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.332` → IC=+0.255 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.332 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.362` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.362 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.2379` → IC=+0.220 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2379 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.1745` → IC=+0.212 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1745 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.9183` → IC=+0.270 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9183 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=262)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `6338.4359` → IC=+0.192 (n=105)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6338.4359 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `195.0` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 195.0 (IC base=+0.188)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5556` → IC=-0.238 (n=82)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5556
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=251)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.179 (n=154)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.8667 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.042)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.233 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.140 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 4.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.211 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5556 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.5598` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.5598 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.905` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.905 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.8622` → IC=+0.145 (n=167)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.8622 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.1182` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1182 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.2808` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.2808 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2536.4746` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2536.4746 (IC base=+0.100)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.254 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.2124` → IC=+0.141 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2124 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.175 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.231 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.312` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.312 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.0668` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0668 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.341` → IC=+0.235 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.341 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1205` → IC=+0.143 (n=247)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1205 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6045` → IC=+0.127 (n=247)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6045 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1987` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1987 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `3.0538` → IC=+0.131 (n=212)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 3.0538 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=254)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2469.6086` → IC=+0.141 (n=221)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2469.6086 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.284 (n=239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.266 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.0777` → IC=+0.274 (n=91)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0777 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.270 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.2368` → IC=+0.317 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2368 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` > `0.2617` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2617 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.724` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.724 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.8895` → IC=+0.303 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8895 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.3468` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3468 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.7731` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7731 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `2705.0574` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2705.0574 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.260)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` > `0.9601` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9601 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.961` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.961 (IC base=+0.045)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.300 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.1667 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.859` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.859 (IC base=+0.053)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `sigma_h` > `0.0026` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `volumen_spike_ratio` > `1.77` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.77
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.261 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2468` → IC=+0.196 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.2468 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.167 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 12.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.1986` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1986 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.208` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.208 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0448` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.0448 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6181` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6181 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.6478` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6478 (IC base=+0.147)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.203 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.190 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0027 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.2558` → IC=+0.230 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2558 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.382 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.9442` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9442 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.738` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.738 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `0.9813` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9813 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.0973` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0973 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.1778` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1778 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.3331` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3331 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.9173` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9173 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `3054.5848` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3054.5848 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.375 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2298` → IC=+0.217 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2298 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.272` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.272 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.4281` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.4281 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.121` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.121 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8238` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8238 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `10039.916` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10039.916 (IC base=+0.132)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64)

- **FILTRO** `dist_vwap_pct` > `0.1911` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1911
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=69)

- **FILTRO** `volumen_pendiente_norm` > `0.1038` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1038
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=43)

- **FILTRO** `libro_liquidez` < `2021.654` → IC=-0.182 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 2021.654
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=43)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.027)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 1.0 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.14` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 8.14 (IC base=+0.027)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.200 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.7714` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.7714 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.034` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.034 (IC base=+0.064)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.082` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.082 (IC base=+0.037)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.198 (n=527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0068 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.9626` → IC=+0.281 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9626 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.3549` → IC=+0.185 (n=179)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3549 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.252` → IC=+0.233 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.252 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.1822` → IC=+0.136 (n=374)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.1822 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.6912` → IC=+0.121 (n=1134)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.6912 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.125 (n=1766)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.06 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2754.3868` → IC=+0.151 (n=526)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2754.3868 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.182 (n=199)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 152.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.232 (n=1257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.227 (n=1424)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.235 (n=1275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.284 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.1545` → IC=+0.194 (n=934)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1545 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.019` → IC=+0.255 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.019 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.47` → IC=+0.224 (n=1336)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.47 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `0.6189` → IC=+0.204 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6189 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `1.229` → IC=+0.218 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.229 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.114` → IC=+0.243 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.114 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2523` → IC=+0.267 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2523 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.0261` → IC=+0.265 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0261 (IC base=+0.222)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.214 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.163 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.286 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.193` → IC=+0.354 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.193 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2113` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2113 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.163 (n=289)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.06 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.324 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.298)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.321 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.2108` → IC=+0.340 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2108 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.307 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.309 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.338 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5758 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.340 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` > `0.248` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.248 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` < `1.9246` → IC=+0.336 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9246 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `2.42` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.42 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.332 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `1980.3` → IC=+0.366 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1980.3 (IC base=+0.298)

### GBM_LATE_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_20min` < `0.3061` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3061
  - _Potencial_: sin este filtro IC_bueno=+0.240 (n=156)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.164 (n=105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0026 (IC base=+0.129)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.158 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0031 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.286 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.3061` → IC=+0.240 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3061 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.2615` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2615 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.779` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.779 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6746` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6746 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `0.9222` → IC=+0.151 (n=104)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.9222 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1584` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1584 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.8608` → IC=+0.226 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8608 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `11341.8291` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11341.8291 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.207 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.185 (n=211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.4082` → IC=+0.223 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4082 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.1415` → IC=+0.187 (n=260)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1415 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.258` → IC=+0.252 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.258 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.3065` → IC=+0.182 (n=240)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.3065 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.8593` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.8593 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1081` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1081 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.6006` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6006 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `5211.9825` → IC=+0.185 (n=214)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 5211.9825 (IC base=+0.173)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.241 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.242 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.311 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` < `0.2327` → IC=+0.167 (n=247)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.2327 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `2.1812` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1812 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `4.9893` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 4.9893 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.188 (n=344)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.06 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `1854.561` → IC=+0.185 (n=211)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1854.561 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.357 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.277 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.300 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.336 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5455 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.123` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.123 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` < `0.1603` → IC=+0.231 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1603 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.378` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.378 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `3.6802` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.6802 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.270)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 35.0 (IC base=+0.270)

### GBM_LATE_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_20min` < `0.3643` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3643
  - _Potencial_: sin este filtro IC_bueno=+0.207 (n=162)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.196 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0019 (IC base=+0.099)

- **PATRÓN** `drift_60min` |x|≤ `0.0759` → IC=+0.130 (n=71)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.0759 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.3643` → IC=+0.207 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3643 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.435` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.435 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `0.7845` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.7845 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `1.9911` → IC=+0.242 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9911 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `7283.8545` → IC=+0.250 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7283.8545 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.232 (n=121)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0843` → IC=+0.179 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0843 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.1347` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1347 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2052` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2052 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.492` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.492 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.0537` → IC=+0.191 (n=121)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.0537 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.1407` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1407 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.797` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.797 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `7420.3777` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7420.3777 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=+0.163)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.223 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.019)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.206 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1714` → IC=+0.159 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1714 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.220 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1781` → IC=+0.151 (n=187)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1781 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.399` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.399 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.16` → IC=+0.138 (n=216)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.16 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.197 (n=107)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.7028 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.0794` → IC=+0.152 (n=110)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0794 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` < `0.1081` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1081 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.9831` → IC=+0.276 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9831 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.7285` → IC=+0.253 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7285 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `1421.853` → IC=+0.223 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1421.853 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.197 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0063 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.195 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.184 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.3315` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3315 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.298` → IC=+0.223 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.298 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.6734` → IC=+0.143 (n=275)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6734 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1933` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1933 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.7671` → IC=+0.135 (n=231)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7671 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=314)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2476.2054` → IC=+0.143 (n=275)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2476.2054 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.283 (n=362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.281 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` < `0.4091` → IC=+0.307 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4091 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.3828` → IC=+0.363 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3828 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.597` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.597 (IC base=+0.253)

- **PATRÓN** `volumen_regimen` > `0.8819` → IC=+0.293 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8819 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` < `1.5061` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5061 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `3.3179` → IC=+0.269 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3179 (IC base=+0.253)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 50.0 (IC base=+0.253)

### GBM_LATE_5M
- **FILTRO** `sigma_h` < `0.0037` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=47)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=214)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.195 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0039 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.2655` → IC=+0.178 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2655 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.240 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.5407` → IC=+0.155 (n=172)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5407 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.1852` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.1852 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.074` → IC=+0.163 (n=158)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.074 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1834` → IC=+0.195 (n=152)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.1834 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.6763` → IC=+0.161 (n=172)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6763 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.152` → IC=+0.167 (n=163)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.152 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.8806` → IC=+0.188 (n=171)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.8806 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4793` → IC=+0.153 (n=171)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4793 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=214)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `7756.2728` → IC=+0.167 (n=172)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7756.2728 (IC base=+0.149)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.176 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0033 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.263 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.144 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.189` → IC=+0.185 (n=109)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 10.189 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.2758` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.2758 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.6649` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6649 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.2332` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2332 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.7539` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.7539 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.5051` → IC=+0.173 (n=105)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.5051 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `9877.829` → IC=+0.154 (n=105)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 9877.829 (IC base=+0.155)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.260 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.283 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.300 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.2325` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2325 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.688` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.688 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.809` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.809 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.5769` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.5769 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1212` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1212 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.8878` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8878 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `7268.8224` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7268.8224 (IC base=+0.223)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.161 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=111)

- **FILTRO** `drift_60min` |x|> `0.0945` → IC=-0.289 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0945
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `ibs_20min` > `0.6567` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6567
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=70)

- **FILTRO** `dist_vwap_pct` > `0.1008` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1008
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.178 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0054 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.226 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.0933` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0933 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2015.645` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2015.645 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=42)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=45)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.186 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7342 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.15` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 13.15 (IC base=+0.062)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.2012` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2012 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.41` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.41 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.5932` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.5932 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0696 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2351.5975` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2351.5975 (IC base=+0.102)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=58)

- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=-0.020)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=-0.020)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.300 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=71)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=78)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.344 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=35)

- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=73)

- **FILTRO** `dist_vwap_pct` > `0.3683` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3683
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=79)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2353` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2353
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `9.988` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 9.988
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.5333` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5333
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=101)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.149 (n=132)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6429 (IC base=+0.062)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.125 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=39)

- **PATRÓN** `ibs_20min` > `0.7184` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7184 (IC base=-0.067)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.3803` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.3803 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.84` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.84 (IC base=+0.085)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.991` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.991 (IC base=+0.174)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7333 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.03 (IC base=+0.095)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.211)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.211)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `17.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `libro_liquidez` < `1970.6128` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 1970.6128
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=75)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `libro_liquidez` < `3962.9688` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3962.9688
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=29)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=27)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9732` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9732
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=62)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=57)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2255.3349` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 2255.3349
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=24)

- **PATRÓN** `libro_liquidez` > `2255.3349` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2255.3349 (IC base=-0.020)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.200 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.127)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0647` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0647 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.1731` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.1731 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.0947` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0947 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2054.213` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2054.213 (IC base=+0.127)

### MOMENTUM_IBS_15M#BTC#15min
- **PATRÓN** `hora_utc` < `18.0` → IC=+0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 18.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.9919` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.9919 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `19045.4888` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 19045.4888 (IC base=+0.093)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.098)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0544` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0544 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.0551` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0551 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `20061.6367` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 20061.6367 (IC base=+0.098)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **FILTRO** `ibs_20min` > `0.7917` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7917
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### MOMENTUM_IBS_15M#ETH#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.140 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 18.0 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.197 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.111)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.053` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `drift_20min_pct` |x|≤ 0.053 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.0373` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.0373 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `15323.3068` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15323.3068 (IC base=+0.111)

### MOMENTUM_IBS_15M#XRP#15min
- **PATRÓN** `hora_utc` < `2.0` → IC=+0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 2.0 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.4` → IC=-0.269 (n=115)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=358)

- **FILTRO** `ibs_20min` < `0.7187` → IC=-0.231 (n=117)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7187
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=356)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.192 (n=115)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=358)

- **FILTRO** `libro_liquidez` < `1980.58` → IC=-0.137 (n=312)

  - _Acción_: SKIP cuando `libro_liquidez` < 1980.58
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=161)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.220 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=52)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=60)

- **FILTRO** `ibs_20min` < `0.8235` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8235
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=51)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 14.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.1477` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.1477 (IC base=+0.057)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=61)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=53)

- **FILTRO** `libro_liquidez` < `14841.6226` → IC=-0.167 (n=52)

  - _Acción_: SKIP cuando `libro_liquidez` < 14841.6226
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

- **FILTRO** `ibs_20min` > `0.1556` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1556
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=65)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=74)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.214 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=-0.040)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.230 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=43)

- **FILTRO** `ibs_20min` < `0.9535` → IC=-0.141 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.9535
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=59)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 16.0 (IC base=+0.056)

- **PATRÓN** `py_entrada` < `0.63` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.63 (IC base=+0.056)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=59)

- **FILTRO** `ibs_20min` < `1.0` → IC=-0.167 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=26)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=57)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.176 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.057)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.5 (IC base=+0.057)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

- **FILTRO** `ibs_20min` > `0.8333` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8333
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=59)

- **FILTRO** `ibs_20min` < `0.7302` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7302
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=66)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=66)

- **PATRÓN** `libro_liquidez` > `2275.4657` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2275.4657 (IC base=+0.011)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=104)

- **FILTRO** `hora_utc` > `19.0` → IC=-0.206 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=105)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=196)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `0.9919` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.9919
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_liquidez` < `3903.1637` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3903.1637
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=47)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.931` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.931 (IC base=+0.062)

- **PATRÓN** `libro_liquidez` > `3903.1637` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3903.1637 (IC base=+0.062)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `ibs_20min` < `0.2368` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.031)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **FILTRO** `drift_7min_pct` |x|> `0.0741` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0741
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=25)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0741` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `drift_7min_pct` |x|≤ 0.0741 (IC base=+0.000)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=74)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.033)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=38)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0611` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `drift_7min_pct` |x|≤ 0.0611 (IC base=+0.029)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33)

- **PATRÓN** `libro_liquidez` > `9401.8411` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 9401.8411 (IC base=+0.041)

### MOMENTUM_IBS_5M#SOL#5min
- **PATRÓN** `drift_7min_pct` |x|≤ `0.0658` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `drift_7min_pct` |x|≤ 0.0658 (IC base=+0.044)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `14.0` → IC=-0.162 (n=651)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=680)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.285 (n=319)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1012)

- **FILTRO** `ibs_7min` < `0.7137` → IC=-0.236 (n=332)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7137
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=999)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.200 (n=444)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=887)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.188 (n=379)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1161)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.3` → IC=-0.269 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=165)

- **FILTRO** `ibs_7min` < `0.9167` → IC=-0.192 (n=141)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9167
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=74)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.226 (n=100)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=115)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=157)

- **FILTRO** `drift_7min_pct` |x|> `0.0977` → IC=-0.153 (n=70)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0977
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=137)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.261 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=213)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.317 (n=69)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=209)

- **FILTRO** `ibs_7min` < `0.7868` → IC=-0.246 (n=69)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7868
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=209)

- **FILTRO** `ballena_activa_n` > `111.0` → IC=-0.204 (n=69)

  - _Acción_: SKIP cuando `ballena_activa_n` > 111.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=209)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.182 (n=61)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=213)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.177 (n=94)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=97)

- **FILTRO** `py_entrada` < `0.28` → IC=-0.417 (n=46)

  - _Acción_: SKIP cuando `py_entrada` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=145)

- **FILTRO** `ibs_7min` < `0.1416` → IC=-0.235 (n=47)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1416
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=144)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.271 (n=46)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.180 (n=120)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=127)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.217 (n=111)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=116)

- **FILTRO** `ibs_7min` < `0.883` → IC=-0.224 (n=74)

  - _Acción_: SKIP cuando `ibs_7min` < 0.883
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=153)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.171 (n=150)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=77)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.142 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=200)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.217 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=188)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.254 (n=59)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=187)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.169 (n=122)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=124)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.246 (n=61)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=185)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.250 (n=94)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=80)

- **FILTRO** `ibs_7min` < `0.7324` → IC=-0.297 (n=57)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7324
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=117)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.295 (n=42)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=132)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.250 (n=54)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=217)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=75)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=100)

- **PATRÓN** `libro_liquidez` > `11036.7223` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 11036.7223 (IC base=+0.064)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=210)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.162 (n=152)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.151 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 18.0 (IC base=+0.137)

- **PATRÓN** `total_vol_5m` < `303.4797` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 303.4797 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.137)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.2125` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.2125
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `pct_vs_K` |x|> `4.502` → IC=-0.470 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.502
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=63)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=-0.142)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9756` → IC=-0.426 (n=25)

  - _Acción_: SKIP cuando `T_h` > 87.9756
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `95.1632` → IC=-0.337 (n=41)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.337 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0034` → IC=-0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0033` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `T_h` > `111.9957` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 111.9957
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `sigma_h` > `0.0035` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `8.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `streak_estiramiento` > `0.4156` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4156
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `streak_estiramiento` > `0.4411` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4411
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` > `12.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=75)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.125 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 4.0 (IC base=-0.013)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=16)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=-0.011)

- **PATRÓN** `libro_liquidez` > `3678.6572` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3678.6572 (IC base=-0.011)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.241 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=38)

### STREAK_MOM_5M
- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=75)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=43)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=42)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.167 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 10.0 (IC base=+0.047)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.047)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=79)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=-0.009)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 4.0 (IC base=+0.062)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=706)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=404)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=412)

### UPDOWN_GBM#15min
- **FILTRO** `ibs_15` < `0.5833` → IC=-0.152 (n=139)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.228 (n=285)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.134 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0035 (IC base=+0.103)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.133 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0054 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.228 (n=285)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.3538` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3538 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.027` → IC=+0.231 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.027 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `4992.5513` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4992.5513 (IC base=+0.103)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.151 (n=210)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1154 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` > `0.4698` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.4698 (IC base=+0.079)

### UPDOWN_GBM#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.133 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=140)

- **FILTRO** `ibs_15` < `0.1` → IC=-0.258 (n=64)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=194)

- **FILTRO** `sigma_ewma_delta_pct` > `5.172` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.172
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=194)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=135)

- **FILTRO** `ibs_15` < `0.592` → IC=-0.183 (n=39)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.592
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=120)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0397` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0397
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `hora_utc` < `19.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.03 (IC base=+0.003)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0039` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `libro_liquidez` < `14061.5224` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 14061.5224
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.149 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0029 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.138 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.002 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.136 (n=75)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.134)

- **PATRÓN** `drift_15min` |x|≤ `0.4549` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `drift_15min` |x|≤ 0.4549 (IC base=+0.134)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0878` → IC=+0.138 (n=67)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.0878 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.167 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 3.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.9432` → IC=+0.250 (n=34)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9432 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.3789` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3789 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.945` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 6.945 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.708` → IC=+0.145 (n=74)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 18.708 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8665.5751` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8665.5751 (IC base=+0.134)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `ibs_15` < `0.1827` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1827
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `11975.2481` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 11975.2481
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0107` → IC=+0.143 (n=54)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.71€ cuando `pct_spot_vs_ref` |x|≤ 0.0107 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.002` → IC=+0.196 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.002 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.1777` → IC=+0.133 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1777 (IC base=+0.104)

- **PATRÓN** `drift_15min` |x|≤ `0.3989` → IC=+0.121 (n=122)

  - _Acción_: Kelly boost +0.60€ cuando `drift_15min` |x|≤ 0.3989 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.143 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 3.0 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.0764` → IC=+0.137 (n=122)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.69€ cuando `ibs_15` > 0.0764 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.763` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.763 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `11034.7966` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11034.7966 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.137 (n=100)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 22.0 (IC base=+0.104)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.6097` → IC=-0.265 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6097
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.7055` → IC=-0.146 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7055
  - _Potencial_: sin este filtro IC_bueno=+0.337 (n=47)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2385` → IC=+0.269 (n=24)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2385 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.7055` → IC=+0.337 (n=47)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7055 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.1005` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1005 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.100)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.154 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0032 (IC base=+0.132)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.175 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.004 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0898` → IC=+0.135 (n=113)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0898 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.141 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 14.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` < `0.345` → IC=+0.161 (n=113)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.345 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.0316` → IC=+0.170 (n=113)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.85€ cuando `ibs_15` > 0.0316 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.4566` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4566 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.395` → IC=+0.184 (n=112)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 23.395 (IC base=+0.132)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `dist_vwap_pct` > `0.1744` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1744
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=43)

- **FILTRO** `sigma_ewma_delta_pct` > `5.626` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.626
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=34)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=84)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0019 (IC base=+0.068)

- **PATRÓN** `drift_15min` |x|≤ `0.1165` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.1165 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `1.0` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 1.0 (IC base=+0.068)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `delta_ratio_macro` |x|> `0.1688` → IC=+0.156 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1688 (IC base=+0.022)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.03 (IC base=+0.022)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=29)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.242 (n=29)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.764` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.764 (IC base=+0.033)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `ibs_15` < `0.5385` → IC=-0.242 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5385
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

- **FILTRO** `dist_vwap_pct` < `0.1891` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1891
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2945` → IC=+0.125 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.2945 (IC base=+0.040)

- **PATRÓN** `ibs_15` < `0.0714` → IC=+0.210 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0714 (IC base=+0.040)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.163 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.005 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0626` → IC=+0.133 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0626 (IC base=+0.085)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.182 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.55 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.4287` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4287 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.54` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.54 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `2507.0533` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2507.0533 (IC base=+0.085)

- **PATRÓN** `drift_60min` |x|≤ `0.1049` → IC=+0.173 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1049 (IC base=+0.096)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0943` → IC=+0.157 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.0943 (IC base=+0.096)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.120 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 16.0 (IC base=+0.096)

- **PATRÓN** `ibs_15` < `0.125` → IC=+0.187 (n=65)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` < 0.125 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1093` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1093 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.469` → IC=+0.134 (n=132)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 6.469 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2604.9815` → IC=+0.149 (n=132)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2604.9815 (IC base=+0.096)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.266 (n=75)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.254)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.306 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.256 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0031 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.276 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.254)

- **PATRÓN** `drift_15min` |x|≤ `0.4081` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4081 (IC base=+0.254)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.259 (n=85)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.339 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.254)

- **PATRÓN** `ibs_15` > `0.7088` → IC=+0.314 (n=84)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7088 (IC base=+0.254)

- **PATRÓN** `dist_vwap_pct` > `0.3609` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3609 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `3208.0074` → IC=+0.269 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3208.0074 (IC base=+0.254)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.269 (n=50)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.254 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.245 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.220)

- **PATRÓN** `drift_15min` |x|≤ `0.6305` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6305 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.254 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.217 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` < `0.9942` → IC=+0.219 (n=55)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9942 (IC base=+0.220)

- **PATRÓN** `ibs_15` > `0.7314` → IC=+0.254 (n=55)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7314 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.3075` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3075 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.744` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.744 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `7152.8647` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7152.8647 (IC base=+0.220)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `dist_vwap_pct` < `0.058` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.058 (IC base=+0.305)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.414` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.414 (IC base=+0.305)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.6522` → IC=-0.244 (n=119)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6522
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=119)

- **FILTRO** `sigma_ewma_delta_pct` > `12.785` → IC=-0.155 (n=236)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.785
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=961)

- **PATRÓN** `ibs_15` > `0.6522` → IC=+0.244 (n=119)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6522 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.53` → IC=+0.271 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.53 (IC base=-0.053)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.0929 (IC base=-0.053)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0033` → IC=-0.211 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=171)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.241 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=176)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.224 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.121 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.043)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `sigma_h` > `0.0047` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=68)

- **FILTRO** `drift_60min` |x|> `0.2078` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2078
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=68)

- **FILTRO** `ibs_15` < `0.5408` → IC=-0.372 (n=45)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5408
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=45)

- **PATRÓN** `ibs_15` > `0.5408` → IC=+0.202 (n=45)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5408 (IC base=-0.087)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1184` → IC=+0.219 (n=30)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1184 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0045 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1816` → IC=+0.180 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1816 (IC base=+0.181)

- **PATRÓN** `drift_15min` |x|≤ `0.6645` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `drift_15min` |x|≤ 0.6645 (IC base=+0.181)

- **PATRÓN** `ibs_15` < `0.3879` → IC=+0.312 (n=30)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3879 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.307` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.307 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `3786.4324` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3786.4324 (IC base=+0.181)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `13.905` → IC=-0.187 (n=65)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.905
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=369)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.659` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.659 (IC base=-0.015)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.154 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=53)

- **FILTRO** `libro_liquidez` < `2491.4834` → IC=-0.207 (n=39)

  - _Acción_: SKIP cuando `libro_liquidez` < 2491.4834
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

- **FILTRO** `sigma_ewma_delta_pct` > `7.734` → IC=-0.153 (n=93)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.734
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=298)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1826` → IC=+0.267 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1826 (IC base=+0.258)

- **PATRÓN** `drift_15min` |x|≤ `0.5899` → IC=+0.265 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5899 (IC base=+0.258)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0656` → IC=+0.276 (n=114)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0656 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.292 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.258)

- **PATRÓN** `ibs_15` > `0.9358` → IC=+0.333 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9358 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` > `0.3763` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3763 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` < `0.0834` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0834 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.952` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.952 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `10246.118` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10246.118 (IC base=+0.258)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2` → IC=+0.278 (n=70)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2 (IC base=+0.245)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.250 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.266 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0021 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1873` → IC=+0.278 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1873 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.6581` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6581 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0878` → IC=+0.250 (n=62)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0878 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.284 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` > `0.8845` → IC=+0.281 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8845 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` < `0.0994` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0994 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.501` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.501 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.495` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.495 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `8349.505` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8349.505 (IC base=+0.245)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.309 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `0.4139` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4139 (IC base=+0.271)

- **PATRÓN** `delta_ratio_macro` |x|> `0.177` → IC=+0.370 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.177 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.271)

- **PATRÓN** `ibs_15` > `0.9731` → IC=+0.413 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9731 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.0728` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0728 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.209` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 16.209 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `9700.4747` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9700.4747 (IC base=+0.271)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0492` → IC=-0.167 (n=22)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0492
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `drift_60min` |x|> `0.1447` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1447
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `drift_15min` |x|> `0.3418` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3418
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.151 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=247)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.237 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.278 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0045` → IC=-0.289 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `111.9997` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `T_h` < 111.9997 (IC base=+0.021)

- **PATRÓN** `T_h` > `146.1132` → IC=+0.453 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.352)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `100.962` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 100.962 (IC base=+0.276)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.276)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9838` → IC=+0.320 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.314)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1359` → IC=+0.457 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1359 (IC base=+0.425)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.0714 sube el IC de +0.040 a +0.210 en UPDOWN_GBM#SOL#5min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.103 a +0.228 en UPDOWN_GBM#15min (n=285). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_NO, IBS < 0.1154 sube el IC de +0.079 a +0.151 en UPDOWN_GBM#15min (n=210). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9432 sube el IC de +0.134 a +0.250 en UPDOWN_GBM#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.7055 sube el IC de +0.100 a +0.337 en UPDOWN_GBM#ETH#15min (n=47). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.345 sube el IC de +0.132 a +0.161 en UPDOWN_GBM#ETH#15min (n=113). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS > 0.0316 sube el IC de +0.132 a +0.170 en UPDOWN_GBM#ETH#15min (n=113). Ya aplicado como kelly_boost=+0.85€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.085 a +0.182 en UPDOWN_GBM#XRP#15min (n=86). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.125 sube el IC de +0.096 a +0.187 en UPDOWN_GBM#XRP#15min (n=65). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6522 sube el IC de -0.044 a +0.244 en UPDOWN_GBM_15M_TARDIO (n=119). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.53 sube el IC de -0.053 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=46). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5408 sube el IC de -0.087 a +0.202 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=45). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3879 sube el IC de +0.181 a +0.312 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9358 sube el IC de +0.258 a +0.333 en UPDOWN_GBM_IBS_ALTO (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8845 sube el IC de +0.245 a +0.281 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.9731 sube el IC de +0.271 a +0.413 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7088 sube el IC de +0.254 a +0.314 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9942 sube el IC de +0.220 a +0.219 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7314 sube el IC de +0.220 a +0.254 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.305 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.305 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#BNB#5min` — IC=+0.219 n=30. Faltan ~10 resoluciones para umbral n≥40. ETA: ~7h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#BNB` — IC=+0.219 n=30. Faltan ~10 resoluciones para umbral n≥40. ETA: ~7h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 490 | +0.045 | +37.59€ | 3 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 490 | +0.045 | +37.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 252 | +0.043 | +24.96€ | 2 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 210 | +0.024 | -0.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 210 | +0.024 | -0.34€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 28 | +0.200 | +12.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 28 | +0.200 | +12.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3552 | -0.115 | -560.91€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 470 | -0.025 | -21.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 3082 | -0.128 | -539.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 409 | -0.189 | -91.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 409 | -0.189 | -91.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 470 | -0.025 | -21.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 470 | -0.025 | -21.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 317 | -0.152 | -148.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 317 | -0.152 | -148.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 877 | +0.003 | -114.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 877 | +0.003 | -114.85€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 754 | -0.228 | -146.54€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 754 | -0.228 | -146.54€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 15245 | +0.114 | -903.72€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3501 | +0.183 | -98.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 100 | -0.098 | -46.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 9021 | +0.085 | -790.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2623 | +0.133 | +32.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1522 | +0.028 | -341.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 14 | -0.044 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1504 | +0.030 | -335.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3432 | +0.140 | -5.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 957 | +0.200 | -27.94€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 41 | -0.105 | -20.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1502 | +0.110 | -19.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 932 | +0.138 | +62.21€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1519 | +0.057 | -259.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 10 | +0.000 | -3.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1508 | +0.058 | -254.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3711 | +0.126 | -39.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1292 | +0.162 | -15.33€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1499 | +0.103 | -23.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 908 | +0.119 | +7.70€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3543 | +0.136 | -204.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1216 | +0.197 | -53.84€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 41 | +0.012 | -8.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1503 | +0.085 | -104.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 783 | +0.143 | -37.72€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1518 | +0.120 | -53.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1505 | +0.121 | -53.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3562 | +0.160 | -348.48€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3562 | +0.160 | -348.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 891 | +0.155 | -115.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 891 | +0.155 | -115.86€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 78 | -0.113 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 78 | -0.113 | -5.72€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 884 | +0.157 | -113.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 884 | +0.157 | -113.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 792 | +0.217 | -44.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 792 | +0.217 | -44.87€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 838 | +0.173 | -82.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 838 | +0.173 | -82.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 175 | +0.410 | -11.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 175 | +0.410 | -11.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 62 | +0.406 | -3.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 62 | +0.406 | -3.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 68 | +0.386 | -6.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 68 | +0.386 | -6.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 43 | +0.411 | -1.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 43 | +0.411 | -1.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 6414 | +0.186 | -628.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 6414 | +0.186 | -628.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1200 | +0.094 | -276.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1200 | +0.094 | -276.51€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 986 | +0.243 | -16.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 986 | +0.243 | -16.99€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1124 | +0.155 | -158.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1124 | +0.155 | -158.92€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1029 | +0.222 | -43.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1029 | +0.222 | -43.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 998 | +0.244 | -14.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 998 | +0.244 | -14.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1077 | +0.179 | -118.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1077 | +0.179 | -118.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2309 | +0.148 | +124.37€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 2309 | +0.148 | +124.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1139 | +0.154 | +73.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1139 | +0.154 | +73.08€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1170 | +0.142 | +51.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1170 | +0.142 | +51.29€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 547 | +0.301 | +6.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 547 | +0.301 | +6.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 229 | +0.275 | -8.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 229 | +0.275 | -8.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 255 | +0.302 | +7.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 255 | +0.302 | +7.49€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 63 | +0.377 | +7.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 63 | +0.377 | +7.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 230 | +0.409 | -10.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 230 | +0.409 | -10.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 103 | +0.405 | -5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 103 | +0.405 | -5.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 103 | +0.414 | -5.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 103 | +0.414 | -5.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 259 | +0.259 | -31.08€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 259 | +0.259 | -31.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 259 | +0.259 | -31.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 259 | +0.259 | -31.08€ | 0 | 4 |
| ✅ GBM_LATE_15M | 4693 | +0.085 | +1660.91€ | 0 | 14 |
| ✅ GBM_LATE_15M#15min | 4693 | +0.085 | +1660.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 819 | +0.176 | +519.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 819 | +0.176 | +519.66€ | 0 | 16 |
| ✅ GBM_LATE_15M#BTC | 469 | +0.181 | +244.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 469 | +0.181 | +244.33€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 827 | +0.189 | +560.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 827 | +0.189 | +560.58€ | 0 | 17 |
| ✅ GBM_LATE_15M#ETH | 623 | -0.002 | +36.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 623 | -0.002 | +36.37€ | 0 | 4 |
| ✅ GBM_LATE_15M#SOL | 874 | +0.001 | +77.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 874 | +0.001 | +77.15€ | 3 | 5 |
| ✅ GBM_LATE_15M#XRP | 1081 | +0.011 | +222.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1081 | +0.011 | +222.82€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5713 | +0.049 | +1710.35€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5713 | +0.049 | +1710.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1094 | -0.028 | +199.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1094 | -0.028 | +199.28€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1088 | -0.012 | +95.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1088 | -0.012 | +95.33€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 697 | +0.240 | +635.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 697 | +0.240 | +635.75€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 997 | -0.018 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 997 | -0.018 | +11.27€ | 6 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1009 | +0.002 | +101.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1009 | +0.002 | +101.14€ | 2 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 828 | +0.212 | +667.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 828 | +0.212 | +667.57€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3443 | +0.175 | +2324.61€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3443 | +0.175 | +2324.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 612 | +0.192 | +446.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 612 | +0.192 | +446.96€ | 0 | 17 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 460 | +0.195 | +305.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 460 | +0.195 | +305.34€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 610 | +0.201 | +471.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 610 | +0.201 | +471.62€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 432 | +0.207 | +314.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 432 | +0.207 | +314.05€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 639 | +0.072 | +251.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 639 | +0.072 | +251.91€ | 1 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 690 | +0.197 | +534.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 690 | +0.197 | +534.73€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 590 | +0.049 | +55.94€ | 0 | 6 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 590 | +0.049 | +55.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 111 | +0.049 | +1.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 111 | +0.049 | +1.45€ | 2 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 119 | +0.161 | +41.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 119 | +0.161 | +41.72€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 231 | -0.011 | +6.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 231 | -0.011 | +6.12€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 128 | +0.054 | +7.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 128 | +0.054 | +7.91€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO | 3999 | +0.168 | +2581.44€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3999 | +0.168 | +2581.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 789 | +0.186 | +554.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 789 | +0.186 | +554.60€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 527 | +0.156 | +282.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 527 | +0.156 | +282.35€ | 1 | 22 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 777 | +0.216 | +638.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 777 | +0.216 | +638.51€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 376 | +0.127 | +158.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 376 | +0.127 | +158.67€ | 1 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 641 | +0.075 | +275.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 641 | +0.075 | +275.86€ | 0 | 15 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 889 | +0.198 | +671.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 889 | +0.198 | +671.46€ | 0 | 23 |
| ✅ GBM_LATE_5M | 299 | +0.108 | +112.03€ | 3 | 13 |
| ✅ GBM_LATE_5M#5min | 299 | +0.108 | +112.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 155 | +0.118 | +61.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 155 | +0.118 | +61.72€ | 0 | 12 |
| ✅ GBM_LATE_5M#DOGE | 6 | -0.037 | -2.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 6 | -0.037 | -2.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 84 | +0.186 | +47.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 84 | +0.186 | +47.82€ | 0 | 10 |
| ✅ GBM_LATE_5M#SOL | 44 | -0.065 | +3.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 44 | -0.065 | +3.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_60M | 495 | -0.047 | +72.78€ | 4 | 6 |
| ✅ GBM_LATE_60M#60min | 495 | -0.047 | +72.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 171 | -0.003 | +5.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 171 | -0.003 | +5.66€ | 3 | 3 |
| ✅ GBM_LATE_60M#ETH | 174 | -0.023 | +43.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 174 | -0.023 | +43.65€ | 1 | 8 |
| ✅ GBM_LATE_60M#SOL | 150 | -0.125 | +23.46€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 150 | -0.125 | +23.46€ | 2 | 2 |
| 🚫 GBM_LATE_60M_FADE | 191 | -0.303 | -33.46€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 191 | -0.303 | -33.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 64 | -0.348 | -18.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 64 | -0.348 | -18.54€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 51 | -0.292 | -7.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 51 | -0.292 | -7.56€ | 2 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 310 | +0.042 | +7.55€ | 1 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 310 | +0.042 | +7.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 121 | +0.012 | +3.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 121 | +0.012 | +3.09€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 73 | +0.100 | +7.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 73 | +0.100 | +7.77€ | 0 | 3 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 69 | +0.176 | +29.52€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 69 | +0.176 | +29.52€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 69 | +0.176 | +29.52€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 69 | +0.176 | +29.52€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 202 | -0.113 | -29.52€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 202 | -0.113 | -29.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 48 | -0.120 | -8.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 48 | -0.120 | -8.11€ | 1 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 42 | -0.023 | -2.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 42 | -0.023 | -2.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 99 | -0.124 | -14.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 99 | -0.124 | -14.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 37 | -0.064 | -3.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 37 | -0.064 | -3.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 23 | -0.100 | -2.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 23 | -0.100 | -2.88€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 16 | -0.178 | -4.14€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 16 | -0.178 | -4.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 302 | -0.003 | -6.79€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 302 | -0.003 | -6.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 102 | -0.010 | -7.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 102 | -0.010 | -7.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 99 | -0.015 | -1.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 99 | -0.015 | -1.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 101 | +0.015 | +2.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 101 | +0.015 | +2.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 751 | +0.031 | +22.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 751 | +0.031 | +22.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 113 | +0.065 | +17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 113 | +0.065 | +17.56€ | 1 | 6 |
| ✅ MOMENTUM_IBS_15M#BTC | 132 | +0.097 | +24.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 132 | +0.097 | +24.51€ | 0 | 7 |
| ✅ MOMENTUM_IBS_15M#DOGE | 117 | +0.013 | -10.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 117 | +0.013 | -10.83€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 136 | +0.065 | +24.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 136 | +0.065 | +24.44€ | 0 | 5 |
| ✅ MOMENTUM_IBS_15M#SOL | 125 | -0.059 | -23.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 125 | -0.059 | -23.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 128 | +0.000 | -9.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 128 | +0.000 | -9.95€ | 0 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 1021 | -0.038 | +13.68€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 1021 | -0.038 | +13.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 161 | -0.034 | +23.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 161 | -0.034 | +23.32€ | 4 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 177 | -0.064 | -19.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 177 | -0.064 | -19.22€ | 6 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 166 | -0.006 | +31.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 166 | -0.006 | +31.69€ | 3 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 179 | -0.014 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 179 | -0.014 | -4.50€ | 3 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 165 | -0.063 | -7.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 165 | -0.063 | -7.74€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 173 | -0.043 | -9.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 173 | -0.043 | -9.87€ | 4 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE | 354 | -0.048 | -19.58€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 354 | -0.048 | -19.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 55 | -0.009 | -1.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 55 | -0.009 | -1.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 50 | -0.154 | -8.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 50 | -0.154 | -8.53€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 68 | -0.086 | -6.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 68 | -0.086 | -6.75€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 83 | +0.018 | +1.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 83 | +0.018 | +1.93€ | 1 | 3 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 70 | +0.000 | -0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 70 | +0.000 | -0.52€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M | 970 | +0.001 | +0.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 970 | +0.001 | +0.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 119 | -0.029 | -0.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 119 | -0.029 | -0.78€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 171 | +0.009 | -2.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 171 | +0.009 | -2.20€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 123 | +0.012 | +0.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 123 | +0.012 | +0.52€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#ETH | 194 | +0.005 | +5.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 194 | +0.005 | +5.37€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#SOL | 197 | +0.007 | +2.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 197 | +0.007 | +2.97€ | 0 | 1 |
| ✅ MOMENTUM_IBS_5M#XRP | 166 | -0.006 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 166 | -0.006 | -5.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 2871 | -0.064 | +70.26€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 2871 | -0.064 | +70.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 422 | -0.101 | +18.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 422 | -0.101 | +18.17€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 552 | -0.052 | +69.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 552 | -0.052 | +69.09€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 438 | -0.061 | -4.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 438 | -0.061 | -4.18€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 492 | -0.075 | -33.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 492 | -0.075 | -33.32€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 522 | -0.044 | -9.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 522 | -0.044 | -9.58€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 445 | -0.053 | +30.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 445 | -0.053 | +30.07€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 2471 | +0.016 | +20.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 2471 | +0.016 | +20.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 415 | +0.025 | +11.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 415 | +0.025 | +11.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 341 | +0.039 | +8.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 341 | +0.039 | +8.88€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 427 | +0.001 | -4.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 427 | +0.001 | -4.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 432 | +0.009 | +2.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 432 | +0.009 | +2.31€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 443 | +0.010 | +0.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 443 | +0.010 | +0.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 413 | +0.018 | +1.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 413 | +0.018 | +1.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 240 | +0.087 | +47.62€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 104 | +0.123 | +35.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 30 | +0.219 | +24.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 30 | +0.219 | +24.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 18 | +0.045 | +2.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 18 | +0.045 | +2.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 9 | +0.061 | +4.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 9 | +0.061 | +4.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 26 | +0.071 | +2.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 26 | +0.071 | +2.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 21 | +0.065 | +1.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 21 | +0.065 | +1.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 218 | -0.136 | -7.98€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 89 | -0.181 | -19.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 76 | -0.192 | -16.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 87 | -0.140 | -2.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 72 | -0.149 | -3.66€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 15 | -0.066 | +1.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 185 | -0.136 | -5.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 33 | -0.129 | -2.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 114 | -0.267 | -24.37€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 47 | -0.194 | -5.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 45 | -0.181 | -4.23€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 51 | -0.255 | -10.96€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 49 | -0.245 | -9.94€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 16 | -0.356 | -8.16€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 15 | -0.331 | -7.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 109 | -0.257 | -21.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 5 | -0.089 | -2.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 48 | +0.240 | +4.75€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 48 | +0.240 | +4.75€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 48 | -0.140 | -13.74€ | 3 | 0 |
| ✅ STREAK_FADE_15M#15min | 48 | -0.140 | -13.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 19 | -0.068 | -4.71€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 19 | -0.068 | -4.71€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 24 | -0.154 | -6.82€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 24 | -0.154 | -6.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 380 | -0.018 | -18.09€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 380 | -0.018 | -18.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 105 | +0.023 | +2.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 105 | +0.023 | +2.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 127 | -0.012 | -7.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 127 | -0.012 | -7.16€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 66 | -0.059 | -6.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 66 | -0.059 | -6.52€ | 2 | 2 |
| ✅ STREAK_FADE_5M#XRP | 82 | -0.048 | -6.49€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 82 | -0.048 | -6.49€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 642 | +0.014 | -5.48€ | 1 | 0 |
| ✅ STREAK_MOM_5M#5min | 642 | +0.014 | -5.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 206 | +0.014 | -1.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 206 | +0.014 | -1.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 120 | -0.016 | -4.29€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 120 | -0.016 | -4.29€ | 3 | 2 |
| ✅ STREAK_MOM_5M#SOL | 167 | +0.015 | -1.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 167 | +0.015 | -1.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 149 | +0.036 | +1.44€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 149 | +0.036 | +1.44€ | 1 | 2 |
| ✅ STRUCT_NO_15M | 1908 | +0.017 | -0.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1908 | +0.017 | -0.97€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 725 | +0.008 | -7.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 725 | +0.008 | -7.96€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 747 | +0.022 | +3.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 747 | +0.022 | +3.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 436 | +0.025 | +3.95€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 436 | +0.025 | +3.95€ | 2 | 0 |
| ✅ UPDOWN_GBM | 2467 | +0.028 | +191.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1058 | +0.089 | +198.77€ | 1 | 8 |
| ✅ UPDOWN_GBM#240min | 124 | +0.016 | -0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 982 | -0.010 | +4.25€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 256 | -0.023 | -10.57€ | 4 | 1 |
| ✅ UPDOWN_GBM#BNB | 108 | +0.127 | +30.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 101 | +0.150 | +32.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6 | -0.075 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 466 | +0.034 | +38.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 130 | +0.061 | +0.72€ | 2 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 38 | +0.075 | +3.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 194 | +0.066 | +41.54€ | 2 | 9 |
| ✅ UPDOWN_GBM#BTC#60min | 86 | -0.057 | -8.56€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 306 | +0.000 | -1.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 63 | +0.115 | +14.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 243 | -0.031 | -16.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 574 | +0.054 | +59.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 243 | +0.120 | +56.44€ | 1 | 13 |
| ✅ UPDOWN_GBM#ETH#240min | 38 | +0.050 | +1.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 174 | +0.011 | +3.11€ | 4 | 3 |
| ✅ UPDOWN_GBM#ETH#60min | 104 | +0.009 | -1.14€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 460 | -0.006 | +0.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 197 | +0.018 | +3.83€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 30 | -0.031 | -2.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 155 | -0.003 | -0.10€ | 2 | 2 |
| ✅ UPDOWN_GBM#SOL#60min | 66 | -0.029 | -0.87€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 551 | +0.023 | +65.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 324 | +0.092 | +90.49€ | 0 | 14 |
| ✅ UPDOWN_GBM#XRP#240min | 17 | -0.112 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 210 | -0.071 | -21.95€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 112 | +0.254 | -0.89€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 112 | +0.254 | -0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 73 | +0.220 | -8.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 73 | +0.220 | -8.37€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 39 | +0.305 | +7.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 39 | +0.305 | +7.48€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1757 | -0.050 | +222.52€ | 2 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1757 | -0.050 | +222.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 122 | -0.073 | +1.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 122 | -0.073 | +1.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 338 | -0.141 | -18.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 338 | -0.141 | -18.84€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 43 | +0.011 | +3.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 43 | +0.011 | +3.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 135 | +0.004 | +21.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 135 | +0.004 | +21.27€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 570 | -0.018 | +140.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 570 | -0.018 | +140.06€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 549 | -0.041 | +74.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 549 | -0.041 | +74.60€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 151 | +0.258 | +78.48€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 151 | +0.258 | +78.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 92 | +0.245 | +38.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 92 | +0.245 | +38.37€ | 0 | 13 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 59 | +0.271 | +40.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 59 | +0.271 | +40.11€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 361 | -0.059 | -26.99€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 361 | -0.059 | -26.99€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 230 | -0.004 | -10.63€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 230 | -0.004 | -10.63€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 19 | +0.068 | +4.22€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 19 | +0.068 | +4.22€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 26 | -0.179 | -5.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 26 | -0.179 | -5.17€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 933 | +0.285 | +382.06€ | 0 | 2 |
| ✅ WEEKLY_PRICE#BTC | 277 | +0.199 | +5.61€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 296 | +0.255 | +66.82€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 360 | +0.373 | +309.64€ | 0 | 1 |