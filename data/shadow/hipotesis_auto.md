# Hipótesis automáticas — 2026-09-15 16:04 UTC
_Generado por shadow_postmortem.py sobre 453593 resoluciones (PNL=+48745.18€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=426)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=409)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.250 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.201 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 67.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.8039` → IC=+0.256 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8039 (IC base=+0.121)

- **PATRÓN** `banda_z` > `10.374` → IC=+0.223 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.374 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.135 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=501)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 96.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.120 (n=409)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.037)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.465` → IC=-0.130 (n=160)

  - _Acción_: SKIP cuando `py_entrada` < 0.465
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=329)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.465` → IC=+0.252 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.465 (IC base=+0.127)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.210 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.127)

- **PATRÓN** `banda_hit_calibrado` > `0.7998` → IC=+0.273 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7998 (IC base=+0.127)

- **PATRÓN** `banda_z` > `11.438` → IC=+0.252 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.438 (IC base=+0.127)

- **PATRÓN** `ballenas_wallet_edge_medio` > `2.978` → IC=+0.133 (n=118)

  - _Acción_: Kelly boost +0.67€ cuando `ballenas_wallet_edge_medio` > 2.978 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=416)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 88.0 (IC base=+0.034)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.213 (n=99)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=86)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=85)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=96)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=-0.018)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.174)

- **PATRÓN** `n_total_lado` > `39.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 39.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.260 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `2707.1913` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2707.1913 (IC base=+0.174)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `145.91` → IC=-0.256 (n=5657)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.91
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=16971)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.82` → IC=-0.288 (n=785)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.82
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=2355)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `483.07` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 483.07
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=915)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `135.32` → IC=-0.284 (n=703)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.32
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2112)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `141.07` → IC=-0.157 (n=1455)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.07
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=4375)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.37` → IC=-0.252 (n=1335)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.37
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4005)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.95` → IC=-0.331 (n=1412)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.95
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=2872)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.38` → IC=-0.269 (n=145)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=304)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.170 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=324)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.274 (n=60)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=181)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.51` → IC=-0.259 (n=81)

  - _Acción_: SKIP cuando `py_entrada` < 0.51
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=27)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.172 (n=59)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=60)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.195 (n=11532)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.69 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=2860)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5240.5962` → IC=+0.167 (n=1824)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5240.5962 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=8683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=10539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.245 (n=7798)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=5663)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7162.5779` → IC=+0.176 (n=1790)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7162.5779 (IC base=+0.136)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.349 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `10987.7492` → IC=+0.202 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10987.7492 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1351)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.37` → IC=+0.274 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1728)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `12937.5849` → IC=+0.211 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12937.5849 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.176 (n=270)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=285)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `4643.6334` → IC=+0.149 (n=229)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4643.6334 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.167 (n=559)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.425 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=542)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `3846.6396` → IC=+0.158 (n=419)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3846.6396 (IC base=+0.134)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=160)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=1969)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.326 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=1034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.301 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.243 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `3739.174` → IC=+0.241 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3739.174 (IC base=+0.238)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=560)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.130 (n=539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 17.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.218 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=631)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1940.1614` → IC=+0.157 (n=357)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1940.1614 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.082)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=1071)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.423 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.269 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.181 (n=1106)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.142 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.230 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=326)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.125)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=8965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=8619)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.219 (n=3193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `5296.2198` → IC=+0.343 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5296.2198 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=2151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.179 (n=2229)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.168)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.293 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.347 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.290)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=2214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.180 (n=2119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=1892)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.246 (n=1979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.236 (n=1692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.320 (n=644)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=1843)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.193 (n=1538)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=26530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.237 (n=10153)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=5427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.175 (n=4608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=4872)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.169)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=4724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=4723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.271 (n=1700)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=4840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4883)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.169)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.235 (n=2358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=4389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=4352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.254 (n=2232)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=4448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=3570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.248 (n=1798)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.202 (n=4044)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.125)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.133 (n=3696)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.07 (IC base=+0.125)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.147 (n=4108)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.94 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=5471)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.125)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.150 (n=3687)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.33 (IC base=+0.125)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=2038)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.130)

- **PATRÓN** `restante_min` < `4.0` → IC=+0.136 (n=1831)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.0 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.146 (n=1944)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.93 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.147 (n=2705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `4.21` → IC=+0.149 (n=1824)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 4.21 (IC base=+0.130)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=2006)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.126 (n=2463)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.147 (n=1873)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=2454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `4.41` → IC=+0.145 (n=2448)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 4.41 (IC base=+0.119)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1604.9934` → IC=+0.297 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.9934 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.274)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.325 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `5072.5083` → IC=+0.290 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5072.5083 (IC base=+0.274)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.326 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.290 (n=441)
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
- **PATRÓN** `ibs_20min` > `0.9773` → IC=+0.230 (n=2003)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9773 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.6067` → IC=+0.243 (n=1605)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6067 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.703` → IC=+0.154 (n=3288)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.703 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.6145` → IC=+0.253 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6145 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `1.0752` → IC=+0.246 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0752 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.1751` → IC=+0.192 (n=4069)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1751 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.3093` → IC=+0.203 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3093 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `1.9304` → IC=+0.199 (n=2617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9304 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.5694` → IC=+0.130 (n=7398)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.5694 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.5729` → IC=+0.181 (n=450)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.5729 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.3455` → IC=+0.167 (n=2519)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3455 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `1.2072` → IC=+0.167 (n=2387)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2072 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.8714` → IC=+0.174 (n=1591)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8714 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2458` → IC=+0.222 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2458 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `1.4641` → IC=+0.198 (n=3974)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4641 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.206 (n=3743)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.059)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.186 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.186 (n=612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0069 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.188 (n=668)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 8.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.069` → IC=+0.280 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.069 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.203 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.6298` → IC=+0.156 (n=1241)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.6298 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.168 (n=1241)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=1229)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=904)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1923` → IC=+0.275 (n=674)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1923 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.250 (n=689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0571` → IC=+0.290 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0571 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.213` → IC=+0.243 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.213 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.232 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2878` → IC=+0.266 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2878 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.7379` → IC=+0.264 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7379 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1734.624` → IC=+0.246 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1734.624 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.221 (n=898)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.238 (n=449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=1019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9223` → IC=+0.254 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9223 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.2132` → IC=+0.219 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2132 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.3823` → IC=+0.213 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3823 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.095` → IC=+0.229 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.095 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.222 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2629 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8772` → IC=+0.215 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8772 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.218 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4925` → IC=+0.224 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4925 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.3852` → IC=+0.218 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3852 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `11927.4558` → IC=+0.226 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11927.4558 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.161 (n=968)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0048 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.169 (n=366)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.171 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6717` → IC=+0.177 (n=1098)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6717 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.156 (n=989)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1327 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.52` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 11.52 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.150 (n=1098)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2085 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.6867` → IC=+0.144 (n=981)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6867 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.192 (n=293)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.154 (n=989)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `13101.8647` → IC=+0.157 (n=732)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 13101.8647 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.162 (n=303)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 217.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.187 (n=1319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0057 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=505)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.457` → IC=+0.231 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.457 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.183 (n=1115)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.3768` → IC=+0.182 (n=171)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.3768 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `3.0416` → IC=+0.196 (n=558)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 3.0416 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=1502)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.218 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.3822` → IC=+0.231 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3822 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.615` → IC=+0.237 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.615 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.574` → IC=+0.214 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.574 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.8406` → IC=+0.202 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8406 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.2947` → IC=+0.222 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2947 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1889.461` → IC=+0.232 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1889.461 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.215 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.213)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1670)

- **PATRÓN** `ibs_20min` > `0.9299` → IC=+0.166 (n=282)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9299 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.3351` → IC=+0.335 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3351 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.4875` → IC=+0.330 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4875 (IC base=+0.007)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.258` → IC=+0.135 (n=524)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 4.258 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.5964` → IC=+0.378 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5964 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.1897` → IC=+0.351 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1897 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.362 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.4862` → IC=+0.349 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4862 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.8189` → IC=+0.343 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8189 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.344 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 167.0 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.163` → IC=+0.193 (n=187)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.163 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` < `0.4612` → IC=+0.146 (n=606)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.4612 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.152 (n=234)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.695 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.148 (n=177)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1643 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.225 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.5064` → IC=+0.180 (n=429)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.5064 (IC base=+0.001)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.140 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=234)

- **FILTRO** `ibs_20min` < `0.3636` → IC=-0.174 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3636
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=189)

- **FILTRO** `ibs_20min` > `0.2727` → IC=-0.128 (n=1708)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=847)

- **FILTRO** `sigma_ewma_delta_pct` > `8.613` → IC=-0.196 (n=278)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.613
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2277)

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

- **PATRÓN** `dist_vwap_pct` > `0.7042` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7042 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` < `1.1047` → IC=+0.201 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1047 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` > `0.9112` → IC=+0.181 (n=158)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.9112 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.2029` → IC=+0.203 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2029 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.1481` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1481 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.4885` → IC=+0.235 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4885 (IC base=-0.046)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6568` → IC=-0.191 (n=422)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1268)

- **FILTRO** `ibs_20min` < `0.7753` → IC=-0.140 (n=1267)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7753
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=423)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=376)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1314)

- **FILTRO** `ibs_20min` > `0.7736` → IC=-0.201 (n=639)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7736
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1919)

- **PATRÓN** `dist_vwap_pct` > `0.9637` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9637 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.2555` → IC=+0.291 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2555 (IC base=-0.086)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.287 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.086)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.266 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=-0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.8242` → IC=+0.281 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8242 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `1.0024` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0024 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` < `0.2603` → IC=+0.240 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2603 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` < `0.7351` → IC=+0.241 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7351 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` > `1.0875` → IC=+0.291 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0875 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1065` → IC=+0.257 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1065 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.2413` → IC=+0.258 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2413 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.4747` → IC=+0.236 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4747 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.240 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.174 (n=2507)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.009 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.9836` → IC=+0.288 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9836 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.704` → IC=+0.281 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.704 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.503` → IC=+0.142 (n=3554)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.503 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.6787` → IC=+0.234 (n=2277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6787 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2482` → IC=+0.258 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2482 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.4779` → IC=+0.239 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4779 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.7831` → IC=+0.235 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7831 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.277 (n=3535)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.139 (n=2570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0084 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.5563` → IC=+0.150 (n=6766)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5563 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.6812` → IC=+0.247 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6812 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2317` → IC=+0.229 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2317 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.715` → IC=+0.227 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.715 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `1.1996` → IC=+0.253 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1996 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.2511` → IC=+0.325 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2511 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` < `1.6234` → IC=+0.253 (n=1188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6234 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `2.37` → IC=+0.255 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.37 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.256 (n=2260)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.067)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.411` → IC=-0.161 (n=387)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.411
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1292)

- **PATRÓN** `ibs_20min` > `0.8645` → IC=+0.251 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8645 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.283` → IC=+0.149 (n=690)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.283 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.298 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.8491` → IC=+0.199 (n=350)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.8491 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.6525` → IC=+0.195 (n=175)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6525 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1673` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1673 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.9827` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9827 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.7276` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7276 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8286` → IC=-0.146 (n=566)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8286
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1702)

- **PATRÓN** `dist_vwap_pct` > `0.3046` → IC=+0.139 (n=247)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.3046 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `0.6545` → IC=+0.133 (n=581)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6545 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2215` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2215 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.162 (n=211)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.188 (n=206)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 235.0 (IC base=+0.008)

- **PATRÓN** `dist_vwap_pct` < `0.1603` → IC=+0.215 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1603 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `1.1352` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1352 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.351 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.777` → IC=+0.229 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.777 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1553` → IC=+0.227 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1553 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `503.0` → IC=+0.212 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 503.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.268 (n=1070)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0963` → IC=+0.248 (n=399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0963 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.241 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.254 (n=449)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.52` → IC=+0.270 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.52 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.11` → IC=+0.256 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.11 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.3455` → IC=+0.238 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3455 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `3.6325` → IC=+0.250 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6325 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.323 (n=434)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.322 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.286 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.885` → IC=+0.297 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.885 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.311 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.6234` → IC=+0.279 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6234 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.2254` → IC=+0.283 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2254 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `1881.0184` → IC=+0.297 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.0184 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.276 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.278)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2435` → IC=-0.213 (n=340)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2435
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1021)

- **FILTRO** `ibs_20min` > `0.8156` → IC=-0.182 (n=448)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8156
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1348)

- **PATRÓN** `ibs_20min` > `0.8024` → IC=+0.145 (n=463)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.8024 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.3046` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3046 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.9565` → IC=+0.207 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9565 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` > `0.6179` → IC=+0.191 (n=273)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.6179 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.268` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.268 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.479` → IC=+0.254 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.479 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.7393` → IC=+0.220 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7393 (IC base=-0.017)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.236 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 171.0 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.1237` → IC=+0.180 (n=98)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1237 (IC base=-0.018)

- **PATRÓN** `dist_vwap_pct` < `0.4612` → IC=+0.159 (n=244)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4612 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` < `0.979` → IC=+0.167 (n=193)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.979 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` > `0.7202` → IC=+0.172 (n=196)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.7202 (IC base=-0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.1528` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1528 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.258 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.235 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.206 (n=815)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.251 (n=826)

- **FILTRO** `ibs_20min` > `0.7143` → IC=-0.236 (n=433)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=1304)

- **FILTRO** `sigma_ewma_delta_pct` > `4.689` → IC=-0.168 (n=405)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.689
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1332)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.251 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.7623` → IC=+0.340 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7623 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.286 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8622 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.7204` → IC=+0.273 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7204 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1092` → IC=+0.275 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1092 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.315 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.321 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.129 (n=873)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.4 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` > `0.5824` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5824 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` < `0.3915` → IC=+0.180 (n=367)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3915 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.7176` → IC=+0.236 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7176 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.179 (n=316)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2193` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2193 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.5839` → IC=+0.203 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5839 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.5045` → IC=+0.180 (n=326)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.5045 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.216 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.323 (n=687)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.284 (n=485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.344 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.268)

- **PATRÓN** `dist_vwap_pct` > `0.2668` → IC=+0.316 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2668 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.295 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.268)

- **PATRÓN** `volumen_regimen` > `0.6887` → IC=+0.286 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6887 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.299 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `1.5512` → IC=+0.273 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5512 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.2094` → IC=+0.275 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2094 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.271 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `2582.8199` → IC=+0.275 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2582.8199 (IC base=+0.268)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.277 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0071 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0141` → IC=+0.291 (n=749)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0141 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.3861` → IC=+0.305 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3861 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.5433` → IC=+0.286 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5433 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` < `0.9062` → IC=+0.268 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9062 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.43` → IC=+0.287 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.43 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.312 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2418` → IC=+0.356 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2418 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `2.5474` → IC=+0.265 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5474 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.1719` → IC=+0.263 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1719 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.267 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `2562.9213` → IC=+0.274 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2562.9213 (IC base=+0.267)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.178 (n=1984)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0047 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.201 (n=1986)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3325` → IC=+0.172 (n=5232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3325 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=6209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6949` → IC=+0.229 (n=5312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6949 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1641` → IC=+0.199 (n=2595)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1641 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.233` → IC=+0.249 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.233 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.162 (n=3967)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2177 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6257` → IC=+0.159 (n=3967)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6257 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1069` → IC=+0.188 (n=2331)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1069 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.171 (n=2487)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6754` → IC=+0.168 (n=1882)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.6754 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3820.3005` → IC=+0.172 (n=1982)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3820.3005 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.184 (n=4857)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 123.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.188 (n=3857)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0063 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.207 (n=1929)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=2751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4587` → IC=+0.227 (n=5780)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4587 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2248` → IC=+0.162 (n=4286)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2248 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.27` → IC=+0.196 (n=1005)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.27 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1889` → IC=+0.156 (n=4222)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1889 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.627` → IC=+0.152 (n=4222)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.627 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.231 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5744` → IC=+0.173 (n=2255)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5744 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6497` → IC=+0.179 (n=1709)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6497 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.171 (n=4742)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 126.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.217 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.206 (n=454)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3121` → IC=+0.204 (n=1000)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3121 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.215 (n=499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.097` → IC=+0.309 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.097 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.240 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.5574` → IC=+0.183 (n=908)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.5574 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.182 (n=908)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.240 (n=644)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.247 (n=650)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.295 (n=486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.240 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.1057` → IC=+0.271 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1057 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.049` → IC=+0.251 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.049 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.096` → IC=+0.234 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.096 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.248 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.679` → IC=+0.242 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.679 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1592.8005` → IC=+0.252 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.8005 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.245 (n=288)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.2646` → IC=+0.174 (n=759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2646 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.200 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4304` → IC=+0.222 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4304 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.2181` → IC=+0.214 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2181 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.697` → IC=+0.228 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.697 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.2719` → IC=+0.176 (n=862)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.2719 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2363` → IC=+0.190 (n=188)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2363 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.199 (n=277)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `9831.6405` → IC=+0.182 (n=862)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9831.6405 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `407.0` → IC=+0.160 (n=690)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 407.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.182 (n=866)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0049 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0581` → IC=+0.200 (n=328)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0581 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.166 (n=905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 7.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.5219` → IC=+0.194 (n=984)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5219 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1377` → IC=+0.168 (n=995)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1377 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.118` → IC=+0.219 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.118 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2113` → IC=+0.164 (n=984)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2113 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1586` → IC=+0.186 (n=301)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1586 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.161 (n=874)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.160 (n=263)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 230.0 (IC base=+0.150)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.198 (n=980)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0058 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1945` → IC=+0.196 (n=653)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1945 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=455)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.584` → IC=+0.265 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.584 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.186 (n=803)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.218` → IC=+0.187 (n=282)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.218 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.681` → IC=+0.187 (n=305)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.681 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `3.6425` → IC=+0.200 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6425 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.228 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.223 (n=742)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0898` → IC=+0.249 (n=277)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0898 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.272 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.3443` → IC=+0.250 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3443 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.272 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.282 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `3.5271` → IC=+0.247 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5271 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1889.461` → IC=+0.238 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1889.461 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.208 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.181 (n=826)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0065 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4219` → IC=+0.167 (n=938)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4219 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.164 (n=944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.4078` → IC=+0.202 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4078 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1348` → IC=+0.196 (n=619)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1348 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.243 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.8633` → IC=+0.161 (n=626)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8633 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1977` → IC=+0.176 (n=313)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.1977 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.168 (n=305)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.5331` → IC=+0.187 (n=305)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.5331 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7289.8412` → IC=+0.191 (n=625)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7289.8412 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.161 (n=771)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 154.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.162 (n=1014)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0071 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3779` → IC=+0.143 (n=1013)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3779 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6027` → IC=+0.180 (n=1013)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6027 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.3378` → IC=+0.139 (n=1110)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3378 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.114` → IC=+0.193 (n=200)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 12.114 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8624` → IC=+0.142 (n=677)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8624 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.130 (n=1013)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6129 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.198 (n=147)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.134 (n=599)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7982 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4836` → IC=+0.141 (n=299)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4836 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `10007.3401` → IC=+0.153 (n=459)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10007.3401 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.149 (n=741)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0077 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5156` → IC=+0.195 (n=1110)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5156 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0114` → IC=+0.233 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0114 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.47` → IC=+0.253 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.47 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2208` → IC=+0.120 (n=1110)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2208 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.8007` → IC=+0.126 (n=712)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8007 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=1141)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2897.5388` → IC=+0.193 (n=503)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2897.5388 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.135 (n=806)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.152 (n=487)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0058 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.5429` → IC=+0.207 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5429 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.6992` → IC=+0.145 (n=201)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.6992 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.1923` → IC=+0.136 (n=1021)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1923 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.33` → IC=+0.158 (n=235)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 7.33 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.041` → IC=+0.129 (n=972)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.041 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2729` → IC=+0.184 (n=131)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2729 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4645` → IC=+0.132 (n=321)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4645 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.1727` → IC=+0.137 (n=436)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.1727 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3082.5359` → IC=+0.160 (n=368)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3082.5359 (IC base=+0.114)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` < `0.0271` → IC=+0.201 (n=1059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0271 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0178` → IC=+0.210 (n=706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0178 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1655` → IC=+0.218 (n=466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1655 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.7209` → IC=+0.255 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7209 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.2313` → IC=+0.234 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2313 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.342` → IC=+0.242 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.342 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.205 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.6122` → IC=+0.210 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6122 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.264 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1918` → IC=+0.214 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1918 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4286` → IC=+0.205 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4286 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.201 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2555.945` → IC=+0.202 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2555.945 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.235 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0221` → IC=+0.212 (n=509)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0221 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0909` → IC=+0.222 (n=375)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0909 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.216 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=515)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.4359` → IC=+0.242 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4359 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1412` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1412 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2669` → IC=+0.203 (n=1165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2669 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.305` → IC=+0.236 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.305 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6302` → IC=+0.218 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6302 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.284 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2444` → IC=+0.198 (n=868)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.2444 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4623` → IC=+0.192 (n=987)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4623 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2526.9853` → IC=+0.212 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2526.9853 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.147 (n=477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0038 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.153 (n=647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0073 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0966` → IC=+0.151 (n=476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0966 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.3952` → IC=+0.169 (n=1425)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3952 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.821` → IC=+0.165 (n=204)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.821 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.703` → IC=+0.166 (n=648)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.703 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8672` → IC=+0.154 (n=817)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8672 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1644` → IC=+0.166 (n=393)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1644 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.157 (n=456)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.5764` → IC=+0.157 (n=455)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5764 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=1573)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `8223.8718` → IC=+0.159 (n=646)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8223.8718 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.160 (n=1203)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 156.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.155 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0037 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.127 (n=1317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=1511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.4833` → IC=+0.157 (n=1317)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4833 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2135` → IC=+0.124 (n=1311)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.2135 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.807` → IC=+0.134 (n=591)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 3.807 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2294` → IC=+0.123 (n=1318)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2294 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.142 (n=386)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.2373` → IC=+0.135 (n=1257)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.2373 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.129 (n=596)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 27.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1032` → IC=+0.150 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1032 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.145 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.2977` → IC=+0.142 (n=319)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.2977 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.6913` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6913 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.256` → IC=+0.167 (n=151)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.256 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6933` → IC=+0.171 (n=141)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6933 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` > `0.0904` → IC=+0.128 (n=119)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.0904 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `9647.1518` → IC=+0.142 (n=319)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 9647.1518 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 150.0 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.206 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.146 (n=467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.3483` → IC=+0.207 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3483 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.1864` → IC=+0.145 (n=468)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1864 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.406` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 4.406 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.129 (n=467)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1917 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.164 (n=212)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.0609 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.204 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.1106` → IC=+0.156 (n=402)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1106 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.132 (n=457)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.160 (n=148)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 159.0 (IC base=+0.125)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.254 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.209 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.216 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.2679` → IC=+0.233 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2679 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.220 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.116` → IC=+0.227 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.116 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.203 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.223 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2528` → IC=+0.312 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2528 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.3745` → IC=+0.233 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3745 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.3885` → IC=+0.259 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3885 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `12369.1399` → IC=+0.216 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12369.1399 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.133 (n=379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0065 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.0998` → IC=+0.159 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0998 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.137 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 11.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.2943` → IC=+0.163 (n=253)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.2943 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.48` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 6.48 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6996` → IC=+0.151 (n=167)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6996 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2209` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2209 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.5396` → IC=+0.129 (n=321)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.5396 (IC base=+0.105)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3831` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3831
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=346)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.205 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.7157` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.7157 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.151 (n=130)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `2963.0907` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2963.0907 (IC base=+0.075)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.128 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 14.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.4524` → IC=+0.168 (n=272)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.4524 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.921` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 8.921 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.7227` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7227 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `2.513` → IC=+0.131 (n=250)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.513 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.133 (n=216)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 44.0 (IC base=+0.085)

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
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.194 (n=3406)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0085 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=7859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.213 (n=7513)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.896` → IC=+0.201 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.896 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.579` → IC=+0.222 (n=3689)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.579 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.163 (n=3379)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8847 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2398` → IC=+0.188 (n=1432)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2398 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.183 (n=2384)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.171 (n=8984)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.04 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3784.5011` → IC=+0.170 (n=2504)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3784.5011 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.195 (n=5416)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 95.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.197 (n=4624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0066 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4746` → IC=+0.183 (n=6928)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4746 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5567` → IC=+0.238 (n=6928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5567 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2345` → IC=+0.164 (n=4356)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2345 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.853` → IC=+0.203 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.853 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7033` → IC=+0.159 (n=2106)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7033 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.2029` → IC=+0.161 (n=1595)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.2029 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.254 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.3011` → IC=+0.189 (n=2810)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.3011 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.177 (n=5806)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 127.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.218 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.233 (n=575)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.208 (n=631)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.319 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.378` → IC=+0.292 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.378 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.244 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` < `1.559` → IC=+0.186 (n=517)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.559 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.2672` → IC=+0.197 (n=532)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2672 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=1136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.259 (n=875)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.254)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.265 (n=889)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.1993` → IC=+0.279 (n=664)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1993 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.3409` → IC=+0.284 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3409 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.611` → IC=+0.263 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.611 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.226` → IC=+0.296 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.226 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `1.9051` → IC=+0.280 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9051 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1582.26` → IC=+0.267 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.26 (IC base=+0.254)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.187 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0027 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1823` → IC=+0.156 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1823 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.6917` → IC=+0.243 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6917 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.3462` → IC=+0.200 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3462 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.805` → IC=+0.158 (n=279)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.805 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.374` → IC=+0.152 (n=1053)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.374 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6942` → IC=+0.182 (n=524)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6942 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.181 (n=327)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4223` → IC=+0.156 (n=1137)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4223 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7608` → IC=+0.158 (n=758)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7608 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10716.3301` → IC=+0.169 (n=1063)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10716.3301 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `495.0` → IC=+0.162 (n=1069)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 495.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.178 (n=712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0037 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.3225` → IC=+0.168 (n=1067)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3225 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.182 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 18.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.6376` → IC=+0.207 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6376 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.7006` → IC=+0.161 (n=169)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7006 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.1325` → IC=+0.167 (n=975)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1325 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.581` → IC=+0.189 (n=191)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.581 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.166 (n=1067)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1954 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1498` → IC=+0.211 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1498 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.172 (n=970)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.5156` → IC=+0.162 (n=866)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5156 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `376.0` → IC=+0.164 (n=582)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 376.0 (IC base=+0.157)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.223 (n=1186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=1245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.221 (n=586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.675` → IC=+0.250 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.675 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.541` → IC=+0.296 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.541 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.2176` → IC=+0.216 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2176 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `3.0059` → IC=+0.233 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0059 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.246 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.230)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.230 (n=521)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.3664` → IC=+0.267 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3664 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.708` → IC=+0.279 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.708 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.3595` → IC=+0.301 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3595 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.791` → IC=+0.224 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.791 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.2457` → IC=+0.226 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2457 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `1893.9584` → IC=+0.230 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1893.9584 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.242 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.230)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.173 (n=561)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0038 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.140 (n=426)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.7095` → IC=+0.234 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7095 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.353` → IC=+0.182 (n=483)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.353 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.295` → IC=+0.165 (n=545)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.295 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8808` → IC=+0.157 (n=850)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8808 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.227 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.5033` → IC=+0.147 (n=539)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.5033 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.7526` → IC=+0.154 (n=817)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7526 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8808.1502` → IC=+0.229 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8808.1502 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.157 (n=383)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 90.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.160 (n=905)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0065 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4329` → IC=+0.153 (n=1027)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4329 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6877` → IC=+0.191 (n=1027)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6877 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.2045` → IC=+0.144 (n=955)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2045 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.113` → IC=+0.205 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.113 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8608` → IC=+0.142 (n=685)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8608 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1836` → IC=+0.152 (n=343)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1836 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.269 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.557` → IC=+0.151 (n=422)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.557 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.472` → IC=+0.173 (n=319)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.472 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10973.4331` → IC=+0.187 (n=343)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 10973.4331 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `195.0` → IC=+0.144 (n=950)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 195.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.178 (n=1299)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.4667 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0026` → IC=+0.191 (n=228)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 1.0026 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.447` → IC=+0.220 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.447 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=905)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2907.4324` → IC=+0.242 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2907.4324 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.127 (n=955)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 53.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.177 (n=550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0061 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1233` → IC=+0.149 (n=417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1233 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.209 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.625 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.4725` → IC=+0.131 (n=1227)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4725 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.437` → IC=+0.125 (n=1205)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.437 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.156 (n=550)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.72 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2178` → IC=+0.172 (n=190)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2178 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4623` → IC=+0.140 (n=365)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4623 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.2143` → IC=+0.124 (n=496)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.2143 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2921.4363` → IC=+0.166 (n=417)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2921.4363 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.218 (n=593)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.205 (n=1169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.312 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1854` → IC=+0.235 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1854 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.552` → IC=+0.242 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.552 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2447` → IC=+0.205 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2447 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.210 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.232 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.5902` → IC=+0.238 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5902 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2565.3121` → IC=+0.211 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2565.3121 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.235 (n=482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.219 (n=482)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=694)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.200 (n=1529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.505` → IC=+0.255 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.505 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.8572` → IC=+0.204 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8572 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.008` → IC=+0.260 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.008 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.241 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.258 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2267` → IC=+0.194 (n=1112)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2267 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4437` → IC=+0.197 (n=1263)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4437 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2541.3638` → IC=+0.201 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2541.3638 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=2556)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.154 (n=2218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0094 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.5293` → IC=+0.155 (n=2521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5293 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 18.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.160 (n=877)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.9375` → IC=+0.211 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9375 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1891` → IC=+0.154 (n=820)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1891 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.736` → IC=+0.166 (n=809)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.736 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.9065` → IC=+0.151 (n=1022)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9065 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1739` → IC=+0.172 (n=688)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1739 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4626` → IC=+0.162 (n=832)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4626 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.9088` → IC=+0.157 (n=1663)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9088 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `8191.84` → IC=+0.152 (n=1143)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8191.84 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.189 (n=644)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4861` → IC=+0.157 (n=1929)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4861 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.163 (n=647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 4.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.1769` → IC=+0.162 (n=849)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1769 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.7057` → IC=+0.147 (n=344)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7057 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.261` → IC=+0.147 (n=1912)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.261 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1151` → IC=+0.148 (n=1610)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1151 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.153 (n=909)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.5735` → IC=+0.143 (n=1909)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5735 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.8264` → IC=+0.149 (n=1273)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8264 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=2556)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7756.2728` → IC=+0.150 (n=1723)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7756.2728 (IC base=+0.138)

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

- **PATRÓN** `drift_60min` |x|≤ `0.3644` → IC=+0.147 (n=861)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3644 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.171 (n=314)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1518` → IC=+0.164 (n=379)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1518 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.145 (n=390)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6078 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.6015` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6015 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.136 (n=887)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.212` → IC=+0.158 (n=840)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.212 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.181 (n=574)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.8855 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0692` → IC=+0.163 (n=408)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0692 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.5736` → IC=+0.143 (n=858)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5736 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.148 (n=572)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `11340.2858` → IC=+0.150 (n=861)

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
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.151 (n=745)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0088 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.148 (n=746)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0045 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.5048` → IC=+0.152 (n=745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.5048 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.152 (n=271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 4.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.5389` → IC=+0.145 (n=497)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5389 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.1834` → IC=+0.154 (n=746)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.1834 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.9678` → IC=+0.175 (n=164)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.9678 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.4249` → IC=+0.150 (n=710)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.4249 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.152 (n=745)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.9097` → IC=+0.147 (n=497)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.9097 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.2712` → IC=+0.153 (n=249)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2712 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.1172` → IC=+0.143 (n=688)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1172 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1782` → IC=+0.164 (n=221)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1782 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.168 (n=245)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=707)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `8269.6944` → IC=+0.152 (n=745)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8269.6944 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.166 (n=537)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0071 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.5119` → IC=+0.183 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.5119 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.158 (n=407)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 10.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.0983` → IC=+0.167 (n=610)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0983 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.176 (n=273)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.4005` → IC=+0.153 (n=626)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4005 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.98` → IC=+0.169 (n=137)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 8.98 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.652` → IC=+0.184 (n=204)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.652 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.7329` → IC=+0.154 (n=545)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7329 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1527` → IC=+0.157 (n=627)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1527 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.175 (n=263)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.166 (n=528)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4508` → IC=+0.166 (n=599)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4508 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `8205.2722` → IC=+0.172 (n=610)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8205.2722 (IC base=+0.151)

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
- **FILTRO** `sigma_h` > `0.008` → IC=-0.258 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.008
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=280)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=292)

- **FILTRO** `dist_vwap_pct` > `0.1654` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1654
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=215)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.180 (n=429)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0051 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.164 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.215 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.1343` → IC=+0.166 (n=285)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1343 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.473` → IC=+0.185 (n=341)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.473 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `0.7924` → IC=+0.125 (n=366)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.7924 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `2.5088` → IC=+0.150 (n=444)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.5088 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=444)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.158 (n=238)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.0688` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0688 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1654` → IC=+0.136 (n=215)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1654 (IC base=-0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.931` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.931 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.0849` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0849 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.6357` → IC=+0.173 (n=145)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.6357 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.4611` → IC=+0.151 (n=130)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4611 (IC base=-0.017)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=153)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=-0.017)

- **PATRÓN** `libro_liquidez` > `2556.9997` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2556.9997 (IC base=-0.017)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.176 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.006 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.5781` → IC=+0.212 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5781 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.188 (n=91)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.734` → IC=+0.139 (n=120)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 3.734 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.0527` → IC=+0.131 (n=166)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0527 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.152 (n=133)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2602` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2602 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.0198` → IC=+0.189 (n=133)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.0198 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2835.039` → IC=+0.127 (n=175)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2835.039 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.0401` → IC=+0.231 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0401 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.4946` → IC=+0.230 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4946 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.732` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 4.732 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.9536` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.9536 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `2.4111` → IC=+0.226 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4111 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `3575.5947` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3575.5947 (IC base=+0.052)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.300 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=85)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=78)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.173 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0049 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.143 (n=197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.6407` → IC=+0.245 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6407 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.5279` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5279 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.057` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.057 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.789` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.789 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6219 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7434` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.7434 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.3826` → IC=+0.143 (n=141)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.3826 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.152 (n=199)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `1072.6991` → IC=+0.191 (n=166)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 1072.6991 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.0933` → IC=+0.186 (n=33)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0933 (IC base=-0.048)

- **PATRÓN** `ibs_20min` < `0.1926` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1926 (IC base=-0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.257` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.257 (IC base=-0.048)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.412` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.412 (IC base=-0.048)

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
  - _Potencial_: sin este filtro IC_bueno=+0.199 (n=171)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.238 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=60)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.321 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.291 (n=41)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.170 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.076)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.132 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 14.0 (IC base=+0.076)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.199 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6744 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1756` → IC=+0.133 (n=96)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.1756 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.655` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.655 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0643 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` < `2.5513` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5513 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `601.2615` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 601.2615 (IC base=+0.076)

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
- **FILTRO** `volumen_regimen` < `1.6687` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6687
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

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
- **FILTRO** `ibs_20min` > `0.3333` → IC=-0.149 (n=72)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3333
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=220)

- **PATRÓN** `ibs_20min` > `0.7368` → IC=+0.134 (n=189)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.7368 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.2365` → IC=+0.136 (n=193)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.2365 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.126` → IC=+0.143 (n=96)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.126 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.157 (n=100)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.048)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=76)

- **FILTRO** `ibs_20min` < `0.5499` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5499
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=69)

- **FILTRO** `volumen_regimen` < `0.758` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.758
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=69)

- **FILTRO** `volumen_spike_ratio` < `1.4594` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4594
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=48)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.144 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0023 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.2127` → IC=+0.143 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2127 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.230 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.171 (n=86)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1622 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.629` → IC=+0.129 (n=103)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 13.629 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `1.8898` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8898 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3566.36` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3566.36 (IC base=+0.103)

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
- **FILTRO** `ibs_20min` > `0.4` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=45)

- **FILTRO** `dist_vwap_pct` > `0.1415` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1415
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=46)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.161 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.3838` → IC=+0.148 (n=86)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3838 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.155 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.7143` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.7143 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.7692 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1961` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1961 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.5494` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5494 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `514.5372` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 514.5372 (IC base=+0.147)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=443)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2816.9896` → IC=+0.175 (n=158)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2816.9896 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2303.417` → IC=+0.125 (n=529)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2303.417 (IC base=+0.097)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=443)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2816.9896` → IC=+0.175 (n=158)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2816.9896 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2303.417` → IC=+0.125 (n=529)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2303.417 (IC base=+0.097)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1312)

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
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=90)

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

- **PATRÓN** `liq_usd_total` > `58893.21` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `liq_usd_total` > 58893.21 (IC base=+0.018)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=555)

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
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=437)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=248)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=248)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9969` → IC=-0.142 (n=65)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9969
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=198)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=158)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=158)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=131)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=74)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=158)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.125 (n=1004)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=5392)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6137)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=1028)

- **FILTRO** `libro_liquidez` < `15888.9153` → IC=-0.153 (n=260)

  - _Acción_: SKIP cuando `libro_liquidez` < 15888.9153
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=783)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1306)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.178 (n=2574)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=7841)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.171 (n=2670)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=8187)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.216 (n=420)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=1327)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.197 (n=443)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=1357)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.216 (n=456)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=1449)

- **FILTRO** `ibs_20min` > `0.287` → IC=-0.170 (n=476)

  - _Acción_: SKIP cuando `ibs_20min` > 0.287
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1429)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.201 (n=420)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=1303)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.194 (n=465)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1446)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2366)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2360)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2366)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=269)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.7128` → IC=-0.203 (n=116)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7128
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=117)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=152)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=611)

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
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=17031)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.281 (n=5674)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=18854)

- **FILTRO** `ibs_7min` < `0.7062` → IC=-0.238 (n=6131)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7062
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=18397)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.160 (n=8147)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=16381)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.224 (n=7646)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=23076)

- **FILTRO** `ibs_7min` > `0.2972` → IC=-0.177 (n=7679)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2972
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=23043)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=924)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=2990)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.257 (n=1291)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2623)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.193 (n=950)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=2964)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=3595)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1755)

- **FILTRO** `ibs_7min` > `0.7979` → IC=-0.206 (n=1337)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7979
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=4013)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.139 (n=988)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=3306)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.254 (n=995)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3299)

- **FILTRO** `ibs_7min` < `0.7596` → IC=-0.186 (n=1073)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7596
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3221)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.170 (n=1072)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3222)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.255 (n=1018)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=3332)

- **FILTRO** `ibs_7min` > `0.2506` → IC=-0.167 (n=1087)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2506
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3263)

- **FILTRO** `ballena_activa_n` > `114.0` → IC=-0.164 (n=1468)

  - _Acción_: SKIP cuando `ballena_activa_n` > 114.0
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2882)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.181 (n=898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=2784)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.320 (n=881)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2801)

- **FILTRO** `drift_7min_pct` |x|> `0.1811` → IC=-0.131 (n=1251)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1811
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=2431)

- **FILTRO** `ibs_7min` < `0.2033` → IC=-0.273 (n=920)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2033
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2762)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.218 (n=891)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=2791)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.235 (n=1317)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=4301)

- **FILTRO** `ibs_7min` > `0.2647` → IC=-0.157 (n=1907)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2647
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3711)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=1277)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=2755)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=972)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3060)

- **FILTRO** `ibs_7min` < `0.7456` → IC=-0.191 (n=1008)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7456
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3024)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.184 (n=988)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3044)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1012)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3120)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.176 (n=1032)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3100)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.181 (n=1027)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3105)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.240 (n=1100)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3354)

- **FILTRO** `ibs_7min` < `0.7241` → IC=-0.210 (n=1110)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7241
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3344)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.176 (n=1401)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=4408)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.124 (n=1246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=2906)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.279 (n=994)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3158)

- **FILTRO** `ibs_7min` < `0.7333` → IC=-0.228 (n=1038)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=3114)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.204 (n=1020)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3132)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.205 (n=1305)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=4158)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=949)

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
- **PATRÓN** `delta_ratio` |x|> `0.417` → IC=+0.146 (n=413)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.417 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.135 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.120)

- **PATRÓN** `total_vol_5m` < `486.9033` → IC=+0.146 (n=207)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 486.9033 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.132 (n=259)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 27.0 (IC base=+0.120)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.135)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `total_vol_5m` < `681.9263` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 681.9263 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 73.0 (IC base=+0.092)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.193 (n=112)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.211 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.156)

- **PATRÓN** `total_vol_5m` < `5917.212` → IC=+0.163 (n=99)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 5917.212 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `3200.0566` → IC=+0.167 (n=100)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3200.0566 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 37.0 (IC base=+0.156)

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
- **FILTRO** `sigma_h` > `0.0078` → IC=-0.351 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=181)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.162 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=-0.154)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `57.4676` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `T_h` > 57.4676
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0053 (IC base=-0.155)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.222 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.217 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=71)

- **FILTRO** `T_h` > `71.1632` → IC=-0.174 (n=210)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=71)

- **FILTRO** `pct_vs_K` |x|> `4.4208` → IC=-0.449 (n=57)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4208
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=172)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.7217` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7217
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=68)

- **FILTRO** `T_h` > `144.6177` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `T_h` > 144.6177
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=61)

- **FILTRO** `pct_vs_K` |x|> `3.3729` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3729
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
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
- **FILTRO** `sigma_h` > `0.0143` → IC=-0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0143
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

- **FILTRO** `sigma_h` < `0.01` → IC=-0.219 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=31)

- **FILTRO** `T_h` > `135.9709` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `T_h` > 135.9709
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

- **FILTRO** `sigma_h` < `0.0142` → IC=-0.375 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=10)

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

- **PATRÓN** `edge` > `0.21` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.21 (IC base=+0.476)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.473 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0108 (IC base=+0.476)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.462 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.476)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.463 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.476)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.480 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.476)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.461 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.476)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.468 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.476)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=123)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=217)

- **FILTRO** `streak_estiramiento` > `0.8581` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8581
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=133)

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
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=505)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=511)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=448)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=912)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=521)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=557)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2291)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1181)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1189)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.190 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.190 (n=475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0071 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.170 (n=461)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.168)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0587` → IC=+0.172 (n=1047)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.0587 (IC base=+0.168)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3418` → IC=+0.204 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3418 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.168)

- **PATRÓN** `ibs_15` > `0.6154` → IC=+0.239 (n=1047)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6154 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1497` → IC=+0.165 (n=518)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1497 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.5472` → IC=+0.166 (n=1101)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.5472 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.868` → IC=+0.241 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.868 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `5104.4221` → IC=+0.179 (n=475)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 5104.4221 (IC base=+0.168)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=330)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.213 (n=176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.196 (n=264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0023 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0624` → IC=+0.244 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0624 (IC base=+0.194)

- **PATRÓN** `drift_15min` |x|≤ `0.3761` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3761 (IC base=+0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.211 (n=88)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3892` → IC=+0.229 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3892 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.210 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.7061` → IC=+0.244 (n=264)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7061 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.203 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.491` → IC=+0.246 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.491 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `13812.6413` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13812.6413 (IC base=+0.194)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.144 (n=251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0061 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.140 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.128)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1428` → IC=+0.157 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1428 (IC base=+0.128)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2698` → IC=+0.161 (n=160)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2698 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.133 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 11.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.136 (n=251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 16.0 (IC base=+0.128)

- **PATRÓN** `ibs_15` > `0.6489` → IC=+0.219 (n=251)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6489 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1444` → IC=+0.151 (n=196)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1444 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `10110.2635` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 10110.2635 (IC base=+0.128)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

- **FILTRO** `ibs_15` > `0.2175` → IC=-0.250 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2175
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=45)

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
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=578)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `ibs_15` < `0.5263` → IC=-0.125 (n=70)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5263
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=145)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.524` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.524 (IC base=+0.008)

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

- **PATRÓN** `ibs_15` < `0.1053` → IC=+0.179 (n=331)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` < 0.1053 (IC base=+0.050)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.372 (n=100)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.330)

- **PATRÓN** `drift_60min` |x|≤ `0.1549` → IC=+0.338 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1549 (IC base=+0.330)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.337 (n=200)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.330)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2954` → IC=+0.365 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2954 (IC base=+0.330)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.330)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.385 (n=268)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.374 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.219` → IC=+0.335 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.219 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.330 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.330)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `3397.72` → IC=+0.344 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3397.72 (IC base=+0.330)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1204` → IC=+0.342 (n=74)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1204 (IC base=+0.332)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.362 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.1544` → IC=+0.340 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1544 (IC base=+0.332)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1021` → IC=+0.337 (n=151)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1021 (IC base=+0.332)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.404 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.348 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.332)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.332 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.332)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.365 (n=168)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.384 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `9126.9924` → IC=+0.351 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9126.9924 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `554.0` → IC=+0.388 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 554.0 (IC base=+0.332)

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
- **FILTRO** `sigma_h` > `0.0125` → IC=-0.200 (n=525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0125
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1578)

- **FILTRO** `ibs_15` < `0.6046` → IC=-0.184 (n=175)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6046
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=525)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.207 (n=247)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=1856)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2875` → IC=+0.217 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2875 (IC base=-0.058)

- **PATRÓN** `ibs_15` > `0.6046` → IC=+0.248 (n=525)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6046 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.167 (n=409)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.058)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1204` → IC=+0.238 (n=728)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1204 (IC base=-0.046)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1821` → IC=+0.236 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1821 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.278 (n=1092)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `0.6528` → IC=+0.262 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6528 (IC base=-0.046)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.207 (n=312)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=938)

- **FILTRO** `sigma_h` < `0.0032` → IC=-0.233 (n=312)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=938)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.212 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=454)

- **FILTRO** `sigma_ewma_delta_pct` > `19.843` → IC=-0.246 (n=226)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.843
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1024)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.148 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.003 (IC base=+0.073)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.245 (n=53)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.073)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.073)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.338 (n=103)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1129` → IC=+0.250 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1129 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.4975` → IC=+0.273 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4975 (IC base=+0.073)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.65` → IC=-0.236 (n=85)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.247 (n=255)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=323)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.148 (n=228)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0039 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0771` → IC=+0.213 (n=113)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0771 (IC base=+0.126)

- **PATRÓN** `drift_15min` |x|≤ `0.4178` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `drift_15min` |x|≤ 0.4178 (IC base=+0.126)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.128 (n=170)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.126)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.222 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.170 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 16.0 (IC base=+0.126)

- **PATRÓN** `ibs_15` > `0.65` → IC=+0.247 (n=255)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.65 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.838` → IC=+0.134 (n=274)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 18.838 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=323)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.247 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.3595` → IC=+0.230 (n=402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3595 (IC base=+0.223)

- **PATRÓN** `drift_15min` |x|≤ `0.766` → IC=+0.225 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.766 (IC base=+0.223)

- **PATRÓN** `delta_ratio_macro` |x|> `0.209` → IC=+0.256 (n=207)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.209 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.223 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.235 (n=307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.271 (n=457)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.3774` → IC=+0.250 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3774 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.178` → IC=+0.237 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.178 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.1` → IC=+0.226 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.1 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3638.7885` → IC=+0.223 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3638.7885 (IC base=+0.223)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0701` → IC=+0.209 (n=204)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0701 (IC base=-0.043)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.245 (n=229)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` < `0.1618` → IC=+0.204 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1618 (IC base=-0.043)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.019` → IC=-0.252 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.019
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=317)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=459)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.351 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.297 (n=323)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `1.0781` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0781 (IC base=-0.046)

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
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.294 (n=342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.282 (n=512)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.303 (n=226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1424` → IC=+0.290 (n=341)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1424 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.109` → IC=+0.325 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.109 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.299 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.323 (n=512)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.322 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.754` → IC=+0.312 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.754 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.285 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `12445.3624` → IC=+0.299 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12445.3624 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.289 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.274 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0025 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0604` → IC=+0.296 (n=96)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0604 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.3849` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3849 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.294 (n=95)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3684` → IC=+0.294 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3684 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.331 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.8593` → IC=+0.302 (n=255)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8593 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.976` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.976 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `11995.5068` → IC=+0.297 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11995.5068 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.302 (n=200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.290 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0692` → IC=+0.314 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0692 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.310 (n=151)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.331 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.317 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.334 (n=227)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2755` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2755 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` < `0.4406` → IC=+0.292 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4406 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.72` → IC=+0.314 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.72 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.976` → IC=+0.292 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 18.976 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.300 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.292 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.289)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.297` → IC=-0.156 (n=30)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.297
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6154 sube el IC de +0.168 a +0.239 en UPDOWN_GBM#15min (n=1047). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7061 sube el IC de +0.194 a +0.244 en UPDOWN_GBM#BTC#15min (n=264). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6489 sube el IC de +0.128 a +0.219 en UPDOWN_GBM#ETH#15min (n=251). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.587 sube el IC de +0.133 a +0.236 en UPDOWN_GBM#SOL#15min (n=146). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5354 sube el IC de +0.175 a +0.271 en UPDOWN_GBM#XRP#15min (n=299). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1053 sube el IC de +0.050 a +0.179 en UPDOWN_GBM#XRP#15min (n=331). Ya aplicado como kelly_boost=+0.89€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6046 sube el IC de -0.058 a +0.248 en UPDOWN_GBM_15M_TARDIO (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.046 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1092). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.073 a +0.338 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=103). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.65 sube el IC de +0.126 a +0.247 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3605 sube el IC de +0.223 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=457). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.146 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.043 a +0.245 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=229). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.046 a +0.297 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=323). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.282 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=512). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8593 sube el IC de +0.275 a +0.302 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.289 a +0.334 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=227). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.330 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=268). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.332 a +0.365 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=168). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.325 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=132). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1149 | +0.083 | +134.99€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1149 | +0.083 | +134.99€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 830 | +0.089 | +109.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 830 | +0.089 | +109.96€ | 3 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 239 | +0.048 | +6.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 239 | +0.048 | +6.27€ | 4 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 54 | +0.161 | +20.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 54 | +0.161 | +20.25€ | 0 | 5 |
| ✅ BALLENAS_TARDIAS | 20187 | -0.105 | -2890.81€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1219 | -0.042 | -202.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 18968 | -0.109 | -2688.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3140 | -0.122 | -556.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3140 | -0.122 | -556.81€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1219 | -0.042 | -202.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1219 | -0.042 | -202.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5830 | -0.052 | -587.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5830 | -0.052 | -587.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5340 | -0.115 | -414.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5340 | -0.115 | -414.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4284 | -0.166 | -968.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4284 | -0.166 | -968.47€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 11784 | -0.043 | +4266.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3175 | -0.008 | +1846.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 8609 | -0.056 | +2420.84€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 11784 | -0.043 | +4266.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3175 | -0.008 | +1846.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 8609 | -0.056 | +2420.84€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 868 | -0.105 | -131.52€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 51 | -0.104 | -12.07€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 817 | -0.104 | -119.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 496 | -0.076 | -65.28€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 35 | -0.122 | -9.20€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 461 | -0.072 | -56.08€ | 1 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 243 | -0.165 | -56.57€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 16 | -0.044 | -2.87€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 227 | -0.172 | -53.70€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 68 | -0.057 | -9.53€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 68 | -0.057 | -9.53€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 73096 | +0.113 | -3837.86€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 11487 | +0.182 | -366.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 280 | -0.117 | -46.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 56247 | +0.100 | -3317.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5082 | +0.116 | -108.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 9373 | +0.096 | -888.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 37 | -0.141 | -0.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 9321 | +0.098 | -876.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 14777 | +0.131 | -326.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3499 | +0.201 | -119.59€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 9320 | +0.108 | -201.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1916 | +0.116 | +16.91€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 9415 | +0.088 | -936.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 44 | -0.065 | -4.30€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 9356 | +0.090 | -920.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 15662 | +0.125 | -302.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4426 | +0.171 | -77.80€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 9397 | +0.108 | -165.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1827 | +0.099 | -51.45€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 14479 | +0.117 | -813.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3444 | +0.186 | -173.96€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 183 | -0.073 | +7.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 9513 | +0.092 | -573.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1339 | +0.138 | -73.60€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 9390 | +0.102 | -570.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 37 | -0.013 | +9.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 9340 | +0.103 | -580.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 11558 | +0.188 | -803.46€ | 3 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 11558 | +0.188 | -803.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2847 | +0.168 | -306.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2847 | +0.168 | -306.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 587 | +0.181 | +8.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 587 | +0.181 | +8.25€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2795 | +0.176 | -265.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2795 | +0.176 | -265.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2512 | +0.236 | -77.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2512 | +0.236 | -77.62€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2738 | +0.191 | -176.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2738 | +0.191 | -176.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 536 | +0.433 | -10.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 536 | +0.433 | -10.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 205 | +0.437 | -1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 205 | +0.437 | -1.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 203 | +0.442 | +0.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 203 | +0.442 | +0.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 121 | +0.402 | -8.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 121 | +0.402 | -8.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 39454 | +0.194 | -3336.51€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 39454 | +0.194 | -3336.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6879 | +0.169 | -884.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6879 | +0.169 | -884.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6254 | +0.222 | -244.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6254 | +0.222 | -244.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6833 | +0.169 | -874.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6833 | +0.169 | -874.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6344 | +0.218 | -264.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6344 | +0.218 | -264.61€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6512 | +0.202 | -449.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6512 | +0.202 | -449.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6632 | +0.191 | -619.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6632 | +0.191 | -619.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 14704 | +0.125 | +288.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 14704 | +0.125 | +288.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7293 | +0.130 | +205.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7293 | +0.130 | +205.30€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7411 | +0.119 | +83.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7411 | +0.119 | +83.19€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1225 | +0.287 | -25.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1225 | +0.287 | -25.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 541 | +0.274 | -18.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 541 | +0.274 | -18.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 585 | +0.290 | -5.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 585 | +0.290 | -5.09€ | 0 | 4 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 832 | +0.067 | -45.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 294 | +0.061 | -23.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 538 | +0.070 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 52 | +0.130 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 52 | +0.130 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 649 | +0.074 | -22.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 111 | +0.093 | -0.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 538 | +0.070 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 131 | +0.004 | -26.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 131 | +0.004 | -26.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 25872 | +0.098 | -803.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2183 | +0.094 | +32.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 23689 | +0.098 | -835.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 14790 | +0.102 | -239.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2183 | +0.094 | +32.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 12607 | +0.103 | -271.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4461 | +0.115 | +32.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4461 | +0.115 | +32.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6621 | +0.078 | -596.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6621 | +0.078 | -596.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 717 | +0.254 | -94.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 717 | +0.254 | -94.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 717 | +0.254 | -94.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 717 | +0.254 | -94.87€ | 0 | 4 |
| ✅ GBM_LATE_15M | 19216 | +0.074 | +8629.26€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 19216 | +0.074 | +8629.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3143 | +0.196 | +2309.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3143 | +0.196 | +2309.51€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 2821 | +0.175 | +1910.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2821 | +0.175 | +1910.41€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 3282 | +0.194 | +2382.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3282 | +0.194 | +2382.92€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 2885 | +0.003 | +431.56€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2885 | +0.003 | +431.56€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 2837 | -0.038 | +621.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2837 | -0.038 | +621.24€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 4248 | -0.051 | +973.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4248 | -0.051 | +973.61€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 20274 | +0.076 | +10055.59€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 20274 | +0.076 | +10055.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3724 | +0.011 | +1942.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3724 | +0.011 | +1942.07€ | 1 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4279 | +0.004 | +793.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4279 | +0.004 | +793.68€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2865 | +0.256 | +2804.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2865 | +0.256 | +2804.63€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3157 | -0.018 | +359.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3157 | -0.018 | +359.56€ | 2 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3378 | +0.013 | +1180.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3378 | +0.013 | +1180.78€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2871 | +0.268 | +2974.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2871 | +0.268 | +2974.87€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 15632 | +0.169 | +11481.25€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 15632 | +0.169 | +11481.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2303 | +0.209 | +1849.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2303 | +0.209 | +1849.08€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2460 | +0.157 | +1788.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2460 | +0.157 | +1788.60€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2411 | +0.204 | +1880.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2411 | +0.204 | +1880.03€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2600 | +0.140 | +1756.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2600 | +0.140 | +1756.13€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2951 | +0.113 | +1922.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2951 | +0.113 | +1922.30€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2907 | +0.202 | +2285.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2907 | +0.202 | +2285.11€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3894 | +0.126 | +1568.43€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3894 | +0.126 | +1568.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 137 | +0.112 | +52.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 137 | +0.112 | +52.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1047 | +0.117 | +412.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1047 | +0.117 | +412.61€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1086 | +0.153 | +505.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1086 | +0.153 | +505.75€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 753 | +0.080 | +196.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 753 | +0.080 | +196.15€ | 1 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 19251 | +0.173 | +13891.25€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 19251 | +0.173 | +13891.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3005 | +0.221 | +2533.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3005 | +0.221 | +2533.84€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3008 | +0.152 | +1978.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3008 | +0.152 | +1978.32€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3110 | +0.220 | +2609.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3110 | +0.220 | +2609.77€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3068 | +0.136 | +1987.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3068 | +0.136 | +1987.00€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3394 | +0.106 | +1933.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3394 | +0.106 | +1933.78€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3666 | +0.202 | +2848.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3666 | +0.202 | +2848.54€ | 0 | 25 |
| ✅ GBM_LATE_5M | 5931 | +0.142 | +3240.27€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5931 | +0.142 | +3240.27€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1557 | +0.140 | +953.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1557 | +0.140 | +953.16€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1806 | +0.147 | +993.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1806 | +0.147 | +993.47€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 312 | +0.041 | +47.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 312 | +0.041 | +47.97€ | 2 | 6 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1226 | +0.065 | +471.10€ | 3 | 18 |
| ✅ GBM_LATE_60M#60min | 1226 | +0.065 | +471.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 433 | +0.088 | +163.42€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 433 | +0.088 | +163.42€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 407 | +0.072 | +194.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 407 | +0.072 | +194.78€ | 2 | 20 |
| ✅ GBM_LATE_60M#SOL | 386 | +0.031 | +112.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 386 | +0.031 | +112.90€ | 3 | 11 |
| 🚫 GBM_LATE_60M_FADE | 291 | -0.271 | -27.91€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 291 | -0.271 | -27.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 108 | -0.227 | -8.73€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 108 | -0.227 | -8.73€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 99 | -0.302 | -15.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 99 | -0.302 | -15.38€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 84 | -0.279 | -3.80€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 84 | -0.279 | -3.80€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 573 | +0.053 | +99.39€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 573 | +0.053 | +99.39€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 221 | +0.038 | +28.33€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 221 | +0.038 | +28.33€ | 4 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 171 | +0.038 | +0.90€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 171 | +0.038 | +0.90€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 181 | +0.085 | +70.16€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 181 | +0.085 | +70.16€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 60 | +0.242 | +35.06€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 60 | +0.242 | +35.06€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 60 | +0.242 | +35.06€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 60 | +0.242 | +35.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1334 | +0.104 | +378.61€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1334 | +0.104 | +378.61€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1334 | +0.104 | +378.61€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1334 | +0.104 | +378.61€ | 0 | 5 |
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
| ✅ LIQUIDACIONES_5M | 1510 | -0.005 | -10.55€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1510 | -0.005 | -10.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 167 | -0.021 | +1.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 167 | -0.021 | +1.08€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 602 | +0.021 | +14.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 602 | +0.021 | +14.85€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 459 | -0.008 | -8.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 459 | -0.008 | -8.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 105 | -0.061 | -6.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 105 | -0.061 | -6.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 888 | -0.046 | -25.69€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 888 | -0.046 | -25.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 262 | -0.053 | -14.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 262 | -0.053 | -14.64€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 281 | -0.037 | -4.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 281 | -0.037 | -4.76€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 345 | -0.048 | -6.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 345 | -0.048 | -6.30€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 12774 | -0.011 | -181.22€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 12774 | -0.011 | -181.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2307 | -0.022 | -48.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2307 | -0.022 | -48.09€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2591 | -0.017 | -23.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2591 | -0.017 | -23.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3058 | -0.018 | -58.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3058 | -0.018 | -58.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 21272 | -0.012 | +956.66€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 21272 | -0.012 | +956.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3679 | +0.010 | +491.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3679 | +0.010 | +491.15€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3458 | -0.025 | -29.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3458 | -0.025 | -29.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3705 | +0.002 | +307.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3705 | +0.002 | +307.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3237 | -0.043 | -67.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3237 | -0.043 | -67.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3559 | -0.016 | +144.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3559 | -0.016 | +144.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3634 | -0.004 | +109.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3634 | -0.004 | +109.88€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4827 | -0.035 | -107.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4827 | -0.035 | -107.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 988 | -0.037 | -21.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 988 | -0.037 | -21.49€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 435 | -0.118 | -16.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 435 | -0.118 | -16.92€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1315 | -0.048 | -21.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1315 | -0.048 | -21.60€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3240 | +0.003 | -6.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3240 | +0.003 | -6.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1217 | +0.005 | +5.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1217 | +0.005 | +5.04€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1387 | +0.007 | -0.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1387 | +0.007 | -0.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 55250 | -0.073 | +1141.81€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 55250 | -0.073 | +1141.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 9264 | -0.082 | +559.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 9264 | -0.082 | +559.02€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 8644 | -0.086 | -272.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 8644 | -0.086 | -272.20€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 9300 | -0.072 | +429.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 9300 | -0.072 | +429.46€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8164 | -0.093 | -223.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8164 | -0.093 | -223.20€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 10263 | -0.047 | +307.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 10263 | -0.047 | +307.04€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 9615 | -0.065 | +341.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 9615 | -0.065 | +341.68€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6686 | -0.021 | -106.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6686 | -0.021 | -106.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1486 | -0.020 | -10.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1486 | -0.020 | -10.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1477 | -0.014 | -7.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1477 | -0.014 | -7.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 988 | -0.035 | -13.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 988 | -0.035 | -13.67€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 961 | +0.112 | +331.27€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 825 | +0.120 | +318.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 187 | +0.135 | +90.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 187 | +0.135 | +90.49€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 162 | +0.098 | +39.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 162 | +0.098 | +39.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 167 | +0.092 | +51.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 167 | +0.092 | +51.40€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#SOL | 149 | +0.156 | +81.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 149 | +0.156 | +81.55€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 160 | +0.117 | +55.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 160 | +0.117 | +55.60€ | 0 | 3 |
| ✅ PRICE_TARGET_GBM | 451 | -0.094 | -15.12€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 200 | -0.134 | -34.68€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 158 | -0.175 | -37.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 161 | -0.083 | +3.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 119 | -0.095 | -3.55€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 90 | -0.022 | +16.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 70 | -0.042 | +10.45€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 347 | -0.122 | -30.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 510 | -0.221 | -40.74€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 215 | -0.205 | -33.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 183 | -0.197 | -30.77€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 180 | -0.242 | -21.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 153 | -0.255 | -25.30€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 115 | -0.209 | +13.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 101 | -0.209 | +10.46€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 437 | -0.222 | -45.60€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 181 | +0.396 | +130.33€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 43 | +0.344 | +36.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 43 | +0.344 | +36.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 115 | +0.483 | +95.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 115 | +0.483 | +95.85€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#sniper | 181 | +0.396 | +130.33€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 378 | +0.032 | +10.73€ | 3 | 1 |
| ✅ STREAK_FADE_15M#15min | 378 | +0.032 | +10.73€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 167 | +0.033 | +2.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 167 | +0.033 | +2.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 42 | -0.023 | -4.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 42 | -0.023 | -4.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 144 | +0.034 | +9.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 144 | +0.034 | +9.50€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 2382 | -0.024 | -104.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2382 | -0.024 | -104.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 562 | -0.023 | -23.39€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 562 | -0.023 | -23.39€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 151 | -0.043 | -13.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 151 | -0.043 | -13.92€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 865 | -0.027 | -40.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 865 | -0.027 | -40.57€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 57 | -0.042 | -3.50€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 57 | -0.042 | -3.50€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 22 | +0.042 | +0.45€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 22 | +0.042 | +0.45€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6272 | +0.023 | +95.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6272 | +0.023 | +95.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2008 | +0.021 | +20.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2008 | +0.021 | +20.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1306 | +0.033 | +37.70€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1306 | +0.033 | +37.70€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1838 | +0.015 | +7.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1838 | +0.015 | +7.47€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1120 | +0.029 | +29.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1120 | +0.029 | +29.72€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5844 | +0.013 | -31.02€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5844 | +0.013 | -31.02€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2310 | +0.020 | +2.22€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2310 | +0.020 | +2.22€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2321 | +0.014 | -8.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2321 | +0.014 | -8.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1213 | -0.005 | -24.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1213 | -0.005 | -24.99€ | 2 | 0 |
| ✅ UPDOWN_GBM | 24562 | +0.029 | +1342.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 6569 | +0.057 | +1032.65€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 916 | +0.004 | +8.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 15527 | +0.023 | +307.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1452 | -0.005 | -10.90€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2138 | +0.071 | +206.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 273 | +0.122 | +84.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1846 | +0.065 | +121.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4373 | +0.030 | +283.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 781 | +0.081 | +182.50€ | 0 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 261 | +0.025 | +7.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2650 | +0.025 | +90.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 644 | +0.000 | +1.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 37 | -0.115 | +1.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2931 | +0.033 | +94.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 229 | +0.106 | +55.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2686 | +0.026 | +40.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 4941 | +0.016 | +194.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1804 | +0.043 | +188.30€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 248 | +0.008 | +8.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2335 | +0.004 | +1.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 522 | -0.009 | -7.86€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 32 | -0.147 | +4.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6444 | +0.016 | +151.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1768 | +0.023 | +102.09€ | 1 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 242 | -0.008 | -2.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4121 | +0.018 | +56.77€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 286 | -0.007 | -4.77€ | 1 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 27 | -0.155 | -0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3733 | +0.040 | +413.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1714 | +0.079 | +420.03€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 130 | -0.015 | -3.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1889 | +0.009 | -3.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 96 | -0.143 | +5.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 399 | +0.330 | +104.56€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 399 | +0.330 | +104.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 224 | +0.332 | +53.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 224 | +0.332 | +53.82€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 175 | +0.325 | +50.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 175 | +0.325 | +50.74€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 8810 | -0.049 | +1837.46€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 8810 | -0.049 | +1837.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 403 | -0.053 | +344.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 403 | -0.053 | +344.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1681 | -0.129 | -7.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1681 | -0.129 | -7.84€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 948 | +0.188 | +526.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 948 | +0.188 | +526.20€ | 2 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2834 | -0.061 | +448.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2834 | -0.061 | +448.59€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2805 | -0.076 | +471.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2805 | -0.076 | +471.19€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 97 | +0.056 | +8.36€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 97 | +0.056 | +8.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 97 | +0.056 | +8.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 97 | +0.056 | +8.36€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 682 | +0.282 | +542.92€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 682 | +0.282 | +542.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 380 | +0.275 | +287.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 380 | +0.275 | +287.60€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 302 | +0.289 | +255.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 302 | +0.289 | +255.32€ | 0 | 13 |
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
  - _Estado_: 446 celda(s) pasan gate riguroso completo de 2034 evaluadas (n>=40) y 2991 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.023 < 0.08 — monitorear
  - _Datos_: n=1767 IC=+0.023 PNL=+101.59€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.096 n=176/60 | contraria IC=+0.114 n=156 | gap=-0.018 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=234, boost estimado=+0.005. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=522/40 IC=-0.009 PNL=-7.86€ | BTC#60min: n=644/40 IC=+0.000 PNL=+1.74€ | SOL#60min: n=286/40 IC=-0.007 PNL=-4.77€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.053 n=254130 | tras_1loss IC=+0.071 n=198856 | tras_2loss IC=+0.038 n=85343/40 | gap=+0.015 (umbral 0.05)

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
  - _Estado_: n=1068 IC=-0.006 PNL=-17.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1068 IC=-0.006 PNL=-17.85€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=384 IC=+0.000 PNL=+6.96€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=384 IC=+0.000 PNL=+6.96€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.168 > 0.1 con n=1394 PNL=+768.49€
  - _Datos_: n=1394 IC=+0.168 PNL=+768.49€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=778 IC=+0.082 PNL=+180.37€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=778 IC=+0.082 PNL=+180.37€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.238 n=59) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=59 IC=+0.238 PNL=+33.06€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=551 PNL=+220.01€
  - _Datos_: n=551 IC=+0.128 PNL=+220.01€

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
  - _Estado_: n=7893 IC=+0.049 PNL=+882.80€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=7893 IC=+0.049 PNL=+882.80€

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
  - _Estado_: n=1314 IC=+0.050 PNL=+162.07€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1314 IC=+0.050 PNL=+162.07€

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
  - _Estado_: n=13174 IC=-0.142 PNL=+664.06€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13174 IC=-0.142 PNL=+664.06€

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
  - _Estado_: n=1462 IC=+0.141 PNL=+793.83€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1462 IC=+0.141 PNL=+793.83€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.240 < -0.1 con n=1342 PNL=-192.48€
  - _Datos_: n=1342 IC=-0.240 PNL=-192.48€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=704) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=704 IC=+0.096 PNL=+178.65€

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
  - _Estado_: n=6875 IC=+0.168 PNL=-886.19€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6875 IC=+0.168 PNL=-886.19€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.1 con n=99 PNL=+62.52€
  - _Datos_: n=99 IC=+0.213 PNL=+62.52€
