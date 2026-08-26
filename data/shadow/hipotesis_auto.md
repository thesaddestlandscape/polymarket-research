# Hipótesis automáticas — 2026-08-26 13:31 UTC
_Generado por shadow_postmortem.py sobre 162274 resoluciones (PNL=+11614.60€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.273 (n=223)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.288 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.149)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.165 (n=216)

  - _Acción_: Kelly boost +0.83€ cuando `n_ballena_banda` > 20.0 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.262 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.149)

- **PATRÓN** `banda_hit_calibrado` > `0.8211` → IC=+0.278 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8211 (IC base=+0.149)

- **PATRÓN** `banda_z` > `10.429` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.429 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.183 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=244)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3025.9246` → IC=+0.232 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3025.9246 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.014)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.725` → IC=+0.293 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.188)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.201 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 20.0 (IC base=+0.188)

- **PATRÓN** `n_total_lado` > `52.0` → IC=+0.247 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 52.0 (IC base=+0.188)

- **PATRÓN** `banda_hit_calibrado` > `0.8207` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8207 (IC base=+0.188)

- **PATRÓN** `banda_z` > `11.557` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.557 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.218 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=174)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `3111.6433` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3111.6433 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.007)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=86)

- **FILTRO** `banda_hit_calibrado` < `0.6284` → IC=-0.218 (n=37)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6284
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=77)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=90)

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

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.078)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.078)

- **PATRÓN** `banda_z` > `8.174` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 8.174 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `148.73` → IC=-0.279 (n=2248)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 148.73
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6749)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `n_ballenas` < `6.0` → IC=-0.167 (n=163)

  - _Acción_: SKIP cuando `n_ballenas` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=506)

- **FILTRO** `restante_s_al_confirmar` < `385.59` → IC=-0.287 (n=167)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 385.59
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=502)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `90.87` → IC=-0.436 (n=279)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 90.87
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=837)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `157.8` → IC=-0.200 (n=612)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.8
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1839)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `150.08` → IC=-0.274 (n=533)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 150.08
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1601)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.95` → IC=-0.344 (n=511)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.95
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=1040)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.187 (n=5166)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.7 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=1539)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2376.0723` → IC=+0.174 (n=1487)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2376.0723 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=3387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=4054)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.260 (n=3165)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=2852)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1836.4049` → IC=+0.180 (n=2383)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1836.4049 (IC base=+0.141)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.393 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.212 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `12480.3954` → IC=+0.214 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12480.3954 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.196 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.289 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=784)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `11931.9544` → IC=+0.207 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11931.9544 (IC base=+0.186)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.135 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.139 (n=527)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.555 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `4922.6447` → IC=+0.163 (n=203)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4922.6447 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.196 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.178 (n=299)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.415 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4200.2035` → IC=+0.156 (n=280)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4200.2035 (IC base=+0.136)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=1163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.130 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 15.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.309 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.291 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.285 (n=454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.416 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2840.5007` → IC=+0.292 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2840.5007 (IC base=+0.281)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.163 (n=277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.252 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=388)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2003.1828` → IC=+0.160 (n=313)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2003.1828 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.081)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.443 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.335 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.232 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `976.9593` → IC=+0.238 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 976.9593 (IC base=+0.220)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.265 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.192 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.342 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.213 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=272)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.102)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **FILTRO** `libro_liquidez` < `7570.2535` → IC=-0.254 (n=120)

  - _Acción_: SKIP cuando `libro_liquidez` < 7570.2535
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=40)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=4325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=3729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.203 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `3146.218` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3146.218 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=1071)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.72` → IC=+0.174 (n=941)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.72 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

- **FILTRO** `py_entrada` > `0.815` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.815
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=61)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.328)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.328)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=945)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.169 (n=403)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.7 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.170 (n=561)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.73 (IC base=+0.160)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.315 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.231)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=1058)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.196 (n=530)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.7 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.455 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.444)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.448 (n=191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.454 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.465 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.444)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.452 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.446)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.448 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.453 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.446)

- **PATRÓN** `libro_liquidez` > `12563.6486` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.6486 (IC base=+0.446)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.442 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.425 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.425 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `3697.0572` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3697.0572 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.457 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.92` → IC=+0.439 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.92 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.435 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `1765.2976` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1765.2976 (IC base=+0.441)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=10291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=7675)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.221 (n=8107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=2214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.132 (n=1416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.158 (n=1547)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.71 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.274 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.238)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=746)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.166 (n=1322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.211 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.161)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.237 (n=1638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.231 (n=1320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.231)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.247 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.217)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=1295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.211 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.184)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.134)

- **PATRÓN** `restante_min` < `3.93` → IC=+0.141 (n=1387)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 3.93 (IC base=+0.134)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.162 (n=1388)

  - _Acción_: Kelly boost +0.81€ cuando `restante_min` > 4.93 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=4359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.150 (n=1836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `lag_apertura_s` < `4.5` → IC=+0.162 (n=1391)

  - _Acción_: Kelly boost +0.81€ cuando `lag_apertura_s` < 4.5 (IC base=+0.134)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.141)

- **PATRÓN** `restante_min` < `3.91` → IC=+0.143 (n=699)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` < 3.91 (IC base=+0.141)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.173 (n=689)

  - _Acción_: Kelly boost +0.86€ cuando `restante_min` > 4.91 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.152 (n=1835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `lag_apertura_s` < `5.7` → IC=+0.173 (n=689)

  - _Acción_: Kelly boost +0.86€ cuando `lag_apertura_s` < 5.7 (IC base=+0.141)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=789)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.126)

- **PATRÓN** `restante_min` < `3.98` → IC=+0.135 (n=702)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 3.98 (IC base=+0.126)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.161 (n=755)

  - _Acción_: Kelly boost +0.80€ cuando `restante_min` > 4.94 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=2185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=930)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `lag_apertura_s` < `3.46` → IC=+0.166 (n=698)

  - _Acción_: Kelly boost +0.83€ cuando `lag_apertura_s` < 3.46 (IC base=+0.126)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.306 (n=220)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.301)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.380 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `3861.5788` → IC=+0.301 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3861.5788 (IC base=+0.301)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.286 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.281 (n=222)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5623.4735` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5623.4735 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.339 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.304)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.309 (n=271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.304)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.304)

- **PATRÓN** `libro_liquidez` > `1864.2726` → IC=+0.323 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1864.2726 (IC base=+0.304)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.391 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.359)

- **PATRÓN** `py_entrada` > `0.88` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.88 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.357 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `786.7393` → IC=+0.381 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 786.7393 (IC base=+0.359)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.420 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.422 (n=241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.412)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.420 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.412)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.426 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.412)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.411 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.412)

- **PATRÓN** `libro_liquidez` > `1852.2015` → IC=+0.425 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1852.2015 (IC base=+0.412)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.417 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.414 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.420 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `5548.4507` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5548.4507 (IC base=+0.409)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.422 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.417)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.417)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.422 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.417)

- **PATRÓN** `libro_liquidez` > `1864.6918` → IC=+0.439 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1864.6918 (IC base=+0.417)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.299 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.436 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1518.0458` → IC=+0.324 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1518.0458 (IC base=+0.282)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.299 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.436 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1518.0458` → IC=+0.324 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1518.0458 (IC base=+0.282)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9498` → IC=+0.213 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9498 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.2097` → IC=+0.234 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2097 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` < `1.0239` → IC=+0.218 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.0239 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.231` → IC=+0.169 (n=865)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.231 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.63 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.0608` → IC=+0.262 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0608 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0784` → IC=+0.134 (n=470)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.0784 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.5756` → IC=+0.145 (n=496)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5756 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.2136` → IC=+0.129 (n=1456)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.2136 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3016` → IC=+0.148 (n=734)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.3016 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.6357` → IC=+0.155 (n=236)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6357 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `1.0494` → IC=+0.150 (n=321)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0494 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1751` → IC=+0.255 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1751 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.6134` → IC=+0.205 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6134 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.924` → IC=+0.235 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.924 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.240 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.030)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.200 (n=158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.168 (n=230)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 8.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.717` → IC=+0.330 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.717 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.145 (n=257)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.04 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.296 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.321 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.343 (n=164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.283 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.282 (n=227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.466` → IC=+0.326 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.466 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.972` → IC=+0.321 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.972 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` < `0.0596` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0596 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.7507` → IC=+0.304 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7507 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `1.5366` → IC=+0.298 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5366 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.328 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `1989.8695` → IC=+0.309 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1989.8695 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.315 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.278)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.250 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.239 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3375` → IC=+0.222 (n=307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3375 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.241 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.217 (n=316)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.4287` → IC=+0.224 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4287 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.3109` → IC=+0.235 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3109 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.5508` → IC=+0.215 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5508 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.271` → IC=+0.247 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.271 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `0.7062` → IC=+0.218 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7062 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.258 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0762` → IC=+0.213 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0762 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2656` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2656 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4455` → IC=+0.272 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4455 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `11170.0615` → IC=+0.226 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11170.0615 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.193 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0021 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.147 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0054 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1677` → IC=+0.158 (n=273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1677 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.4268` → IC=+0.174 (n=360)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.4268 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1424` → IC=+0.171 (n=341)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1424 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.938` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.938 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6337` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6337 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.0208` → IC=+0.144 (n=186)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0208 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0937` → IC=+0.223 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0937 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.7427` → IC=+0.180 (n=204)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.7427 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.4117` → IC=+0.162 (n=306)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4117 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=528)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `14050.8954` → IC=+0.183 (n=137)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14050.8954 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `227.0` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 227.0 (IC base=+0.142)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0684` → IC=+0.129 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.0684 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.924` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.924 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=198)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `1917.9762` → IC=+0.142 (n=191)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1917.9762 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.128 (n=92)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 30.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.283 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.37` → IC=+0.273 (n=302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.37 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.264 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.272 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.5294` → IC=+0.293 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5294 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.961` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.961 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.4179` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4179 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.8237` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8237 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.7662` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7662 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.281 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.221 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.260)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.872` → IC=-0.170 (n=189)

  - _Acción_: SKIP cuando `ibs_20min` > 0.872
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=569)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=63)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=695)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.124 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.0838` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0838 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `1.1445` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1445 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7026 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.1127` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1127 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.8068` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8068 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.2362` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2362 (IC base=-0.055)

- **PATRÓN** `volumen_regimen` > `0.6189` → IC=+0.122 (n=96)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.6189 (IC base=-0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.055` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.055 (IC base=-0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.3816` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3816 (IC base=-0.055)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=-0.055)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `ibs_20min` > `0.76` → IC=-0.162 (n=312)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=940)

- **FILTRO** `sigma_ewma_delta_pct` > `4.919` → IC=-0.153 (n=266)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.919
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=986)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.040)

- **PATRÓN** `drift_60min` |x|≤ `0.2653` → IC=+0.138 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2653 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `0.5263` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.5263 (IC base=+0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.4991` → IC=-0.138 (n=216)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.4991
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=422)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.141 (n=104)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=534)

- **FILTRO** `ibs_20min` > `0.7778` → IC=-0.167 (n=280)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=846)

- **FILTRO** `sigma_ewma_delta_pct` > `6.624` → IC=-0.167 (n=187)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.624
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=939)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.083)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` < `0.2029` → IC=+0.226 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2029 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=-0.034)

- **PATRÓN** `volumen_regimen` > `1.1383` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1383 (IC base=-0.034)

- **PATRÓN** `volumen_spike_ratio` > `1.9841` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.9841 (IC base=-0.034)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.149 (n=896)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0087 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.9462` → IC=+0.245 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9462 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `1.2452` → IC=+0.288 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2452 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` > `1.0201` → IC=+0.194 (n=420)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.0201 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` < `0.1152` → IC=+0.168 (n=1184)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1152 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2472` → IC=+0.203 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2472 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `1.4823` → IC=+0.187 (n=407)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4823 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `2.8672` → IC=+0.165 (n=407)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.8672 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.269 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0966` → IC=+0.178 (n=1155)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.0966 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `1.0527` → IC=+0.214 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0527 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1466` → IC=+0.201 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1466 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.6271` → IC=+0.210 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6271 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2514` → IC=+0.355 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2514 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.3777` → IC=+0.281 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3777 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.253 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.039)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `5.153` → IC=-0.205 (n=120)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.153
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=599)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.08` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.08 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.0503` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0503 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.5866` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5866 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `volumen_regimen` > `0.9955` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.9955 (IC base=-0.041)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.205 (n=181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.264 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.958` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.958 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` < `0.1461` → IC=+0.186 (n=307)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1461 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.4263` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.4263 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.035` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.035 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `3.7364` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 3.7364 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `1915.5084` → IC=+0.214 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.5084 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.192 (n=105)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 54.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.366 (n=214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.346)

- **PATRÓN** `drift_60min` |x|≤ `0.2083` → IC=+0.361 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2083 (IC base=+0.346)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.385 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.346)

- **PATRÓN** `ibs_20min` < `0.3056` → IC=+0.356 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3056 (IC base=+0.346)

- **PATRÓN** `ibs_20min` > `0.1351` → IC=+0.347 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1351 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.446` → IC=+0.348 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.446 (IC base=+0.346)

- **PATRÓN** `volumen_pendiente_norm` > `0.1384` → IC=+0.381 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1384 (IC base=+0.346)

- **PATRÓN** `volumen_spike_ratio` < `1.7842` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7842 (IC base=+0.346)

- **PATRÓN** `volumen_spike_ratio` > `1.997` → IC=+0.336 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.997 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `1900.976` → IC=+0.349 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1900.976 (IC base=+0.346)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.346)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.149 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=297)

- **FILTRO** `dist_vwap_pct` < `0.6615` → IC=-0.211 (n=43)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6615
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=24)

- **FILTRO** `volumen_regimen` > `1.0046` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0046
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=51)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `volumen_regimen` > `0.8819` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8819
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `volumen_pendiente_norm` < `0.0424` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0424
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=885)

- **PATRÓN** `dist_vwap_pct` > `0.6615` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6615 (IC base=-0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.3934` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3934 (IC base=-0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.091` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.091 (IC base=-0.071)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.5333` → IC=-0.149 (n=303)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5333
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=304)

- **FILTRO** `ibs_20min` > `0.7436` → IC=-0.168 (n=218)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7436
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=656)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=52)

- **FILTRO** `volumen_regimen` > `1.3709` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3709
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=52)

- **PATRÓN** `ibs_20min` > `0.85` → IC=+0.247 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.85 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` > `0.3163` → IC=+0.250 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3163 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.175 (n=115)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8622 (IC base=-0.009)

- **PATRÓN** `volumen_regimen` > `1.1437` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.1437 (IC base=-0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2337` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2337 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.4987` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4987 (IC base=-0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.0538` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.0538 (IC base=-0.009)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.203 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=-0.009)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0236` → IC=+0.319 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0236 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9016` → IC=+0.292 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9016 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.8873` → IC=+0.327 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8873 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.169` → IC=+0.275 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.169 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.8368` → IC=+0.251 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8368 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.0807` → IC=+0.223 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0807 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4052` → IC=+0.253 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4052 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.233 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2661.3588` → IC=+0.234 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2661.3588 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.282 (n=246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.4769` → IC=+0.271 (n=487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4769 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.277 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.2766` → IC=+0.324 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2766 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` < `0.2448` → IC=+0.277 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2448 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.698` → IC=+0.312 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.698 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `1.2502` → IC=+0.302 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2502 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.1688` → IC=+0.299 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1688 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.249 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.266)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.194 (n=1050)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0082 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.8919` → IC=+0.257 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8919 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.7903` → IC=+0.253 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7903 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.334` → IC=+0.252 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.334 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.160 (n=1608)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2177 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.6867` → IC=+0.172 (n=1436)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.6867 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.180 (n=822)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.2835` → IC=+0.157 (n=1819)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.2835 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.8576` → IC=+0.146 (n=1378)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8576 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=1898)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `3831.2799` → IC=+0.193 (n=772)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3831.2799 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.180 (n=1080)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 125.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.202 (n=1825)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.3937` → IC=+0.201 (n=2072)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3937 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.217 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.4063` → IC=+0.237 (n=2072)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4063 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.3513` → IC=+0.177 (n=1820)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.3513 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.785` → IC=+0.220 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.785 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.176` → IC=+0.165 (n=1688)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.176 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.8596` → IC=+0.173 (n=1125)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8596 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.248 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.8709` → IC=+0.178 (n=976)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.8709 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6202` → IC=+0.208 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6202 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.180 (n=1031)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 203.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.231 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.314 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.973` → IC=+0.356 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.973 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1402` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1402 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4214` → IC=+0.141 (n=293)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4214 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.280 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.274)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.289 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.3227` → IC=+0.317 (n=178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3227 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.318 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` < `0.3503` → IC=+0.311 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3503 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.89` → IC=+0.298 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.89 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` < `0.081` → IC=+0.294 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.081 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` < `1.7889` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7889 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `1982.2745` → IC=+0.355 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.2745 (IC base=+0.274)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.316 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.274)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.236 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.221 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4979` → IC=+0.223 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4979 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.211` → IC=+0.250 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.211 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.777` → IC=+0.250 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.777 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6321` → IC=+0.209 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6321 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.8983` → IC=+0.201 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8983 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2676` → IC=+0.255 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2676 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.3897` → IC=+0.250 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3897 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `11952.667` → IC=+0.210 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11952.667 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.215 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.29` → IC=+0.178 (n=423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.29 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.176 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.4047` → IC=+0.189 (n=423)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.4047 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1569` → IC=+0.181 (n=412)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1569 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.484` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.484 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6405` → IC=+0.227 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6405 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1711` → IC=+0.230 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1711 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.732` → IC=+0.179 (n=210)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.732 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `14111.5146` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 14111.5146 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 239.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.144` → IC=+0.156 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.144 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.218 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.293 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2298` → IC=+0.139 (n=275)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.2298 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.0095` → IC=+0.210 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0095 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=155)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `1961.8084` → IC=+0.175 (n=112)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1961.8084 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.305 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1893` → IC=+0.323 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1893 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.337 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.0082` → IC=+0.387 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0082 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.335` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.335 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.399` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.399 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.0261` → IC=+0.292 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0261 (IC base=+0.283)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.219 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.4977` → IC=+0.203 (n=325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4977 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.206 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.4502` → IC=+0.243 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4502 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `1.0396` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0396 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.407` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.407 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.6356` → IC=+0.200 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6356 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.1005` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1005 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.435` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.435 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.4478` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4478 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=367)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `8624.0494` → IC=+0.203 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8624.0494 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.188 (n=174)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 156.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.244 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3741` → IC=+0.166 (n=405)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3741 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.179 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.3456` → IC=+0.212 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3456 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.5272` → IC=+0.158 (n=475)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.5272 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.315` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.315 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8556` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8556 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6177` → IC=+0.154 (n=405)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6177 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1001` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1001 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.8878` → IC=+0.187 (n=199)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.8878 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.122 (n=191)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 196.0 (IC base=+0.143)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.205 (n=154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.8511` → IC=+0.235 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8511 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.7937` → IC=+0.270 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7937 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.134 (n=462)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.6182 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.5701` → IC=+0.128 (n=385)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.5701 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2913.4394` → IC=+0.184 (n=210)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2913.4394 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.187 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0048 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.195 (n=185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 14.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.4098` → IC=+0.229 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4098 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2166` → IC=+0.139 (n=355)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2166 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.672` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.672 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.8565` → IC=+0.168 (n=257)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.8565 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2168` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2168 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.2636` → IC=+0.216 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2636 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=329)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2044.392` → IC=+0.168 (n=257)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2044.392 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0222` → IC=+0.197 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0222 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.1619` → IC=+0.189 (n=220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1619 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.164 (n=227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.258 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.9761` → IC=+0.240 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9761 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.073` → IC=+0.244 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.073 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2022` → IC=+0.165 (n=499)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2022 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.8296` → IC=+0.192 (n=332)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.8296 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0805` → IC=+0.215 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0805 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.1643` → IC=+0.179 (n=406)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.1643 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.167 (n=307)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=557)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.284 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.399` → IC=+0.237 (n=420)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.399 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=229)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.3738` → IC=+0.256 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3738 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `1.1476` → IC=+0.225 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.1476 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.162` → IC=+0.268 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.162 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.7158` → IC=+0.238 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7158 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.7123` → IC=+0.271 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7123 (IC base=+0.219)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.6275` → IC=+0.150 (n=349)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6275 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.7807` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7807 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.104` → IC=+0.212 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.104 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1717` → IC=+0.183 (n=99)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1717 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2945.8225` → IC=+0.122 (n=260)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2945.8225 (IC base=+0.082)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.180 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0034 (IC base=+0.071)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.142 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 13.0 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.6296` → IC=+0.124 (n=354)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.6296 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.101` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.101 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.6508` → IC=+0.143 (n=113)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6508 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.6065` → IC=+0.157 (n=132)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.6065 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `9388.7076` → IC=+0.144 (n=161)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 9388.7076 (IC base=+0.071)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.176 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=69)

- **FILTRO** `ibs_20min` < `0.381` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.381
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `libro_liquidez` < `6190.8221` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 6190.8221
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` > `0.9291` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9291 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7932` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7932 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.351` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 4.351 (IC base=+0.024)

- **PATRÓN** `libro_liquidez` > `11186.7795` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 11186.7795 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.238 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.216 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2802` → IC=+0.195 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.2802 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.179 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 13.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.185 (n=128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 13.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.6561` → IC=+0.197 (n=143)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6561 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.493` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.493 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.2319` → IC=+0.184 (n=131)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.2319 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.492` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.492 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.197 (n=143)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 1.218 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.0867` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0867 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5104` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5104 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.3274` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3274 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `12888.6124` → IC=+0.170 (n=95)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 12888.6124 (IC base=+0.167)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.285 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.300 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.2275` → IC=+0.271 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2275 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.333 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` > `0.999` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.999 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.561` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.561 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` < `0.6762` → IC=+0.378 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6762 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `2.2928` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2928 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `1.5483` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5483 (IC base=+0.271)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.367 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.058)

- **PATRÓN** `drift_60min` |x|≤ `0.2707` → IC=+0.155 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2707 (IC base=+0.058)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.227 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.6219` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.6219 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.025` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 6.025 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `9491.207` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9491.207 (IC base=+0.058)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5417` → IC=-0.208 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5417
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=141)

- **FILTRO** `ibs_20min` > `0.66` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=82)

- **FILTRO** `dist_vwap_pct` > `0.1911` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1911
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=88)

- **FILTRO** `volumen_pendiente_norm` > `0.1063` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1063
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=65)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.125 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.013)

- **PATRÓN** `ibs_20min` > `0.9868` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.9868 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` > `0.5918` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5918 (IC base=+0.013)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6522 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.2226` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2226 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.99` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.99 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0773 (IC base=+0.029)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.212 (n=1219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.156 (n=2415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 8.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.9437` → IC=+0.289 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9437 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `1.0669` → IC=+0.252 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0669 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.365` → IC=+0.246 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.365 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.6321` → IC=+0.154 (n=634)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6321 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `1.0819` → IC=+0.156 (n=862)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0819 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.182 (n=680)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.3299` → IC=+0.145 (n=2087)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.3299 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.8862` → IC=+0.156 (n=1581)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8862 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=2197)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3801.753` → IC=+0.197 (n=896)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3801.753 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.194 (n=1153)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 162.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.227 (n=1614)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4451` → IC=+0.203 (n=2417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4451 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.195 (n=2201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.199 (n=893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5506` → IC=+0.248 (n=2417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5506 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.7107` → IC=+0.181 (n=1982)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.7107 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.417` → IC=+0.224 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.417 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.645` → IC=+0.197 (n=2271)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 2.645 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.6239` → IC=+0.188 (n=613)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6239 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.189 (n=613)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.1929 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.270 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.2624` → IC=+0.212 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2624 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `182.0` → IC=+0.167 (n=1291)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 182.0 (IC base=+0.193)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.224 (n=197)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.167 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 11.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.284 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.431` → IC=+0.356 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.431 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2129` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2129 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.8938` → IC=+0.130 (n=236)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.8938 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.315 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.1543` → IC=+0.326 (n=170)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1543 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.283 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.296 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.341 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.979` → IC=+0.309 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.979 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` < `0.0695` → IC=+0.300 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0695 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.6987` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6987 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `1997.707` → IC=+0.339 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1997.707 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 68.0 (IC base=+0.280)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.185 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0028 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.220 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3282` → IC=+0.211 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3282 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.2647` → IC=+0.247 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2647 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.757` → IC=+0.209 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.757 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6538` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6538 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.0941` → IC=+0.191 (n=192)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.0941 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1444` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1444 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.1158` → IC=+0.192 (n=329)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.1158 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.4704` → IC=+0.184 (n=334)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4704 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `11693.3416` → IC=+0.197 (n=282)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 11693.3416 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.202 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.176 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0057 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.1687` → IC=+0.186 (n=275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1687 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.179 (n=428)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 18.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.3756` → IC=+0.215 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3756 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.7539` → IC=+0.176 (n=455)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.7539 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.682` → IC=+0.224 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.682 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6259` → IC=+0.236 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6259 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.204` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.204 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1498` → IC=+0.294 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1498 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.7452` → IC=+0.200 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7452 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.4122` → IC=+0.191 (n=315)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4122 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=531)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `13332.8168` → IC=+0.169 (n=137)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 13332.8168 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `313.0` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 313.0 (IC base=+0.167)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.186 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.241 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.7122` → IC=+0.256 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7122 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.113` → IC=+0.338 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.113 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.2327` → IC=+0.181 (n=286)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.2327 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `2.1217` → IC=+0.182 (n=124)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.1217 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `3.8523` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 3.8523 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.193 (n=242)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.03 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `1917.9762` → IC=+0.199 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.9762 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.235 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.330 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.274 (n=162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.264)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.269 (n=327)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` < `0.5575` → IC=+0.332 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5575 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.108` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.108 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.3655` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3655 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.264)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.272 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.264)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 19.0 (IC base=+0.264)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.153 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0089 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1452` → IC=+0.142 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1452 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.168 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.3491` → IC=+0.196 (n=426)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3491 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.9062` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9062 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.544` → IC=+0.194 (n=204)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 4.544 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6318` → IC=+0.197 (n=143)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6318 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.2022` → IC=+0.160 (n=142)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.2022 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2691` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2691 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.4116` → IC=+0.237 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4116 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4789.9771` → IC=+0.231 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4789.9771 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.197 (n=199)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 167.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.225 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4941` → IC=+0.164 (n=352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.4941 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.178 (n=253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 11.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.0817` → IC=+0.245 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0817 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1609` → IC=+0.156 (n=181)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1609 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.6682` → IC=+0.175 (n=376)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.6682 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.457` → IC=+0.258 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.457 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.5903` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.5903 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `1.1142` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.1142 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2303` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2303 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1819` → IC=+0.187 (n=260)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.1819 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4569` → IC=+0.177 (n=295)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4569 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `9323.6962` → IC=+0.198 (n=160)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 9323.6962 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.244 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 138.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.170 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0107 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.132 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 12.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.9062` → IC=+0.300 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9062 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.7691` → IC=+0.252 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7691 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.432` → IC=+0.223 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.432 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2898.7698` → IC=+0.278 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2898.7698 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.171 (n=256)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 68.0 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.185 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0059 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.2594` → IC=+0.138 (n=299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2594 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.198 (n=448)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5714 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.4633` → IC=+0.137 (n=406)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.4633 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.994` → IC=+0.135 (n=439)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 2.994 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.703` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.703 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.072` → IC=+0.175 (n=121)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.072 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.7463` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.7463 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=469)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2571.994` → IC=+0.163 (n=203)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2571.994 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.215 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.9722` → IC=+0.301 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9722 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `1.4073` → IC=+0.294 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4073 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.053` → IC=+0.252 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.053 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.6122` → IC=+0.184 (n=191)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6122 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `1.0445` → IC=+0.195 (n=260)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.0445 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1718` → IC=+0.258 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1718 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `1.8344` → IC=+0.183 (n=348)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8344 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=638)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `3109.2978` → IC=+0.179 (n=191)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 3109.2978 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.220 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.296 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.6476` → IC=+0.221 (n=628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6476 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.222 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.4887` → IC=+0.276 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4887 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `1.1519` → IC=+0.220 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.1519 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.6` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.6 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.02` → IC=+0.215 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.02 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.254 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.5476` → IC=+0.232 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5476 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.159 (n=309)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 33.0 (IC base=+0.211)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=890)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.131 (n=358)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0105 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.8291` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.8291 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `1.5265` → IC=+0.206 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.5265 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.7125` → IC=+0.140 (n=159)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7125 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.1533` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1533 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.1228` → IC=+0.126 (n=351)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.1228 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=396)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8162.0536` → IC=+0.148 (n=271)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 8162.0536 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.201 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3507` → IC=+0.167 (n=599)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3507 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.204 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6296` → IC=+0.152 (n=598)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.6296 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.184` → IC=+0.144 (n=607)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.184 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.6272` → IC=+0.171 (n=156)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6272 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.8049` → IC=+0.142 (n=771)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.8049 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.151` → IC=+0.161 (n=305)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.151 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.061` → IC=+0.145 (n=682)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.061 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2237` → IC=+0.159 (n=669)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2237 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.162 (n=329)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.489` → IC=+0.163 (n=672)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.489 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.5137` → IC=+0.149 (n=600)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5137 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=890)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `8382.2484` → IC=+0.150 (n=679)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8382.2484 (IC base=+0.144)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `dist_vwap_pct` < `0.6194` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6194
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=46)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.146 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 12.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.9366` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.9366 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.6194` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6194 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.972` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 3.972 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `0.5135` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5135 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.0831` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.0831 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `12213.6971` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12213.6971 (IC base=+0.059)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.191 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0044 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.338` → IC=+0.150 (n=375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.338 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.198 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.165 (n=165)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.144 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6099` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6099 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.148 (n=379)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1847` → IC=+0.145 (n=375)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1847 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6217` → IC=+0.139 (n=375)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6217 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0724` → IC=+0.180 (n=179)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0724 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.5688` → IC=+0.153 (n=373)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5688 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.1689` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.1689 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `11854.8179` → IC=+0.141 (n=335)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 11854.8179 (IC base=+0.137)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.181 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0092 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4362` → IC=+0.152 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4362 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.222 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.2929` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.2929 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.7909` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.7909 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `1.0394` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0394 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.4185` → IC=+0.155 (n=175)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.4185 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.435` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.435 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.159` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 7.159 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.0961` → IC=+0.141 (n=179)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0961 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1211` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1211 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.157 (n=199)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8385.7236` → IC=+0.175 (n=204)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 8385.7236 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.181 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0088 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.4057` → IC=+0.203 (n=183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4057 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.183 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 9.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.089` → IC=+0.191 (n=208)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.089 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1899` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1899 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.7707` → IC=+0.162 (n=232)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.7707 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.388` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.388 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6723` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6723 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.0653` → IC=+0.180 (n=176)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0653 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.1175` → IC=+0.207 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1175 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.4319` → IC=+0.184 (n=204)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4319 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `10385.425` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 10385.425 (IC base=+0.156)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

- **FILTRO** `sigma_ewma_delta_pct` < `3.03` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.03
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=22)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.773` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.773 (IC base=-0.006)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7741` → IC=-0.167 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7741
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=119)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=160)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.260 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=110)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `volumen_regimen` < `0.6601` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6601
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=83)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.178 (n=150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0054 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.7741` → IC=+0.227 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7741 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `1.4999` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4999 (IC base=+0.058)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=119)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `1942.5119` → IC=+0.130 (n=98)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1942.5119 (IC base=+0.058)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7741` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7741
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=43)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.061)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.125 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 10.0 (IC base=+0.061)

- **PATRÓN** `ibs_20min` > `0.7741` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7741 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.15` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 13.15 (IC base=+0.061)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=43)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **FILTRO** `ibs_20min` > `0.2768` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2768
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `volumen_regimen` > `0.8876` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8876
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.171 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` < `0.1239` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1239 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.06` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.06 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.6214` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6214 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2519.6873` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2519.6873 (IC base=+0.107)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **FILTRO** `sigma_h` > `0.0165` → IC=-0.309 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0165
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=59)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.217 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=20)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.272 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `volumen_regimen` > `0.903` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.903
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=-0.026)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.344 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=36)

- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=74)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `dist_vwap_pct` > `0.3507` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3507
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=80)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.002` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `ibs_20min` < `0.4953` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4953
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `drift_60min` |x|> `0.0966` → IC=-0.262 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0966
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.274 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

- **FILTRO** `ibs_20min` > `0.6267` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6267
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` < `7.79` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 7.79
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `sigma_ewma_delta_pct` > `4.524` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.524
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=26)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `libro_liquidez` < `4361.6218` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4361.6218
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `drift_60min` |x|> `0.0425` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0425
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `ibs_20min` > `0.8144` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8144
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `dist_vwap_pct` < `0.2821` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2821
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `sigma_ewma_delta_pct` < `5.949` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.949
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `volumen_regimen` > `0.6161` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.6161
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `ibs_20min` < `0.6` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.342 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.382 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `ibs_20min` > `0.2759` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `ibs_20min` < `0.7391` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `dist_vwap_pct` < `0.3782` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3782
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `libro_liquidez` < `1344.8221` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 1344.8221
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=6)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.513` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.513
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.2275` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2275
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=112)

- **PATRÓN** `ibs_20min` > `0.5842` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.5842 (IC base=+0.046)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 12.0 (IC base=+0.025)

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

- **PATRÓN** `drift_60min` |x|≤ `0.129` → IC=+0.147 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.129 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.3803` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3803 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.574` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.574 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6628` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6628 (IC base=+0.094)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0022` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0022
  - _Potencial_: sin este filtro IC_bueno=+0.321 (n=26)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1478` → IC=+0.147 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1478 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.8029` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8029 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.517` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.517 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `ibs_20min` > `0.0435` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0435
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2598.9726` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.9726 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.148 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2495.3515` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2495.3515 (IC base=+0.126)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2598.9726` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.9726 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.148 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2495.3515` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2495.3515 (IC base=+0.126)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=43)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=98)

- **FILTRO** `libro_liquidez` < `2110.4161` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 2110.4161
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=86)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_15M#XRP#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=390)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.129 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=361)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9427` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9427
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=77)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35151.71` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `liq_usd_total` < 35151.71
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=33)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **PATRÓN** `liq_usd_total` > `35151.71` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `liq_usd_total` > 35151.71 (IC base=-0.007)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.8738` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.8738
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=48)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=36)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=114)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.139 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=96)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_usd_total` < `5231.58` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 5231.58
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9861` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9861
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=84)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=85)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=51)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=73)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=25)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_usd_total` < `20545.57` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `liq_usd_total` < 20545.57
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2127.4213` → IC=-0.136 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 2127.4213
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=129)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=379)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1852` → IC=-0.129 (n=95)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1852
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=186)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.168 (n=752)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2301)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.217 (n=718)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2314)

- **FILTRO** `ibs_20min` > `0.2727` → IC=-0.181 (n=756)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=2276)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.231 (n=102)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=345)

- **FILTRO** `ibs_20min` < `0.7263` → IC=-0.199 (n=111)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7263
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=336)

- **FILTRO** `ibs_20min` > `0.2721` → IC=-0.135 (n=176)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2721
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=343)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.230 (n=120)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=392)

- **FILTRO** `ballena_activa_n` > `78.0` → IC=-0.167 (n=127)

  - _Acción_: SKIP cuando `ballena_activa_n` > 78.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=385)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.185 (n=198)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=263)

- **FILTRO** `ibs_20min` < `0.7273` → IC=-0.209 (n=115)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=346)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.197 (n=173)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=337)

- **FILTRO** `ibs_20min` > `0.7608` → IC=-0.205 (n=127)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7608
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=383)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.133 (n=137)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=414)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.183 (n=143)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=396)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.136 (n=182)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=357)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.230 (n=113)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=365)

- **FILTRO** `ibs_20min` > `0.2778` → IC=-0.181 (n=117)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=361)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.139 (n=214)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=264)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.214 (n=124)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=384)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=493)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.273 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=322)

- **FILTRO** `ibs_20min` > `0.2861` → IC=-0.250 (n=118)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2861
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=356)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=374)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=380)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2063.3848` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 2063.3848
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `drift_20min_pct` |x|> `0.1906` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1906
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=58)

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
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.033)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=630)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=2175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=5315)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.287 (n=1810)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5680)

- **FILTRO** `ibs_7min` < `0.7355` → IC=-0.234 (n=1872)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7355
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=5618)

- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.176 (n=2489)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=5001)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.229 (n=2125)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7089)

- **FILTRO** `ibs_7min` > `0.7213` → IC=-0.169 (n=2303)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7213
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=6911)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.161 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=782)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.331 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=773)

- **FILTRO** `ibs_7min` < `0.9818` → IC=-0.203 (n=671)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9818
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=348)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.265 (n=253)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=766)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.232 (n=375)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1189)

- **FILTRO** `drift_7min_pct` |x|> `0.1398` → IC=-0.159 (n=531)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1398
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1033)

- **FILTRO** `ibs_7min` > `0.8364` → IC=-0.196 (n=390)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8364
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1174)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.156 (n=318)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1179)

- **FILTRO** `py_entrada` < `0.38` → IC=-0.243 (n=364)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1133)

- **FILTRO** `ibs_7min` < `0.8058` → IC=-0.162 (n=374)

  - _Acción_: SKIP cuando `ibs_7min` < 0.8058
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1123)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.169 (n=373)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1124)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.231 (n=362)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1169)

- **FILTRO** `ballena_activa_n` > `124.0` → IC=-0.170 (n=380)

  - _Acción_: SKIP cuando `ballena_activa_n` > 124.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=1151)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.193 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=790)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.339 (n=247)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=805)

- **FILTRO** `ibs_7min` < `0.2125` → IC=-0.281 (n=263)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2125
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=789)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.286 (n=260)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=792)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=348)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=1266)

- **FILTRO** `ibs_7min` > `0.8182` → IC=-0.181 (n=403)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8182
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1211)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.150 (n=389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=891)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.267 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=981)

- **FILTRO** `ibs_7min` < `0.765` → IC=-0.186 (n=320)

  - _Acción_: SKIP cuando `ibs_7min` < 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=960)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.212 (n=318)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=962)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.126 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=858)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.286 (n=306)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=962)

- **FILTRO** `ibs_7min` > `0.1818` → IC=-0.158 (n=428)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1818
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=840)

- **FILTRO** `ballena_activa_n` > `38.0` → IC=-0.205 (n=313)

  - _Acción_: SKIP cuando `ballena_activa_n` > 38.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=955)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.233 (n=335)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1073)

- **FILTRO** `ibs_7min` < `0.7714` → IC=-0.200 (n=351)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7714
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1057)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.205 (n=344)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1064)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.172 (n=422)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1270)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.296 (n=297)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=937)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.242 (n=296)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=938)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.243 (n=306)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=928)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.274 (n=308)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=1237)

- **FILTRO** `ibs_7min` > `0.83` → IC=-0.160 (n=386)

  - _Acción_: SKIP cuando `ibs_7min` > 0.83
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=1159)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=149)

- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=412)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=248)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=435)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.45` → IC=+0.196 (n=90)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio` |x|> 0.45 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.123 (n=213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 18.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.218 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 422.506 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=117)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3593.2243` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3593.2243 (IC base=+0.127)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4421` → IC=+0.136 (n=20)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.4421 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `600.958` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 600.958 (IC base=+0.130)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `3221.1629` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3221.1629 (IC base=+0.125)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4028` → IC=+0.134 (n=39)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.4028 (IC base=+0.076)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.076)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `3436.4906` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3436.4906 (IC base=+0.076)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0147` → IC=-0.141 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0147
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.317 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=82)

- **FILTRO** `T_h` > `111.9853` → IC=-0.373 (n=61)

  - _Acción_: SKIP cuando `T_h` > 111.9853
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `98.7549` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=-0.172)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.128 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=50)

- **FILTRO** `T_h` > `143.1632` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=69)

- **FILTRO** `T_h` < `111.9668` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `T_h` < 111.9668
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=52)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3968` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3968 (IC base=-0.025)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.005` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` > `87.9947` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `T_h` > 87.9947
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `8.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `streak_estiramiento` > `0.359` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.359
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `py_entrada` < `0.49` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=76)

- **FILTRO** `streak_estiramiento` > `0.437` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.437
  - _Potencial_: sin este filtro IC_bueno=+0.409 (n=9)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 44.0 (IC base=+0.027)

### STREAK_FADE_5M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=187)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=87)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=96)

- **FILTRO** `streak_estiramiento` > `0.6136` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6136
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=97)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=125)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=265)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.133 (n=137)

  - _Acción_: Kelly boost +0.67€ cuando `streak_len` < 3.0 (IC base=+0.060)

- **PATRÓN** `streak_estiramiento` < `0.5593` → IC=+0.121 (n=56)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.5593 (IC base=+0.003)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=142)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=197)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.133 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.075)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1134)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=652)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=660)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.148 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0029 (IC base=+0.111)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.123 (n=377)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.61€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.111)

- **PATRÓN** `ibs_15` > `0.5217` → IC=+0.199 (n=377)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5217 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.763` → IC=+0.248 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.763 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2964.2504` → IC=+0.140 (n=251)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2964.2504 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 86.0 (IC base=+0.111)

- **PATRÓN** `ibs_15` < `0.1129` → IC=+0.136 (n=413)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` < 0.1129 (IC base=+0.028)

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.2` → IC=-0.220 (n=105)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=318)

- **FILTRO** `sigma_ewma_delta_pct` > `6.729` → IC=-0.198 (n=51)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.729
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=372)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0397` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0397
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=41)

- **FILTRO** `sigma_h` < `0.0059` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

- **FILTRO** `ibs_15` < `0.1983` → IC=-0.265 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1983
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.7305` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.7305
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **FILTRO** `dist_vwap_pct` < `0.4006` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.4006
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=51)

- **FILTRO** `libro_liquidez` < `13834.2565` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 13834.2565
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=51)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.163 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0035 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1957` → IC=+0.157 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1957 (IC base=+0.141)

- **PATRÓN** `drift_15min` |x|≤ `0.4671` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `drift_15min` |x|≤ 0.4671 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.262` → IC=+0.203 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.262 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 4.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.8714` → IC=+0.250 (n=70)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8714 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.5371` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.5371 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `12240.9476` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 12240.9476 (IC base=+0.141)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0179` → IC=-0.177 (n=29)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0179
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.167 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=22)

- **FILTRO** `ibs_15` < `0.2361` → IC=-0.208 (n=22)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2361
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

- **FILTRO** `dist_vwap_pct` < `0.372` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.372
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=75)

- **FILTRO** `ibs_15` < `0.6426` → IC=-0.250 (n=22)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6426
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=68)

- **PATRÓN** `ibs_15` > `0.9253` → IC=+0.136 (n=31)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` > 0.9253 (IC base=-0.014)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.617` → IC=-0.237 (n=36)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.617
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=74)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.127 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0044 (IC base=+0.080)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1911` → IC=+0.200 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1911 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.237 (n=74)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.0929 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.080)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.130 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0052 (IC base=+0.017)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=57)

- **FILTRO** `dist_vwap_pct` > `0.1635` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1635
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=67)

- **FILTRO** `libro_liquidez` < `6390.4813` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 6390.4813
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `drift_15min` |x|> `0.559` → IC=-0.163 (n=96)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.559
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=290)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.021)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=32)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.265 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.477` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.477 (IC base=+0.056)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `ibs_15` < `0.1667` → IC=-0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `dist_vwap_pct` < `0.116` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.116
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `sigma_ewma_delta_pct` < `2.724` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.724
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0128` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0128
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=37)

- **FILTRO** `ibs_15` < `0.6` → IC=-0.182 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **PATRÓN** `dist_vwap_pct` < `0.4088` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.4088 (IC base=-0.026)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.185 (n=90)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` > 0.55 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.4747` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4747 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.569` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.569 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.093)

- **PATRÓN** `ibs_15` < `0.125` → IC=+0.205 (n=103)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.125 (IC base=+0.047)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.0615` → IC=+0.354 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0615 (IC base=+0.302)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1559` → IC=+0.315 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1559 (IC base=+0.302)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4171` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4171 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.316 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.302)

- **PATRÓN** `ibs_15` > `0.8055` → IC=+0.362 (n=121)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8055 (IC base=+0.302)

- **PATRÓN** `dist_vwap_pct` > `0.447` → IC=+0.378 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.447 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.631` → IC=+0.331 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.631 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `6339.6393` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6339.6393 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `540.0` → IC=+0.377 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 540.0 (IC base=+0.302)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1421` → IC=+0.306 (n=34)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1421 (IC base=+0.271)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.306 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.1567` → IC=+0.300 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1567 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `0.4366` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4366 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.271)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.275 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.271)

- **PATRÓN** `ibs_15` > `0.8246` → IC=+0.319 (n=70)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8246 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.4311` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4311 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.871` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.871 (IC base=+0.271)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.397 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.0534` → IC=+0.409 (n=20)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0534 (IC base=+0.335)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.402 (n=39)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.344 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.335)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.339 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.335)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.426 (n=52)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` > `0.1297` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1297 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.86` → IC=+0.397 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.86 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `3128.4304` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3128.4304 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 198.0 (IC base=+0.335)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0092` → IC=-0.141 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0092
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=712)

- **FILTRO** `ibs_15` < `0.4486` → IC=-0.276 (n=96)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4486
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=289)

- **FILTRO** `sigma_ewma_delta_pct` > `17.235` → IC=-0.179 (n=325)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.235
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=2334)

- **PATRÓN** `ibs_15` > `0.4486` → IC=+0.156 (n=289)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` > 0.4486 (IC base=-0.054)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1216` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1216 (IC base=-0.082)

- **PATRÓN** `ibs_15` < `0.3315` → IC=+0.345 (n=114)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3315 (IC base=-0.082)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.266 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0929 (IC base=-0.082)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=-0.082)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.231 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=389)

- **FILTRO** `sigma_h` < `0.0027` → IC=-0.211 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0027
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=441)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.250 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=446)

- **FILTRO** `sigma_ewma_delta_pct` > `19.716` → IC=-0.259 (n=110)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.716
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=478)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.123 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0028 (IC base=+0.016)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4476` → IC=-0.360 (n=41)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4476
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=123)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=147)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.182 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.036)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3269` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3269 (IC base=+0.036)

- **PATRÓN** `ibs_15` > `0.4476` → IC=+0.172 (n=123)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` > 0.4476 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.6956` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.6956 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `10832.9607` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10832.9607 (IC base=+0.036)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.233 (n=73)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.315 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `0.4277` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4277 (IC base=+0.237)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1117` → IC=+0.246 (n=65)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1117 (IC base=+0.237)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2552` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2552 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.296 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.250 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.237)

- **PATRÓN** `ibs_15` < `0.3357` → IC=+0.340 (n=73)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3357 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` < `0.1085` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1085 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.609` → IC=+0.266 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.609 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `13114.1262` → IC=+0.352 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13114.1262 (IC base=+0.237)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.751` → IC=-0.172 (n=56)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.751
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=172)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=208)

- **FILTRO** `sigma_ewma_delta_pct` > `8.896` → IC=-0.138 (n=208)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.896
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=709)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.096)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.188 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=81)

- **FILTRO** `sigma_ewma_delta_pct` > `14.4` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.4
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=205)

- **FILTRO** `libro_liquidez` < `2584.1244` → IC=-0.183 (n=77)

  - _Acción_: SKIP cuando `libro_liquidez` < 2584.1244
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=159)

- **FILTRO** `sigma_ewma_delta_pct` > `9.247` → IC=-0.135 (n=190)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.247
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=661)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.277 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.302 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.313 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.271)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1908` → IC=+0.322 (n=99)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1908 (IC base=+0.271)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.319 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.304 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.271)

- **PATRÓN** `ibs_15` > `0.8604` → IC=+0.312 (n=195)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8604 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.2982` → IC=+0.349 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2982 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.523` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.523 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.463` → IC=+0.270 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.463 (IC base=+0.271)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.270 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `12007.5914` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12007.5914 (IC base=+0.271)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.254 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.314 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.253)

- **PATRÓN** `drift_60min` |x|≤ `0.1871` → IC=+0.278 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1871 (IC base=+0.253)

- **PATRÓN** `drift_15min` |x|≤ `0.6649` → IC=+0.266 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6649 (IC base=+0.253)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2087` → IC=+0.293 (n=56)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2087 (IC base=+0.253)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4151` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4151 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.283 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.253)

- **PATRÓN** `ibs_15` > `0.9661` → IC=+0.310 (n=56)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9661 (IC base=+0.253)

- **PATRÓN** `dist_vwap_pct` > `0.3017` → IC=+0.345 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3017 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.523` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.523 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.438` → IC=+0.255 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.438 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `11800.2375` → IC=+0.293 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11800.2375 (IC base=+0.253)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.303 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.304 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0603` → IC=+0.318 (n=42)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0603 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.370 (n=44)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.346 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.366 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8607` → IC=+0.341 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8607 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.952` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.952 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.291)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1065` → IC=-0.220 (n=23)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1065
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1222` → IC=-0.181 (n=92)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1222
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=278)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.160 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=278)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1801` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1801
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=47)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2312` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2312
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.167 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9965` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9965 (IC base=+0.081)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.081)

- **PATRÓN** `T_h` > `146.1038` → IC=+0.441 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.341)

- **PATRÓN** `ratio` < `1.0177` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0177 (IC base=+0.341)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `ratio` > 1.0126 (IC base=+0.341)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.996` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.996 (IC base=+0.259)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.259)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `145.7785` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7785 (IC base=+0.300)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.417)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5217 sube el IC de +0.111 a +0.199 en UPDOWN_GBM#15min (n=377). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8714 sube el IC de +0.141 a +0.250 en UPDOWN_GBM#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.080 a +0.237 en UPDOWN_GBM#ETH#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.093 a +0.185 en UPDOWN_GBM#XRP#15min (n=90). Ya aplicado como kelly_boost=+0.92€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.125 sube el IC de +0.047 a +0.205 en UPDOWN_GBM#XRP#15min (n=103). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.4486 sube el IC de -0.054 a +0.156 en UPDOWN_GBM_15M_TARDIO (n=289). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3315 sube el IC de -0.082 a +0.345 en UPDOWN_GBM_15M_TARDIO (n=114). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4476 sube el IC de +0.036 a +0.172 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=123). Ya aplicado como kelly_boost=+0.86€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3357 sube el IC de +0.237 a +0.340 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=73). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.096 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8604 sube el IC de +0.271 a +0.312 en UPDOWN_GBM_IBS_ALTO (n=195). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9661 sube el IC de +0.253 a +0.310 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8607 sube el IC de +0.291 a +0.341 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=86). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8055 sube el IC de +0.302 a +0.362 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=121). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8246 sube el IC de +0.271 a +0.319 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.335 a +0.426 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#ETH#5min` — IC=+0.176 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#ETH` — IC=+0.176 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 591 | +0.085 | +45.74€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 591 | +0.085 | +45.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 347 | +0.110 | +34.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 347 | +0.110 | +34.74€ | 0 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.030 | +0.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.030 | +0.07€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 6514 | -0.099 | -890.55€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 669 | -0.089 | -118.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 5845 | -0.100 | -772.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1076 | +0.018 | -124.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1076 | +0.018 | -124.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 669 | -0.089 | -118.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 669 | -0.089 | -118.30€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 359 | -0.137 | -154.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 359 | -0.137 | -154.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2134 | -0.073 | -103.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2134 | -0.073 | -103.08€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1551 | -0.192 | -351.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1551 | -0.192 | -351.70€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 30323 | +0.114 | -1978.03€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 5666 | +0.187 | -193.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 107 | -0.105 | -50.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 21417 | +0.095 | -1695.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3133 | +0.121 | -38.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 3595 | +0.063 | -616.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 20 | -0.045 | +2.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 3570 | +0.064 | -612.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 6292 | +0.134 | -131.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1597 | +0.197 | -85.93€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 3563 | +0.110 | -77.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1090 | +0.129 | +54.62€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 3604 | +0.078 | -471.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 20 | +0.045 | +2.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 3583 | +0.079 | -472.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 6755 | +0.129 | -79.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2061 | +0.169 | -10.76€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3566 | +0.114 | -40.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1116 | +0.104 | -19.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 6484 | +0.132 | -425.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1951 | +0.202 | -101.49€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 46 | +0.000 | -9.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3560 | +0.095 | -240.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 927 | +0.132 | -73.91€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 3593 | +0.105 | -254.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 3575 | +0.105 | -252.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 5631 | +0.173 | -439.13€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 5631 | +0.173 | -439.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1416 | +0.167 | -150.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1416 | +0.167 | -150.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 111 | -0.119 | +2.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 111 | -0.119 | +2.57€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1405 | +0.160 | -168.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1405 | +0.160 | -168.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1261 | +0.231 | -34.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1261 | +0.231 | -34.61€ | 0 | 2 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1359 | +0.185 | -102.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1359 | +0.185 | -102.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 284 | +0.444 | +2.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 284 | +0.444 | +2.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 109 | +0.446 | +2.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 109 | +0.446 | +2.47€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 106 | +0.426 | -1.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 106 | +0.426 | -1.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 66 | +0.441 | +1.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 66 | +0.441 | +1.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 15312 | +0.191 | -1354.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 15312 | +0.191 | -1354.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 2813 | +0.124 | -521.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 2813 | +0.124 | -521.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2376 | +0.238 | -44.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2376 | +0.238 | -44.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2642 | +0.161 | -345.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2642 | +0.161 | -345.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2427 | +0.231 | -68.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2427 | +0.231 | -68.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2476 | +0.217 | -118.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2476 | +0.217 | -118.12€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 2578 | +0.184 | -255.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 2578 | +0.184 | -255.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 5542 | +0.134 | +190.48€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 5542 | +0.134 | +190.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 2753 | +0.141 | +133.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 2753 | +0.141 | +133.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 2789 | +0.126 | +56.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 2789 | +0.126 | +56.85€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 746 | +0.301 | +9.51€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 746 | +0.301 | +9.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 320 | +0.280 | -7.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 320 | +0.280 | -7.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 350 | +0.304 | +11.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 350 | +0.304 | +11.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 76 | +0.359 | +5.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 76 | +0.359 | +5.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 315 | +0.412 | -15.12€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 315 | +0.412 | -15.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 141 | +0.409 | -7.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 141 | +0.409 | -7.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 143 | +0.417 | -6.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 143 | +0.417 | -6.42€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 210 | +0.094 | -2.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 64 | +0.106 | +0.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 146 | +0.088 | -3.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 6 | +0.075 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 6 | +0.075 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 172 | +0.098 | -0.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 26 | +0.143 | +2.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 146 | +0.088 | -3.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 32 | +0.029 | -4.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 32 | +0.029 | -4.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 5603 | +0.096 | -209.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 578 | +0.057 | -30.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 5025 | +0.100 | -179.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 3872 | +0.096 | -99.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 578 | +0.057 | -30.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 3294 | +0.102 | -68.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 1731 | +0.096 | -110.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 1731 | +0.096 | -110.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 411 | +0.282 | -28.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 411 | +0.282 | -28.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 411 | +0.282 | -28.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 411 | +0.282 | -28.59€ | 0 | 4 |
| ✅ GBM_LATE_15M | 7234 | +0.044 | +2299.70€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 7234 | +0.044 | +2299.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 958 | +0.173 | +601.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 958 | +0.173 | +601.17€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 1010 | +0.175 | +593.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1010 | +0.175 | +593.96€ | 0 | 31 |
| ✅ GBM_LATE_15M#DOGE | 961 | +0.183 | +636.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 961 | +0.183 | +636.27€ | 0 | 18 |
| ✅ GBM_LATE_15M#ETH | 1178 | -0.047 | +32.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1178 | -0.047 | +32.04€ | 2 | 11 |
| ✅ GBM_LATE_15M#SOL | 1363 | -0.042 | +142.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1363 | -0.042 | +142.07€ | 4 | 3 |
| ✅ GBM_LATE_15M#XRP | 1764 | -0.051 | +294.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1764 | -0.051 | +294.19€ | 4 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 8200 | +0.045 | +3179.36€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 8200 | +0.045 | +3179.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1243 | -0.023 | +624.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1243 | -0.023 | +624.15€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1798 | -0.036 | +167.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1798 | -0.036 | +167.61€ | 0 | 1 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 831 | +0.235 | +742.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 831 | +0.235 | +742.63€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1392 | -0.044 | +6.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1392 | -0.044 | +6.25€ | 8 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1481 | -0.018 | +290.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1481 | -0.018 | +290.43€ | 4 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1455 | +0.241 | +1348.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1455 | +0.241 | +1348.29€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 5847 | +0.170 | +4016.59€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 5847 | +0.170 | +4016.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 731 | +0.190 | +529.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 731 | +0.190 | +529.95€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 993 | +0.166 | +681.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 993 | +0.166 | +681.90€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 723 | +0.199 | +553.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 723 | +0.199 | +553.92€ | 0 | 15 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 972 | +0.162 | +626.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 972 | +0.162 | +626.78€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1130 | +0.121 | +653.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1130 | +0.121 | +653.76€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1298 | +0.191 | +970.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1298 | +0.191 | +970.29€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 991 | +0.077 | +186.82€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 991 | +0.077 | +186.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 291 | +0.118 | +102.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 291 | +0.118 | +102.96€ | 3 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 200 | +0.183 | +61.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 200 | +0.183 | +61.07€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 295 | -0.029 | -5.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 295 | -0.029 | -5.55€ | 4 | 3 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO | 6805 | +0.168 | +4491.59€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#15min | 6805 | +0.168 | +4491.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 917 | +0.189 | +653.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 917 | +0.189 | +653.93€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1111 | +0.163 | +702.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1111 | +0.163 | +702.72€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 906 | +0.218 | +751.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 906 | +0.218 | +751.86€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1036 | +0.146 | +593.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1036 | +0.146 | +593.30€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1237 | +0.106 | +611.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1237 | +0.106 | +611.53€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1598 | +0.193 | +1178.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1598 | +0.193 | +1178.26€ | 0 | 23 |
| ✅ GBM_LATE_5M | 1447 | +0.129 | +665.58€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 1447 | +0.129 | +665.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 62 | +0.203 | +39.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 62 | +0.203 | +39.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 565 | +0.128 | +295.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 565 | +0.128 | +295.94€ | 1 | 20 |
| ✅ GBM_LATE_5M#DOGE | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 548 | +0.145 | +252.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 548 | +0.145 | +252.03€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 114 | -0.017 | +2.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 114 | -0.017 | +2.12€ | 2 | 1 |
| ✅ GBM_LATE_5M#XRP | 145 | +0.180 | +80.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 145 | +0.180 | +80.43€ | 0 | 0 |
| ✅ GBM_LATE_60M | 511 | -0.042 | +83.01€ | 5 | 7 |
| ✅ GBM_LATE_60M#60min | 511 | -0.042 | +83.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 175 | -0.003 | +4.17€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 175 | -0.003 | +4.17€ | 2 | 4 |
| ✅ GBM_LATE_60M#ETH | 184 | -0.011 | +56.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 184 | -0.011 | +56.06€ | 4 | 7 |
| ✅ GBM_LATE_60M#SOL | 152 | -0.123 | +22.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 152 | -0.123 | +22.77€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE | 193 | -0.305 | -34.48€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 193 | -0.305 | -34.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 12 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 52 | -0.296 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 52 | -0.296 | -8.07€ | 10 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 324 | +0.037 | +2.43€ | 2 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 324 | +0.037 | +2.43€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 125 | +0.020 | +4.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 125 | +0.020 | +4.84€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 82 | +0.071 | +2.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 82 | +0.071 | +2.06€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 117 | +0.029 | -4.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 117 | +0.029 | -4.47€ | 2 | 5 |
| ✅ LATE_WINDOW_5MIN | 10 | +0.167 | +4.09€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 10 | +0.167 | +4.09€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 10 | +0.167 | +4.09€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 10 | +0.167 | +4.09€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 292 | +0.119 | +90.14€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 292 | +0.119 | +90.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 292 | +0.119 | +90.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 292 | +0.119 | +90.14€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 216 | -0.110 | -29.46€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 216 | -0.110 | -29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 55 | -0.132 | -9.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 55 | -0.132 | -9.15€ | 2 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 44 | -0.043 | -3.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 584 | -0.058 | -41.25€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 584 | -0.058 | -41.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 34 | -0.028 | -2.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 34 | -0.028 | -2.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 97 | -0.066 | -6.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 97 | -0.066 | -6.22€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 67 | -0.094 | -7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 67 | -0.094 | -7.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 159 | -0.028 | -5.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 159 | -0.028 | -5.20€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 178 | -0.039 | -10.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 178 | -0.039 | -10.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 49 | -0.167 | -9.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 49 | -0.167 | -9.12€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 422 | -0.009 | -5.07€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 422 | -0.009 | -5.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 133 | -0.033 | -9.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 133 | -0.033 | -9.78€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 134 | -0.007 | -0.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 134 | -0.007 | -0.05€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 155 | +0.010 | +4.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 155 | +0.010 | +4.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 4181 | -0.001 | -65.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 4181 | -0.001 | -65.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 464 | +0.000 | +5.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 464 | +0.000 | +5.06€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 709 | -0.001 | -20.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 709 | -0.001 | -20.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 826 | +0.013 | +17.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 826 | +0.013 | +17.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 747 | -0.011 | -30.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 747 | -0.011 | -30.86€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 837 | -0.013 | -28.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 837 | -0.013 | -28.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 6085 | -0.035 | +187.25€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 6085 | -0.035 | +187.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 966 | -0.024 | +136.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 966 | -0.024 | +136.71€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1093 | -0.033 | -26.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1093 | -0.033 | -26.67€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 971 | -0.045 | +90.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 971 | -0.045 | +90.46€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1090 | -0.034 | -30.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1090 | -0.034 | -30.85€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 983 | -0.043 | +28.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 983 | -0.043 | +28.29€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 982 | -0.034 | -10.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 982 | -0.034 | -10.71€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 554 | -0.059 | -41.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 554 | -0.059 | -41.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 66 | -0.059 | -4.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 66 | -0.059 | -4.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 35 | -0.095 | -3.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 35 | -0.095 | -3.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3159 | +0.003 | -7.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3159 | +0.003 | -7.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1149 | +0.006 | +5.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1149 | +0.006 | +5.23€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 16704 | -0.074 | +250.67€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 16704 | -0.074 | +250.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 2583 | -0.093 | +263.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 2583 | -0.093 | +263.89€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 3028 | -0.059 | -4.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 3028 | -0.059 | -4.09€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 2666 | -0.086 | +19.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 2666 | -0.086 | +19.10€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 2548 | -0.095 | -171.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 2548 | -0.095 | -171.15€ | 8 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 3100 | -0.048 | +22.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 3100 | -0.048 | +22.40€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 2779 | -0.069 | +120.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 2779 | -0.069 | +120.53€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6011 | -0.010 | -119.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6011 | -0.010 | -119.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1204 | +0.000 | -15.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1204 | +0.000 | -15.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1000 | -0.019 | -29.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1000 | -0.019 | -29.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 398 | +0.098 | +99.21€ | 1 | 6 |
| ✅ ORDER_FLOW_5M#5min | 262 | +0.117 | +86.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 79 | +0.130 | +35.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 79 | +0.130 | +35.70€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 45 | +0.074 | +6.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 45 | +0.074 | +6.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 35 | +0.176 | +19.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 35 | +0.176 | +19.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 46 | +0.125 | +14.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 46 | +0.125 | +14.98€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 57 | +0.076 | +9.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 57 | +0.076 | +9.50€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 256 | -0.163 | -20.27€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 114 | -0.233 | -32.63€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 99 | -0.262 | -31.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 97 | -0.146 | -3.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 78 | -0.163 | -6.13€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 45 | -0.011 | +15.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 38 | +0.000 | +14.95€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 215 | -0.182 | -23.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 176 | -0.163 | +30.67€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 76 | -0.077 | +22.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 74 | -0.066 | +23.10€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 68 | -0.243 | -5.68€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 64 | -0.242 | -7.07€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 32 | -0.176 | +14.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 30 | -0.156 | +16.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 168 | -0.153 | +32.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 54 | +0.268 | +9.77€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 22 | +0.458 | +11.45€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 22 | +0.458 | +11.45€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 54 | +0.268 | +9.77€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 133 | -0.018 | -10.81€ | 4 | 1 |
| ✅ STREAK_FADE_15M#15min | 133 | -0.018 | -10.81€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 54 | -0.018 | -6.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 54 | -0.018 | -6.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 12 | +0.086 | +2.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 12 | +0.086 | +2.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 58 | -0.050 | -6.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 58 | -0.050 | -6.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1024 | -0.016 | -43.27€ | 1 | 0 |
| ✅ STREAK_FADE_5M#5min | 1024 | -0.016 | -43.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 355 | -0.013 | -10.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 355 | -0.013 | -10.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 342 | +0.009 | -4.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 342 | +0.009 | -4.65€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 132 | -0.037 | -12.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 132 | -0.037 | -12.47€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 195 | -0.048 | -15.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 195 | -0.048 | -15.79€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 1987 | +0.026 | +36.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 1987 | +0.026 | +36.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 662 | +0.027 | +8.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 662 | +0.027 | +8.87€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 356 | +0.008 | +0.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 356 | +0.008 | +0.23€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 588 | +0.030 | +9.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 588 | +0.030 | +9.20€ | 1 | 2 |
| ✅ STREAK_MOM_5M#XRP | 381 | +0.035 | +18.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 381 | +0.035 | +18.22€ | 2 | 1 |
| ✅ STRUCT_NO_15M | 2997 | +0.007 | -29.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 2997 | +0.007 | -29.61€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1153 | +0.007 | -12.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1153 | +0.007 | -12.69€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1160 | +0.014 | -4.30€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1160 | +0.014 | -4.30€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 684 | -0.003 | -12.62€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 684 | -0.003 | -12.62€ | 2 | 0 |
| ✅ UPDOWN_GBM | 5693 | +0.007 | +148.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2151 | +0.047 | +216.21€ | 0 | 8 |
| ✅ UPDOWN_GBM#240min | 241 | +0.031 | +7.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 2895 | -0.019 | -64.95€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 359 | -0.018 | -9.77€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 193 | +0.095 | +37.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 178 | +0.117 | +40.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 6 | +0.000 | +0.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1239 | +0.016 | +56.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 216 | +0.069 | +27.58€ | 3 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 71 | +0.089 | +9.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 817 | +0.008 | +25.86€ | 4 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 117 | -0.046 | -7.65€ | 2 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 723 | -0.009 | -2.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 120 | +0.107 | +29.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 8 | +0.000 | -0.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 595 | -0.033 | -31.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1308 | +0.008 | +13.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 601 | +0.029 | +23.31€ | 1 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 70 | +0.083 | +6.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 468 | -0.023 | -17.10€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 154 | +0.013 | +1.72€ | 0 | 1 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1379 | -0.007 | -16.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 494 | +0.006 | -0.90€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 56 | -0.017 | -3.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 729 | -0.007 | -8.64€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 88 | -0.033 | -3.84€ | 2 | 1 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 849 | +0.006 | +60.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 542 | +0.059 | +96.18€ | 0 | 6 |
| ✅ UPDOWN_GBM#XRP#240min | 30 | -0.125 | -4.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 277 | -0.081 | -30.62€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 180 | +0.302 | +27.53€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 180 | +0.302 | +27.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 103 | +0.271 | +4.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 103 | +0.271 | +4.07€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 77 | +0.335 | +23.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 77 | +0.335 | +23.46€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3606 | -0.075 | +811.13€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3606 | -0.075 | +811.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 297 | -0.049 | +342.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 297 | -0.049 | +342.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 741 | -0.162 | -80.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 741 | -0.162 | -80.97€ | 4 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 75 | +0.058 | +11.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 75 | +0.058 | +11.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 261 | +0.112 | +109.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 261 | +0.112 | +109.27€ | 2 | 16 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1145 | -0.067 | +221.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1145 | -0.067 | +221.60€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1087 | -0.085 | +207.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1087 | -0.085 | +207.04€ | 4 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 28 | +0.000 | -0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 28 | +0.000 | -0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 28 | +0.000 | -0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 28 | +0.000 | -0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 291 | +0.271 | +207.56€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 291 | +0.271 | +207.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 164 | +0.253 | +102.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 164 | +0.253 | +102.44€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 127 | +0.291 | +105.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 127 | +0.291 | +105.12€ | 0 | 12 |
| ✅ UPDOWN_OU_5M | 418 | -0.076 | -38.67€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 418 | -0.076 | -38.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 252 | -0.032 | -18.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 252 | -0.032 | -18.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 42 | +0.000 | +2.47€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 42 | +0.000 | +2.47€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 28 | -0.200 | -6.19€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 28 | -0.200 | -6.19€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 31 | -0.167 | -4.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 31 | -0.167 | -4.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 36 | -0.184 | -5.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 36 | -0.184 | -5.77€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1057 | +0.286 | +427.80€ | 0 | 5 |
| ✅ WEEKLY_PRICE#BTC | 314 | +0.199 | -2.94€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 329 | +0.255 | +70.48€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 414 | +0.373 | +360.27€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.088) — sin ventaja clara. oversold(IBS<0.3): IC=+0.007 n=1996 | neutral: IC=+0.001 n=2136 | overbought(IBS>0.7): IC=+0.089 n=2229
  - _Datos_: n=6666 IC=+0.034 PNL=+553.29€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 383s) 16 celda(s) GATE OK de 2011 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.006 < 0.08 — monitorear
  - _Datos_: n=494 IC=+0.006 PNL=-0.90€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=329/15 IC=+0.255 PNL=+70.48€ | BTC: n=314/15 IC=+0.199 PNL=-2.94€ | SOL: n=414/15 IC=+0.373 PNL=+360.27€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.076 n=91065 | tras_1loss IC=+0.045 n=70905 | tras_2loss IC=+0.009 n=32204/40 | gap=+0.067 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 19 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
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
  - _Estado_: 5631 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.128 n=41/60 | contraria IC=-0.022 n=21 | gap=+0.150 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=57, boost estimado=+0.025. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 46/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=154/40 IC=+0.013 PNL=+1.72€ | BTC#60min: n=117/40 IC=-0.046 PNL=-7.65€ | SOL#60min: n=88/40 IC=-0.033 PNL=-3.84€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.009 n=593 | contrario_BTC IC=-0.006 n=443/40 | gap=+0.004 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=73 PNL=+42.34€
  - _Datos_: n=73 IC=+0.180 PNL=+42.34€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.08 con n=92 PNL=+22.62€
  - _Datos_: n=92 IC=+0.128 PNL=+22.62€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 11/25 ops en el filtro definido (IC actual=+0.190 PNL=+11.09€)
  - _Datos_: n=11 IC=+0.190 PNL=+11.09€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.1 con n=899 PNL=+432.52€
  - _Datos_: n=899 IC=+0.331 PNL=+432.52€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=51 IC=+0.047 PNL=+11.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=51 IC=+0.047 PNL=+11.33€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 15/30 ops en el filtro definido (IC actual=+0.110 PNL=+5.52€)
  - _Datos_: n=15 IC=+0.110 PNL=+5.52€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=5452 IC=+0.003 PNL=+97.48€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=5452 IC=+0.003 PNL=+97.48€

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
  - _Estado_: n=298 IC=+0.000 PNL=-2.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=298 IC=+0.000 PNL=-2.39€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=61 IC=-0.103 PNL=-7.38€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=61 IC=-0.103 PNL=-7.38€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.098 < -0.08 con n=95 PNL=-9.23€
  - _Datos_: n=95 IC=-0.098 PNL=-9.23€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.1 con n=502 PNL=+108.03€
  - _Datos_: n=502 IC=+0.111 PNL=+108.03€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=169 IC=+0.085 PNL=+40.94€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=169 IC=+0.085 PNL=+40.94€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=216 IC=+0.069 PNL=+27.58€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=216 IC=+0.069 PNL=+27.58€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=1245 IC=+0.033 PNL=+81.63€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1245 IC=+0.033 PNL=+81.63€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 19/30 ops en el filtro definido (IC actual=-0.158 PNL=-2.48€)
  - _Datos_: n=19 IC=-0.158 PNL=-2.48€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=71 IC=-0.007 PNL=+9.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=71 IC=-0.007 PNL=+9.84€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=80 IC=+0.024 PNL=+5.36€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=80 IC=+0.024 PNL=+5.36€

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
  - _Estado_: n=2043 IC=-0.014 PNL=-41.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2043 IC=-0.014 PNL=-41.12€

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
  - _Estado_: 10/30 ops en el filtro definido (IC actual=+0.167 PNL=+4.09€)
  - _Datos_: n=10 IC=+0.167 PNL=+4.09€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1530 IC=+0.028 PNL=+102.57€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1530 IC=+0.028 PNL=+102.57€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=425 IC=+0.029 PNL=-2.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=425 IC=+0.029 PNL=-2.62€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=84 PNL=+19.17€
  - _Datos_: n=84 IC=+0.105 PNL=+19.17€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.164 > 0.08 con n=108 PNL=+3.02€
  - _Datos_: n=108 IC=+0.164 PNL=+3.02€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=112 PNL=+30.12€
  - _Datos_: n=112 IC=+0.105 PNL=+30.12€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=6761 IC=+0.096 PNL=+1839.86€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=6761 IC=+0.096 PNL=+1839.86€

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
  - _Estado_: n=774 IC=+0.025 PNL=+42.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=774 IC=+0.025 PNL=+42.87€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=205 PNL=+60.85€
  - _Datos_: n=205 IC=+0.128 PNL=+60.85€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=94 IC=-0.094 PNL=+19.83€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=94 IC=-0.094 PNL=+19.83€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.440 > 0.1 con n=579 PNL=+478.10€
  - _Datos_: n=579 IC=+0.440 PNL=+478.10€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1407 IC=+0.021 PNL=+69.60€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1407 IC=+0.021 PNL=+69.60€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.164 > 0.1 con n=751 PNL=+269.25€
  - _Datos_: n=751 IC=+0.164 PNL=+269.25€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 18/40 ops en el filtro definido (IC actual=-0.225 PNL=-3.72€)
  - _Datos_: n=18 IC=-0.225 PNL=-3.72€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=409 IC=+0.047 PNL=+56.86€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=409 IC=+0.047 PNL=+56.86€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=61 IC=+0.040 PNL=-7.01€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=61 IC=+0.040 PNL=-7.01€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=3979 IC=-0.135 PNL=+266.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3979 IC=-0.135 PNL=+266.97€

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
  - _Estado_: n=545 IC=+0.142 PNL=+221.88€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=545 IC=+0.142 PNL=+221.88€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.08 con n=502 PNL=+108.03€
  - _Datos_: n=502 IC=+0.111 PNL=+108.03€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=582 IC=+0.005 PNL=+5.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=582 IC=+0.005 PNL=+5.35€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.099 > 0.08 con n=576 PNL=+339.05€
  - _Datos_: n=576 IC=+0.099 PNL=+339.05€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.08 con n=140 PNL=+33.47€
  - _Datos_: n=140 IC=+0.141 PNL=+33.47€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.237 < -0.1 con n=431 PNL=-49.00€
  - _Datos_: n=431 IC=-0.237 PNL=-49.00€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1030 IC=+0.141 PNL=+537.48€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1030 IC=+0.141 PNL=+537.48€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 23/40 ops en el filtro definido (IC actual=+0.060 PNL=+2.13€)
  - _Datos_: n=23 IC=+0.060 PNL=+2.13€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=608 IC=-0.028 PNL=+36.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=608 IC=-0.028 PNL=+36.26€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=517 PNL=+314.56€
  - _Datos_: n=517 IC=+0.184 PNL=+314.56€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=933 IC=-0.042 PNL=+168.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=933 IC=-0.042 PNL=+168.06€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.114 > 0.08 con n=234 PNL=-32.22€
  - _Datos_: n=234 IC=+0.114 PNL=-32.22€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=1335 PNL=-119.63€
  - _Datos_: n=1335 IC=+0.239 PNL=-119.63€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 9/40 ops en el filtro definido (IC actual=-0.021 PNL=+2.00€)
  - _Datos_: n=9 IC=-0.021 PNL=+2.00€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.126 n=153) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=153 IC=+0.126 PNL=+46.55€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.351 > 0.08 con n=65 PNL=+47.79€
  - _Datos_: n=65 IC=+0.351 PNL=+47.79€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.433 n=223) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=223 IC=+0.433 PNL=+302.61€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=2813 IC=+0.124 PNL=-521.94€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=2813 IC=+0.124 PNL=-521.94€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 39/40 ops en el filtro definido (IC actual=+0.159 PNL=+19.22€)
  - _Datos_: n=39 IC=+0.159 PNL=+19.22€
