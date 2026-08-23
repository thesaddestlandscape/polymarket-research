# Hipótesis automáticas — 2026-08-23 21:33 UTC
_Generado por shadow_postmortem.py sobre 130413 resoluciones (PNL=+9312.82€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.171 (n=86)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=193)

- **FILTRO** `banda_hit_calibrado` < `0.618` → IC=-0.176 (n=69)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.618
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=210)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=215)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.259 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.126)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.138 (n=197)

  - _Acción_: Kelly boost +0.69€ cuando `n_ballena_banda` > 20.0 (IC base=+0.126)

- **PATRÓN** `n_total_lado` > `55.0` → IC=+0.199 (n=144)

  - _Acción_: Kelly boost +0.99€ cuando `n_total_lado` > 55.0 (IC base=+0.126)

- **PATRÓN** `banda_hit_calibrado` > `0.8135` → IC=+0.261 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8135 (IC base=+0.126)

- **PATRÓN** `banda_z` > `9.861` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 9.861 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.128 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 11.0 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=217)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3247.8763` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3247.8763 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.018)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.725` → IC=+0.289 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.159)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `n_ballena_banda` > 26.0 (IC base=+0.159)

- **PATRÓN** `n_total_lado` > `56.0` → IC=+0.210 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 56.0 (IC base=+0.159)

- **PATRÓN** `banda_hit_calibrado` > `0.8197` → IC=+0.280 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8197 (IC base=+0.159)

- **PATRÓN** `banda_z` > `9.932` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `banda_z` > 9.932 (IC base=+0.159)

- **PATRÓN** `ballenas_wallet_edge_medio` > `1.307` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `ballenas_wallet_edge_medio` > 1.307 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.185 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 11.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.159 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3786.4324` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3786.4324 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `287.0` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 287.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.013)

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

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.078)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.078)

- **PATRÓN** `banda_z` > `8.174` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 8.174 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `158.5` → IC=-0.248 (n=1819)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.5
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=5457)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `147.79` → IC=-0.224 (n=197)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.79
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=594)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `n_ballenas` < `5.0` → IC=-0.190 (n=140)

  - _Acción_: SKIP cuando `n_ballenas` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=474)

- **FILTRO** `restante_s_al_confirmar` > `643.37` → IC=-0.190 (n=153)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 643.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=461)

- **FILTRO** `restante_s_al_confirmar` < `360.9` → IC=-0.300 (n=153)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 360.9
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=461)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `110.65` → IC=-0.388 (n=203)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 110.65
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=611)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `170.08` → IC=-0.144 (n=479)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 170.08
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1438)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `150.62` → IC=-0.258 (n=449)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 150.62
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1347)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `147.91` → IC=-0.311 (n=336)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.91
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=1008)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.187 (n=4367)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.7 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=1402)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2371.8003` → IC=+0.172 (n=1347)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2371.8003 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=2820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=3294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.261 (n=2478)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=2591)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `1751.4727` → IC=+0.169 (n=2130)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1751.4727 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.387 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.183 (n=358)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 11.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.283 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=674)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.175)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.6` → IC=+0.176 (n=211)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.6 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `5007.3254` → IC=+0.163 (n=197)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5007.3254 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.199 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.183 (n=279)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.415 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4414.8029` → IC=+0.158 (n=264)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4414.8029 (IC base=+0.139)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=1023)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.134 (n=697)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 12.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.314 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.288 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.281)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.290 (n=383)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.320 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `3447.6628` → IC=+0.305 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3447.6628 (IC base=+0.281)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.250 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=370)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2077.2934` → IC=+0.163 (n=298)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2077.2934 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.162 (n=140)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4420.281 (IC base=+0.086)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.439 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.301 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `793.7358` → IC=+0.230 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 793.7358 (IC base=+0.210)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.263 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.198 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 8.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.350 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.214 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.101)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=80)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=3799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=3266)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.204 (n=1910)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.175 (n=651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 11.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.194 (n=971)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.74 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=49)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=830)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.169 (n=963)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.74 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.172 (n=510)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.73 (IC base=+0.165)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.235 (n=739)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.318 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.234)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=628)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.449 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.447 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `4389.547` → IC=+0.454 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4389.547 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.445 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `10601.0016` → IC=+0.470 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10601.0016 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.435 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.410 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.417)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.425 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.417)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.417)

- **PATRÓN** `libro_liquidez` > `4049.2655` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4049.2655 (IC base=+0.417)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.451 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.932` → IC=+0.427 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.932 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.92` → IC=+0.432 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.92 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.434)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.197 (n=4505)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 8.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.228 (n=6493)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=1699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.141 (n=844)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 8.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.168 (n=1219)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.71 (IC base=+0.126)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.271 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.239)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.163 (n=785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 8.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.207 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.160)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.298 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.237)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.232 (n=706)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.272 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.227)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.198 (n=1109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 12.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.239 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.202 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.129)

- **PATRÓN** `restante_min` < `3.92` → IC=+0.143 (n=1093)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` < 3.92 (IC base=+0.129)

- **PATRÓN** `restante_min` > `4.92` → IC=+0.151 (n=1166)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.92 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.144 (n=2333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 12.0 (IC base=+0.129)

- **PATRÓN** `lag_apertura_s` < `4.57` → IC=+0.148 (n=1093)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 4.57 (IC base=+0.129)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.219 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.141)

- **PATRÓN** `restante_min` < `3.86` → IC=+0.156 (n=545)

  - _Acción_: Kelly boost +0.78€ cuando `restante_min` < 3.86 (IC base=+0.141)

- **PATRÓN** `restante_min` > `4.86` → IC=+0.159 (n=745)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.86 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.164 (n=1154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 12.0 (IC base=+0.141)

- **PATRÓN** `lag_apertura_s` < `6.36` → IC=+0.160 (n=545)

  - _Acción_: Kelly boost +0.80€ cuando `lag_apertura_s` < 6.36 (IC base=+0.141)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.186 (n=593)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.37 (IC base=+0.117)

- **PATRÓN** `restante_min` < `3.98` → IC=+0.136 (n=553)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 3.98 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.151 (n=612)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` > 4.94 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.132 (n=728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.39` → IC=+0.158 (n=550)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 3.39 (IC base=+0.117)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.312 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.309 (n=533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.303)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.392 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.303)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.287 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.283 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.361 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5707.6363` → IC=+0.327 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5707.6363 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.338 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.314 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.303)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.303)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.301 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.303)

- **PATRÓN** `libro_liquidez` > `2542.757` → IC=+0.329 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2542.757 (IC base=+0.303)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.377 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.380)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.423 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.380)

- **PATRÓN** `py_entrada` > `0.88` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.88 (IC base=+0.380)

- **PATRÓN** `libro_liquidez` > `791.5739` → IC=+0.395 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 791.5739 (IC base=+0.380)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.419 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.413)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.427 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.413)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.426 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.413)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.422 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.413)

- **PATRÓN** `libro_liquidez` > `1864.6918` → IC=+0.426 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1864.6918 (IC base=+0.413)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.419 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.414)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.424 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.414)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.422 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.414)

- **PATRÓN** `libro_liquidez` > `5330.8398` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5330.8398 (IC base=+0.414)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.414 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.408)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.433 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.408)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.413 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.408)

- **PATRÓN** `libro_liquidez` > `1933.7222` → IC=+0.444 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1933.7222 (IC base=+0.408)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.87` → IC=+0.436 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.87 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.298 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `1534.561` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1534.561 (IC base=+0.279)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.87` → IC=+0.436 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.87 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.298 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `1534.561` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1534.561 (IC base=+0.279)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9516` → IC=+0.232 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9516 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.2573` → IC=+0.236 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2573 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.6939` → IC=+0.232 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6939 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.992` → IC=+0.197 (n=759)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 4.992 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0803` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0803 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` < `0.1057` → IC=+0.130 (n=897)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1057 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.3107` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.3107 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `2.5664` → IC=+0.134 (n=831)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5664 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `1.4731` → IC=+0.132 (n=944)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.4731 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.2093` → IC=+0.131 (n=1278)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2093 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` < `0.1756` → IC=+0.147 (n=641)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1756 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.156 (n=216)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6267 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `1.0473` → IC=+0.137 (n=293)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0473 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.0793` → IC=+0.249 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0793 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.6349` → IC=+0.207 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6349 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `2.9971` → IC=+0.227 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9971 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.263 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.033)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.170 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0071 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.163 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.349` → IC=+0.343 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.349 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.154 (n=325)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.06 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.319 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.329 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.329 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.297 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.5765` → IC=+0.330 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5765 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0645` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0645 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `1.7987` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7987 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.334 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1982.2745` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.2745 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.287)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.289 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.222 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.4506` → IC=+0.230 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4506 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.2046` → IC=+0.235 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2046 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.7164` → IC=+0.234 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7164 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.777` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.777 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2957` → IC=+0.227 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2957 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.8798` → IC=+0.239 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8798 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.0775` → IC=+0.229 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0775 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2656` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2656 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.3528` → IC=+0.268 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3528 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.0145` → IC=+0.227 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0145 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `13285.6042` → IC=+0.252 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13285.6042 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.182 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0021 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3117` → IC=+0.145 (n=370)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3117 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.141 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.143 (n=385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 18.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.3948` → IC=+0.165 (n=326)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.3948 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1843` → IC=+0.170 (n=328)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1843 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.989` → IC=+0.237 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.989 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.182 (n=124)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6267 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.0206` → IC=+0.135 (n=168)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.0206 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1081` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1081 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.5404` → IC=+0.158 (n=267)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.5404 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4188` → IC=+0.158 (n=267)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4188 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=478)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `12236.1369` → IC=+0.153 (n=168)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12236.1369 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `254.0` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 254.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0071 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.136 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=184)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `1917.67` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1917.67 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 23.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.328 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0858` → IC=+0.305 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0858 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.289 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.285)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` < `0.5027` → IC=+0.312 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5027 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.013` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.013 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` > `0.3362` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3362 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `2.9495` → IC=+0.286 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9495 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.302 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `sigma_h` > `0.0048` → IC=-0.142 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=431)

- **FILTRO** `ibs_20min` > `0.882` → IC=-0.183 (n=162)

  - _Acción_: SKIP cuando `ibs_20min` > 0.882
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=488)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.141 (n=51)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=599)

- **PATRÓN** `dist_vwap_pct` > `0.1367` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1367 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.0641` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0641 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.6131` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.6131 (IC base=-0.068)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `ibs_20min` > `0.75` → IC=-0.135 (n=272)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=845)

- **FILTRO** `sigma_ewma_delta_pct` > `3.026` → IC=-0.132 (n=324)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.026
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=793)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.127 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0076 (IC base=+0.057)

- **PATRÓN** `drift_60min` |x|≤ `0.2528` → IC=+0.130 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.2528 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.3333` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.3333 (IC base=+0.057)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.4414` → IC=-0.137 (n=265)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4414
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=266)

- **FILTRO** `sigma_h` > `0.011` → IC=-0.151 (n=250)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=753)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.164 (n=242)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=761)

- **FILTRO** `sigma_ewma_delta_pct` > `6.517` → IC=-0.165 (n=165)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.517
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=838)

- **PATRÓN** `dist_vwap_pct` < `0.1852` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1852 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.9484` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9484 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` < `0.1977` → IC=+0.226 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1977 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` < `0.6886` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6886 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` > `1.0971` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0971 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.158 (n=760)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0078 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.9479` → IC=+0.251 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9479 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.4271` → IC=+0.257 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4271 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.333` → IC=+0.127 (n=1305)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.333 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.1596` → IC=+0.188 (n=254)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.1596 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1157` → IC=+0.159 (n=973)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1157 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2516` → IC=+0.210 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2516 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.5046` → IC=+0.166 (n=336)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.5046 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.9418` → IC=+0.169 (n=336)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.9418 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.286 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.165 (n=1041)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.5906` → IC=+0.221 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5906 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1295` → IC=+0.189 (n=580)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1295 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.199 (n=632)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.6258 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2533` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2533 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `1.6216` → IC=+0.251 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6216 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.245 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.034)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.936` → IC=-0.214 (n=110)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.936
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=552)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.418` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.418 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.0542` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0542 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.317` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.317 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ballena_activa_n` > `491.0` → IC=-0.200 (n=28)

  - _Acción_: SKIP cuando `ballena_activa_n` > 491.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=85)

- **PATRÓN** `volumen_regimen` < `0.5607` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.5607 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` > `0.9955` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.9955 (IC base=-0.042)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.292 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0614` → IC=+0.222 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0614 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.263 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.303 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.1444` → IC=+0.187 (n=266)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1444 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `2.0881` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.0881 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `3.9033` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.9033 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1914.9184` → IC=+0.206 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.9184 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.413 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.372)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.403 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.372)

- **PATRÓN** `volumen_pendiente_norm` > `0.1384` → IC=+0.389 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1384 (IC base=+0.372)

- **PATRÓN** `volumen_spike_ratio` < `2.9764` → IC=+0.444 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9764 (IC base=+0.372)

- **PATRÓN** `libro_liquidez` > `1874.461` → IC=+0.415 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1874.461 (IC base=+0.372)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.132 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=251)

- **FILTRO** `ibs_20min` < `0.1055` → IC=-0.163 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1055
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=281)

- **FILTRO** `dist_vwap_pct` < `0.6455` → IC=-0.227 (n=42)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6455
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=21)

- **FILTRO** `volumen_regimen` > `1.0124` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0124
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=48)

- **FILTRO** `libro_liquidez` < `8696.3344` → IC=-0.195 (n=93)

  - _Acción_: SKIP cuando `libro_liquidez` < 8696.3344
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=281)

- **FILTRO** `dist_vwap_pct` < `0.1085` → IC=-0.143 (n=54)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `volumen_regimen` > `0.8819` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8819
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

- **FILTRO** `volumen_regimen` < `0.6808` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6808
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.161 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=831)

- **PATRÓN** `dist_vwap_pct` > `0.6455` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6455 (IC base=-0.059)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.5072` → IC=-0.140 (n=248)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5072
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=250)

- **FILTRO** `ibs_20min` > `0.7273` → IC=-0.144 (n=203)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=613)

- **FILTRO** `dist_vwap_pct` > `0.1326` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1326
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `volumen_regimen` > `1.2342` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.2342
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=42)

- **PATRÓN** `ibs_20min` > `0.84` → IC=+0.224 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.84 (IC base=-0.004)

- **PATRÓN** `dist_vwap_pct` > `0.3033` → IC=+0.231 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3033 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6209` → IC=+0.123 (n=136)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6209 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2609` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2609 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.9854` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.9854 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.185 (n=90)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 80.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.344 (n=209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.247 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.280 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.2452` → IC=+0.329 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2452 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.128` → IC=+0.267 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.128 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.8308` → IC=+0.244 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8308 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` < `0.0807` → IC=+0.212 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0807 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2413` → IC=+0.276 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2413 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.2651` → IC=+0.225 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2651 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2507.0533` → IC=+0.222 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2507.0533 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.281 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.273 (n=407)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.301 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.2791` → IC=+0.324 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2791 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` > `0.3856` → IC=+0.264 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3856 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` < `0.223` → IC=+0.270 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.223 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.486` → IC=+0.284 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.486 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.283 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7044 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `1.5839` → IC=+0.253 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5839 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.232 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.262)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.216 (n=652)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.171 (n=743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.9015` → IC=+0.259 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9015 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.7409` → IC=+0.246 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7409 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.446` → IC=+0.278 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.446 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.6919` → IC=+0.177 (n=1167)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6919 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1033` → IC=+0.188 (n=688)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1033 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.3453` → IC=+0.154 (n=1505)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.3453 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.4539` → IC=+0.148 (n=1710)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4539 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=1536)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3500.7061` → IC=+0.196 (n=652)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3500.7061 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.191 (n=759)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 132.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.208 (n=1495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.194 (n=1699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.245 (n=1702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` < `0.3215` → IC=+0.178 (n=1472)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.3215 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.761` → IC=+0.196 (n=330)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.761 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.469` → IC=+0.186 (n=1719)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 5.469 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `0.8516` → IC=+0.176 (n=932)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8516 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.2504` → IC=+0.232 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2504 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5932` → IC=+0.185 (n=481)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.5932 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.7655` → IC=+0.205 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7655 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.192 (n=440)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 60.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.210 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.377` → IC=+0.359 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.377 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1402` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1402 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4192` → IC=+0.134 (n=260)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4192 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.186 (n=269)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.06 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.302 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.291)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.316 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.2108` → IC=+0.332 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2108 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.315 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.4177` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4177 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.0686` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0686 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.8747` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8747 (IC base=+0.291)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.374 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1966.1335` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.1335 (IC base=+0.291)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.264 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.221 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.6555` → IC=+0.240 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6555 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1693` → IC=+0.246 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1693 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.216` → IC=+0.300 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.216 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.3047` → IC=+0.182 (n=256)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.3047 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8896` → IC=+0.217 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8896 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.231 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.1727` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1727 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `11364.2884` → IC=+0.223 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11364.2884 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.182 (n=347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0047 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.2044` → IC=+0.184 (n=305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.2044 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.165 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.3777` → IC=+0.193 (n=347)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3777 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1897` → IC=+0.179 (n=353)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1897 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.746` → IC=+0.233 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.746 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.634` → IC=+0.237 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.634 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.065` → IC=+0.203 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.065 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.773` → IC=+0.185 (n=160)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.773 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4262` → IC=+0.149 (n=240)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4262 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `244.0` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 244.0 (IC base=+0.149)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.198 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0076 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1433` → IC=+0.157 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1433 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.212 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.804` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.804 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2317` → IC=+0.134 (n=249)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.2317 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.0183` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0183 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `3.9092` → IC=+0.138 (n=114)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 3.9092 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.175 (n=244)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.04 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `1970.8484` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1970.8484 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.339 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.302)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.304 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.2366` → IC=+0.326 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2366 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.329 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.3486` → IC=+0.323 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3486 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.578` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.578 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.3308` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3308 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `4.3528` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.3528 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.302)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.238 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.1348` → IC=+0.232 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1348 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.230 (n=228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.270 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.1644` → IC=+0.239 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1644 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.788` → IC=+0.389 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.788 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6331` → IC=+0.238 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6331 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1648` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1648 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4657` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4657 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.4571` → IC=+0.244 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4571 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `9480.4909` → IC=+0.233 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9480.4909 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 198.0 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.204 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2729` → IC=+0.173 (n=295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2729 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.159 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.3077` → IC=+0.224 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3077 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.5137` → IC=+0.170 (n=392)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.5137 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.607` → IC=+0.265 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.607 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.0458` → IC=+0.150 (n=295)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0458 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6089` → IC=+0.159 (n=335)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6089 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1001` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1001 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.9099` → IC=+0.210 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9099 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.217 (n=111)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.212 (n=335)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.203 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.131 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.8621` → IC=+0.223 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8621 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.6608` → IC=+0.268 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6608 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.464` → IC=+0.261 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.464 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `0.6776` → IC=+0.129 (n=340)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6776 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `1.5631` → IC=+0.121 (n=312)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.5631 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2751.5045` → IC=+0.203 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2751.5045 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.215 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.199 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 14.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.4444` → IC=+0.212 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4444 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.434` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 7.434 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `0.8507` → IC=+0.149 (n=223)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.8507 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2708` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2708 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `2.1018` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.1018 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2599.7014` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2599.7014 (IC base=+0.105)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0163` → IC=+0.220 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0163 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.1493` → IC=+0.174 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1493 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.8026` → IC=+0.225 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8026 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `1.5864` → IC=+0.240 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.5864 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.956` → IC=+0.243 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.956 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2275` → IC=+0.171 (n=421)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2275 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.8407` → IC=+0.184 (n=280)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8407 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.2072` → IC=+0.182 (n=338)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.2072 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.842` → IC=+0.171 (n=256)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.842 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=465)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2507.5041` → IC=+0.172 (n=376)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2507.5041 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.272 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.4413` → IC=+0.233 (n=383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4413 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.246 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.1224` → IC=+0.326 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1224 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` < `0.3609` → IC=+0.242 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3609 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.735` → IC=+0.260 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.735 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6963` → IC=+0.259 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6963 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2945` → IC=+0.337 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2945 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.8936` → IC=+0.247 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8936 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.186 (n=167)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 31.0 (IC base=+0.229)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.153 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0058 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.156 (n=280)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.6 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.5255` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5255 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.989` → IC=+0.255 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.989 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.1852` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1852 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `3335.1863` → IC=+0.132 (n=142)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3335.1863 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 278.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.263 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.2632` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.2632 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.232` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.232 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.6741` → IC=+0.128 (n=100)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.6741 (IC base=+0.053)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `ibs_20min` < `0.2178` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2178
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=52)

- **FILTRO** `libro_liquidez` < `7625.2292` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 7625.2292
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=35)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.007)

- **PATRÓN** `ibs_20min` > `0.2178` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.2178 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.2396` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2396 (IC base=+0.007)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.003` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 4.003 (IC base=+0.007)

- **PATRÓN** `libro_liquidez` > `7625.2292` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 7625.2292 (IC base=+0.007)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3002` → IC=+0.214 (n=96)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3002 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.217 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.3222` → IC=+0.186 (n=84)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.3222 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.5684` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5684 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` < `0.2305` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2305 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.492` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.492 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.2361` → IC=+0.204 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2361 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.0902` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0902 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.602` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.602 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `12686.2928` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 12686.2928 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 131.0 (IC base=+0.159)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `sigma_h` > `0.0045` → IC=-0.143 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.217 (n=51)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.261 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.265 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.2111` → IC=+0.245 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2111 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.300 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.8134` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8134 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1417` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1417 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.836` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.836 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `0.7026` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7026 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.1851` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1851 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.3201` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3201 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.5657` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5657 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `3094.8617` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3094.8617 (IC base=+0.237)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.357 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.095)

- **PATRÓN** `drift_60min` |x|≤ `0.2623` → IC=+0.179 (n=51)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2623 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.244 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.529` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.529 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.939` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.939 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.6933` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6933 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `9493.103` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9493.103 (IC base=+0.095)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5385` → IC=-0.174 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5385
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=129)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=77)

- **FILTRO** `ibs_20min` > `0.6667` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6667
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=77)

- **FILTRO** `volumen_pendiente_norm` > `0.1087` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1087
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=60)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.139 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 15.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.155 (n=85)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.8889 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.176` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.176 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.188` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.188 (IC base=+0.035)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.233 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.781` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.781 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.99` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.99 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0773 (IC base=+0.029)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.222 (n=747)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=1142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.147 (n=826)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.95` → IC=+0.288 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.95 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `1.0106` → IC=+0.246 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0106 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.41` → IC=+0.235 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.41 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.154 (n=665)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7028 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.2381` → IC=+0.146 (n=504)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2381 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2394` → IC=+0.183 (n=392)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2394 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.7976` → IC=+0.140 (n=1922)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.7976 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.9213` → IC=+0.155 (n=1281)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.9213 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=1751)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3400.5924` → IC=+0.192 (n=745)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3400.5924 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.199 (n=758)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 166.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.214 (n=1776)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.3891` → IC=+0.197 (n=2017)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3891 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.188 (n=1846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 7.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.5398` → IC=+0.241 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5398 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.6724` → IC=+0.174 (n=1619)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.6724 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.339` → IC=+0.203 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.339 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.597` → IC=+0.190 (n=1894)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.597 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.6151` → IC=+0.175 (n=512)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6151 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `1.1898` → IC=+0.179 (n=512)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.1898 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.1667` → IC=+0.235 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1667 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.2742` → IC=+0.193 (n=601)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.2742 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.133 (n=595)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 57.0 (IC base=+0.184)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.210 (n=184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.158 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.289 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.154` → IC=+0.356 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.154 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2113` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2113 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.159 (n=297)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.06 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.312 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.287 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.2086` → IC=+0.329 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2086 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.293 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.300 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.5819` → IC=+0.339 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5819 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` < `0.0647` → IC=+0.312 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0647 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.7667` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7667 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.316 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1989.2275` → IC=+0.329 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1989.2275 (IC base=+0.287)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.185 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0028 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.200 (n=148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3434` → IC=+0.220 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3434 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.2304` → IC=+0.239 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2304 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.065` → IC=+0.247 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.065 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.2821` → IC=+0.168 (n=326)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2821 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.8877` → IC=+0.171 (n=217)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8877 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2551` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2551 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.6131` → IC=+0.196 (n=278)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.6131 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.3498` → IC=+0.200 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3498 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `10994.9669` → IC=+0.199 (n=217)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 10994.9669 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.204 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.3167` → IC=+0.172 (n=367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3167 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.161 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.170 (n=380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 18.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` < `0.5045` → IC=+0.188 (n=367)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5045 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` < `0.1431` → IC=+0.191 (n=325)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.1431 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.682` → IC=+0.227 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.682 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.6202` → IC=+0.236 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6202 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.0924` → IC=+0.271 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0924 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.7479` → IC=+0.201 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7479 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.5117` → IC=+0.182 (n=243)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.5117 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=474)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `12582.7558` → IC=+0.180 (n=123)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 12582.7558 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `315.0` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 315.0 (IC base=+0.160)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.245 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.717` → IC=+0.247 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.717 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.864` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.864 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.2327` → IC=+0.168 (n=251)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.2327 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.1733` → IC=+0.149 (n=109)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1733 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `4.0128` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 4.0128 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.208 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1854.4986` → IC=+0.185 (n=214)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1854.4986 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.332 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.273 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.282 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.5575` → IC=+0.340 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5575 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.2282` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2282 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.4009` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4009 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `2.5357` → IC=+0.276 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5357 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.145 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0062 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.164 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.008 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.1221` → IC=+0.146 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1221 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.161 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.3665` → IC=+0.208 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3665 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.919` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.919 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.544` → IC=+0.201 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.544 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7028 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.2022` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.2022 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4166` → IC=+0.223 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4166 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `8687.9043` → IC=+0.238 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8687.9043 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.202 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 233.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.247 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.4237` → IC=+0.140 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4237 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.161 (n=184)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.0606` → IC=+0.231 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0606 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.7345` → IC=+0.144 (n=279)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.7345 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.624` → IC=+0.274 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.624 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.5724` → IC=+0.148 (n=89)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.5724 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `1.091` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 1.091 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2596` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2596 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.1725` → IC=+0.174 (n=185)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.1725 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.5672` → IC=+0.151 (n=187)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5672 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4090.2043` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 4090.2043 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.164 (n=126)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 171.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.172 (n=175)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0082 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.9268` → IC=+0.268 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9268 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.6755` → IC=+0.231 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6755 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.146` → IC=+0.262 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.146 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `2730.2904` → IC=+0.277 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2730.2904 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.183 (n=162)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 70.0 (IC base=+0.080)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.190 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.005 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.181 (n=377)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5714 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.448` → IC=+0.127 (n=338)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.448 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `1.0484` → IC=+0.130 (n=171)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.0484 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.072` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.072 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `1.4277` → IC=+0.152 (n=231)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4277 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `1404.9736` → IC=+0.136 (n=251)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1404.9736 (IC base=+0.099)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.241 (n=218)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0992` → IC=+0.179 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0992 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.171 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 8.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.9795` → IC=+0.300 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9795 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `1.22` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.22 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.924` → IC=+0.250 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.924 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.611` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.611 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `1.0463` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.0463 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2429` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2429 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.7439` → IC=+0.181 (n=430)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.7439 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.9023` → IC=+0.171 (n=287)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.9023 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=527)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `2635.1118` → IC=+0.183 (n=320)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2635.1118 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.237 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.306 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.3797` → IC=+0.228 (n=464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3797 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.225 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.4875` → IC=+0.281 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4875 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.6747` → IC=+0.222 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6747 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.01` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.01 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.906` → IC=+0.217 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.906 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.8813` → IC=+0.234 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8813 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.286 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.6697` → IC=+0.217 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6697 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 37.0 (IC base=+0.208)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=452)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.153 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 16.0 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.2874` → IC=+0.174 (n=133)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2874 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2691` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2691 (IC base=+0.059)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=160)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `7152.007` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 7152.007 (IC base=+0.059)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.209 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1901` → IC=+0.178 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1901 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.196 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 16.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.254 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.612` → IC=+0.182 (n=309)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.612 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6795` → IC=+0.182 (n=86)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6795 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.315` → IC=+0.159 (n=335)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.315 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.448` → IC=+0.174 (n=170)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.448 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.654` → IC=+0.150 (n=341)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 5.654 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.3715` → IC=+0.169 (n=351)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.3715 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.6466` → IC=+0.154 (n=351)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6466 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.151 (n=302)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0763` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0763 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.6912` → IC=+0.186 (n=348)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.6912 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.151 (n=348)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=452)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `6239.5556` → IC=+0.177 (n=351)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 6239.5556 (IC base=+0.150)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `dist_vwap_pct` < `0.5361` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.5361
  - _Potencial_: sin este filtro IC_bueno=+0.259 (n=27)

- **FILTRO** `sigma_ewma_delta_pct` > `5.401` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.401
  - _Potencial_: sin este filtro IC_bueno=+0.210 (n=29)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.250 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0037 (IC base=+0.065)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.6176` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6176 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.5361` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5361 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.401` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.401 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `12732.4097` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12732.4097 (IC base=+0.065)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.192 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0045 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.065` → IC=+0.194 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.065 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.279 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.0962` → IC=+0.234 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0962 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.4828` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.4828 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.29` → IC=+0.158 (n=217)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.29 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.584` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.584 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.051` → IC=+0.164 (n=206)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.051 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.3022` → IC=+0.173 (n=209)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.3022 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.906` → IC=+0.160 (n=139)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.906 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.0814` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0814 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.7181` → IC=+0.173 (n=209)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.7181 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `9882.4678` → IC=+0.159 (n=209)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9882.4678 (IC base=+0.146)

### GBM_LATE_5M#ETH#5min
- **FILTRO** `libro_liquidez` < `7085.816` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 7085.816
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=41)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.9785` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9785 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.504` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.504 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.9592` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.9592 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.2506` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.2506 (IC base=+0.065)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `7085.816` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7085.816 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 108.0 (IC base=+0.065)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.294 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.231 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.2126` → IC=+0.320 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2126 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.6918` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6918 (IC base=+0.232)

- **PATRÓN** `ibs_20min` > `0.1577` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1577 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.4676` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4676 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` < `0.1463` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1463 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.758` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.758 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` < `0.9902` → IC=+0.340 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9902 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` < `0.1261` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1261 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `2.4942` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4942 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `7445.2749` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7445.2749 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 157.0 (IC base=+0.232)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `sigma_ewma_delta_pct` < `2.482` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.482
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `sigma_ewma_delta_pct` < `2.985` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.985
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.482` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 2.482 (IC base=-0.017)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.149 (n=55)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=112)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=160)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **FILTRO** `volumen_regimen` > `0.8876` → IC=-0.196 (n=54)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8876
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.180 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0054 (IC base=+0.057)

- **PATRÓN** `drift_60min` |x|≤ `0.1151` → IC=+0.151 (n=41)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1151 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.213 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.0949` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0949 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.0847` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0847 (IC base=+0.057)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=111)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2013.1835` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2013.1835 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=42)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.062)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7342 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.15` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 13.15 (IC base=+0.062)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.326 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=43)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.360 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

- **FILTRO** `volumen_regimen` > `0.8876` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8876
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.242 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.368 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2012` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2012 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.41` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.41 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.8241` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8241 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2340.5972` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2340.5972 (IC base=+0.100)

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
- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=58)

- **FILTRO** `libro_liquidez` < `2167.8726` → IC=-0.337 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2167.8726
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=48)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.380 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=75)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=75)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

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

- **FILTRO** `sigma_ewma_delta_pct` > `4.524` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.524
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=26)

- **FILTRO** `libro_liquidez` < `4361.6218` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 4361.6218
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `ibs_20min` > `0.8144` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8144
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.5333` → IC=-0.186 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5333
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=101)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6429 (IC base=+0.059)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.991` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.991 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `2399.5952` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.5952 (IC base=+0.159)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2547.7568` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2547.7568 (IC base=+0.096)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.088)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2547.7568` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2547.7568 (IC base=+0.096)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.088)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=95)

- **FILTRO** `libro_liquidez` < `2012.8653` → IC=-0.397 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 2012.8653
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=84)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=234)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.285 (n=63)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=77)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35898.38` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `liq_usd_total` < 35898.38
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.214 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=84)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.134 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.059)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `liq_usd_total` < `24810.11` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_usd_total` < 24810.11
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 56.0 (IC base=+0.035)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_usd_total` < `5082.42` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `liq_usd_total` < 5082.42
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9797` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9797
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=73)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.152 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=47)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `liq_usd_total` < `433.59` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_usd_total` < 433.59
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=66)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=61)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=66)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_usd_total` < `17791.23` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 17791.23
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2168.7825` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 2168.7825
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=72)

- **PATRÓN** `libro_liquidez` > `2223.5408` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2223.5408 (IC base=+0.010)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=248)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.154 (n=539)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1676)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.258 (n=518)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1611)

- **FILTRO** `ibs_20min` > `0.2778` → IC=-0.227 (n=532)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=1597)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.145 (n=530)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1599)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.162 (n=140)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=183)

- **FILTRO** `ibs_20min` < `0.7767` → IC=-0.167 (n=106)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7767
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=217)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.193 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=270)

- **FILTRO** `ibs_20min` > `0.7602` → IC=-0.233 (n=88)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7602
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=268)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.123 (n=144)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.505 (IC base=-0.008)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.140 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=199)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.277 (n=92)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=277)

- **FILTRO** `ibs_20min` > `0.2136` → IC=-0.223 (n=92)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2136
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=277)

- **FILTRO** `ballena_activa_n` > `82.0` → IC=-0.210 (n=91)

  - _Acción_: SKIP cuando `ballena_activa_n` > 82.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=278)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.179 (n=107)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=223)

- **FILTRO** `ibs_20min` < `0.7248` → IC=-0.179 (n=82)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7248
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=248)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.213 (n=120)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=241)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.218 (n=122)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=239)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.125 (n=102)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=295)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.245 (n=96)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=288)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.205 (n=93)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=291)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.297 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=255)

- **FILTRO** `drift_20min_pct` |x|> `0.3125` → IC=-0.238 (n=82)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.3125
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=250)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.214 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=222)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.214 (n=89)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=363)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.293 (n=109)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=218)

- **FILTRO** `drift_20min_pct` |x|> `0.1499` → IC=-0.134 (n=219)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1499
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=108)

- **FILTRO** `ibs_20min` > `0.2959` → IC=-0.331 (n=81)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2959
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=246)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=167)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `py_entrada` < `0.36` → IC=-0.279 (n=1294)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=4072)

- **FILTRO** `ibs_7min` < `0.7407` → IC=-0.226 (n=1338)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=4028)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.179 (n=1789)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3577)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.223 (n=1592)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4883)

- **FILTRO** `ibs_7min` > `0.7039` → IC=-0.172 (n=1618)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7039
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4857)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=187)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=564)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.174 (n=522)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=229)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.219 (n=183)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=568)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.124 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=705)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.252 (n=248)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=790)

- **FILTRO** `drift_7min_pct` |x|> `0.1375` → IC=-0.172 (n=352)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1375
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=686)

- **FILTRO** `ibs_7min` > `0.2951` → IC=-0.192 (n=352)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2951
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=686)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.249 (n=257)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=857)

- **FILTRO** `ballena_activa_n` > `130.0` → IC=-0.164 (n=278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 130.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=836)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.190 (n=279)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=857)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.198 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=554)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.341 (n=180)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=554)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.272 (n=182)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=552)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.280 (n=180)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=554)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.269 (n=245)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=873)

- **FILTRO** `ibs_7min` > `0.8222` → IC=-0.180 (n=279)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8222
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=839)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.158 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=696)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.272 (n=213)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=700)

- **FILTRO** `ibs_7min` < `0.7828` → IC=-0.196 (n=228)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7828
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=685)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.220 (n=223)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=690)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.305 (n=224)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=686)

- **FILTRO** `ibs_7min` > `0.1739` → IC=-0.159 (n=309)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1739
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=601)

- **FILTRO** `ballena_activa_n` > `35.0` → IC=-0.206 (n=226)

  - _Acción_: SKIP cuando `ballena_activa_n` > 35.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=684)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.216 (n=241)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=743)

- **FILTRO** `ibs_7min` < `0.7727` → IC=-0.200 (n=245)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7727
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=739)

- **FILTRO** `ballena_activa_n` > `17.0` → IC=-0.215 (n=244)

  - _Acción_: SKIP cuando `ballena_activa_n` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=740)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.177 (n=292)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=888)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.283 (n=205)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=665)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.224 (n=208)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=662)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.215 (n=212)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=658)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.289 (n=226)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=867)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.135 (n=371)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=722)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.135 (n=354)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=739)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=149)

- **FILTRO** `drift_7min_pct` |x|> `0.106` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.106
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=116)

- **FILTRO** `ibs_7min` > `0.0606` → IC=-0.133 (n=58)

  - _Acción_: SKIP cuando `ibs_7min` > 0.0606
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=117)

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

- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.143 (n=228)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.142 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 4.0 (IC base=+0.118)

- **PATRÓN** `total_vol_5m` < `389.535` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 389.535 (IC base=+0.118)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4415` → IC=+0.167 (n=16)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4415 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.300 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.125)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `total_vol_5m` < 422.506 (IC base=+0.125)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.167 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 14.0 (IC base=+0.083)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.083)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=66)

- **FILTRO** `T_h` > `87.9756` → IC=-0.370 (n=75)

  - _Acción_: SKIP cuando `T_h` > 87.9756
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=40)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.123 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0039 (IC base=-0.184)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.350 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=20)

- **FILTRO** `T_h` > `98.7549` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=-0.167)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.125 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=30)

- **FILTRO** `T_h` > `119.1632` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `T_h` > 119.1632
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=45)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.318 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.309 (n=19)

- **FILTRO** `T_h` < `95.1632` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `T_h` < 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=51)

- **PATRÓN** `T_h` < `119.1632` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `T_h` < 119.1632 (IC base=-0.046)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `87.9957` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `8.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `streak_estiramiento` > `0.4086` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4086
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `ballena_activa_n` > `62.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 62.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.49` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=69)

- **FILTRO** `streak_estiramiento` > `0.437` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.437
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 52.0 (IC base=+0.000)

### STREAK_FADE_5M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=160)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.167 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=43)

- **FILTRO** `libro_liquidez` < `3605.4421` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 3605.4421
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=53)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.5 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `3605.4421` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3605.4421 (IC base=+0.042)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=63)

- **FILTRO** `streak_estiramiento` > `0.644` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.644
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=64)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=77)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.135 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 18.0 (IC base=+0.027)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=149)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.167 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 19.0 (IC base=-0.004)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.505 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 22.0 (IC base=+0.084)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1014)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=595)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=603)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.144 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0036 (IC base=+0.108)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.124 (n=360)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.108)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.189 (n=371)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.5 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.3754` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.3754 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.553` → IC=+0.238 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.553 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `6215.1452` → IC=+0.139 (n=120)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 6215.1452 (IC base=+0.108)

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.2368` → IC=-0.223 (n=117)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2368
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=240)

- **FILTRO** `sigma_ewma_delta_pct` > `6.729` → IC=-0.198 (n=51)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.729
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=306)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=96)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=203)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0397` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0397
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.220 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `dist_vwap_pct` < `0.2283` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2283
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=3)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0039` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=47)

- **FILTRO** `ibs_15` < `0.3286` → IC=-0.182 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.3286
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=42)

- **FILTRO** `dist_vwap_pct` < `0.2527` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2527
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.163 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0029 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.168` → IC=+0.174 (n=84)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.168 (IC base=+0.136)

- **PATRÓN** `drift_15min` |x|≤ `0.6592` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `drift_15min` |x|≤ 0.6592 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2917` → IC=+0.176 (n=32)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2917 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 4.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.9375` → IC=+0.283 (n=44)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9375 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1166` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1166 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.945` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 6.945 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.598` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 18.598 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `11130.6446` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11130.6446 (IC base=+0.136)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2056` → IC=-0.204 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2056
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.9263` → IC=-0.143 (n=54)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.9263
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.5859` → IC=-0.257 (n=35)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5859
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=73)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.122 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0043 (IC base=+0.091)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2085` → IC=+0.192 (n=37)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2085 (IC base=+0.091)

- **PATRÓN** `ibs_15` > `0.5859` → IC=+0.260 (n=73)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5859 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` < `0.0929` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.0929 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.091)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `sigma_h` < `0.0028` → IC=-0.122 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0028
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=56)

- **FILTRO** `ibs_15` < `0.0101` → IC=-0.237 (n=17)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

- **FILTRO** `dist_vwap_pct` > `0.1689` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1689
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

- **FILTRO** `sigma_ewma_delta_pct` > `7.153` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.153
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=52)

- **FILTRO** `drift_15min` |x|> `0.5961` → IC=-0.167 (n=64)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5961
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=195)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `delta_ratio_macro` |x|> `0.2161` → IC=+0.156 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.2161 (IC base=+0.033)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.03 (IC base=+0.033)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.177 (n=29)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=31)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.258 (n=31)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.764` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.764 (IC base=+0.048)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `ibs_15` < `0.1667` → IC=-0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1667
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=33)

- **FILTRO** `dist_vwap_pct` < `0.1008` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1008
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `sigma_ewma_delta_pct` < `2.366` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.366
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=34)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0106 (IC base=+0.000)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` < `0.4088` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4088 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.157 (n=100)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` > 0.4444 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.4713` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4713 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.54` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.54 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.144 (n=88)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.086)

- **PATRÓN** `ibs_15` < `0.1163` → IC=+0.167 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1163 (IC base=+0.041)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.295 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.1981` → IC=+0.297 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1981 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1559` → IC=+0.293 (n=80)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1559 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.309 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.352 (n=120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.5342` → IC=+0.357 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5342 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.489` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.489 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `7219.8643` → IC=+0.333 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7219.8643 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `550.0` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 550.0 (IC base=+0.284)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1396` → IC=+0.318 (n=31)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1396 (IC base=+0.258)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.281 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1898` → IC=+0.278 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1898 (IC base=+0.258)

- **PATRÓN** `drift_15min` |x|≤ `0.411` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.411 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.303 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.266 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.258)

- **PATRÓN** `ibs_15` > `0.7363` → IC=+0.306 (n=70)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7363 (IC base=+0.258)

- **PATRÓN** `dist_vwap_pct` > `0.4105` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4105 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.871` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.871 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.106` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.106 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `8508.8052` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8508.8052 (IC base=+0.258)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.333 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.395 (n=17)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.312)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1549` → IC=+0.389 (n=34)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1549 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.312)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.318 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.312)

- **PATRÓN** `ibs_15` > `0.7045` → IC=+0.406 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7045 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` > `0.4682` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4682 (IC base=+0.312)

- **PATRÓN** `dist_vwap_pct` < `0.3445` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3445 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `3078.5215` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3078.5215 (IC base=+0.312)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.4151` → IC=-0.307 (n=86)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4151
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=258)

- **FILTRO** `sigma_h` > `0.0086` → IC=-0.156 (n=724)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=1407)

- **FILTRO** `ibs_15` > `0.53` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=58)

- **FILTRO** `sigma_ewma_delta_pct` > `16.746` → IC=-0.199 (n=287)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.746
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=1844)

- **PATRÓN** `ibs_15` > `0.4151` → IC=+0.150 (n=258)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` > 0.4151 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.53` → IC=+0.283 (n=58)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.53 (IC base=-0.098)

- **PATRÓN** `dist_vwap_pct` < `0.1474` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1474 (IC base=-0.098)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.233 (n=118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=358)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.233 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=362)

- **FILTRO** `sigma_ewma_delta_pct` > `25.561` → IC=-0.250 (n=78)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 25.561
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=398)

- **FILTRO** `libro_liquidez` < `11403.3144` → IC=-0.204 (n=157)

  - _Acción_: SKIP cuando `libro_liquidez` < 11403.3144
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=319)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4875` → IC=-0.351 (n=45)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4875
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=93)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=121)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.000)

- **PATRÓN** `ibs_15` > `0.4875` → IC=+0.174 (n=93)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.87€ cuando `ibs_15` > 0.4875 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` > `0.7261` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.7261 (IC base=+0.000)

- **PATRÓN** `libro_liquidez` > `10004.8873` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10004.8873 (IC base=+0.000)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1677` → IC=+0.192 (n=37)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.96€ cuando `pct_spot_vs_ref` |x|≤ 0.1677 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.167 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0056 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.218 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.004 (IC base=+0.167)

- **PATRÓN** `drift_15min` |x|≤ `0.6513` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.6513 (IC base=+0.167)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1155` → IC=+0.167 (n=37)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.1155 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.167 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 14.0 (IC base=+0.167)

- **PATRÓN** `ibs_15` < `0.3879` → IC=+0.321 (n=37)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3879 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.178` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.178 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.936` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 11.936 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `4836.9669` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4836.9669 (IC base=+0.167)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.187 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=127)

- **FILTRO** `sigma_ewma_delta_pct` > `12.226` → IC=-0.180 (n=120)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.226
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=625)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.085` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 11.085 (IC base=-0.062)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.005` → IC=-0.167 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=149)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.164 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=66)

- **FILTRO** `libro_liquidez` < `2507.6219` → IC=-0.186 (n=49)

  - _Acción_: SKIP cuando `libro_liquidez` < 2507.6219
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=149)

- **FILTRO** `sigma_h` > `0.0077` → IC=-0.157 (n=345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=348)

- **FILTRO** `sigma_ewma_delta_pct` > `15.17` → IC=-0.213 (n=85)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.17
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=608)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.274 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.290 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1927` → IC=+0.284 (n=179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1927 (IC base=+0.267)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0596` → IC=+0.279 (n=179)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0596 (IC base=+0.267)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4165` → IC=+0.331 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4165 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.291 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.272 (n=182)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.267)

- **PATRÓN** `ibs_15` > `0.9661` → IC=+0.367 (n=81)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9661 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.2797` → IC=+0.341 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2797 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.266 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.772` → IC=+0.275 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.772 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `9931.1033` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9931.1033 (IC base=+0.267)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.257 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.250)

- **PATRÓN** `drift_60min` |x|≤ `0.1871` → IC=+0.286 (n=101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1871 (IC base=+0.250)

- **PATRÓN** `drift_15min` |x|≤ `0.6237` → IC=+0.280 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6237 (IC base=+0.250)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0911` → IC=+0.261 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0911 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.266 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.248 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.250)

- **PATRÓN** `ibs_15` > `0.9676` → IC=+0.354 (n=46)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9676 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` > `0.263` → IC=+0.316 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.263 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.679` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.679 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.495` → IC=+0.256 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.495 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `8349.505` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8349.505 (IC base=+0.250)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.290 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1995` → IC=+0.342 (n=36)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1995 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.339 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.283)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.280 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8702` → IC=+0.319 (n=70)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8702 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.7261` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7261 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.88` → IC=+0.302 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.88 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `9979.9504` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9979.9504 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=+0.283)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0492` → IC=-0.167 (n=22)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0492
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `drift_15min` |x|> `0.3418` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3418
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.147 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=251)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.278 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `113.3454` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `T_h` < 113.3454 (IC base=+0.079)

- **PATRÓN** `ratio` < `0.972` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.972 (IC base=+0.079)

- **PATRÓN** `T_h` > `146.1064` → IC=+0.443 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1064 (IC base=+0.345)

- **PATRÓN** `ratio` > `1.0147` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0147 (IC base=+0.345)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.9997` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `T_h` < 111.9997 (IC base=+0.076)

- **PATRÓN** `T_h` < `111.9957` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9957 (IC base=+0.262)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.262)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `87.9936` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9936 (IC base=+0.108)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.306 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.306)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.420)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.108 a +0.189 en UPDOWN_GBM#15min (n=371). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.9375 sube el IC de +0.136 a +0.283 en UPDOWN_GBM#BTC#15min (n=44). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5859 sube el IC de +0.091 a +0.260 en UPDOWN_GBM#ETH#15min (n=73). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.048 a +0.258 en UPDOWN_GBM#SOL#15min (n=31). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.086 a +0.157 en UPDOWN_GBM#XRP#15min (n=100). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1163 sube el IC de +0.041 a +0.167 en UPDOWN_GBM#XRP#15min (n=88). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.53 sube el IC de -0.098 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=58). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4875 sube el IC de +0.000 a +0.174 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=93). Ya aplicado como kelly_boost=+0.87€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3879 sube el IC de +0.167 a +0.321 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=37). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.062 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9661 sube el IC de +0.267 a +0.367 en UPDOWN_GBM_IBS_ALTO (n=81). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9676 sube el IC de +0.250 a +0.354 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=46). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8702 sube el IC de +0.283 a +0.319 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.284 a +0.352 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.7363 sube el IC de +0.258 a +0.306 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=70). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7045 sube el IC de +0.312 a +0.406 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#DOGE#5min` — IC=+0.095 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#DOGE` — IC=+0.095 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL#5min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `ORDER_FLOW_5M#SOL` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 557 | +0.072 | +39.71€ | 3 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 557 | +0.072 | +39.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 313 | +0.090 | +28.71€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 313 | +0.090 | +28.71€ | 0 | 12 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.030 | +0.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.030 | +0.07€ | 6 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 5629 | -0.098 | -633.09€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 614 | -0.080 | -103.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 5015 | -0.100 | -530.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 791 | -0.033 | -93.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 791 | -0.033 | -93.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 614 | -0.080 | -103.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 614 | -0.080 | -103.00€ | 3 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 359 | -0.137 | -154.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 359 | -0.137 | -154.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 1796 | -0.054 | -31.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 1796 | -0.054 | -31.40€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1344 | -0.170 | -211.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1344 | -0.170 | -211.38€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 24982 | +0.114 | -1673.68€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 4912 | +0.185 | -189.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 106 | -0.102 | -48.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 17005 | +0.093 | -1422.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2959 | +0.125 | -11.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 2860 | +0.060 | -508.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 18 | -0.045 | +2.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 2837 | +0.062 | -504.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 5276 | +0.135 | -119.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1368 | +0.191 | -97.40€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 2829 | +0.111 | -59.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1037 | +0.133 | +60.07€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 2863 | +0.072 | -417.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 17 | +0.022 | -2.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 2845 | +0.072 | -412.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 5675 | +0.130 | -41.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1793 | +0.170 | +1.16€ | 0 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 2828 | +0.115 | -29.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1042 | +0.109 | -5.33€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 5448 | +0.129 | -404.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1701 | +0.201 | -91.32€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 45 | +0.011 | -8.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 2822 | +0.086 | -237.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 880 | +0.133 | -66.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 2860 | +0.111 | -182.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 15 | -0.022 | -2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 2844 | +0.112 | -179.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 4937 | +0.178 | -345.70€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 4937 | +0.178 | -345.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1240 | +0.174 | -122.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1240 | +0.174 | -122.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 100 | -0.108 | +3.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 100 | -0.108 | +3.11€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1235 | +0.165 | -140.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1235 | +0.165 | -140.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1106 | +0.234 | -25.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1106 | +0.234 | -25.77€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1177 | +0.196 | -73.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1177 | +0.196 | -73.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 247 | +0.436 | -2.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 247 | +0.436 | -2.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 90 | +0.435 | +0.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 90 | +0.435 | +0.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 95 | +0.417 | -3.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 95 | +0.417 | -3.16€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 59 | +0.434 | +0.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 59 | +0.434 | +0.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 12199 | +0.195 | -1038.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 12199 | +0.195 | -1038.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 2256 | +0.126 | -420.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 2256 | +0.126 | -420.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1884 | +0.239 | -39.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1884 | +0.239 | -39.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2120 | +0.160 | -284.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2120 | +0.160 | -284.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1932 | +0.237 | -41.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1932 | +0.237 | -41.93€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1946 | +0.227 | -72.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1946 | +0.227 | -72.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 2061 | +0.195 | -179.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 2061 | +0.195 | -179.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 4367 | +0.129 | +88.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 4367 | +0.129 | +88.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 2169 | +0.141 | +91.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 2169 | +0.141 | +91.76€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 2198 | +0.117 | -3.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 2198 | +0.117 | -3.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 682 | +0.303 | +10.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 682 | +0.303 | +10.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 291 | +0.278 | -8.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 291 | +0.278 | -8.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 318 | +0.303 | +9.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 318 | +0.303 | +9.57€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 73 | +0.380 | +9.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 73 | +0.380 | +9.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 284 | +0.413 | -12.24€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 284 | +0.413 | -12.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 126 | +0.414 | -4.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 126 | +0.414 | -4.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 129 | +0.408 | -8.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 129 | +0.408 | -8.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 29 | +0.371 | +0.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 29 | +0.371 | +0.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 131 | +0.086 | -3.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 41 | +0.081 | -1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 90 | +0.087 | -2.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 5 | +0.054 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 5 | +0.054 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 106 | +0.093 | -1.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 16 | +0.089 | +0.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 90 | +0.087 | -2.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 20 | +0.000 | -4.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 20 | +0.000 | -4.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 3557 | +0.100 | -134.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 368 | +0.035 | -34.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 3189 | +0.107 | -99.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 2449 | +0.097 | -74.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 368 | +0.035 | -34.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 2081 | +0.108 | -39.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 1108 | +0.106 | -60.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 1108 | +0.106 | -60.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 365 | +0.279 | -27.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 365 | +0.279 | -27.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 365 | +0.279 | -27.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 365 | +0.279 | -27.34€ | 0 | 4 |
| ✅ GBM_LATE_15M | 6249 | +0.049 | +1935.47€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 6249 | +0.049 | +1935.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 843 | +0.176 | +534.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 843 | +0.176 | +534.73€ | 0 | 17 |
| ✅ GBM_LATE_15M#BTC | 841 | +0.170 | +462.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 841 | +0.170 | +462.75€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 853 | +0.191 | +587.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 853 | +0.191 | +587.35€ | 0 | 17 |
| ✅ GBM_LATE_15M#ETH | 975 | -0.055 | -10.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 975 | -0.055 | -10.90€ | 3 | 3 |
| ✅ GBM_LATE_15M#SOL | 1203 | -0.036 | +139.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1203 | -0.036 | +139.68€ | 4 | 3 |
| ✅ GBM_LATE_15M#XRP | 1534 | -0.035 | +221.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1534 | -0.035 | +221.85€ | 4 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 7197 | +0.043 | +2710.25€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 7197 | +0.043 | +2710.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1126 | -0.028 | +510.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1126 | -0.028 | +510.46€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1553 | -0.038 | +148.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1553 | -0.038 | +148.07€ | 1 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 717 | +0.241 | +658.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 717 | +0.241 | +658.57€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1259 | -0.040 | +16.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1259 | -0.040 | +16.83€ | 9 | 1 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1314 | -0.009 | +270.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1314 | -0.009 | +270.88€ | 4 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1228 | +0.235 | +1105.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1228 | +0.235 | +1105.44€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 4869 | +0.171 | +3325.78€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 4869 | +0.171 | +3325.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 634 | +0.193 | +466.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 634 | +0.193 | +466.11€ | 0 | 16 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 803 | +0.163 | +516.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 803 | +0.163 | +516.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 630 | +0.201 | +486.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 630 | +0.201 | +486.64€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 779 | +0.173 | +520.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 779 | +0.173 | +520.73€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 953 | +0.108 | +507.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 953 | +0.108 | +507.66€ | 1 | 17 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1070 | +0.197 | +827.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1070 | +0.197 | +827.71€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 791 | +0.071 | +132.21€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 791 | +0.071 | +132.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 196 | +0.106 | +60.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 196 | +0.106 | +60.81€ | 2 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 174 | +0.176 | +58.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 174 | +0.176 | +58.12€ | 1 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 272 | -0.015 | -0.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 272 | -0.015 | -0.29€ | 4 | 4 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO | 5667 | +0.162 | +3583.89€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#15min | 5667 | +0.162 | +3583.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 807 | +0.182 | +553.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 807 | +0.182 | +553.90€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 923 | +0.160 | +560.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 923 | +0.160 | +560.22€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 798 | +0.216 | +655.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 798 | +0.216 | +655.60€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 783 | +0.133 | +391.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 783 | +0.133 | +391.82€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1014 | +0.090 | +448.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1014 | +0.090 | +448.08€ | 0 | 14 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1342 | +0.191 | +974.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1342 | +0.191 | +974.28€ | 0 | 26 |
| ✅ GBM_LATE_5M | 703 | +0.120 | +299.80€ | 1 | 22 |
| ✅ GBM_LATE_5M#5min | 703 | +0.120 | +299.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 322 | +0.136 | +175.07€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 322 | +0.136 | +175.07€ | 2 | 20 |
| ✅ GBM_LATE_5M#DOGE | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 155 | +0.169 | +72.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 155 | +0.169 | +72.28€ | 1 | 22 |
| ✅ GBM_LATE_5M#SOL | 89 | -0.038 | +1.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 89 | -0.038 | +1.15€ | 2 | 1 |
| ✅ GBM_LATE_5M#XRP | 124 | +0.159 | +55.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 124 | +0.159 | +55.72€ | 0 | 0 |
| ✅ GBM_LATE_60M | 501 | -0.045 | +74.00€ | 4 | 8 |
| ✅ GBM_LATE_60M#60min | 501 | -0.045 | +74.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 173 | -0.003 | +5.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 173 | -0.003 | +5.67€ | 2 | 3 |
| ✅ GBM_LATE_60M#ETH | 177 | -0.020 | +44.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 177 | -0.020 | +44.02€ | 3 | 8 |
| ✅ GBM_LATE_60M#SOL | 151 | -0.121 | +24.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 151 | -0.121 | +24.30€ | 3 | 2 |
| 🚫 GBM_LATE_60M_FADE | 193 | -0.305 | -34.48€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 193 | -0.305 | -34.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 52 | -0.296 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 52 | -0.296 | -8.07€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 311 | +0.040 | +5.51€ | 1 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 311 | +0.040 | +5.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 121 | +0.012 | +3.09€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 121 | +0.012 | +3.09€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 74 | +0.092 | +5.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 74 | +0.092 | +5.73€ | 0 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LEADLAG_BTC_XRP_15M | 214 | +0.093 | +38.26€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 214 | +0.093 | +38.26€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 214 | +0.093 | +38.26€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 214 | +0.093 | +38.26€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 213 | -0.105 | -27.93€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 213 | -0.105 | -27.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 52 | -0.111 | -7.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 52 | -0.111 | -7.62€ | 2 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 44 | -0.043 | -3.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 430 | -0.058 | -30.45€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 430 | -0.058 | -30.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 20 | +0.000 | -0.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 20 | +0.000 | -0.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 78 | -0.113 | -9.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 78 | -0.113 | -9.93€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 47 | -0.051 | -3.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 47 | -0.051 | -3.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 129 | -0.019 | -3.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 129 | -0.019 | -3.27€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#SOL | 109 | -0.032 | -5.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 109 | -0.032 | -5.59€ | 1 | 1 |
| ✅ LIQUIDACIONES_5M#XRP | 47 | -0.153 | -8.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 47 | -0.153 | -8.10€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 373 | -0.020 | -11.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 373 | -0.020 | -11.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 119 | -0.045 | -11.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 119 | -0.045 | -11.97€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 120 | -0.025 | -2.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 120 | -0.025 | -2.65€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 134 | +0.007 | +2.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 134 | +0.007 | +2.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 2974 | +0.006 | -29.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 2974 | +0.006 | -29.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 267 | +0.006 | +8.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 267 | +0.006 | +8.46€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M#BTC | 556 | +0.013 | -4.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 556 | +0.013 | -4.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 465 | +0.001 | -16.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 465 | +0.001 | -16.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 570 | +0.018 | +19.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 570 | +0.018 | +19.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 535 | -0.005 | -22.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 535 | -0.005 | -22.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 581 | +0.003 | -13.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 581 | +0.003 | -13.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 4344 | -0.034 | +108.88€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 4344 | -0.034 | +108.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 679 | -0.043 | +54.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 679 | -0.043 | +54.16€ | 4 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 779 | -0.029 | -21.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 779 | -0.029 | -21.83€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 691 | -0.031 | +108.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 691 | -0.031 | +108.43€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 781 | -0.022 | -17.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 781 | -0.022 | -17.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 709 | -0.050 | -0.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 709 | -0.050 | -0.92€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 705 | -0.030 | -13.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 705 | -0.030 | -13.77€ | 5 | 0 |
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
| ✅ MOMENTUM_IBS_5M | 2139 | +0.007 | +5.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 2139 | +0.007 | +5.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 575 | +0.022 | +16.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 575 | +0.022 | +16.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 939 | +0.007 | +0.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 939 | +0.007 | +0.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 11841 | -0.071 | +217.31€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 11841 | -0.071 | +217.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 1789 | -0.094 | +186.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 1789 | -0.094 | +186.43€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 2250 | -0.056 | +23.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 2250 | -0.056 | +23.75€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 1852 | -0.082 | +36.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 1852 | -0.082 | +36.38€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 1823 | -0.100 | -170.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 1823 | -0.100 | -170.20€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 2164 | -0.049 | +30.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 2164 | -0.049 | +30.64€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 1963 | -0.057 | +110.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 1963 | -0.057 | +110.31€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6004 | -0.010 | -119.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6004 | -0.010 | -119.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1197 | +0.000 | -14.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1197 | +0.000 | -14.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1000 | -0.019 | -29.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1000 | -0.019 | -29.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 342 | +0.084 | +66.36€ | 1 | 3 |
| ✅ ORDER_FLOW_5M#5min | 206 | +0.101 | +53.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 62 | +0.125 | +27.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 62 | +0.125 | +27.34€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 35 | +0.095 | +7.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 35 | +0.095 | +7.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 26 | +0.071 | +4.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 26 | +0.071 | +4.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 37 | +0.090 | +5.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 37 | +0.090 | +5.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 46 | +0.083 | +8.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 46 | +0.083 | +8.01€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM | 240 | -0.165 | -21.98€ | 2 | 1 |
| 🚫 PRICE_TARGET_GBM#BTC | 104 | -0.226 | -30.78€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 91 | -0.242 | -27.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 93 | -0.153 | -4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 77 | -0.158 | -5.62€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 16 | -0.089 | +0.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 43 | -0.033 | +13.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 38 | +0.000 | +14.95€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 206 | -0.168 | -18.49€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 34 | -0.139 | -3.50€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 156 | -0.177 | +21.99€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 68 | -0.114 | +13.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 66 | -0.103 | +14.86€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 63 | -0.238 | -5.88€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 60 | -0.226 | -3.33€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 25 | -0.167 | +14.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 24 | -0.154 | +14.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 150 | -0.165 | +26.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 6 | -0.113 | -4.08€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 119 | -0.045 | -15.95€ | 5 | 1 |
| ✅ STREAK_FADE_15M#15min | 119 | -0.045 | -15.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 51 | -0.028 | -7.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 51 | -0.028 | -7.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 10 | +0.042 | +0.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 10 | +0.042 | +0.95€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 49 | -0.088 | -8.96€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 49 | -0.088 | -8.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 741 | -0.001 | -20.28€ | 1 | 0 |
| ✅ STREAK_FADE_5M#5min | 741 | -0.001 | -20.28€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 254 | +0.008 | -2.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 254 | +0.008 | -2.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 245 | +0.014 | -2.66€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 245 | +0.014 | -2.66€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 96 | +0.000 | -3.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 96 | +0.000 | -3.48€ | 3 | 2 |
| ✅ STREAK_FADE_5M#XRP | 146 | -0.041 | -11.49€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 146 | -0.041 | -11.49€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 26 | -0.107 | -3.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 26 | -0.107 | -3.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 16 | -0.133 | -3.24€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 16 | -0.133 | -3.24€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 10 | +0.000 | -0.15€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 10 | +0.000 | -0.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 1438 | +0.018 | +9.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 1438 | +0.018 | +9.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 476 | +0.021 | +2.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 476 | +0.021 | +2.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 250 | +0.000 | -2.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 250 | +0.000 | -2.76€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 435 | +0.006 | -4.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 435 | +0.006 | -4.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 277 | +0.048 | +14.01€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 277 | +0.048 | +14.01€ | 2 | 3 |
| ✅ STRUCT_NO_15M | 2699 | +0.002 | -42.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 2699 | +0.002 | -42.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1033 | +0.005 | -13.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1033 | +0.005 | -13.40€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1039 | +0.007 | -10.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1039 | +0.007 | -10.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 627 | -0.013 | -18.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 627 | -0.013 | -18.21€ | 2 | 0 |
| ✅ UPDOWN_GBM | 4501 | +0.010 | +135.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1790 | +0.048 | +173.59€ | 0 | 6 |
| ✅ UPDOWN_GBM#240min | 195 | +0.028 | +3.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 2142 | -0.015 | -37.63€ | 3 | 0 |
| ✅ UPDOWN_GBM#60min | 327 | -0.011 | -3.63€ | 4 | 0 |
| ✅ UPDOWN_GBM#BNB | 173 | +0.071 | +26.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 160 | +0.093 | +29.46€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 951 | +0.023 | +49.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 189 | +0.071 | +17.03€ | 4 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 58 | +0.100 | +7.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 578 | +0.017 | +29.39€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 108 | -0.045 | -6.52€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 557 | +0.008 | +7.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 103 | +0.090 | +23.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 450 | -0.011 | -15.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1006 | +0.014 | +21.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 467 | +0.044 | +30.41€ | 1 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 58 | +0.083 | +4.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 330 | -0.033 | -16.31€ | 6 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 136 | +0.022 | +3.23€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1029 | -0.005 | -11.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 391 | +0.004 | -4.29€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 44 | -0.043 | -4.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 499 | -0.001 | -2.29€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 83 | -0.018 | -0.34€ | 1 | 3 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 783 | +0.001 | +43.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 480 | +0.054 | +77.51€ | 0 | 6 |
| ✅ UPDOWN_GBM#XRP#240min | 27 | -0.121 | -4.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 276 | -0.079 | -30.11€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 160 | +0.284 | +13.57€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 160 | +0.284 | +13.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 93 | +0.258 | -0.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 93 | +0.258 | -0.61€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 67 | +0.312 | +14.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 67 | +0.312 | +14.18€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 2941 | -0.084 | +383.37€ | 4 | 3 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 2941 | -0.084 | +383.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 246 | -0.085 | +113.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 246 | -0.085 | +113.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 606 | -0.160 | -62.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 606 | -0.160 | -62.71€ | 4 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 68 | +0.043 | +8.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 68 | +0.043 | +8.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 193 | +0.049 | +48.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 193 | +0.049 | +48.75€ | 2 | 15 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 937 | -0.066 | +178.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 937 | -0.066 | +178.08€ | 2 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 891 | -0.089 | +97.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 891 | -0.089 | +97.16€ | 5 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 20 | -0.091 | -2.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 20 | -0.091 | -2.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 20 | -0.091 | -2.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 20 | -0.091 | -2.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 238 | +0.267 | +156.70€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 238 | +0.267 | +156.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 134 | +0.250 | +74.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 134 | +0.250 | +74.13€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 104 | +0.283 | +82.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 104 | +0.283 | +82.57€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 368 | -0.062 | -28.63€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 368 | -0.062 | -28.63€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 233 | -0.006 | -11.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 233 | -0.006 | -11.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 23 | +0.020 | +3.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 23 | +0.020 | +3.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 26 | -0.179 | -5.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 26 | -0.179 | -5.17€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 29 | -0.177 | -4.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1029 | +0.288 | +420.68€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 307 | +0.202 | +0.48€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 320 | +0.258 | +71.68€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 402 | +0.374 | +348.52€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.095) — sin ventaja clara. oversold(IBS<0.3): IC=-0.005 n=1542 | neutral: IC=+0.008 n=1635 | overbought(IBS>0.7): IC=+0.089 n=1837
  - _Datos_: n=5277 IC=+0.033 PNL=+371.51€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 5 celda(s) pasan gate riguroso completo de 175 evaluadas (n>=40) y 515 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.004 < 0.08 — monitorear
  - _Datos_: n=391 IC=+0.004 PNL=-4.29€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=320/15 IC=+0.258 PNL=+71.68€ | BTC: n=307/15 IC=+0.202 PNL=+0.48€ | SOL: n=402/15 IC=+0.374 PNL=+348.52€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.081 n=73563 | tras_1loss IC=+0.045 n=56556 | tras_2loss IC=+0.008 n=25696/40 | gap=+0.073 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 17 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL
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
  - _Estado_: 4439 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.136 n=31/60 | contraria IC=-0.045 n=18 | gap=+0.181 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=40, boost estimado=+0.002. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 37/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=136/40 IC=+0.022 PNL=+3.23€ | BTC#60min: n=108/40 IC=-0.045 PNL=-6.52€ | SOL#60min: n=83/40 IC=-0.018 PNL=-0.34€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.008 n=437 | contrario_BTC IC=+0.015 n=334/40 | gap=+0.023 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=69 PNL=+33.14€
  - _Datos_: n=69 IC=+0.162 PNL=+33.14€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.08 con n=87 PNL=+20.86€
  - _Datos_: n=87 IC=+0.129 PNL=+20.86€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 10/25 ops en el filtro definido (IC actual=+0.167 PNL=+9.17€)
  - _Datos_: n=10 IC=+0.167 PNL=+9.17€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=874 PNL=+424.44€
  - _Datos_: n=874 IC=+0.335 PNL=+424.44€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=38 IC=+0.050 PNL=+10.89€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=38 IC=+0.050 PNL=+10.89€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 12/30 ops en el filtro definido (IC actual=+0.043 PNL=+0.77€)
  - _Datos_: n=12 IC=+0.043 PNL=+0.77€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=4260 IC=+0.006 PNL=+84.95€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=4260 IC=+0.006 PNL=+84.95€

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
  - _Estado_: n=267 IC=+0.009 PNL=+3.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=267 IC=+0.009 PNL=+3.24€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=60 IC=-0.097 PNL=-6.87€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=60 IC=-0.097 PNL=-6.87€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=78 IC=-0.013 PNL=-0.33€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=78 IC=-0.013 PNL=-0.33€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.1 con n=478 PNL=+90.70€
  - _Datos_: n=478 IC=+0.108 PNL=+90.70€

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
  - _Estado_: n=189 IC=+0.071 PNL=+17.03€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=189 IC=+0.071 PNL=+17.03€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=1070 IC=+0.037 PNL=+67.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1070 IC=+0.037 PNL=+67.96€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 16/30 ops en el filtro definido (IC actual=-0.178 PNL=-2.92€)
  - _Datos_: n=16 IC=-0.178 PNL=-2.92€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=49 IC=+0.069 PNL=+14.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=49 IC=+0.069 PNL=+14.01€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=56 IC=+0.052 PNL=+7.70€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=56 IC=+0.052 PNL=+7.70€

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
  - _Estado_: n=1427 IC=-0.016 PNL=-41.89€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1427 IC=-0.016 PNL=-41.89€

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
  - _Estado_: n=1197 IC=+0.027 PNL=+78.27€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1197 IC=+0.027 PNL=+78.27€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=397 IC=+0.029 PNL=-5.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=397 IC=+0.029 PNL=-5.11€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.08 con n=63 PNL=+18.83€
  - _Datos_: n=63 IC=+0.131 PNL=+18.83€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.08 con n=103 PNL=-0.50€
  - _Datos_: n=103 IC=+0.157 PNL=-0.50€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=101 PNL=+23.10€
  - _Datos_: n=101 IC=+0.112 PNL=+23.10€

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
  - _Estado_: n=606 IC=+0.026 PNL=+35.95€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=606 IC=+0.026 PNL=+35.95€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.02 con n=174 PNL=+50.21€
  - _Datos_: n=174 IC=+0.131 PNL=+50.21€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=87 IC=-0.129 PNL=+13.53€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=87 IC=-0.129 PNL=+13.53€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.441 > 0.1 con n=569 PNL=+467.91€
  - _Datos_: n=569 IC=+0.441 PNL=+467.91€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1258 IC=+0.025 PNL=+60.14€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1258 IC=+0.025 PNL=+60.14€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.159 > 0.1 con n=701 PNL=+238.33€
  - _Datos_: n=701 IC=+0.159 PNL=+238.33€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 15/40 ops en el filtro definido (IC actual=-0.199 PNL=-3.78€)
  - _Datos_: n=15 IC=-0.199 PNL=-3.78€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=349 IC=+0.041 PNL=+41.98€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=349 IC=+0.041 PNL=+41.98€

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
  - _Estado_: n=56 IC=+0.069 PNL=-2.41€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=56 IC=+0.069 PNL=-2.41€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=3111 IC=-0.122 PNL=+367.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3111 IC=-0.122 PNL=+367.40€

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
  - _Estado_: n=493 IC=+0.134 PNL=+176.37€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=493 IC=+0.134 PNL=+176.37€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.08 con n=478 PNL=+90.70€
  - _Datos_: n=478 IC=+0.108 PNL=+90.70€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=461 IC=+0.010 PNL=+5.63€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=461 IC=+0.010 PNL=+5.63€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.093 > 0.08 con n=509 PNL=+297.58€
  - _Datos_: n=509 IC=+0.093 PNL=+297.58€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.08 con n=127 PNL=+21.64€
  - _Datos_: n=127 IC=+0.136 PNL=+21.64€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=306 PNL=-19.38€
  - _Datos_: n=306 IC=-0.224 PNL=-19.38€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=854 IC=+0.158 PNL=+480.31€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=854 IC=+0.158 PNL=+480.31€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 17/40 ops en el filtro definido (IC actual=+0.022 PNL=-1.83€)
  - _Datos_: n=17 IC=+0.022 PNL=-1.83€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=506 IC=-0.034 PNL=+10.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=506 IC=-0.034 PNL=+10.49€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.08 con n=450 PNL=+246.25€
  - _Datos_: n=450 IC=+0.177 PNL=+246.25€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=817 IC=-0.031 PNL=+118.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=817 IC=-0.031 PNL=+118.11€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.08 con n=217 PNL=-27.08€
  - _Datos_: n=217 IC=+0.121 PNL=-27.08€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.246 > 0.08 con n=1114 PNL=-97.15€
  - _Datos_: n=1114 IC=+0.246 PNL=-97.15€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 7/40 ops en el filtro definido (IC actual=+0.019 PNL=+3.02€)
  - _Datos_: n=7 IC=+0.019 PNL=+3.02€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.088 n=112) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=112 IC=+0.088 PNL=+14.03€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.341 > 0.08 con n=61 PNL=+46.09€
  - _Datos_: n=61 IC=+0.341 PNL=+46.09€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.435 n=214) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=214 IC=+0.435 PNL=+289.06€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=2256 IC=+0.126 PNL=-420.55€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=2256 IC=+0.126 PNL=-420.55€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 30/40 ops en el filtro definido (IC actual=+0.219 PNL=+21.61€)
  - _Datos_: n=30 IC=+0.219 PNL=+21.61€
