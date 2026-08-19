# Hipótesis automáticas — 2026-08-19 03:06 UTC
_Generado por shadow_postmortem.py sobre 71119 resoluciones (PNL=+7057.96€)_

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
- **FILTRO** `restante_s_al_confirmar` < `154.18` → IC=-0.247 (n=952)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 154.18
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2856)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `119.48` → IC=-0.404 (n=102)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.48
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=307)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `641.33` → IC=-0.297 (n=116)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 641.33
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=352)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `13.78` → IC=-0.492 (n=126)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 13.78
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=256)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `concentracion_yes` < `1.0` → IC=-0.121 (n=64)

  - _Acción_: SKIP cuando `concentracion_yes` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=864)

- **FILTRO** `n_ballenas` < `4.0` → IC=-0.147 (n=222)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=706)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `177.08` → IC=-0.287 (n=247)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 177.08
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=503)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=2405)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.090)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=1176)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2373.5135` → IC=+0.167 (n=1137)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2373.5135 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.158 (n=4050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=2971)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=2045)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `4054.8773` → IC=+0.182 (n=832)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4054.8773 (IC base=+0.153)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.364 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.232 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.302 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

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
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.125 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 15.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.296 (n=248)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=498)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.397 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.276 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` < `0.31` → IC=+0.347 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.31 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `911.1943` → IC=+0.249 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 911.1943 (IC base=+0.232)

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

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=1197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.201 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `3268.7028` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3268.7028 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.162 (n=607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.172 (n=614)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.73 (IC base=+0.154)

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

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.187 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 7.0 (IC base=+0.157)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.188 (n=232)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.7 (IC base=+0.157)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.232 (n=405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.319 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.216)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min
- **FILTRO** `py_entrada` > `0.755` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.197 (n=285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.186 (n=514)

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
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=3237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.225 (n=3373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `py_entrada` > `0.73` → IC=+0.134 (n=443)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.73 (IC base=+0.093)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.298 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.324 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.244)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.219 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.155)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=773)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.297 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.258 (n=250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.282 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.244)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=541)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.247 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.224 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.147)

- **PATRÓN** `restante_min` < `3.8` → IC=+0.164 (n=576)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` < 3.8 (IC base=+0.147)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.206 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.91 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.154 (n=1592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.155 (n=1732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `lag_apertura_s` < `5.53` → IC=+0.211 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.53 (IC base=+0.147)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.241 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.153)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.167 (n=376)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` < 4.07 (IC base=+0.153)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.192 (n=310)

  - _Acción_: Kelly boost +0.96€ cuando `restante_min` > 4.88 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.163 (n=752)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.153)

- **PATRÓN** `lag_apertura_s` < `7.0` → IC=+0.196 (n=284)

  - _Acción_: Kelly boost +0.98€ cuando `lag_apertura_s` < 7.0 (IC base=+0.153)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.43` → IC=+0.172 (n=778)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.43 (IC base=+0.141)

- **PATRÓN** `restante_min` < `3.9` → IC=+0.151 (n=293)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` < 3.9 (IC base=+0.141)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.223 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=878)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.141)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.221 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.28 (IC base=+0.141)

- **PATRÓN** `profundidad_ratio_no` > `11.0` → IC=+0.155 (n=294)

  - _Acción_: Kelly boost +0.78€ cuando `profundidad_ratio_no` > 11.0 (IC base=+0.141)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.308 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.313 (n=425)
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
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.375)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.375)

- **PATRÓN** `libro_liquidez` > `943.1727` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 943.1727 (IC base=+0.375)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1397.8324` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1397.8324 (IC base=+0.258)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.278 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.258)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1397.8324` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1397.8324 (IC base=+0.258)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.268 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4219` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4219 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.694` → IC=+0.237 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.694 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.2802` → IC=+0.247 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2802 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6468` → IC=+0.241 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6468 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.6604` → IC=+0.122 (n=2211)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6604 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.242` → IC=+0.139 (n=585)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.242 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.8798` → IC=+0.142 (n=333)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8798 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `0.6966` → IC=+0.138 (n=446)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6966 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.3315` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3315 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.5637` → IC=+0.259 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5637 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.8566` → IC=+0.232 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8566 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.280 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 235.0 (IC base=+0.078)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.170 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.007 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.193 (n=151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.9185` → IC=+0.280 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9185 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.471` → IC=+0.347 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.471 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.156 (n=306)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.06 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.315 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.338 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.1333` → IC=+0.344 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1333 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.289 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.300 (n=208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.289)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.336 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` < `0.0645` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0645 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` > `0.24` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.24 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` < `1.7987` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7987 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.335 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1980.3` → IC=+0.324 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1980.3 (IC base=+0.289)

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

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.174 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0018 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.146 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0029 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1903` → IC=+0.174 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1903 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.185 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 12.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.4755` → IC=+0.204 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4755 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1392` → IC=+0.162 (n=264)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1392 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.439` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.439 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.3019` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.3019 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6842` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6842 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.1879` → IC=+0.188 (n=142)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1879 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1063` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1063 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.6686` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6686 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `12550.5978` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 12550.5978 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 235.0 (IC base=+0.143)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.165 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.007 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.208 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.932` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.932 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.144 (n=417)

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

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.0972 (IC base=-0.017)

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

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1873 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6986 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `1.1434` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1434 (IC base=+0.034)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.233 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.3584` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3584 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.215` → IC=+0.128 (n=1029)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.215 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.339` → IC=+0.200 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.339 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `2.2067` → IC=+0.154 (n=452)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.2067 (IC base=+0.049)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.0994` → IC=+0.168 (n=872)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0994 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.4957` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4957 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `1.2602` → IC=+0.221 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2602 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2118` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2118 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `3.7438` → IC=+0.324 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.7438 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.316 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 68.0 (IC base=+0.050)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.939` → IC=-0.210 (n=105)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.939
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=540)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.382` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 3.382 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.0503` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0503 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.3584` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.3584 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` < `0.0555` → IC=-0.156 (n=88)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0555
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=264)

- **PATRÓN** `volumen_regimen` < `1.164` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.164 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.5727` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5727 (IC base=-0.008)

- **PATRÓN** `volumen_regimen` > `1.1352` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1352 (IC base=-0.008)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.281 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0611` → IC=+0.211 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0611 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.247 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.958` → IC=+0.305 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.958 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.1441` → IC=+0.183 (n=257)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1441 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.0929` → IC=+0.161 (n=122)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.0929 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.193 (n=389)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.06 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `1915.1084` → IC=+0.207 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.1084 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.177)

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
- **FILTRO** `ibs_20min` < `0.6396` → IC=-0.132 (n=161)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6396
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=83)

- **FILTRO** `dist_vwap_pct` < `0.3632` → IC=-0.225 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3632
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

- **FILTRO** `volumen_regimen` > `0.8629` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8629
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **FILTRO** `libro_liquidez` < `8612.4997` → IC=-0.214 (n=61)

  - _Acción_: SKIP cuando `libro_liquidez` < 8612.4997
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=183)

- **FILTRO** `volumen_regimen` > `0.7318` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.7318
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=707)

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

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.298 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.329 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.32` → IC=+0.334 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.32 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.5418` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5418 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.927` → IC=+0.288 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.927 (IC base=+0.285)

- **PATRÓN** `volumen_regimen` > `0.8948` → IC=+0.322 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8948 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `3.5418` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5418 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2886.2525` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2886.2525 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.285)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.157 (n=435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0047 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.191 (n=590)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0066 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0932` → IC=+0.140 (n=573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0932 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.155 (n=436)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.9185` → IC=+0.252 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9185 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.151 (n=382)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.935` → IC=+0.268 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.935 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.1837` → IC=+0.143 (n=676)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1837 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.140 (n=676)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6287 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1106` → IC=+0.154 (n=438)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1106 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.145 (n=1467)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.06 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2699.9007` → IC=+0.174 (n=434)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2699.9007 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.219 (n=1274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.2346` → IC=+0.220 (n=1119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2346 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.257 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.277 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.607` → IC=+0.236 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.607 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2517` → IC=+0.188 (n=984)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2517 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.8747` → IC=+0.198 (n=656)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.8747 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.322` → IC=+0.277 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.322 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.5489` → IC=+0.230 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5489 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `3.1445` → IC=+0.247 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1445 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.281 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.213)

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

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.293 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.330 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.215` → IC=+0.333 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.215 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.320 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` < `0.0497` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0497 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.376 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1962.999` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1962.999 (IC base=+0.294)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.002` → IC=+0.284 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.002 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.269 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.273 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.6943` → IC=+0.264 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6943 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.1472` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1472 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.549` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.549 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.3738` → IC=+0.227 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3738 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `0.9007` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9007 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2865` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2865 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `2.6612` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6612 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.0183` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0183 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.207 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.002` → IC=+0.182 (n=212)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.002 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1925` → IC=+0.205 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1925 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=220)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.301` → IC=+0.232 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.301 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.678` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.678 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.6392` → IC=+0.228 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6392 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.195` → IC=+0.199 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.195 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.1417` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1417 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.6478` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6478 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `12277.8554` → IC=+0.216 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12277.8554 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `248.0` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 248.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.172 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0065 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1453` → IC=+0.155 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1453 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.209 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.4145` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.4145 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.0095` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0095 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `3.8997` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 3.8997 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.175 (n=232)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.04 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `1970.8484` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1970.8484 (IC base=+0.145)

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

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.261 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1364` → IC=+0.197 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1364 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.332` → IC=+0.259 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.332 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.409` → IC=+0.259 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.409 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` < `1.2366` → IC=+0.223 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2366 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0792` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0792 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.9099` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9099 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=262)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `6728.8499` → IC=+0.198 (n=104)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6728.8499 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `195.0` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 195.0 (IC base=+0.191)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5556` → IC=-0.238 (n=82)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5556
  - _Potencial_: sin este filtro IC_bueno=+0.213 (n=249)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.8667 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.386` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 7.386 (IC base=+0.041)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.229 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.239 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.213 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5556 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.5773` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.5773 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.906` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.906 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `0.8656` → IC=+0.143 (n=166)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.8656 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.1184` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1184 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.5628` → IC=+0.123 (n=120)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.5628 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2493.5794` → IC=+0.194 (n=83)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2493.5794 (IC base=+0.101)

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

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.283 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.268 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.277 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.276 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.2353` → IC=+0.317 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2353 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` > `0.3918` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3918 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.724` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.724 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` > `1.0811` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0811 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.3468` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3468 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `1.7731` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7731 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `2699.3874` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2699.3874 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.262)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9524 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.863` → IC=+0.253 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.863 (IC base=+0.042)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.297 (n=67)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.1667 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.859` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.859 (IC base=+0.054)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `sigma_h` > `0.0026` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `volumen_spike_ratio` > `1.77` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.77
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.256 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.2468` → IC=+0.189 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2468 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 12.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.1986` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1986 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.506` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.506 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.03` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.03 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6181` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6181 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.6478` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6478 (IC base=+0.142)

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

- **PATRÓN** `ibs_20min` < `0.0816` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0816 (IC base=+0.047)

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

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.232 (n=1250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.228 (n=1419)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0038 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.235 (n=1275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.5011` → IC=+0.285 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5011 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.1545` → IC=+0.196 (n=931)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1545 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.023` → IC=+0.254 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.023 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.473` → IC=+0.225 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.473 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.6189` → IC=+0.204 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6189 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `1.234` → IC=+0.217 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.234 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.113` → IC=+0.245 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.113 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2523` → IC=+0.267 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2523 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.0258` → IC=+0.267 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0258 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.197 (n=196)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 56.0 (IC base=+0.223)

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

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.324 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.301)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.321 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.301)

- **PATRÓN** `drift_60min` |x|≤ `0.2101` → IC=+0.344 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2101 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.307 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.313 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.301)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.343 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5758 (IC base=+0.301)

- **PATRÓN** `volumen_pendiente_norm` < `0.0689` → IC=+0.348 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0689 (IC base=+0.301)

- **PATRÓN** `volumen_spike_ratio` < `1.8956` → IC=+0.333 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8956 (IC base=+0.301)

- **PATRÓN** `volumen_spike_ratio` > `2.8455` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8455 (IC base=+0.301)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.332 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `1980.3` → IC=+0.366 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1980.3 (IC base=+0.301)

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

- **PATRÓN** `sigma_h` < `0.0018` → IC=+0.207 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0018 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1874` → IC=+0.184 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1874 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.191 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` < `0.4082` → IC=+0.222 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4082 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1407` → IC=+0.186 (n=259)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1407 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.258` → IC=+0.252 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.258 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.3065` → IC=+0.180 (n=239)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.3065 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.8593` → IC=+0.189 (n=159)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.8593 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1081` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1081 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.6006` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6006 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `5196.667` → IC=+0.185 (n=214)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 5196.667 (IC base=+0.172)

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

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.357 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.277 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.272)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.306 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` < `0.5421` → IC=+0.339 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5421 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.123` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.123 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.236 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.3816` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3816 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` < `3.6802` → IC=+0.267 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.6802 (IC base=+0.272)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.272)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 35.0 (IC base=+0.272)

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

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.923` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 2.923 (IC base=+0.017)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.206 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1743` → IC=+0.165 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1743 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.222 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1817` → IC=+0.154 (n=186)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1817 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.399` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.399 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.391` → IC=+0.139 (n=250)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.391 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.197 (n=107)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.7028 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.0794` → IC=+0.152 (n=110)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0794 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` < `0.1742` → IC=+0.272 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1742 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.9831` → IC=+0.276 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9831 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.7285` → IC=+0.261 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7285 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1416.659` → IC=+0.223 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1416.659 (IC base=+0.133)

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

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.282 (n=360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.281 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4091` → IC=+0.309 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4091 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` > `0.3829` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3829 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.597` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.597 (IC base=+0.255)

- **PATRÓN** `volumen_regimen` > `0.8819` → IC=+0.293 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8819 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.5095` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5095 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `3.4227` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4227 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.255)

### GBM_LATE_5M
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=50)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=212)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.194 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.15` → IC=+0.198 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.15 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.233 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.5407` → IC=+0.153 (n=171)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5407 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.1852` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.1852 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.074` → IC=+0.158 (n=156)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.074 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.1834` → IC=+0.191 (n=150)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.1834 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.6677` → IC=+0.153 (n=171)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6677 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.152` → IC=+0.163 (n=161)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.152 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.817` → IC=+0.190 (n=169)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.817 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.4927` → IC=+0.149 (n=169)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4927 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=212)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7727.9509` → IC=+0.165 (n=171)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 7727.9509 (IC base=+0.146)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.179 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0033 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0685` → IC=+0.257 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0685 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.269 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.144 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.189` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 10.189 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2758` → IC=+0.170 (n=104)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2758 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.6545` → IC=+0.179 (n=104)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6545 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.2332` → IC=+0.149 (n=112)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.2332 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.7111` → IC=+0.179 (n=104)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.7111 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5051` → IC=+0.170 (n=104)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.5051 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `9874.0183` → IC=+0.151 (n=104)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 9874.0183 (IC base=+0.150)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.260 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0019` → IC=+0.220 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0019 (IC base=+0.223)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `libro_liquidez` < `3962.9688` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3962.9688
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

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

### MOMENTUM_IBS_15M
- **PATRÓN** `hora_utc` < `3.0` → IC=+0.147 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 3.0 (IC base=+0.077)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0662` → IC=+0.138 (n=147)

  - _Acción_: Kelly boost +0.69€ cuando `drift_20min_pct` |x|≤ 0.0662 (IC base=+0.077)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2255.3349` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 2255.3349
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=24)

- **PATRÓN** `libro_liquidez` > `2255.3349` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2255.3349 (IC base=-0.020)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.146)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.1286` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `drift_20min_pct` |x|≤ 0.1286 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.1731` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1731 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.0947` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.0947 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `1969.7035` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1969.7035 (IC base=+0.146)

### MOMENTUM_IBS_15M#BTC#15min
- **PATRÓN** `hora_utc` < `18.0` → IC=+0.145 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 18.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.9919` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.9919 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `19045.4888` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 19045.4888 (IC base=+0.085)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.239 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.093)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.0544` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.0544 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.0568` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.0568 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `20048.6739` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 20048.6739 (IC base=+0.093)

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
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 18.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.231 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.118)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.053` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.053 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.0752` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.0752 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `15323.3068` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15323.3068 (IC base=+0.118)

### MOMENTUM_IBS_15M#XRP#15min
- **PATRÓN** `hora_utc` < `2.0` → IC=+0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 2.0 (IC base=+0.045)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `hora_utc` < `14.0` → IC=-0.130 (n=214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=254)

- **FILTRO** `py_entrada` < `0.4` → IC=-0.276 (n=114)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=354)

- **FILTRO** `ibs_20min` < `0.7187` → IC=-0.237 (n=116)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7187
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=352)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.204 (n=113)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=355)

- **FILTRO** `libro_liquidez` < `1986.4584` → IC=-0.145 (n=308)

  - _Acción_: SKIP cuando `libro_liquidez` < 1986.4584
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=160)

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

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.138 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 14.0 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.1477` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.1477 (IC base=+0.063)

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

- **FILTRO** `py_entrada` > `0.53` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=73)

- **FILTRO** `ibs_20min` > `0.206` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` > 0.206
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=73)

- **FILTRO** `ballena_activa_n` > `49.0` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `ballena_activa_n` > 49.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=73)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=-0.041)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.230 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=43)

- **FILTRO** `ibs_20min` < `0.9535` → IC=-0.141 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.9535
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=27)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=57)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.063)

- **PATRÓN** `py_entrada` < `0.62` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.62 (IC base=+0.063)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `hora_utc` > `19.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=58)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=57)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.067)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.5 (IC base=+0.067)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

- **FILTRO** `ibs_20min` > `0.9118` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9118
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=52)

- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=59)

- **FILTRO** `ballena_activa_n` > `21.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 21.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=59)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **FILTRO** `drift_20min_pct` |x|> `0.1156` → IC=-0.182 (n=42)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1156
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=43)

- **FILTRO** `ibs_20min` < `0.7302` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7302
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=64)

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
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=192)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `0.9919` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.9919
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 14.0 (IC base=+0.079)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_liquidez` < `3903.1637` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3903.1637
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=45)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` > `0.931` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.931 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `3903.1637` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3903.1637 (IC base=+0.065)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `ibs_20min` < `0.2368` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.042)

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
- **FILTRO** `hora_utc` < `6.0` → IC=-0.186 (n=320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=992)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.284 (n=317)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=995)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.239 (n=328)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=984)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.196 (n=445)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=867)

- **FILTRO** `libro_liquidez` < `1979.0922` → IC=-0.155 (n=865)

  - _Acción_: SKIP cuando `libro_liquidez` < 1979.0922
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=447)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.189 (n=374)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1126)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.3` → IC=-0.269 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=162)

- **FILTRO** `ibs_7min` < `0.914` → IC=-0.188 (n=139)

  - _Acción_: SKIP cuando `ibs_7min` < 0.914
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=73)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.230 (n=98)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=114)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.226 (n=49)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=154)

- **FILTRO** `drift_7min_pct` |x|> `0.1093` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1093
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=153)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=213)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.314 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=204)

- **FILTRO** `ibs_7min` < `0.8` → IC=-0.243 (n=68)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=204)

- **FILTRO** `ballena_activa_n` > `112.0` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `ballena_activa_n` > 112.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=206)

- **FILTRO** `libro_liquidez` < `11004.0343` → IC=-0.135 (n=179)

  - _Acción_: SKIP cuando `libro_liquidez` < 11004.0343
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=93)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.182 (n=61)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=206)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.181 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=97)

- **FILTRO** `py_entrada` < `0.29` → IC=-0.418 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.29
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=142)

- **FILTRO** `ibs_7min` < `0.1416` → IC=-0.235 (n=47)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1416
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=142)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.271 (n=46)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=143)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.178 (n=119)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=121)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.5 (IC base=-0.037)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.214 (n=110)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=113)

- **FILTRO** `ibs_7min` < `0.883` → IC=-0.220 (n=73)

  - _Acción_: SKIP cuando `ibs_7min` < 0.883
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=150)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.169 (n=146)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=77)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.130 (n=79)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=178)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.219 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=188)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.267 (n=58)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=185)

- **FILTRO** `ibs_7min` < `0.7692` → IC=-0.217 (n=58)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=185)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.254 (n=59)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=184)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.247 (n=93)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=80)

- **FILTRO** `ibs_7min` < `0.7324` → IC=-0.297 (n=57)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7324
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=116)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.300 (n=43)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=130)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.245 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=211)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=28)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

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
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=41)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=42)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.167 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 10.0 (IC base=+0.047)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.047)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=78)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 20.0 (IC base=-0.009)

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

- **PATRÓN** `ibs_15` < `0.4651` → IC=+0.123 (n=415)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.62€ cuando `ibs_15` < 0.4651 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.5709` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.5709 (IC base=+0.083)

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

- **PATRÓN** `sigma_h` < `0.002` → IC=+0.191 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.002 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1803` → IC=+0.126 (n=105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.1803 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.0764` → IC=+0.128 (n=119)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.64€ cuando `ibs_15` > 0.0764 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.44` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.44 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `10347.0867` → IC=+0.136 (n=119)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 10347.0867 (IC base=+0.100)

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

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.150 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.184 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.004 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 16.0 (IC base=+0.140)

- **PATRÓN** `ibs_15` < `0.345` → IC=+0.167 (n=112)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.345 (IC base=+0.140)

- **PATRÓN** `ibs_15` > `0.0316` → IC=+0.181 (n=111)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.0316 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.4566` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4566 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `23.352` → IC=+0.188 (n=110)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 23.352 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11036.7661` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11036.7661 (IC base=+0.140)

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
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=80)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.167 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0022 (IC base=+0.061)

- **PATRÓN** `drift_15min` |x|≤ `0.1159` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.1159 (IC base=+0.061)

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

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.210 (n=36)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1154 (IC base=+0.045)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1048` → IC=+0.167 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1048 (IC base=+0.099)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0966` → IC=+0.162 (n=131)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.0966 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.122 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 19.0 (IC base=+0.099)

- **PATRÓN** `ibs_15` < `0.1282` → IC=+0.202 (n=65)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1282 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1093` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1093 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.427` → IC=+0.127 (n=148)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 9.427 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2605.055` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2605.055 (IC base=+0.099)

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
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=957)

- **PATRÓN** `ibs_15` > `0.6429` → IC=+0.233 (n=118)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6429 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.53` → IC=+0.271 (n=46)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.53 (IC base=-0.052)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.0929 (IC base=-0.052)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=367)

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

- **FILTRO** `sigma_ewma_delta_pct` > `7.734` → IC=-0.149 (n=92)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.734
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=297)

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

- **H-IBS-UPDOWN_GBM#SOL#5min**: dentro de BUY_NO, IBS < 0.1154 sube el IC de +0.045 a +0.210 en UPDOWN_GBM#SOL#5min (n=36). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5833 sube el IC de +0.102 a +0.227 en UPDOWN_GBM#15min (n=284). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.130 a +0.250 en UPDOWN_GBM#BTC#15min (n=34). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.7055 sube el IC de +0.100 a +0.337 en UPDOWN_GBM#ETH#15min (n=47). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS < 0.345 sube el IC de +0.140 a +0.167 en UPDOWN_GBM#ETH#15min (n=112). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_NO, IBS > 0.0316 sube el IC de +0.140 a +0.181 en UPDOWN_GBM#ETH#15min (n=111). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.033 a +0.242 en UPDOWN_GBM#SOL#15min (n=29). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.085 a +0.182 en UPDOWN_GBM#XRP#15min (n=86). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1282 sube el IC de +0.099 a +0.202 en UPDOWN_GBM#XRP#15min (n=65). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6429 sube el IC de -0.046 a +0.233 en UPDOWN_GBM_15M_TARDIO (n=118). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
| ✅ BALLENAS_CONFIRMADAS_15M | 490 | +0.045 | +37.59€ | 3 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 490 | +0.045 | +37.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 252 | +0.043 | +24.96€ | 2 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 210 | +0.024 | -0.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 210 | +0.024 | -0.34€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 28 | +0.200 | +12.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 28 | +0.200 | +12.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3540 | -0.115 | -555.78€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 468 | -0.025 | -21.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 3072 | -0.128 | -534.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 409 | -0.189 | -91.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 409 | -0.189 | -91.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 468 | -0.025 | -21.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 468 | -0.025 | -21.27€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 317 | -0.152 | -148.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 317 | -0.152 | -148.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 871 | +0.003 | -112.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 871 | +0.003 | -112.28€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 750 | -0.227 | -144.10€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 750 | -0.227 | -144.10€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 15189 | +0.114 | -896.04€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3492 | +0.183 | -98.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 100 | -0.098 | -46.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 8975 | +0.085 | -782.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2622 | +0.133 | +32.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1515 | +0.027 | -339.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 14 | -0.044 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1497 | +0.030 | -333.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 3423 | +0.140 | -4.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 955 | +0.199 | -28.79€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 41 | -0.105 | -20.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1495 | +0.111 | -16.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 932 | +0.138 | +62.21€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1511 | +0.056 | -260.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 10 | +0.000 | -3.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1500 | +0.057 | -254.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3701 | +0.127 | -38.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1290 | +0.162 | -16.17€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1491 | +0.103 | -21.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 908 | +0.119 | +7.70€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 3529 | +0.136 | -202.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1211 | +0.197 | -51.78€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 41 | +0.012 | -8.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1495 | +0.085 | -104.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 782 | +0.143 | -37.88€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1510 | +0.121 | -50.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | +1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1497 | +0.122 | -50.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3553 | +0.159 | -350.34€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3553 | +0.159 | -350.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 889 | +0.154 | -116.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 889 | +0.154 | -116.65€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 78 | -0.113 | -5.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 78 | -0.113 | -5.72€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 881 | +0.157 | -112.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 881 | +0.157 | -112.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 790 | +0.216 | -45.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 790 | +0.216 | -45.50€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 836 | +0.172 | -83.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 836 | +0.172 | -83.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 173 | +0.409 | -11.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 173 | +0.409 | -11.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 62 | +0.406 | -3.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 62 | +0.406 | -3.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 67 | +0.384 | -6.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 67 | +0.384 | -6.82€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 42 | +0.409 | -1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 42 | +0.409 | -1.47€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 6380 | +0.186 | -623.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 6380 | +0.186 | -623.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1195 | +0.093 | -276.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1195 | +0.093 | -276.72€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 981 | +0.244 | -15.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 981 | +0.244 | -15.69€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1117 | +0.155 | -158.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1117 | +0.155 | -158.05€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1025 | +0.222 | -43.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1025 | +0.222 | -43.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 992 | +0.244 | -14.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 992 | +0.244 | -14.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1070 | +0.180 | -116.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1070 | +0.180 | -116.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 2299 | +0.147 | +122.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 2299 | +0.147 | +122.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 1135 | +0.153 | +72.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 1135 | +0.153 | +72.17€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 1164 | +0.141 | +50.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 1164 | +0.141 | +50.55€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 546 | +0.301 | +6.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 546 | +0.301 | +6.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 229 | +0.275 | -8.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 229 | +0.275 | -8.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 255 | +0.302 | +7.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 255 | +0.302 | +7.49€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 62 | +0.375 | +7.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 62 | +0.375 | +7.35€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 230 | +0.409 | -10.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 230 | +0.409 | -10.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 103 | +0.405 | -5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 103 | +0.405 | -5.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 103 | +0.414 | -5.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 103 | +0.414 | -5.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 24 | +0.346 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 258 | +0.258 | -31.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 258 | +0.258 | -31.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 258 | +0.258 | -31.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 258 | +0.258 | -31.22€ | 0 | 5 |
| ✅ GBM_LATE_15M | 4681 | +0.085 | +1660.75€ | 0 | 13 |
| ✅ GBM_LATE_15M#15min | 4681 | +0.085 | +1660.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 817 | +0.176 | +519.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 817 | +0.176 | +519.82€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 467 | +0.180 | +240.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 467 | +0.180 | +240.46€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 824 | +0.189 | +558.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 824 | +0.189 | +558.78€ | 0 | 16 |
| ✅ GBM_LATE_15M#ETH | 622 | -0.002 | +37.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 622 | -0.002 | +37.44€ | 0 | 4 |
| ✅ GBM_LATE_15M#SOL | 872 | +0.002 | +79.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 872 | +0.002 | +79.29€ | 3 | 5 |
| ✅ GBM_LATE_15M#XRP | 1079 | +0.012 | +224.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1079 | +0.012 | +224.96€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5703 | +0.050 | +1711.66€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5703 | +0.050 | +1711.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1092 | -0.028 | +199.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1092 | -0.028 | +199.44€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1086 | -0.011 | +97.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1086 | -0.011 | +97.47€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 696 | +0.239 | +633.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 696 | +0.239 | +633.87€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 995 | -0.019 | +10.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 995 | -0.019 | +10.97€ | 6 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1008 | +0.002 | +102.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1008 | +0.002 | +102.21€ | 2 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 826 | +0.213 | +667.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 826 | +0.213 | +667.69€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 3430 | +0.175 | +2319.90€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 3430 | +0.175 | +2319.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 611 | +0.193 | +449.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 611 | +0.193 | +449.00€ | 0 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 458 | +0.194 | +301.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 458 | +0.194 | +301.47€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 607 | +0.201 | +469.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 607 | +0.201 | +469.82€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 430 | +0.208 | +314.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 430 | +0.208 | +314.25€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 636 | +0.072 | +250.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 636 | +0.072 | +250.52€ | 1 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 688 | +0.197 | +534.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 688 | +0.197 | +534.85€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 586 | +0.048 | +51.98€ | 0 | 6 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 586 | +0.048 | +51.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 110 | +0.045 | -0.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 110 | +0.045 | -0.72€ | 2 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 119 | +0.161 | +41.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 119 | +0.161 | +41.72€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 230 | -0.013 | +4.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 230 | -0.013 | +4.65€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 126 | +0.055 | +7.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 126 | +0.055 | +7.60€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO | 3987 | +0.168 | +2574.80€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3987 | +0.168 | +2574.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 787 | +0.187 | +554.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 787 | +0.187 | +554.76€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 525 | +0.155 | +278.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 525 | +0.155 | +278.48€ | 1 | 22 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 774 | +0.216 | +636.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 774 | +0.216 | +636.71€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 375 | +0.126 | +156.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 375 | +0.126 | +156.85€ | 1 | 22 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 639 | +0.076 | +276.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 639 | +0.076 | +276.43€ | 0 | 15 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 887 | +0.199 | +671.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 887 | +0.199 | +671.58€ | 0 | 23 |
| ✅ GBM_LATE_5M | 293 | +0.107 | +108.48€ | 3 | 13 |
| ✅ GBM_LATE_5M#5min | 293 | +0.107 | +108.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 153 | +0.113 | +57.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 153 | +0.113 | +57.72€ | 0 | 13 |
| ✅ GBM_LATE_5M#ETH | 83 | +0.194 | +48.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 83 | +0.194 | +48.75€ | 0 | 11 |
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
| ✅ LEADLAG_BTC_XRP_15M | 68 | +0.186 | +31.56€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 68 | +0.186 | +31.56€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 68 | +0.186 | +31.56€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 68 | +0.186 | +31.56€ | 0 | 2 |
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
| ✅ LIQUIDACIONES_5M | 98 | -0.120 | -13.50€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 98 | -0.120 | -13.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 36 | -0.053 | -2.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 36 | -0.053 | -2.69€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_15M | 738 | +0.034 | +26.92€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M#15min | 738 | +0.034 | +26.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 111 | +0.075 | +21.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 111 | +0.075 | +21.64€ | 1 | 6 |
| ✅ MOMENTUM_IBS_15M#BTC | 130 | +0.091 | +21.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 130 | +0.091 | +21.13€ | 0 | 7 |
| ✅ MOMENTUM_IBS_15M#DOGE | 115 | +0.013 | -10.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 115 | +0.013 | -10.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 134 | +0.066 | +26.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 134 | +0.066 | +26.00€ | 0 | 5 |
| ✅ MOMENTUM_IBS_15M#SOL | 122 | -0.048 | -22.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 122 | -0.048 | -22.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 126 | +0.000 | -8.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 126 | +0.000 | -8.96€ | 0 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 1005 | -0.038 | +11.38€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 1005 | -0.038 | +11.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 159 | -0.034 | +22.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 159 | -0.034 | +22.65€ | 4 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 175 | -0.065 | -19.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 175 | -0.065 | -19.21€ | 7 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 163 | -0.003 | +31.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 163 | -0.003 | +31.28€ | 3 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 176 | -0.011 | -3.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 176 | -0.011 | -3.04€ | 3 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 161 | -0.064 | -7.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 161 | -0.064 | -7.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 171 | -0.049 | -12.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 171 | -0.049 | -12.33€ | 4 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE | 350 | -0.045 | -19.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 350 | -0.045 | -19.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 55 | -0.009 | -1.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 55 | -0.009 | -1.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 50 | -0.154 | -8.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 50 | -0.154 | -8.53€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 28 | -0.133 | -4.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 67 | -0.080 | -6.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 67 | -0.080 | -6.18€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 81 | +0.018 | +0.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 81 | +0.018 | +0.94€ | 1 | 3 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 69 | +0.007 | -0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 69 | +0.007 | -0.01€ | 1 | 1 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 2812 | -0.063 | +79.00€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 2812 | -0.063 | +79.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 415 | -0.100 | +19.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 415 | -0.100 | +19.78€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 539 | -0.053 | +70.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 539 | -0.053 | +70.58€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 429 | -0.061 | -2.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 429 | -0.061 | -2.75€ | 5 | 1 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 480 | -0.077 | -31.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 480 | -0.077 | -31.96€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 512 | -0.043 | -8.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 512 | -0.043 | -8.72€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 437 | -0.051 | +32.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 437 | -0.051 | +32.08€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 2453 | +0.018 | +24.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 2453 | +0.018 | +24.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 411 | +0.025 | +11.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 411 | +0.025 | +11.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 341 | +0.039 | +8.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 341 | +0.039 | +8.88€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 421 | +0.006 | -2.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 421 | +0.006 | -2.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 431 | +0.010 | +2.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 431 | +0.010 | +2.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 442 | +0.011 | +1.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 442 | +0.011 | +1.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 407 | +0.021 | +2.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 407 | +0.021 | +2.04€ | 0 | 0 |
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
| ✅ STREAK_FADE_5M | 379 | -0.017 | -17.58€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 379 | -0.017 | -17.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 105 | +0.023 | +2.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 105 | +0.023 | +2.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 127 | -0.012 | -7.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 127 | -0.012 | -7.16€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 66 | -0.059 | -6.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 66 | -0.059 | -6.52€ | 2 | 2 |
| ✅ STREAK_FADE_5M#XRP | 81 | -0.042 | -5.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 81 | -0.042 | -5.97€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 15 | -0.066 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 9 | -0.061 | -1.63€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 640 | +0.013 | -6.55€ | 1 | 0 |
| ✅ STREAK_MOM_5M#5min | 640 | +0.013 | -6.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 206 | +0.014 | -1.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 206 | +0.014 | -1.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 119 | -0.021 | -4.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 119 | -0.021 | -4.79€ | 3 | 2 |
| ✅ STREAK_MOM_5M#SOL | 167 | +0.015 | -1.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 167 | +0.015 | -1.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 148 | +0.033 | +0.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 148 | +0.033 | +0.87€ | 1 | 1 |
| ✅ STRUCT_NO_15M | 1907 | +0.017 | -1.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1907 | +0.017 | -1.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 725 | +0.008 | -7.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 725 | +0.008 | -7.96€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 747 | +0.022 | +3.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 747 | +0.022 | +3.03€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 435 | +0.024 | +3.47€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 435 | +0.024 | +3.47€ | 2 | 0 |
| ✅ UPDOWN_GBM | 2446 | +0.029 | +194.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1051 | +0.091 | +205.84€ | 1 | 8 |
| ✅ UPDOWN_GBM#240min | 124 | +0.016 | -0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 968 | -0.011 | -0.08€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 256 | -0.023 | -10.57€ | 4 | 1 |
| ✅ UPDOWN_GBM#BNB | 107 | +0.133 | +32.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 100 | +0.157 | +34.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6 | -0.075 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 461 | +0.031 | +33.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 129 | +0.057 | -0.98€ | 2 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 38 | +0.075 | +3.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 190 | +0.062 | +37.76€ | 2 | 5 |
| ✅ UPDOWN_GBM#BTC#60min | 86 | -0.057 | -8.56€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 306 | +0.000 | -1.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 63 | +0.115 | +14.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 243 | -0.031 | -16.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 568 | +0.054 | +62.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 241 | +0.126 | +60.52€ | 1 | 13 |
| ✅ UPDOWN_GBM#ETH#240min | 38 | +0.050 | +1.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 170 | +0.006 | +2.04€ | 4 | 2 |
| ✅ UPDOWN_GBM#ETH#60min | 104 | +0.009 | -1.14€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 455 | -0.005 | +1.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 195 | +0.018 | +4.47€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 30 | -0.031 | -2.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 152 | +0.000 | -0.15€ | 2 | 1 |
| ✅ UPDOWN_GBM#SOL#60min | 66 | -0.029 | -0.87€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 547 | +0.025 | +68.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 323 | +0.094 | +92.53€ | 0 | 14 |
| ✅ UPDOWN_GBM#XRP#240min | 17 | -0.112 | -2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 207 | -0.069 | -21.37€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 112 | +0.254 | -0.89€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 112 | +0.254 | -0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 73 | +0.220 | -8.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 73 | +0.220 | -8.37€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 39 | +0.305 | +7.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 39 | +0.305 | +7.48€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1749 | -0.050 | +223.46€ | 2 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1749 | -0.050 | +223.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 122 | -0.073 | +1.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 122 | -0.073 | +1.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 337 | -0.140 | -17.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 337 | -0.140 | -17.77€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 42 | +0.000 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 42 | +0.000 | +2.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 134 | +0.000 | +19.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 134 | +0.000 | +19.88€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 567 | -0.017 | +140.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 567 | -0.017 | +140.58€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 547 | -0.039 | +76.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 547 | -0.039 | +76.74€ | 3 | 0 |
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