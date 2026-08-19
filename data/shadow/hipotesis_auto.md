# Hipótesis automáticas — 2026-08-19 08:04 UTC
_Generado por shadow_postmortem.py sobre 73401 resoluciones (PNL=+7706.64€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.355` → IC=-0.143 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=150)

- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.227 (n=53)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.183 (n=165)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=212)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.241 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.082)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.082)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.183 (n=165)

  - _Acción_: Kelly boost +0.91€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.082)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=212)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.016)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `banda_hit_calibrado` < `0.6142` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6142
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=82)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.338 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=111)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.091)

- **PATRÓN** `n_total_lado` > `94.0` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 94.0 (IC base=+0.091)

- **PATRÓN** `banda_hit_calibrado` > `0.6142` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `banda_hit_calibrado` > 0.6142 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.132 (n=85)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.485 (IC base=+0.007)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=85)

- **FILTRO** `banda_hit_calibrado` < `0.6274` → IC=-0.210 (n=36)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6274
  - _Potencial_: sin este filtro IC_bueno=+0.210 (n=74)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=86)

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

- **PATRÓN** `py_entrada` > `0.33` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.33 (IC base=+0.071)

- **PATRÓN** `banda_hit_calibrado` > `0.6274` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6274 (IC base=+0.071)

- **PATRÓN** `banda_z` > `8.673` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.673 (IC base=+0.071)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.071)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `154.88` → IC=-0.247 (n=979)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.88
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2937)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `119.16` → IC=-0.405 (n=103)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.16
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=312)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `641.55` → IC=-0.290 (n=117)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 641.55
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=354)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `47.34` → IC=-0.485 (n=132)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 47.34
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=268)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `concentracion_yes` < `1.0` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `concentracion_yes` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=892)

- **FILTRO** `n_ballenas` < `4.0` → IC=-0.148 (n=231)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=729)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `155.26` → IC=-0.296 (n=194)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 155.26
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=583)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.183 (n=2510)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.7 (IC base=+0.088)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=1185)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `2371.8003` → IC=+0.168 (n=1145)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2371.8003 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=4588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=3068)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.288 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=2065)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `4055.5019` → IC=+0.183 (n=844)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4055.5019 (IC base=+0.153)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.365 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.301 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.153 (n=347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` > `0.6` → IC=+0.174 (n=185)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.6 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `5033.4098` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5033.4098 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.201 (n=165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.219 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `5287.6073` → IC=+0.176 (n=211)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5287.6073 (IC base=+0.141)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.144 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 11.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.320 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.314 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.403 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `3334.5877` → IC=+0.359 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3334.5877 (IC base=+0.300)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.172 (n=251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 16.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.238 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=277)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2164.5524` → IC=+0.168 (n=275)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2164.5524 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.121 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5700.7138` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5700.7138 (IC base=+0.097)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.187 (n=506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.398 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.276 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` < `0.31` → IC=+0.344 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.31 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `900.209` → IC=+0.243 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 900.209 (IC base=+0.230)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.256 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.194 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 13.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.340 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3467.6863` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3467.6863 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=259)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=65)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=96)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=1249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.197 (n=949)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.75 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.160 (n=622)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 15.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.75` → IC=+0.170 (n=711)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.75 (IC base=+0.153)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.176 (n=313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.183 (n=235)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.7 (IC base=+0.154)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.237 (n=412)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.321 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.218)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.250 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=59)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.199 (n=300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.188 (n=520)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.72 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.430 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.418 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.410)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.410)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.413 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.409 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.408)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.435 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.408)

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
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.185 (n=3445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.217 (n=3515)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.182)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.298 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.311 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.238)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.156 (n=318)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 5.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.212 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.150)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.218 (n=804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.288 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.275 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.241)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.178 (n=579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 11.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.228 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.223 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.149)

- **PATRÓN** `restante_min` < `3.8` → IC=+0.164 (n=594)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` < 3.8 (IC base=+0.149)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.208 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=1817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.157 (n=1792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 17.0 (IC base=+0.149)

- **PATRÓN** `lag_apertura_s` < `5.61` → IC=+0.209 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.61 (IC base=+0.149)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.236 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.154)

- **PATRÓN** `restante_min` < `3.74` → IC=+0.170 (n=295)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` < 3.74 (IC base=+0.154)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.195 (n=313)

  - _Acción_: Kelly boost +0.98€ cuando `restante_min` > 4.88 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=901)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=783)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `lag_apertura_s` < `7.33` → IC=+0.202 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 7.33 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.43` → IC=+0.174 (n=798)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.43 (IC base=+0.144)

- **PATRÓN** `restante_min` < `3.88` → IC=+0.156 (n=300)

  - _Acción_: Kelly boost +0.78€ cuando `restante_min` < 3.88 (IC base=+0.144)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.207 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.94 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.155 (n=907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `lag_apertura_s` < `3.32` → IC=+0.221 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.32 (IC base=+0.144)

- **PATRÓN** `profundidad_ratio_no` > `10.8` → IC=+0.151 (n=299)

  - _Acción_: Kelly boost +0.76€ cuando `profundidad_ratio_no` > 10.8 (IC base=+0.144)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.313 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.312 (n=430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.387 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.277 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.273)

- **PATRÓN** `py_entrada` < `0.725` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.725 (IC base=+0.273)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `3909.8054` → IC=+0.284 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3909.8054 (IC base=+0.273)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.313 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.320 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.302)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.399 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.305 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `1873.4324` → IC=+0.314 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1873.4324 (IC base=+0.302)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.447 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.379)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.379)

- **PATRÓN** `libro_liquidez` > `909.4383` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 909.4383 (IC base=+0.379)

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
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.291 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.260)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.387 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.277 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1397.8324` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1397.8324 (IC base=+0.260)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.291 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.260)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.387 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.277 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1397.8324` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1397.8324 (IC base=+0.260)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.271 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.4164` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4164 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.673` → IC=+0.235 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.673 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.279` → IC=+0.244 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.279 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.646` → IC=+0.244 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.646 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.6654` → IC=+0.123 (n=2248)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6654 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.2419` → IC=+0.143 (n=595)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2419 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `1.3132` → IC=+0.142 (n=507)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.3132 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `0.6966` → IC=+0.142 (n=453)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6966 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.3324` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3324 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.5637` → IC=+0.262 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5637 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.8665` → IC=+0.237 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8665 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.293 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.174 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0074 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.162 (n=288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.9185` → IC=+0.285 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9185 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.363` → IC=+0.342 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.363 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.153 (n=318)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.06 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.319 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.333 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.1274` → IC=+0.347 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1274 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.290 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.295 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.286)

- **PATRÓN** `ibs_20min` < `0.5701` → IC=+0.328 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5701 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.321 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.286)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` < `1.7987` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7987 (IC base=+0.286)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.332 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1980.3` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1980.3 (IC base=+0.286)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.286)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.346 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.269 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.0774` → IC=+0.265 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0774 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` > `0.7272` → IC=+0.294 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7272 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.3145` → IC=+0.333 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3145 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.34` → IC=+0.350 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.34 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` < `1.3738` → IC=+0.289 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3738 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` > `0.7626` → IC=+0.265 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7626 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.1734` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1734 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `2.7036` → IC=+0.311 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7036 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `13015.3205` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13015.3205 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `369.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 369.0 (IC base=+0.267)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.174 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0018 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.158 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0029 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1861` → IC=+0.177 (n=221)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1861 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.185 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 12.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.4787` → IC=+0.204 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4787 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1415` → IC=+0.168 (n=272)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1415 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.365` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.365 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2895` → IC=+0.168 (n=251)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2895 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.6842` → IC=+0.164 (n=224)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6842 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.1879` → IC=+0.195 (n=149)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1879 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1063` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1063 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.5138` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5138 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `12777.1965` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 12777.1965 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 197.0 (IC base=+0.149)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.185 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0075 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.132 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.285 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.146 (n=427)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.06 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `1917.6878` → IC=+0.142 (n=174)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1917.6878 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.337 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.291 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.314 (n=84)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.289 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=258)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `ibs_20min` < `0.5025` → IC=+0.314 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5025 (IC base=+0.288)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` < `4.5585` → IC=+0.277 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.5585 (IC base=+0.288)

- **PATRÓN** `volumen_spike_ratio` > `2.9594` → IC=+0.282 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9594 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.291 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.288)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `9.896` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.896 (IC base=+0.038)

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
- **PATRÓN** `sigma_ewma_delta_pct` > `8.156` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 8.156 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` < `0.7863` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.7863 (IC base=-0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1797` → IC=+0.226 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1797 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6986 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `1.3906` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3906 (IC base=+0.030)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `ibs_20min` > `0.9425` → IC=+0.236 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9425 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.3483` → IC=+0.190 (n=85)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3483 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.204` → IC=+0.128 (n=1048)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.204 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.0912` → IC=+0.122 (n=625)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.0912 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.3408` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.3408 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` > `2.9129` → IC=+0.168 (n=314)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.9129 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.253 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.169 (n=885)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.4844` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4844 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.196 (n=205)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.7156 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` > `1.2602` → IC=+0.213 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2602 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.3468` → IC=+0.352 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3468 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `3.7273` → IC=+0.323 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7273 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.286 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.049)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.939` → IC=-0.206 (n=107)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.939
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=544)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.382` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.382 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0503` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0503 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.3584` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.3584 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` < `0.0377` → IC=-0.174 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0377
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=271)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=344)

- **PATRÓN** `volumen_regimen` < `0.5591` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5591 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.1352` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1352 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.290 (n=122)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0611` → IC=+0.218 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0611 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.263 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.924` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.924 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` < `0.1444` → IC=+0.188 (n=264)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1444 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.4263` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4263 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `3.9529` → IC=+0.202 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.9529 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.196 (n=399)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.06 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `1914.9184` → IC=+0.202 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.9184 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.402 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.372)

- **PATRÓN** `drift_60min` |x|≤ `0.1764` → IC=+0.378 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1764 (IC base=+0.372)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.397 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.372)

- **PATRÓN** `ibs_20min` < `0.3009` → IC=+0.389 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3009 (IC base=+0.372)

- **PATRÓN** `ibs_20min` > `0.0514` → IC=+0.369 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0514 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` < `0.3211` → IC=+0.402 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3211 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` > `0.1384` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1384 (IC base=+0.372)

- **PATRÓN** `volumen_spike_ratio` < `2.9764` → IC=+0.444 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9764 (IC base=+0.372)

- **PATRÓN** `libro_liquidez` > `1874.461` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.461 (IC base=+0.372)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.623` → IC=-0.123 (n=165)

  - _Acción_: SKIP cuando `ibs_20min` < 0.623
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=85)

- **FILTRO** `dist_vwap_pct` < `0.3632` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3632
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

- **FILTRO** `volumen_regimen` > `0.8629` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8629
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **FILTRO** `libro_liquidez` < `8647.6879` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 8647.6879
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=188)

- **FILTRO** `volumen_regimen` > `0.7318` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.7318
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=711)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.4444` → IC=-0.154 (n=151)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=153)

- **FILTRO** `dist_vwap_pct` > `0.1358` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1358
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=41)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.75 (IC base=-0.016)

- **PATRÓN** `dist_vwap_pct` > `0.1776` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1776 (IC base=-0.016)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.298 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.157 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.228 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.326` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.326 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.128` → IC=+0.228 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.128 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.5938` → IC=+0.153 (n=306)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.5938 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.3138` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3138 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.7671` → IC=+0.128 (n=111)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7671 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.6656` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.6656 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=311)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2468.9826` → IC=+0.141 (n=274)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2468.9826 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.278 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.288 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.327 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.3243` → IC=+0.329 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3243 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.5126` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5126 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.885` → IC=+0.282 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.885 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` > `0.8948` → IC=+0.313 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8948 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.3405` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3405 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `3.4615` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4615 (IC base=+0.277)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.160 (n=445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0046 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.195 (n=607)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0066 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0907` → IC=+0.143 (n=587)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.0907 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=601)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.9197` → IC=+0.254 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9197 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.2233` → IC=+0.160 (n=307)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.2233 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.948` → IC=+0.268 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.948 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.142 (n=694)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1861 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.142 (n=693)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6297 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.11` → IC=+0.157 (n=453)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.11 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.148 (n=1338)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.05 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2716.8736` → IC=+0.180 (n=445)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2716.8736 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.221 (n=1306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.2896` → IC=+0.217 (n=1304)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2896 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.266 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.3777` → IC=+0.277 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3777 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.567` → IC=+0.230 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.567 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2517` → IC=+0.189 (n=1008)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.2517 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8751` → IC=+0.196 (n=672)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.8751 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2701` → IC=+0.266 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2701 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.6779` → IC=+0.227 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6779 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `3.1117` → IC=+0.246 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1117 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.233 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 134.0 (IC base=+0.212)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.155 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0058 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.214 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.331 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.482` → IC=+0.366 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.482 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1402` → IC=+0.141 (n=76)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1402 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.186 (n=262)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.298 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.312 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.2108` → IC=+0.331 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2108 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.314 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.4194` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4194 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.0686` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0686 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.8142` → IC=+0.387 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8142 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.372 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1966.1335` → IC=+0.375 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.1335 (IC base=+0.290)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0017` → IC=+0.275 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0017 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.250 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6923` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6923 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.2785` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2785 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.48` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.48 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.3738` → IC=+0.228 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3738 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.7639` → IC=+0.216 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7639 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.0992` → IC=+0.256 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0992 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4774` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4774 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `11869.8733` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11869.8733 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.198 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0033 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.190 (n=217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.002 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1881` → IC=+0.213 (n=214)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1881 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.235 (n=168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.2977` → IC=+0.239 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2977 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.472` → IC=+0.282 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.472 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.8681` → IC=+0.220 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8681 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1937` → IC=+0.213 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1937 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.6134` → IC=+0.290 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6134 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `12777.1965` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12777.1965 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `221.0` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 221.0 (IC base=+0.189)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.198 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0076 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.144` → IC=+0.154 (n=206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.144 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.212 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.326 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.2317` → IC=+0.135 (n=247)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.2317 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.0183` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0183 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.143 (n=113)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.178 (n=240)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.04 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `1962.7584` → IC=+0.167 (n=103)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1962.7584 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 27.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.339 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.307)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.318 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1156` → IC=+0.361 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1156 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.329 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.3388` → IC=+0.332 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3388 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.45` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.45 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3308` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3308 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` < `4.3528` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.3528 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.1707` → IC=+0.308 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1707 (IC base=+0.307)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.306 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.254 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.1663` → IC=+0.300 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1663 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.262 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.268 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `0.6507` → IC=+0.316 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6507 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` < `0.3604` → IC=+0.279 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3604 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.328` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.328 (IC base=+0.250)

- **PATRÓN** `volumen_regimen` > `0.6636` → IC=+0.277 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6636 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.1967` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1967 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.6992` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6992 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `2.4116` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4116 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.266 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `10076.1613` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10076.1613 (IC base=+0.250)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.250)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.253 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.1364` → IC=+0.196 (n=156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1364 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.227 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.332` → IC=+0.254 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.332 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.362` → IC=+0.262 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.362 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.2379` → IC=+0.215 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2379 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.0843` → IC=+0.209 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0843 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `1.9183` → IC=+0.264 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9183 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=266)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `3166.7394` → IC=+0.188 (n=155)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3166.7394 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 103.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.375` → IC=-0.198 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.254 (n=226)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8667 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.042)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.227 (n=86)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.142 (n=266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 4.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.254 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.5497` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.5497 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.974` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.974 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` > `0.8699` → IC=+0.145 (n=170)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.8699 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.1184` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1184 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` > `2.2808` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.2808 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2080.7013` → IC=+0.170 (n=116)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2080.7013 (IC base=+0.102)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.250 (n=114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.2133` → IC=+0.144 (n=220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.2133 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.178 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.228 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.312` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.312 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.068` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.068 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.38` → IC=+0.233 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.38 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1238` → IC=+0.143 (n=250)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1238 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.5999` → IC=+0.127 (n=250)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.5999 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.1987` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1987 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `3.0538` → IC=+0.131 (n=215)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 3.0538 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=258)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2472.2755` → IC=+0.146 (n=224)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2472.2755 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.277 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.256 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.259 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.2453` → IC=+0.318 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2453 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` > `0.1521` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1521 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.43` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.43 (IC base=+0.255)

- **PATRÓN** `volumen_regimen` > `0.8907` → IC=+0.297 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8907 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.3437` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3437 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `3.7273` → IC=+0.308 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7273 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `2699.3874` → IC=+0.258 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2699.3874 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.255)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` > `0.9601` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.9601 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.863` → IC=+0.259 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.863 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.047)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.311 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.068)

- **PATRÓN** `drift_60min` |x|≤ `0.163` → IC=+0.128 (n=143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.163 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.128 (n=189)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.3846 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.859` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.859 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.6134` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.6134 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.068)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `ibs_20min` < `0.5377` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5377
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.5377 (IC base=-0.083)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.254 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2699` → IC=+0.202 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2699 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.183 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 3.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.211 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.2561` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2561 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.208` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.208 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2986` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.2986 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.7418` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.7418 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1153` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1153 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.6449` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6449 (IC base=+0.167)

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

- **PATRÓN** `dist_vwap_pct` < `0.1367` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1367 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.121` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.121 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8238` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8238 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `10039.916` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10039.916 (IC base=+0.132)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1589` → IC=-0.174 (n=44)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1589
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=45)

- **FILTRO** `ibs_20min` > `0.6154` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6154
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

- **FILTRO** `dist_vwap_pct` > `0.177` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.177
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=72)

- **FILTRO** `volumen_pendiente_norm` > `0.0819` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0819
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=44)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.127 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 14.0 (IC base=+0.027)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 1.0 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.14` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 8.14 (IC base=+0.027)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.191 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0059 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.7714` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.7714 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.99` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.99 (IC base=+0.070)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.070)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0588 (IC base=+0.042)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.195 (n=533)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0068 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.142 (n=602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.9631` → IC=+0.282 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9631 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.3442` → IC=+0.186 (n=183)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3442 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.251` → IC=+0.233 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.251 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.1804` → IC=+0.135 (n=379)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.1804 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.6907` → IC=+0.122 (n=1152)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.6907 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.126 (n=1794)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.06 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2767.3045` → IC=+0.162 (n=533)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2767.3045 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.185 (n=220)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 147.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.232 (n=1285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.219)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.223 (n=1462)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.230 (n=1550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.5082` → IC=+0.282 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5082 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.1531` → IC=+0.196 (n=954)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1531 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.002` → IC=+0.254 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.002 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.473` → IC=+0.224 (n=1370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.473 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `0.6189` → IC=+0.205 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6189 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `1.229` → IC=+0.212 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.229 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` < `0.1112` → IC=+0.237 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1112 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.252` → IC=+0.259 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.252 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `2.0257` → IC=+0.260 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0257 (IC base=+0.219)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.208 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.157 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.9474` → IC=+0.289 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9474 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.136` → IC=+0.356 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.136 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2113` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2113 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.158 (n=296)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.06 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.310 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.297 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.332 (n=176)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.299 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.309 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.337 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.319 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.88` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.88 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.8175` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8175 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.324 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1981.9582` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.9582 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.291)

### GBM_LATE_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_20min` < `0.3232` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3232
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=162)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.173 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0026 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.162 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0031 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.286 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.3232` → IC=+0.250 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3232 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3501` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3501 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.337` → IC=+0.283 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.337 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6694` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6694 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.9222` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.9222 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1584` → IC=+0.197 (n=120)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1584 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.9369` → IC=+0.237 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9369 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `12045.4998` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12045.4998 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.206 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1869` → IC=+0.191 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1869 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.4082` → IC=+0.228 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4082 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1435` → IC=+0.195 (n=267)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1435 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.3` → IC=+0.255 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.3 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.2979` → IC=+0.187 (n=244)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.2979 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.8592` → IC=+0.191 (n=163)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.8592 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.1081` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1081 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.5501` → IC=+0.324 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5501 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `5224.4606` → IC=+0.196 (n=218)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 5224.4606 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `262.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 262.0 (IC base=+0.179)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.241 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.244 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.312 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.239` → IC=+0.168 (n=248)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.239 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.1812` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1812 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `4.9893` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 4.9893 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.189 (n=345)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.06 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1854.4986` → IC=+0.187 (n=212)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1854.4986 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.331 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.265)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.273 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.282 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` < `0.5575` → IC=+0.339 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5575 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.093` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.093 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.219 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.3976` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3976 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `2.5357` → IC=+0.271 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5357 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.265)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 18.0 (IC base=+0.265)

### GBM_LATE_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_20min` < `0.3665` → IC=-0.202 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3665
  - _Potencial_: sin este filtro IC_bueno=+0.208 (n=166)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.178 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0019 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.140 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.3665` → IC=+0.208 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3665 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.4312` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4312 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.325` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.325 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.7845` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7845 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.1223` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1223 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2893` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2893 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.9911` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9911 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `7345.5998` → IC=+0.256 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7345.5998 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `189.0` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 189.0 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.221 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2298` → IC=+0.167 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2298 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.1347` → IC=+0.282 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1347 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1103` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1103 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.713` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.713 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.9197` → IC=+0.193 (n=112)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.9197 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` < `0.1393` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1393 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.797` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.797 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `4951.8866` → IC=+0.200 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4951.8866 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.167)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.743` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.743 (IC base=+0.022)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.209 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1743` → IC=+0.161 (n=163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1743 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.221 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1779` → IC=+0.147 (n=188)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1779 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.399` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.399 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.347` → IC=+0.136 (n=251)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.347 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.703` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.703 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `1.0794` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0794 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.1693` → IC=+0.265 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1693 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.9831` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9831 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.6077` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6077 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `1425.2754` → IC=+0.217 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1425.2754 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.199 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.198 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.248 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.3315` → IC=+0.258 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3315 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.293` → IC=+0.216 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.293 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.6695` → IC=+0.145 (n=277)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6695 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1932` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1932 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5848` → IC=+0.131 (n=261)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.5848 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `2477.03` → IC=+0.145 (n=277)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2477.03 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.274 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.3041` → IC=+0.245 (n=370)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3041 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.269 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.301 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4167 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.4796` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4796 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.507` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.507 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `0.883` → IC=+0.283 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.883 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.326` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.326 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` < `1.5095` → IC=+0.221 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5095 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.6744` → IC=+0.258 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6744 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 49.0 (IC base=+0.245)

### GBM_LATE_5M
- **FILTRO** `sigma_h` < `0.0037` → IC=-0.192 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=53)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=241)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.225 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.2471` → IC=+0.192 (n=193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.2471 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.244 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.5506` → IC=+0.172 (n=193)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5506 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.1229` → IC=+0.165 (n=204)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1229 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.803` → IC=+0.170 (n=177)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 5.803 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.1834` → IC=+0.202 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1834 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.6671` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6671 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.179 (n=157)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.941` → IC=+0.223 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.941 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=241)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `7518.5292` → IC=+0.191 (n=192)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7518.5292 (IC base=+0.155)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.198 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0032 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.0847` → IC=+0.288 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0847 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.286 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.6264` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6264 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.805` → IC=+0.200 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.805 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `1.2899` → IC=+0.198 (n=114)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.2899 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.6446` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6446 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `2.9759` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.9759 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `1.4793` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4793 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `9877.829` → IC=+0.181 (n=114)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9877.829 (IC base=+0.173)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.269 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.3626` → IC=+0.250 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3626 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.304 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.2435` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2435 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.773` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.773 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.838` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.838 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.5769` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.5769 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.1284` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1284 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.8878` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8878 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `7268.8224` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7268.8224 (IC base=+0.221)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.161 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=111)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=159)

- **FILTRO** `drift_60min` |x|> `0.0927` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0927
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `ibs_20min` > `0.6471` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6471
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `dist_vwap_pct` > `0.1008` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1008
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

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

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

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
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=59)

- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `volumen_regimen` > `0.903` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.903
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

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

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.380 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=75)

- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=74)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `ibs_20min` > `0.6267` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6267
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `sigma_ewma_delta_pct` > `4.524` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.524
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=26)

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

- **FILTRO** `ibs_20min` < `0.7391` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

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
- **PATRÓN** `hora_utc` < `5.0` → IC=+0.237 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.181)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` < `5.0` → IC=+0.237 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.181)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `17.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
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
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=40)

- **FILTRO** `hora_utc` < `3.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=34)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=29)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `5178.69` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `liq_usd_total` < 5178.69
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9732` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9732
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=62)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=57)

### MOMENTUM_IBS_15M
- **PATRÓN** `hora_utc` < `4.0` → IC=+0.131 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.075)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0648` → IC=+0.153 (n=168)

  - _Acción_: Kelly boost +0.76€ cuando `drift_20min_pct` |x|≤ 0.0648 (IC base=+0.075)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2133.705` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 2133.705
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=34)

- **PATRÓN** `libro_liquidez` > `2261.4863` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2261.4863 (IC base=+0.000)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 4.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.154 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 16.0 (IC base=+0.149)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0662` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0662 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.1731` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1731 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.0968` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.0968 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2061.1835` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2061.1835 (IC base=+0.149)

### MOMENTUM_IBS_15M#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.086)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0383` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0383 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.9851` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.9851 (IC base=+0.086)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.265 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.113)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0531` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0531 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.0568` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0568 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `20101.4917` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20101.4917 (IC base=+0.113)

### MOMENTUM_IBS_15M#DOGE#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `ibs_20min` > `0.8701` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8701
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### MOMENTUM_IBS_15M#ETH#15min
- **PATRÓN** `hora_utc` < `2.0` → IC=+0.188 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 2.0 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `15323.3068` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 15323.3068 (IC base=+0.092)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.145 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `drift_20min_pct` |x|> `0.1191` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1191
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

### MOMENTUM_IBS_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.8052` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8052
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=46)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.39` → IC=-0.305 (n=121)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=394)

- **FILTRO** `ibs_20min` < `0.7186` → IC=-0.254 (n=128)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7186
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=387)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.190 (n=127)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=388)

- **FILTRO** `libro_liquidez` < `2436.3906` → IC=-0.131 (n=386)

  - _Acción_: SKIP cuando `libro_liquidez` < 2436.3906
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=129)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.237 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=64)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=55)

- **FILTRO** `ibs_20min` > `0.9273` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9273
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=61)

- **FILTRO** `ibs_20min` < `0.7129` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7129
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=61)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=54)

- **PATRÓN** `ibs_20min` < `0.1608` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.1608 (IC base=+0.053)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=67)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=60)

- **FILTRO** `ibs_20min` < `0.7576` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=64)

- **FILTRO** `ballena_activa_n` > `40.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 40.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=64)

- **FILTRO** `libro_liquidez` < `14386.2811` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 14386.2811
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=29)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=85)

- **FILTRO** `ibs_20min` > `0.1853` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1853
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=83)

- **FILTRO** `ballena_activa_n` > `45.0` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `ballena_activa_n` > 45.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=83)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 5.0 (IC base=-0.027)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.238 (n=40)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=45)

- **FILTRO** `ibs_20min` < `0.7` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=65)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=63)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 16.0 (IC base=+0.062)

- **PATRÓN** `py_entrada` < `0.62` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.62 (IC base=+0.062)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=66)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=64)

- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=62)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 3.0 (IC base=+0.047)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.5 (IC base=+0.047)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=67)

- **FILTRO** `ibs_20min` > `0.8095` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8095
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=44)

- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=66)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=66)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=65)

- **FILTRO** `ibs_20min` < `0.7302` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7302
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=72)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=64)

- **PATRÓN** `py_entrada` < `0.515` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.515 (IC base=+0.005)

- **PATRÓN** `libro_liquidez` > `2271.3284` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2271.3284 (IC base=+0.005)

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
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=227)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_liquidez` < `3938.8737` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 3938.8737
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=47)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` > `0.9333` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9333 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `3938.8737` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3938.8737 (IC base=+0.049)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `ibs_20min` < `0.2368` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.250 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=38)

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
- **FILTRO** `hora_utc` < `13.0` → IC=-0.156 (n=687)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=709)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.286 (n=339)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=1057)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.241 (n=349)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=1047)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.218 (n=342)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=1054)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.157 (n=430)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1293)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.162 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=86)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.268 (n=54)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=175)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.225 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=122)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.179 (n=54)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=175)

- **FILTRO** `drift_7min_pct` |x|> `0.1048` → IC=-0.161 (n=57)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1048
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=172)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.257 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=221)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.345 (n=69)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=220)

- **FILTRO** `ibs_7min` < `0.7868` → IC=-0.257 (n=72)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7868
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=217)

- **FILTRO** `ballena_activa_n` > `113.0` → IC=-0.203 (n=72)

  - _Acción_: SKIP cuando `ballena_activa_n` > 113.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=217)

- **FILTRO** `libro_liquidez` < `10926.2646` → IC=-0.146 (n=190)

  - _Acción_: SKIP cuando `libro_liquidez` < 10926.2646
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=99)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.157 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=244)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.173 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=101)

- **FILTRO** `py_entrada` < `0.28` → IC=-0.382 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=151)

- **FILTRO** `ibs_7min` < `0.1416` → IC=-0.250 (n=50)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1416
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=150)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.280 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=152)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.159 (n=136)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=141)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.212 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=182)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.199 (n=134)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=105)

- **FILTRO** `ibs_7min` < `0.8137` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8137
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=180)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.154 (n=160)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=210)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.214 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=194)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.246 (n=61)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=194)

- **FILTRO** `ibs_7min` < `0.7692` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=193)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.258 (n=60)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=195)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.262 (n=99)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=85)

- **FILTRO** `ibs_7min` < `0.7295` → IC=-0.306 (n=60)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7295
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=124)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.278 (n=61)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=123)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.202 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=233)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=77)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=108)

- **PATRÓN** `libro_liquidez` > `11027.6956` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11027.6956 (IC base=+0.060)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=210)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.184 (n=166)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.167 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 18.0 (IC base=+0.146)

- **PATRÓN** `total_vol_5m` < `315.516` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 315.516 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3593.7807` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3593.7807 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 36.0 (IC base=+0.146)

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

- **FILTRO** `streak_estiramiento` > `0.437` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.437
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

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
- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=13)

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
- **FILTRO** `hora_utc` > `8.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=43)

- **FILTRO** `streak_estiramiento` > `0.644` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.644
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STREAK_MOM_5M
- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.132 (n=66)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=43)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.167 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 10.0 (IC base=+0.047)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.047)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `libro_liquidez` < `3496.0203` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 3496.0203
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=83)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=-0.017)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.070)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=713)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=410)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=418)

### UPDOWN_GBM#15min
- **FILTRO** `ibs_15` < `0.5837` → IC=-0.148 (n=140)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5837
  - _Potencial_: sin este filtro IC_bueno=+0.230 (n=287)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.139 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0035 (IC base=+0.106)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.135 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0054 (IC base=+0.106)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.122 (n=321)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.61€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.106)

- **PATRÓN** `ibs_15` > `0.5837` → IC=+0.230 (n=287)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5837 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.3516` → IC=+0.189 (n=88)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.3516 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.021` → IC=+0.233 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.021 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `5011.7166` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 5011.7166 (IC base=+0.106)

- **PATRÓN** `ibs_15` < `0.1208` → IC=+0.150 (n=224)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1208 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.5499` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.5499 (IC base=+0.075)

### UPDOWN_GBM#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0043` → IC=-0.135 (n=198)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0043
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=67)

- **FILTRO** `ibs_15` < `0.1` → IC=-0.258 (n=64)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=201)

- **FILTRO** `sigma_ewma_delta_pct` > `5.127` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.127
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=201)

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

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.154 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0029 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.157 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.002 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.154 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.141)

- **PATRÓN** `drift_15min` |x|≤ `0.3775` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `drift_15min` |x|≤ 0.3775 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0911` → IC=+0.143 (n=68)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.0911 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.9453` → IC=+0.257 (n=35)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9453 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.029` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 7.029 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.708` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 18.708 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `8665.5751` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8665.5751 (IC base=+0.141)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `ibs_15` < `0.1827` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1827
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `11975.2481` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 11975.2481
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0085` → IC=+0.167 (n=49)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.83€ cuando `pct_spot_vs_ref` |x|≤ 0.0085 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.220 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1675` → IC=+0.146 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1675 (IC base=+0.111)

- **PATRÓN** `drift_15min` |x|≤ `0.3989` → IC=+0.125 (n=142)

  - _Acción_: Kelly boost +0.62€ cuando `drift_15min` |x|≤ 0.3989 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.136 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 12.0 (IC base=+0.111)

- **PATRÓN** `ibs_15` > `0.0686` → IC=+0.129 (n=141)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` > 0.0686 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.79` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.79 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `10571.0959` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 10571.0959 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 20.0 (IC base=+0.111)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.6097` → IC=-0.265 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6097
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.531` → IC=-0.227 (n=31)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.531
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=63)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2385` → IC=+0.269 (n=24)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2385 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.147 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.531` → IC=+0.269 (n=63)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.531 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0929 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.167 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0028 (IC base=+0.121)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.159 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0039 (IC base=+0.121)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0804` → IC=+0.139 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.0804 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.159 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 12.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.126 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 14.0 (IC base=+0.121)

- **PATRÓN** `ibs_15` < `0.385` → IC=+0.147 (n=120)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` < 0.385 (IC base=+0.121)

- **PATRÓN** `ibs_15` > `0.032` → IC=+0.147 (n=120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` > 0.032 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.4224` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4224 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` < `22.914` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 22.914 (IC base=+0.121)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `ibs_15` < `0.0049` → IC=-0.206 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `dist_vwap_pct` > `0.1641` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1641
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=46)

- **FILTRO** `sigma_ewma_delta_pct` > `5.626` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.626
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=37)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.176 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0021 (IC base=+0.061)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.3157` → IC=+0.147 (n=32)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.3157 (IC base=+0.050)

- **PATRÓN** `ibs_15` < `0.0714` → IC=+0.186 (n=33)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` < 0.0714 (IC base=+0.050)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.050)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.173 (n=53)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.082)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0776` → IC=+0.121 (n=159)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.61€ cuando `delta_ratio_macro` |x|> 0.0776 (IC base=+0.082)

- **PATRÓN** `ibs_15` < `0.1304` → IC=+0.181 (n=70)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` < 0.1304 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.4097` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4097 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.919` → IC=+0.132 (n=142)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 5.919 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2560.2434` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2560.2434 (IC base=+0.082)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2095` → IC=+0.273 (n=86)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2095 (IC base=+0.259)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.306 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.256 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0032 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1599` → IC=+0.282 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1599 (IC base=+0.259)

- **PATRÓN** `drift_15min` |x|≤ `0.4081` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4081 (IC base=+0.259)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.264 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.339 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `ibs_15` > `0.7088` → IC=+0.318 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7088 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` > `0.3609` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3609 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` < `0.0842` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0842 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.438` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.438 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `3208.0074` → IC=+0.272 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3208.0074 (IC base=+0.259)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2061` → IC=+0.259 (n=56)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2061 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.259 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.245 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.224)

- **PATRÓN** `drift_15min` |x|≤ `0.6305` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6305 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.259 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.224)

- **PATRÓN** `ibs_15` < `0.9993` → IC=+0.224 (n=56)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.9993 (IC base=+0.224)

- **PATRÓN** `ibs_15` > `0.7314` → IC=+0.259 (n=56)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7314 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `15.813` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 15.813 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `7152.8647` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7152.8647 (IC base=+0.224)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `dist_vwap_pct` < `0.058` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.058 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.414` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.414 (IC base=+0.309)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.4` → IC=-0.331 (n=81)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=166)

- **FILTRO** `sigma_ewma_delta_pct` > `12.676` → IC=-0.163 (n=247)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.676
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=990)

- **PATRÓN** `ibs_15` > `0.4` → IC=+0.173 (n=166)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` > 0.4 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.531` → IC=+0.280 (n=48)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.531 (IC base=-0.054)

- **PATRÓN** `dist_vwap_pct` < `0.0928` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.0928 (IC base=-0.054)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.224 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=210)

- **FILTRO** `sigma_ewma_delta_pct` > `21.242` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 21.242
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=204)

- **FILTRO** `libro_liquidez` < `13600.036` → IC=-0.216 (n=199)

  - _Acción_: SKIP cuando `libro_liquidez` < 13600.036
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=67)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.121 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 5.0 (IC base=+0.065)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `sigma_h` > `0.0045` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=71)

- **FILTRO** `drift_60min` |x|> `0.2076` → IC=-0.260 (n=23)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2076
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=71)

- **FILTRO** `ibs_15` < `0.5496` → IC=-0.357 (n=47)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5496
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=47)

- **PATRÓN** `ibs_15` > `0.5496` → IC=+0.214 (n=47)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5496 (IC base=-0.073)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1184` → IC=+0.206 (n=32)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1184 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.206 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.173)

- **PATRÓN** `ibs_15` < `0.428` → IC=+0.324 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.428 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.284` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.284 (IC base=+0.173)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.176 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=106)

- **FILTRO** `sigma_ewma_delta_pct` > `13.824` → IC=-0.187 (n=65)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 13.824
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=382)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.659` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.659 (IC base=-0.025)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.154 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=53)

- **FILTRO** `libro_liquidez` < `2491.4834` → IC=-0.207 (n=39)

  - _Acción_: SKIP cuando `libro_liquidez` < 2491.4834
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

- **FILTRO** `sigma_ewma_delta_pct` > `7.667` → IC=-0.153 (n=96)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.667
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=311)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.287 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0026 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.275 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.266)

- **PATRÓN** `drift_15min` |x|≤ `0.4795` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4795 (IC base=+0.266)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.281 (n=117)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.300 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.266)

- **PATRÓN** `ibs_15` > `0.9378` → IC=+0.350 (n=78)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9378 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` > `0.3696` → IC=+0.329 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3696 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` < `0.0774` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0774 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.98` → IC=+0.280 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.98 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.266)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1986` → IC=+0.284 (n=72)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1986 (IC base=+0.253)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0022` → IC=+0.273 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0022 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.1837` → IC=+0.284 (n=72)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1837 (IC base=+0.253)

- **PATRÓN** `drift_15min` |x|≤ `0.6436` → IC=+0.270 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6436 (IC base=+0.253)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0911` → IC=+0.258 (n=64)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0911 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.292 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.253)

- **PATRÓN** `ibs_15` > `0.8877` → IC=+0.303 (n=64)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8877 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.3682` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3682 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` < `0.0966` → IC=+0.291 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0966 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `27.672` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 27.672 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.495` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.495 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `8508.8052` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8508.8052 (IC base=+0.253)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.271 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.314 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `0.4139` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4139 (IC base=+0.278)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0547` → IC=+0.333 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0547 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.306 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.9815` → IC=+0.413 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9815 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.0728` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0728 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.209` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 16.209 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `10076.1613` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10076.1613 (IC base=+0.278)

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

- **FILTRO** `sigma_h` > `0.007` → IC=-0.143 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=250)

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

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.0714 sube el IC de +0.050 a +0.186 en UPDOWN_GBM#SOL#5min (n=33). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5837 sube el IC de +0.106 a +0.230 en UPDOWN_GBM#15min (n=287). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_NO, IBS < 0.1208 sube el IC de +0.075 a +0.150 en UPDOWN_GBM#15min (n=224). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9453 sube el IC de +0.141 a +0.257 en UPDOWN_GBM#BTC#15min (n=35). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.531 sube el IC de +0.104 a +0.269 en UPDOWN_GBM#ETH#15min (n=63). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.085 a +0.182 en UPDOWN_GBM#XRP#15min (n=86). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1304 sube el IC de +0.082 a +0.181 en UPDOWN_GBM#XRP#15min (n=70). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4 sube el IC de -0.040 a +0.173 en UPDOWN_GBM_15M_TARDIO (n=166). Ya aplicado como kelly_boost=+0.86€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.531 sube el IC de -0.054 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=48). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5496 sube el IC de -0.073 a +0.214 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=47). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.428 sube el IC de +0.173 a +0.324 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9378 sube el IC de +0.266 a +0.350 en UPDOWN_GBM_IBS_ALTO (n=78). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8877 sube el IC de +0.253 a +0.303 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=64). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.9815 sube el IC de +0.278 a +0.413 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7088 sube el IC de +0.259 a +0.318 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS < 0.9993 sube el IC de +0.224 a +0.224 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7314 sube el IC de +0.224 a +0.259 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#BNB#5min` — IC=+0.214 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#BNB` — IC=+0.214 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 493 | +0.045 | +38.20€ | 3 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 493 | +0.045 | +38.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 254 | +0.043 | +24.88€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 254 | +0.043 | +24.88€ | 2 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 211 | +0.026 | +0.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 211 | +0.026 | +0.36€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 28 | +0.200 | +12.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 28 | +0.200 | +12.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3602 | -0.115 | -585.41€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 471 | -0.026 | -22.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 3131 | -0.129 | -562.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 415 | -0.193 | -97.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 415 | -0.193 | -97.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 471 | -0.026 | -22.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 471 | -0.026 | -22.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 321 | -0.147 | -146.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 321 | -0.147 | -146.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 893 | +0.004 | -120.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 893 | +0.004 | -120.19€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 777 | -0.229 | -159.47€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 777 | -0.229 | -159.47€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 15533 | +0.113 | -974.98€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3542 | +0.183 | -102.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 101 | -0.092 | -45.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 9254 | +0.083 | -847.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2636 | +0.132 | +21.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1563 | +0.026 | -353.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 14 | -0.044 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1545 | +0.029 | -348.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3488 | +0.138 | -23.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 970 | +0.199 | -31.08€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 41 | -0.105 | -20.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1541 | +0.106 | -31.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 936 | +0.137 | +59.83€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1561 | +0.056 | -271.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 10 | +0.000 | -3.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1550 | +0.057 | -266.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3767 | +0.126 | -42.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1306 | +0.164 | -14.36€ | 0 | 6 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1536 | +0.103 | -24.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 913 | +0.117 | +5.57€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3595 | +0.135 | -214.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1230 | +0.196 | -55.91€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 42 | +0.023 | -7.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1536 | +0.085 | -107.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 787 | +0.141 | -43.65€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1559 | +0.116 | -69.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1546 | +0.116 | -70.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3605 | +0.159 | -359.02€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3605 | +0.159 | -359.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 904 | +0.153 | -120.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 904 | +0.153 | -120.39€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 78 | -0.113 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 78 | -0.113 | -5.72€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 896 | +0.154 | -118.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 896 | +0.154 | -118.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 797 | +0.218 | -43.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 797 | +0.218 | -43.47€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 2 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 851 | +0.173 | -84.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 851 | +0.173 | -84.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 176 | +0.410 | -11.29€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 176 | +0.410 | -11.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 63 | +0.408 | -3.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 63 | +0.408 | -3.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 68 | +0.386 | -6.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 68 | +0.386 | -6.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 43 | +0.411 | -1.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 43 | +0.411 | -1.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 6588 | +0.182 | -685.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 6588 | +0.182 | -685.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1231 | +0.092 | -286.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1231 | +0.092 | -286.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1010 | +0.238 | -24.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1010 | +0.238 | -24.37€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1163 | +0.150 | -175.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1163 | +0.150 | -175.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1056 | +0.218 | -49.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1056 | +0.218 | -49.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1020 | +0.241 | -19.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1020 | +0.241 | -19.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1108 | +0.174 | -130.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1108 | +0.174 | -130.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2359 | +0.149 | +133.57€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 2359 | +0.149 | +133.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1166 | +0.154 | +75.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1166 | +0.154 | +75.48€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1193 | +0.144 | +58.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1193 | +0.144 | +58.09€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 551 | +0.301 | +6.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 551 | +0.301 | +6.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 231 | +0.273 | -9.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 231 | +0.273 | -9.71€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 256 | +0.302 | +8.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 256 | +0.302 | +8.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 64 | +0.379 | +8.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 64 | +0.379 | +8.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 230 | +0.409 | -10.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 230 | +0.409 | -10.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 103 | +0.405 | -5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 103 | +0.405 | -5.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 103 | +0.414 | -5.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 103 | +0.414 | -5.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 260 | +0.260 | -30.33€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 260 | +0.260 | -30.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 260 | +0.260 | -30.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 260 | +0.260 | -30.33€ | 0 | 4 |
| ✅ GBM_LATE_15M | 4768 | +0.085 | +1761.25€ | 0 | 13 |
| ✅ GBM_LATE_15M#15min | 4768 | +0.085 | +1761.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 834 | +0.175 | +524.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 834 | +0.175 | +524.89€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 482 | +0.186 | +262.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 482 | +0.186 | +262.78€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 844 | +0.192 | +581.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 844 | +0.192 | +581.91€ | 0 | 17 |
| ✅ GBM_LATE_15M#ETH | 630 | -0.006 | +37.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 630 | -0.006 | +37.81€ | 0 | 2 |
| ✅ GBM_LATE_15M#SOL | 883 | +0.001 | +126.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 883 | +0.001 | +126.88€ | 3 | 5 |
| ✅ GBM_LATE_15M#XRP | 1095 | +0.010 | +226.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1095 | +0.010 | +226.98€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5795 | +0.049 | +1876.85€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5795 | +0.049 | +1876.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1110 | -0.029 | +297.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1110 | -0.029 | +297.40€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1105 | -0.014 | +92.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1105 | -0.014 | +92.54€ | 2 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 711 | +0.240 | +650.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 711 | +0.240 | +650.97€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1007 | -0.019 | +8.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1007 | -0.019 | +8.76€ | 6 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1021 | +0.001 | +154.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1021 | +0.001 | +154.12€ | 2 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 841 | +0.211 | +673.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 841 | +0.211 | +673.06€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3515 | +0.176 | +2399.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3515 | +0.176 | +2399.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 626 | +0.193 | +458.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 626 | +0.193 | +458.23€ | 0 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 472 | +0.198 | +322.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 472 | +0.198 | +322.10€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 622 | +0.203 | +487.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 622 | +0.203 | +487.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 444 | +0.206 | +332.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 444 | +0.206 | +332.87€ | 0 | 27 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 648 | +0.074 | +259.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 648 | +0.074 | +259.03€ | 1 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 703 | +0.195 | +540.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 703 | +0.195 | +540.34€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 610 | +0.057 | +73.66€ | 0 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 610 | +0.057 | +73.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 119 | +0.070 | +11.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 119 | +0.070 | +11.85€ | 1 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 119 | +0.161 | +41.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 119 | +0.161 | +41.72€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 237 | -0.002 | +10.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 237 | -0.002 | +10.36€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 134 | +0.059 | +10.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 134 | +0.059 | +10.99€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 4075 | +0.168 | +2642.50€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 4075 | +0.168 | +2642.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 802 | +0.183 | +551.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 802 | +0.183 | +551.98€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 540 | +0.162 | +308.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 540 | +0.162 | +308.31€ | 1 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 791 | +0.215 | +645.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 791 | +0.215 | +645.99€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 390 | +0.133 | +177.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 390 | +0.133 | +177.98€ | 1 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 647 | +0.076 | +287.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 647 | +0.076 | +287.41€ | 0 | 15 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 905 | +0.195 | +670.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 905 | +0.195 | +670.83€ | 0 | 24 |
| ✅ GBM_LATE_5M | 333 | +0.109 | +131.02€ | 3 | 12 |
| ✅ GBM_LATE_5M#5min | 333 | +0.109 | +131.02€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 166 | +0.137 | +79.68€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 166 | +0.137 | +79.68€ | 0 | 11 |
| ✅ GBM_LATE_5M#DOGE | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 87 | +0.185 | +49.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 87 | +0.185 | +49.62€ | 0 | 10 |
| ✅ GBM_LATE_5M#SOL | 44 | -0.065 | +3.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 44 | -0.065 | +3.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 23 | +0.100 | +2.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 23 | +0.100 | +2.42€ | 0 | 0 |
| ✅ GBM_LATE_60M | 498 | -0.046 | +73.63€ | 5 | 6 |
| ✅ GBM_LATE_60M#60min | 498 | -0.046 | +73.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 173 | -0.003 | +5.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 173 | -0.003 | +5.67€ | 3 | 3 |
| ✅ GBM_LATE_60M#ETH | 174 | -0.023 | +43.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 174 | -0.023 | +43.65€ | 1 | 8 |
| ✅ GBM_LATE_60M#SOL | 151 | -0.121 | +24.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 151 | -0.121 | +24.30€ | 3 | 2 |
| 🚫 GBM_LATE_60M_FADE | 192 | -0.304 | -33.97€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 192 | -0.304 | -33.97€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 64 | -0.348 | -18.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 64 | -0.348 | -18.54€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 52 | -0.296 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 52 | -0.296 | -8.07€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 310 | +0.042 | +7.55€ | 1 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 310 | +0.042 | +7.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 121 | +0.012 | +3.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 121 | +0.012 | +3.09€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 73 | +0.100 | +7.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 73 | +0.100 | +7.77€ | 0 | 3 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 72 | +0.162 | +26.62€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 72 | +0.162 | +26.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 72 | +0.162 | +26.62€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 72 | +0.162 | +26.62€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 202 | -0.113 | -29.52€ | 5 | 0 |
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
| ✅ LIQUIDACIONES_5M | 105 | -0.117 | -14.15€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 105 | -0.117 | -14.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 40 | -0.095 | -4.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 40 | -0.095 | -4.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 25 | -0.056 | -1.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 25 | -0.056 | -1.99€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 16 | -0.178 | -4.14€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 16 | -0.178 | -4.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 15 | -0.110 | -2.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 15 | -0.110 | -2.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 303 | -0.002 | -6.09€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 303 | -0.002 | -6.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 102 | -0.010 | -7.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 102 | -0.010 | -7.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 99 | -0.015 | -1.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 99 | -0.015 | -1.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 102 | +0.019 | +3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 102 | +0.019 | +3.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 835 | +0.039 | +46.01€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M#15min | 835 | +0.039 | +46.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 122 | +0.089 | +29.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 122 | +0.089 | +29.97€ | 1 | 7 |
| ✅ MOMENTUM_IBS_15M#BTC | 147 | +0.104 | +33.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 147 | +0.104 | +33.13€ | 0 | 7 |
| ✅ MOMENTUM_IBS_15M#DOGE | 128 | +0.015 | -10.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 128 | +0.015 | -10.63€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 153 | +0.055 | +22.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 153 | +0.055 | +22.94€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M#SOL | 142 | -0.035 | -19.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 142 | -0.035 | -19.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 143 | +0.003 | -9.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 143 | +0.003 | -9.58€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 1113 | -0.037 | +17.40€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 1113 | -0.037 | +17.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 173 | -0.037 | +22.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 173 | -0.037 | +22.14€ | 5 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 195 | -0.058 | -21.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 195 | -0.058 | -21.44€ | 8 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 179 | -0.003 | +34.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 179 | -0.003 | +34.49€ | 4 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 197 | -0.018 | -0.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 197 | -0.018 | -0.09€ | 3 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 181 | -0.063 | -7.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 181 | -0.063 | -7.48€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 188 | -0.042 | -10.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 188 | -0.042 | -10.21€ | 4 | 2 |
| ✅ MOMENTUM_IBS_15M_FADE | 385 | -0.056 | -23.48€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 385 | -0.056 | -23.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 63 | -0.038 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 63 | -0.038 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 52 | -0.148 | -8.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 52 | -0.148 | -8.54€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 29 | -0.113 | -3.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 29 | -0.113 | -3.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 72 | -0.081 | -6.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 72 | -0.081 | -6.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 90 | +0.011 | +2.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 90 | +0.011 | +2.19€ | 1 | 3 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 79 | -0.031 | -3.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 79 | -0.031 | -3.09€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 3119 | -0.059 | +136.87€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 3119 | -0.059 | +136.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 458 | -0.098 | +36.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 458 | -0.098 | +36.41€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 601 | -0.047 | +72.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 601 | -0.047 | +72.72€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 477 | -0.064 | +7.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 477 | -0.064 | +7.46€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 537 | -0.062 | -21.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 537 | -0.062 | -21.86€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 564 | -0.037 | -3.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 564 | -0.037 | -3.78€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 482 | -0.056 | +45.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 482 | -0.056 | +45.92€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 2632 | +0.019 | +28.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 2632 | +0.019 | +28.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 454 | +0.026 | +12.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 454 | +0.026 | +12.74€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 353 | +0.038 | +10.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 353 | +0.038 | +10.03€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 464 | +0.011 | -0.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 464 | +0.011 | -0.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 444 | +0.009 | +2.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 444 | +0.009 | +2.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 469 | +0.014 | +2.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 469 | +0.014 | +2.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 448 | +0.018 | +1.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 448 | +0.018 | +1.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 259 | +0.098 | +61.15€ | 1 | 6 |
| ✅ ORDER_FLOW_5M#5min | 123 | +0.140 | +48.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 33 | +0.214 | +26.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 33 | +0.214 | +26.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 21 | +0.065 | +3.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 21 | +0.065 | +3.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 12 | +0.129 | +9.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 12 | +0.129 | +9.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 29 | +0.081 | +3.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 29 | +0.081 | +3.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 28 | +0.100 | +6.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 28 | +0.100 | +6.05€ | 0 | 0 |
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
| ✅ RESOLUTION_SNIPER | 49 | +0.245 | +6.70€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 17 | +0.380 | +8.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 17 | +0.380 | +8.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 49 | +0.245 | +6.70€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 50 | -0.115 | -12.78€ | 3 | 0 |
| ✅ STREAK_FADE_15M#15min | 50 | -0.115 | -12.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 20 | -0.045 | -4.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 20 | -0.045 | -4.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 25 | -0.130 | -6.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 25 | -0.130 | -6.34€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 406 | -0.017 | -18.38€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 406 | -0.017 | -18.38€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 114 | +0.026 | +2.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 114 | +0.026 | +2.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 133 | -0.011 | -7.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 133 | -0.011 | -7.24€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 66 | -0.059 | -6.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 66 | -0.059 | -6.52€ | 2 | 2 |
| ✅ STREAK_FADE_5M#XRP | 93 | -0.047 | -7.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 93 | -0.047 | -7.10€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 677 | +0.018 | -2.01€ | 1 | 0 |
| ✅ STREAK_MOM_5M#5min | 677 | +0.018 | -2.01€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 215 | +0.011 | -2.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 215 | +0.011 | -2.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 124 | -0.016 | -4.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 124 | -0.016 | -4.32€ | 3 | 2 |
| ✅ STREAK_MOM_5M#SOL | 184 | +0.032 | +2.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 184 | +0.032 | +2.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 154 | +0.038 | +2.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 154 | +0.038 | +2.16€ | 2 | 2 |
| ✅ STRUCT_NO_15M | 1929 | +0.015 | -4.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1929 | +0.015 | -4.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 732 | +0.005 | -9.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 732 | +0.005 | -9.55€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 755 | +0.021 | +1.92€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 755 | +0.021 | +1.92€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 442 | +0.022 | +2.87€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 442 | +0.022 | +2.87€ | 2 | 0 |
| ✅ UPDOWN_GBM | 2595 | +0.029 | +202.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1103 | +0.087 | +200.76€ | 1 | 9 |
| ✅ UPDOWN_GBM#240min | 127 | +0.004 | -2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 1062 | -0.004 | +15.76€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 256 | -0.023 | -10.57€ | 4 | 1 |
| ✅ UPDOWN_GBM#BNB | 113 | +0.135 | +35.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 106 | +0.157 | +37.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6 | -0.075 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 495 | +0.041 | +55.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 132 | +0.067 | +3.80€ | 2 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 39 | +0.061 | +2.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 220 | +0.077 | +55.79€ | 2 | 9 |
| ✅ UPDOWN_GBM#BTC#60min | 86 | -0.057 | -8.56€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 306 | +0.000 | -1.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 63 | +0.115 | +14.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 243 | -0.031 | -16.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 609 | +0.052 | +53.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 253 | +0.116 | +55.17€ | 1 | 14 |
| ✅ UPDOWN_GBM#ETH#240min | 39 | +0.037 | +0.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 198 | +0.015 | -0.30€ | 4 | 1 |
| ✅ UPDOWN_GBM#ETH#60min | 104 | +0.009 | -1.14€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 490 | +0.000 | +3.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 210 | +0.024 | +5.91€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 31 | -0.045 | -3.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 171 | +0.009 | +1.79€ | 2 | 3 |
| ✅ UPDOWN_GBM#SOL#60min | 66 | -0.029 | -0.87€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 580 | +0.017 | +57.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 339 | +0.084 | +83.58€ | 0 | 13 |
| ✅ UPDOWN_GBM#XRP#240min | 17 | -0.112 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 224 | -0.071 | -23.16€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 114 | +0.259 | +1.28€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 114 | +0.259 | +1.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 74 | +0.224 | -7.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 74 | +0.224 | -7.21€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 40 | +0.309 | +8.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 40 | +0.309 | +8.50€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1813 | -0.049 | +479.19€ | 2 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1813 | -0.049 | +479.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 127 | -0.058 | +105.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 127 | -0.058 | +105.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 349 | -0.138 | -15.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 349 | -0.138 | -15.79€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 43 | +0.011 | +3.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 43 | +0.011 | +3.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 141 | +0.011 | +24.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 141 | +0.011 | +24.51€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 588 | -0.019 | +238.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 588 | -0.019 | +238.83€ | 2 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 565 | -0.043 | +122.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 565 | -0.043 | +122.41€ | 3 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 8 | -0.040 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 156 | +0.266 | +87.52€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 156 | +0.266 | +87.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 95 | +0.253 | +44.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 95 | +0.253 | +44.47€ | 0 | 13 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 61 | +0.278 | +43.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 61 | +0.278 | +43.04€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 365 | -0.059 | -27.10€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 365 | -0.059 | -27.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 232 | -0.004 | -10.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 232 | -0.004 | -10.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 21 | +0.065 | +4.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 21 | +0.065 | +4.12€ | 0 | 0 |
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
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.131) — sin ventaja clara. oversold(IBS<0.3): IC=-0.009 n=915 | neutral: IC=+0.019 n=863 | overbought(IBS>0.7): IC=+0.122 n=1130
  - _Datos_: n=3121 IC=+0.049 PNL=+322.10€

**🟡 H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: H=19h: IC=+0.111 n=124 PNL=+34.97€ → BOOST

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 1 celda(s) pasan gate riguroso completo de 54 evaluadas (n>=40) y 290 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.024 < 0.08 — monitorear
  - _Datos_: n=210 IC=+0.024 PNL=+5.91€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=296/15 IC=+0.255 PNL=+66.82€ | BTC: n=277/15 IC=+0.199 PNL=+5.61€ | SOL: n=360/15 IC=+0.373 PNL=+309.64€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.100 n=42577 | tras_1loss IC=+0.058 n=30532 | tras_2loss IC=+0.018 n=13440/40 | gap=+0.082 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 15 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.204 n=19/60 | contraria IC=-0.043 n=12 | gap=+0.246 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=25, boost estimado=+0.010. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 29/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=104/40 IC=+0.009 PNL=-1.14€ | BTC#60min: n=86/40 IC=-0.057 PNL=-8.56€ | SOL#60min: n=66/40 IC=-0.029 PNL=-0.87€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.052 n=208 | contrario_BTC IC=+0.007 n=134/40 | gap=-0.045 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.156 > 0.08 con n=62 PNL=+28.27€
  - _Datos_: n=62 IC=+0.156 PNL=+28.27€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.08 con n=77 PNL=+18.48€
  - _Datos_: n=77 IC=+0.120 PNL=+18.48€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 4/25 ops en el filtro definido (IC actual=+0.067 PNL=+4.17€)
  - _Datos_: n=4 IC=+0.067 PNL=+4.17€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.341 > 0.1 con n=794 PNL=+391.67€
  - _Datos_: n=794 IC=+0.341 PNL=+391.67€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=17 IC=+0.022 PNL=+4.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=17 IC=+0.022 PNL=+4.57€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 10/30 ops en el filtro definido (IC actual=+0.042 PNL=+0.77€)
  - _Datos_: n=10 IC=+0.042 PNL=+0.77€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=2365 IC=+0.023 PNL=+147.48€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=2365 IC=+0.023 PNL=+147.48€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 1/15 ops en el filtro definido (IC actual=+0.008 PNL=+1.22€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.22€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=197 IC=+0.003 PNL=-3.10€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=197 IC=+0.003 PNL=-3.10€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=59 IC=-0.107 PNL=-7.47€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=59 IC=-0.107 PNL=-7.47€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=40 IC=+0.024 PNL=+3.19€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=40 IC=+0.024 PNL=+3.19€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.1 con n=427 PNL=+68.64€
  - _Datos_: n=427 IC=+0.106 PNL=+68.64€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=164 IC=+0.090 PNL=+41.87€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=164 IC=+0.090 PNL=+41.87€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=132 IC=+0.067 PNL=+3.80€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=132 IC=+0.067 PNL=+3.80€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=682 PNL=+108.20€
  - _Datos_: n=682 IC=+0.088 PNL=+108.20€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 16/30 ops en el filtro definido (IC actual=-0.178 PNL=-2.92€)
  - _Datos_: n=16 IC=-0.178 PNL=-2.92€

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 14/20 ops en el filtro definido (IC actual=+0.131 PNL=+8.58€)
  - _Datos_: n=14 IC=+0.131 PNL=+8.58€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=31 IC=+0.136 PNL=+4.66€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=31 IC=+0.136 PNL=+4.66€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 4/15 ops en el filtro definido (IC actual=+0.000 PNL=-0.05€)
  - _Datos_: n=4 IC=+0.000 PNL=-0.05€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=165 IC=+0.051 PNL=+19.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=165 IC=+0.051 PNL=+19.92€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=33 PNL=+9.78€
  - _Datos_: n=33 IC=+0.214 PNL=+9.78€

**⏳ H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: 30
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: 4/30 ops en el filtro definido (IC actual=+0.067 PNL=+2.07€)
  - _Datos_: n=4 IC=+0.067 PNL=+2.07€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=570 IC=+0.089 PNL=+131.47€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=570 IC=+0.089 PNL=+131.47€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=318 IC=+0.041 PNL=+4.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=318 IC=+0.041 PNL=+4.64€

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 32/40 ops en el filtro definido (IC actual=+0.147 PNL=+11.35€)
  - _Datos_: n=32 IC=+0.147 PNL=+11.35€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.153 > 0.08 con n=93 PNL=-2.25€
  - _Datos_: n=93 IC=+0.153 PNL=-2.25€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=80 PNL=+16.80€
  - _Datos_: n=80 IC=+0.098 PNL=+16.80€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=571 IC=+0.144 PNL=+1.44€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=571 IC=+0.144 PNL=+1.44€

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
  - _Estado_: n=371 IC=+0.034 PNL=+19.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=371 IC=+0.034 PNL=+19.37€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.02 con n=132 PNL=+62.11€
  - _Datos_: n=132 IC=+0.187 PNL=+62.11€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=86 IC=-0.125 PNL=+14.04€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=86 IC=-0.125 PNL=+14.04€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.445 > 0.1 con n=523 PNL=+435.60€
  - _Datos_: n=523 IC=+0.445 PNL=+435.60€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1003 IC=+0.023 PNL=+32.88€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1003 IC=+0.023 PNL=+32.88€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.159 > 0.1 con n=581 PNL=+192.89€
  - _Datos_: n=581 IC=+0.159 PNL=+192.89€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 12/40 ops en el filtro definido (IC actual=-0.214 PNL=-6.49€)
  - _Datos_: n=12 IC=-0.214 PNL=-6.49€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=211 IC=+0.082 PNL=+49.56€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=211 IC=+0.082 PNL=+49.56€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**⏳ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: 50
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: 32/50 ops en el filtro definido (IC actual=+0.147 PNL=+5.51€)
  - _Datos_: n=32 IC=+0.147 PNL=+5.51€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=1553 IC=-0.149 PNL=+54.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1553 IC=-0.149 PNL=+54.43€

**⏳ H-CUSTOM-LATE15-PHOTO-FINISH** — GBM_LATE_15M photo finish — entrar pegado al strike es moneda al aire cobrada como favorito
  - _Hipótesis_: Detectado 2026-07-05 validando contra nuestros datos la única idea aprovechable de un artículo-anuncio de copy-bot: GBM_LATE_15M con |drift_ventana_pct|<0.02 tenía IC=-0.145 n=181 (win 35%, -9.70€), estable en ambas mitades temporales (-0.163/-0.127), monótono con la distancia (0.02-0.05: IC=+0.061; ≥0.05: IC=+0.14..0.19) y consistente en crudo y normalizado por sigma (|d_gbm|<0.1 IC=-0.081 n=244). BTC (IC=-0.163 n=90) y ETH (-0.130 n=79) concentraban el daño; SOL/XRP apenas entran en esa zona. Mecanismo: sin distancia real al strike el resultado es ~50/50 pero py_entrada ya cobra favorito. Filtro GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict el 2026-07-05. Esta hipótesis trackea la zona filtrada: si vuelven a aparecer ops aquí, el filtro se ha roto.
  - _Umbral_: 200
  - _Acción_: Si aparecen ops nuevas en la zona → el filtro está roto, revisar shadow_predict. Si el buffer [0.02,0.05) se vuelve negativo con n≥60 forward → subir el corte a 0.05.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=334 IC=+0.149 PNL=+124.36€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=334 IC=+0.149 PNL=+124.36€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.08 con n=427 PNL=+68.64€
  - _Datos_: n=427 IC=+0.106 PNL=+68.64€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=283 IC=+0.016 PNL=+11.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=283 IC=+0.016 PNL=+11.59€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.08 con n=411 PNL=+267.57€
  - _Datos_: n=411 IC=+0.130 PNL=+267.57€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.08 con n=101 PNL=+11.24€
  - _Datos_: n=101 IC=+0.141 PNL=+11.24€

**⏳ H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: 289
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: 77/289 ops en el filtro definido (IC actual=-0.310 PNL=-19.86€)
  - _Datos_: n=77 IC=-0.310 PNL=-19.86€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=846 IC=+0.158 PNL=+477.00€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=846 IC=+0.158 PNL=+477.00€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 15/40 ops en el filtro definido (IC actual=+0.022 PNL=-1.76€)
  - _Datos_: n=15 IC=+0.022 PNL=-1.76€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=350 IC=-0.009 PNL=+18.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=350 IC=-0.009 PNL=+18.27€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.08 con n=293 PNL=+175.24€
  - _Datos_: n=293 IC=+0.208 PNL=+175.24€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=581 IC=+0.018 PNL=+145.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=581 IC=+0.018 PNL=+145.72€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.08 con n=163 PNL=-10.91€
  - _Datos_: n=163 IC=+0.136 PNL=-10.91€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.08 con n=686 PNL=-74.66€
  - _Datos_: n=686 IC=+0.243 PNL=-74.66€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 4/40 ops en el filtro definido (IC actual=+0.000 PNL=+1.83€)
  - _Datos_: n=4 IC=+0.000 PNL=+1.83€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.181 n=45) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=45 IC=+0.181 PNL=+22.38€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.360 > 0.08 con n=48 PNL=+40.53€
  - _Datos_: n=48 IC=+0.360 PNL=+40.53€

**⏳ H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: 200
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: 188/200 ops en el filtro definido (IC actual=+0.442 PNL=+250.61€)
  - _Datos_: n=188 IC=+0.442 PNL=+250.61€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=1231 IC=+0.092 PNL=-286.92€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=1231 IC=+0.092 PNL=-286.92€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 18/40 ops en el filtro definido (IC actual=+0.180 PNL=+7.75€)
  - _Datos_: n=18 IC=+0.180 PNL=+7.75€
