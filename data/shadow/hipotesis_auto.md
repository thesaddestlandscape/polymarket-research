# Hipótesis automáticas — 2026-08-25 15:19 UTC
_Generado por shadow_postmortem.py sobre 151947 resoluciones (PNL=+10112.81€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.167 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.272 (n=217)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.377 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=215)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.288 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.145)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `n_ballena_banda` > 20.0 (IC base=+0.145)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.235 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 58.0 (IC base=+0.145)

- **PATRÓN** `banda_hit_calibrado` > `0.8208` → IC=+0.276 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8208 (IC base=+0.145)

- **PATRÓN** `banda_z` > `10.241` → IC=+0.247 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.241 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=238)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3473.3708` → IC=+0.234 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3473.3708 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.5 (IC base=+0.018)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.725` → IC=+0.292 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.184)

- **PATRÓN** `n_ballena_banda` > `21.0` → IC=+0.201 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 21.0 (IC base=+0.184)

- **PATRÓN** `n_total_lado` > `59.0` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 59.0 (IC base=+0.184)

- **PATRÓN** `banda_hit_calibrado` > `0.8205` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8205 (IC base=+0.184)

- **PATRÓN** `banda_z` > `11.467` → IC=+0.260 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.467 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.218 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=168)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `3111.6433` → IC=+0.235 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3111.6433 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `296.0` → IC=+0.321 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 296.0 (IC base=+0.184)

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

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.078)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.078)

- **PATRÓN** `banda_z` > `8.174` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `banda_z` > 8.174 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `148.86` → IC=-0.278 (n=2132)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 148.86
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=6396)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `n_ballenas` < `6.0` → IC=-0.167 (n=163)

  - _Acción_: SKIP cuando `n_ballenas` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=492)

- **FILTRO** `restante_s_al_confirmar` < `380.16` → IC=-0.282 (n=163)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 380.16
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=492)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `84.18` → IC=-0.449 (n=253)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 84.18
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=761)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `158.28` → IC=-0.197 (n=575)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.28
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1725)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `150.33` → IC=-0.280 (n=521)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 150.33
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1564)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.92` → IC=-0.337 (n=490)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.92
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=996)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.190 (n=4932)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=1491)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2376.0723` → IC=+0.177 (n=1440)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2376.0723 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=3132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=3874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.258 (n=2993)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=2768)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `1813.8317` → IC=+0.177 (n=2307)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1813.8317 (IC base=+0.139)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.400 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.217 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `11938.9123` → IC=+0.217 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11938.9123 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.193 (n=523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.190 (n=404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.286 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=750)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `11725.4851` → IC=+0.189 (n=194)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 11725.4851 (IC base=+0.183)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=443)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.142 (n=515)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.555 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `4978.014` → IC=+0.163 (n=200)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4978.014 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.210 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.415` → IC=+0.182 (n=294)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.415 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4247.4138` → IC=+0.158 (n=276)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4247.4138 (IC base=+0.139)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.131 (n=717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.306 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.289 (n=434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.284)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.329 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.284 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2826.4245` → IC=+0.298 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2826.4245 (IC base=+0.284)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` > `0.66` → IC=+0.262 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.66 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=381)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2043.1794` → IC=+0.166 (n=306)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2043.1794 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4420.281 (IC base=+0.080)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=756)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.445 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.348 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.227 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `840.3405` → IC=+0.231 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 840.3405 (IC base=+0.217)

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

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.217 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=272)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.102)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.292 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=87)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=126)

- **FILTRO** `libro_liquidez` < `7404.7045` → IC=-0.248 (n=117)

  - _Acción_: SKIP cuando `libro_liquidez` < 7404.7045
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=40)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=4160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=3599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.202 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `3258.7888` → IC=+0.354 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3258.7888 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=1033)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.190 (n=1010)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.73 (IC base=+0.171)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

- **FILTRO** `py_entrada` > `0.795` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=52)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.326)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.326)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.326)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.173 (n=387)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.7 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.167 (n=542)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.73 (IC base=+0.161)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=948)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.232 (n=818)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.314 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.232)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=1013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=882)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=703)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.453 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.452 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `3299.2146` → IC=+0.464 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3299.2146 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.450 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.445 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.455 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `12146.257` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12146.257 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.441 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` < `0.91` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.91 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.423 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.423 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `3624.439` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3624.439 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.457 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.92` → IC=+0.436 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.92 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.433 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=10793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=7246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.222 (n=7612)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=2082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.133 (n=1340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 11.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.160 (n=1437)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.71 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.270 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.236)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.169 (n=1248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.213 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=1716)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=1144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.289 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.234)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=1163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.248 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=1223)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.234 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.188)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=1499)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.131)

- **PATRÓN** `restante_min` < `3.92` → IC=+0.139 (n=1301)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 3.92 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.92` → IC=+0.158 (n=1388)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.92 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.150 (n=1755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `4.54` → IC=+0.157 (n=1295)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 4.54 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.139)

- **PATRÓN** `restante_min` < `3.88` → IC=+0.145 (n=648)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` < 3.88 (IC base=+0.139)

- **PATRÓN** `restante_min` > `4.9` → IC=+0.172 (n=669)

  - _Acción_: Kelly boost +0.86€ cuando `restante_min` > 4.9 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.162 (n=866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `lag_apertura_s` < `5.83` → IC=+0.174 (n=643)

  - _Acción_: Kelly boost +0.87€ cuando `lag_apertura_s` < 5.83 (IC base=+0.139)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.190 (n=653)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.37 (IC base=+0.122)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.137 (n=657)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 3.95 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.154 (n=701)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=2043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.47` → IC=+0.156 (n=652)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 3.47 (IC base=+0.122)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.303 (n=500)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.379 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.300)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.286 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.281 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5612.6302` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5612.6302 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.337 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.303)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.310 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.303)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.303)

- **PATRÓN** `libro_liquidez` > `1876.0591` → IC=+0.324 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1876.0591 (IC base=+0.303)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.419 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.420 (n=236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.418 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.423 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.409)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.408 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.409)

- **PATRÓN** `libro_liquidez` > `1864.6918` → IC=+0.422 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1864.6918 (IC base=+0.409)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.415 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.425 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.411 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.417 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.406)

- **PATRÓN** `libro_liquidez` > `5705.9228` → IC=+0.444 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5705.9228 (IC base=+0.406)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.420 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.420 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `1921.0334` → IC=+0.438 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1921.0334 (IC base=+0.415)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.300 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.434 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.310 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `821.9118` → IC=+0.298 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 821.9118 (IC base=+0.284)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.300 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.434 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.310 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `821.9118` → IC=+0.298 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 821.9118 (IC base=+0.284)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9448` → IC=+0.220 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9448 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1937` → IC=+0.235 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1937 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.7404` → IC=+0.225 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7404 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.071` → IC=+0.184 (n=815)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.071 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `0.6372` → IC=+0.229 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6372 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.262 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.134 (n=981)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.3067` → IC=+0.153 (n=142)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.3067 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.5817` → IC=+0.146 (n=453)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5817 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.4596` → IC=+0.134 (n=1028)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4596 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2129` → IC=+0.124 (n=1371)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2129 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1787` → IC=+0.150 (n=664)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1787 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.151 (n=227)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6279 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `1.0494` → IC=+0.145 (n=308)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0494 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1726` → IC=+0.252 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1726 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.6146` → IC=+0.218 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6146 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.9394` → IC=+0.228 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9394 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.267 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.028)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.189 (n=149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0075 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.181 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.377` → IC=+0.339 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.377 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.152 (n=340)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.06 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.319 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.336 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.2028` → IC=+0.331 (n=187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2028 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.301 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.289)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.319 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` < `0.0622` → IC=+0.315 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0622 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` < `1.7889` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7889 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` > `1.4634` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4634 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.340 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1989.8695` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1989.8695 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.289)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.273 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.221 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.9595` → IC=+0.248 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9595 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.2322` → IC=+0.238 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2322 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `1.0239` → IC=+0.222 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.0239 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.375` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.375 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.294` → IC=+0.220 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.294 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `1.1082` → IC=+0.255 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1082 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` < `0.0769` → IC=+0.226 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0769 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2704` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2704 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.258 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `12448.5931` → IC=+0.239 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12448.5931 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `369.0` → IC=+0.218 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 369.0 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.186 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0021 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1658` → IC=+0.152 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1658 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.143 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.147 (n=415)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.4191` → IC=+0.170 (n=349)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.4191 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1939` → IC=+0.168 (n=341)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1939 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.989` → IC=+0.232 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.989 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.174 (n=133)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6279 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.0218` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.0218 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.094` → IC=+0.218 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.094 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.7548` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.7548 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4122` → IC=+0.158 (n=293)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4122 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=512)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `13845.8953` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 13845.8953 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 233.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.192 (n=131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0075 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0861` → IC=+0.129 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.0861 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.923` → IC=+0.280 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.923 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.4203` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.4203 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=185)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `1917.67` → IC=+0.144 (n=178)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1917.67 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 27.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.315 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0885` → IC=+0.304 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0885 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.284 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.294 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.311 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.008` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.008 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.4178` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.4178 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` < `2.0261` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0261 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.8959` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8959 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.239 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.277)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.8786` → IC=-0.182 (n=177)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8786
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=532)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.139 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=650)

- **PATRÓN** `dist_vwap_pct` < `0.0784` → IC=+0.346 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0784 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` > `0.8071` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8071 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1238` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1238 (IC base=-0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.0641` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0641 (IC base=-0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.5868` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5868 (IC base=-0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.1413` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1413 (IC base=-0.060)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `ibs_20min` > `0.48` → IC=-0.120 (n=601)

  - _Acción_: SKIP cuando `ibs_20min` > 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=603)

- **FILTRO** `sigma_ewma_delta_pct` > `4.908` → IC=-0.147 (n=259)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.908
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=945)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.204 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.074)

- **PATRÓN** `drift_60min` |x|≤ `0.461` → IC=+0.136 (n=75)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.461 (IC base=+0.074)

- **PATRÓN** `hora_utc` > `23.0` → IC=+0.250 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 23.0 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.5263` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.5263 (IC base=+0.074)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `sigma_h` > `0.0246` → IC=-0.147 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0246
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=454)

- **FILTRO** `ibs_20min` < `0.4437` → IC=-0.151 (n=302)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4437
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=303)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=93)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=512)

- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.170 (n=268)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=806)

- **FILTRO** `sigma_ewma_delta_pct` > `6.547` → IC=-0.183 (n=178)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.547
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=896)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.077)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6932 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` < `0.2029` → IC=+0.229 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2029 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6961 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` > `1.1355` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1355 (IC base=-0.035)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.133 (n=1146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0073 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.9462` → IC=+0.248 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9462 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `1.2364` → IC=+0.285 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2364 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.084` → IC=+0.123 (n=1003)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 5.084 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.1691` → IC=+0.198 (n=293)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 1.1691 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` < `0.1152` → IC=+0.164 (n=1101)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.1152 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2434` → IC=+0.223 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2434 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.4852` → IC=+0.182 (n=379)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4852 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` > `2.8755` → IC=+0.174 (n=378)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.8755 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.269 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.097` → IC=+0.174 (n=1096)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.097 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.6407` → IC=+0.219 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6407 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` < `0.1458` → IC=+0.194 (n=651)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1458 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.6318` → IC=+0.206 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6318 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2479` → IC=+0.341 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2479 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `2.9138` → IC=+0.278 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9138 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.251 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.036)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.936` → IC=-0.214 (n=110)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.936
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=552)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.885` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 4.885 (IC base=-0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.0542` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0542 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `2.317` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.317 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `1.1167` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 1.1167 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` > `0.9983` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.9983 (IC base=-0.041)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.292 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0614` → IC=+0.221 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0614 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.263 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.932` → IC=+0.303 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.932 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.1458` → IC=+0.185 (n=277)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1458 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.425` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.425 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `2.0881` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.0881 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `3.8995` → IC=+0.210 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.8995 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `1912.1779` → IC=+0.203 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.1779 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.416 (n=81)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.370)

- **PATRÓN** `drift_60min` |x|≤ `0.1847` → IC=+0.376 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1847 (IC base=+0.370)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.393 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.370)

- **PATRÓN** `ibs_20min` < `0.3056` → IC=+0.383 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3056 (IC base=+0.370)

- **PATRÓN** `volumen_pendiente_norm` < `0.1035` → IC=+0.391 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1035 (IC base=+0.370)

- **PATRÓN** `volumen_pendiente_norm` > `0.3816` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3816 (IC base=+0.370)

- **PATRÓN** `volumen_spike_ratio` < `2.9594` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9594 (IC base=+0.370)

- **PATRÓN** `libro_liquidez` > `1881.0184` → IC=+0.403 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.0184 (IC base=+0.370)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.159 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=282)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.151 (n=61)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=857)

- **PATRÓN** `dist_vwap_pct` > `0.6615` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6615 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.3934` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3934 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `2.091` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.091 (IC base=-0.067)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.5294` → IC=-0.144 (n=282)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5294
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=286)

- **FILTRO** `ibs_20min` > `0.7391` → IC=-0.159 (n=212)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7391
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=644)

- **FILTRO** `dist_vwap_pct` > `0.1358` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1358
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=50)

- **FILTRO** `volumen_regimen` > `1.3709` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3709
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=50)

- **FILTRO** `volumen_spike_ratio` < `2.3381` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.3381
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **PATRÓN** `ibs_20min` > `0.85` → IC=+0.250 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.85 (IC base=-0.004)

- **PATRÓN** `dist_vwap_pct` > `0.3189` → IC=+0.263 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3189 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.639` → IC=+0.150 (n=161)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.639 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2631` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2631 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.4987` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4987 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.586` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.586 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.209 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.227 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.288 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `1.2861` → IC=+0.333 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2861 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.128` → IC=+0.271 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.128 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `0.8361` → IC=+0.246 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8361 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.0805` → IC=+0.210 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0805 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.276 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4159` → IC=+0.234 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4159 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2658.4002` → IC=+0.230 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2658.4002 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.277 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0212` → IC=+0.271 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0212 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.431` → IC=+0.269 (n=457)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.431 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.2727` → IC=+0.317 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2727 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` < `0.244` → IC=+0.270 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.244 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.5` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.5 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.001` → IC=+0.260 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.001 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` > `1.2535` → IC=+0.300 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2535 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.354 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.1847` → IC=+0.281 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1847 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.242 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.259)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.184 (n=1449)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0066 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.8942` → IC=+0.261 (n=1446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8942 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.7869` → IC=+0.251 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7869 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.233` → IC=+0.259 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.233 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.2354` → IC=+0.164 (n=1511)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2354 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.8611` → IC=+0.180 (n=1007)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.8611 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.104` → IC=+0.189 (n=772)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.104 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.2957` → IC=+0.159 (n=1691)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.2957 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=1770)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3723.8216` → IC=+0.201 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3723.8216 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.184 (n=950)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 135.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.203 (n=1670)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3742` → IC=+0.199 (n=1897)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3742 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.207 (n=962)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.186 (n=916)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.240 (n=1898)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2104` → IC=+0.179 (n=1563)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2104 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.806` → IC=+0.206 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.806 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.164 (n=1576)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1737 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.8545` → IC=+0.175 (n=1051)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8545 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2433` → IC=+0.227 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2433 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.5782` → IC=+0.182 (n=568)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5782 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6536` → IC=+0.199 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6536 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.172 (n=856)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 218.0 (IC base=+0.183)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.222 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.482` → IC=+0.360 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.482 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1404` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1404 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4177` → IC=+0.134 (n=266)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4177 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.185 (n=277)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.06 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.304 (n=100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.308 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.2245` → IC=+0.327 (n=131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2245 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.343 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.0253` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0253 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.639` → IC=+0.302 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.639 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.0812` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0812 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.1762` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1762 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.8142` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8142 (IC base=+0.290)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1978.9302` → IC=+0.365 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.9302 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.290)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.248 (n=101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.209 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.5086` → IC=+0.226 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5086 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.2046` → IC=+0.255 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2046 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.777` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.777 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.3058` → IC=+0.190 (n=301)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.3058 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `0.9007` → IC=+0.209 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9007 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2715` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2715 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.234 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `11833.4765` → IC=+0.219 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11833.4765 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.188 (n=347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0043 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2835` → IC=+0.179 (n=394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.2835 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.170 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.3843` → IC=+0.189 (n=394)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.3843 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1603` → IC=+0.181 (n=380)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1603 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.578` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.578 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.637` → IC=+0.216 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.637 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.212 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.732` → IC=+0.186 (n=192)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.732 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `248.0` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 248.0 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.170 (n=210)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0066 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.144` → IC=+0.153 (n=211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.144 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.212 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.877` → IC=+0.314 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.877 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.2301` → IC=+0.129 (n=254)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.2301 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.0183` → IC=+0.196 (n=113)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.0183 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `3.8997` → IC=+0.144 (n=116)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 3.8997 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `1962.7584` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 1962.7584 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.311 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.339 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.322 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.323 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.093` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.093 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.404` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.404 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` < `4.276` → IC=+0.298 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 4.276 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` > `1.8509` → IC=+0.302 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8509 (IC base=+0.297)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.235 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.5026` → IC=+0.203 (n=301)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5026 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.248 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `1.061` → IC=+0.247 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.061 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.902` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.902 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `0.6382` → IC=+0.212 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6382 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.263 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.4394` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4394 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.4658` → IC=+0.227 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4658 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=337)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `9742.9195` → IC=+0.210 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9742.9195 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.252 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3624` → IC=+0.169 (n=379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3624 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.170 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 14.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.150 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.4496` → IC=+0.196 (n=379)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.4496 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.7604` → IC=+0.156 (n=452)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.7604 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.457` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.457 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8485` → IC=+0.151 (n=253)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8485 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6135` → IC=+0.159 (n=379)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6135 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.083` → IC=+0.133 (n=243)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.083 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1001` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1001 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.8877` → IC=+0.196 (n=182)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.8877 (IC base=+0.143)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.4286` → IC=-0.224 (n=121)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4286
  - _Potencial_: sin este filtro IC_bueno=+0.223 (n=366)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.190 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0099 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.8519` → IC=+0.230 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8519 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.7694` → IC=+0.268 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7694 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.292 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.134 (n=435)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.6182 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2846.759` → IC=+0.195 (n=198)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2846.759 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.196 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0048 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.184 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 14.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.4286` → IC=+0.223 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4286 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2188` → IC=+0.125 (n=331)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.2188 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.673` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 7.673 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` > `0.853` → IC=+0.150 (n=244)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.853 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.1104` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1104 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.2766` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2766 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=314)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `1956.4442` → IC=+0.159 (n=244)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1956.4442 (IC base=+0.112)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0219` → IC=+0.202 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0219 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.1598` → IC=+0.176 (n=211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1598 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.9306` → IC=+0.252 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9306 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.941` → IC=+0.237 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.941 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.037` → IC=+0.246 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.037 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.2221` → IC=+0.171 (n=475)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2221 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.836` → IC=+0.186 (n=317)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.836 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `2.1643` → IC=+0.180 (n=385)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.1643 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8108` → IC=+0.170 (n=292)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8108 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.170 (n=532)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.259 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.3761` → IC=+0.232 (n=386)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3761 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.258 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.1341` → IC=+0.310 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1341 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `1.077` → IC=+0.231 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.077 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.824` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.824 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.7169` → IC=+0.246 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7169 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.7671` → IC=+0.274 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7671 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.191 (n=221)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 30.0 (IC base=+0.222)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.5258` → IC=+0.141 (n=357)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.5258 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.7744` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7744 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.14` → IC=+0.218 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.14 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `2969.2175` → IC=+0.129 (n=238)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2969.2175 (IC base=+0.088)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.236 (n=108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.059)

- **PATRÓN** `ibs_20min` < `0.2708` → IC=+0.141 (n=215)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.2708 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.542` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.542 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `3827.6428` → IC=+0.122 (n=215)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3827.6428 (IC base=+0.059)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=64)

- **FILTRO** `ibs_20min` < `0.3107` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3107
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=69)

- **FILTRO** `volumen_spike_ratio` > `2.223` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.223
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=53)

- **FILTRO** `libro_liquidez` < `5689.8897` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 5689.8897
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=69)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.121 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 9.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` > `0.9061` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9061 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.1862` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1862 (IC base=+0.021)

- **PATRÓN** `libro_liquidez` > `12687.2059` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 12687.2059 (IC base=+0.021)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.250 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.195 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0047 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2802` → IC=+0.208 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2802 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.161 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.178 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 14.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.6346` → IC=+0.195 (n=126)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6346 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.0393` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.0393 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.4984` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4984 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.2377` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.2377 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.817` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.817 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.9027` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9027 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1701` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1701 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5902` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5902 (IC base=+0.163)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `ballena_activa_n` > `147.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 147.0
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.273 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.289 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.224` → IC=+0.276 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.224 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.292 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` > `0.9989` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9989 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` > `0.1417` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1417 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.648` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.648 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` < `0.7015` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7015 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.184` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.184 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `2.3129` → IC=+0.275 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3129 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.9173` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9173 (IC base=+0.259)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.367 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.065)

- **PATRÓN** `drift_60min` |x|≤ `0.3482` → IC=+0.131 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.3482 (IC base=+0.065)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.5743` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.5743 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.025` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 6.025 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `9491.207` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9491.207 (IC base=+0.065)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5417` → IC=-0.208 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5417
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=138)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=82)

- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.125 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.021)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 1.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.5948` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5948 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.856` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.856 (IC base=+0.021)

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
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.203 (n=1141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.9445` → IC=+0.288 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9445 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `1.0494` → IC=+0.255 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0494 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.496` → IC=+0.230 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.496 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.7083` → IC=+0.152 (n=782)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.7083 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.0869` → IC=+0.152 (n=806)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0869 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1658` → IC=+0.181 (n=632)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1658 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.8992` → IC=+0.153 (n=1466)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8992 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=2041)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3097.4289` → IC=+0.192 (n=1140)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3097.4289 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.183 (n=1002)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 173.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.224 (n=1492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.4329` → IC=+0.200 (n=2231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4329 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=1012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=1057)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.244 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5455 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.7104` → IC=+0.177 (n=1839)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.7104 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.25` → IC=+0.201 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.25 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.603` → IC=+0.195 (n=2089)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 2.603 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6226` → IC=+0.175 (n=577)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6226 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `1.1936` → IC=+0.189 (n=577)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.1936 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2339` → IC=+0.252 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2339 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.2558` → IC=+0.200 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2558 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.157 (n=491)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 35.0 (IC base=+0.189)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.007` → IC=+0.208 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.159 (n=282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.949` → IC=+0.283 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.949 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.154` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.154 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.1438` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1438 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.158 (n=308)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.06 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.312 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.288 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.2138` → IC=+0.331 (n=187)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2138 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.296 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.307 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.289)

- **PATRÓN** `ibs_20min` < `0.578` → IC=+0.342 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.578 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` < `0.0645` → IC=+0.310 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0645 (IC base=+0.289)

- **PATRÓN** `volumen_pendiente_norm` > `0.2284` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2284 (IC base=+0.289)

- **PATRÓN** `volumen_spike_ratio` > `1.4411` → IC=+0.302 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4411 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.324 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1990.5404` → IC=+0.349 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1990.5404 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.289)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.184 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.207 (n=131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.3404` → IC=+0.216 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3404 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2594` → IC=+0.248 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2594 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.757` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.757 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6564` → IC=+0.184 (n=131)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6564 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.1073` → IC=+0.194 (n=178)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 1.1073 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1444` → IC=+0.235 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1444 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `2.53` → IC=+0.197 (n=344)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.53 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.4677` → IC=+0.202 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4677 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `11449.08` → IC=+0.204 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11449.08 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.204 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.172 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0057 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3278` → IC=+0.178 (n=395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3278 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.173 (n=411)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 18.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.3703` → IC=+0.209 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3703 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.7428` → IC=+0.176 (n=433)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.7428 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.639` → IC=+0.228 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.639 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.231 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6225 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `1.2206` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.2206 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1498` → IC=+0.287 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1498 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.7476` → IC=+0.213 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7476 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.4115` → IC=+0.189 (n=300)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4115 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=510)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `13110.5319` → IC=+0.179 (n=132)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 13110.5319 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `316.0` → IC=+0.225 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 316.0 (IC base=+0.167)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.257 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.175 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.717` → IC=+0.246 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.717 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.912` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.912 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.2322` → IC=+0.169 (n=258)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.2322 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.1406` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1406 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `3.9028` → IC=+0.170 (n=116)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 3.9028 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.206 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1854.121` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1854.121 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 36.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.332 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.278 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.276 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.276 (n=292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.5597` → IC=+0.339 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5597 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.02` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.02 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.1577` → IC=+0.226 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1577 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.3816` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3816 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `3.6549` → IC=+0.267 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.6549 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.268)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.009` → IC=+0.150 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.009 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.169 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.3491` → IC=+0.193 (n=392)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.3491 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.9062` → IC=+0.214 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9062 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.544` → IC=+0.194 (n=191)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 4.544 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6318` → IC=+0.192 (n=131)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6318 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.2229` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.2229 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4206` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4206 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4459.4354` → IC=+0.219 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4459.4354 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.182 (n=177)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 171.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.234 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.5023` → IC=+0.153 (n=321)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.5023 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.174 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.077` → IC=+0.241 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.077 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.727` → IC=+0.165 (n=338)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.727 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.581` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.581 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.047` → IC=+0.141 (n=293)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.047 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.5857` → IC=+0.161 (n=107)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.5857 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6387` → IC=+0.150 (n=287)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6387 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.264` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.264 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1429` → IC=+0.177 (n=233)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.1429 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4473` → IC=+0.169 (n=264)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4473 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4274.4143` → IC=+0.167 (n=214)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4274.4143 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.218 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 141.0 (IC base=+0.141)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.155 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0104 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.129 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 12.0 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.286 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0166` → IC=+0.268 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0166 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.529` → IC=+0.223 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.529 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2791.9187` → IC=+0.270 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2791.9187 (IC base=+0.087)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.186 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0058 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1512` → IC=+0.147 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1512 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.175 (n=198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.190 (n=427)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5833 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.4697` → IC=+0.129 (n=383)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.4697 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.129 (n=413)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.7028` → IC=+0.137 (n=188)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.7028 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` > `1.1762` → IC=+0.132 (n=142)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.1762 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.4132` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4132 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `1086.3059` → IC=+0.140 (n=381)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1086.3059 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.217 (n=182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.9722` → IC=+0.295 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9722 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `1.3244` → IC=+0.282 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3244 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.053` → IC=+0.253 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.053 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.6183` → IC=+0.185 (n=182)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6183 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `1.0479` → IC=+0.191 (n=247)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.0479 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5675` → IC=+0.173 (n=218)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5675 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.8445` → IC=+0.181 (n=330)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8445 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=607)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3108.1723` → IC=+0.190 (n=182)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3108.1723 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.220 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.309 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.4354` → IC=+0.229 (n=518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4354 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.221 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.49` → IC=+0.275 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.49 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `1.1223` → IC=+0.220 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.1223 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.209` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.209 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.977` → IC=+0.216 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.977 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `1.2349` → IC=+0.247 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2349 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2863` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2863 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.6423` → IC=+0.229 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6423 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.168 (n=308)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 37.0 (IC base=+0.210)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=713)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `1.74` → IC=+0.200 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.74 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `8331.3362` → IC=+0.130 (n=214)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 8331.3362 (IC base=+0.078)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.212 (n=241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.181 (n=481)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.210 (n=222)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.6273` → IC=+0.165 (n=481)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.6273 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6082` → IC=+0.154 (n=163)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.6082 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.7556` → IC=+0.152 (n=602)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.7556 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.913` → IC=+0.172 (n=275)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 2.913 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2654` → IC=+0.169 (n=547)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2654 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.169 (n=267)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.5395` → IC=+0.176 (n=541)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.5395 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=713)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `8241.0265` → IC=+0.164 (n=546)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 8241.0265 (IC base=+0.149)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `dist_vwap_pct` < `0.6194` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6194
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=46)

- **FILTRO** `sigma_ewma_delta_pct` > `3.972` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.972
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=48)

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

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.190 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0038 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.3097` → IC=+0.174 (n=296)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3097 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.260 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.144` → IC=+0.222 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.144 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.6649` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6649 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1975` → IC=+0.154 (n=267)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1975 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.139` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.139 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.160 (n=298)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2467` → IC=+0.164 (n=296)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2467 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.7036` → IC=+0.158 (n=264)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7036 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.199 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.6056` → IC=+0.183 (n=295)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.6056 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `11627.7321` → IC=+0.173 (n=264)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 11627.7321 (IC base=+0.151)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.148 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0094 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.227 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.2829` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2829 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `1.1861` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1861 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.483` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.483 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `1.4092` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.4092 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `7710.7968` → IC=+0.152 (n=159)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7710.7968 (IC base=+0.103)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.254 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.186 (n=116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0065 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.2923` → IC=+0.231 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2923 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.207 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.5833 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.1096` → IC=+0.210 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1096 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` < `0.6774` → IC=+0.186 (n=183)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.6774 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.561` → IC=+0.282 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.561 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.0554` → IC=+0.211 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0554 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.0898` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0898 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `2.1543` → IC=+0.237 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1543 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.4319` → IC=+0.194 (n=171)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4319 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `10240.4839` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 10240.4839 (IC base=+0.175)

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
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.155 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.207 (n=114)

- **FILTRO** `sigma_h` > `0.0111` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=160)

- **FILTRO** `drift_60min` |x|> `0.0909` → IC=-0.262 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0909
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=37)

- **FILTRO** `dist_vwap_pct` > `0.1067` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=53)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.178 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0054 (IC base=+0.051)

- **PATRÓN** `drift_60min` |x|≤ `0.1198` → IC=+0.144 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1198 (IC base=+0.051)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.216 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.051)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=112)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.051)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.149 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=69)

- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=43)

- **FILTRO** `sigma_h` > `0.0036` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=36)

- **FILTRO** `hora_utc` > `2.0` → IC=-0.179 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7342 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.15` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 13.15 (IC base=+0.057)

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

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.242 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.2012` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2012 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.41` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.41 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.8241` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8241 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0919 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `1923.3872` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1923.3872 (IC base=+0.095)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **FILTRO** `ibs_20min` < `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

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

- **FILTRO** `dist_vwap_pct` > `0.0767` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0767
  - _Potencial_: sin este filtro IC_bueno=-0.290 (n=79)

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
- **FILTRO** `sigma_h` > `0.002` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `ibs_20min` > `0.0328` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0328
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_ewma_delta_pct` < `8.204` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.204
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

- **FILTRO** `volumen_regimen` < `1.6138` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6138
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

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
- **FILTRO** `sigma_h` > `0.0019` → IC=-0.420 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

- **FILTRO** `drift_60min` |x|> `0.046` → IC=-0.413 (n=21)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.346 (n=11)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.413 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.346 (n=11)

- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `dist_vwap_pct` < `0.1247` → IC=-0.403 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1247
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=3)

- **FILTRO** `sigma_ewma_delta_pct` < `10.347` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 10.347
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `volumen_regimen` < `1.0933` → IC=-0.423 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0933
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `libro_liquidez` < `2178.6163` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 2178.6163
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

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
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.273 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `drift_60min` |x|> `0.0825` → IC=-0.350 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0825
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `ibs_20min` < `0.6` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_ewma_delta_pct` < `5.022` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.022
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=4)

- **FILTRO** `volumen_regimen` > `0.5422` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.5422
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `volumen_regimen` < `1.0086` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0086
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `libro_liquidez` < `1333.5577` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 1333.5577
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

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
- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.239 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=135)

- **FILTRO** `ibs_20min` > `0.5131` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5131
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=103)

- **PATRÓN** `ibs_20min` > `0.5964` → IC=+0.150 (n=135)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.5964 (IC base=+0.052)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.127 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 12.0 (IC base=+0.025)

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

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.140 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0031 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1242` → IC=+0.167 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1242 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.3394` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.3394 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.84` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.84 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.0498` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0498 (IC base=+0.097)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **PATRÓN** `sigma_h` < `0.0021` → IC=+0.300 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0021 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0637` → IC=+0.206 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0637 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.9489` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9489 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.212` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.212 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.7062` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7062 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2437.2713` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2437.2713 (IC base=+0.130)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.133 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2598.9726` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.9726 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 18.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3255.1474` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3255.1474 (IC base=+0.114)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.133 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2598.9726` → IC=+0.224 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.9726 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 18.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3255.1474` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3255.1474 (IC base=+0.114)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=97)

- **FILTRO** `libro_liquidez` < `2110.4161` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 2110.4161
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=85)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

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
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=379)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=333)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.285 (n=63)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35151.71` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `liq_usd_total` < 35151.71
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=32)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **PATRÓN** `liq_usd_total` > `35151.71` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `liq_usd_total` > 35151.71 (IC base=-0.015)

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
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=110)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.139 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=92)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.123 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 11.0 (IC base=+0.039)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=114)

- **FILTRO** `liq_n` < `8.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `liq_n` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

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
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9861` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9861
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=78)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=81)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.152 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=53)

- **FILTRO** `libro_liquidez` < `4789.3421` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 4789.3421
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=72)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_n` < `8.0` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `liq_n` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `liq_usd_total` < `20545.57` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `liq_usd_total` < 20545.57
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=340)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1966` → IC=-0.133 (n=88)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1966
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=173)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.166 (n=684)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=2129)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.225 (n=671)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=2074)

- **FILTRO** `ibs_20min` > `0.2762` → IC=-0.196 (n=686)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2762
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2059)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.224 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=309)

- **FILTRO** `ibs_20min` < `0.7265` → IC=-0.195 (n=103)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7265
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=309)

- **FILTRO** `ibs_20min` > `0.76` → IC=-0.164 (n=117)

  - _Acción_: SKIP cuando `ibs_20min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=352)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.121 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=319)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.224 (n=114)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=356)

- **FILTRO** `ibs_20min` > `0.212` → IC=-0.181 (n=117)

  - _Acción_: SKIP cuando `ibs_20min` > 0.212
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=353)

- **FILTRO** `ballena_activa_n` > `79.0` → IC=-0.172 (n=117)

  - _Acción_: SKIP cuando `ballena_activa_n` > 79.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=353)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.187 (n=180)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=248)

- **FILTRO** `ibs_20min` < `0.7273` → IC=-0.216 (n=107)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=321)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.224 (n=114)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=346)

- **FILTRO** `ibs_20min` > `0.28` → IC=-0.188 (n=155)

  - _Acción_: SKIP cuando `ibs_20min` > 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=305)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.141 (n=126)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=380)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.209 (n=125)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=363)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.145 (n=164)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=324)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.259 (n=106)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=325)

- **FILTRO** `ibs_20min` > `0.2778` → IC=-0.213 (n=106)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=325)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.172 (n=193)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=238)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.199 (n=111)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=360)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=456)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.275 (n=140)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=287)

- **FILTRO** `drift_20min_pct` |x|> `0.2772` → IC=-0.128 (n=213)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2772
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=214)

- **FILTRO** `ibs_20min` > `0.2949` → IC=-0.285 (n=105)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2949
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=322)

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
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=339)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=630)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.142 (n=2031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4832)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.286 (n=1650)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=5213)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.234 (n=1712)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=5151)

- **FILTRO** `ballena_activa_n` > `19.0` → IC=-0.175 (n=2321)

  - _Acción_: SKIP cuando `ballena_activa_n` > 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4542)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.227 (n=1982)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=6416)

- **FILTRO** `ibs_7min` > `0.7241` → IC=-0.168 (n=2098)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7241
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=6300)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.154 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=716)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.329 (n=226)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=708)

- **FILTRO** `ibs_7min` < `0.985` → IC=-0.196 (n=616)

  - _Acción_: SKIP cuando `ibs_7min` < 0.985
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=318)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.260 (n=231)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=703)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.240 (n=352)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1061)

- **FILTRO** `drift_7min_pct` |x|> `0.1048` → IC=-0.133 (n=706)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1048
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=707)

- **FILTRO** `ibs_7min` > `0.8378` → IC=-0.199 (n=353)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8378
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=1060)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.161 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1101)

- **FILTRO** `py_entrada` < `0.39` → IC=-0.250 (n=346)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1045)

- **FILTRO** `ballena_activa_n` > `147.0` → IC=-0.170 (n=346)

  - _Acción_: SKIP cuando `ballena_activa_n` > 147.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1045)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.222 (n=343)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1077)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.170 (n=353)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1067)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.213 (n=273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=686)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.333 (n=226)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=733)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.276 (n=239)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=720)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.273 (n=236)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=723)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.261 (n=320)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1150)

- **FILTRO** `ibs_7min` > `0.8222` → IC=-0.186 (n=367)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8222
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1103)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.157 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=814)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.269 (n=288)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=885)

- **FILTRO** `ibs_7min` < `0.7689` → IC=-0.188 (n=293)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7689
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=880)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.211 (n=292)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=881)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.135 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=796)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.283 (n=275)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=881)

- **FILTRO** `ibs_7min` > `0.1818` → IC=-0.154 (n=391)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1818
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=765)

- **FILTRO** `ballena_activa_n` > `39.0` → IC=-0.214 (n=285)

  - _Acción_: SKIP cuando `ballena_activa_n` > 39.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=871)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.224 (n=310)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=973)

- **FILTRO** `ibs_7min` < `0.7719` → IC=-0.199 (n=320)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7719
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=963)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.196 (n=304)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=979)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.182 (n=363)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1160)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.289 (n=273)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=850)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.241 (n=272)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=851)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.250 (n=270)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=853)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.274 (n=290)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1126)

- **FILTRO** `ibs_7min` > `0.8393` → IC=-0.145 (n=353)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8393
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=1063)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.122 (n=477)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=939)

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

- **PATRÓN** `delta_ratio` |x|> `0.3996` → IC=+0.144 (n=254)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.3996 (IC base=+0.118)

- **PATRÓN** `total_vol_5m` < `451.5692` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `total_vol_5m` < 451.5692 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `3571.4392` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3571.4392 (IC base=+0.118)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `315.516` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 315.516 (IC base=+0.122)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `libro_liquidez` > `3657.0978` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3657.0978 (IC base=+0.100)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.150 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 16.0 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.079)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0147` → IC=-0.141 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0147
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.310 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=81)

- **FILTRO** `T_h` > `111.9853` → IC=-0.369 (n=59)

  - _Acción_: SKIP cuando `T_h` > 111.9853
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=61)

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
- **FILTRO** `sigma_h` < `0.0047` → IC=-0.138 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=47)

- **FILTRO** `T_h` > `143.1632` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=62)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.321 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=20)

- **FILTRO** `T_h` < `111.9558` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `T_h` < 111.9558
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=50)

- **PATRÓN** `T_h` < `143.1632` → IC=+0.125 (n=62)

  - _Acción_: Kelly boost +0.62€ cuando `T_h` < 143.1632 (IC base=-0.032)

- **PATRÓN** `pct_vs_K` |x|≤ `1.4281` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `pct_vs_K` |x|≤ 1.4281 (IC base=-0.032)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.167 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` > `87.9947` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `T_h` > 87.9947
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

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
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=74)

- **FILTRO** `streak_estiramiento` > `0.437` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.437
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 44.0 (IC base=+0.017)

### STREAK_FADE_5M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=182)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=54)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=66)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.167 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 10.0 (IC base=+0.028)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.5 (IC base=+0.028)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=82)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=91)

- **FILTRO** `streak_estiramiento` > `0.644` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.644
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=92)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=108)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=252)

- **FILTRO** `streak_estiramiento` > `0.5355` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5355
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=46)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `streak_len` < 3.0 (IC base=+0.061)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=118)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=182)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.125 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 14.0 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 25.0 (IC base=+0.068)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1100)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=634)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=642)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.146 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0029 (IC base=+0.108)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.121 (n=373)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.61€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.108)

- **PATRÓN** `ibs_15` > `0.5217` → IC=+0.195 (n=372)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.5217 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.176 (n=103)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.614` → IC=+0.243 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.614 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `7101.5791` → IC=+0.151 (n=124)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7101.5791 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 73.0 (IC base=+0.108)

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.1916` → IC=-0.216 (n=100)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1916
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=301)

- **FILTRO** `sigma_ewma_delta_pct` > `6.694` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.694
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=349)

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

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.156 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0033 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.1944` → IC=+0.167 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1944 (IC base=+0.140)

- **PATRÓN** `drift_15min` |x|≤ `0.4671` → IC=+0.162 (n=69)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.4671 (IC base=+0.140)

- **PATRÓN** `delta_ratio_macro` |x|> `0.262` → IC=+0.203 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.262 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.151 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 16.0 (IC base=+0.140)

- **PATRÓN** `ibs_15` > `0.8714` → IC=+0.246 (n=69)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8714 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.2982` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2982 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.5344` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.5344 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `11264.8587` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 11264.8587 (IC base=+0.140)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.015` → IC=-0.167 (n=31)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.015
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `ibs_15` < `0.1827` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1827
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` < `0.6404` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6404
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=65)

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

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=54)

- **FILTRO** `dist_vwap_pct` > `0.1641` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1641
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=64)

- **FILTRO** `drift_15min` |x|> `0.5919` → IC=-0.178 (n=85)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5919
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=256)

### UPDOWN_GBM#ETH#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `13.193` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 13.193 (IC base=+0.034)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.034)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

- **FILTRO** `dist_vwap_pct` < `0.116` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.116
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `sigma_ewma_delta_pct` < `2.366` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 2.366
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.179 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=27)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.155 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0106 (IC base=-0.009)

- **PATRÓN** `dist_vwap_pct` < `0.4088` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4088 (IC base=-0.009)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.090)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.181 (n=89)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.55 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.4747` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4747 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.569` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.569 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2503.3208` → IC=+0.148 (n=89)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2503.3208 (IC base=+0.090)

- **PATRÓN** `ibs_15` < `0.1282` → IC=+0.190 (n=98)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` < 0.1282 (IC base=+0.040)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.394 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.299)

- **PATRÓN** `drift_60min` |x|≤ `0.0615` → IC=+0.351 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0615 (IC base=+0.299)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1549` → IC=+0.313 (n=89)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1549 (IC base=+0.299)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4217` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4217 (IC base=+0.299)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.321 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.299)

- **PATRÓN** `ibs_15` > `0.8044` → IC=+0.359 (n=119)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8044 (IC base=+0.299)

- **PATRÓN** `dist_vwap_pct` > `0.538` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.538 (IC base=+0.299)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.631` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.631 (IC base=+0.299)

- **PATRÓN** `libro_liquidez` > `7404.7045` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7404.7045 (IC base=+0.299)

- **PATRÓN** `ballena_activa_n` < `546.0` → IC=+0.373 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 546.0 (IC base=+0.299)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1971` → IC=+0.283 (n=67)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1971 (IC base=+0.267)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.306 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.284 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.297 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.267)

- **PATRÓN** `drift_15min` |x|≤ `0.4366` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4366 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.306 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.275 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.267)

- **PATRÓN** `ibs_15` > `0.8246` → IC=+0.314 (n=68)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8246 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.4267` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4267 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.871` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.871 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.018` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.018 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `8910.53` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8910.53 (IC base=+0.267)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.393 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.0534` → IC=+0.409 (n=20)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0534 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.400 (n=38)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.341 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.333)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.339 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.424 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.1297` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1297 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.86` → IC=+0.393 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.86 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3128.4304` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3128.4304 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 198.0 (IC base=+0.333)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `ibs_15` < `0.4476` → IC=-0.279 (n=93)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4476
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=280)

- **FILTRO** `sigma_ewma_delta_pct` > `17.025` → IC=-0.188 (n=312)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.025
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=2142)

- **PATRÓN** `ibs_15` > `0.4476` → IC=+0.145 (n=280)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` > 0.4476 (IC base=-0.056)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0853` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0853 (IC base=-0.095)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.337 (n=84)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.095)

- **PATRÓN** `dist_vwap_pct` < `0.1907` → IC=+0.247 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1907 (IC base=-0.095)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 67.0 (IC base=-0.095)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.234 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=414)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.222 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=276)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.241 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=418)

- **FILTRO** `sigma_ewma_delta_pct` > `18.983` → IC=-0.243 (n=107)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.983
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=444)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4359` → IC=-0.378 (n=39)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4359
  - _Potencial_: sin este filtro IC_bueno=+0.164 (n=117)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=139)

- **PATRÓN** `drift_60min` |x|≤ `0.0629` → IC=+0.167 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0629 (IC base=+0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3346` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3346 (IC base=+0.025)

- **PATRÓN** `ibs_15` > `0.4359` → IC=+0.164 (n=117)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` > 0.4359 (IC base=+0.025)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.025)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.152` → IC=+0.231 (n=50)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.152 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.214)

- **PATRÓN** `drift_15min` |x|≤ `0.4463` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4463 (IC base=+0.214)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1065` → IC=+0.217 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1065 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.256 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.236 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.214)

- **PATRÓN** `ibs_15` < `0.428` → IC=+0.347 (n=57)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.428 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.1242` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1242 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.79` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.79 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.416` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.416 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `6950.975` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6950.975 (IC base=+0.214)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0085` → IC=-0.233 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=144)

- **FILTRO** `drift_15min` |x|> `0.5292` → IC=-0.127 (n=108)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5292
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=109)

- **FILTRO** `sigma_ewma_delta_pct` > `12.676` → IC=-0.150 (n=135)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 12.676
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=718)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.089)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.178 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

- **FILTRO** `sigma_ewma_delta_pct` > `14.239` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 14.239
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=200)

- **FILTRO** `libro_liquidez` < `2583.781` → IC=-0.171 (n=74)

  - _Acción_: SKIP cuando `libro_liquidez` < 2583.781
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=153)

- **FILTRO** `drift_15min` |x|> `1.5354` → IC=-0.146 (n=196)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.5354
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=591)

- **FILTRO** `sigma_ewma_delta_pct` > `15.442` → IC=-0.177 (n=97)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.442
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=690)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.289 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.319 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.270)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1898` → IC=+0.323 (n=94)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1898 (IC base=+0.270)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3963` → IC=+0.309 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3963 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.269 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.270)

- **PATRÓN** `ibs_15` > `0.8606` → IC=+0.313 (n=185)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8606 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.285` → IC=+0.361 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.285 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.523` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.523 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.463` → IC=+0.268 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.463 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.269 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `11757.2155` → IC=+0.331 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11757.2155 (IC base=+0.270)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.263 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.305 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.252)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.290 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.252)

- **PATRÓN** `drift_15min` |x|≤ `0.6649` → IC=+0.271 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.6649 (IC base=+0.252)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1425` → IC=+0.275 (n=78)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1425 (IC base=+0.252)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1313` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1313 (IC base=+0.252)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.271 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.250 (n=118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.252)

- **PATRÓN** `ibs_15` > `0.9676` → IC=+0.354 (n=53)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9676 (IC base=+0.252)

- **PATRÓN** `dist_vwap_pct` > `0.2907` → IC=+0.360 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2907 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.438` → IC=+0.255 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.438 (IC base=+0.252)

- **PATRÓN** `libro_liquidez` > `13081.1746` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13081.1746 (IC base=+0.252)

- **PATRÓN** `ballena_activa_n` < `581.0` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 581.0 (IC base=+0.252)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.294 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.295 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0603` → IC=+0.309 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0603 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1879` → IC=+0.364 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1879 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3802` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3802 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.328 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8607` → IC=+0.333 (n=82)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8607 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.952` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.952 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.296 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `10076.1613` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10076.1613 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.289)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1055` → IC=-0.289 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1055
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0068` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.0798` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0798
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `63.9981` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9981 (IC base=+0.085)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.085)

- **PATRÓN** `T_h` > `146.1038` → IC=+0.441 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.342)

- **PATRÓN** `ratio` < `1.0177` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0177 (IC base=+0.342)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `ratio` > 1.0126 (IC base=+0.342)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `87.9965` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `T_h` < 87.9965 (IC base=+0.083)

- **PATRÓN** `T_h` < `111.996` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.996 (IC base=+0.259)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.284 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.259)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `87.9936` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9936 (IC base=+0.115)

- **PATRÓN** `T_h` > `145.7785` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7785 (IC base=+0.299)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.419)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0106 (IC=+0.155 n=27). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5217 sube el IC de +0.108 a +0.195 en UPDOWN_GBM#15min (n=372). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8714 sube el IC de +0.140 a +0.246 en UPDOWN_GBM#BTC#15min (n=69). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.080 a +0.237 en UPDOWN_GBM#ETH#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.056 a +0.265 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.090 a +0.181 en UPDOWN_GBM#XRP#15min (n=89). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1282 sube el IC de +0.040 a +0.190 en UPDOWN_GBM#XRP#15min (n=98). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.095 a +0.337 en UPDOWN_GBM_15M_TARDIO (n=84). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4359 sube el IC de +0.025 a +0.164 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=117). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.428 sube el IC de +0.214 a +0.347 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=57). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.089 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8606 sube el IC de +0.270 a +0.313 en UPDOWN_GBM_IBS_ALTO (n=185). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9676 sube el IC de +0.252 a +0.354 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=53). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8607 sube el IC de +0.289 a +0.333 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=82). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8044 sube el IC de +0.299 a +0.359 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=119). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8246 sube el IC de +0.267 a +0.314 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=68). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.333 a +0.424 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.348 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 583 | +0.085 | +45.70€ | 2 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 583 | +0.085 | +45.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 339 | +0.110 | +34.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 339 | +0.110 | +34.69€ | 0 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.030 | +0.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.030 | +0.07€ | 5 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 6298 | -0.099 | -834.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 655 | -0.085 | -110.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 5643 | -0.100 | -723.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 988 | +0.016 | -109.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 988 | +0.016 | -109.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 655 | -0.085 | -110.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 655 | -0.085 | -110.39€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 359 | -0.137 | -154.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 359 | -0.137 | -154.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 725 | -0.137 | -38.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 725 | -0.137 | -38.80€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2085 | -0.075 | -111.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2085 | -0.075 | -111.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 1486 | -0.185 | -309.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 1486 | -0.185 | -309.95€ | 1 | 0 |
| ✅ FAVORITO_CONFIRMADO | 28669 | +0.114 | -1861.54€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 5437 | +0.188 | -175.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 107 | -0.105 | -50.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 20050 | +0.094 | -1608.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3075 | +0.123 | -26.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 3366 | +0.062 | -582.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 19 | -0.068 | +0.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 3342 | +0.064 | -576.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 5981 | +0.135 | -115.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1526 | +0.198 | -80.65€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 3340 | +0.111 | -71.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1073 | +0.132 | +58.96€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 3374 | +0.076 | -461.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 19 | +0.023 | -2.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 3354 | +0.077 | -456.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 6417 | +0.131 | -43.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1977 | +0.172 | +2.55€ | 0 | 8 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3338 | +0.117 | -23.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1090 | +0.105 | -14.42€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 6167 | +0.131 | -411.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1879 | +0.202 | -95.03€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 46 | +0.000 | -9.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3330 | +0.093 | -235.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 912 | +0.132 | -71.28€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 3364 | +0.104 | -247.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 17 | -0.022 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 3346 | +0.104 | -245.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 5411 | +0.176 | -399.47€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 5411 | +0.176 | -399.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1361 | +0.171 | -136.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1361 | +0.171 | -136.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 107 | -0.124 | +1.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 107 | -0.124 | +1.58€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1352 | +0.161 | -159.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1352 | +0.161 | -159.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1212 | +0.232 | -30.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1212 | +0.232 | -30.78€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1300 | +0.191 | -88.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1300 | +0.191 | -88.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 272 | +0.442 | +0.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 272 | +0.442 | +0.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 102 | +0.442 | +1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 102 | +0.442 | +1.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 104 | +0.424 | -2.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 104 | +0.424 | -2.10€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 63 | +0.439 | +1.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 63 | +0.439 | +1.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 14368 | +0.192 | -1253.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 14368 | +0.192 | -1253.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 2647 | +0.124 | -491.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 2647 | +0.124 | -491.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2229 | +0.236 | -50.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2229 | +0.236 | -50.57€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2490 | +0.162 | -322.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2490 | +0.162 | -322.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2273 | +0.234 | -54.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2273 | +0.234 | -54.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2311 | +0.218 | -106.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2311 | +0.218 | -106.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 2418 | +0.188 | -227.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 2418 | +0.188 | -227.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 5177 | +0.131 | +143.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 5177 | +0.131 | +143.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 2570 | +0.139 | +109.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 2570 | +0.139 | +109.04€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 2607 | +0.122 | +34.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 2607 | +0.122 | +34.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 733 | +0.300 | +7.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 733 | +0.300 | +7.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 313 | +0.278 | -8.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 313 | +0.278 | -8.16€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 344 | +0.303 | +10.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 344 | +0.303 | +10.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 76 | +0.359 | +5.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 76 | +0.359 | +5.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 306 | +0.409 | -16.19€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 306 | +0.409 | -16.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 136 | +0.406 | -7.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 136 | +0.406 | -7.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 139 | +0.415 | -6.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 139 | +0.415 | -6.97€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 31 | +0.348 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 182 | +0.098 | -0.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 54 | +0.107 | +0.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 128 | +0.092 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 5 | +0.054 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 5 | +0.054 | +2.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 150 | +0.099 | +0.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 22 | +0.125 | +1.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 128 | +0.092 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 27 | +0.052 | -2.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 27 | +0.052 | -2.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 4967 | +0.096 | -186.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 510 | +0.047 | -36.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 4457 | +0.102 | -149.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 3431 | +0.096 | -91.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 510 | +0.047 | -36.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 2921 | +0.104 | -54.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 1536 | +0.097 | -95.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 1536 | +0.097 | -95.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 400 | +0.284 | -25.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 400 | +0.284 | -25.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 400 | +0.284 | -25.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 400 | +0.284 | -25.34€ | 0 | 4 |
| ✅ GBM_LATE_15M | 6783 | +0.044 | +2068.89€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 6783 | +0.044 | +2068.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 869 | +0.176 | +553.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 869 | +0.176 | +553.79€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 953 | +0.174 | +546.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 953 | +0.174 | +546.98€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 878 | +0.189 | +596.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 878 | +0.189 | +596.44€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 1101 | -0.049 | +21.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1101 | -0.049 | +21.35€ | 2 | 6 |
| ✅ GBM_LATE_15M#SOL | 1303 | -0.038 | +154.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1303 | -0.038 | +154.99€ | 4 | 4 |
| ✅ GBM_LATE_15M#XRP | 1679 | -0.050 | +195.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1679 | -0.050 | +195.35€ | 5 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 7742 | +0.044 | +2911.94€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 7742 | +0.044 | +2911.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1151 | -0.028 | +504.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1151 | -0.028 | +504.24€ | 1 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1711 | -0.032 | +173.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1711 | -0.032 | +173.57€ | 0 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 743 | +0.241 | +681.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 743 | +0.241 | +681.38€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1336 | -0.042 | +15.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1336 | -0.042 | +15.40€ | 8 | 3 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1424 | -0.013 | +298.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1424 | -0.013 | +298.34€ | 5 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1377 | +0.235 | +1239.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1377 | +0.235 | +1239.01€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 5420 | +0.170 | +3692.29€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 5420 | +0.170 | +3692.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 655 | +0.194 | +483.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 655 | +0.194 | +483.56€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 926 | +0.167 | +618.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 926 | +0.167 | +618.24€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 650 | +0.199 | +497.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 650 | +0.199 | +497.84€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 905 | +0.164 | +570.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 905 | +0.164 | +570.03€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1067 | +0.116 | +600.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1067 | +0.116 | +600.36€ | 1 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1217 | +0.193 | +922.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1217 | +0.193 | +922.26€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 905 | +0.074 | +162.21€ | 0 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 905 | +0.074 | +162.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 14 | +0.087 | +3.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 14 | +0.087 | +3.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 259 | +0.113 | +86.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 259 | +0.113 | +86.40€ | 4 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 193 | +0.177 | +59.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 193 | +0.177 | +59.68€ | 1 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 290 | -0.024 | -1.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 290 | -0.024 | -1.08€ | 3 | 4 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 148 | +0.060 | +14.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 148 | +0.060 | +14.84€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO | 6326 | +0.165 | +4079.22€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#15min | 6326 | +0.165 | +4079.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 831 | +0.184 | +577.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 831 | +0.184 | +577.08€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1049 | +0.165 | +668.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1049 | +0.165 | +668.01€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 822 | +0.217 | +678.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 822 | +0.217 | +678.61€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 949 | +0.139 | +501.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 949 | +0.139 | +501.36€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1166 | +0.099 | +550.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1166 | +0.099 | +550.86€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1509 | +0.192 | +1103.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1509 | +0.192 | +1103.30€ | 0 | 24 |
| ✅ GBM_LATE_5M | 1155 | +0.123 | +503.43€ | 1 | 16 |
| ✅ GBM_LATE_5M#5min | 1155 | +0.123 | +503.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 460 | +0.139 | +263.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 460 | +0.139 | +263.59€ | 2 | 21 |
| ✅ GBM_LATE_5M#DOGE | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 13 | -0.108 | -4.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 444 | +0.141 | +186.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 444 | +0.141 | +186.42€ | 0 | 20 |
| ✅ GBM_LATE_5M#SOL | 114 | -0.017 | +2.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 114 | -0.017 | +2.12€ | 2 | 1 |
| ✅ GBM_LATE_5M#XRP | 124 | +0.159 | +55.72€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 124 | +0.159 | +55.72€ | 0 | 0 |
| ✅ GBM_LATE_60M | 504 | -0.047 | +68.78€ | 4 | 6 |
| ✅ GBM_LATE_60M#60min | 504 | -0.047 | +68.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 174 | -0.006 | +4.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 174 | -0.006 | +4.02€ | 4 | 3 |
| ✅ GBM_LATE_60M#ETH | 178 | -0.022 | +41.98€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 178 | -0.022 | +41.98€ | 4 | 7 |
| ✅ GBM_LATE_60M#SOL | 152 | -0.123 | +22.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 152 | -0.123 | +22.77€ | 7 | 1 |
| 🚫 GBM_LATE_60M_FADE | 193 | -0.305 | -34.48€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 193 | -0.305 | -34.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 76 | -0.256 | -7.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 76 | -0.256 | -7.36€ | 17 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 65 | -0.351 | -19.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 65 | -0.351 | -19.05€ | 16 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 52 | -0.296 | -8.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 52 | -0.296 | -8.07€ | 17 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 316 | +0.041 | +4.24€ | 2 | 2 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 316 | +0.041 | +4.24€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 123 | +0.020 | +5.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 123 | +0.020 | +5.30€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 77 | +0.082 | +2.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 77 | +0.082 | +2.26€ | 0 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 5 |
| ✅ LATE_WINDOW_5MIN | 9 | +0.143 | +3.37€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 9 | +0.143 | +3.37€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 9 | +0.143 | +3.37€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 9 | +0.143 | +3.37€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 264 | +0.113 | +72.52€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 264 | +0.113 | +72.52€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 264 | +0.113 | +72.52€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 264 | +0.113 | +72.52€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 215 | -0.108 | -28.95€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 215 | -0.108 | -28.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 54 | -0.125 | -8.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 54 | -0.125 | -8.64€ | 2 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 44 | -0.043 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 44 | -0.043 | -3.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 44 | +0.000 | -0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 573 | -0.060 | -42.53€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 573 | -0.060 | -42.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 34 | -0.028 | -2.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 34 | -0.028 | -2.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 96 | -0.071 | -7.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 96 | -0.071 | -7.52€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 67 | -0.094 | -7.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 67 | -0.094 | -7.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 155 | -0.022 | -4.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 155 | -0.022 | -4.09€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#SOL | 172 | -0.046 | -11.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 172 | -0.046 | -11.53€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 49 | -0.167 | -9.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 49 | -0.167 | -9.12€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 405 | -0.011 | -6.54€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 405 | -0.011 | -6.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 127 | -0.043 | -11.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 127 | -0.043 | -11.20€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 129 | -0.011 | -0.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 129 | -0.011 | -0.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 149 | +0.017 | +5.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 149 | +0.017 | +5.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M | 3780 | +0.002 | -47.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 3780 | +0.002 | -47.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 384 | +0.005 | +7.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 384 | +0.005 | +7.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 598 | +0.005 | -8.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 624 | -0.002 | -19.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 624 | -0.002 | -19.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 740 | +0.011 | +15.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 740 | +0.011 | +15.41€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 686 | -0.002 | -22.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 686 | -0.002 | -22.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 748 | -0.004 | -19.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 748 | -0.004 | -19.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 5558 | -0.036 | +160.14€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 5558 | -0.036 | +160.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 881 | -0.029 | +123.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 881 | -0.029 | +123.05€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 995 | -0.031 | -18.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 995 | -0.031 | -18.38€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 888 | -0.043 | +93.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 888 | -0.043 | +93.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 994 | -0.036 | -32.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 994 | -0.036 | -32.92€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 902 | -0.049 | +1.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 902 | -0.049 | +1.28€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 898 | -0.031 | -6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 898 | -0.031 | -6.88€ | 5 | 0 |
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
| ✅ MOMENTUM_IBS_5M | 2996 | +0.006 | +1.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 2996 | +0.006 | +1.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 986 | +0.014 | +14.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 986 | +0.014 | +14.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1385 | +0.006 | -2.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1385 | +0.006 | -2.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 15261 | -0.073 | +287.07€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 15261 | -0.073 | +287.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 2347 | -0.093 | +260.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 2347 | -0.093 | +260.22€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 2811 | -0.057 | +0.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 2811 | -0.057 | +0.23€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 2429 | -0.084 | +22.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 2429 | -0.084 | +22.80€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 2329 | -0.098 | -175.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 2329 | -0.098 | -175.09€ | 8 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 2806 | -0.047 | +36.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 2806 | -0.047 | +36.37€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 2539 | -0.066 | +142.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 2539 | -0.066 | +142.54€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6011 | -0.010 | -119.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6011 | -0.010 | -119.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 3 | 0 |
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
| ✅ ORDER_FLOW_5M | 376 | +0.087 | +76.99€ | 1 | 3 |
| ✅ ORDER_FLOW_5M#5min | 240 | +0.103 | +64.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 72 | +0.122 | +29.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 72 | +0.122 | +29.98€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 41 | +0.081 | +7.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 41 | +0.081 | +7.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 29 | +0.113 | +7.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 29 | +0.113 | +7.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 43 | +0.100 | +9.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 43 | +0.100 | +9.30€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#XRP | 55 | +0.079 | +9.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 55 | +0.079 | +9.79€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM | 252 | -0.158 | -18.23€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 110 | -0.223 | -30.59€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 95 | -0.253 | -29.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 97 | -0.146 | -3.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 78 | -0.163 | -6.13€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 45 | -0.011 | +15.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 38 | +0.000 | +14.95€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 211 | -0.176 | -21.04€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 166 | -0.167 | +27.93€ | 4 | 2 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 72 | -0.095 | +17.65€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 70 | -0.083 | +18.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 65 | -0.231 | -3.31€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 61 | -0.230 | -4.69€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 29 | -0.177 | +13.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 27 | -0.155 | +15.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 158 | -0.156 | +29.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 131 | -0.026 | -12.65€ | 4 | 1 |
| ✅ STREAK_FADE_15M#15min | 131 | -0.026 | -12.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 54 | -0.018 | -6.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 54 | -0.018 | -6.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 11 | +0.064 | +1.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 11 | +0.064 | +1.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 57 | -0.059 | -6.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 57 | -0.059 | -6.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 928 | -0.007 | -31.96€ | 1 | 0 |
| ✅ STREAK_FADE_5M#5min | 928 | -0.007 | -31.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 318 | +0.000 | -5.46€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 318 | +0.000 | -5.46€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 308 | +0.010 | -4.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 308 | +0.010 | -4.19€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 115 | -0.013 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 115 | -0.013 | -7.62€ | 3 | 2 |
| ✅ STREAK_FADE_5M#XRP | 187 | -0.045 | -14.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 187 | -0.045 | -14.68€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 29 | -0.081 | -3.00€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 18 | -0.135 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 11 | +0.021 | +0.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 1810 | +0.023 | +23.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 1810 | +0.023 | +23.20€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 604 | +0.023 | +5.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 604 | +0.023 | +5.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 318 | +0.009 | +0.59€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 318 | +0.009 | +0.59€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 546 | +0.025 | +6.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 546 | +0.025 | +6.38€ | 2 | 1 |
| ✅ STREAK_MOM_5M#XRP | 342 | +0.029 | +10.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 342 | +0.029 | +10.82€ | 2 | 2 |
| ✅ STRUCT_NO_15M | 2900 | +0.005 | -34.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 2900 | +0.005 | -34.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1119 | +0.006 | -13.98€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1119 | +0.006 | -13.98€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1115 | +0.014 | -4.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1115 | +0.014 | -4.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 666 | -0.009 | -16.32€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 666 | -0.009 | -16.32€ | 2 | 0 |
| ✅ UPDOWN_GBM | 5263 | +0.008 | +142.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2035 | +0.044 | +188.88€ | 0 | 7 |
| ✅ UPDOWN_GBM#240min | 227 | +0.028 | +5.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 2610 | -0.016 | -48.93€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 344 | -0.012 | -3.00€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 188 | +0.084 | +31.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 173 | +0.106 | +34.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 6 | +0.000 | +0.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1131 | +0.017 | +56.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 213 | +0.067 | +24.96€ | 3 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 67 | +0.094 | +9.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 720 | +0.010 | +26.95€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 113 | -0.048 | -7.05€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 667 | -0.002 | +1.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 116 | +0.093 | +25.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 8 | +0.000 | -0.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 543 | -0.023 | -23.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1199 | +0.011 | +18.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 554 | +0.032 | +24.53€ | 1 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 65 | +0.082 | +4.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 420 | -0.024 | -15.85€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 145 | +0.024 | +4.83€ | 0 | 2 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1249 | -0.006 | -12.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 458 | +0.000 | -4.44€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 51 | -0.028 | -3.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 642 | -0.002 | -3.44€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 86 | -0.023 | -0.78€ | 1 | 2 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 827 | +0.002 | +49.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 521 | +0.053 | +84.37€ | 0 | 6 |
| ✅ UPDOWN_GBM#XRP#240min | 30 | -0.125 | -4.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 276 | -0.079 | -30.11€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 177 | +0.299 | +24.78€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 177 | +0.299 | +24.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 101 | +0.267 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 101 | +0.267 | +1.83€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 76 | +0.333 | +22.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 76 | +0.333 | +22.95€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3359 | -0.084 | +384.19€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3359 | -0.084 | +384.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 277 | -0.063 | +129.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 277 | -0.063 | +129.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 694 | -0.170 | -85.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 694 | -0.170 | -85.66€ | 4 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 73 | +0.047 | +8.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 73 | +0.047 | +8.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 231 | +0.088 | +81.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 231 | +0.088 | +81.64€ | 2 | 15 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1070 | -0.073 | +158.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1070 | -0.073 | +158.69€ | 3 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1014 | -0.091 | +91.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1014 | -0.091 | +91.19€ | 5 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 26 | +0.000 | -1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 26 | +0.000 | -1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 26 | +0.000 | -1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 26 | +0.000 | -1.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 276 | +0.270 | +189.45€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 276 | +0.270 | +189.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 155 | +0.252 | +92.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 155 | +0.252 | +92.61€ | 0 | 14 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 121 | +0.289 | +96.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 121 | +0.289 | +96.84€ | 0 | 12 |
| ✅ UPDOWN_OU_5M | 381 | -0.064 | -30.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#5min | 381 | -0.064 | -30.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 236 | -0.008 | -11.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 236 | -0.008 | -11.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 29 | +0.016 | +3.07€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 29 | +0.016 | +3.07€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 27 | -0.190 | -5.68€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 27 | -0.190 | -5.68€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 31 | -0.167 | -4.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 31 | -0.167 | -4.88€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 29 | -0.210 | -5.21€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 29 | -0.210 | -5.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 29 | -0.177 | -5.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1051 | +0.286 | +427.58€ | 0 | 5 |
| ✅ WEEKLY_PRICE#BTC | 313 | +0.202 | -1.41€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 328 | +0.255 | +68.92€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 410 | +0.374 | +360.08€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.085) — sin ventaja clara. oversold(IBS<0.3): IC=+0.004 n=1821 | neutral: IC=+0.004 n=1973 | overbought(IBS>0.7): IC=+0.088 n=2089
  - _Datos_: n=6164 IC=+0.033 PNL=+471.44€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 5 celda(s) pasan gate riguroso completo de 197 evaluadas (n>=40) y 563 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.000 < 0.08 — monitorear
  - _Datos_: n=458 IC=+0.000 PNL=-4.44€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=328/15 IC=+0.255 PNL=+68.92€ | BTC: n=313/15 IC=+0.202 PNL=-1.41€ | SOL: n=410/15 IC=+0.374 PNL=+360.08€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.076 n=85312 | tras_1loss IC=+0.045 n=66325 | tras_2loss IC=+0.008 n=30144/40 | gap=+0.068 (umbral 0.05)

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
  - _Estado_: 5201 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.119 n=40/60 | contraria IC=-0.045 n=20 | gap=+0.165 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=48, boost estimado=+0.004. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 43/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=145/40 IC=+0.024 PNL=+4.83€ | BTC#60min: n=113/40 IC=-0.048 PNL=-7.05€ | SOL#60min: n=86/40 IC=-0.023 PNL=-0.78€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.003 n=527 | contrario_BTC IC=-0.009 n=397/40 | gap=-0.006 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=88 PNL=+18.82€
  - _Datos_: n=88 IC=+0.122 PNL=+18.82€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=894 PNL=+430.77€
  - _Datos_: n=894 IC=+0.332 PNL=+430.77€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=43 IC=+0.078 PNL=+12.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=43 IC=+0.078 PNL=+12.38€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 13/30 ops en el filtro definido (IC actual=+0.065 PNL=+1.67€)
  - _Datos_: n=13 IC=+0.065 PNL=+1.67€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=5022 IC=+0.004 PNL=+91.58€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=5022 IC=+0.004 PNL=+91.58€

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
  - _Estado_: n=283 IC=+0.009 PNL=+4.38€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=283 IC=+0.009 PNL=+4.38€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.081 < -0.08 con n=91 PNL=-7.19€
  - _Datos_: n=91 IC=-0.081 PNL=-7.19€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.1 con n=496 PNL=+99.57€
  - _Datos_: n=496 IC=+0.108 PNL=+99.57€

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
  - _Estado_: n=213 IC=+0.067 PNL=+24.96€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=213 IC=+0.067 PNL=+24.96€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=1191 IC=+0.036 PNL=+76.69€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1191 IC=+0.036 PNL=+76.69€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 17/30 ops en el filtro definido (IC actual=-0.201 PNL=-3.48€)
  - _Datos_: n=17 IC=-0.201 PNL=-3.48€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=64 IC=-0.015 PNL=+9.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=64 IC=-0.015 PNL=+9.39€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=73 IC=+0.020 PNL=+6.16€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=73 IC=+0.020 PNL=+6.16€

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
  - _Estado_: n=1939 IC=-0.013 PNL=-40.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1939 IC=-0.013 PNL=-40.80€

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
  - _Estado_: 9/30 ops en el filtro definido (IC actual=+0.143 PNL=+3.37€)
  - _Datos_: n=9 IC=+0.143 PNL=+3.37€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1422 IC=+0.024 PNL=+84.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1422 IC=+0.024 PNL=+84.71€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=415 IC=+0.035 PNL=+0.71€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=415 IC=+0.035 PNL=+0.71€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=78 PNL=+20.03€
  - _Datos_: n=78 IC=+0.113 PNL=+20.03€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=110 PNL=+27.17€
  - _Datos_: n=110 IC=+0.098 PNL=+27.17€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=2693 IC=+0.101 PNL=+490.48€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=2693 IC=+0.101 PNL=+490.48€

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
  - _Estado_: n=734 IC=+0.026 PNL=+42.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=734 IC=+0.026 PNL=+42.51€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.02 con n=196 PNL=+55.28€
  - _Datos_: n=196 IC=+0.126 PNL=+55.28€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.440 > 0.1 con n=577 PNL=+477.86€
  - _Datos_: n=577 IC=+0.440 PNL=+477.86€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1356 IC=+0.024 PNL=+70.73€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1356 IC=+0.024 PNL=+70.73€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.159 > 0.1 con n=736 PNL=+252.78€
  - _Datos_: n=736 IC=+0.159 PNL=+252.78€

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
  - _Estado_: n=389 IC=+0.040 PNL=+46.97€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=389 IC=+0.040 PNL=+46.97€

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
  - _Estado_: n=60 IC=+0.048 PNL=-4.97€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=60 IC=+0.048 PNL=-4.97€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=3704 IC=-0.132 PNL=+282.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3704 IC=-0.132 PNL=+282.06€

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
  - _Estado_: n=528 IC=+0.138 PNL=+196.41€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=528 IC=+0.138 PNL=+196.41€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.08 con n=496 PNL=+99.57€
  - _Datos_: n=496 IC=+0.108 PNL=+99.57€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=533 IC=+0.006 PNL=+5.86€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=533 IC=+0.006 PNL=+5.86€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.094 > 0.08 con n=538 PNL=+319.36€
  - _Datos_: n=538 IC=+0.094 PNL=+319.36€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.140 > 0.08 con n=137 PNL=+30.84€
  - _Datos_: n=137 IC=+0.140 PNL=+30.84€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.225 < -0.1 con n=394 PNL=-24.68€
  - _Datos_: n=394 IC=-0.225 PNL=-24.68€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=899 IC=+0.153 PNL=+492.92€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=899 IC=+0.153 PNL=+492.92€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 22/40 ops en el filtro definido (IC actual=+0.042 PNL=+0.30€)
  - _Datos_: n=22 IC=+0.042 PNL=+0.30€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=572 IC=-0.026 PNL=+33.07€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=572 IC=-0.026 PNL=+33.07€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.183 > 0.08 con n=493 PNL=+286.69€
  - _Datos_: n=493 IC=+0.183 PNL=+286.69€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=883 IC=-0.041 PNL=+115.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=883 IC=-0.041 PNL=+115.94€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=231 PNL=-27.10€
  - _Datos_: n=231 IC=+0.122 PNL=-27.10€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.08 con n=1261 PNL=-110.27€
  - _Datos_: n=1261 IC=+0.243 PNL=-110.27€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.114 n=138) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=138 IC=+0.114 PNL=+33.77€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.344 > 0.08 con n=62 PNL=+46.59€
  - _Datos_: n=62 IC=+0.344 PNL=+46.59€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.433 n=222) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=222 IC=+0.433 PNL=+300.62€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=2647 IC=+0.124 PNL=-491.32€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=2647 IC=+0.124 PNL=-491.32€

**⏳ H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: 40
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: 35/40 ops en el filtro definido (IC actual=+0.176 PNL=+19.80€)
  - _Datos_: n=35 IC=+0.176 PNL=+19.80€
