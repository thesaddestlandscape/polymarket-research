# Hipótesis automáticas — 2026-08-31 03:33 UTC
_Generado por shadow_postmortem.py sobre 222123 resoluciones (PNL=+17316.61€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `ballena_activa_n` > `121.0` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 121.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.261 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.168)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.182 (n=262)

  - _Acción_: Kelly boost +0.91€ cuando `n_ballena_banda` > 19.0 (IC base=+0.168)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.256 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.168)

- **PATRÓN** `banda_hit_calibrado` > `0.8239` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8239 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.193 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 11.0 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=302)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `3000.2192` → IC=+0.231 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3000.2192 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.139 (n=206)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=-0.008)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `n_ballena_banda` < `34.0` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `n_ballena_banda` < 34.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=110)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.123 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=113)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.260 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.205)

- **PATRÓN** `n_ballena_banda` > `17.0` → IC=+0.218 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 17.0 (IC base=+0.205)

- **PATRÓN** `n_total_lado` > `55.0` → IC=+0.247 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 55.0 (IC base=+0.205)

- **PATRÓN** `banda_hit_calibrado` > `0.829` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.829 (IC base=+0.205)

- **PATRÓN** `banda_z` > `12.108` → IC=+0.274 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 12.108 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.219 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.210 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.221 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `4013.8598` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4013.8598 (IC base=+0.205)

- **PATRÓN** `ballena_activa_n` < `237.0` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 237.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.030)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=93)

- **FILTRO** `banda_hit_calibrado` < `0.6329` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6329
  - _Potencial_: sin este filtro IC_bueno=+0.238 (n=82)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=97)

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

- **PATRÓN** `py_entrada` > `0.335` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.335 (IC base=+0.085)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.085)

- **PATRÓN** `banda_z` > `8.441` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 8.441 (IC base=+0.085)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=-0.024)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `146.07` → IC=-0.294 (n=3120)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.07
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=9363)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `146.13` → IC=-0.255 (n=410)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.13
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1231)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `439.86` → IC=-0.167 (n=214)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 439.86
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=642)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `111.95` → IC=-0.398 (n=400)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 111.95
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1200)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `158.15` → IC=-0.151 (n=835)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.15
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2507)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `139.18` → IC=-0.324 (n=712)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.18
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=2138)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `123.17` → IC=-0.396 (n=548)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.17
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=1646)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.193 (n=6583)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.7 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=1806)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2386.174` → IC=+0.177 (n=1728)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2386.174 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.147 (n=4019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.159 (n=5341)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.257 (n=4176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3366)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1918.2624` → IC=+0.181 (n=2835)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1918.2624 (IC base=+0.141)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.215 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.387 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `12803.5958` → IC=+0.224 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12803.5958 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.261 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=987)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `13461.0349` → IC=+0.238 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13461.0349 (IC base=+0.190)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.128 (n=512)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` > `0.555` → IC=+0.134 (n=588)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` > 0.555 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=266)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `4842.4379` → IC=+0.157 (n=211)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4842.4379 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.195 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.180 (n=295)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.41 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.162 (n=205)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.132)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=79)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=1439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.132 (n=1210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 15.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.328 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.276 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.277 (n=573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.274)

- **PATRÓN** `py_entrada` < `0.195` → IC=+0.410 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.195 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `2172.4252` → IC=+0.277 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2172.4252 (IC base=+0.274)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.158 (n=299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.655 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=411)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2079.6986` → IC=+0.167 (n=301)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2079.6986 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.220 (n=362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.439 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=341)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` < `0.21` → IC=+0.350 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.21 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2131.9537` → IC=+0.223 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2131.9537 (IC base=+0.212)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=97)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.203 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `3443.9514` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3443.9514 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.120 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.214 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=282)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.293 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=98)

- **FILTRO** `py_entrada` > `0.835` → IC=-0.364 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=141)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=5363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=4536)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.203 (n=2561)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2367.8896` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2367.8896 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.165 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.173 (n=1315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.177 (n=1407)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.164)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=81)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=82)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.330)

- **PATRÓN** `py_entrada` > `0.835` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.835 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `2916.5858` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.5858 (IC base=+0.330)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.174 (n=1297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=1142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.170 (n=1289)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.73 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.180 (n=922)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.72 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=1224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.315 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.233)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=1317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.195 (n=673)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.7 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.468 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.447)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.449 (n=233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.457 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.447)

- **PATRÓN** `libro_liquidez` > `3363.9486` → IC=+0.461 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3363.9486 (IC base=+0.447)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.440 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `10601.0016` → IC=+0.458 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10601.0016 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.457 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.439 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.441 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.438)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `3624.439` → IC=+0.478 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3624.439 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.456 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `1930.7091` → IC=+0.435 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.7091 (IC base=+0.442)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=14141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.212 (n=14008)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.168 (n=1984)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.72 (IC base=+0.139)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=2473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.270 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.233)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.168 (n=1889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 12.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.208 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.168)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=1269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.290 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.228)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.212 (n=2346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.242 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.206)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.190 (n=1870)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.229 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.183)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.210 (n=2096)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.135)

- **PATRÓN** `restante_min` < `3.96` → IC=+0.145 (n=1924)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` < 3.96 (IC base=+0.135)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.156 (n=2043)

  - _Acción_: Kelly boost +0.78€ cuando `restante_min` > 4.93 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.151 (n=2835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 8.0 (IC base=+0.135)

- **PATRÓN** `lag_apertura_s` < `4.22` → IC=+0.157 (n=1913)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 4.22 (IC base=+0.135)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.213 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.138)

- **PATRÓN** `restante_min` < `3.93` → IC=+0.149 (n=963)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` < 3.93 (IC base=+0.138)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.153 (n=1316)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.88 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.164 (n=1405)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 8.0 (IC base=+0.138)

- **PATRÓN** `lag_apertura_s` < `7.0` → IC=+0.155 (n=1257)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 7.0 (IC base=+0.138)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.131)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.139 (n=961)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 4.01 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.164 (n=1057)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` > 4.94 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=3006)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=1275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `3.41` → IC=+0.170 (n=961)

  - _Acción_: Kelly boost +0.85€ cuando `lag_apertura_s` < 3.41 (IC base=+0.131)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.825` → IC=+0.377 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.825 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `2006.5399` → IC=+0.297 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.5399 (IC base=+0.296)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.291 (n=280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.280 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `4107.9466` → IC=+0.298 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4107.9466 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.333 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.300)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.309 (n=312)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.300)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.369 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `1723.1828` → IC=+0.313 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1723.1828 (IC base=+0.300)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.340 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.341)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.355 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.341)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.373 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.357 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.366 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.341)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.421 (n=277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.421 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.427 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.415)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.416 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.415)

- **PATRÓN** `libro_liquidez` > `2076.1143` → IC=+0.427 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.1143 (IC base=+0.415)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.421 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.412 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.422 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.410)

- **PATRÓN** `libro_liquidez` > `5506.0634` → IC=+0.454 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5506.0634 (IC base=+0.410)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.432 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.419 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `2076.021` → IC=+0.453 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2076.021 (IC base=+0.423)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.305 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.426 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.295 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2128.4861` → IC=+0.322 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2128.4861 (IC base=+0.284)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.305 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.284)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.426 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.295 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2128.4861` → IC=+0.322 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2128.4861 (IC base=+0.284)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9474` → IC=+0.210 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9474 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.2619` → IC=+0.227 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2619 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.4806` → IC=+0.213 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4806 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.377` → IC=+0.155 (n=1121)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 5.377 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.217 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.0807` → IC=+0.246 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0807 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.0803` → IC=+0.162 (n=673)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0803 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `2.4442` → IC=+0.166 (n=1442)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4442 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2083` → IC=+0.141 (n=1891)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.2083 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3017` → IC=+0.139 (n=998)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3017 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `0.6125` → IC=+0.152 (n=320)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6125 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.3136` → IC=+0.279 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3136 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.9552` → IC=+0.236 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9552 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.230 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.029)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.145 (n=215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0052 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.172 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.007 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.183 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.297` → IC=+0.315 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.297 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2206` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2206 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.130 (n=546)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.184 (n=469)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.04 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.163 (n=289)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 59.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.264 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.261)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.272 (n=358)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.261)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.330 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.260 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.261)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.283 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` < `0.4058` → IC=+0.293 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4058 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.063` → IC=+0.283 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.063 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` < `0.0697` → IC=+0.260 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0697 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.2578` → IC=+0.350 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2578 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `2.9515` → IC=+0.328 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9515 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `1919.1505` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.1505 (IC base=+0.261)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.257 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 63.0 (IC base=+0.261)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.263 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.2004` → IC=+0.230 (n=331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2004 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.215 (n=499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.399` → IC=+0.226 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.399 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1838` → IC=+0.224 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1838 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.5162` → IC=+0.221 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5162 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.343` → IC=+0.232 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.343 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.217 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2653 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.244 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.221 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `2.1084` → IC=+0.236 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1084 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `14063.1806` → IC=+0.220 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14063.1806 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `396.0` → IC=+0.211 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 396.0 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.158 (n=185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0023 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.150 (n=367)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0036 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0738` → IC=+0.167 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0738 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.151 (n=577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 18.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.4593` → IC=+0.180 (n=485)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.4593 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1795` → IC=+0.169 (n=488)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1795 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.981` → IC=+0.226 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.981 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.6178` → IC=+0.204 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6178 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.7416` → IC=+0.167 (n=298)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.7416 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.3983` → IC=+0.167 (n=445)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.3983 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=714)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `14339.8207` → IC=+0.182 (n=250)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 14339.8207 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 211.0 (IC base=+0.143)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.204 (n=268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=216)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.106` → IC=+0.269 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.106 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.1358` → IC=+0.150 (n=487)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.1358 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.3214` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.3214 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `3.34` → IC=+0.147 (n=448)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 3.34 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.7005` → IC=+0.163 (n=509)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.7005 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.182 (n=577)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.199 (n=280)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 43.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.254 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0096 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.461` → IC=+0.250 (n=458)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.461 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.246 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.274 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.280 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.131` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.131 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.949` → IC=+0.246 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.949 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.396` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.396 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.6195` → IC=+0.243 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6195 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.261 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1866.5484` → IC=+0.248 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1866.5484 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.232 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.243)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.164 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=427)

- **FILTRO** `ibs_20min` < `0.2901` → IC=-0.136 (n=182)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2901
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=371)

- **FILTRO** `ibs_20min` > `0.8531` → IC=-0.179 (n=244)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8531
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=736)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=914)

- **PATRÓN** `dist_vwap_pct` > `0.2741` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2741 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` < `0.6297` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6297 (IC base=-0.044)

- **PATRÓN** `volumen_regimen` > `0.7026` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7026 (IC base=-0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4376` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4376 (IC base=-0.044)

- **PATRÓN** `volumen_spike_ratio` > `1.9251` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9251 (IC base=-0.044)

- **PATRÓN** `ballena_activa_n` < `134.0` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 134.0 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.1401` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1401 (IC base=-0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.283 (IC base=-0.050)

- **PATRÓN** `volumen_spike_ratio` > `1.4743` → IC=+0.128 (n=143)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4743 (IC base=-0.050)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=114)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.136 (n=374)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1129)

- **FILTRO** `sigma_ewma_delta_pct` > `5.018` → IC=-0.166 (n=324)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.018
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1179)

- **FILTRO** `volumen_pendiente_norm` < `0.0964` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `volumen_spike_ratio` > `1.6234` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.6234
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.175 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0057 (IC base=+0.030)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.6887` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6887 (IC base=+0.030)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5186` → IC=-0.171 (n=284)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5186
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=554)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.195 (n=198)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=640)

- **FILTRO** `sigma_h` > `0.0238` → IC=-0.145 (n=342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0238
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1027)

- **FILTRO** `ibs_20min` > `0.797` → IC=-0.183 (n=342)

  - _Acción_: SKIP cuando `ibs_20min` > 0.797
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1027)

- **FILTRO** `sigma_ewma_delta_pct` > `8.566` → IC=-0.157 (n=167)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.566
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1202)

- **PATRÓN** `dist_vwap_pct` > `0.1876` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1876 (IC base=-0.108)

- **PATRÓN** `dist_vwap_pct` < `0.3549` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3549 (IC base=-0.108)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.0825` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0825 (IC base=-0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.4272` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4272 (IC base=-0.108)

- **PATRÓN** `dist_vwap_pct` < `0.2072` → IC=+0.209 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2072 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` < `0.6057` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.6057 (IC base=-0.056)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.0889` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0889 (IC base=-0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.717` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.717 (IC base=-0.056)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.056)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.136 (n=1655)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0076 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.2682` → IC=+0.120 (n=3649)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.2682 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `1.2307` → IC=+0.292 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2307 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` > `1.1627` → IC=+0.224 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1627 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` < `0.1162` → IC=+0.193 (n=1622)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1162 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2555` → IC=+0.202 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2555 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.4996` → IC=+0.214 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4996 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `2.8921` → IC=+0.197 (n=556)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.8921 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.284 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0891` → IC=+0.200 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0891 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7508` → IC=+0.239 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7508 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` < `0.219` → IC=+0.214 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.219 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.223 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6986 (IC base=+0.041)

- **PATRÓN** `volumen_regimen` > `1.2272` → IC=+0.237 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2272 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2628` → IC=+0.343 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2628 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.9255` → IC=+0.295 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9255 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.266 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.041)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2469` → IC=-0.151 (n=290)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2469
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=591)

- **FILTRO** `sigma_ewma_delta_pct` > `2.143` → IC=-0.172 (n=248)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.143
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=564)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.424` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 7.424 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2093` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2093 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.7557` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7557 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8792` → IC=-0.165 (n=323)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8792
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=972)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.130 (n=98)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 288.0 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2117` → IC=+0.137 (n=122)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2117 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` < `0.5591` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5591 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.8117` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.8117 (IC base=-0.043)

- **PATRÓN** `ballena_activa_n` < `272.0` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 272.0 (IC base=-0.043)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.290 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.228 (n=193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.263 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.126` → IC=+0.285 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.126 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.1461` → IC=+0.221 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1461 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.546` → IC=+0.218 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.546 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `4.1999` → IC=+0.219 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 4.1999 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `1917.5696` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.5696 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.315 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.312)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.333 (n=327)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.312)

- **PATRÓN** `drift_60min` |x|≤ `0.2365` → IC=+0.314 (n=245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2365 (IC base=+0.312)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.342 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.312)

- **PATRÓN** `ibs_20min` < `0.3388` → IC=+0.332 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3388 (IC base=+0.312)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.734` → IC=+0.319 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.734 (IC base=+0.312)

- **PATRÓN** `volumen_pendiente_norm` > `0.3658` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3658 (IC base=+0.312)

- **PATRÓN** `volumen_spike_ratio` > `2.4592` → IC=+0.343 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4592 (IC base=+0.312)

- **PATRÓN** `libro_liquidez` > `1774.642` → IC=+0.339 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.642 (IC base=+0.312)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.309 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.312)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.148 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=434)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=387)

- **FILTRO** `dist_vwap_pct` < `0.3182` → IC=-0.207 (n=39)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3182
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=41)

- **FILTRO** `volumen_regimen` > `0.9592` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9592
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=61)

- **FILTRO** `ibs_20min` > `0.7414` → IC=-0.144 (n=374)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7414
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=728)

- **FILTRO** `dist_vwap_pct` < `0.0964` → IC=-0.136 (n=53)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0964
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `volumen_pendiente_norm` < `0.1167` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1167
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=5)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=70)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1032)

- **PATRÓN** `dist_vwap_pct` > `1.5591` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.5591 (IC base=-0.087)

- **PATRÓN** `volumen_spike_ratio` < `1.3975` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3975 (IC base=-0.087)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7576` → IC=-0.142 (n=526)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.234 (n=272)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.237 (n=238)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=726)

- **FILTRO** `dist_vwap_pct` > `0.1358` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1358
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `volumen_regimen` > `1.3203` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.3203
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

- **FILTRO** `volumen_pendiente_norm` < `0.1132` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1132
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `volumen_spike_ratio` > `1.4195` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4195
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `volumen_spike_ratio` < `2.3625` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 2.3625
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

- **PATRÓN** `ibs_20min` > `0.8824` → IC=+0.292 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8824 (IC base=-0.014)

- **PATRÓN** `dist_vwap_pct` > `1.2681` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2681 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` < `0.8598` → IC=+0.213 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8598 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` > `1.1463` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1463 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1176` → IC=+0.216 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1176 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.231` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.231 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.4718` → IC=+0.250 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4718 (IC base=-0.014)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0247` → IC=+0.330 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0247 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.243 (n=570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8902` → IC=+0.311 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8902 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `1.3472` → IC=+0.351 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3472 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.219` → IC=+0.279 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.219 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.8367` → IC=+0.271 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8367 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2423` → IC=+0.275 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2423 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.4438` → IC=+0.253 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4438 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `3013.6279` → IC=+0.248 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3013.6279 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.282 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.274)

- **PATRÓN** `sigma_h` > `0.0238` → IC=+0.296 (n=224)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0238 (IC base=+0.274)

- **PATRÓN** `drift_60min` |x|≤ `0.2938` → IC=+0.281 (n=449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2938 (IC base=+0.274)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.280 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.277 (n=227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` < `0.275` → IC=+0.328 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.275 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` < `0.2021` → IC=+0.283 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2021 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.321 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` < `0.6367` → IC=+0.284 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6367 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `1.2624` → IC=+0.305 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2624 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.2435` → IC=+0.382 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2435 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.1847` → IC=+0.292 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1847 (IC base=+0.274)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.198 (n=1028)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0102 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.166 (n=2707)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.173 (n=3095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `1.1141` → IC=+0.256 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1141 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.528` → IC=+0.242 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.528 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.172 (n=2118)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.624 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.1047` → IC=+0.190 (n=1122)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1047 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `2.3373` → IC=+0.162 (n=2477)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.3373 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=2415)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `3961.3086` → IC=+0.189 (n=1025)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3961.3086 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.180 (n=1990)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 158.0 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.193 (n=1889)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.006 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.213 (n=944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.187 (n=1339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 7.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.4163` → IC=+0.235 (n=2832)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4163 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2188` → IC=+0.177 (n=2234)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2188 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.957` → IC=+0.211 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.957 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1685` → IC=+0.169 (n=2191)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1685 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.3` → IC=+0.258 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.9209` → IC=+0.172 (n=1475)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.9209 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.7159` → IC=+0.213 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7159 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.177 (n=1793)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 173.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.168 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0057 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.196 (n=228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0071 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.2711` → IC=+0.173 (n=502)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2711 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=456)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.307 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.622` → IC=+0.288 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.622 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2163` → IC=+0.236 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2163 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `2.7238` → IC=+0.135 (n=420)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.7238 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4525` → IC=+0.156 (n=420)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4525 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=377)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.278 (n=295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.251)

- **PATRÓN** `drift_60min` |x|≤ `0.2619` → IC=+0.289 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2619 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.272 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` < `0.2791` → IC=+0.278 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2791 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.566` → IC=+0.269 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.566 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0887` → IC=+0.239 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0887 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.311` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.311 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.9498` → IC=+0.253 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9498 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.8798` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8798 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1914.6582` → IC=+0.300 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.6582 (IC base=+0.251)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.273 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.251)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.248 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.4094` → IC=+0.195 (n=444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4094 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.9917` → IC=+0.288 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9917 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.1867` → IC=+0.236 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1867 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.987` → IC=+0.258 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.987 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6383` → IC=+0.200 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6383 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `1.067` → IC=+0.204 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.067 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.209 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.3802` → IC=+0.238 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3802 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `15220.5605` → IC=+0.200 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15220.5605 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.167 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2231` → IC=+0.178 (n=477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2231 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.4432` → IC=+0.199 (n=542)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.4432 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5785` → IC=+0.160 (n=92)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.5785 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1515` → IC=+0.177 (n=537)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1515 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.365` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.365 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6862` → IC=+0.226 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6862 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.223 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.5146` → IC=+0.165 (n=434)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.5146 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.3943` → IC=+0.154 (n=434)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.3943 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `15313.978` → IC=+0.189 (n=181)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 15313.978 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.223 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.155` → IC=+0.187 (n=305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.155 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.211 (n=178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.312 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.297` → IC=+0.282 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.297 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` < `0.2317` → IC=+0.157 (n=400)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2317 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.1405` → IC=+0.155 (n=166)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1405 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.9664` → IC=+0.188 (n=174)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.9664 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `3.4342` → IC=+0.154 (n=180)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 3.4342 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=435)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.251 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.2226` → IC=+0.274 (n=232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2226 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.267 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3` → IC=+0.293 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.262` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.262 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.283` → IC=+0.238 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.283 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3747` → IC=+0.327 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3747 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `3.1577` → IC=+0.262 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1577 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1866.5527` → IC=+0.263 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1866.5527 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.201 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.218 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.4749` → IC=+0.184 (n=444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4749 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.4502` → IC=+0.220 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4502 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.8741` → IC=+0.248 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8741 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.391` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.391 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.7015` → IC=+0.191 (n=396)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.7015 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.633` → IC=+0.224 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.633 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=504)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `12339.0205` → IC=+0.233 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12339.0205 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.156 (n=254)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 139.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.221 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3745` → IC=+0.155 (n=529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3745 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.170 (n=177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.157 (n=196)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.3886` → IC=+0.207 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3886 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.378` → IC=+0.198 (n=117)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 12.378 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1598` → IC=+0.150 (n=529)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1598 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.5948` → IC=+0.144 (n=529)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.5948 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1052` → IC=+0.172 (n=169)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1052 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.9183` → IC=+0.166 (n=282)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.9183 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.5842` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.5842 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `9534.8435` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9534.8435 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.138 (n=230)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 143.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.180 (n=273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0106 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.5435` → IC=+0.187 (n=602)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5435 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.1462` → IC=+0.262 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1462 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.267 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.131 (n=602)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6228 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4424` → IC=+0.141 (n=190)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4424 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `1.8041` → IC=+0.124 (n=378)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.8041 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=473)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3232.1195` → IC=+0.219 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3232.1195 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.140 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0056 (IC base=+0.127)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.208 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4997` → IC=+0.127 (n=505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4997 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.181 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 14.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.413` → IC=+0.226 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.413 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.9777` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.9777 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.79` → IC=+0.220 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.79 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1545` → IC=+0.140 (n=506)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1545 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.8386` → IC=+0.152 (n=337)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.8386 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2644` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2644 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.0865` → IC=+0.184 (n=169)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.0865 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2178.9306` → IC=+0.170 (n=337)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2178.9306 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0244` → IC=+0.205 (n=286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0244 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1638` → IC=+0.210 (n=277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1638 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.898` → IC=+0.265 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.898 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9501` → IC=+0.241 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9501 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.264` → IC=+0.245 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.264 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.8245` → IC=+0.211 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8245 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2417` → IC=+0.271 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2417 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `2.5754` → IC=+0.199 (n=590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5754 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=753)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.264 (n=206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.6724` → IC=+0.231 (n=616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6724 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.265 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.384` → IC=+0.259 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.384 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.478` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.478 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.239 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.343 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.7756` → IC=+0.274 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7756 (IC base=+0.220)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.163 (n=271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0079 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3319` → IC=+0.126 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.3319 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.160 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 8.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.6207` → IC=+0.183 (n=534)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6207 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.8094` → IC=+0.281 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8094 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.306` → IC=+0.185 (n=163)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 8.306 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8887` → IC=+0.136 (n=322)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8887 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `0.6971` → IC=+0.142 (n=431)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6971 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.201 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.3729` → IC=+0.127 (n=480)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.3729 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.935` → IC=+0.138 (n=363)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.935 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=621)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3054.5848` → IC=+0.145 (n=271)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3054.5848 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 13.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.31` → IC=+0.124 (n=405)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.31 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.162 (n=199)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 18.0 (IC base=+0.048)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=94)

- **FILTRO** `libro_liquidez` < `8727.5698` → IC=-0.143 (n=40)

  - _Acción_: SKIP cuando `libro_liquidez` < 8727.5698
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=82)

- **FILTRO** `ibs_20min` > `0.6789` → IC=-0.128 (n=92)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6789
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=181)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.135 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 9.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.9398` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9398 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.7807` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.7807 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.167` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 4.167 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `16641.4238` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16641.4238 (IC base=+0.057)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.153 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0027 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.134 (n=181)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.6789 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.0832` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0832 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.130 (n=117)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 278.0 (IC base=+0.045)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.224 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=85)

- **FILTRO** `ibs_20min` > `0.645` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` > 0.645
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=85)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.292 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.308 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.2319` → IC=+0.305 (n=75)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2319 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.326 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.295)

- **PATRÓN** `ibs_20min` > `0.8368` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8368 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.375 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.738` → IC=+0.375 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.738 (IC base=+0.295)

- **PATRÓN** `volumen_regimen` < `0.8662` → IC=+0.318 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8662 (IC base=+0.295)

- **PATRÓN** `volumen_regimen` > `1.074` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.074 (IC base=+0.295)

- **PATRÓN** `volumen_pendiente_norm` > `0.1796` → IC=+0.407 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1796 (IC base=+0.295)

- **PATRÓN** `volumen_spike_ratio` > `1.8383` → IC=+0.338 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8383 (IC base=+0.295)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.274 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.000)

- **PATRÓN** `drift_60min` |x|≤ `0.125` → IC=+0.141 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.125 (IC base=+0.000)

- **PATRÓN** `libro_liquidez` > `9130.6927` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9130.6927 (IC base=+0.000)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5714` → IC=-0.179 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5714
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=156)

- **FILTRO** `ibs_20min` > `0.475` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **FILTRO** `dist_vwap_pct` > `0.1911` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1911
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=60)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.4994` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4994 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.935` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.935 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.041)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.190 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0144 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2982` → IC=+0.167 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2982 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.433` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.433 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1924` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1924 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.247` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.247 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.301` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 3.301 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6571 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` < `0.2238` → IC=+0.154 (n=105)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2238 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.0219` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.0219 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.597` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.597 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=87)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.214 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.3187` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3187 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `1.6114` → IC=+0.120 (n=106)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.6114 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 17.0 (IC base=+0.100)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.197 (n=1637)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0082 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=3641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `1.0405` → IC=+0.242 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0405 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.393` → IC=+0.233 (n=1854)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.393 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.7004` → IC=+0.154 (n=1115)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7004 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.0816` → IC=+0.157 (n=1149)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0816 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1676` → IC=+0.185 (n=952)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1676 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.882` → IC=+0.166 (n=2193)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.882 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=2847)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `3920.5916` → IC=+0.194 (n=1203)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3920.5916 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.208 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.207 (n=2237)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.4745` → IC=+0.196 (n=3355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4745 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=1545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.241 (n=3357)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.4208` → IC=+0.176 (n=2418)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.4208 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.204 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.536` → IC=+0.191 (n=3284)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.536 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.6176` → IC=+0.186 (n=813)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6176 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `1.1975` → IC=+0.163 (n=813)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1975 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.258 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.3467` → IC=+0.204 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3467 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.181 (n=992)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 37.0 (IC base=+0.186)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.182 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0052 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.214 (n=267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.663` → IC=+0.316 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.663 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2174` → IC=+0.243 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2174 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `1.8922` → IC=+0.171 (n=338)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8922 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.274 (n=414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.269 (n=414)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1683` → IC=+0.291 (n=276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1683 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.291 (n=285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.519` → IC=+0.303 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.519 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.196` → IC=+0.285 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.196 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.3034` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3034 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.9552` → IC=+0.340 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9552 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `1924.8502` → IC=+0.279 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1924.8502 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.257 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.269)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.204 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.170 (n=519)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0032 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.3033` → IC=+0.167 (n=511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3033 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.3271` → IC=+0.212 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3271 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.2354` → IC=+0.222 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2354 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.699` → IC=+0.217 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.699 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.396` → IC=+0.166 (n=501)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.396 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.2714` → IC=+0.174 (n=581)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.2714 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.0886` → IC=+0.177 (n=264)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0886 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.184 (n=476)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.1464` → IC=+0.179 (n=154)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1464 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `2.4168` → IC=+0.197 (n=532)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.4168 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.3834` → IC=+0.178 (n=532)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.3834 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `12937.5849` → IC=+0.199 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12937.5849 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.179 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0023 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.171 (n=247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0048 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.2608` → IC=+0.178 (n=479)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2608 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.168 (n=510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.178 (n=561)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 18.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.4047` → IC=+0.217 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4047 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` < `0.3254` → IC=+0.179 (n=537)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3254 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.888` → IC=+0.208 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.888 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.255 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.618 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2166` → IC=+0.274 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2166 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.395` → IC=+0.204 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.395 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `14781.5472` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 14781.5472 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `382.0` → IC=+0.170 (n=234)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 382.0 (IC base=+0.166)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.265 (n=164)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.260 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.7037` → IC=+0.262 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7037 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.332` → IC=+0.333 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.332 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.2289` → IC=+0.206 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2289 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.9531` → IC=+0.210 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9531 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `4.2028` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 4.2028 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.260 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.286 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.280 (n=193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5314` → IC=+0.290 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5314 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.238` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.238 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.3667` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3667 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.252 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.4041` → IC=+0.227 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4041 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.250 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1875.8832` → IC=+0.247 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.8832 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.205 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.237)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.147 (n=579)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0086 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.143 (n=517)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0038 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.2304` → IC=+0.144 (n=386)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.2304 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.163 (n=523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.3246` → IC=+0.190 (n=579)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.3246 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.7873` → IC=+0.199 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7873 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.485` → IC=+0.194 (n=269)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 4.485 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.9051` → IC=+0.168 (n=386)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.9051 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.2145` → IC=+0.141 (n=193)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.2145 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.255 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1957` → IC=+0.210 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1957 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4459.4354` → IC=+0.219 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4459.4354 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.186 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.003 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4548` → IC=+0.154 (n=510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4548 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.177 (n=233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1187` → IC=+0.231 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1187 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1556` → IC=+0.145 (n=243)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1556 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.3593` → IC=+0.138 (n=503)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.3593 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.432` → IC=+0.232 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.432 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.59` → IC=+0.138 (n=482)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.59 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.5844` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.5844 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1367` → IC=+0.169 (n=170)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.1367 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.276 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.175 (n=204)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `9988.1936` → IC=+0.191 (n=231)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 9988.1936 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `190.0` → IC=+0.157 (n=380)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 190.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.142 (n=426)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0079 (IC base=+0.090)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.138 (n=434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 12.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.4762` → IC=+0.179 (n=639)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.4762 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.8694` → IC=+0.207 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8694 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.507` → IC=+0.218 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.507 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `2992.2942` → IC=+0.249 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2992.2942 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.146 (n=413)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 65.0 (IC base=+0.090)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.176 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0056 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.158 (n=200)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.138 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 15.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.191 (n=599)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.5034` → IC=+0.129 (n=561)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.5034 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.7039` → IC=+0.149 (n=263)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.7039 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.2071` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2071 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` > `1.7854` → IC=+0.125 (n=299)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.7854 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2687.2246` → IC=+0.163 (n=271)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2687.2246 (IC base=+0.104)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0276` → IC=+0.225 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0276 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=771)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `0.9465` → IC=+0.295 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9465 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `1.3532` → IC=+0.291 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3532 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.182` → IC=+0.249 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.182 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` > `0.6792` → IC=+0.204 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6792 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2417` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2417 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.68` → IC=+0.188 (n=686)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.68 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.8322` → IC=+0.197 (n=457)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.8322 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.196 (n=877)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.301 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0249` → IC=+0.240 (n=263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0249 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.4947` → IC=+0.227 (n=694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4947 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.224 (n=832)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.4912` → IC=+0.274 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4912 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.1725` → IC=+0.232 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1725 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.664` → IC=+0.285 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.664 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `1.2366` → IC=+0.236 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2366 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.325 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.8631` → IC=+0.218 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8631 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.186 (n=505)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 36.0 (IC base=+0.218)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=1362)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.132 (n=887)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0105 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.4485` → IC=+0.133 (n=886)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.4485 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.129 (n=365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 4.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.2701` → IC=+0.143 (n=1007)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.2701 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.559` → IC=+0.126 (n=926)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.559 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.128 (n=318)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 1.0851 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2519` → IC=+0.153 (n=191)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2519 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4634` → IC=+0.159 (n=332)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4634 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.3963` → IC=+0.149 (n=451)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.3963 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.195 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0036 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.165 (n=910)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.184 (n=365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 4.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.2009` → IC=+0.163 (n=455)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.2009 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.1812` → IC=+0.153 (n=399)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1812 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.224` → IC=+0.158 (n=1034)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.224 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2228` → IC=+0.151 (n=1005)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2228 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.1476` → IC=+0.147 (n=1028)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1476 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.5254` → IC=+0.155 (n=1024)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5254 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.145 (n=1024)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=1362)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7593.8032` → IC=+0.145 (n=1033)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7593.8032 (IC base=+0.140)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `3.645` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.645
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=164)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.645` → IC=+0.127 (n=164)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.645 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.9341` → IC=+0.177 (n=63)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.9341 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.525` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.525 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `12272.8392` → IC=+0.136 (n=138)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 12272.8392 (IC base=+0.086)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.191 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.168 (n=185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.178 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1706` → IC=+0.179 (n=244)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1706 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6595` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6595 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.163 (n=553)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1909` → IC=+0.155 (n=554)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1909 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0691` → IC=+0.167 (n=265)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0691 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.5555` → IC=+0.150 (n=552)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.5555 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.8045` → IC=+0.141 (n=368)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8045 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `11991.7118` → IC=+0.142 (n=495)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11991.7118 (IC base=+0.137)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.211 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.188 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0104 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.2581` → IC=+0.169 (n=161)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2581 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.196 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.9583` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9583 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.656` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.656 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.111` → IC=+0.170 (n=216)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 3.111 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` < `0.096` → IC=+0.167 (n=220)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.096 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.6449` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.6449 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.4219` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.4219 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `1793.9526` → IC=+0.177 (n=215)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1793.9526 (IC base=+0.158)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.147 (n=335)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0092 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.5223` → IC=+0.138 (n=335)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.5223 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.143 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 5.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.2859` → IC=+0.148 (n=299)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.2859 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.8531` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.8531 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.209` → IC=+0.130 (n=279)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.209 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.954` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.954 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.818` → IC=+0.132 (n=332)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 6.818 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.7281` → IC=+0.153 (n=148)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7281 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1823` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1823 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.4422` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4422 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.8727` → IC=+0.136 (n=218)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8727 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `8911.9459` → IC=+0.144 (n=299)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 8911.9459 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.224 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.5088` → IC=+0.189 (n=307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5088 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.167 (n=211)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 11.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.1288` → IC=+0.166 (n=306)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.1288 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.1836` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1836 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.138` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.138 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.567` → IC=+0.143 (n=317)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.567 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2058` → IC=+0.163 (n=307)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2058 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` < `0.1393` → IC=+0.162 (n=312)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.1393 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4591` → IC=+0.167 (n=301)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4591 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4556` → IC=+0.167 (n=301)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4556 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `8742.148` → IC=+0.145 (n=274)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 8742.148 (IC base=+0.141)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=64)

- **FILTRO** `sigma_ewma_delta_pct` < `4.642` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 4.642
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=31)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.218` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.218 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.1303` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1303 (IC base=+0.000)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6842` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6842
  - _Potencial_: sin este filtro IC_bueno=+0.247 (n=172)

- **FILTRO** `sigma_h` > `0.011` → IC=-0.289 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=168)

- **FILTRO** `ibs_20min` > `0.113` → IC=-0.185 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` > 0.113
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=31)

- **FILTRO** `dist_vwap_pct` > `0.111` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.111
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=64)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.208 (n=176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.247 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1239` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1239 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.6` → IC=+0.262 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.6 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.6319` → IC=+0.141 (n=76)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6319 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `1.1556` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1556 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` < `0.0644` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0644 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.3093` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3093 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.3951` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3951 (IC base=+0.086)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=157)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `1560.1458` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1560.1458 (IC base=+0.086)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.7342` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.238 (n=63)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=49)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.337 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.103)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.7342` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7342 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.35` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.35 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.9151` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.9151 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` > `1.1556` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1556 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.0478` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0478 (IC base=+0.103)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=47)

- **FILTRO** `ibs_20min` > `0.1674` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1674
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.188 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0058 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=98)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.131 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.2466` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2466 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.891` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.891 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8208` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8208 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `1.0919` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0919 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.0801` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0801 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2204.6678` → IC=+0.255 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2204.6678 (IC base=+0.129)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `18.0` → IC=-0.121 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=30)

- **FILTRO** `sigma_h` > `0.0119` → IC=-0.281 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0119
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=41)

- **FILTRO** `volumen_regimen` > `0.8778` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8778
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=-0.011)

- **PATRÓN** `ibs_20min` > `0.7867` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7867 (IC base=-0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.507` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.507 (IC base=-0.011)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1243` → IC=-0.382 (n=32)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1243
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=63)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.462 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=73)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.380 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=77)

- **FILTRO** `dist_vwap_pct` > `0.3683` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3683
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=81)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.6047` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6047
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `sigma_h` < `0.0031` → IC=-0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0031
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.326 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `dist_vwap_pct` < `0.0931` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6354` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6354
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `volumen_regimen` > `0.5614` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.5614
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `ibs_20min` < `0.5833` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `dist_vwap_pct` < `0.3782` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.3782
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=149)

- **FILTRO** `ibs_20min` > `0.447` → IC=-0.202 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.447
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=138)

- **FILTRO** `dist_vwap_pct` > `0.213` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.213
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=148)

- **PATRÓN** `ibs_20min` > `0.5964` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.5964 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.447` → IC=+0.129 (n=138)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.447 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.659` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.659 (IC base=+0.046)

- **PATRÓN** `libro_liquidez` > `3314.3277` → IC=+0.128 (n=92)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3314.3277 (IC base=+0.046)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `sigma_h` < `0.0017` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0017
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=54)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=53)

- **FILTRO** `ibs_20min` < `0.557` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` < 0.557
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=47)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.176 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0035 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.251 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.328` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.328 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.501` → IC=+0.128 (n=76)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 14.501 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.5657` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5657 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `1.6024` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.6024 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.130 (n=71)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.115)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=30)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.077)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.139 (n=34)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.077)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.250 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` > `0.7289` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7289 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.413` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 7.413 (IC base=+0.077)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.992` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.992 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8554 (IC base=+0.065)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.5556` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5556
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

- **FILTRO** `sigma_ewma_delta_pct` > `1.488` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 1.488
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.129 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0069 (IC base=+0.093)

- **PATRÓN** `drift_60min` |x|≤ `0.1849` → IC=+0.143 (n=40)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1849 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.121 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.791 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.093)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2495.7692` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2495.7692 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2493.9311` → IC=+0.151 (n=130)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2493.9311 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2495.7692` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2495.7692 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2493.9311` → IC=+0.151 (n=130)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2493.9311 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=101)

- **FILTRO** `libro_liquidez` < `2114.4748` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 2114.4748
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=136)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `libro_liquidez` < `13600.036` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 13600.036
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=750)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9444` → IC=-0.289 (n=36)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9444
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.125 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 16.0 (IC base=+0.036)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_n` < `2.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=75)

- **FILTRO** `liq_usd_total` < `29085.84` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `liq_usd_total` < 29085.84
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=66)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `libro_liquidez` < `15381.0964` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 15381.0964
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `ballena_activa_n` > `630.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 630.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `liq_n` > `12.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `liq_n` > 12.0 (IC base=+0.010)

- **PATRÓN** `liq_usd_total` > `106707.5` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `liq_usd_total` > 106707.5 (IC base=+0.010)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.495 (IC base=+0.010)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.8759` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.8759
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=51)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=228)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` > `0.56` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=115)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.128 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=60)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=27)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=85)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=32)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.6408` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.6408
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=600)

### MOMENTUM_IBS_15M#SOL#15min
- **FILTRO** `drift_20min_pct` |x|> `0.1771` → IC=-0.132 (n=112)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1771
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=220)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.45` → IC=-0.187 (n=1076)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3434)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.207 (n=1094)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=3591)

- **FILTRO** `ibs_20min` > `0.2727` → IC=-0.164 (n=1169)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=3516)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.256 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=491)

- **FILTRO** `ibs_20min` < `0.7229` → IC=-0.227 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7229
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=490)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.155 (n=198)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=618)

- **FILTRO** `ibs_20min` > `0.1807` → IC=-0.121 (n=407)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1807
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=409)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.215 (n=184)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=585)

- **FILTRO** `ballena_activa_n` > `64.0` → IC=-0.148 (n=191)

  - _Acción_: SKIP cuando `ballena_activa_n` > 64.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=578)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.125 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=495)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.173 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=397)

- **FILTRO** `ibs_20min` < `0.7222` → IC=-0.178 (n=175)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7222
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=526)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.238 (n=185)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=599)

- **FILTRO** `ibs_20min` > `0.7391` → IC=-0.206 (n=195)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7391
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=589)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.181 (n=189)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=602)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.193 (n=190)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=599)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.162 (n=196)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=593)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.142 (n=213)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=556)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.195 (n=185)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=577)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.204 (n=184)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=556)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=725)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.240 (n=183)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=582)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.306 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=375)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=381)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `libro_liquidez` < `2063.3848` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 2063.3848
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `ibs_20min` < `1.0` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `drift_20min_pct` |x|> `0.0299` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.0299
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `ibs_20min` < `0.0752` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0752
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `libro_liquidez` < `15251.0076` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 15251.0076
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=3295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8023)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.285 (n=2699)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=8619)

- **FILTRO** `ibs_7min` < `0.7206` → IC=-0.235 (n=2829)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7206
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=8489)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.169 (n=3828)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7490)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.227 (n=3282)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=10841)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.167 (n=3529)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=10594)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.3` → IC=-0.326 (n=384)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1201)

- **FILTRO** `ibs_7min` < `0.9626` → IC=-0.193 (n=1045)

  - _Acción_: SKIP cuando `ibs_7min` < 0.9626
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=540)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.235 (n=394)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=1191)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.233 (n=601)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1860)

- **FILTRO** `drift_7min_pct` |x|> `0.1194` → IC=-0.138 (n=833)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1194
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1628)

- **FILTRO** `ibs_7min` > `0.2973` → IC=-0.172 (n=836)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2973
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1625)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.152 (n=475)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=1680)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.267 (n=491)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1664)

- **FILTRO** `ibs_7min` < `0.7849` → IC=-0.185 (n=537)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7849
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1618)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.190 (n=536)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1619)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.236 (n=505)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1681)

- **FILTRO** `ballena_activa_n` > `100.0` → IC=-0.176 (n=733)

  - _Acción_: SKIP cuando `ballena_activa_n` > 100.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1453)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.196 (n=413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=1268)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.311 (n=528)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1153)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.287 (n=416)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=1265)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.234 (n=401)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=1280)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.241 (n=555)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1916)

- **FILTRO** `ibs_7min` > `0.8094` → IC=-0.170 (n=617)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8094
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1854)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.150 (n=590)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=1335)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.253 (n=464)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1461)

- **FILTRO** `ibs_7min` < `0.7575` → IC=-0.183 (n=481)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7575
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=1444)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.180 (n=636)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=1289)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.258 (n=482)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=1450)

- **FILTRO** `ibs_7min` > `0.1924` → IC=-0.172 (n=656)

  - _Acción_: SKIP cuando `ibs_7min` > 0.1924
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=1276)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.192 (n=482)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=1450)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.243 (n=511)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1632)

- **FILTRO** `ibs_7min` < `0.75` → IC=-0.201 (n=520)

  - _Acción_: SKIP cuando `ibs_7min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=1623)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.181 (n=524)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1619)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.189 (n=624)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1994)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.309 (n=444)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1385)

- **FILTRO** `ibs_7min` < `0.74` → IC=-0.241 (n=457)

  - _Acción_: SKIP cuando `ibs_7min` < 0.74
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=1372)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.231 (n=447)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1382)

- **FILTRO** `libro_liquidez` < `2717.0387` → IC=-0.140 (n=1207)

  - _Acción_: SKIP cuando `libro_liquidez` < 2717.0387
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=622)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=507)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=1948)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.158 (n=612)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1843)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.142 (n=577)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1878)

### MOMENTUM_IBS_5M_FADE#BNB#5min
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
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=435)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.132 (n=422)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.167 (n=133)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 453.526 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3219.1556` → IC=+0.150 (n=158)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3219.1556 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.263 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.109)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3971` → IC=+0.148 (n=69)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.3971 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2091.1708` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2091.1708 (IC base=+0.102)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4128` → IC=+0.189 (n=43)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.4128 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.138 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 10.0 (IC base=+0.114)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 459.6089 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `8205.41` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 8205.41 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 152.0 (IC base=+0.114)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.194 (n=60)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 18.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.239 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `11104.393` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 11104.393 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3102.7214` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3102.7214 (IC base=+0.142)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.151 (n=64)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.098)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.132 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 18.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `pct_vs_K` |x|> `3.9227` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.9227
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=96)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9936` → IC=-0.423 (n=24)

  - _Acción_: SKIP cuando `T_h` > 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.142)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `143.1632` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=105)

- **FILTRO** `pct_vs_K` |x|> `4.7` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.7
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=102)

- **FILTRO** `pct_vs_K` |x|> `4.3806` → IC=-0.473 (n=35)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.3806
  - _Potencial_: sin este filtro IC_bueno=-0.303 (n=69)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3968` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `pct_vs_K` |x|≤ 1.3968 (IC base=-0.084)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **PATRÓN** `T_h` < `119.1632` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `T_h` < 119.1632 (IC base=+0.026)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8662` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.8662 (IC base=+0.026)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` < `87.9918` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `T_h` < 87.9918
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.382 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.312 (n=30)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `5.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=50)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=102)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.015)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.437 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 44.0 (IC base=+0.051)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.250 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=67)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=65)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `streak_estiramiento` > `0.5544` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.5544
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=106)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=112)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=116)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=119)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=200)

- **PATRÓN** `streak_estiramiento` < `0.3225` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.3225 (IC base=+0.024)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=410)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=203)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=278)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.070)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1372)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=775)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=783)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.156 (n=181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1873` → IC=+0.131 (n=410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.1873 (IC base=+0.124)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2128` → IC=+0.144 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.2128 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.129 (n=435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 4.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.163 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `ibs_15` > `0.5321` → IC=+0.216 (n=410)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5321 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.188 (n=110)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.247 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=429)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `8147.128` → IC=+0.183 (n=137)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 8147.128 (IC base=+0.124)

### UPDOWN_GBM#5min
- **FILTRO** `ibs_15` < `0.273` → IC=-0.164 (n=144)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.273
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=437)

- **FILTRO** `sigma_ewma_delta_pct` > `6.666` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.666
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=528)

### UPDOWN_GBM#60min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0282` → IC=-0.204 (n=25)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0282
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=51)

- **FILTRO** `ibs_15` < `0.1315` → IC=-0.324 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1315
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.236` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 18.236 (IC base=+0.007)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0044` → IC=-0.241 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=76)

- **FILTRO** `ibs_15` > `0.6881` → IC=-0.167 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.6881
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=76)

- **FILTRO** `libro_liquidez` < `13834.2565` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 13834.2565
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=76)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.179 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0036 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.198 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0045 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.1916` → IC=+0.202 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1916 (IC base=+0.171)

- **PATRÓN** `drift_15min` |x|≤ `0.4558` → IC=+0.202 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4558 (IC base=+0.171)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.198 (n=41)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.195 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 4.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_15` > `0.8845` → IC=+0.271 (n=81)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8845 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3217` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3217 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.1189` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1189 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.224 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.598` → IC=+0.172 (n=120)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 18.598 (IC base=+0.171)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=49)

- **FILTRO** `ibs_15` < `0.1461` → IC=-0.250 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1461
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **FILTRO** `libro_liquidez` < `13135.9064` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 13135.9064
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=93)

- **FILTRO** `ibs_15` < `0.6426` → IC=-0.200 (n=28)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6426
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=84)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6314` → IC=-0.250 (n=38)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6314
  - _Potencial_: sin este filtro IC_bueno=+0.228 (n=79)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.125 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0044 (IC base=+0.071)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2671` → IC=+0.188 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.2671 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.228 (n=79)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.071)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=81)

- **FILTRO** `dist_vwap_pct` > `0.1505` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1505
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=83)

- **FILTRO** `ballena_activa_n` > `1.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35)

- **FILTRO** `drift_15min` |x|> `0.5033` → IC=-0.152 (n=139)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5033
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=418)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6136` → IC=-0.147 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6136
  - _Potencial_: sin este filtro IC_bueno=+0.294 (n=32)

- **PATRÓN** `ibs_15` > `0.6136` → IC=+0.294 (n=32)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6136 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.477` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.477 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `2964.2504` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2964.2504 (IC base=+0.076)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.023` → IC=-0.227 (n=31)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.023
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

- **FILTRO** `drift_60min` |x|> `0.7244` → IC=-0.136 (n=31)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.7244
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=65)

- **FILTRO** `ibs_15` < `0.25` → IC=-0.300 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=48)

- **FILTRO** `sigma_ewma_delta_pct` < `6.107` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 6.107
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` < `0.3754` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.3754 (IC base=+0.008)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0597` → IC=+0.145 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio_macro` |x|> 0.0597 (IC base=+0.107)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.173 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.107)

- **PATRÓN** `ibs_15` > `0.4444` → IC=+0.167 (n=109)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` > 0.4444 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.3338` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3338 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.845` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.845 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2479.6478` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2479.6478 (IC base=+0.107)

- **PATRÓN** `ibs_15` < `0.1404` → IC=+0.202 (n=122)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1404 (IC base=+0.035)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.385 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.319)

- **PATRÓN** `drift_60min` |x|≤ `0.1153` → IC=+0.343 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1153 (IC base=+0.319)

- **PATRÓN** `drift_15min` |x|≤ `0.4326` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4326 (IC base=+0.319)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.321 (n=177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.319)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.350 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.319)

- **PATRÓN** `ibs_15` > `0.9108` → IC=+0.375 (n=118)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9108 (IC base=+0.319)

- **PATRÓN** `dist_vwap_pct` > `0.2982` → IC=+0.362 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2982 (IC base=+0.319)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.888` → IC=+0.322 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.888 (IC base=+0.319)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.293` → IC=+0.320 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.293 (IC base=+0.319)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.323 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.319)

- **PATRÓN** `libro_liquidez` > `7959.8654` → IC=+0.355 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7959.8654 (IC base=+0.319)

- **PATRÓN** `ballena_activa_n` < `535.0` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 535.0 (IC base=+0.319)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1934` → IC=+0.321 (n=93)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1934 (IC base=+0.307)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.312 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0024 (IC base=+0.307)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.338 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.340 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.307)

- **PATRÓN** `drift_15min` |x|≤ `0.3756` → IC=+0.338 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3756 (IC base=+0.307)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1063` → IC=+0.310 (n=93)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1063 (IC base=+0.307)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.357 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.307)

- **PATRÓN** `ibs_15` > `0.8418` → IC=+0.353 (n=93)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8418 (IC base=+0.307)

- **PATRÓN** `dist_vwap_pct` > `0.4531` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4531 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.991` → IC=+0.317 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.991 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `11204.8499` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11204.8499 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `582.0` → IC=+0.422 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 582.0 (IC base=+0.307)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.329 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.330)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.361 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.330)

- **PATRÓN** `drift_60min` |x|≤ `0.1189` → IC=+0.365 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1189 (IC base=+0.330)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.363 (n=49)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.330)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2065` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2065 (IC base=+0.330)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.331 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.330)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.329 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.330)

- **PATRÓN** `ibs_15` > `0.8893` → IC=+0.402 (n=49)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8893 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` < `0.3445` → IC=+0.338 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3445 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.330)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.333 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 177.0 (IC base=+0.330)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.198 (n=286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=861)

- **FILTRO** `ibs_15` < `0.5433` → IC=-0.214 (n=138)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5433
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=283)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.135 (n=302)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=845)

- **FILTRO** `sigma_ewma_delta_pct` > `17.791` → IC=-0.172 (n=404)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.791
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3537` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3537 (IC base=-0.072)

- **PATRÓN** `ibs_15` > `0.5433` → IC=+0.191 (n=283)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.5433 (IC base=-0.072)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1333` → IC=+0.239 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1333 (IC base=-0.077)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0739` → IC=+0.237 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0739 (IC base=-0.077)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.294 (n=279)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` > `1.0082` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0082 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` < `0.1516` → IC=+0.234 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1516 (IC base=-0.077)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.232 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=-0.077)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.250 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=560)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.230 (n=246)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=500)

- **FILTRO** `drift_15min` |x|> `0.7564` → IC=-0.218 (n=186)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7564
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=560)

- **FILTRO** `sigma_ewma_delta_pct` > `19.475` → IC=-0.271 (n=138)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.475
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=608)

- **FILTRO** `libro_liquidez` < `15700.8148` → IC=-0.219 (n=492)

  - _Acción_: SKIP cuando `libro_liquidez` < 15700.8148
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=254)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1422` → IC=+0.140 (n=23)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio_macro` |x|> 0.1422 (IC base=+0.015)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.300 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.015)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.4827` → IC=-0.340 (n=48)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4827
  - _Potencial_: sin este filtro IC_bueno=+0.185 (n=144)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=175)

- **PATRÓN** `drift_60min` |x|≤ `0.0637` → IC=+0.206 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0637 (IC base=+0.051)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3622` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3622 (IC base=+0.051)

- **PATRÓN** `ibs_15` > `0.4827` → IC=+0.185 (n=144)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` > 0.4827 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.051)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.241 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.233 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `0.4267` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4267 (IC base=+0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0822` → IC=+0.226 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0822 (IC base=+0.222)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3069` → IC=+0.232 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3069 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.300 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.321 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.222)

- **PATRÓN** `ibs_15` < `0.3707` → IC=+0.296 (n=145)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3707 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.1348` → IC=+0.230 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1348 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.416` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.416 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `11493.267` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11493.267 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `188.0` → IC=+0.220 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 188.0 (IC base=+0.222)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.236 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=212)

- **FILTRO** `drift_60min` |x|> `0.1627` → IC=-0.170 (n=95)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1627
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=187)

- **FILTRO** `drift_15min` |x|> `0.7897` → IC=-0.250 (n=70)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7897
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=212)

- **FILTRO** `sigma_ewma_delta_pct` > `16.006` → IC=-0.147 (n=137)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.006
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1096)

- **PATRÓN** `ibs_15` > `0.8125` → IC=+0.206 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8125 (IC base=-0.123)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0746` → IC=+0.144 (n=57)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.0746 (IC base=-0.057)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.212 (n=64)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` < `0.2814` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2814 (IC base=-0.057)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 38.0 (IC base=-0.057)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0216` → IC=-0.274 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0216
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=204)

- **FILTRO** `sigma_ewma_delta_pct` > `15.608` → IC=-0.200 (n=38)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.608
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=270)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.293 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2275` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2275 (IC base=-0.072)

- **PATRÓN** `ibs_15` < `0.0566` → IC=+0.318 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0566 (IC base=-0.072)

- **PATRÓN** `ibs_15` > `0.2615` → IC=+0.328 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2615 (IC base=-0.072)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.072)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.292 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.294 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.325 (n=95)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1375` → IC=+0.311 (n=189)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1375 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.355 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.315 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.9676` → IC=+0.363 (n=129)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9676 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.3131` → IC=+0.352 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3131 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.732` → IC=+0.296 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.732 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.289 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `13561.3229` → IC=+0.356 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13561.3229 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.072` → IC=+0.289 (n=55)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.072 (IC base=+0.284)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.293 (n=109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.304 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.162` → IC=+0.307 (n=143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.162 (IC base=+0.284)

- **PATRÓN** `drift_15min` |x|≤ `0.7222` → IC=+0.288 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7222 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1394` → IC=+0.309 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1394 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.348 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.9691` → IC=+0.329 (n=74)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9691 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.346` → IC=+0.370 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.346 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.121` → IC=+0.296 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.121 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13625.3561` → IC=+0.355 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13625.3561 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.290 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0655` → IC=+0.339 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0655 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.069` → IC=+0.302 (n=109)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.069 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1273` → IC=+0.367 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1273 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.319 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.846` → IC=+0.315 (n=122)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.846 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.0914` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0914 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` < `15.362` → IC=+0.288 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 15.362 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.299 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.287)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.302 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 207.0 (IC base=+0.287)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0852` → IC=-0.269 (n=63)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0852
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=123)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.238 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=123)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.170 (n=101)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=50)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.161 (n=57)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=31)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1143` → IC=-0.149 (n=35)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1143
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=73)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `drift_15min` |x|> `0.3434` → IC=-0.184 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3434
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#ETH#5min
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1979` → IC=-0.382 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1979
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0054` → IC=-0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `T_h` < `79.3918` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 79.3918 (IC base=+0.099)

- **PATRÓN** `ratio` < `0.9922` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.099)

- **PATRÓN** `T_h` > `146.0625` → IC=+0.428 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.345)

- **PATRÓN** `ratio` < `1.0189` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0189 (IC base=+0.345)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.345)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `63.9936` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 63.9936 (IC base=+0.087)

- **PATRÓN** `ratio` < `0.973` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.087)

- **PATRÓN** `T_h` < `135.9918` → IC=+0.332 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 135.9918 (IC base=+0.273)

- **PATRÓN** `ratio` < `1.0189` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 1.0189 (IC base=+0.273)

- **PATRÓN** `ratio` > `1.0147` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0147 (IC base=+0.273)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `58.5234` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 58.5234 (IC base=+0.141)

- **PATRÓN** `T_h` < `111.9838` → IC=+0.325 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9838 (IC base=+0.315)

- **PATRÓN** `T_h` > `88.9843` → IC=+0.315 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 88.9843 (IC base=+0.315)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `113.2461` → IC=+0.430 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 113.2461 (IC base=+0.412)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.0059 (IC=+0.222 n=16). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5321 sube el IC de +0.124 a +0.216 en UPDOWN_GBM#15min (n=410). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8845 sube el IC de +0.171 a +0.271 en UPDOWN_GBM#BTC#15min (n=81). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6314 sube el IC de +0.071 a +0.228 en UPDOWN_GBM#ETH#15min (n=79). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6136 sube el IC de +0.076 a +0.294 en UPDOWN_GBM#SOL#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4444 sube el IC de +0.107 a +0.167 en UPDOWN_GBM#XRP#15min (n=109). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1404 sube el IC de +0.035 a +0.202 en UPDOWN_GBM#XRP#15min (n=122). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5433 sube el IC de -0.072 a +0.191 en UPDOWN_GBM_15M_TARDIO (n=283). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.077 a +0.294 en UPDOWN_GBM_15M_TARDIO (n=279). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.015 a +0.300 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.4827 sube el IC de +0.051 a +0.185 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=144). Ya aplicado como kelly_boost=+0.92€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3707 sube el IC de +0.222 a +0.296 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=145). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8125 sube el IC de -0.123 a +0.206 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.057 a +0.212 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=64). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.0566 sube el IC de -0.072 a +0.318 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=20). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS > 0.2615 sube el IC de -0.072 a +0.328 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=27). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.9676 sube el IC de +0.287 a +0.363 en UPDOWN_GBM_IBS_ALTO (n=129). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9691 sube el IC de +0.284 a +0.329 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.846 sube el IC de +0.287 a +0.315 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=122). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.9108 sube el IC de +0.319 a +0.375 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=118). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8418 sube el IC de +0.307 a +0.353 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=93). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8893 sube el IC de +0.330 a +0.402 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=49). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.357 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.357 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN` — IC=+0.227 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC#5min` — IC=+0.227 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC` — IC=+0.227 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#5min` — IC=+0.227 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min` — IC=+0.150 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 682 | +0.092 | +37.74€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 682 | +0.092 | +37.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 430 | +0.116 | +28.13€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 430 | +0.116 | +28.13€ | 2 | 11 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 7 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 29 | +0.177 | +10.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 12483 | -0.105 | -2132.91€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 856 | -0.012 | -122.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 11627 | -0.112 | -2010.21€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 1641 | -0.069 | -338.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 1641 | -0.069 | -338.04€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 856 | -0.012 | -122.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 856 | -0.012 | -122.70€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 1600 | -0.153 | -495.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 1600 | -0.153 | -495.95€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 3342 | -0.063 | -298.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 3342 | -0.063 | -298.25€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 2850 | -0.113 | -300.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 2850 | -0.113 | -300.16€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2194 | -0.188 | -577.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2194 | -0.188 | -577.82€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 2122 | -0.056 | +898.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 596 | -0.003 | +318.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 1526 | -0.076 | +580.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 2122 | -0.056 | +898.35€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 596 | -0.003 | +318.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 1526 | -0.076 | +580.31€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 53 | -0.136 | -16.89€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 53 | -0.136 | -16.89€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 53 | -0.136 | -16.89€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 53 | -0.136 | -16.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 39914 | +0.114 | -2488.36€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6997 | +0.187 | -225.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 121 | -0.085 | -49.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 29342 | +0.097 | -2168.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3454 | +0.119 | -44.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 4917 | +0.075 | -723.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 22 | -0.083 | +0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | -0.089 | -6.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 4890 | +0.076 | -717.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 8116 | +0.134 | -161.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2007 | +0.202 | -72.73€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 4882 | +0.110 | -118.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1185 | +0.128 | +51.72€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 4931 | +0.083 | -591.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 24 | +0.077 | +2.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 4905 | +0.083 | -592.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 8709 | +0.127 | -127.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2559 | +0.170 | -10.67€ | 1 | 7 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 4890 | +0.113 | -81.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1248 | +0.099 | -27.31€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 8324 | +0.130 | -545.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2367 | +0.198 | -146.74€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 57 | +0.025 | -7.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 4879 | +0.096 | -321.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1021 | +0.134 | -69.22€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 4917 | +0.105 | -338.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 18 | +0.000 | +0.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 4896 | +0.106 | -338.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 6937 | +0.175 | -537.20€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 6937 | +0.175 | -537.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 1752 | +0.164 | -193.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 1752 | +0.164 | -193.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 141 | -0.129 | -1.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 141 | -0.129 | -1.63€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 1724 | +0.168 | -183.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 1724 | +0.168 | -183.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1556 | +0.233 | -44.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1556 | +0.233 | -44.48€ | 0 | 2 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 1685 | +0.185 | -128.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 1685 | +0.185 | -128.02€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 353 | +0.447 | +3.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 353 | +0.447 | +3.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 138 | +0.443 | +1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 138 | +0.443 | +1.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 127 | +0.438 | +0.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 127 | +0.438 | +0.52€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 84 | +0.442 | +1.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 84 | +0.442 | +1.60€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 20895 | +0.191 | -1842.36€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 20895 | +0.191 | -1842.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 3758 | +0.139 | -630.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 3758 | +0.139 | -630.12€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 3280 | +0.233 | -82.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 3280 | +0.233 | -82.93€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 3574 | +0.168 | -438.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 3574 | +0.168 | -438.35€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 3330 | +0.228 | -108.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 3330 | +0.228 | -108.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 3439 | +0.206 | -220.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 3439 | +0.206 | -220.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 3514 | +0.183 | -361.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 3514 | +0.183 | -361.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 7645 | +0.135 | +295.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 7645 | +0.135 | +295.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 3809 | +0.138 | +171.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 3809 | +0.138 | +171.72€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 3836 | +0.131 | +123.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 3836 | +0.131 | +123.47€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 862 | +0.296 | -1.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 862 | +0.296 | -1.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 373 | +0.279 | -10.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 373 | +0.279 | -10.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 403 | +0.300 | +7.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 403 | +0.300 | +7.94€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 86 | +0.341 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 86 | +0.341 | +1.56€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 363 | +0.415 | -15.27€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 363 | +0.415 | -15.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 164 | +0.410 | -8.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 164 | +0.410 | -8.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 166 | +0.423 | -5.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 166 | +0.423 | -5.61€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 33 | +0.357 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 33 | +0.357 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 334 | +0.095 | -2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 101 | +0.102 | -2.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 233 | +0.091 | -0.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 14 | +0.131 | +3.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 14 | +0.131 | +3.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 271 | +0.101 | +3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 38 | +0.150 | +3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 233 | +0.091 | -0.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 49 | +0.029 | -8.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 49 | +0.029 | -8.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 10201 | +0.095 | -378.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 957 | +0.065 | -35.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 9244 | +0.098 | -342.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 6417 | +0.098 | -142.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 957 | +0.065 | -35.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 5460 | +0.103 | -106.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 896 | +0.111 | +3.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 896 | +0.111 | +3.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 2888 | +0.084 | -239.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 2888 | +0.084 | -239.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 508 | +0.284 | -32.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 508 | +0.284 | -32.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 508 | +0.284 | -32.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 508 | +0.284 | -32.59€ | 0 | 4 |
| ✅ GBM_LATE_15M | 9568 | +0.046 | +3262.16€ | 0 | 14 |
| ✅ GBM_LATE_15M#15min | 9568 | +0.046 | +3262.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1384 | +0.188 | +954.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1384 | +0.188 | +954.22€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 1394 | +0.176 | +864.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1394 | +0.176 | +864.42€ | 0 | 29 |
| ✅ GBM_LATE_15M#DOGE | 1398 | +0.194 | +999.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 1398 | +0.194 | +999.54€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 1533 | -0.048 | +46.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1533 | -0.048 | +46.67€ | 4 | 10 |
| ✅ GBM_LATE_15M#SOL | 1652 | -0.057 | +141.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1652 | -0.057 | +141.89€ | 5 | 3 |
| ✅ GBM_LATE_15M#XRP | 2207 | -0.076 | +255.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2207 | -0.076 | +255.42€ | 5 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 10422 | +0.048 | +4117.54€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 10422 | +0.048 | +4117.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 1693 | -0.015 | +658.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 1693 | -0.015 | +658.35€ | 2 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2272 | -0.037 | +194.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2272 | -0.037 | +194.05€ | 1 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1258 | +0.248 | +1188.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1258 | +0.248 | +1188.21€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1679 | -0.058 | -31.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1679 | -0.058 | -31.43€ | 10 | 2 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1762 | -0.031 | +381.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1762 | -0.031 | +381.55€ | 7 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1758 | +0.255 | +1726.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1758 | +0.255 | +1726.81€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 7875 | +0.171 | +5536.78€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 7875 | +0.171 | +5536.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1060 | +0.195 | +786.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1060 | +0.195 | +786.40€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1313 | +0.167 | +911.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1313 | +0.167 | +911.29€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1072 | +0.197 | +809.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1072 | +0.197 | +809.94€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1296 | +0.154 | +825.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1296 | +0.154 | +825.03€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1475 | +0.121 | +901.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1475 | +0.121 | +901.05€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 1659 | +0.201 | +1303.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 1659 | +0.201 | +1303.06€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 1606 | +0.086 | +419.52€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 1606 | +0.086 | +419.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 56 | +0.086 | +14.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 395 | +0.049 | +80.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 395 | +0.049 | +80.77€ | 3 | 9 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 238 | +0.154 | +119.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 238 | +0.154 | +119.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 261 | +0.169 | +92.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 261 | +0.169 | +92.77€ | 2 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 334 | -0.018 | +3.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 334 | -0.018 | +3.39€ | 3 | 5 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 322 | +0.120 | +108.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 322 | +0.120 | +108.66€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO | 9285 | +0.172 | +6456.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#15min | 9285 | +0.172 | +6456.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1333 | +0.211 | +1064.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1333 | +0.211 | +1064.74€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1499 | +0.166 | +1020.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1499 | +0.166 | +1020.55€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1324 | +0.218 | +1096.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1324 | +0.218 | +1096.56€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1450 | +0.139 | +868.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1450 | +0.139 | +868.47€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1648 | +0.097 | +819.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1648 | +0.097 | +819.28€ | 0 | 16 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2031 | +0.204 | +1586.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2031 | +0.204 | +1586.84€ | 0 | 21 |
| ✅ GBM_LATE_5M | 2719 | +0.129 | +1251.13€ | 1 | 23 |
| ✅ GBM_LATE_5M#5min | 2719 | +0.129 | +1251.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 112 | +0.210 | +82.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 112 | +0.210 | +82.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 922 | +0.127 | +451.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 922 | +0.127 | +451.56€ | 1 | 17 |
| ✅ GBM_LATE_5M#DOGE | 335 | +0.171 | +202.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 335 | +0.171 | +202.98€ | 0 | 12 |
| ✅ GBM_LATE_5M#ETH | 854 | +0.133 | +383.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 854 | +0.133 | +383.13€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 139 | -0.018 | -0.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 139 | -0.018 | -0.54€ | 2 | 2 |
| ✅ GBM_LATE_5M#XRP | 357 | +0.116 | +131.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 357 | +0.116 | +131.70€ | 0 | 0 |
| ✅ GBM_LATE_60M | 574 | -0.009 | +129.23€ | 4 | 11 |
| ✅ GBM_LATE_60M#60min | 574 | -0.009 | +129.23€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 197 | +0.033 | +25.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 197 | +0.033 | +25.75€ | 2 | 8 |
| ✅ GBM_LATE_60M#ETH | 211 | +0.026 | +77.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 211 | +0.026 | +77.16€ | 2 | 10 |
| ✅ GBM_LATE_60M#SOL | 166 | -0.101 | +26.32€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 166 | -0.101 | +26.32€ | 3 | 3 |
| 🚫 GBM_LATE_60M_FADE | 197 | -0.304 | -34.30€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 197 | -0.304 | -34.30€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 78 | -0.263 | -8.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 78 | -0.263 | -8.38€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 66 | -0.353 | -19.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 66 | -0.353 | -19.56€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 53 | -0.282 | -6.35€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 53 | -0.282 | -6.35€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 381 | +0.041 | +11.63€ | 3 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 381 | +0.041 | +11.63€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 163 | +0.039 | +21.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 163 | +0.039 | +21.02€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 94 | +0.073 | -3.10€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 94 | +0.073 | -3.10€ | 1 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 124 | +0.016 | -6.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 124 | +0.016 | -6.29€ | 2 | 5 |
| ✅ LATE_WINDOW_5MIN | 31 | +0.227 | +11.99€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 31 | +0.227 | +11.99€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 31 | +0.227 | +11.99€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 31 | +0.227 | +11.99€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 370 | +0.100 | +92.85€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 370 | +0.100 | +92.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 370 | +0.100 | +92.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 370 | +0.100 | +92.85€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 274 | -0.094 | -32.24€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 274 | -0.094 | -32.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 65 | -0.082 | -7.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 65 | -0.082 | -7.05€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 60 | -0.048 | -4.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 60 | -0.048 | -4.98€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 72 | -0.027 | -3.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 72 | -0.027 | -3.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 48 | -0.180 | -9.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 48 | -0.180 | -9.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 945 | -0.021 | -23.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 945 | -0.021 | -23.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 60 | +0.000 | -2.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 60 | +0.000 | -2.56€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 130 | -0.038 | -4.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 130 | -0.038 | -4.81€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 72 | -0.095 | -7.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 72 | -0.095 | -7.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 274 | +0.011 | +7.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 274 | +0.011 | +7.17€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 349 | -0.010 | -8.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 349 | -0.010 | -8.26€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 60 | -0.113 | -7.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 60 | -0.113 | -7.62€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 501 | -0.009 | -2.02€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 501 | -0.009 | -2.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 156 | -0.044 | -11.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 156 | -0.044 | -11.59€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 153 | +0.003 | +2.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 153 | +0.003 | +2.35€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 192 | +0.010 | +7.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 192 | +0.010 | +7.22€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 5447 | -0.000 | -71.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 5447 | -0.000 | -71.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 529 | -0.005 | +1.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 529 | -0.005 | +1.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 600 | +0.003 | -9.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 600 | +0.003 | -9.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1120 | +0.011 | -11.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1120 | +0.011 | -11.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1268 | +0.008 | +12.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1268 | +0.008 | +12.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 933 | -0.009 | -32.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 933 | -0.009 | -32.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 997 | -0.013 | -32.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 997 | -0.013 | -32.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 9195 | -0.037 | +216.95€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 9195 | -0.037 | +216.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 1469 | -0.034 | +153.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 1469 | -0.034 | +153.82€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 1625 | -0.030 | -32.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 1625 | -0.030 | -32.43€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 1485 | -0.047 | +83.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 1485 | -0.047 | +83.03€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 1580 | -0.036 | -19.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 1580 | -0.036 | -19.40€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 1531 | -0.040 | +37.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 1531 | -0.040 | +37.73€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 1505 | -0.036 | -5.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 1505 | -0.036 | -5.81€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 556 | -0.061 | -42.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 556 | -0.061 | -42.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 104 | -0.038 | -5.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 104 | -0.038 | -5.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 67 | -0.065 | -5.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 67 | -0.065 | -5.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 108 | -0.118 | -14.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 108 | -0.118 | -14.05€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 140 | -0.028 | -6.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 101 | -0.044 | -7.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 101 | -0.044 | -7.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3171 | +0.004 | -4.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3171 | +0.004 | -4.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 126 | -0.039 | -1.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 126 | -0.039 | -1.34€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1160 | +0.008 | +7.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1160 | +0.008 | +7.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1386 | +0.006 | -1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1386 | +0.006 | -1.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 178 | -0.006 | -5.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 25441 | -0.079 | +399.47€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 25441 | -0.079 | +399.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 4046 | -0.091 | +388.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 4046 | -0.091 | +388.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 4341 | -0.074 | -100.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 4341 | -0.074 | -100.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 4152 | -0.084 | +82.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 4152 | -0.084 | +82.59€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 3857 | -0.099 | -197.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 3857 | -0.099 | -197.05€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 4761 | -0.053 | +72.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 4761 | -0.053 | +72.91€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 4284 | -0.076 | +152.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 4284 | -0.076 | +152.79€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6012 | -0.010 | -119.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 992 | -0.018 | -21.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 992 | -0.018 | -21.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1204 | +0.000 | -15.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1204 | +0.000 | -15.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1001 | -0.019 | -30.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1001 | -0.019 | -30.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1310 | -0.002 | -14.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1310 | -0.002 | -14.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 780 | -0.010 | -14.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 725 | -0.020 | -23.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 725 | -0.020 | -23.89€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 600 | +0.101 | +166.48€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 464 | +0.114 | +153.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 113 | +0.109 | +42.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 113 | +0.109 | +42.29€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 91 | +0.102 | +22.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 91 | +0.102 | +22.47€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 86 | +0.114 | +31.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 86 | +0.114 | +31.36€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 79 | +0.142 | +35.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 79 | +0.142 | +35.66€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 95 | +0.098 | +22.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 95 | +0.098 | +22.12€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 273 | -0.162 | -26.18€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 122 | -0.242 | -36.11€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 107 | -0.271 | -35.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 15 | -0.022 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 103 | -0.129 | -4.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 84 | -0.140 | -7.57€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 19 | -0.068 | +2.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 48 | -0.020 | +14.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 41 | -0.012 | +13.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 7 | -0.019 | +0.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 232 | -0.179 | -28.98€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 41 | -0.058 | +2.80€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 239 | -0.209 | +0.65€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 100 | -0.137 | +4.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 98 | -0.130 | +5.21€ | 0 | 2 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 92 | -0.298 | -20.74€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 88 | -0.300 | -22.13€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 47 | -0.173 | +17.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 45 | -0.160 | +19.03€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 231 | -0.204 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 8 | -0.120 | -1.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 82 | +0.345 | +22.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 21 | +0.326 | +3.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 21 | +0.326 | +3.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 44 | +0.478 | +21.92€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 44 | +0.478 | +21.92€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 82 | +0.345 | +22.35€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 191 | +0.039 | +3.22€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 191 | +0.039 | +3.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 84 | +0.035 | -0.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 84 | +0.035 | -0.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 12 | +0.043 | +0.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 12 | +0.043 | +0.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 19 | +0.113 | +1.96€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 19 | +0.113 | +1.96€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 76 | +0.013 | +0.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 76 | +0.013 | +0.51€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1433 | -0.025 | -67.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1433 | -0.025 | -67.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 507 | -0.009 | -11.54€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 507 | -0.009 | -11.54€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 507 | -0.019 | -19.50€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 507 | -0.019 | -19.50€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 135 | -0.040 | -12.98€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 135 | -0.040 | -12.98€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 284 | -0.056 | -23.42€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 284 | -0.056 | -23.42€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 40 | -0.024 | -1.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 40 | -0.024 | -1.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 24 | -0.115 | -3.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 24 | -0.115 | -3.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 16 | +0.089 | +1.64€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 16 | +0.089 | +1.64€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 2942 | +0.026 | +58.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 2942 | +0.026 | +58.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 968 | +0.027 | +13.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 968 | +0.027 | +13.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 570 | +0.032 | +17.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 570 | +0.032 | +17.06€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 881 | +0.020 | +5.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 881 | +0.020 | +5.11€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 523 | +0.029 | +22.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 523 | +0.029 | +22.37€ | 2 | 1 |
| ✅ STRUCT_NO_15M | 3626 | +0.009 | -30.52€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 3626 | +0.009 | -30.52€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1391 | +0.010 | -12.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1391 | +0.010 | -12.35€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1428 | +0.018 | -0.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1428 | +0.018 | -0.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 807 | -0.007 | -17.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 807 | -0.007 | -17.93€ | 2 | 0 |
| ✅ UPDOWN_GBM | 7426 | +0.004 | +159.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2651 | +0.038 | +239.32€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 296 | +0.017 | +2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 3985 | -0.015 | -75.96€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 447 | -0.008 | -5.70€ | 3 | 1 |
| ✅ UPDOWN_GBM#BNB | 196 | +0.091 | +38.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 179 | +0.119 | +42.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 8 | -0.040 | -1.01€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BNB#5min | 9 | -0.102 | -2.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 1610 | +0.014 | +74.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 263 | +0.089 | +54.18€ | 3 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 87 | +0.073 | +7.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1099 | -0.001 | +17.02€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 143 | -0.031 | -6.52€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 834 | -0.006 | -2.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 123 | +0.100 | +28.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 9 | +0.021 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 702 | -0.026 | -31.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1762 | -0.004 | -15.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 804 | +0.015 | +10.77€ | 1 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 86 | +0.045 | +3.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 656 | -0.033 | -28.79€ | 4 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 201 | +0.007 | +0.05€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 1961 | -0.002 | -7.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 655 | -0.002 | -2.10€ | 1 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 73 | +0.007 | -1.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1118 | +0.001 | -4.42€ | 4 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 103 | -0.005 | +0.77€ | 2 | 2 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1061 | +0.009 | +73.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 627 | +0.052 | +105.85€ | 0 | 8 |
| ✅ UPDOWN_GBM#XRP#240min | 33 | -0.157 | -6.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 401 | -0.043 | -26.02€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 236 | +0.319 | +51.36€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 236 | +0.319 | +51.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 138 | +0.307 | +21.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 138 | +0.307 | +21.53€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 98 | +0.330 | +29.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 98 | +0.330 | +29.83€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 4646 | -0.076 | +893.65€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 4646 | -0.076 | +893.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 303 | -0.051 | +341.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 940 | -0.167 | -111.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 940 | -0.167 | -111.77€ | 5 | 2 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 78 | +0.062 | +12.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 78 | +0.062 | +12.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 384 | +0.137 | +173.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 384 | +0.137 | +173.09€ | 2 | 16 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1515 | -0.070 | +274.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1515 | -0.070 | +274.31€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1426 | -0.093 | +203.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1426 | -0.093 | +203.90€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 34 | +0.000 | -1.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 34 | +0.000 | -1.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 34 | +0.000 | -1.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 34 | +0.000 | -1.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 378 | +0.287 | +293.81€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 378 | +0.287 | +293.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 216 | +0.284 | +165.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 216 | +0.284 | +165.23€ | 0 | 13 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 162 | +0.287 | +128.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 162 | +0.287 | +128.59€ | 0 | 11 |
| ✅ UPDOWN_OU_5M | 598 | -0.097 | -67.78€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 598 | -0.097 | -67.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 296 | -0.070 | -31.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 296 | -0.070 | -31.88€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 146 | -0.047 | -7.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 146 | -0.047 | -7.54€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 30 | -0.188 | -6.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 30 | -0.188 | -6.21€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 51 | -0.141 | -6.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 51 | -0.141 | -6.51€ | 2 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 42 | -0.227 | -8.83€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 42 | -0.227 | -8.83€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1208 | +0.293 | +527.26€ | 0 | 5 |
| ✅ WEEKLY_PRICE#BTC | 369 | +0.214 | +11.32€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 389 | +0.272 | +112.70€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 450 | +0.372 | +403.23€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.088) — sin ventaja clara. oversold(IBS<0.3): IC=+0.018 n=2651 | neutral: IC=-0.001 n=2836 | overbought(IBS>0.7): IC=+0.087 n=2965
  - _Datos_: n=8804 IC=+0.036 PNL=+806.97€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: (cache 204s) 48 celda(s) GATE OK de 2271 trackeadas

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.002 < 0.08 — monitorear
  - _Datos_: n=655 IC=-0.002 PNL=-2.10€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=389/15 IC=+0.272 PNL=+112.70€ | BTC: n=369/15 IC=+0.214 PNL=+11.32€ | SOL: n=450/15 IC=+0.372 PNL=+403.23€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.072 n=124217 | tras_1loss IC=+0.044 n=97603 | tras_2loss IC=+0.006 n=44424/40 | gap=+0.066 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 20 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC
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
  - _Estado_: 7364 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.115 n=50/60 | contraria IC=+0.033 n=28 | gap=+0.082 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=115, boost estimado=+0.023. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 79 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=201/40 IC=+0.007 PNL=+0.05€ | BTC#60min: n=143/40 IC=-0.031 PNL=-6.52€ | SOL#60min: n=103/40 IC=-0.005 PNL=+0.77€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.013 n=774 | contrario_BTC IC=-0.022 n=599/40 | gap=-0.010 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.08 con n=77 PNL=+50.02€
  - _Datos_: n=77 IC=+0.196 PNL=+50.02€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.143 > 0.08 con n=96 PNL=+27.92€
  - _Datos_: n=96 IC=+0.143 PNL=+27.92€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 19/25 ops en el filtro definido (IC actual=+0.249 PNL=+14.35€)
  - _Datos_: n=19 IC=+0.249 PNL=+14.35€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.336 > 0.1 con n=1024 PNL=+531.44€
  - _Datos_: n=1024 IC=+0.336 PNL=+531.44€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=65 IC=+0.037 PNL=+11.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=65 IC=+0.037 PNL=+11.42€

**⏳ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: 30
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: 24/30 ops en el filtro definido (IC actual=+0.192 PNL=+15.20€)
  - _Datos_: n=24 IC=+0.192 PNL=+15.20€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=7149 IC=+0.001 PNL=+105.54€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=7149 IC=+0.001 PNL=+105.54€

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
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=371 IC=+0.007 PNL=+0.95€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=371 IC=+0.007 PNL=+0.95€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=76 IC=-0.077 PNL=-6.65€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=76 IC=-0.077 PNL=-6.65€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.083 < -0.08 con n=130 PNL=-10.38€
  - _Datos_: n=130 IC=-0.083 PNL=-10.38€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.1 con n=546 PNL=+146.00€
  - _Datos_: n=546 IC=+0.124 PNL=+146.00€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=194 IC=+0.076 PNL=+41.53€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=194 IC=+0.076 PNL=+41.53€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=263 IC=+0.089 PNL=+54.18€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=263 IC=+0.089 PNL=+54.18€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=1538 IC=+0.027 PNL=+100.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1538 IC=+0.027 PNL=+100.91€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 27/30 ops en el filtro definido (IC actual=-0.224 PNL=-5.54€)
  - _Datos_: n=27 IC=-0.224 PNL=-5.54€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=84 IC=-0.046 PNL=+6.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=84 IC=-0.046 PNL=+6.24€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=100 IC=+0.010 PNL=+5.99€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=100 IC=+0.010 PNL=+5.99€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.037 PNL=+1.09€)
  - _Datos_: n=6 IC=+0.037 PNL=+1.09€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2297 IC=-0.023 PNL=-61.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2297 IC=-0.023 PNL=-61.13€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=38 PNL=+9.28€
  - _Datos_: n=38 IC=+0.175 PNL=+9.28€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.227 n=31) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=31 IC=+0.227 PNL=+11.99€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=1935 IC=+0.016 PNL=+88.52€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1935 IC=+0.016 PNL=+88.52€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=503 IC=+0.027 PNL=+2.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=503 IC=+0.027 PNL=+2.60€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.08 con n=163 PNL=+40.32€
  - _Datos_: n=163 IC=+0.106 PNL=+40.32€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=136 PNL=+2.57€
  - _Datos_: n=136 IC=+0.116 PNL=+2.57€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.135 > 0.08 con n=124 PNL=+40.89€
  - _Datos_: n=124 IC=+0.135 PNL=+40.89€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=26823 IC=+0.102 PNL=+8465.96€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=26823 IC=+0.102 PNL=+8465.96€

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
  - _Estado_: n=979 IC=+0.031 PNL=+55.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=979 IC=+0.031 PNL=+55.44€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=327 PNL=+98.69€
  - _Datos_: n=327 IC=+0.117 PNL=+98.69€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.445 > 0.1 con n=648 PNL=+567.92€
  - _Datos_: n=648 IC=+0.445 PNL=+567.92€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1719 IC=+0.024 PNL=+103.24€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1719 IC=+0.024 PNL=+103.24€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=831 PNL=+313.57€
  - _Datos_: n=831 IC=+0.166 PNL=+313.57€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 37/40 ops en el filtro definido (IC actual=-0.269 PNL=-7.97€)
  - _Datos_: n=37 IC=-0.269 PNL=-7.97€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=484 IC=+0.035 PNL=+55.78€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=484 IC=+0.035 PNL=+55.78€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.1 con n=81 PNL=+9.72€
  - _Datos_: n=81 IC=+0.102 PNL=+9.72€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=5976 IC=-0.146 PNL=+211.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=5976 IC=-0.146 PNL=+211.74€

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
  - _Estado_: n=734 IC=+0.143 PNL=+338.47€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=734 IC=+0.143 PNL=+338.47€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.08 con n=546 PNL=+146.00€
  - _Datos_: n=546 IC=+0.124 PNL=+146.00€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=750 IC=+0.001 PNL=+2.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=750 IC=+0.001 PNL=+2.66€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=730 PNL=+375.47€
  - _Datos_: n=730 IC=+0.083 PNL=+375.47€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=162 PNL=+59.16€
  - _Datos_: n=162 IC=+0.171 PNL=+59.16€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.244 < -0.1 con n=658 PNL=-89.89€
  - _Datos_: n=658 IC=-0.244 PNL=-89.89€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1616 IC=+0.124 PNL=+838.63€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1616 IC=+0.124 PNL=+838.63€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 39/40 ops en el filtro definido (IC actual=+0.085 PNL=+9.49€)
  - _Datos_: n=39 IC=+0.085 PNL=+9.49€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=778 IC=-0.024 PNL=+56.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=778 IC=-0.024 PNL=+56.29€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.183 > 0.08 con n=688 PNL=+429.19€
  - _Datos_: n=688 IC=+0.183 PNL=+429.19€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1160 IC=-0.069 PNL=+137.17€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1160 IC=-0.069 PNL=+137.17€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=282 PNL=-38.18€
  - _Datos_: n=282 IC=+0.116 PNL=-38.18€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.234 > 0.08 con n=1721 PNL=-169.04€
  - _Datos_: n=1721 IC=+0.234 PNL=-169.04€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 12/40 ops en el filtro definido (IC actual=-0.043 PNL=+0.42€)
  - _Datos_: n=12 IC=-0.043 PNL=+0.42€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=194) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=194 IC=+0.102 PNL=+44.87€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.342 > 0.08 con n=80 PNL=+50.95€
  - _Datos_: n=80 IC=+0.342 PNL=+50.95€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.429 n=251) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=251 IC=+0.429 PNL=+344.17€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=3758 IC=+0.139 PNL=-630.12€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=3758 IC=+0.139 PNL=-630.12€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.1 con n=47 PNL=+29.24€
  - _Datos_: n=47 IC=+0.214 PNL=+29.24€
