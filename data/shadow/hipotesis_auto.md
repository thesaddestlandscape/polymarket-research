# Hipótesis automáticas — 2026-09-15 12:47 UTC
_Generado por shadow_postmortem.py sobre 451529 resoluciones (PNL=+48358.63€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=421)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=407)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.252 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.201 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 67.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.804` → IC=+0.256 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.804 (IC base=+0.121)

- **PATRÓN** `banda_z` > `10.429` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.429 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.136 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=496)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.157 (n=138)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 98.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.121 (n=407)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.122 (n=133)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 97.0 (IC base=+0.037)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.385` → IC=-0.131 (n=155)

  - _Acción_: SKIP cuando `py_entrada` < 0.385
  - _Potencial_: sin este filtro IC_bueno=+0.249 (n=329)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.385` → IC=+0.249 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.385 (IC base=+0.128)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.210 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.8017` → IC=+0.271 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8017 (IC base=+0.128)

- **PATRÓN** `banda_z` > `11.461` → IC=+0.256 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.461 (IC base=+0.128)

- **PATRÓN** `ballenas_wallet_edge_medio` > `3.005` → IC=+0.136 (n=116)

  - _Acción_: Kelly boost +0.68€ cuando `ballenas_wallet_edge_medio` > 3.005 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=411)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 88.0 (IC base=+0.034)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.213 (n=99)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=85)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=84)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=95)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.250 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.105)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.105)

- **PATRÓN** `banda_z` > `6.169` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 6.169 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `1162.8377` → IC=+0.151 (n=64)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1162.8377 (IC base=+0.105)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.189)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2692.3774` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2692.3774 (IC base=+0.189)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `145.96` → IC=-0.256 (n=5629)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.96
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=16894)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.82` → IC=-0.288 (n=785)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.82
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=2355)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `484.43` → IC=-0.165 (n=302)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 484.43
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=909)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `134.98` → IC=-0.286 (n=700)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.98
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2103)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `141.07` → IC=-0.158 (n=1452)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.07
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=4359)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.37` → IC=-0.252 (n=1326)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.37
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3979)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `157.73` → IC=-0.334 (n=1403)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.73
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=2850)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.38` → IC=-0.271 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=295)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=94)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=312)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.276 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=180)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.269 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=26)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=79)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.195 (n=11499)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.69 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=2850)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5226.7593` → IC=+0.167 (n=1819)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5226.7593 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=8683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=10539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.245 (n=7760)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=5644)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7144.005` → IC=+0.176 (n=1784)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7144.005 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.350 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `10962.1513` → IC=+0.203 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10962.1513 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.210 (n=1218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.209 (n=1343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.274 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `12932.3181` → IC=+0.211 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12932.3181 (IC base=+0.203)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.179 (n=269)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.62 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=285)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `4643.6334` → IC=+0.149 (n=229)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4643.6334 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.175 (n=420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 11.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.166 (n=558)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.425 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=542)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `3846.6396` → IC=+0.158 (n=419)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3846.6396 (IC base=+0.134)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=159)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.326 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.301 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.242 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `3739.174` → IC=+0.240 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3739.174 (IC base=+0.237)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=558)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.131 (n=537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 17.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.218 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=629)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1940.1614` → IC=+0.159 (n=356)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1940.1614 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.082)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=1069)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.423 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.269 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.181 (n=1103)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.03 (IC base=+0.177)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.170 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 13.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.338 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.180 (n=179)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.141 (n=673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.228 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=325)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.124)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=8921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=8575)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.218 (n=3184)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `5296.2198` → IC=+0.343 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5296.2198 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.178 (n=2222)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.167)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.329 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.297 (n=156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.354 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.294)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=2205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.180 (n=2110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.181 (n=1887)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=1684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.320 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.304 (n=49)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=1836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.192 (n=1534)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.438 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.436 (n=355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `2060.1801` → IC=+0.443 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.1801 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.437 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.443 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.454 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `11667.7741` → IC=+0.452 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11667.7741 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.452 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.462 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.440 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `3860.0656` → IC=+0.444 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3860.0656 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.410 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` < `0.795` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=18)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=19)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=26384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.236 (n=10128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=5400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=4581)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=4851)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.168)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=4696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=4695)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.271 (n=1694)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=2533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=4865)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.168)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=1685)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=4366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=4329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.254 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=1908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=3567)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.248 (n=1795)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.190)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.202 (n=4025)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.06` → IC=+0.133 (n=3662)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.06 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.146 (n=4086)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.94 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=4850)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.150 (n=3667)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.33 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=2027)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.130)

- **PATRÓN** `restante_min` < `3.99` → IC=+0.136 (n=1815)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 3.99 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.145 (n=1933)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.93 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=2396)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `4.22` → IC=+0.148 (n=1815)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 4.22 (IC base=+0.130)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=1998)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.125 (n=2453)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.147 (n=1864)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=2454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `4.41` → IC=+0.145 (n=2436)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 4.41 (IC base=+0.119)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1614.3793` → IC=+0.297 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1614.3793 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.274)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.325 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `5072.5083` → IC=+0.290 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5072.5083 (IC base=+0.274)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.290 (n=440)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.382 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `1492.929` → IC=+0.312 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1492.929 (IC base=+0.290)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.436 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.431 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `1854.0504` → IC=+0.437 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1854.0504 (IC base=+0.430)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.436 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=191)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.432 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.429)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.437 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.447 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.431 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.433 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `2127.0131` → IC=+0.454 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2127.0131 (IC base=+0.432)

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
- **PATRÓN** `ibs_20min` > `0.9773` → IC=+0.230 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9773 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.6046` → IC=+0.243 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6046 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.718` → IC=+0.154 (n=3276)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.718 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.251 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6141 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.0681` → IC=+0.248 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0681 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1751` → IC=+0.191 (n=4046)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1751 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.3093` → IC=+0.202 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3093 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.472` → IC=+0.195 (n=3906)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.472 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.57` → IC=+0.130 (n=7362)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.57 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.5669` → IC=+0.182 (n=451)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.5669 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.3425` → IC=+0.168 (n=2494)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3425 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.8696` → IC=+0.174 (n=1579)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8696 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2457` → IC=+0.220 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2457 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `1.4638` → IC=+0.198 (n=3943)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4638 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.206 (n=3714)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.059)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.186 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0049 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.186 (n=450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0076 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.188 (n=668)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 8.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.069` → IC=+0.279 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.069 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.201 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.166 (n=1236)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=1222)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=898)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.274 (n=671)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.252 (n=682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0571` → IC=+0.289 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0571 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.363` → IC=+0.246 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.363 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0688` → IC=+0.233 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0688 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2883` → IC=+0.266 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2883 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.7352` → IC=+0.266 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7352 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=1027)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1578.8947` → IC=+0.248 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1578.8947 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.221 (n=894)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.239 (n=446)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=1064)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9238` → IC=+0.255 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9238 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2116` → IC=+0.220 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2116 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.769` → IC=+0.238 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.769 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2628` → IC=+0.222 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2628 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.8751` → IC=+0.215 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8751 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.0994` → IC=+0.218 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0994 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4925` → IC=+0.225 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4925 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.3949` → IC=+0.219 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3949 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `11871.8913` → IC=+0.227 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11871.8913 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.161 (n=960)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0048 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.169 (n=364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.171 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6717` → IC=+0.179 (n=1090)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6717 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.132` → IC=+0.158 (n=979)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.132 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.496` → IC=+0.177 (n=187)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.496 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.151 (n=1090)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.204 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6855` → IC=+0.144 (n=974)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6855 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.193 (n=291)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.155 (n=982)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `13051.2772` → IC=+0.157 (n=727)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 13051.2772 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `308.0` → IC=+0.156 (n=600)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 308.0 (IC base=+0.142)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.187 (n=1313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0057 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=1384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.186 (n=657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 8.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.457` → IC=+0.231 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.457 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.182 (n=1109)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.3763` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.3763 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `3.0251` → IC=+0.192 (n=556)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 3.0251 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.189 (n=1495)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.217 (n=761)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.3824` → IC=+0.231 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3824 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.68` → IC=+0.233 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.68 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.389` → IC=+0.214 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.389 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.268 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.8406` → IC=+0.200 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8406 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.289` → IC=+0.223 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.289 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1891.307` → IC=+0.230 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1891.307 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.211 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.213)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1662)

- **PATRÓN** `ibs_20min` > `0.9299` → IC=+0.167 (n=280)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9299 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.3351` → IC=+0.335 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3351 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.6419` → IC=+0.333 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6419 (IC base=+0.007)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.272` → IC=+0.135 (n=521)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 4.272 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.5993` → IC=+0.378 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5993 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.363 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1929 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.362 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.3975` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3975 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.8203` → IC=+0.342 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8203 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.343 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 167.0 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.1628` → IC=+0.193 (n=187)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1628 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` < `0.4587` → IC=+0.144 (n=600)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4587 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `0.8572` → IC=+0.151 (n=353)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8572 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `1.1639` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1639 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.225 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `1.5064` → IC=+0.181 (n=427)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.5064 (IC base=+0.000)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.140 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=234)

- **FILTRO** `ibs_20min` < `0.3636` → IC=-0.174 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3636
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=189)

- **FILTRO** `ibs_20min` > `0.2727` → IC=-0.128 (n=1702)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=843)

- **FILTRO** `sigma_ewma_delta_pct` > `8.618` → IC=-0.199 (n=277)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.618
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2268)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `1.1883` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1883 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4558` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4558 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.5788` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5788 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.7744` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7744 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.9536` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9536 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `1.4528` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4528 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6927` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6927 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` < `1.1047` → IC=+0.199 (n=207)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.1047 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` > `0.9112` → IC=+0.185 (n=157)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.9112 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.2029` → IC=+0.204 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2029 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.4885` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4885 (IC base=-0.046)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6434` → IC=-0.187 (n=420)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6434
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1262)

- **FILTRO** `ibs_20min` < `0.7753` → IC=-0.140 (n=1261)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7753
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=421)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=376)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=1306)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.200 (n=635)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1911)

- **PATRÓN** `dist_vwap_pct` > `0.9583` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9583 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.2555` → IC=+0.290 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2555 (IC base=-0.086)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.286 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=-0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.086)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.265 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=-0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.8242` → IC=+0.281 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8242 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `0.7702` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7702 (IC base=-0.029)

- **PATRÓN** `dist_vwap_pct` < `0.26` → IC=+0.241 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.26 (IC base=-0.029)

- **PATRÓN** `volumen_regimen` < `0.7344` → IC=+0.239 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7344 (IC base=-0.029)

- **PATRÓN** `volumen_regimen` > `1.0829` → IC=+0.297 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0829 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1065` → IC=+0.254 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1065 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.24` → IC=+0.254 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.24 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.4747` → IC=+0.237 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4747 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.237 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.176 (n=2498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.009 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.8815` → IC=+0.263 (n=3395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8815 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `1.0117` → IC=+0.283 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0117 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.503` → IC=+0.142 (n=3537)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.503 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` > `0.6786` → IC=+0.234 (n=2266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6786 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2487` → IC=+0.257 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2487 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.4779` → IC=+0.237 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4779 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.7839` → IC=+0.234 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7839 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.276 (n=3515)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.085)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.138 (n=2561)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0083 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.557` → IC=+0.149 (n=6738)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.557 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.6784` → IC=+0.247 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6784 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.1662` → IC=+0.229 (n=1896)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1662 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `1.1988` → IC=+0.255 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1988 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.2511` → IC=+0.323 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2511 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.6229` → IC=+0.252 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6229 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `2.3723` → IC=+0.255 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3723 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.253 (n=2544)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.067)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `2.601` → IC=-0.148 (n=512)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.601
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1160)

- **PATRÓN** `ibs_20min` > `0.8641` → IC=+0.248 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8641 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.283` → IC=+0.150 (n=687)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.283 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.8494` → IC=+0.199 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8494 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.6662` → IC=+0.197 (n=173)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6662 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` < `0.1673` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1673 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.9827` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9827 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.7276` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7276 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8296` → IC=-0.148 (n=563)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8296
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1696)

- **PATRÓN** `dist_vwap_pct` > `0.3024` → IC=+0.140 (n=248)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.3024 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `0.6545` → IC=+0.132 (n=577)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6545 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.159 (n=209)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.186 (n=205)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 235.0 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` < `0.1592` → IC=+0.215 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1592 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.1336` → IC=+0.234 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1336 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.777` → IC=+0.232 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.777 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1553` → IC=+0.226 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1553 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `504.0` → IC=+0.212 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 504.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.268 (n=1065)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.247 (n=397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.254 (n=449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.771` → IC=+0.271 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.771 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.11` → IC=+0.255 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.11 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8725` → IC=+0.240 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8725 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `3.6325` → IC=+0.249 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6325 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.293 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.322 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.285 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.884` → IC=+0.296 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.884 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.309 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` < `1.6226` → IC=+0.278 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6226 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.2115` → IC=+0.282 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2115 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `1881.2284` → IC=+0.296 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.2284 (IC base=+0.277)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.274 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.277)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2435` → IC=-0.213 (n=339)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2435
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1018)

- **FILTRO** `ibs_20min` > `0.816` → IC=-0.181 (n=447)

  - _Acción_: SKIP cuando `ibs_20min` > 0.816
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=1343)

- **PATRÓN** `ibs_20min` > `0.8012` → IC=+0.144 (n=462)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.8012 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.3046` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3046 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.9565` → IC=+0.206 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9565 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` > `0.6183` → IC=+0.189 (n=271)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.6183 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.2683` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2683 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4842` → IC=+0.252 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4842 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.7422` → IC=+0.218 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7422 (IC base=-0.017)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.250 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 118.0 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.180 (n=98)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.122 (IC base=-0.020)

- **PATRÓN** `dist_vwap_pct` < `0.4535` → IC=+0.156 (n=242)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.4535 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` < `0.9712` → IC=+0.165 (n=192)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.9712 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` > `0.7126` → IC=+0.170 (n=195)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.7126 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.1565` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1565 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.254 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.233 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.206 (n=810)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.251 (n=822)

- **FILTRO** `ibs_20min` > `0.7187` → IC=-0.235 (n=429)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7187
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=1302)

- **FILTRO** `sigma_ewma_delta_pct` > `4.704` → IC=-0.168 (n=405)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.704
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1326)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.251 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7667` → IC=+0.340 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7667 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8618` → IC=+0.287 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8618 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.7204` → IC=+0.273 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7204 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1089` → IC=+0.276 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1089 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.314 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.4402` → IC=+0.276 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4402 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.320 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.128 (n=869)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.4 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` > `0.5672` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5672 (IC base=+0.002)

- **PATRÓN** `dist_vwap_pct` < `0.3848` → IC=+0.180 (n=361)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3848 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` < `0.7176` → IC=+0.234 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7176 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.180 (n=314)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.22` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.22 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.5839` → IC=+0.201 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5839 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.5045` → IC=+0.179 (n=322)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.5045 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.213 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.015` → IC=+0.321 (n=685)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.284 (n=485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.343 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.2632` → IC=+0.315 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2632 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.294 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` > `0.6873` → IC=+0.286 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6873 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.298 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `2.5542` → IC=+0.271 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5542 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.2072` → IC=+0.272 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2072 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.270 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `2580.3091` → IC=+0.274 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2580.3091 (IC base=+0.267)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.277 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0071 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0202` → IC=+0.298 (n=508)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0202 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.282 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.386` → IC=+0.304 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.386 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.5418` → IC=+0.285 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5418 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` < `0.8998` → IC=+0.267 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8998 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.438` → IC=+0.288 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.438 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` > `1.2434` → IC=+0.313 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2434 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2419` → IC=+0.355 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2419 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `2.5563` → IC=+0.264 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5563 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.1719` → IC=+0.264 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1719 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.268 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `2559.8293` → IC=+0.274 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2559.8293 (IC base=+0.267)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.178 (n=1981)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0047 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.200 (n=1977)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.332` → IC=+0.172 (n=5217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.332 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=6186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6957` → IC=+0.229 (n=5296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6957 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1641` → IC=+0.198 (n=2593)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1641 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.219` → IC=+0.249 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.219 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2155` → IC=+0.163 (n=3956)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2155 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.159 (n=3956)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6248 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1067` → IC=+0.186 (n=2322)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1067 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.3086` → IC=+0.167 (n=4953)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.3086 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6758` → IC=+0.167 (n=1876)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.6758 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.172 (n=1976)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.183 (n=4840)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 123.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.187 (n=3833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0063 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0788` → IC=+0.207 (n=1915)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0788 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=2742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4585` → IC=+0.227 (n=5742)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4585 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2233` → IC=+0.162 (n=4246)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2233 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.27` → IC=+0.193 (n=996)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.27 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1845` → IC=+0.155 (n=4195)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1845 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6264` → IC=+0.152 (n=4195)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6264 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.228 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5742` → IC=+0.172 (n=2239)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5742 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6482` → IC=+0.178 (n=1696)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6482 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.171 (n=4706)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 126.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.216 (n=333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.205 (n=456)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3129` → IC=+0.203 (n=997)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3129 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.215 (n=499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.097` → IC=+0.307 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.097 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.238 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.5605` → IC=+0.182 (n=904)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.5605 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.182 (n=904)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.239 (n=637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.248 (n=646)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.295 (n=482)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.241 (n=725)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.1053` → IC=+0.273 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1053 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.041` → IC=+0.252 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.041 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.07` → IC=+0.236 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.07 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.255 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8745` → IC=+0.250 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8745 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6638` → IC=+0.240 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6638 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1585.6447` → IC=+0.253 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1585.6447 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.245 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.2644` → IC=+0.175 (n=756)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2644 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.200 (n=588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4339` → IC=+0.224 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4339 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.2171` → IC=+0.214 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2171 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.681` → IC=+0.227 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.681 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.268` → IC=+0.176 (n=859)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.268 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.190 (n=188)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.198 (n=276)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `9812.7811` → IC=+0.182 (n=859)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9812.7811 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `407.0` → IC=+0.160 (n=687)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 407.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.182 (n=862)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0049 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2259` → IC=+0.173 (n=860)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2259 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.167 (n=896)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5226` → IC=+0.196 (n=977)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5226 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.170 (n=985)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.1` → IC=+0.217 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.1 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.166 (n=977)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.204 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.188 (n=299)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.162 (n=868)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.158 (n=261)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 230.0 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.197 (n=978)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0058 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1938` → IC=+0.196 (n=652)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1938 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=455)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.584` → IC=+0.265 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.584 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.185 (n=801)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2187` → IC=+0.187 (n=282)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2187 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.6803` → IC=+0.186 (n=304)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.6803 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `3.6503` → IC=+0.203 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6503 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.224 (n=727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.223 (n=737)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0898` → IC=+0.248 (n=276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0898 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.272 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.3443` → IC=+0.250 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3443 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.268 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.277 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `3.5269` → IC=+0.245 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5269 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1890.8984` → IC=+0.236 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1890.8984 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.205 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.181 (n=825)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.4219` → IC=+0.168 (n=935)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4219 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.165 (n=940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.4079` → IC=+0.203 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4079 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1347` → IC=+0.195 (n=620)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1347 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.181` → IC=+0.243 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.181 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8629` → IC=+0.161 (n=624)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8629 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1956` → IC=+0.178 (n=312)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.1956 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.170 (n=304)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.5331` → IC=+0.186 (n=304)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5331 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7289.8412` → IC=+0.193 (n=623)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7289.8412 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.162 (n=768)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 154.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.162 (n=886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.006 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3751` → IC=+0.143 (n=1006)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3751 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6027` → IC=+0.179 (n=1006)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6027 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.3365` → IC=+0.139 (n=1099)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.3365 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.114` → IC=+0.190 (n=198)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 12.114 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8596` → IC=+0.140 (n=671)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8596 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.6121` → IC=+0.129 (n=1007)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6121 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.196 (n=146)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.133 (n=594)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.7994 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4836` → IC=+0.142 (n=297)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4836 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `9950.2818` → IC=+0.153 (n=456)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 9950.2818 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.149 (n=739)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0077 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5156` → IC=+0.195 (n=1107)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5156 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0114` → IC=+0.233 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0114 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.465` → IC=+0.253 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.465 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2184` → IC=+0.121 (n=1107)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2184 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.8007` → IC=+0.126 (n=710)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8007 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1138)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2897.5388` → IC=+0.193 (n=502)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2897.5388 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.134 (n=805)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.152 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.174 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5429` → IC=+0.206 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5429 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.692` → IC=+0.145 (n=201)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.692 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.191` → IC=+0.135 (n=1010)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.191 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.335` → IC=+0.157 (n=234)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 7.335 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.0388` → IC=+0.128 (n=966)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0388 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.184 (n=131)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4645` → IC=+0.132 (n=319)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4645 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.1727` → IC=+0.137 (n=433)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.1727 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3071.3046` → IC=+0.160 (n=366)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3071.3046 (IC base=+0.113)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` < `0.027` → IC=+0.201 (n=1057)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.027 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.208 (n=704)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.220 (n=465)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.7209` → IC=+0.254 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7209 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `1.2285` → IC=+0.232 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2285 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.342` → IC=+0.242 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.342 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.204 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2075 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.6122` → IC=+0.209 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6122 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.1692` → IC=+0.257 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1692 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.1918` → IC=+0.213 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1918 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.43` → IC=+0.205 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.43 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.200 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2555.945` → IC=+0.201 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2555.945 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.238 (n=372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.213 (n=506)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.022 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.222 (n=372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=515)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.0244` → IC=+0.304 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0244 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1297` → IC=+0.221 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1297 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.265` → IC=+0.204 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.265 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.305` → IC=+0.234 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.305 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6302` → IC=+0.218 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6302 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.283 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2444` → IC=+0.198 (n=862)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.2444 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4614` → IC=+0.191 (n=980)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4614 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2524.095` → IC=+0.212 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2524.095 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.148 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.157 (n=473)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0087 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.150 (n=473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.3958` → IC=+0.170 (n=1419)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3958 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.8162` → IC=+0.168 (n=206)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.8162 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.699` → IC=+0.168 (n=643)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.699 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.866` → IC=+0.156 (n=813)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.866 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.165 (n=392)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.157 (n=453)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.5919` → IC=+0.159 (n=452)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5919 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=1564)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `8121.9037` → IC=+0.162 (n=643)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 8121.9037 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.160 (n=1199)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 156.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.159 (n=496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0037 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.336` → IC=+0.126 (n=1309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.336 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=1499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.4833` → IC=+0.156 (n=1309)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4833 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2117` → IC=+0.122 (n=1298)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2117 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.825` → IC=+0.133 (n=586)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.825 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2259` → IC=+0.122 (n=1309)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2259 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1668` → IC=+0.139 (n=380)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1668 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `2.2358` → IC=+0.133 (n=1249)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.2358 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.127 (n=593)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1013` → IC=+0.145 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1013 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.156 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 10.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.2979` → IC=+0.147 (n=315)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.2979 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.6865` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6865 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.31` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.31 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6895 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `9633.8027` → IC=+0.143 (n=315)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 9633.8027 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 150.0 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.209 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.147 (n=466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.3483` → IC=+0.206 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3483 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1841` → IC=+0.145 (n=466)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1841 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.137 (n=188)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.130 (n=466)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1917 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.143 (n=416)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.7044 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.207 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.4163` → IC=+0.151 (n=456)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4163 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.160 (n=148)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 159.0 (IC base=+0.125)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.254 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.214 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.221 (n=145)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.240 (n=294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.2663` → IC=+0.237 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2663 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3803` → IC=+0.222 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3803 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.085` → IC=+0.238 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.085 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.205 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.228 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2528` → IC=+0.312 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2528 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `1.374` → IC=+0.231 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.374 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.3885` → IC=+0.259 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3885 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `12390.1326` → IC=+0.221 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12390.1326 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.131 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0065 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.0998` → IC=+0.156 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0998 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.133 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 11.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.298` → IC=+0.161 (n=252)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.298 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.51` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.51 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6989` → IC=+0.149 (n=166)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6989 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `1.5407` → IC=+0.126 (n=319)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.5407 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3715` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3715
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=339)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.203 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.297` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 5.297 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `2944.1737` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2944.1737 (IC base=+0.073)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.124 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.4524` → IC=+0.168 (n=269)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.4524 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.024` → IC=+0.121 (n=93)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 5.024 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.7211` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.7211 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `2.4929` → IC=+0.132 (n=245)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.4929 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.134 (n=211)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 44.0 (IC base=+0.084)

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
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.192 (n=3395)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0085 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=7820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.212 (n=7483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8917` → IC=+0.199 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8917 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.221 (n=3676)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8833` → IC=+0.164 (n=3367)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8833 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.188 (n=1429)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.182 (n=2374)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.170 (n=8945)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.04 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3784.1723` → IC=+0.170 (n=2494)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3784.1723 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.193 (n=5372)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 94.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.197 (n=4594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0066 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.473` → IC=+0.184 (n=6891)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.473 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.557` → IC=+0.239 (n=6891)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.557 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2337` → IC=+0.164 (n=4322)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2337 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.856` → IC=+0.201 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.856 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.159 (n=2098)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7031 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.201` → IC=+0.162 (n=1587)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.201 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.252 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.3005` → IC=+0.191 (n=2792)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.3005 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.177 (n=5772)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 127.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.225 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.231 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=855)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.318 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.366` → IC=+0.291 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.366 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.242 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5578` → IC=+0.188 (n=514)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.5578 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.5831` → IC=+0.196 (n=390)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5831 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.262 (n=661)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.266 (n=885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.1993` → IC=+0.280 (n=660)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1993 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.3409` → IC=+0.286 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3409 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.611` → IC=+0.264 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.611 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.2258` → IC=+0.294 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2258 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `1.9032` → IC=+0.282 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9032 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1579.1972` → IC=+0.268 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1579.1972 (IC base=+0.255)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.188 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0027 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1817` → IC=+0.157 (n=790)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1817 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.6905` → IC=+0.245 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6905 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.3452` → IC=+0.202 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3452 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.805` → IC=+0.161 (n=278)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.805 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.367` → IC=+0.151 (n=1047)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.367 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6939` → IC=+0.181 (n=521)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6939 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.154` → IC=+0.181 (n=327)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.154 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4264` → IC=+0.157 (n=1131)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4264 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7608` → IC=+0.157 (n=754)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7608 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10682.1975` → IC=+0.169 (n=1058)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10682.1975 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `495.0` → IC=+0.163 (n=1062)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 495.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.178 (n=710)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0037 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.3218` → IC=+0.169 (n=1060)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3218 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.182 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 18.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.6377` → IC=+0.208 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6377 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.6991` → IC=+0.161 (n=169)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6991 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.1318` → IC=+0.169 (n=965)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1318 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.618` → IC=+0.190 (n=188)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.618 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.168 (n=1060)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1888 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.1498` → IC=+0.211 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1498 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.408` → IC=+0.171 (n=962)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.408 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `12094.187` → IC=+0.158 (n=706)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12094.187 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `376.0` → IC=+0.166 (n=578)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 376.0 (IC base=+0.158)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.223 (n=1180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=787)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.675` → IC=+0.250 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.675 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.471` → IC=+0.297 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.471 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.2162` → IC=+0.216 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2162 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.6743` → IC=+0.216 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6743 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=1338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.245 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.230)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.233 (n=518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.3701` → IC=+0.267 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3701 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.708` → IC=+0.278 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.708 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.298 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.791` → IC=+0.224 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.791 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.2419` → IC=+0.225 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2419 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `1894.26` → IC=+0.231 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.26 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.241 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.230)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.173 (n=560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0038 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4307` → IC=+0.137 (n=1270)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.4307 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.7054` → IC=+0.234 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7054 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.3511` → IC=+0.178 (n=486)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.3511 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.295` → IC=+0.165 (n=544)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.295 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8805` → IC=+0.158 (n=847)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8805 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.227 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.5044` → IC=+0.149 (n=537)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5044 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.7526` → IC=+0.153 (n=814)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7526 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8841.0428` → IC=+0.228 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8841.0428 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.157 (n=383)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 90.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.159 (n=900)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4318` → IC=+0.153 (n=1022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4318 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.3291` → IC=+0.227 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3291 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2039` → IC=+0.142 (n=947)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2039 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.113` → IC=+0.201 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.113 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.25` → IC=+0.136 (n=955)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.25 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8591` → IC=+0.142 (n=682)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8591 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1774` → IC=+0.153 (n=341)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1774 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.267 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5583` → IC=+0.146 (n=419)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5583 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.472` → IC=+0.172 (n=318)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.472 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7628.6335` → IC=+0.180 (n=464)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7628.6335 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.177 (n=1294)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.4667 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `1.0011` → IC=+0.188 (n=229)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 1.0011 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.428` → IC=+0.218 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.428 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.123 (n=902)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2911.4143` → IC=+0.244 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.4143 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.126 (n=953)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 53.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.177 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0061 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1221` → IC=+0.147 (n=415)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1221 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.153 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.209 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.625 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.4698` → IC=+0.131 (n=1219)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4698 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.437` → IC=+0.125 (n=1200)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.437 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.154 (n=548)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.72 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2178` → IC=+0.170 (n=189)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2178 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4615` → IC=+0.138 (n=363)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4615 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.5476` → IC=+0.127 (n=363)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.5476 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2921.4363` → IC=+0.167 (n=415)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2921.4363 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.215 (n=591)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.204 (n=1164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.311 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.1854` → IC=+0.234 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1854 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.552` → IC=+0.242 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.552 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.2434` → IC=+0.205 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2434 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.209 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2361` → IC=+0.232 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2361 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.5902` → IC=+0.237 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5902 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.211 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2562.8289` → IC=+0.209 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2562.8289 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.238 (n=479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.221 (n=479)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.200 (n=1519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.505` → IC=+0.255 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.505 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.8558` → IC=+0.204 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8558 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.01` → IC=+0.259 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.01 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.240 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.257 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2322` → IC=+0.192 (n=1106)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2322 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.197 (n=1257)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=2548)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.154 (n=2215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0094 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.5274` → IC=+0.155 (n=2517)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.5274 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.160 (n=877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.9375` → IC=+0.211 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9375 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1884` → IC=+0.155 (n=821)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1884 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.736` → IC=+0.165 (n=808)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.736 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.9056` → IC=+0.151 (n=1018)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.9056 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1738` → IC=+0.174 (n=688)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1738 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4626` → IC=+0.162 (n=831)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4626 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.9083` → IC=+0.157 (n=1661)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9083 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `8127.2771` → IC=+0.152 (n=1141)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8127.2771 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.188 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4837` → IC=+0.157 (n=1923)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4837 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.163 (n=647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 4.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.1769` → IC=+0.162 (n=846)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1769 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.142 (n=756)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.146 (n=1906)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1137` → IC=+0.148 (n=1605)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1137 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.153 (n=907)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.5724` → IC=+0.143 (n=1903)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5724 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.8251` → IC=+0.150 (n=1269)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8251 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=2548)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7743.0752` → IC=+0.151 (n=1718)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7743.0752 (IC base=+0.138)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.168 (n=275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0034 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0921` → IC=+0.186 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0921 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.5245` → IC=+0.197 (n=206)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5245 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.2354` → IC=+0.176 (n=140)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2354 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.25` → IC=+0.165 (n=392)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 8.25 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2448` → IC=+0.158 (n=308)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2448 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.8235` → IC=+0.191 (n=205)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.8235 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.7022` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.7022 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `12593.9941` → IC=+0.200 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12593.9941 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.203 (n=379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.166 (n=288)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.171 (n=314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1518` → IC=+0.164 (n=379)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1518 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.148 (n=390)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6071 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.6015` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6015 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.136 (n=886)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.212` → IC=+0.158 (n=840)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.212 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8865` → IC=+0.182 (n=574)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8865 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.163 (n=408)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.5736` → IC=+0.144 (n=857)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5736 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.149 (n=571)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `11340.2858` → IC=+0.151 (n=860)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11340.2858 (IC base=+0.135)

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
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.149 (n=742)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0088 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.147 (n=741)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0045 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.5046` → IC=+0.152 (n=742)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.5046 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.152 (n=271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 4.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.1834` → IC=+0.152 (n=743)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.1834 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.9629` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.9629 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.4248` → IC=+0.150 (n=704)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.4248 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.735` → IC=+0.151 (n=743)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.735 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.1122` → IC=+0.146 (n=653)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1122 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.2702` → IC=+0.155 (n=247)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2702 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.167 (n=220)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.167 (n=244)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=702)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `8268.5946` → IC=+0.150 (n=741)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8268.5946 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.164 (n=533)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0071 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.5101` → IC=+0.184 (n=605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.5101 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.158 (n=407)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 10.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.0956` → IC=+0.166 (n=605)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0956 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1548` → IC=+0.175 (n=275)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1548 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.3912` → IC=+0.152 (n=618)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3912 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.966` → IC=+0.176 (n=137)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 8.966 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.186 (n=202)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6473 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.7274` → IC=+0.156 (n=541)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7274 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1526` → IC=+0.155 (n=621)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.1526 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.177 (n=261)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1996` → IC=+0.167 (n=523)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.1996 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4499` → IC=+0.166 (n=594)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4499 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `8204.9591` → IC=+0.171 (n=605)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8204.9591 (IC base=+0.151)

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

- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.176 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0134 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.6223` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6223 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.121 (n=93)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 68.0 (IC base=+0.061)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.008` → IC=-0.255 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.008
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=280)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=291)

- **FILTRO** `dist_vwap_pct` > `0.1654` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1654
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=214)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.178 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0051 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.164 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.213 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1326` → IC=+0.166 (n=285)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1326 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.473` → IC=+0.183 (n=339)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.473 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.0919` → IC=+0.121 (n=547)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0919 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2901` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2901 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `2.5266` → IC=+0.149 (n=442)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.5266 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=442)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.157 (n=237)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.0688` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0688 (IC base=-0.016)

- **PATRÓN** `dist_vwap_pct` < `0.1654` → IC=+0.139 (n=214)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1654 (IC base=-0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.931` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.931 (IC base=-0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.0857` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0857 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.637` → IC=+0.173 (n=145)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.637 (IC base=-0.016)

- **PATRÓN** `volumen_spike_ratio` > `1.4611` → IC=+0.157 (n=129)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4611 (IC base=-0.016)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=152)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=-0.016)

- **PATRÓN** `libro_liquidez` > `2526.1581` → IC=+0.145 (n=74)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2526.1581 (IC base=-0.016)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.197 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0047 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.5781` → IC=+0.210 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5781 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.734` → IC=+0.136 (n=119)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.734 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `1.0552` → IC=+0.131 (n=166)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0552 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.149 (n=132)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.2692` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2692 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `2.0205` → IC=+0.181 (n=133)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.0205 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2835.039` → IC=+0.125 (n=174)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2835.039 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.0401` → IC=+0.231 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0401 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.4946` → IC=+0.230 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4946 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `0.9643` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.9643 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.0796` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0796 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `2.4111` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4111 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `3575.5947` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3575.5947 (IC base=+0.056)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.300 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=85)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=78)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.171 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0049 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.6407` → IC=+0.243 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6407 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.5279` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5279 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.057` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.057 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.789` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.789 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6219 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.7434` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.7434 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `1.3826` → IC=+0.143 (n=141)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.3826 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `1072.6991` → IC=+0.189 (n=165)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1072.6991 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.0933` → IC=+0.186 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0933 (IC base=-0.048)

- **PATRÓN** `ibs_20min` < `0.1926` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1926 (IC base=-0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.257` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.257 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.0655` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0655 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.7615` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7615 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.048)

- **PATRÓN** `libro_liquidez` > `1005.653` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1005.653 (IC base=-0.048)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` < `0.6744` → IC=-0.207 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6744
  - _Potencial_: sin este filtro IC_bueno=+0.198 (n=170)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.238 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=60)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.321 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.291 (n=41)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.167 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.075)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.132 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 14.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.198 (n=170)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.6744 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1831` → IC=+0.139 (n=95)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1831 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.655` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.655 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `0.9509` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.9509 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `2.5513` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.5513 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `599.301` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 599.301 (IC base=+0.075)

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

- **FILTRO** `volumen_pendiente_norm` > `0.176` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.176
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=61)

- **FILTRO** `sigma_h` > `0.0051` → IC=-0.337 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=92)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=120)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=110)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=39)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `drift_60min` |x|> `0.1067` → IC=-0.237 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

- **FILTRO** `volumen_regimen` < `0.892` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.892
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=38)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `volumen_regimen` > `0.9045` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9045
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=27)

- **FILTRO** `volumen_regimen` > `0.5996` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.5996
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

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
- **FILTRO** `dist_vwap_pct` > `0.6344` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6344
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=265)

- **PATRÓN** `ibs_20min` > `0.7368` → IC=+0.135 (n=187)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.7368 (IC base=+0.061)

- **PATRÓN** `ibs_20min` < `0.234` → IC=+0.132 (n=191)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.234 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.126` → IC=+0.139 (n=95)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.126 (IC base=+0.050)

- **PATRÓN** `libro_liquidez` > `3761.0521` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3761.0521 (IC base=+0.050)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

- **FILTRO** `ibs_20min` < `0.5084` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5084
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=68)

- **FILTRO** `volumen_regimen` < `0.8072` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8072
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=61)

- **PATRÓN** `drift_60min` |x|≤ `0.2127` → IC=+0.139 (n=81)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2127 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.230 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1524 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.682` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 10.682 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.1443` → IC=+0.122 (n=96)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.1443 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.1659` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1659 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.9499` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.9499 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3550.6412` → IC=+0.143 (n=96)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3550.6412 (IC base=+0.105)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=57)

- **FILTRO** `ibs_20min` < `0.7272` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7272
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=57)

- **FILTRO** `ibs_20min` > `0.3298` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3298
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

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.020)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2121` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2121
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=34)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.161 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0057 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3795` → IC=+0.155 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3795 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.7143` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.7143 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.7692 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.2073` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2073 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.204 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.4486` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4486 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `514.5372` → IC=+0.144 (n=85)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 514.5372 (IC base=+0.143)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.127 (n=440)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2814.617` → IC=+0.171 (n=156)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2814.617 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2300.2562` → IC=+0.122 (n=525)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2300.2562 (IC base=+0.095)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.127 (n=440)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2814.617` → IC=+0.171 (n=156)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2814.617 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2300.2562` → IC=+0.122 (n=525)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2300.2562 (IC base=+0.095)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=77)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=122)

- **FILTRO** `libro_liquidez` < `2404.4298` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 2404.4298
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=104)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=189)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=175)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `libro_liquidez` < `14445.5423` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 14445.5423
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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1303)

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
- **FILTRO** `liq_usd_total` < `32944.1` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `liq_usd_total` < 32944.1
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=88)

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

- **PATRÓN** `liq_usd_total` > `55522.43` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `liq_usd_total` > 55522.43 (IC base=+0.011)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=548)

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
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=433)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=247)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=247)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9969` → IC=-0.142 (n=65)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9969
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=197)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=157)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=157)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=94)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=74)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=155)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=54)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=40)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=85)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.125 (n=997)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=5379)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6111)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=1025)

- **FILTRO** `libro_liquidez` < `15888.9153` → IC=-0.153 (n=260)

  - _Acción_: SKIP cuando `libro_liquidez` < 15888.9153
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=780)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1302)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.177 (n=2551)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=7808)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.171 (n=2661)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=8140)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.217 (n=418)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=1320)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.195 (n=441)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=1350)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.216 (n=453)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=1441)

- **FILTRO** `ibs_20min` > `0.2865` → IC=-0.170 (n=473)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2865
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=1421)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.200 (n=414)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=1297)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.194 (n=465)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1437)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2360)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2348)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=2354)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=268)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.7128` → IC=-0.203 (n=116)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7128
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=116)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=151)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=607)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=7497)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=16910)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.280 (n=5632)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=18775)

- **FILTRO** `ibs_7min` < `0.7069` → IC=-0.236 (n=6100)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7069
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=18307)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.160 (n=8108)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=16299)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.223 (n=7613)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=22959)

- **FILTRO** `ibs_7min` > `0.2973` → IC=-0.177 (n=7640)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2973
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=22932)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=918)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=2972)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.256 (n=1283)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2607)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.192 (n=946)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=2944)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=3582)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1744)

- **FILTRO** `ibs_7min` > `0.7979` → IC=-0.205 (n=1331)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7979
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=3995)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.139 (n=988)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=3288)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.253 (n=987)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3289)

- **FILTRO** `ibs_7min` < `0.76` → IC=-0.186 (n=1068)

  - _Acción_: SKIP cuando `ibs_7min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3208)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.170 (n=1064)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3212)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.256 (n=1010)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=3319)

- **FILTRO** `ibs_7min` > `0.2506` → IC=-0.167 (n=1082)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2506
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3247)

- **FILTRO** `ballena_activa_n` > `114.0` → IC=-0.164 (n=1455)

  - _Acción_: SKIP cuando `ballena_activa_n` > 114.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2874)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.181 (n=898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=2763)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.319 (n=872)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2789)

- **FILTRO** `drift_7min_pct` |x|> `0.181` → IC=-0.129 (n=1244)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.181
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=2417)

- **FILTRO** `ibs_7min` < `0.2034` → IC=-0.272 (n=915)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2034
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2746)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.217 (n=888)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=2773)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.235 (n=1311)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=4278)

- **FILTRO** `ibs_7min` > `0.2649` → IC=-0.157 (n=1900)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2649
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=3689)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=1277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=2738)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=965)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3050)

- **FILTRO** `ibs_7min` < `0.7455` → IC=-0.190 (n=1003)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7455
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3012)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.184 (n=982)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3033)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1005)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3106)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.175 (n=1027)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3084)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.181 (n=1020)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3091)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.239 (n=1090)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3344)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.208 (n=1106)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3328)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.176 (n=1398)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4383)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=1246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=2885)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.278 (n=986)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3145)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.227 (n=1028)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=3103)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.203 (n=1014)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3117)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.205 (n=1302)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=4134)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=948)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=479)

- **FILTRO** `libro_liquidez` < `10498.4421` → IC=-0.159 (n=130)

  - _Acción_: SKIP cuando `libro_liquidez` < 10498.4421
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=392)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.157 (n=97)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=312)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=525)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.133 (n=617)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.134 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.120)

- **PATRÓN** `total_vol_5m` < `474.7871` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 474.7871 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.131 (n=258)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 27.0 (IC base=+0.120)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.133 (n=47)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.133)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.182 (n=83)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.095)

- **PATRÓN** `total_vol_5m` < `672.2721` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 672.2721 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `7829.679` → IC=+0.123 (n=112)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 7829.679 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 81.0 (IC base=+0.095)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.190 (n=111)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.211 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.153)

- **PATRÓN** `total_vol_5m` < `5917.212` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 5917.212 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3171.8207` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3171.8207 (IC base=+0.153)

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
- **FILTRO** `sigma_h` > `0.0044` → IC=-0.293 (n=182)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=91)

- **FILTRO** `T_h` > `52.6662` → IC=-0.250 (n=182)

  - _Acción_: SKIP cuando `T_h` > 52.6662
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=91)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.162 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=-0.154)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.328 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=29)

- **FILTRO** `T_h` > `57.4676` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `T_h` > 57.4676
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0053 (IC base=-0.155)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.222 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `T_h` < `87.9936` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.232 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=212)

- **FILTRO** `T_h` < `87.9773` → IC=-0.181 (n=92)

  - _Acción_: SKIP cuando `T_h` < 87.9773
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=189)

- **FILTRO** `T_h` > `87.9558` → IC=-0.309 (n=171)

  - _Acción_: SKIP cuando `T_h` > 87.9558
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `pct_vs_K` |x|> `4.4208` → IC=-0.449 (n=57)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4208
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=172)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0036` → IC=-0.278 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=78)

- **FILTRO** `T_h` > `63.9952` → IC=-0.196 (n=77)

  - _Acción_: SKIP cuando `T_h` > 63.9952
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=26)

- **FILTRO** `T_h` > `144.6177` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `T_h` > 144.6177
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=61)

- **FILTRO** `pct_vs_K` |x|> `2.3742` → IC=-0.427 (n=39)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3742
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=41)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.986` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=57)

- **FILTRO** `T_h` < `87.9808` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `T_h` < 87.9808
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=52)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.385 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **FILTRO** `T_h` > `71.0631` → IC=-0.333 (n=58)

  - _Acción_: SKIP cuando `T_h` > 71.0631
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0068` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=41)

- **FILTRO** `T_h` > `135.9709` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `T_h` > 135.9709
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

- **FILTRO** `sigma_h` > `0.0064` → IC=-0.371 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

- **FILTRO** `T_h` > `87.2992` → IC=-0.403 (n=29)

  - _Acción_: SKIP cuando `T_h` > 87.2992
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2005` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.462 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.364)

- **PATRÓN** `T_h` > `0.8157` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8157 (IC base=+0.364)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.458 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.364)

- **PATRÓN** `edge` > `0.1035` → IC=+0.448 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1035 (IC base=+0.405)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.462 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.405)

- **PATRÓN** `T_h` > `0.8587` → IC=+0.427 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8587 (IC base=+0.405)

- **PATRÓN** `dist_50` > `0.3792` → IC=+0.474 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3792 (IC base=+0.405)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.414 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.405)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.434 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.405)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.472)

- **PATRÓN** `edge` > `0.1135` → IC=+0.481 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1135 (IC base=+0.476)

- **PATRÓN** `sigma_h` < `0.0144` → IC=+0.482 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0144 (IC base=+0.476)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.462 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.476)

- **PATRÓN** `T_h` < `1.3487` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.3487 (IC base=+0.476)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.463 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.476)

- **PATRÓN** `dist_50` > `0.4568` → IC=+0.481 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4568 (IC base=+0.476)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.461 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.476)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.468 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.476)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=121)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=217)

- **FILTRO** `streak_estiramiento` > `0.8581` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8581
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=133)

- **PATRÓN** `streak_estiramiento` < `0.4429` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.4429 (IC base=+0.022)

- **PATRÓN** `streak_estiramiento` < `0.5577` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.5577 (IC base=+0.033)

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
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=498)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=504)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=300)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=446)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=902)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=520)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=555)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2286)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1177)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1185)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.189 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0039 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.191 (n=348)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.009 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.169 (n=460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.168)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0585` → IC=+0.173 (n=1044)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.0585 (IC base=+0.168)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3418` → IC=+0.205 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3418 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.168)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.239 (n=1044)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1497` → IC=+0.165 (n=518)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1497 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.547` → IC=+0.167 (n=1096)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.547 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.861` → IC=+0.246 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.861 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `5059.1554` → IC=+0.182 (n=473)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 5059.1554 (IC base=+0.168)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=324)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.217 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.197 (n=262)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0023 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0624` → IC=+0.244 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0624 (IC base=+0.195)

- **PATRÓN** `drift_15min` |x|≤ `0.3761` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3761 (IC base=+0.195)

- **PATRÓN** `delta_ratio_macro` |x|> `0.25` → IC=+0.211 (n=88)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.25 (IC base=+0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3853` → IC=+0.232 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3853 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.212 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_15` > `0.7746` → IC=+0.263 (n=234)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7746 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.205 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.491` → IC=+0.252 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.491 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `13812.6413` → IC=+0.235 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13812.6413 (IC base=+0.195)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `20.029` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 20.029 (IC base=-0.005)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.147 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0061 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.140 (n=84)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.129)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1416` → IC=+0.161 (n=166)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1416 (IC base=+0.129)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2698` → IC=+0.163 (n=158)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2698 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.134 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.146 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.221 (n=249)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1439` → IC=+0.151 (n=193)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1439 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.912` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.912 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `10110.2635` → IC=+0.135 (n=113)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 10110.2635 (IC base=+0.129)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=46)

- **FILTRO** `ibs_15` > `0.2175` → IC=-0.250 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2175
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.587` → IC=-0.180 (n=48)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.587
  - _Potencial_: sin este filtro IC_bueno=+0.236 (n=146)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.142 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.005 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.176 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0076 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1419` → IC=+0.172 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1419 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0657` → IC=+0.167 (n=130)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio_macro` |x|> 0.0657 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.189 (n=88)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.170 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.587` → IC=+0.236 (n=146)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.587 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.5591` → IC=+0.144 (n=172)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.5591 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3002.1997` → IC=+0.235 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3002.1997 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 35.0 (IC base=+0.133)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5826` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5826
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=572)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.524` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.524 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0142` → IC=+0.241 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0142 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.194 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0668` → IC=+0.188 (n=267)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0668 (IC base=+0.175)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.225 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.175)

- **PATRÓN** `ibs_15` > `0.5354` → IC=+0.271 (n=299)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5354 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1729` → IC=+0.199 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1729 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.796` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.796 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.409` → IC=+0.175 (n=266)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 7.409 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2713.7902` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2713.7902 (IC base=+0.175)

- **PATRÓN** `ibs_15` < `0.1053` → IC=+0.180 (n=329)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` < 0.1053 (IC base=+0.049)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.332 (n=200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.372 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.338 (n=263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.341 (n=199)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2966` → IC=+0.370 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2966 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.353 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.389 (n=267)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.374 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.994` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.994 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.341 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3397.72` → IC=+0.347 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3397.72 (IC base=+0.333)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1204` → IC=+0.342 (n=74)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1204 (IC base=+0.336)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.333 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.362 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1544` → IC=+0.340 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1544 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1021` → IC=+0.342 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1021 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.404 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.353 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.336)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.336 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.371 (n=168)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.345 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `9041.1491` → IC=+0.360 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9041.1491 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `555.0` → IC=+0.397 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 555.0 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.333 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.325)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.336 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.325)

- **PATRÓN** `drift_60min` |x|≤ `0.1549` → IC=+0.331 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1549 (IC base=+0.325)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0918` → IC=+0.325 (n=118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0918 (IC base=+0.325)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.325)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.347 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.325)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.388 (n=132)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.325)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.337 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.325)

- **PATRÓN** `dist_vwap_pct` < `0.0995` → IC=+0.335 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0995 (IC base=+0.325)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.370 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.325)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.344 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.325)

- **PATRÓN** `libro_liquidez` > `3558.8831` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3558.8831 (IC base=+0.325)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.327 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.325)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.202 (n=524)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1573)

- **FILTRO** `ibs_15` < `0.6026` → IC=-0.182 (n=174)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6026
  - _Potencial_: sin este filtro IC_bueno=+0.247 (n=524)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.207 (n=247)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1850)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.219 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=-0.058)

- **PATRÓN** `ibs_15` > `0.6026` → IC=+0.247 (n=524)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6026 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` < `0.2663` → IC=+0.169 (n=406)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.2663 (IC base=-0.058)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1199` → IC=+0.238 (n=720)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1199 (IC base=-0.047)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1825` → IC=+0.237 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1825 (IC base=-0.047)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.278 (n=1080)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` > `0.4044` → IC=+0.261 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4044 (IC base=-0.047)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.208 (n=310)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=934)

- **FILTRO** `sigma_h` < `0.0032` → IC=-0.235 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=933)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.212 (n=790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=454)

- **FILTRO** `sigma_ewma_delta_pct` > `19.843` → IC=-0.244 (n=225)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.843
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1019)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.153 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.003 (IC base=+0.073)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.259 (n=52)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.073)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.073)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.346 (n=102)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.354` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.354 (IC base=+0.073)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6489` → IC=-0.233 (n=84)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6489
  - _Potencial_: sin este filtro IC_bueno=+0.243 (n=255)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.139 (n=322)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.148 (n=228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0039 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.210 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.125)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.125)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.126 (n=228)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.63€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.125)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.222 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.170 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 16.0 (IC base=+0.125)

- **PATRÓN** `ibs_15` > `0.6489` → IC=+0.243 (n=255)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6489 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.167 (n=181)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.882` → IC=+0.129 (n=200)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 6.882 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=322)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.246 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.4235` → IC=+0.229 (n=451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4235 (IC base=+0.223)

- **PATRÓN** `drift_15min` |x|≤ `0.7631` → IC=+0.224 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7631 (IC base=+0.223)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2065` → IC=+0.254 (n=205)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2065 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.252 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.234 (n=306)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.270 (n=451)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.7494` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7494 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.178` → IC=+0.244 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.178 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.02` → IC=+0.224 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.02 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3628.461` → IC=+0.224 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3628.461 (IC base=+0.223)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0501` → IC=-0.149 (n=383)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0501
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=129)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.180 (n=383)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=129)

- **FILTRO** `drift_60min` |x|> `0.1644` → IC=-0.210 (n=174)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1644
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=338)

- **FILTRO** `drift_15min` |x|> `0.8398` → IC=-0.229 (n=127)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8398
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=385)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0717` → IC=+0.204 (n=201)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0717 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.241 (n=226)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.1618` → IC=+0.200 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1618 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0189` → IC=-0.250 (n=314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0189
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=316)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=456)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1053` → IC=+0.356 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1053 (IC base=-0.047)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.300 (n=318)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` > `1.0781` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0781 (IC base=-0.047)

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
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.296 (n=341)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.302 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1417` → IC=+0.292 (n=340)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1417 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.306 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.324 (n=510)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.322 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.312 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `12407.0839` → IC=+0.303 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12407.0839 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.297 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.277 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0025 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0602` → IC=+0.304 (n=95)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0602 (IC base=+0.277)

- **PATRÓN** `drift_15min` |x|≤ `0.3845` → IC=+0.283 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3845 (IC base=+0.277)

- **PATRÓN** `delta_ratio_macro` |x|> `0.246` → IC=+0.304 (n=95)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.246 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3724` → IC=+0.299 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3724 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.331 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8593` → IC=+0.305 (n=254)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8593 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.976` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.976 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `11990.51` → IC=+0.302 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11990.51 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.301 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.289 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0692` → IC=+0.314 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0692 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1901` → IC=+0.309 (n=103)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1901 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.331 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.316 (n=215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.333 (n=226)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.306 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2752 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` < `0.4391` → IC=+0.291 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4391 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.72` → IC=+0.312 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.72 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.299 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.293 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0852` → IC=-0.269 (n=63)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0852
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=193)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.253 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=169)

- **FILTRO** `drift_60min` |x|> `0.2669` → IC=-0.192 (n=63)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2669
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=193)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1206` → IC=-0.151 (n=107)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1206
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=322)

- **FILTRO** `drift_15min` |x|> `0.5254` → IC=-0.133 (n=107)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5254
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=322)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1792` → IC=-0.135 (n=72)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1792
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
- **PATRÓN** `T_h` > `87.9712` → IC=+0.147 (n=185)

  - _Acción_: Kelly boost +0.74€ cuando `T_h` > 87.9712 (IC base=+0.135)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.328 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.135)

- **PATRÓN** `T_h` > `145.8502` → IC=+0.409 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8502 (IC base=+0.347)

- **PATRÓN** `ratio` > `1.0088` → IC=+0.359 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0088 (IC base=+0.347)

### WEEKLY_PRICE#BTC
- **FILTRO** `ratio` > `0.9932` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `ratio` > 0.9932
  - _Potencial_: sin este filtro IC_bueno=+0.286 (n=68)

- **PATRÓN** `T_h` > `144.5528` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `T_h` > 144.5528 (IC base=+0.095)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.095)

- **PATRÓN** `T_h` > `87.9936` → IC=+0.303 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9936 (IC base=+0.300)

- **PATRÓN** `ratio` > `1.0368` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0368 (IC base=+0.300)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `63.9918` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 63.9918 (IC base=+0.195)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.415 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.195)

- **PATRÓN** `T_h` > `87.9957` → IC=+0.344 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.326)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.362 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.326)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.406)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.168 a +0.239 en UPDOWN_GBM#15min (n=1044). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7746 sube el IC de +0.195 a +0.263 en UPDOWN_GBM#BTC#15min (n=234). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.129 a +0.221 en UPDOWN_GBM#ETH#15min (n=249). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.587 sube el IC de +0.133 a +0.236 en UPDOWN_GBM#SOL#15min (n=146). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5354 sube el IC de +0.175 a +0.271 en UPDOWN_GBM#XRP#15min (n=299). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1053 sube el IC de +0.049 a +0.180 en UPDOWN_GBM#XRP#15min (n=329). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6026 sube el IC de -0.058 a +0.247 en UPDOWN_GBM_15M_TARDIO (n=524). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.047 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1080). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.073 a +0.346 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=102). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6489 sube el IC de +0.125 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3605 sube el IC de +0.223 a +0.270 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=451). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.146 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.044 a +0.241 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=226). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.047 a +0.300 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=318). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.283 a +0.324 en UPDOWN_GBM_IBS_ALTO (n=510). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8593 sube el IC de +0.277 a +0.305 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=254). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.289 a +0.333 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=226). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.333 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=267). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.336 a +0.371 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=168). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.325 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=132). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1142 | +0.083 | +135.01€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1142 | +0.083 | +135.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 825 | +0.089 | +108.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 825 | +0.089 | +108.94€ | 3 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 238 | +0.046 | +5.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 238 | +0.046 | +5.27€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 53 | +0.173 | +22.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 53 | +0.173 | +22.29€ | 0 | 5 |
| ✅ BALLENAS_TARDIAS | 20094 | -0.105 | -2905.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1211 | -0.042 | -212.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 18883 | -0.109 | -2693.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3140 | -0.122 | -556.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3140 | -0.122 | -556.81€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1211 | -0.042 | -212.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1211 | -0.042 | -212.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5811 | -0.053 | -588.85€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5811 | -0.053 | -588.85€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5305 | -0.115 | -410.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5305 | -0.115 | -410.93€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4253 | -0.166 | -976.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4253 | -0.166 | -976.08€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 11685 | -0.043 | +4261.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3152 | -0.008 | +1840.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 8533 | -0.057 | +2420.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 11685 | -0.043 | +4261.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3152 | -0.008 | +1840.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 8533 | -0.057 | +2420.77€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 843 | -0.102 | -123.46€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 47 | -0.092 | -9.84€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 796 | -0.103 | -113.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 486 | -0.074 | -61.69€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 33 | -0.100 | -7.05€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 453 | -0.071 | -54.64€ | 1 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 231 | -0.165 | -53.02€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 14 | -0.044 | -2.79€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 217 | -0.171 | -50.23€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 65 | -0.052 | -8.60€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 65 | -0.052 | -8.60€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 72807 | +0.113 | -3850.74€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 11444 | +0.182 | -358.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 280 | -0.117 | -46.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 56013 | +0.100 | -3336.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5070 | +0.115 | -109.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 9334 | +0.095 | -897.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 37 | -0.141 | -0.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 9282 | +0.097 | -885.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 14718 | +0.130 | -323.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3484 | +0.202 | -111.54€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 9281 | +0.108 | -205.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1911 | +0.116 | +16.63€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 9376 | +0.088 | -932.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 44 | -0.065 | -4.30€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 9317 | +0.090 | -917.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 15601 | +0.124 | -310.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4408 | +0.171 | -79.31€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 9359 | +0.108 | -171.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1822 | +0.099 | -51.23€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 14427 | +0.116 | -816.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3434 | +0.186 | -173.20€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 183 | -0.073 | +7.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 9473 | +0.092 | -576.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1337 | +0.137 | -74.61€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 9351 | +0.102 | -570.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 37 | -0.013 | +9.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 9301 | +0.103 | -579.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 11514 | +0.188 | -804.04€ | 3 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 11514 | +0.188 | -804.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2838 | +0.167 | -309.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2838 | +0.167 | -309.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 576 | +0.182 | +9.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 576 | +0.182 | +9.95€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2786 | +0.176 | -264.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2786 | +0.176 | -264.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2504 | +0.236 | -76.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2504 | +0.236 | -76.19€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2731 | +0.190 | -177.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2731 | +0.190 | -177.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 536 | +0.433 | -10.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 536 | +0.433 | -10.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 205 | +0.437 | -1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 205 | +0.437 | -1.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 203 | +0.442 | +0.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 203 | +0.442 | +0.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 121 | +0.402 | -8.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 121 | +0.402 | -8.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 39308 | +0.194 | -3334.04€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 39308 | +0.194 | -3334.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6852 | +0.168 | -883.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6852 | +0.168 | -883.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6226 | +0.222 | -244.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6226 | +0.222 | -244.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6811 | +0.168 | -875.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6811 | +0.168 | -875.10€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6319 | +0.218 | -263.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6319 | +0.218 | -263.90€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6489 | +0.202 | -447.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6489 | +0.202 | -447.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6611 | +0.190 | -619.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6611 | +0.190 | -619.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 14637 | +0.124 | +281.23€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 14637 | +0.124 | +281.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7259 | +0.130 | +203.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7259 | +0.130 | +203.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7378 | +0.119 | +77.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7378 | +0.119 | +77.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1224 | +0.287 | -25.82€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1224 | +0.287 | -25.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 541 | +0.274 | -18.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 541 | +0.274 | -18.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 584 | +0.290 | -5.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 584 | +0.290 | -5.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 99 | +0.332 | -1.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 99 | +0.332 | -1.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 541 | +0.430 | -8.57€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 541 | +0.430 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 252 | +0.429 | -4.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 252 | +0.429 | -4.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 250 | +0.432 | -3.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 250 | +0.432 | -3.70€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 39 | +0.378 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 39 | +0.378 | -0.28€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 829 | +0.068 | -44.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 294 | +0.061 | -23.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 535 | +0.072 | -20.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 52 | +0.130 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 52 | +0.130 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 646 | +0.076 | -21.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 111 | +0.093 | -0.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 535 | +0.072 | -20.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 131 | +0.004 | -26.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 131 | +0.004 | -26.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 25734 | +0.098 | -798.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2171 | +0.095 | +33.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 23563 | +0.098 | -832.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 14714 | +0.102 | -237.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2171 | +0.095 | +33.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 12543 | +0.103 | -271.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4430 | +0.114 | +30.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4430 | +0.114 | +30.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6590 | +0.079 | -591.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6590 | +0.079 | -591.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 715 | +0.255 | -95.42€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 715 | +0.255 | -95.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 715 | +0.255 | -95.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 715 | +0.255 | -95.42€ | 0 | 4 |
| ✅ GBM_LATE_15M | 19123 | +0.074 | +8573.95€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 19123 | +0.074 | +8573.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3129 | +0.195 | +2294.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3129 | +0.195 | +2294.23€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 2804 | +0.176 | +1892.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2804 | +0.176 | +1892.11€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 3266 | +0.193 | +2363.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3266 | +0.193 | +2363.64€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 2869 | +0.003 | +431.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2869 | +0.003 | +431.93€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 2827 | -0.038 | +621.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2827 | -0.038 | +621.00€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 4228 | -0.051 | +971.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4228 | -0.051 | +971.05€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 20193 | +0.076 | +10007.90€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 20193 | +0.076 | +10007.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3707 | +0.012 | +1942.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3707 | +0.012 | +1942.42€ | 1 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4263 | +0.004 | +790.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4263 | +0.004 | +790.19€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2854 | +0.255 | +2787.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2854 | +0.255 | +2787.15€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3147 | -0.019 | +354.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3147 | -0.019 | +354.44€ | 2 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3363 | +0.013 | +1178.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3363 | +0.013 | +1178.27€ | 3 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2859 | +0.267 | +2955.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2859 | +0.267 | +2955.43€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 15559 | +0.169 | +11375.10€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 15559 | +0.169 | +11375.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2291 | +0.209 | +1837.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2291 | +0.209 | +1837.67€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2447 | +0.157 | +1761.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2447 | +0.157 | +1761.03€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2401 | +0.203 | +1864.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2401 | +0.203 | +1864.47€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2587 | +0.140 | +1733.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2587 | +0.140 | +1733.40€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2938 | +0.112 | +1904.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2938 | +0.112 | +1904.98€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2895 | +0.202 | +2273.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2895 | +0.202 | +2273.54€ | 0 | 30 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3873 | +0.125 | +1549.94€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3873 | +0.125 | +1549.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 136 | +0.109 | +50.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 136 | +0.109 | +50.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1040 | +0.117 | +402.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1040 | +0.117 | +402.20€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1081 | +0.154 | +506.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1081 | +0.154 | +506.67€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 745 | +0.078 | +188.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 745 | +0.078 | +188.89€ | 1 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 19163 | +0.172 | +13783.66€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 19163 | +0.172 | +13783.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 2991 | +0.221 | +2518.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 2991 | +0.221 | +2518.56€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2990 | +0.152 | +1954.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2990 | +0.152 | +1954.24€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3095 | +0.220 | +2592.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3095 | +0.220 | +2592.44€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3055 | +0.135 | +1967.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3055 | +0.135 | +1967.67€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3381 | +0.106 | +1919.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3381 | +0.106 | +1919.56€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3651 | +0.202 | +2831.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3651 | +0.202 | +2831.18€ | 0 | 24 |
| ✅ GBM_LATE_5M | 5918 | +0.142 | +3230.58€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5918 | +0.142 | +3230.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1556 | +0.140 | +955.20€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1556 | +0.140 | +955.20€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1794 | +0.146 | +981.74€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1794 | +0.146 | +981.74€ | 0 | 30 |
| ✅ GBM_LATE_5M#SOL | 312 | +0.041 | +47.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 312 | +0.041 | +47.97€ | 2 | 6 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1222 | +0.065 | +467.07€ | 3 | 18 |
| ✅ GBM_LATE_60M#60min | 1222 | +0.065 | +467.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 431 | +0.089 | +162.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 431 | +0.089 | +162.56€ | 0 | 16 |
| ✅ GBM_LATE_60M#ETH | 406 | +0.071 | +192.42€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 406 | +0.071 | +192.42€ | 2 | 19 |
| ✅ GBM_LATE_60M#SOL | 385 | +0.030 | +112.09€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 385 | +0.030 | +112.09€ | 3 | 11 |
| 🚫 GBM_LATE_60M_FADE | 291 | -0.271 | -27.91€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 291 | -0.271 | -27.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 108 | -0.227 | -8.73€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 108 | -0.227 | -8.73€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 99 | -0.302 | -15.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 99 | -0.302 | -15.38€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 84 | -0.279 | -3.80€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 84 | -0.279 | -3.80€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 567 | +0.055 | +100.95€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 567 | +0.055 | +100.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 217 | +0.043 | +29.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 217 | +0.043 | +29.84€ | 3 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 171 | +0.038 | +0.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 171 | +0.038 | +0.90€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 179 | +0.086 | +70.21€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 179 | +0.086 | +70.21€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 56 | +0.241 | +31.18€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 56 | +0.241 | +31.18€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 56 | +0.241 | +31.18€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 56 | +0.241 | +31.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1323 | +0.103 | +370.11€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1323 | +0.103 | +370.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1323 | +0.103 | +370.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1323 | +0.103 | +370.11€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M | 348 | -0.083 | -33.50€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 348 | -0.083 | -33.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 84 | -0.081 | -6.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 84 | -0.081 | -6.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 117 | -0.013 | -2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 117 | -0.013 | -2.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1501 | -0.004 | -11.02€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1501 | -0.004 | -11.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 165 | -0.027 | -1.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 165 | -0.027 | -1.96€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 595 | +0.026 | +17.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 595 | +0.026 | +17.43€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 459 | -0.008 | -8.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 459 | -0.008 | -8.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 105 | -0.061 | -6.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 105 | -0.061 | -6.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 883 | -0.047 | -26.45€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 883 | -0.047 | -26.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 261 | -0.055 | -15.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 261 | -0.055 | -15.26€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 278 | -0.036 | -4.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 278 | -0.036 | -4.33€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 344 | -0.049 | -6.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 344 | -0.049 | -6.86€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 12728 | -0.011 | -180.88€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 12728 | -0.011 | -180.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2291 | -0.022 | -50.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2291 | -0.022 | -50.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2587 | -0.016 | -21.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2587 | -0.016 | -21.25€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3032 | -0.018 | -58.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3032 | -0.018 | -58.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 21160 | -0.012 | +958.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 21160 | -0.012 | +958.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3662 | +0.009 | +489.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3662 | +0.009 | +489.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3440 | -0.025 | -30.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3440 | -0.025 | -30.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3685 | +0.002 | +305.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3685 | +0.002 | +305.74€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3222 | -0.042 | -62.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3222 | -0.042 | -62.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3538 | -0.016 | +142.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3538 | -0.016 | +142.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3613 | -0.004 | +113.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3613 | -0.004 | +113.59€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4809 | -0.035 | -110.97€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4809 | -0.035 | -110.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 979 | -0.038 | -26.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 979 | -0.038 | -26.04€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 433 | -0.116 | -15.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 433 | -0.116 | -15.85€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1308 | -0.047 | -22.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1308 | -0.047 | -22.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3219 | +0.003 | -8.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3219 | +0.003 | -8.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1196 | +0.004 | +3.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1196 | +0.004 | +3.63€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1387 | +0.007 | -0.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1387 | +0.007 | -0.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 54979 | -0.073 | +1163.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 54979 | -0.073 | +1163.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 9216 | -0.081 | +576.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 9216 | -0.081 | +576.72€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 8605 | -0.086 | -275.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 8605 | -0.086 | -275.37€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 9250 | -0.072 | +430.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 9250 | -0.072 | +430.18€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8126 | -0.093 | -222.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8126 | -0.093 | -222.39€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 10215 | -0.047 | +313.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 10215 | -0.047 | +313.07€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 9567 | -0.065 | +341.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 9567 | -0.065 | +341.06€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6685 | -0.021 | -107.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6685 | -0.021 | -107.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1485 | -0.021 | -10.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1485 | -0.021 | -10.84€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1477 | -0.014 | -7.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1477 | -0.014 | -7.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 988 | -0.035 | -13.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 988 | -0.035 | -13.67€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 958 | +0.112 | +329.25€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 822 | +0.120 | +316.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 186 | +0.133 | +88.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 186 | +0.133 | +88.49€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 162 | +0.098 | +39.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 162 | +0.098 | +39.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 166 | +0.095 | +53.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 166 | +0.095 | +53.30€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 148 | +0.153 | +79.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 148 | +0.153 | +79.63€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 160 | +0.117 | +55.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 160 | +0.117 | +55.60€ | 0 | 3 |
| ✅ PRICE_TARGET_GBM | 451 | -0.094 | -15.12€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 200 | -0.134 | -34.68€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 158 | -0.175 | -37.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 161 | -0.083 | +3.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 119 | -0.095 | -3.55€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 90 | -0.022 | +16.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 70 | -0.042 | +10.45€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 347 | -0.122 | -30.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 510 | -0.221 | -40.74€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 215 | -0.205 | -33.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 183 | -0.197 | -30.77€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 180 | -0.242 | -21.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 153 | -0.255 | -25.30€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 115 | -0.209 | +13.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 101 | -0.209 | +10.46€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 437 | -0.222 | -45.60€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 181 | +0.396 | +130.33€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 43 | +0.344 | +36.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 43 | +0.344 | +36.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 115 | +0.483 | +95.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 115 | +0.483 | +95.85€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#sniper | 181 | +0.396 | +130.33€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 376 | +0.029 | +9.67€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 376 | +0.029 | +9.67€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 166 | +0.030 | +1.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 166 | +0.030 | +1.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 41 | -0.035 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 41 | -0.035 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 144 | +0.034 | +9.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 144 | +0.034 | +9.50€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 2375 | -0.023 | -102.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2375 | -0.023 | -102.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 562 | -0.023 | -23.39€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 562 | -0.023 | -23.39€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 151 | -0.043 | -13.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 151 | -0.043 | -13.92€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 858 | -0.024 | -37.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 858 | -0.024 | -37.99€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 57 | -0.042 | -3.50€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 57 | -0.042 | -3.50€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 22 | +0.042 | +0.45€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 22 | +0.042 | +0.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6242 | +0.022 | +88.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6242 | +0.022 | +88.62€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2001 | +0.021 | +20.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2001 | +0.021 | +20.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1298 | +0.030 | +33.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1298 | +0.030 | +33.76€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1826 | +0.014 | +5.54€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1826 | +0.014 | +5.54€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1117 | +0.028 | +29.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1117 | +0.028 | +29.26€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5832 | +0.012 | -31.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5832 | +0.012 | -31.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2305 | +0.020 | +1.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2305 | +0.020 | +1.84€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2318 | +0.015 | -7.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2318 | +0.015 | -7.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1209 | -0.006 | -25.92€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1209 | -0.006 | -25.92€ | 2 | 0 |
| ✅ UPDOWN_GBM | 24401 | +0.029 | +1338.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 6523 | +0.057 | +1029.67€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 916 | +0.004 | +8.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 15427 | +0.023 | +306.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1437 | -0.004 | -10.22€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2129 | +0.072 | +207.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 272 | +0.124 | +85.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1838 | +0.065 | +122.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4353 | +0.030 | +282.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 774 | +0.084 | +182.93€ | 0 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 261 | +0.025 | +7.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2643 | +0.024 | +88.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 638 | +0.000 | +2.52€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 37 | -0.115 | +1.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2913 | +0.033 | +96.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 229 | +0.106 | +55.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2668 | +0.027 | +42.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 4896 | +0.016 | +196.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1789 | +0.042 | +187.38€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 248 | +0.008 | +8.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2310 | +0.004 | +3.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 517 | -0.009 | -7.26€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 32 | -0.147 | +4.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6399 | +0.016 | +147.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1756 | +0.022 | +100.25€ | 1 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 242 | -0.008 | -2.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4092 | +0.018 | +55.40€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 282 | -0.007 | -5.48€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 27 | -0.155 | -0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3709 | +0.040 | +410.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1703 | +0.079 | +418.60€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 130 | -0.015 | -3.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1876 | +0.008 | -4.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 96 | -0.143 | +5.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 398 | +0.333 | +106.30€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 398 | +0.333 | +106.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 223 | +0.336 | +55.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 223 | +0.336 | +55.56€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 175 | +0.325 | +50.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 175 | +0.325 | +50.74€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 8767 | -0.050 | +1828.60€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 8767 | -0.050 | +1828.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 403 | -0.053 | +344.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 403 | -0.053 | +344.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1673 | -0.129 | -10.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1673 | -0.129 | -10.04€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 940 | +0.188 | +521.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 940 | +0.188 | +521.00€ | 2 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2822 | -0.062 | +446.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2822 | -0.062 | +446.43€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2790 | -0.077 | +471.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2790 | -0.077 | +471.89€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 97 | +0.056 | +8.36€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 97 | +0.056 | +8.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 97 | +0.056 | +8.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 97 | +0.056 | +8.36€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 680 | +0.283 | +543.19€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 680 | +0.283 | +543.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 379 | +0.277 | +289.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 379 | +0.277 | +289.64€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 301 | +0.289 | +253.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 301 | +0.289 | +253.55€ | 0 | 12 |
| ✅ UPDOWN_OU_5M | 685 | -0.110 | -80.89€ | 6 | 0 |
| ✅ UPDOWN_OU_5M#5min | 685 | -0.110 | -80.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 183 | -0.073 | -12.69€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 183 | -0.073 | -12.69€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 66 | -0.176 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 66 | -0.176 | -10.12€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1852 | +0.303 | +939.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 616 | +0.244 | +99.15€ | 1 | 4 |
| ✅ WEEKLY_PRICE#ETH | 655 | +0.291 | +255.97€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 581 | +0.375 | +584.28€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.033 n=347 — no justifica filtro, seguir monitorizando
  - _Datos_: n=347 IC=+0.033 PNL=+24.30€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 442 celda(s) pasan gate riguroso completo de 2029 evaluadas (n>=40) y 2989 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.022 < 0.08 — monitorear
  - _Datos_: n=1752 IC=+0.022 PNL=+96.86€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=655/15 IC=+0.291 PNL=+255.97€ | BTC: n=616/15 IC=+0.244 PNL=+99.15€ | SOL: n=581/15 IC=+0.375 PNL=+584.28€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.093 n=175/60 | contraria IC=+0.118 n=155 | gap=-0.025 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=232, boost estimado=+0.005. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=515/40 IC=-0.009 PNL=-7.00€ | BTC#60min: n=636/40 IC=+0.000 PNL=+3.10€ | SOL#60min: n=282/40 IC=-0.007 PNL=-5.48€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.054 n=252860 | tras_1loss IC=+0.070 n=197885 | tras_2loss IC=+0.038 n=84969/40 | gap=+0.015 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=254 PNL=+157.57€
  - _Datos_: n=254 IC=+0.191 PNL=+157.57€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=31 PNL=+21.19€
  - _Datos_: n=31 IC=+0.227 PNL=+21.19€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.341 > 0.1 con n=1553 PNL=+929.02€
  - _Datos_: n=1553 IC=+0.341 PNL=+929.02€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=179 IC=+0.058 PNL=+20.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=179 IC=+0.058 PNL=+20.88€

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
  - _Estado_: n=1057 IC=-0.004 PNL=-13.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1057 IC=-0.004 PNL=-13.43€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=376 IC=-0.005 PNL=+4.06€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=376 IC=-0.005 PNL=+4.06€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=347 IC=+0.033 PNL=+24.30€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=347 IC=+0.033 PNL=+24.30€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.168 > 0.1 con n=1389 PNL=+766.39€
  - _Datos_: n=1389 IC=+0.168 PNL=+766.39€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=774 IC=+0.084 PNL=+182.93€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=774 IC=+0.084 PNL=+182.93€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.241 n=56) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=56 IC=+0.241 PNL=+31.18€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.02 con n=550 PNL=+218.01€
  - _Datos_: n=550 IC=+0.127 PNL=+218.01€

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
  - _Estado_: n=7836 IC=+0.049 PNL=+885.44€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=7836 IC=+0.049 PNL=+885.44€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.155 < -0.1 con n=146 PNL=+12.34€
  - _Datos_: n=146 IC=-0.155 PNL=+12.34€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1303 IC=+0.050 PNL=+161.69€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1303 IC=+0.050 PNL=+161.69€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=53 IC=-0.118 PNL=+6.20€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=53 IC=-0.118 PNL=+6.20€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.1 con n=242 PNL=+75.92€
  - _Datos_: n=242 IC=+0.131 PNL=+75.92€

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
  - _Estado_: n=13102 IC=-0.142 PNL=+664.56€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13102 IC=-0.142 PNL=+664.56€

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
  - _Estado_: n=1451 IC=+0.142 PNL=+779.27€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1451 IC=+0.142 PNL=+779.27€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.242 < -0.1 con n=1329 PNL=-196.23€
  - _Datos_: n=1329 IC=-0.242 PNL=-196.23€

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
  - _Estado_: 26/40 ops en el filtro definido (IC actual=+0.036 PNL=+7.17€)
  - _Datos_: n=26 IC=+0.036 PNL=+7.17€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=698) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=698 IC=+0.096 PNL=+174.49€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=372) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=372 IC=+0.414 PNL=+520.78€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=6843 IC=+0.168 PNL=-883.39€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6843 IC=+0.168 PNL=-883.39€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.1 con n=99 PNL=+62.52€
  - _Datos_: n=99 IC=+0.213 PNL=+62.52€
