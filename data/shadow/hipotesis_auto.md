# Hipótesis automáticas — 2026-08-19 01:57 UTC
_Generado por shadow_postmortem.py sobre 70455 resoluciones (PNL=+7035.90€)_

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
- **FILTRO** `restante_s_al_confirmar` < `153.02` → IC=-0.246 (n=939)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 153.02
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2820)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `119.16` → IC=-0.403 (n=101)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.16
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=306)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `641.03` → IC=-0.271 (n=116)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 641.03
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=349)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `13.73` → IC=-0.492 (n=123)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 13.73
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=251)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `concentracion_yes` < `1.0` → IC=-0.121 (n=64)

  - _Acción_: SKIP cuando `concentracion_yes` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=851)

- **FILTRO** `restante_s_al_confirmar` < `247.78` → IC=-0.145 (n=686)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 247.78
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=229)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.97` → IC=-0.291 (n=185)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.97
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=556)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.191 (n=2394)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=1176)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2373.5135` → IC=+0.168 (n=1136)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2373.5135 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.158 (n=4050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=2927)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=1538)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=2038)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `4054.8773` → IC=+0.182 (n=829)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4054.8773 (IC base=+0.153)

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

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.300 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=447)

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
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.126 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 15.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.299 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.315 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.299 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.299 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `3334.5877` → IC=+0.356 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3334.5877 (IC base=+0.298)

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

- **PATRÓN** `libro_liquidez` > `5700.7138` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5700.7138 (IC base=+0.099)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.187 (n=496)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.397 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.276 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` < `0.31` → IC=+0.351 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.31 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `911.3292` → IC=+0.248 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 911.3292 (IC base=+0.235)

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
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.162 (n=258)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.113)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=65)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=96)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=1186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.201 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=605)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.156)

- **PATRÓN** `py_entrada` < `0.741` → IC=+0.169 (n=666)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.741 (IC base=+0.156)

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
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.156)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.187 (n=231)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.7 (IC base=+0.156)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.233 (n=403)
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
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.196 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.186 (n=511)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.72 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.433 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.416 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.939` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.939 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.418 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.409)

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

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.409)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=1779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.197 (n=3170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.248 (n=1636)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.188)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=592)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.096)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.137 (n=436)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` > 0.73 (IC base=+0.096)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.298 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.252 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.329 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.247)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.218 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.155)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.295 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.256 (n=285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.245)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.284 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.245)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.251 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.226 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.147)

- **PATRÓN** `restante_min` < `3.81` → IC=+0.162 (n=575)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` < 3.81 (IC base=+0.147)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.209 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=1779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.154 (n=1710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `lag_apertura_s` < `5.53` → IC=+0.214 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.53 (IC base=+0.147)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.242 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.153)

- **PATRÓN** `restante_min` < `3.73` → IC=+0.169 (n=282)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` < 3.73 (IC base=+0.153)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.192 (n=306)

  - _Acción_: Kelly boost +0.96€ cuando `restante_min` > 4.88 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.158 (n=844)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 17.0 (IC base=+0.153)

- **PATRÓN** `lag_apertura_s` < `7.11` → IC=+0.194 (n=282)

  - _Acción_: Kelly boost +0.97€ cuando `lag_apertura_s` < 7.11 (IC base=+0.153)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.207 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.140)

- **PATRÓN** `restante_min` < `3.91` → IC=+0.147 (n=290)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` < 3.91 (IC base=+0.140)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.223 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.140)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.221 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.28 (IC base=+0.140)

- **PATRÓN** `profundidad_ratio_no` > `11.2` → IC=+0.159 (n=288)

  - _Acción_: Kelly boost +0.79€ cuando `profundidad_ratio_no` > 11.2 (IC base=+0.140)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1397.8324` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1397.8324 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.278 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1397.8324` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1397.8324 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.142 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.9851` → IC=+0.267 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9851 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.4219` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4219 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.694` → IC=+0.237 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.694 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.2802` → IC=+0.247 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2802 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.6468` → IC=+0.241 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6468 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.6654` → IC=+0.123 (n=2199)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6654 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.2421` → IC=+0.139 (n=580)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2421 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `1.3132` → IC=+0.139 (n=496)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.3132 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `0.6951` → IC=+0.138 (n=443)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6951 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.3266` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3266 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.5637` → IC=+0.261 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5637 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.817` → IC=+0.226 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.817 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.295 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.078)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.168 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.007 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9216` → IC=+0.279 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9216 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.482` → IC=+0.347 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.482 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.156 (n=306)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.06 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.312 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.338 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1333` → IC=+0.342 (n=131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1333 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.288 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.297 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.333 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.321 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.8119` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8119 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.331 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1915.4982` → IC=+0.313 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.4982 (IC base=+0.287)

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
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0018 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.152 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0029 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1881` → IC=+0.170 (n=213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1881 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.171 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.201 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1378` → IC=+0.160 (n=260)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1378 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.413` → IC=+0.225 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.413 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2895` → IC=+0.160 (n=242)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2895 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6827` → IC=+0.161 (n=216)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6827 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.5142` → IC=+0.255 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5142 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `12236.1369` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 12236.1369 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `244.0` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 244.0 (IC base=+0.142)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.165 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.007 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.206 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.932` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.932 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.4168` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.4168 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.143 (n=416)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.06 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.355 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.319 (n=81)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.289 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.289)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.315 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.071` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.071 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` > `0.4259` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4259 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` < `4.6682` → IC=+0.277 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.6682 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` > `2.9594` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9594 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.294 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.289)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `ibs_20min` > `0.772` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.772 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.896` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.896 (IC base=+0.058)

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
- **PATRÓN** `sigma_ewma_delta_pct` > `8.176` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 8.176 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` < `0.1873` → IC=+0.229 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1873 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.035)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.232 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.3584` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3584 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.21` → IC=+0.127 (n=1026)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.21 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.339` → IC=+0.200 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.339 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.2067` → IC=+0.156 (n=451)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.2067 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.259 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.166 (n=872)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.4959` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4959 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.2602` → IC=+0.219 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2602 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.2118` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2118 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `3.7438` → IC=+0.332 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7438 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.335 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.049)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.003` → IC=-0.210 (n=105)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.003
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=537)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.413` → IC=+0.177 (n=125)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.413 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0503` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0503 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.3584` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.3584 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` < `0.0381` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0381
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=264)

- **PATRÓN** `volumen_regimen` < `1.0528` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0528 (IC base=-0.016)

- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5727 (IC base=-0.010)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.281 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0611` → IC=+0.211 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0611 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.245 (n=163)
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

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.192 (n=388)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.06 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1915.1084` → IC=+0.207 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.1084 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.411 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.373)

- **PATRÓN** `drift_60min` |x|≤ `0.1775` → IC=+0.375 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1775 (IC base=+0.373)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.397 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.373)

- **PATRÓN** `ibs_20min` < `0.2417` → IC=+0.391 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2417 (IC base=+0.373)

- **PATRÓN** `ibs_20min` > `0.0506` → IC=+0.372 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0506 (IC base=+0.373)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.399 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.373)

- **PATRÓN** `volumen_pendiente_norm` > `0.1288` → IC=+0.400 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1288 (IC base=+0.373)

- **PATRÓN** `volumen_spike_ratio` < `2.9702` → IC=+0.441 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9702 (IC base=+0.373)

- **PATRÓN** `libro_liquidez` > `1869.9762` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1869.9762 (IC base=+0.373)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.6396` → IC=-0.130 (n=160)

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
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=183)

- **FILTRO** `dist_vwap_pct` < `0.0649` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0649
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `volumen_regimen` > `0.7318` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.7318
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=705)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.45` → IC=-0.158 (n=147)

  - _Acción_: SKIP cuando `ibs_20min` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=149)

- **FILTRO** `dist_vwap_pct` > `0.1234` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1234
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `volumen_regimen` > `1.2342` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2342
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **PATRÓN** `ibs_20min` > `0.45` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.45 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.1779` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1779 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.298 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.154 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.227 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.326` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.326 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.128` → IC=+0.225 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.128 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.5938` → IC=+0.150 (n=304)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.5938 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.3138` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3138 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.1447` → IC=+0.125 (n=166)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.1447 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=308)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2467.4755` → IC=+0.139 (n=272)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2467.4755 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.302 (n=281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.329 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.3182` → IC=+0.338 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3182 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.5433` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5433 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.001` → IC=+0.292 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.001 (IC base=+0.288)

- **PATRÓN** `volumen_regimen` > `0.8997` → IC=+0.320 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8997 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `3.6746` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6746 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `2861.3406` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2861.3406 (IC base=+0.288)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.158 (n=434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0047 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.190 (n=592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0066 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0932` → IC=+0.139 (n=572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0932 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.156 (n=434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.9185` → IC=+0.251 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9185 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.151 (n=382)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.935` → IC=+0.269 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.935 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.1837` → IC=+0.143 (n=676)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1837 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.141 (n=675)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6287 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1103` → IC=+0.155 (n=436)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1103 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.145 (n=1465)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.06 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2699.8737` → IC=+0.177 (n=434)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2699.8737 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.220 (n=1256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.2355` → IC=+0.223 (n=1104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2355 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.257 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.278 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.616` → IC=+0.236 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.616 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.234` → IC=+0.215 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.234 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.252` → IC=+0.190 (n=972)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.252 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.711` → IC=+0.194 (n=868)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.711 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.271 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.6954` → IC=+0.230 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6954 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `3.1445` → IC=+0.245 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1445 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.294 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.214)

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

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.289 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.326 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.215` → IC=+0.329 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.215 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.315 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.0497` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0497 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.2006` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2006 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.314 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.08 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1903.8` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.8 (IC base=+0.290)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.316 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.265 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0031 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.273 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.8703` → IC=+0.276 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8703 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.3045` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3045 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.296` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.296 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `0.6489` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6489 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.7493` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7493 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.4783` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4783 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.0183` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0183 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.212 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.182 (n=209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.002 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1925` → IC=+0.202 (n=206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1925 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.301` → IC=+0.233 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.301 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.411` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.411 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.6385` → IC=+0.225 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6385 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1409` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1409 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.6231` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6231 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `12093.0773` → IC=+0.225 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12093.0773 (IC base=+0.180)

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

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.337 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.313 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.315)

- **PATRÓN** `drift_60min` |x|≤ `0.1704` → IC=+0.365 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1704 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.329 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.3182` → IC=+0.332 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3182 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.476` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.476 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.3361` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3361 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `3.318` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.318 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.294 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.248)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.254 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.248)

- **PATRÓN** `drift_60min` |x|≤ `0.1718` → IC=+0.315 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1718 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.253 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` > `0.7234` → IC=+0.312 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7234 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` < `0.3636` → IC=+0.283 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3636 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.328` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.328 (IC base=+0.248)

- **PATRÓN** `volumen_regimen` > `0.7651` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7651 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` > `0.114` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.114 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` < `1.6992` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6992 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` > `2.4116` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4116 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.255 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.248)

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
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=247)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.8667 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.041)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.229 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.239 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.219 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5588 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.5824` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.5824 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.974` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.974 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `0.871` → IC=+0.151 (n=164)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.871 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.1184` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1184 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.6882` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.6882 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2451.0367` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2451.0367 (IC base=+0.106)

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

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.285 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.265)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.273 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.265)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.293 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.288 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.2333` → IC=+0.319 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2333 (IC base=+0.265)

- **PATRÓN** `dist_vwap_pct` > `0.2648` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2648 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.724` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.724 (IC base=+0.265)

- **PATRÓN** `volumen_regimen` > `0.9` → IC=+0.306 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.3601` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3601 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `2.2444` → IC=+0.229 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2444 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `1.6659` → IC=+0.261 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6659 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `2678.9499` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2678.9499 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.265)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9524 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.863` → IC=+0.253 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.863 (IC base=+0.042)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.288 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.060)

- **PATRÓN** `ibs_20min` < `0.1605` → IC=+0.131 (n=128)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.1605 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.859` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.859 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `2.6304` → IC=+0.134 (n=121)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.6304 (IC base=+0.060)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `sigma_h` > `0.0026` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `volumen_spike_ratio` > `1.77` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.77
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.244 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2954` → IC=+0.167 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2954 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.194 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 13.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1986` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1986 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.27` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.27 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1856 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `0.7208` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.7208 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.091` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.091 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4163` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4163 (IC base=+0.135)

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
- **FILTRO** `ibs_20min` > `0.6852` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6852
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=62)

- **FILTRO** `dist_vwap_pct` > `0.19` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.19
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=66)

- **FILTRO** `volumen_regimen` > `1.2053` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2053
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=55)

- **FILTRO** `volumen_pendiente_norm` > `0.1038` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1038
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

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

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0773 (IC base=+0.062)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.195 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0068 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.962` → IC=+0.279 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.962 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.3557` → IC=+0.185 (n=179)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3557 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.251` → IC=+0.232 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.251 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.1826` → IC=+0.133 (n=371)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.1826 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.6913` → IC=+0.120 (n=1130)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.6913 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.124 (n=1760)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.06 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2751.5045` → IC=+0.150 (n=524)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2751.5045 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.179 (n=194)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 150.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.232 (n=1234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.230 (n=1403)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.235 (n=1275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.286 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.1554` → IC=+0.197 (n=915)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1554 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.033` → IC=+0.251 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.033 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.48` → IC=+0.226 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.48 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.6189` → IC=+0.205 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6189 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `1.234` → IC=+0.214 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.234 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1145` → IC=+0.249 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1145 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.252` → IC=+0.261 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.252 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `2.0258` → IC=+0.272 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0258 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.204 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.224)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.210 (n=181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.162 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.9474` → IC=+0.286 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9474 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.193` → IC=+0.354 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.193 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2139` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2139 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.162 (n=288)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.06 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.318 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.298)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.318 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.2108` → IC=+0.337 (n=170)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2108 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.307 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.309 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.340 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` < `0.0689` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0689 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` < `1.88` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.88 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `2.8175` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8175 (IC base=+0.298)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.329 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `1915.4982` → IC=+0.343 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.4982 (IC base=+0.298)

### GBM_LATE_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_20min` < `0.3033` → IC=-0.217 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3033
  - _Potencial_: sin este filtro IC_bueno=+0.240 (n=156)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.160 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0026 (IC base=+0.127)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.158 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0031 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.286 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.3033` → IC=+0.240 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3033 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.2615` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2615 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.71` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.71 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6694` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6694 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.9205` → IC=+0.151 (n=104)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.9205 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1588` → IC=+0.181 (n=114)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1588 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.8608` → IC=+0.223 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.8608 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `11338.6336` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11338.6336 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0017` → IC=+0.216 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0017 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.181 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4191` → IC=+0.220 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4191 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.1378` → IC=+0.182 (n=256)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1378 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.232` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.232 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.3025` → IC=+0.178 (n=237)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.3025 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.856` → IC=+0.181 (n=158)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.856 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.0979` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0979 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5729` → IC=+0.315 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5729 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `5105.835` → IC=+0.182 (n=212)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 5105.835 (IC base=+0.169)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.277 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.322 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.276)

- **PATRÓN** `ibs_20min` < `0.5421` → IC=+0.342 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5421 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.123` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.123 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` < `0.1603` → IC=+0.240 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1603 (IC base=+0.276)

- **PATRÓN** `volumen_pendiente_norm` > `0.3816` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3816 (IC base=+0.276)

- **PATRÓN** `volumen_spike_ratio` < `3.6802` → IC=+0.272 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.6802 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.293 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 35.0 (IC base=+0.276)

### GBM_LATE_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_20min` < `0.3643` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3643
  - _Potencial_: sin este filtro IC_bueno=+0.205 (n=161)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.196 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0019 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.0759` → IC=+0.130 (n=71)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.0759 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.3643` → IC=+0.205 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3643 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.435` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.435 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.499` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 4.499 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.7845` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.7845 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `1.981` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.981 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `7283.8545` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7283.8545 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.097)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1714` → IC=+0.161 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1714 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.228 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1817` → IC=+0.160 (n=183)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1817 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.414` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.414 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.931` → IC=+0.143 (n=222)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 2.931 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.194 (n=106)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.7028 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0809` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.0809 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.9831` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9831 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.7285` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7285 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1404.9736` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1404.9736 (IC base=+0.136)

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

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.286 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.2502` → IC=+0.259 (n=313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2502 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.281 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.1882` → IC=+0.362 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1882 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` > `0.3845` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3845 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.763` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.763 (IC base=+0.258)

- **PATRÓN** `volumen_regimen` > `1.2502` → IC=+0.310 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2502 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.332` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.332 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.5149` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5149 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6958` → IC=+0.277 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6958 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `2852.5264` → IC=+0.260 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2852.5264 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.258)

### GBM_LATE_5M
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=44)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=49)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=204)

- **PATRÓN** `drift_60min` |x|≤ `0.0797` → IC=+0.184 (n=17)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0797 (IC base=-0.022)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.189 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0039 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.237 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.231 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5406` → IC=+0.159 (n=165)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5406 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1765` → IC=+0.151 (n=173)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1765 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.051` → IC=+0.160 (n=148)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.051 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.3953` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.3953 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6656` → IC=+0.153 (n=165)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6656 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.2296` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.2296 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.817` → IC=+0.185 (n=163)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.817 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.4927` → IC=+0.148 (n=163)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4927 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=204)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `8604.1542` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 8604.1542 (IC base=+0.142)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.164 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0033 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.250 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.250 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.1373` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1373 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.318` → IC=+0.185 (n=90)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 6.318 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2758` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2758 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6446` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6446 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.7111` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.7111 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.4927` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4927 (IC base=+0.142)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1802` → IC=+0.312 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1802 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.333 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.2325` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2325 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.688` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.688 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.809` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.809 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `1.1102` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1102 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.1037` → IC=+0.314 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1037 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.8733` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8733 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `8454.4508` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8454.4508 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.233)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `libro_liquidez` < `3889.971` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3889.971
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.123)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0796` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `drift_20min_pct` |x|≤ 0.0796 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.1458` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.1458 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2054.213` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2054.213 (IC base=+0.123)

### MOMENTUM_IBS_15M#BTC#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.071)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0531` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0531 (IC base=+0.071)

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
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 19.0 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.112)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0523` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0523 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `15313.5075` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 15313.5075 (IC base=+0.112)

### MOMENTUM_IBS_15M#XRP#15min
- **PATRÓN** `hora_utc` < `3.0` → IC=+0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.060)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `hora_utc` < `14.0` → IC=-0.134 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=254)

- **FILTRO** `py_entrada` < `0.4` → IC=-0.283 (n=113)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=344)

- **FILTRO** `ibs_20min` < `0.7187` → IC=-0.250 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7187
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=343)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.208 (n=111)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=346)

- **FILTRO** `libro_liquidez` < `2017.8084` → IC=-0.147 (n=301)

  - _Acción_: SKIP cuando `libro_liquidez` < 2017.8084
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=156)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=52)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.243 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=41)

- **FILTRO** `ibs_20min` < `0.8235` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8235
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=37)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=50)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=60)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=59)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=52)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.161 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=34)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=69)

- **FILTRO** `ibs_20min` > `0.2136` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2136
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=70)

- **FILTRO** `ballena_activa_n` > `49.0` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 49.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=69)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.230 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=41)

- **FILTRO** `ibs_20min` < `0.7` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=57)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=55)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.62` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.62 (IC base=+0.076)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=57)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=57)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=56)

- **FILTRO** `libro_liquidez` < `12171.3382` → IC=-0.161 (n=54)

  - _Acción_: SKIP cuando `libro_liquidez` < 12171.3382
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.060)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.5 (IC base=+0.060)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=42)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=58)

- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=58)

- **FILTRO** `ballena_activa_n` > `22.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 22.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=57)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=56)

- **FILTRO** `ibs_20min` < `0.7187` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7187
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=61)

- **FILTRO** `libro_liquidez` < `2529.5412` → IC=-0.173 (n=53)

  - _Acción_: SKIP cuando `libro_liquidez` < 2529.5412
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=64)

- **PATRÓN** `py_entrada` < `0.52` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.52 (IC base=+0.017)

- **PATRÓN** `libro_liquidez` > `2275.4657` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2275.4657 (IC base=+0.017)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=187)

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
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.931` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.931 (IC base=+0.057)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `ibs_20min` < `0.2368` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.043)

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
- **FILTRO** `hora_utc` < `14.0` → IC=-0.155 (n=598)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=680)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.284 (n=303)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=975)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.240 (n=313)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=965)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.187 (n=429)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=849)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.192 (n=332)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1094)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.218 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=103)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.222 (n=95)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=109)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.214 (n=47)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

- **FILTRO** `drift_7min_pct` |x|> `0.0977` → IC=-0.147 (n=66)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0977
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=129)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.187 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=187)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.306 (n=65)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=203)

- **FILTRO** `ibs_7min` < `0.803` → IC=-0.225 (n=67)

  - _Acción_: SKIP cuando `ibs_7min` < 0.803
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=201)

- **FILTRO** `ballena_activa_n` > `111.0` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `ballena_activa_n` > 111.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=202)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.182 (n=61)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=192)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.197 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=97)

- **FILTRO** `py_entrada` < `0.28` → IC=-0.415 (n=45)

  - _Acción_: SKIP cuando `py_entrada` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=139)

- **FILTRO** `ibs_7min` < `0.2525` → IC=-0.242 (n=60)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2525
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=124)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.261 (n=44)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=140)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.206 (n=107)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=123)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.51 (IC base=-0.043)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.207 (n=104)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=113)

- **FILTRO** `ibs_7min` < `0.8284` → IC=-0.214 (n=54)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8284
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=163)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.149 (n=152)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=65)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.120 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=166)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.167 (n=55)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=188)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=180)

- **FILTRO** `py_entrada` < `0.4` → IC=-0.254 (n=59)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=178)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.158 (n=115)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=122)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.221 (n=59)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=178)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.261 (n=90)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=78)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.289 (n=55)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=113)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.291 (n=41)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=127)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.245 (n=49)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=201)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=75)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=98)

- **PATRÓN** `libro_liquidez` > `11036.7223` → IC=+0.128 (n=76)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 11036.7223 (IC base=+0.057)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=208)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=137)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.4015` → IC=+0.158 (n=150)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.4015 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.142 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 18.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `315.516` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 315.516 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.134)

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
- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `libro_liquidez` < `3635.0406` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 3635.0406
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

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
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=75)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=43)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=41)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.167 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 10.0 (IC base=+0.047)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.047)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=76)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=-0.009)

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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=403)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=411)

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

- **PATRÓN** `ibs_15` < `0.4585` → IC=+0.121 (n=404)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.60€ cuando `ibs_15` < 0.4585 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.4806` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.4806 (IC base=+0.083)

### UPDOWN_GBM#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.133 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=139)

- **FILTRO** `ibs_15` < `0.1` → IC=-0.258 (n=64)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=193)

- **FILTRO** `sigma_ewma_delta_pct` > `5.127` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.127
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=193)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

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
- **FILTRO** `ibs_15` < `0.1827` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1827
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `11975.2481` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 11975.2481
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.029` → IC=+0.121 (n=114)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.60€ cuando `pct_spot_vs_ref` |x|≤ 0.029 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.002` → IC=+0.192 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.002 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.1796` → IC=+0.128 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.1796 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.159 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 3.0 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.758` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.758 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `11034.7966` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11034.7966 (IC base=+0.105)

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

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.141 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0026 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.189 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.004 (IC base=+0.137)

- **PATRÓN** `drift_15min` |x|≤ `0.4389` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `drift_15min` |x|≤ 0.4389 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1155` → IC=+0.140 (n=98)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.1155 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.152 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 16.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` < `0.345` → IC=+0.158 (n=109)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.345 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.0316` → IC=+0.182 (n=108)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.0316 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.4696` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4696 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.352` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 23.352 (IC base=+0.137)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `ibs_15` < `0.0681` → IC=-0.200 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0681
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `dist_vwap_pct` > `0.1744` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1744
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **FILTRO** `sigma_ewma_delta_pct` > `5.384` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.384
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=32)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=74)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0094` → IC=+0.122 (n=35)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.61€ cuando `pct_spot_vs_ref` |x|≤ 0.0094 (IC base=+0.065)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.176 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0021 (IC base=+0.065)

- **PATRÓN** `drift_15min` |x|≤ `0.3841` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `drift_15min` |x|≤ 0.3841 (IC base=+0.065)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.211` → IC=+0.128 (n=49)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio_macro` |x|> 0.211 (IC base=+0.060)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.060)

- **PATRÓN** `ibs_15` < `0.1034` → IC=+0.243 (n=33)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1034 (IC base=+0.060)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1495` → IC=+0.192 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1495 (IC base=+0.104)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0979` → IC=+0.154 (n=128)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.0979 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.130 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 19.0 (IC base=+0.104)

- **PATRÓN** `ibs_15` < `0.125` → IC=+0.208 (n=63)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.125 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.138` → IC=+0.145 (n=119)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 5.138 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2604.9815` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2604.9815 (IC base=+0.104)

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
- **FILTRO** `ibs_15` < `0.6429` → IC=-0.242 (n=118)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6429
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=118)

- **FILTRO** `sigma_ewma_delta_pct` > `12.766` → IC=-0.152 (n=234)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.766
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=950)

- **PATRÓN** `ibs_15` > `0.6429` → IC=+0.233 (n=118)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6429 (IC base=-0.048)

- **PATRÓN** `ibs_15` < `0.53` → IC=+0.271 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.53 (IC base=-0.051)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.0929 (IC base=-0.051)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.238 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=176)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.224 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=202)

- **FILTRO** `libro_liquidez` < `13596.8271` → IC=-0.213 (n=193)

  - _Acción_: SKIP cuando `libro_liquidez` < 13596.8271
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=65)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.121 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.043)

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
- **FILTRO** `sigma_ewma_delta_pct` > `13.905` → IC=-0.182 (n=64)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.905
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=363)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.659` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.659 (IC base=-0.015)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.0051` → IC=-0.160 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=104)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.163 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=59)

- **FILTRO** `libro_liquidez` < `2490.4522` → IC=-0.200 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 2490.4522
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

- **FILTRO** `sigma_ewma_delta_pct` > `7.734` → IC=-0.149 (n=92)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.734
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=295)

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

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.1034 sube el IC de +0.060 a +0.243 en UPDOWN_GBM#SOL#5min (n=33). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.102 a +0.227 en UPDOWN_GBM#15min (n=284). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.130 a +0.250 en UPDOWN_GBM#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.7055 sube el IC de +0.100 a +0.337 en UPDOWN_GBM#ETH#15min (n=47). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.345 sube el IC de +0.137 a +0.158 en UPDOWN_GBM#ETH#15min (n=109). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS > 0.0316 sube el IC de +0.137 a +0.182 en UPDOWN_GBM#ETH#15min (n=108). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.085 a +0.182 en UPDOWN_GBM#XRP#15min (n=86). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.125 sube el IC de +0.104 a +0.208 en UPDOWN_GBM#XRP#15min (n=63). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6429 sube el IC de -0.048 a +0.233 en UPDOWN_GBM_15M_TARDIO (n=118). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.53 sube el IC de -0.051 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=46). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
| ✅ BALLENAS_TARDIAS | 3508 | -0.114 | -541.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 465 | -0.022 | -18.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 3043 | -0.128 | -523.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 407 | -0.190 | -93.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 407 | -0.190 | -93.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 465 | -0.022 | -18.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 465 | -0.022 | -18.06€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 313 | -0.157 | -149.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 313 | -0.157 | -149.27€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 857 | +0.004 | -106.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 857 | +0.004 | -106.76€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 741 | -0.224 | -134.46€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 741 | -0.224 | -134.46€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 15081 | +0.115 | -869.95€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3478 | +0.183 | -92.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 100 | -0.098 | -46.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 8887 | +0.086 | -762.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2616 | +0.133 | +32.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1500 | +0.029 | -331.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 14 | -0.044 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1482 | +0.032 | -325.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3402 | +0.142 | +8.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 951 | +0.200 | -26.01€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 41 | -0.105 | -20.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1480 | +0.113 | -9.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 930 | +0.140 | +64.35€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1498 | +0.056 | -257.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 10 | +0.000 | -3.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1487 | +0.057 | -252.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3677 | +0.126 | -44.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1284 | +0.162 | -16.38€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1476 | +0.102 | -27.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 905 | +0.118 | +7.49€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3509 | +0.136 | -199.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1207 | +0.198 | -48.98€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 41 | +0.012 | -8.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1480 | +0.086 | -102.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 781 | +0.142 | -39.29€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1495 | +0.123 | -44.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1482 | +0.124 | -44.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3542 | +0.159 | -348.57€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3542 | +0.159 | -348.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 887 | +0.156 | -114.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 887 | +0.156 | -114.51€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 78 | -0.113 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 78 | -0.113 | -5.72€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 878 | +0.156 | -113.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 878 | +0.156 | -113.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 788 | +0.216 | -44.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 788 | +0.216 | -44.69€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 832 | +0.172 | -83.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 832 | +0.172 | -83.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 173 | +0.409 | -11.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 173 | +0.409 | -11.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 62 | +0.406 | -3.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 62 | +0.406 | -3.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 67 | +0.384 | -6.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 67 | +0.384 | -6.82€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 42 | +0.409 | -1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 42 | +0.409 | -1.47€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 6313 | +0.188 | -599.82€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 6313 | +0.188 | -599.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1182 | +0.096 | -267.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1182 | +0.096 | -267.92€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 970 | +0.247 | -10.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 970 | +0.247 | -10.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1108 | +0.155 | -156.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1108 | +0.155 | -156.47€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1015 | +0.222 | -42.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1015 | +0.222 | -42.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 982 | +0.245 | -13.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 982 | +0.245 | -13.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1056 | +0.183 | -108.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1056 | +0.183 | -108.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2277 | +0.147 | +117.70€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 2277 | +0.147 | +117.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1125 | +0.153 | +70.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1125 | +0.153 | +70.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1152 | +0.140 | +47.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1152 | +0.140 | +47.54€ | 0 | 7 |
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
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 257 | +0.257 | -31.92€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 257 | +0.257 | -31.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 257 | +0.257 | -31.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 257 | +0.257 | -31.92€ | 0 | 5 |
| ✅ GBM_LATE_15M | 4657 | +0.086 | +1652.41€ | 0 | 14 |
| ✅ GBM_LATE_15M#15min | 4657 | +0.086 | +1652.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 813 | +0.176 | +515.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 813 | +0.176 | +515.85€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 463 | +0.180 | +235.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 463 | +0.180 | +235.13€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 820 | +0.190 | +558.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 820 | +0.190 | +558.77€ | 0 | 16 |
| ✅ GBM_LATE_15M#ETH | 618 | -0.002 | +35.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 618 | -0.002 | +35.81€ | 0 | 3 |
| ✅ GBM_LATE_15M#SOL | 869 | +0.003 | +80.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 869 | +0.003 | +80.44€ | 3 | 5 |
| ✅ GBM_LATE_15M#XRP | 1074 | +0.013 | +226.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1074 | +0.013 | +226.40€ | 0 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5681 | +0.049 | +1697.65€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5681 | +0.049 | +1697.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1088 | -0.029 | +198.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1088 | -0.029 | +198.31€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1080 | -0.012 | +94.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1080 | -0.012 | +94.36€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 693 | +0.240 | +631.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 693 | +0.240 | +631.83€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 992 | -0.019 | +8.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 992 | -0.019 | +8.27€ | 7 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1006 | +0.001 | +97.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1006 | +0.001 | +97.11€ | 3 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 822 | +0.214 | +667.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 822 | +0.214 | +667.77€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3405 | +0.176 | +2308.46€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3405 | +0.176 | +2308.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 607 | +0.191 | +440.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 607 | +0.191 | +440.99€ | 0 | 17 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 453 | +0.195 | +298.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 453 | +0.195 | +298.18€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 603 | +0.203 | +469.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 603 | +0.203 | +469.82€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 425 | +0.207 | +307.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 425 | +0.207 | +307.90€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 633 | +0.075 | +256.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 633 | +0.075 | +256.64€ | 1 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 684 | +0.198 | +534.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 684 | +0.198 | +534.93€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 574 | +0.050 | +50.70€ | 0 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 574 | +0.050 | +50.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 106 | +0.037 | -6.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 106 | +0.037 | -6.05€ | 2 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 119 | +0.161 | +41.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 119 | +0.161 | +41.72€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 227 | -0.007 | +7.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 227 | -0.007 | +7.58€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 121 | +0.061 | +8.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 121 | +0.061 | +8.72€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO | 3964 | +0.168 | +2561.41€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3964 | +0.168 | +2561.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 783 | +0.185 | +546.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 783 | +0.185 | +546.75€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 522 | +0.153 | +271.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 522 | +0.153 | +271.11€ | 1 | 22 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 771 | +0.218 | +638.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 771 | +0.218 | +638.79€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 370 | +0.124 | +153.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 370 | +0.124 | +153.39€ | 1 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 636 | +0.077 | +277.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 636 | +0.077 | +277.67€ | 0 | 15 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 882 | +0.200 | +673.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 882 | +0.200 | +673.70€ | 0 | 25 |
| ✅ GBM_LATE_5M | 284 | +0.105 | +102.01€ | 3 | 14 |
| ✅ GBM_LATE_5M#5min | 284 | +0.105 | +102.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 150 | +0.105 | +51.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 150 | +0.105 | +51.72€ | 0 | 11 |
| ✅ GBM_LATE_5M#ETH | 78 | +0.200 | +46.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 78 | +0.200 | +46.83€ | 0 | 11 |
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
| ✅ LIQUIDACIONES_5M | 95 | -0.119 | -12.96€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 95 | -0.119 | -12.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 34 | -0.028 | -1.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 34 | -0.028 | -1.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 22 | -0.125 | -3.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 22 | -0.125 | -3.36€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 16 | -0.178 | -4.14€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 16 | -0.178 | -4.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 301 | -0.002 | -6.28€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 301 | -0.002 | -6.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 102 | -0.010 | -7.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 102 | -0.010 | -7.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 98 | -0.010 | -1.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 98 | -0.010 | -1.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 101 | +0.015 | +2.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 101 | +0.015 | +2.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 713 | +0.033 | +15.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 713 | +0.033 | +15.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 107 | +0.060 | +13.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 107 | +0.060 | +13.64€ | 1 | 5 |
| ✅ MOMENTUM_IBS_15M#BTC | 125 | +0.075 | +14.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 125 | +0.075 | +14.35€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M#DOGE | 112 | +0.018 | -10.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 112 | +0.018 | -10.12€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 129 | +0.065 | +22.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 129 | +0.065 | +22.63€ | 0 | 4 |
| ✅ MOMENTUM_IBS_15M#SOL | 118 | -0.033 | -19.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 118 | -0.033 | -19.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 122 | +0.008 | -6.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 122 | +0.008 | -6.05€ | 0 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 975 | -0.042 | +4.63€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 975 | -0.042 | +4.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 154 | -0.051 | +16.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 154 | -0.051 | +16.66€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 169 | -0.073 | -20.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 169 | -0.073 | -20.40€ | 7 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 159 | +0.003 | +34.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 159 | +0.003 | +34.09€ | 3 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 171 | -0.015 | -5.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 171 | -0.015 | -5.57€ | 4 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 156 | -0.063 | -9.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 156 | -0.063 | -9.01€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 166 | -0.048 | -11.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 166 | -0.048 | -11.14€ | 4 | 2 |
| ✅ MOMENTUM_IBS_15M_FADE | 345 | -0.050 | -21.17€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 345 | -0.050 | -21.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 54 | -0.018 | -1.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 54 | -0.018 | -1.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 50 | -0.154 | -8.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 50 | -0.154 | -8.53€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 66 | -0.088 | -6.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 66 | -0.088 | -6.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 80 | +0.012 | +0.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 80 | +0.012 | +0.44€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 67 | +0.007 | +0.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 67 | +0.007 | +0.06€ | 1 | 1 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 2704 | -0.064 | +79.63€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 2704 | -0.064 | +79.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 399 | -0.099 | +23.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 399 | -0.099 | +23.76€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 521 | -0.054 | +72.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 521 | -0.054 | +72.91€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 414 | -0.067 | -9.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 414 | -0.067 | -9.56€ | 5 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 460 | -0.076 | -27.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 460 | -0.076 | -27.55€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 492 | -0.041 | -4.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 492 | -0.041 | -4.43€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 418 | -0.055 | +24.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 418 | -0.055 | +24.50€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 2405 | +0.015 | +14.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 2405 | +0.015 | +14.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 403 | +0.018 | +8.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 403 | +0.018 | +8.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 339 | +0.037 | +6.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 339 | +0.037 | +6.36€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 413 | +0.006 | -2.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 413 | +0.006 | -2.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 424 | +0.007 | +1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 424 | +0.007 | +1.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 430 | +0.009 | +0.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 430 | +0.009 | +0.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 396 | +0.018 | +0.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 396 | +0.018 | +0.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 238 | +0.083 | +44.36€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 102 | +0.115 | +31.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 29 | +0.210 | +22.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 29 | +0.210 | +22.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 18 | +0.045 | +2.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 18 | +0.045 | +2.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 8 | +0.040 | +3.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 8 | +0.040 | +3.01€ | 0 | 0 |
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
| ✅ STREAK_FADE_5M | 374 | -0.024 | -20.78€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 374 | -0.024 | -20.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 104 | +0.019 | +1.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 104 | +0.019 | +1.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 127 | -0.012 | -7.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 127 | -0.012 | -7.16€ | 2 | 0 |
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
| ✅ STREAK_MOM_5M | 633 | +0.018 | -0.63€ | 1 | 0 |
| ✅ STREAK_MOM_5M#5min | 633 | +0.018 | -0.63€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 205 | +0.017 | -1.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 205 | +0.017 | -1.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 118 | -0.017 | -4.28€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 118 | -0.017 | -4.28€ | 3 | 2 |
| ✅ STREAK_MOM_5M#SOL | 164 | +0.024 | +0.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 164 | +0.024 | +0.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 146 | +0.041 | +4.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 146 | +0.041 | +4.24€ | 1 | 2 |
| ✅ STRUCT_NO_15M | 1907 | +0.017 | -1.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1907 | +0.017 | -1.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 725 | +0.008 | -7.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 725 | +0.008 | -7.96€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 747 | +0.022 | +3.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 747 | +0.022 | +3.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 435 | +0.024 | +3.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 435 | +0.024 | +3.47€ | 2 | 0 |
| ✅ UPDOWN_GBM | 2403 | +0.029 | +191.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1035 | +0.091 | +200.29€ | 1 | 8 |
| ✅ UPDOWN_GBM#240min | 124 | +0.016 | -0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 941 | -0.011 | +2.01€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 256 | -0.023 | -10.57€ | 4 | 1 |
| ✅ UPDOWN_GBM#BNB | 104 | +0.123 | +27.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 97 | +0.146 | +28.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6 | -0.075 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 453 | +0.032 | +33.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 129 | +0.057 | -0.98€ | 2 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 38 | +0.075 | +3.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 182 | +0.065 | +37.38€ | 2 | 6 |
| ✅ UPDOWN_GBM#BTC#60min | 86 | -0.057 | -8.56€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 306 | +0.000 | -1.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 63 | +0.115 | +14.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 243 | -0.031 | -16.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 557 | +0.055 | +58.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 237 | +0.123 | +56.47€ | 1 | 14 |
| ✅ UPDOWN_GBM#ETH#240min | 38 | +0.050 | +1.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 163 | +0.009 | +2.66€ | 4 | 3 |
| ✅ UPDOWN_GBM#ETH#60min | 104 | +0.009 | -1.14€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 441 | -0.001 | +5.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 191 | +0.023 | +6.14€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 30 | -0.031 | -2.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 142 | +0.007 | +2.72€ | 2 | 3 |
| ✅ UPDOWN_GBM#SOL#60min | 66 | -0.029 | -0.87€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 540 | +0.024 | +69.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 318 | +0.097 | +94.77€ | 0 | 14 |
| ✅ UPDOWN_GBM#XRP#240min | 17 | -0.112 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 205 | -0.075 | -22.40€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 112 | +0.254 | -0.89€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 112 | +0.254 | -0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 73 | +0.220 | -8.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 73 | +0.220 | -8.37€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 39 | +0.305 | +7.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 39 | +0.305 | +7.48€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1739 | -0.050 | +219.04€ | 2 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1739 | -0.050 | +219.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 121 | -0.077 | +0.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 121 | -0.077 | +0.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 337 | -0.140 | -17.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 337 | -0.140 | -17.77€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 42 | +0.000 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 42 | +0.000 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 134 | +0.000 | +19.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 134 | +0.000 | +19.88€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 563 | -0.015 | +142.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 563 | -0.015 | +142.99€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 542 | -0.040 | +70.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 542 | -0.040 | +70.75€ | 4 | 0 |
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