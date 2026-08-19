# Hipótesis automáticas — 2026-08-19 01:04 UTC
_Generado por shadow_postmortem.py sobre 69970 resoluciones (PNL=+7001.37€)_

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
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=209)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.239 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.080)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.080)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.080)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.140 (n=209)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.5 (IC base=+0.018)

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
- **FILTRO** `restante_s_al_confirmar` < `152.71` → IC=-0.248 (n=932)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.71
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2797)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `119.16` → IC=-0.402 (n=100)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.16
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=301)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `641.03` → IC=-0.271 (n=116)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 641.03
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=349)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `13.71` → IC=-0.492 (n=121)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 13.71
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=251)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `concentracion_yes` < `1.0` → IC=-0.131 (n=63)

  - _Acción_: SKIP cuando `concentracion_yes` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=843)

- **FILTRO** `restante_s_al_confirmar` < `247.76` → IC=-0.148 (n=679)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 247.76
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=227)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.96` → IC=-0.289 (n=183)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.96
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=551)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.191 (n=2383)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.7 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=1176)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2373.5135` → IC=+0.168 (n=1136)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2373.5135 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.158 (n=4050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=2899)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=2034)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `4052.555` → IC=+0.182 (n=826)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4052.555 (IC base=+0.152)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.364 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.302 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=341)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.145 (n=426)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` > 0.555 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.201 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.220 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5297.7285` → IC=+0.173 (n=209)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 5297.7285 (IC base=+0.141)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.127 (n=622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 15.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.299 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.315 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=270)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.299 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1919.6059` → IC=+0.321 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.6059 (IC base=+0.297)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.172 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 16.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=275)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2169.3562` → IC=+0.169 (n=273)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2169.3562 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.121 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `5697.4897` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5697.4897 (IC base=+0.099)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.397 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.276 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` < `0.31` → IC=+0.354 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.31 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `913.222` → IC=+0.247 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 913.222 (IC base=+0.236)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.256 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.195 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 13.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.335 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.224 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=258)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.112)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=65)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=96)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.193 (n=1181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.201 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.163 (n=604)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` < `0.741` → IC=+0.169 (n=665)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` < 0.741 (IC base=+0.155)

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
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.182 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 7.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.187 (n=231)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.7 (IC base=+0.155)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.233 (n=402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.318 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.216)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.186 (n=511)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.72 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.433 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.415 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.408)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.408)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.403 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.408)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.408)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.418 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.407 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.435 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.406)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.417 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.384)

- **PATRÓN** `py_entrada` < `0.91` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.91 (IC base=+0.384)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.384)

- **PATRÓN** `libro_liquidez` > `2008.7424` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.7424 (IC base=+0.384)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=1779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.203 (n=1575)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.248 (n=1632)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.188)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `py_entrada` > `0.73` → IC=+0.136 (n=435)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` > 0.73 (IC base=+0.096)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.298 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.259 (n=243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.329 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.249)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.218 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.155)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.293 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.262 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.286 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.247)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.250 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.226 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.147)

- **PATRÓN** `restante_min` < `3.81` → IC=+0.162 (n=569)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` < 3.81 (IC base=+0.147)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.207 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=1779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.162 (n=1218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.147)

- **PATRÓN** `lag_apertura_s` < `5.51` → IC=+0.213 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.51 (IC base=+0.147)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.244 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.152)

- **PATRÓN** `restante_min` < `3.74` → IC=+0.170 (n=283)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` < 3.74 (IC base=+0.152)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.192 (n=303)

  - _Acción_: Kelly boost +0.96€ cuando `restante_min` > 4.88 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.169 (n=602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 12.0 (IC base=+0.152)

- **PATRÓN** `lag_apertura_s` < `7.13` → IC=+0.195 (n=280)

  - _Acción_: Kelly boost +0.98€ cuando `lag_apertura_s` < 7.13 (IC base=+0.152)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.43` → IC=+0.172 (n=764)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.43 (IC base=+0.141)

- **PATRÓN** `restante_min` < `3.91` → IC=+0.147 (n=287)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` < 3.91 (IC base=+0.141)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.222 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.149 (n=909)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.141)

- **PATRÓN** `lag_apertura_s` < `3.27` → IC=+0.223 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.27 (IC base=+0.141)

- **PATRÓN** `profundidad_ratio_no` > `11.3` → IC=+0.161 (n=287)

  - _Acción_: Kelly boost +0.80€ cuando `profundidad_ratio_no` > 11.3 (IC base=+0.141)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.308 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.312 (n=424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.385 (n=137)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.318 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.399 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.301)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.304 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `1876.0591` → IC=+0.319 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.0591 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.375)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.375)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.397 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1401.7964` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1401.7964 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.278 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.397 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1401.7964` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1401.7964 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.142 (n=448)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.9851` → IC=+0.267 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9851 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.4219` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4219 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.71` → IC=+0.237 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.71 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.2802` → IC=+0.247 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2802 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.6468` → IC=+0.241 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6468 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.6654` → IC=+0.123 (n=2192)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6654 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.2421` → IC=+0.140 (n=578)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2421 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `1.3118` → IC=+0.139 (n=494)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.3118 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `0.6951` → IC=+0.139 (n=441)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6951 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.3296` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3296 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.5637` → IC=+0.257 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5637 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.8566` → IC=+0.228 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8566 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `245.0` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 245.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.168 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.007 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.195 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.9216` → IC=+0.279 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9216 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.471` → IC=+0.346 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.471 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.155 (n=305)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.06 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.311 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.336 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.1333` → IC=+0.341 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1333 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.288 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.295 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.578` → IC=+0.333 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.578 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.316 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` < `1.8119` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8119 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `1.5851` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5851 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.329 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `1915.4982` → IC=+0.313 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.4982 (IC base=+0.285)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.340 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.289 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.327 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` > `0.917` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.917 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` > `0.2115` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2115 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.529` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.529 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` < `1.3738` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3738 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.1734` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1734 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `2.7035` → IC=+0.321 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7035 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `13015.3205` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13015.3205 (IC base=+0.262)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.175 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0018 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.149 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0029 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1881` → IC=+0.168 (n=212)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1881 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.171 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.204 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1374` → IC=+0.162 (n=258)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1374 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.472` → IC=+0.234 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.472 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.2895` → IC=+0.163 (n=241)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2895 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6821` → IC=+0.159 (n=215)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6821 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.0934` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0934 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.5138` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5138 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `12200.4416` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12200.4416 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `244.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 244.0 (IC base=+0.143)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.165 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.007 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.204 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.932` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.932 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.4168` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.4168 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.143 (n=415)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.06 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.355 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.317 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.289 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.5011` → IC=+0.314 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5011 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.093` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.093 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.3362` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3362 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `4.8135` → IC=+0.275 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.8135 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `2.9764` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9764 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.292 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.288)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0993` → IC=+0.138 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.0993 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.5406` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.5406 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.0972` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.0972 (IC base=-0.019)

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
- **PATRÓN** `sigma_ewma_delta_pct` > `8.411` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 8.411 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` < `0.1873` → IC=+0.229 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1873 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.036)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `ibs_20min` > `0.9432` → IC=+0.233 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9432 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.3587` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3587 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.204` → IC=+0.127 (n=1026)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.204 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.3396` → IC=+0.197 (n=107)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.3396 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.2038` → IC=+0.155 (n=450)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.2038 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.229 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.167 (n=871)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.5002` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5002 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.2604` → IC=+0.217 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2604 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2118` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2118 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `3.7394` → IC=+0.320 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7394 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.332 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.049)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.003` → IC=-0.210 (n=105)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.003
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=534)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.382` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 3.382 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.0503` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0503 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `2.3584` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.3584 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` < `0.0555` → IC=-0.152 (n=87)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0555
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=262)

- **PATRÓN** `volumen_regimen` < `1.0528` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0528 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5727 (IC base=-0.010)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.279 (n=120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0611` → IC=+0.211 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0611 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.244 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.958` → IC=+0.305 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.958 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` < `0.1438` → IC=+0.183 (n=257)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1438 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `3.8997` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.8997 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.192 (n=387)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.06 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1915.1184` → IC=+0.212 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.1184 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.431 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.372)

- **PATRÓN** `drift_60min` |x|≤ `0.1806` → IC=+0.374 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1806 (IC base=+0.372)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.397 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.372)

- **PATRÓN** `ibs_20min` < `0.2414` → IC=+0.390 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2414 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` < `0.3211` → IC=+0.395 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3211 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` > `0.404` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.404 (IC base=+0.372)

- **PATRÓN** `volumen_spike_ratio` < `2.9702` → IC=+0.440 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9702 (IC base=+0.372)

- **PATRÓN** `libro_liquidez` > `1868.3264` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1868.3264 (IC base=+0.372)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.6396` → IC=-0.127 (n=159)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6396
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=83)

- **FILTRO** `dist_vwap_pct` < `0.3632` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3632
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

- **FILTRO** `volumen_regimen` > `0.8629` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8629
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **FILTRO** `libro_liquidez` < `8611.2001` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `libro_liquidez` < 8611.2001
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=182)

- **FILTRO** `dist_vwap_pct` < `0.0649` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0649
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `volumen_regimen` > `0.7318` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.7318
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=704)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.4545` → IC=-0.151 (n=147)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4545
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=147)

- **FILTRO** `dist_vwap_pct` > `0.1234` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1234
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `volumen_regimen` > `1.2342` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2342
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **PATRÓN** `ibs_20min` > `0.4545` → IC=+0.124 (n=147)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.4545 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.1779` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1779 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.296 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.154 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.207 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.226 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.326` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.326 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.128` → IC=+0.224 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.128 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.5938` → IC=+0.149 (n=303)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.5938 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.3138` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3138 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.6244` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.6244 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=307)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2467.4755` → IC=+0.137 (n=271)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2467.4755 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.301 (n=280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.329 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3182` → IC=+0.338 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3182 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.5441` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5441 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.001` → IC=+0.291 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.001 (IC base=+0.287)

- **PATRÓN** `volumen_regimen` > `0.7147` → IC=+0.308 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7147 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `3.6746` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6746 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `2861.3406` → IC=+0.292 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2861.3406 (IC base=+0.287)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.159 (n=432)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0047 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.193 (n=588)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0066 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0933` → IC=+0.140 (n=570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0933 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.9206` → IC=+0.252 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9206 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.151 (n=382)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.935` → IC=+0.268 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.935 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1814` → IC=+0.144 (n=672)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1814 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.144 (n=672)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6258 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1103` → IC=+0.154 (n=435)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1103 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.146 (n=1460)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.06 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2699.8737` → IC=+0.180 (n=432)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2699.8737 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.220 (n=1249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.2358` → IC=+0.223 (n=1098)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2358 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.257 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.280 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.631` → IC=+0.234 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.631 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.234` → IC=+0.216 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.234 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.2517` → IC=+0.193 (n=968)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2517 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.8747` → IC=+0.199 (n=645)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.8747 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2702` → IC=+0.284 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2702 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `2.0525` → IC=+0.225 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0525 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `3.1492` → IC=+0.246 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1492 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.279 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.215)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.161 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.205 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.228 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.572` → IC=+0.372 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.572 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1492` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.1492 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.185 (n=252)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.289 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.322 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.2174` → IC=+0.319 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2174 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.312 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.0505` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0505 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.2006` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2006 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.312 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.08 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1962.1404` → IC=+0.344 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1962.1404 (IC base=+0.287)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.316 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.269 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.273 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.871` → IC=+0.283 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.871 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.3045` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3045 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.296` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.296 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.3694` → IC=+0.232 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3694 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.9006` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9006 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `3.0052` → IC=+0.237 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0052 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.9953` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9953 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.212 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.181 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.002 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1903` → IC=+0.199 (n=204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1903 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.2977` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2977 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.411` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.411 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.6385` → IC=+0.225 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6385 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.6916` → IC=+0.181 (n=208)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6916 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1409` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1409 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.6231` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6231 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `11777.8012` → IC=+0.212 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11777.8012 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.170 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0065 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.147` → IC=+0.155 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.147 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.284 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.321 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.0095` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0095 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.140 (n=109)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.174 (n=231)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.04 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `1970.881` → IC=+0.157 (n=100)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1970.881 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.335 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.311 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.313)

- **PATRÓN** `drift_60min` |x|≤ `0.1704` → IC=+0.364 (n=101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1704 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.329 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.25 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.735` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.735 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` < `3.417` → IC=+0.315 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.417 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `1912.8634` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.8634 (IC base=+0.313)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.002` → IC=+0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.266 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.1718` → IC=+0.312 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1718 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.253 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.274 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.252)

- **PATRÓN** `ibs_20min` > `0.7312` → IC=+0.310 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7312 (IC base=+0.252)

- **PATRÓN** `dist_vwap_pct` < `0.364` → IC=+0.289 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.364 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.807` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.807 (IC base=+0.252)

- **PATRÓN** `volumen_regimen` > `0.6636` → IC=+0.279 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6636 (IC base=+0.252)

- **PATRÓN** `volumen_pendiente_norm` > `0.1116` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1116 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` < `1.688` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.688 (IC base=+0.252)

- **PATRÓN** `volumen_spike_ratio` > `2.5007` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5007 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.253 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.252)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.260 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1364` → IC=+0.199 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1364 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.237 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.332` → IC=+0.259 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.332 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.409` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.409 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `1.2379` → IC=+0.219 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2379 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.083` → IC=+0.216 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.083 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.9228` → IC=+0.274 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9228 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=258)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 108.0 (IC base=+0.189)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5588` → IC=-0.235 (n=81)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5588
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=246)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.8667 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.044)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.218 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.239 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.222 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5588 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.5824` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.5824 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.906` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.906 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` > `0.871` → IC=+0.151 (n=164)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.871 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.1184` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1184 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `1.6882` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.6882 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2415.134` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2415.134 (IC base=+0.108)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.248 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.2105` → IC=+0.144 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.2105 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.173 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.229 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.312` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.312 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.0668` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0668 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.341` → IC=+0.233 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.341 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1205` → IC=+0.143 (n=247)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1205 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6045` → IC=+0.125 (n=246)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6045 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `3.0381` → IC=+0.129 (n=211)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 3.0381 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=253)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2469.6086` → IC=+0.140 (n=220)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2469.6086 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.284 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.275 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.291 (n=89)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.294 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.2333` → IC=+0.322 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2333 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.724` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.724 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` > `0.8965` → IC=+0.310 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8965 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `1.6659` → IC=+0.264 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6659 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `2672.4942` → IC=+0.281 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2672.4942 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.267)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9524 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.863` → IC=+0.253 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.863 (IC base=+0.044)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.288 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.3636` → IC=+0.125 (n=166)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.3636 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.874` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.874 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` < `2.6304` → IC=+0.130 (n=117)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.6304 (IC base=+0.059)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `sigma_h` > `0.0026` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `volumen_spike_ratio` > `1.77` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.77
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.232 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2503` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2503 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.206 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1659` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1659 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.889` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.889 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.178` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.178 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7151 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0902` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0902 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4192` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4192 (IC base=+0.139)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.203 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.214 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.261` → IC=+0.257 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.261 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.6639` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6639 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.831` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.831 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.9813` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9813 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `1.0973` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0973 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.1778` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1778 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.3331` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3331 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.5464` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5464 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `3088.7155` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3088.7155 (IC base=+0.204)

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
- **FILTRO** `ibs_20min` > `0.6852` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6852
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

- **FILTRO** `dist_vwap_pct` > `0.19` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.19
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

- **FILTRO** `volumen_pendiente_norm` > `0.1087` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1087
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `libro_liquidez` < `2536.4746` → IC=-0.154 (n=53)

  - _Acción_: SKIP cuando `libro_liquidez` < 2536.4746
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.024)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.175 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0059 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.504` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 7.504 (IC base=+0.058)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0588 (IC base=+0.065)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.195 (n=525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0068 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.9626` → IC=+0.280 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9626 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.359` → IC=+0.185 (n=179)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.359 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.252` → IC=+0.232 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.252 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.1816` → IC=+0.135 (n=371)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.1816 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.6912` → IC=+0.121 (n=1127)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.6912 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.124 (n=1755)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.06 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2741.8936` → IC=+0.153 (n=523)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2741.8936 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.188 (n=190)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 147.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.233 (n=1228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.231 (n=1395)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.235 (n=1275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.287 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.1556` → IC=+0.199 (n=911)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.1556 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.033` → IC=+0.254 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.033 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.485` → IC=+0.226 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.485 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.6189` → IC=+0.204 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6189 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `1.0629` → IC=+0.215 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0629 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1146` → IC=+0.248 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1146 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2523` → IC=+0.270 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2523 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.5394` → IC=+0.286 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5394 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.210 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.224)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.209 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.160 (n=266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.9474` → IC=+0.286 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9474 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.154` → IC=+0.354 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.154 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2139` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2139 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.161 (n=287)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.06 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.318 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.318 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.2108` → IC=+0.335 (n=168)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2108 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.307 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.296)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.339 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.296)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` < `1.88` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.88 (IC base=+0.296)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.343 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `1915.4982` → IC=+0.343 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.4982 (IC base=+0.296)

### GBM_LATE_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_20min` < `0.3033` → IC=-0.217 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3033
  - _Potencial_: sin este filtro IC_bueno=+0.245 (n=155)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.160 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0026 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.173 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0034 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.286 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.3033` → IC=+0.245 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3033 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.2647` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2647 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.71` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.71 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6694` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6694 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.9205` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.9205 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.1584` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1584 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.8379` → IC=+0.221 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8379 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `11338.6336` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11338.6336 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0017` → IC=+0.216 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0017 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.181 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4191` → IC=+0.223 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4191 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.1378` → IC=+0.185 (n=255)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1378 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.232` → IC=+0.255 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.232 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.3025` → IC=+0.181 (n=236)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.3025 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.856` → IC=+0.185 (n=157)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.856 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.0979` → IC=+0.309 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0979 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.6006` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6006 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `5105.835` → IC=+0.185 (n=211)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 5105.835 (IC base=+0.171)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.243 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.717` → IC=+0.244 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.717 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` < `0.2327` → IC=+0.167 (n=247)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.2327 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.9083` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.9083 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `4.0232` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 4.0232 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.187 (n=343)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1854.4986` → IC=+0.185 (n=211)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1854.4986 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.367 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.277 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.309 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.5421` → IC=+0.340 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5421 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.605` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.605 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.235 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.378` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.378 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` < `3.6802` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.6802 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.293 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 21.0 (IC base=+0.277)

### GBM_LATE_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_20min` < `0.3557` → IC=-0.222 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3557
  - _Potencial_: sin este filtro IC_bueno=+0.208 (n=159)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.196 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0019 (IC base=+0.101)

- **PATRÓN** `drift_60min` |x|≤ `0.2822` → IC=+0.121 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.2822 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.154 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.3557` → IC=+0.208 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3557 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.4382` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4382 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.292` → IC=+0.207 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.292 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `0.7843` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.7843 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `1.0903` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0903 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.9911` → IC=+0.247 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9911 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `7279.5454` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7279.5454 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.101)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.233 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.056` → IC=+0.191 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.056 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.3087` → IC=+0.243 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3087 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.2018` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2018 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.7` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.7 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.044` → IC=+0.192 (n=118)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.044 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` < `0.141` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.141 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.0794` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0794 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.4499` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4499 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `7139.809` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7139.809 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.158)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.223 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.017)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.204 (n=106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1743` → IC=+0.161 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1743 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.234 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1817` → IC=+0.158 (n=182)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1817 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.414` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.414 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.92` → IC=+0.143 (n=222)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 2.92 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.192 (n=105)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.7028 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.0809` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.0809 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.7971` → IC=+0.260 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7971 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.7285` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7285 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1404.9736` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1404.9736 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.195 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0063 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.195 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.3318` → IC=+0.250 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3318 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.298` → IC=+0.222 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.298 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `0.6734` → IC=+0.141 (n=274)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6734 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.1932` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1932 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.7671` → IC=+0.134 (n=230)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.7671 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=313)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2476.2054` → IC=+0.141 (n=274)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2476.2054 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.132)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.286 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.261)

- **PATRÓN** `drift_60min` |x|≤ `0.2502` → IC=+0.260 (n=311)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2502 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.281 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` < `0.187` → IC=+0.365 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.187 (IC base=+0.261)

- **PATRÓN** `dist_vwap_pct` > `0.3856` → IC=+0.354 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3856 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.839` → IC=+0.322 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.839 (IC base=+0.261)

- **PATRÓN** `volumen_regimen` > `0.883` → IC=+0.298 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.883 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.332` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.332 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` < `1.5149` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5149 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `2.7123` → IC=+0.274 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7123 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `2842.9596` → IC=+0.267 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2842.9596 (IC base=+0.261)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.235 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.261)

### GBM_LATE_5M
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=44)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=49)

- **FILTRO** `volumen_pendiente_norm` > `0.1403` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1403
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=48)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=199)

- **PATRÓN** `drift_60min` |x|≤ `0.0797` → IC=+0.184 (n=17)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0797 (IC base=-0.022)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.187 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0039 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.232 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.138 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.210 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.5387` → IC=+0.150 (n=161)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5387 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1765` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1765 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.051` → IC=+0.151 (n=144)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.051 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.3884` → IC=+0.169 (n=161)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.3884 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.6649` → IC=+0.138 (n=161)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6649 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.1509` → IC=+0.151 (n=150)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1509 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.817` → IC=+0.179 (n=160)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.817 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=199)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8505.7624` → IC=+0.158 (n=144)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8505.7624 (IC base=+0.134)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.163 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0033 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.243 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.147 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.214 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.1373` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1373 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.189` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 10.189 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.2467` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2467 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `0.7325` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7325 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.698` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.698 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.4793` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4793 (IC base=+0.132)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.275 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.306 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.329 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.3964` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3964 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.498` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.498 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.567` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.567 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.809` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.809 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.0755` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0755 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` < `0.1109` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1109 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.8878` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8878 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `8306.7713` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8306.7713 (IC base=+0.229)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.161 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=110)

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
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0054 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `1.0949` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 1.0949 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `1760.3207` → IC=+0.134 (n=99)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1760.3207 (IC base=+0.059)

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

- **PATRÓN** `dist_vwap_pct` < `0.1209` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1209 (IC base=+0.102)

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

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.250 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=-0.013)

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
- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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
- **FILTRO** `ibs_20min` < `0.6` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

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
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.292 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.227)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.292 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.227)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `libro_liquidez` < `6033.6058` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 6033.6058
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=22)

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

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.121)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0647` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0647 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.0947` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0947 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2061.3329` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2061.3329 (IC base=+0.121)

### MOMENTUM_IBS_15M#BTC#15min
- **PATRÓN** `hora_utc` < `5.0` → IC=+0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 5.0 (IC base=+0.068)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0376` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0376 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.0648` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0648 (IC base=+0.068)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **FILTRO** `ibs_20min` > `0.7917` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7917
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### MOMENTUM_IBS_15M#ETH#15min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 19.0 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.105)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0609` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0609 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `15313.5075` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15313.5075 (IC base=+0.105)

### MOMENTUM_IBS_15M#XRP#15min
- **PATRÓN** `hora_utc` < `4.0` → IC=+0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.062)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.4` → IC=-0.278 (n=106)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=339)

- **FILTRO** `ibs_20min` < `0.7217` → IC=-0.243 (n=111)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7217
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=334)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.203 (n=109)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=336)

- **FILTRO** `libro_liquidez` < `2035.06` → IC=-0.134 (n=293)

  - _Acción_: SKIP cuando `libro_liquidez` < 2035.06
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=152)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=54)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=41)

- **FILTRO** `ibs_20min` < `0.763` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.763
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=47)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=48)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=58)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `ballena_activa_n` > `49.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 49.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

- **FILTRO** `ibs_20min` > `0.2136` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2136
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **FILTRO** `ballena_activa_n` > `71.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 71.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.222 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=40)

- **FILTRO** `ibs_20min` < `0.7` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=56)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=65)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.073)

- **PATRÓN** `py_entrada` < `0.69` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.69 (IC base=+0.073)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=56)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=55)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.5 (IC base=+0.052)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=42)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=58)

- **FILTRO** `ibs_20min` < `0.7187` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7187
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=56)

- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=53)

- **FILTRO** `ibs_20min` < `0.7169` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7169
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `libro_liquidez` < `2537.1559` → IC=-0.167 (n=52)

  - _Acción_: SKIP cuando `libro_liquidez` < 2537.1559
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=27)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=62)

- **PATRÓN** `py_entrada` < `0.52` → IC=+0.125 (n=62)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.52 (IC base=+0.024)

- **PATRÓN** `libro_liquidez` > `2636.658` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2636.658 (IC base=+0.024)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=181)

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
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.931` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.931 (IC base=+0.042)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `ibs_20min` < `0.2368` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.056)

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
- **FILTRO** `hora_utc` < `15.0` → IC=-0.150 (n=610)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=636)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.284 (n=290)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=956)

- **FILTRO** `ibs_7min` < `0.719` → IC=-0.238 (n=311)

  - _Acción_: SKIP cuando `ibs_7min` < 0.719
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=935)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.183 (n=414)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=832)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.191 (n=328)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=1054)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.3` → IC=-0.271 (n=46)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=151)

- **FILTRO** `ibs_7min` < `0.8485` → IC=-0.200 (n=98)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8485
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.223 (n=92)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=105)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.202 (n=45)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=147)

- **FILTRO** `drift_7min_pct` |x|> `0.0977` → IC=-0.142 (n=65)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0977
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=127)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.167 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=178)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.297 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=201)

- **FILTRO** `ibs_7min` < `0.803` → IC=-0.216 (n=65)

  - _Acción_: SKIP cuando `ibs_7min` < 0.803
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=198)

- **FILTRO** `ballena_activa_n` > `111.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 111.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=199)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.182 (n=61)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=182)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.179 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=97)

- **FILTRO** `py_entrada` < `0.28` → IC=-0.411 (n=43)

  - _Acción_: SKIP cuando `py_entrada` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=136)

- **FILTRO** `ibs_7min` < `0.1429` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1429
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=135)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.261 (n=44)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=135)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.198 (n=104)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=119)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.209 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=110)

- **FILTRO** `ibs_7min` < `0.8284` → IC=-0.222 (n=52)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8284
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=159)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=159)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.120 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=157)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.167 (n=55)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=179)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.148 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=180)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=174)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.155 (n=111)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=121)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=175)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.163 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=86)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.275 (n=87)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=77)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.300 (n=53)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=111)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.286 (n=40)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=124)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.245 (n=49)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=195)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.133 (n=88)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=-0.020)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=75)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=94)

- **FILTRO** `libro_liquidez` < `11020.0019` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `libro_liquidez` < 11020.0019
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=74)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.158 (n=147)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.145 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 18.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `325.231` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 325.231 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.135)

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
- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=16)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=-0.035)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.241 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=26)

- **FILTRO** `streak_estiramiento` > `0.6102` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6102
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

### STREAK_MOM_5M
- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=43)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.167 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 10.0 (IC base=+0.047)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.047)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `libro_liquidez` < `3496.0203` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3496.0203
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=76)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=+0.000)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.220 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.070)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=706)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=401)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=409)

### UPDOWN_GBM#15min
- **FILTRO** `ibs_15` < `0.5833` → IC=-0.152 (n=139)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=284)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.134 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0035 (IC base=+0.102)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.130 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0054 (IC base=+0.102)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.227 (n=284)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.3538` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3538 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.021` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.021 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `4986.1852` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4986.1852 (IC base=+0.102)

- **PATRÓN** `ibs_15` < `0.4561` → IC=+0.122 (n=398)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` < 0.4561 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.4863` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.4863 (IC base=+0.082)

### UPDOWN_GBM#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.133 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=136)

- **FILTRO** `ibs_15` < `0.1461` → IC=-0.241 (n=83)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1461
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=171)

- **FILTRO** `sigma_ewma_delta_pct` > `5.172` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.172
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=190)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=134)

- **FILTRO** `ibs_15` < `0.592` → IC=-0.183 (n=39)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.592
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=119)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0397` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0397
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `hora_utc` < `19.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.03 (IC base=+0.005)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0039` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `ibs_15` < `0.3405` → IC=-0.265 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3405
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.145 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0029 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.132 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.002 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.132 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.130)

- **PATRÓN** `drift_15min` |x|≤ `0.3806` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.3806 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0878` → IC=+0.132 (n=66)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0878 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.9375` → IC=+0.250 (n=34)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9375 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.3789` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3789 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.945` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.945 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.598` → IC=+0.153 (n=73)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 18.598 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `8560.6622` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8560.6622 (IC base=+0.130)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1001` → IC=-0.206 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1001
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `ibs_15` < `0.0668` → IC=-0.324 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0668
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0181` → IC=+0.122 (n=72)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.61€ cuando `pct_spot_vs_ref` |x|≤ 0.0181 (IC base=+0.090)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.214 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.302` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.302 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.754` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.754 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `11028.905` → IC=+0.143 (n=96)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11028.905 (IC base=+0.090)

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

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.158 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0026 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.189 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.004 (IC base=+0.141)

- **PATRÓN** `drift_15min` |x|≤ `0.4389` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.4389 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.158 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 16.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` < `0.3424` → IC=+0.164 (n=108)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.3424 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.0304` → IC=+0.182 (n=108)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.0304 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.4696` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4696 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.05` → IC=+0.194 (n=106)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 23.05 (IC base=+0.141)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `ibs_15` < `0.0681` → IC=-0.200 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0681
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=37)

- **FILTRO** `dist_vwap_pct` > `0.1774` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1774
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `sigma_ewma_delta_pct` > `5.662` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.662
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=70)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0021 (IC base=+0.067)

- **PATRÓN** `drift_15min` |x|≤ `0.4028` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `drift_15min` |x|≤ 0.4028 (IC base=+0.067)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `delta_ratio_macro` |x|> `0.1688` → IC=+0.156 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1688 (IC base=+0.028)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.03 (IC base=+0.028)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.2171` → IC=+0.140 (n=48)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.2171 (IC base=+0.046)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.128 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.046)

- **PATRÓN** `ibs_15` < `0.1` → IC=+0.265 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1 (IC base=+0.046)

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

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.156 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0063 (IC base=+0.108)

- **PATRÓN** `drift_60min` |x|≤ `0.1563` → IC=+0.203 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1563 (IC base=+0.108)

- **PATRÓN** `drift_15min` |x|≤ `0.7446` → IC=+0.122 (n=141)

  - _Acción_: Kelly boost +0.61€ cuando `drift_15min` |x|≤ 0.7446 (IC base=+0.108)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0971` → IC=+0.164 (n=126)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.0971 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.136 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 19.0 (IC base=+0.108)

- **PATRÓN** `ibs_15` < `0.2353` → IC=+0.188 (n=94)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` < 0.2353 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.127` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.127 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.552` → IC=+0.139 (n=142)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 9.552 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2603.9534` → IC=+0.156 (n=126)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2603.9534 (IC base=+0.108)

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
- **FILTRO** `ibs_15` < `0.3768` → IC=-0.323 (n=77)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3768
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=158)

- **FILTRO** `sigma_ewma_delta_pct` > `12.796` → IC=-0.154 (n=232)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.796
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=945)

- **PATRÓN** `ibs_15` > `0.3768` → IC=+0.156 (n=158)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` > 0.3768 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.53` → IC=+0.271 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.53 (IC base=-0.052)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.0929 (IC base=-0.052)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0033` → IC=-0.219 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=170)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.247 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=176)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.224 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.121 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.050)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `sigma_h` > `0.0047` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=67)

- **FILTRO** `drift_60min` |x|> `0.2078` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2078
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=67)

- **FILTRO** `ibs_15` < `0.5166` → IC=-0.370 (n=44)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5166
  - _Potencial_: sin este filtro IC_bueno=+0.181 (n=45)

- **PATRÓN** `ibs_15` > `0.5166` → IC=+0.181 (n=45)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` > 0.5166 (IC base=-0.093)

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
- **FILTRO** `sigma_ewma_delta_pct` > `13.982` → IC=-0.182 (n=64)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.982
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=360)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.749` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.749 (IC base=-0.011)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.0051` → IC=-0.173 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=104)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.163 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=58)

- **FILTRO** `libro_liquidez` < `2490.4522` → IC=-0.200 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 2490.4522
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

- **FILTRO** `sigma_ewma_delta_pct` > `7.842` → IC=-0.145 (n=91)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.842
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=294)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.292 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.1826` → IC=+0.263 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1826 (IC base=+0.255)

- **PATRÓN** `drift_15min` |x|≤ `0.5909` → IC=+0.262 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5909 (IC base=+0.255)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0673` → IC=+0.272 (n=112)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0673 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.255)

- **PATRÓN** `ibs_15` > `0.9358` → IC=+0.331 (n=75)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9358 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` > `0.3789` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3789 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` < `0.0845` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0845 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.952` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.952 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `5397.7239` → IC=+0.266 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5397.7239 (IC base=+0.255)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2` → IC=+0.275 (n=69)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2 (IC base=+0.242)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.246 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.262 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0021 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1873` → IC=+0.275 (n=69)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1873 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.6581` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6581 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0878` → IC=+0.246 (n=61)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0878 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` > `0.8845` → IC=+0.278 (n=61)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8845 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.3789` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3789 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` < `0.0966` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0966 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `27.672` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 27.672 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.438` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.438 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `8349.505` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8349.505 (IC base=+0.242)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.305 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.267)

- **PATRÓN** `drift_15min` |x|≤ `0.4139` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4139 (IC base=+0.267)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1796` → IC=+0.409 (n=20)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1796 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.312 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.267)

- **PATRÓN** `ibs_15` > `0.978` → IC=+0.409 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.978 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` < `0.0769` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0769 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.209` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 16.209 (IC base=+0.267)

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

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.1 sube el IC de +0.046 a +0.265 en UPDOWN_GBM#SOL#5min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.102 a +0.227 en UPDOWN_GBM#15min (n=284). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.130 a +0.250 en UPDOWN_GBM#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.7055 sube el IC de +0.100 a +0.337 en UPDOWN_GBM#ETH#15min (n=47). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.3424 sube el IC de +0.141 a +0.164 en UPDOWN_GBM#ETH#15min (n=108). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS > 0.0304 sube el IC de +0.141 a +0.182 en UPDOWN_GBM#ETH#15min (n=108). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.085 a +0.182 en UPDOWN_GBM#XRP#15min (n=86). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.2353 sube el IC de +0.108 a +0.188 en UPDOWN_GBM#XRP#15min (n=94). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.3768 sube el IC de -0.045 a +0.156 en UPDOWN_GBM_15M_TARDIO (n=158). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.53 sube el IC de -0.052 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=46). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5166 sube el IC de -0.093 a +0.181 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=45). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3879 sube el IC de +0.181 a +0.312 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=30). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9358 sube el IC de +0.255 a +0.331 en UPDOWN_GBM_IBS_ALTO (n=75). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8845 sube el IC de +0.242 a +0.278 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=61). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.978 sube el IC de +0.267 a +0.409 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7088 sube el IC de +0.254 a +0.314 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9942 sube el IC de +0.220 a +0.219 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7314 sube el IC de +0.220 a +0.254 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=55). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.305 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.305 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 489 | +0.046 | +39.63€ | 3 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 489 | +0.046 | +39.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 252 | +0.043 | +24.96€ | 2 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 210 | +0.024 | -0.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 210 | +0.024 | -0.34€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 27 | +0.224 | +15.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 27 | +0.224 | +15.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3488 | -0.114 | -539.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 465 | -0.022 | -18.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 3023 | -0.127 | -521.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 401 | -0.190 | -96.89€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 401 | -0.190 | -96.89€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 465 | -0.022 | -18.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 465 | -0.022 | -18.06€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 312 | -0.159 | -150.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 312 | -0.159 | -150.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 851 | +0.008 | -100.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 851 | +0.008 | -100.33€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 734 | -0.226 | -135.18€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 734 | -0.226 | -135.18€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 15009 | +0.115 | -861.20€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3466 | +0.183 | -92.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 100 | -0.098 | -46.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 8829 | +0.086 | -751.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2614 | +0.133 | +30.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1491 | +0.030 | -328.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 14 | -0.044 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1473 | +0.032 | -322.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3389 | +0.142 | +9.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 948 | +0.200 | -25.49€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 41 | -0.105 | -20.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1470 | +0.114 | -8.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 930 | +0.140 | +64.35€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1488 | +0.057 | -253.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 10 | +0.000 | -3.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1477 | +0.058 | -248.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3662 | +0.126 | -45.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1280 | +0.162 | -17.47€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1466 | +0.102 | -25.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 904 | +0.118 | +5.97€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3493 | +0.137 | -196.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1202 | +0.199 | -47.97€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 41 | +0.012 | -8.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1470 | +0.086 | -100.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 780 | +0.142 | -40.21€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1486 | +0.122 | -46.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1473 | +0.123 | -46.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3537 | +0.159 | -350.16€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3537 | +0.159 | -350.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 886 | +0.155 | -114.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 886 | +0.155 | -114.88€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 78 | -0.113 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 78 | -0.113 | -5.72€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 877 | +0.155 | -114.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 877 | +0.155 | -114.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 787 | +0.216 | -45.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 787 | +0.216 | -45.07€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 830 | +0.171 | -84.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 830 | +0.171 | -84.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 172 | +0.408 | -11.77€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 172 | +0.408 | -11.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 62 | +0.406 | -3.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 62 | +0.406 | -3.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 67 | +0.384 | -6.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 67 | +0.384 | -6.82€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 41 | +0.407 | -1.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 41 | +0.407 | -1.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 6279 | +0.188 | -593.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 6279 | +0.188 | -593.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1176 | +0.096 | -267.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1176 | +0.096 | -267.29€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 965 | +0.249 | -8.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 965 | +0.249 | -8.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1102 | +0.155 | -155.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1102 | +0.155 | -155.69€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1010 | +0.221 | -42.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1010 | +0.221 | -42.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 977 | +0.247 | -10.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 977 | +0.247 | -10.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1049 | +0.183 | -108.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1049 | +0.183 | -108.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2261 | +0.147 | +116.79€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 2261 | +0.147 | +116.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1117 | +0.152 | +67.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1117 | +0.152 | +67.99€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1144 | +0.141 | +48.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1144 | +0.141 | +48.80€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 545 | +0.301 | +6.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 545 | +0.301 | +6.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 229 | +0.275 | -8.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 229 | +0.275 | -8.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 254 | +0.301 | +6.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 254 | +0.301 | +6.98€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 62 | +0.375 | +7.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 62 | +0.375 | +7.35€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 230 | +0.409 | -10.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 230 | +0.409 | -10.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 103 | +0.405 | -5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 103 | +0.405 | -5.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 103 | +0.414 | -5.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 103 | +0.414 | -5.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 255 | +0.259 | -30.00€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 255 | +0.259 | -30.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 255 | +0.259 | -30.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 255 | +0.259 | -30.00€ | 0 | 5 |
| ✅ GBM_LATE_15M | 4644 | +0.085 | +1640.69€ | 0 | 14 |
| ✅ GBM_LATE_15M#15min | 4644 | +0.085 | +1640.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 810 | +0.175 | +509.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 810 | +0.175 | +509.51€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 461 | +0.180 | +235.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 461 | +0.180 | +235.09€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 817 | +0.189 | +552.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 817 | +0.189 | +552.84€ | 0 | 16 |
| ✅ GBM_LATE_15M#ETH | 617 | -0.001 | +36.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 617 | -0.001 | +36.88€ | 0 | 4 |
| ✅ GBM_LATE_15M#SOL | 868 | +0.002 | +79.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 868 | +0.002 | +79.67€ | 3 | 5 |
| ✅ GBM_LATE_15M#XRP | 1071 | +0.013 | +226.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1071 | +0.013 | +226.70€ | 0 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5664 | +0.049 | +1691.62€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5664 | +0.049 | +1691.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1084 | -0.029 | +199.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1084 | -0.029 | +199.03€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1077 | -0.011 | +97.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1077 | -0.011 | +97.58€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 690 | +0.238 | +625.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 690 | +0.238 | +625.90€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 990 | -0.018 | +10.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 990 | -0.018 | +10.41€ | 7 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1003 | +0.001 | +94.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1003 | +0.001 | +94.87€ | 3 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 820 | +0.213 | +663.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 820 | +0.213 | +663.84€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3390 | +0.177 | +2305.89€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3390 | +0.177 | +2305.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 604 | +0.190 | +434.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 604 | +0.190 | +434.65€ | 0 | 17 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 450 | +0.197 | +300.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 450 | +0.197 | +300.18€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 601 | +0.202 | +465.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 601 | +0.202 | +465.77€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 423 | +0.208 | +308.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 423 | +0.208 | +308.73€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 630 | +0.077 | +261.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 630 | +0.077 | +261.68€ | 1 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 682 | +0.199 | +534.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 682 | +0.199 | +534.89€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 568 | +0.051 | +51.44€ | 0 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 568 | +0.051 | +51.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 104 | +0.038 | -6.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 104 | +0.038 | -6.09€ | 2 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 118 | +0.167 | +43.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 118 | +0.167 | +43.76€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 226 | -0.009 | +6.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 226 | -0.009 | +6.45€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 119 | +0.062 | +8.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 119 | +0.062 | +8.59€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO | 3949 | +0.168 | +2548.52€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3949 | +0.168 | +2548.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 780 | +0.184 | +540.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 780 | +0.184 | +540.41€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 520 | +0.155 | +275.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 520 | +0.155 | +275.19€ | 1 | 22 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 768 | +0.218 | +636.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 768 | +0.218 | +636.78€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 367 | +0.126 | +155.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 367 | +0.126 | +155.55€ | 1 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 635 | +0.076 | +264.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 635 | +0.076 | +264.89€ | 0 | 15 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 879 | +0.202 | +675.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 879 | +0.202 | +675.70€ | 0 | 25 |
| ✅ GBM_LATE_5M | 279 | +0.098 | +92.09€ | 4 | 14 |
| ✅ GBM_LATE_5M#5min | 279 | +0.098 | +92.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 146 | +0.095 | +43.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 146 | +0.095 | +43.72€ | 0 | 11 |
| ✅ GBM_LATE_5M#ETH | 77 | +0.196 | +44.91€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 77 | +0.196 | +44.91€ | 0 | 11 |
| ✅ GBM_LATE_5M#SOL | 44 | -0.065 | +3.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 44 | -0.065 | +3.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_60M | 494 | -0.046 | +73.29€ | 4 | 6 |
| ✅ GBM_LATE_60M#60min | 494 | -0.046 | +73.29€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 171 | -0.003 | +5.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 171 | -0.003 | +5.66€ | 3 | 3 |
| ✅ GBM_LATE_60M#ETH | 174 | -0.023 | +43.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 174 | -0.023 | +43.65€ | 1 | 8 |
| ✅ GBM_LATE_60M#SOL | 149 | -0.122 | +23.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 149 | -0.122 | +23.97€ | 2 | 1 |
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
| ✅ LEADLAG_BTC_XRP_15M | 65 | +0.187 | +30.65€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 65 | +0.187 | +30.65€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 65 | +0.187 | +30.65€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 65 | +0.187 | +30.65€ | 0 | 2 |
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
| ✅ LIQUIDACIONES_5M | 91 | -0.124 | -12.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 91 | -0.124 | -12.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 31 | -0.015 | -0.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 31 | -0.015 | -0.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 21 | -0.152 | -3.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 21 | -0.152 | -3.84€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 16 | -0.178 | -4.14€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 16 | -0.178 | -4.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 300 | +0.000 | -5.77€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 300 | +0.000 | -5.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 102 | -0.010 | -7.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 102 | -0.010 | -7.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 97 | -0.005 | -0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 97 | -0.005 | -0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 101 | +0.015 | +2.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 101 | +0.015 | +2.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 689 | +0.030 | +8.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 689 | +0.030 | +8.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 104 | +0.057 | +11.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 104 | +0.057 | +11.72€ | 1 | 5 |
| ✅ MOMENTUM_IBS_15M#BTC | 122 | +0.073 | +14.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 122 | +0.073 | +14.83€ | 0 | 3 |
| ✅ MOMENTUM_IBS_15M#DOGE | 109 | +0.013 | -10.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 109 | +0.013 | -10.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 123 | +0.060 | +18.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 123 | +0.060 | +18.70€ | 0 | 4 |
| ✅ MOMENTUM_IBS_15M#SOL | 112 | -0.035 | -19.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 112 | -0.035 | -19.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 119 | +0.004 | -6.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 119 | +0.004 | -6.58€ | 0 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 947 | -0.040 | +10.13€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 947 | -0.040 | +10.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 150 | -0.046 | +18.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 150 | -0.046 | +18.10€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 164 | -0.072 | -20.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 164 | -0.072 | -20.07€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 154 | +0.006 | +34.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 154 | +0.006 | +34.81€ | 3 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 166 | -0.018 | -6.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 166 | -0.018 | -6.96€ | 3 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 152 | -0.065 | -8.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 152 | -0.065 | -8.41€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 161 | -0.040 | -7.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 161 | -0.040 | -7.35€ | 5 | 2 |
| ✅ MOMENTUM_IBS_15M_FADE | 339 | -0.054 | -21.92€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 339 | -0.054 | -21.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 53 | -0.027 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 53 | -0.027 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 50 | -0.154 | -8.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 50 | -0.154 | -8.53€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 64 | -0.091 | -6.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 64 | -0.091 | -6.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 78 | +0.000 | -0.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 78 | +0.000 | -0.56€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 66 | +0.015 | +0.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 66 | +0.015 | +0.63€ | 1 | 1 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 2628 | -0.065 | +85.41€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 2628 | -0.065 | +85.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 389 | -0.096 | +25.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 389 | -0.096 | +25.42€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 506 | -0.057 | +75.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 506 | -0.057 | +75.28€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 402 | -0.062 | -3.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 402 | -0.062 | -3.16€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 445 | -0.079 | -28.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 445 | -0.079 | -28.18€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 478 | -0.044 | -2.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 478 | -0.044 | -2.90€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 408 | -0.059 | +18.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 408 | -0.059 | +18.95€ | 5 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE | 2351 | +0.016 | +16.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 2351 | +0.016 | +16.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 395 | +0.016 | +7.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 395 | +0.016 | +7.57€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 335 | +0.034 | +5.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 335 | +0.034 | +5.37€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 407 | +0.009 | -0.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 407 | +0.009 | -0.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 411 | +0.009 | +1.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 411 | +0.009 | +1.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 412 | +0.012 | +1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 412 | +0.012 | +1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 391 | +0.019 | +1.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 391 | +0.019 | +1.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 233 | +0.083 | +44.65€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 97 | +0.116 | +32.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 27 | +0.259 | +26.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 27 | +0.259 | +26.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 17 | +0.022 | +1.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 17 | +0.022 | +1.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 8 | +0.040 | +3.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 8 | +0.040 | +3.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 25 | +0.056 | +1.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 25 | +0.056 | +1.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 20 | +0.045 | +0.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 20 | +0.045 | +0.50€ | 0 | 0 |
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
| ✅ STREAK_FADE_5M | 370 | -0.024 | -20.74€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 370 | -0.024 | -20.74€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 101 | +0.024 | +2.11€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 101 | +0.024 | +2.11€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 126 | -0.016 | -7.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 126 | -0.016 | -7.65€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 64 | -0.076 | -8.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 64 | -0.076 | -8.25€ | 2 | 1 |
| ✅ STREAK_FADE_5M#XRP | 79 | -0.056 | -6.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 79 | -0.056 | -6.96€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 627 | +0.020 | +0.43€ | 1 | 0 |
| ✅ STREAK_MOM_5M#5min | 627 | +0.020 | +0.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 202 | +0.015 | -1.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 202 | +0.015 | -1.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 117 | -0.013 | -3.77€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 117 | -0.013 | -3.77€ | 2 | 2 |
| ✅ STREAK_MOM_5M#SOL | 163 | +0.027 | +0.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 163 | +0.027 | +0.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 145 | +0.044 | +4.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 145 | +0.044 | +4.75€ | 2 | 2 |
| ✅ STRUCT_NO_15M | 1904 | +0.017 | -1.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1904 | +0.017 | -1.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 725 | +0.008 | -7.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 725 | +0.008 | -7.96€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 746 | +0.021 | +2.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 746 | +0.021 | +2.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 433 | +0.024 | +3.50€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 433 | +0.024 | +3.50€ | 2 | 0 |
| ✅ UPDOWN_GBM | 2371 | +0.027 | +177.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1026 | +0.090 | +199.16€ | 1 | 8 |
| ✅ UPDOWN_GBM#240min | 124 | +0.016 | -0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 919 | -0.017 | -11.71€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 255 | -0.021 | -9.16€ | 4 | 1 |
| ✅ UPDOWN_GBM#BNB | 102 | +0.115 | +24.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 95 | +0.139 | +26.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6 | -0.075 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 443 | +0.024 | +21.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 128 | +0.054 | -2.24€ | 2 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 38 | +0.075 | +3.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 173 | +0.049 | +27.41€ | 2 | 5 |
| ✅ UPDOWN_GBM#BTC#60min | 86 | -0.057 | -8.56€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 306 | +0.000 | -1.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 63 | +0.115 | +14.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 243 | -0.031 | -16.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 549 | +0.057 | +61.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 236 | +0.126 | +58.51€ | 1 | 13 |
| ✅ UPDOWN_GBM#ETH#240min | 38 | +0.050 | +1.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 157 | +0.009 | +2.51€ | 4 | 2 |
| ✅ UPDOWN_GBM#ETH#60min | 103 | +0.014 | +0.27€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 436 | -0.007 | +1.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 189 | +0.018 | +5.16€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 30 | -0.031 | -2.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 139 | -0.004 | -0.93€ | 2 | 3 |
| ✅ UPDOWN_GBM#SOL#60min | 66 | -0.029 | -0.87€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 533 | +0.025 | +71.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 315 | +0.099 | +96.66€ | 0 | 16 |
| ✅ UPDOWN_GBM#XRP#240min | 17 | -0.112 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 201 | -0.076 | -22.35€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 112 | +0.254 | -0.89€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 112 | +0.254 | -0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 73 | +0.220 | -8.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 73 | +0.220 | -8.37€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 39 | +0.305 | +7.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 39 | +0.305 | +7.48€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1729 | -0.050 | +219.18€ | 2 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1729 | -0.050 | +219.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 120 | -0.082 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 120 | -0.082 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 335 | -0.141 | -17.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 335 | -0.141 | -17.11€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 42 | +0.000 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 42 | +0.000 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 134 | +0.000 | +19.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 134 | +0.000 | +19.88€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 559 | -0.015 | +140.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 559 | -0.015 | +140.81€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 539 | -0.038 | +73.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 539 | -0.038 | +73.97€ | 4 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 149 | +0.255 | +74.94€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 149 | +0.255 | +74.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 91 | +0.242 | +36.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 91 | +0.242 | +36.67€ | 0 | 13 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 58 | +0.267 | +38.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 58 | +0.267 | +38.27€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 360 | -0.058 | -26.48€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 360 | -0.058 | -26.48€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 229 | -0.002 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 229 | -0.002 | -10.12€ | 0 | 0 |
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