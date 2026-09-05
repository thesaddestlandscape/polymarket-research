# Hipótesis automáticas — 2026-09-05 13:30 UTC
_Generado por shadow_postmortem.py sobre 296014 resoluciones (PNL=+28989.37€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.150 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.268 (n=325)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.392 (n=81)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=315)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.268 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.141)

- **PATRÓN** `n_ballena_banda` > `19.0` → IC=+0.145 (n=322)

  - _Acción_: Kelly boost +0.73€ cuando `n_ballena_banda` > 19.0 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.245 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.141)

- **PATRÓN** `banda_hit_calibrado` > `0.6176` → IC=+0.239 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6176 (IC base=+0.141)

- **PATRÓN** `banda_z` > `11.557` → IC=+0.273 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.557 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.169 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=364)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3120.8362` → IC=+0.183 (n=159)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3120.8362 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.134 (n=315)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.025)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.159 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.273 (n=253)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=185)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=210)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.273 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.166)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.241 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.166)

- **PATRÓN** `banda_hit_calibrado` > `0.6206` → IC=+0.268 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6206 (IC base=+0.166)

- **PATRÓN** `banda_z` > `11.557` → IC=+0.271 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.557 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.200 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=284)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2988.1169` → IC=+0.182 (n=168)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2988.1169 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=185)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.015)

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

- **FILTRO** `n_ballena_banda` < `30.0` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `n_ballena_banda` < 30.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=52)

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
- **FILTRO** `restante_s_al_confirmar` < `147.36` → IC=-0.300 (n=3963)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.36
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=11896)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.44` → IC=-0.330 (n=533)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.44
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1601)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `627.34` → IC=-0.153 (n=335)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 627.34
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=652)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.78` → IC=-0.403 (n=523)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.78
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=1569)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `145.69` → IC=-0.312 (n=882)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.69
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=2648)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `159.6` → IC=-0.376 (n=957)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 159.6
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=1943)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.191 (n=8328)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.7 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=2132)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2365.062` → IC=+0.164 (n=2046)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2365.062 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.148 (n=5856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.150 (n=7084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.253 (n=5264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.180 (n=4088)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4551.444` → IC=+0.179 (n=1775)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 4551.444 (IC base=+0.139)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=936)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.375 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `13044.1569` → IC=+0.224 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13044.1569 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=874)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=971)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.288 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=1238)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `12459.7568` → IC=+0.207 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12459.7568 (IC base=+0.192)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.595` → IC=+0.161 (n=302)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.595 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `4800.0243` → IC=+0.151 (n=216)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4800.0243 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.190 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.180 (n=345)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.41 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4096.0208` → IC=+0.154 (n=328)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4096.0208 (IC base=+0.131)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=102)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=1464)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.311 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.263 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.254)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.255 (n=733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.254)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.395 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.259 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1930.2375` → IC=+0.268 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.2375 (IC base=+0.254)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.66` → IC=+0.261 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.66 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=480)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1493.0973` → IC=+0.153 (n=399)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1493.0973 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.216 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.426 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=841)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.23` → IC=+0.348 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.23 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `939.0669` → IC=+0.198 (n=822)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 939.0669 (IC base=+0.196)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.207 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.332 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=172)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3436.2112` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3436.2112 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.225 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=297)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **FILTRO** `libro_liquidez` < `11360.7096` → IC=-0.266 (n=143)

  - _Acción_: SKIP cuando `libro_liquidez` < 11360.7096
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=6515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.198 (n=5552)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.205 (n=3124)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `5756.5432` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5756.5432 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=1604)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=1674)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.340 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.291)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=1567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=1399)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.175 (n=1678)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.187 (n=1116)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.72 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=1259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.315 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.236)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=1596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=1368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.193 (n=826)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.7 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.188 (n=688)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.451 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.443 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.939` → IC=+0.481 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.939 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.442 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `3434.6605` → IC=+0.453 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3434.6605 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.444)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.444)

- **PATRÓN** `libro_liquidez` > `10987.7492` → IC=+0.463 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10987.7492 (IC base=+0.444)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.449 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `2360.5304` → IC=+0.445 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2360.5304 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.426 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.462 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` < `0.932` → IC=+0.423 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.932 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `libro_liquidez` < `6196.1698` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 6196.1698
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=18323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.211 (n=18699)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=3818)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.156 (n=3269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.184 (n=2781)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.72 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=1191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.228 (n=1212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.273 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.226)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.167 (n=2532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 12.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=3249)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.166)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=1621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.227 (n=1231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=1283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.241 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=1318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=2472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.236 (n=1312)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.205 (n=2658)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.130)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.140 (n=2484)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 4.01 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.159 (n=2491)

  - _Acción_: Kelly boost +0.79€ cuando `restante_min` > 4.94 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.145 (n=3272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `3.85` → IC=+0.158 (n=2479)

  - _Acción_: Kelly boost +0.79€ cuando `lag_apertura_s` < 3.85 (IC base=+0.130)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.211 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.136)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.147 (n=1227)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` < 3.95 (IC base=+0.136)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.151 (n=1710)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.88 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.153 (n=2643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 12.0 (IC base=+0.136)

- **PATRÓN** `lag_apertura_s` < `6.89` → IC=+0.149 (n=1620)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 6.89 (IC base=+0.136)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.199 (n=1329)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.123)

- **PATRÓN** `restante_min` < `4.44` → IC=+0.129 (n=1652)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.44 (IC base=+0.123)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.168 (n=1261)

  - _Acción_: Kelly boost +0.84€ cuando `restante_min` > 4.95 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.126 (n=1420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=1666)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `lag_apertura_s` < `3.29` → IC=+0.169 (n=1256)

  - _Acción_: Kelly boost +0.84€ cuando `lag_apertura_s` < 3.29 (IC base=+0.123)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.378 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1738.7704` → IC=+0.295 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1738.7704 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.294 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.278 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `5497.3627` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5497.3627 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.337 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=367)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.373 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.293 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1720.692` → IC=+0.320 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1720.692 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.331 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.325)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.353 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.325)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.370 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.325)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.346 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.325)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.364 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.325)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.421)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.426 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.421)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.427 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.421)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.433 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.421)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.423 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.421)

- **PATRÓN** `libro_liquidez` > `1978.9685` → IC=+0.434 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.9685 (IC base=+0.421)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.418)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.424 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.418)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.428 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.418)

- **PATRÓN** `libro_liquidez` > `5433.9622` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5433.9622 (IC base=+0.418)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.435 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.428 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.428 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `1957.89` → IC=+0.451 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.89 (IC base=+0.425)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.372)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.372)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.316 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.413 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.276 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1391.4835` → IC=+0.284 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1391.4835 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.316 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.413 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.276 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1391.4835` → IC=+0.284 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1391.4835 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9518` → IC=+0.212 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9518 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.4564` → IC=+0.226 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4564 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.689` → IC=+0.157 (n=1516)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.689 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.229 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `1.0799` → IC=+0.245 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0799 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.1712` → IC=+0.191 (n=698)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1712 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `2.8651` → IC=+0.182 (n=2409)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.8651 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.4728` → IC=+0.180 (n=2409)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4728 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.403` → IC=+0.126 (n=3779)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.403 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.3294` → IC=+0.143 (n=1422)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.3294 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.6881` → IC=+0.145 (n=601)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6881 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.0483` → IC=+0.144 (n=619)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0483 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.3031` → IC=+0.234 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3031 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.6099` → IC=+0.190 (n=1886)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.6099 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.217 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.040)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.197 (n=298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0076 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.2919` → IC=+0.164 (n=889)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2919 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.201 (n=430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.738` → IC=+0.298 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.738 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.240 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `2.6489` → IC=+0.149 (n=792)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.6489 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.152 (n=792)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=744)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.194 (n=364)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 43.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.252 (n=405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.260 (n=543)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.289 (n=405)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.250 (n=550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.251 (n=617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.4091` → IC=+0.276 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4091 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.382` → IC=+0.263 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.382 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.0697` → IC=+0.243 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0697 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.336 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.5816` → IC=+0.269 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5816 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.265 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1719.82` → IC=+0.262 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1719.82 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.257 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.245)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.250 (n=230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.218 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.2082` → IC=+0.234 (n=460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2082 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.929` → IC=+0.240 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.929 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.8352` → IC=+0.220 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8352 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.4658` → IC=+0.216 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4658 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.225` → IC=+0.226 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.225 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.098` → IC=+0.213 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.098 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2495` → IC=+0.218 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2495 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.0825` → IC=+0.230 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0825 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.216 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4772` → IC=+0.242 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4772 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `11871.8913` → IC=+0.243 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11871.8913 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.153 (n=753)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0061 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.148 (n=671)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0029 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0782` → IC=+0.161 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0782 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.148 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.146 (n=535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 12.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6604` → IC=+0.171 (n=751)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6604 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.169 (n=642)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.496` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.496 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.615` → IC=+0.172 (n=251)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.615 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.0647` → IC=+0.212 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0647 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.725` → IC=+0.166 (n=429)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.725 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.4033` → IC=+0.162 (n=642)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4033 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `12582.7558` → IC=+0.153 (n=500)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 12582.7558 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.177 (n=187)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 211.0 (IC base=+0.145)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.202 (n=280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.201 (n=413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.248 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.364` → IC=+0.275 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.364 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` < `0.1042` → IC=+0.165 (n=690)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.1042 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `3.8523` → IC=+0.162 (n=755)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 3.8523 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `1.8939` → IC=+0.181 (n=676)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8939 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.193 (n=886)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.200 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.230 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.229 (n=617)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.4928` → IC=+0.227 (n=691)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4928 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=325)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.0312` → IC=+0.277 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0312 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.949` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.949 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.3749` → IC=+0.300 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3749 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.6995` → IC=+0.223 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6995 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.4265` → IC=+0.213 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4265 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.235 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.211 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.226)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.8186` → IC=-0.183 (n=304)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8186
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=918)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=72)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1150)

- **PATRÓN** `dist_vwap_pct` < `0.2033` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2033 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` < `0.6119` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6119 (IC base=-0.028)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1929 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.6117` → IC=+0.305 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6117 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.9125` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9125 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 177.0 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1427` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1427 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.278 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` > `1.573` → IC=+0.129 (n=203)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.573 (IC base=-0.039)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=150)

- **FILTRO** `ibs_20min` < `0.28` → IC=-0.172 (n=62)

  - _Acción_: SKIP cuando `ibs_20min` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=128)

- **FILTRO** `sigma_ewma_delta_pct` > `8.368` → IC=-0.193 (n=210)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.368
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=1632)

- **FILTRO** `volumen_pendiente_norm` < `0.1097` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1097
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=27)

- **FILTRO** `volumen_spike_ratio` > `1.4181` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4181
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=16)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.180 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=+0.047)

- **PATRÓN** `ibs_20min` > `0.28` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.28 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.6372` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6372 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.7744` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7744 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.6091` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6091 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `2.1624` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1624 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.4181` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4181 (IC base=-0.062)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5078` → IC=-0.161 (n=375)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5078
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=730)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.192 (n=144)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=961)

- **FILTRO** `ibs_20min` > `0.79` → IC=-0.198 (n=439)

  - _Acción_: SKIP cuando `ibs_20min` > 0.79
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=1323)

- **FILTRO** `sigma_ewma_delta_pct` > `8.957` → IC=-0.134 (n=200)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.957
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1562)

- **PATRÓN** `dist_vwap_pct` > `0.6657` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6657 (IC base=-0.095)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.095)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.273 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.066` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.066 (IC base=-0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.4974` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4974 (IC base=-0.095)

- **PATRÓN** `volumen_spike_ratio` > `2.442` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.442 (IC base=-0.095)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.204 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2288 (IC base=-0.050)

- **PATRÓN** `volumen_regimen` > `1.2934` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2934 (IC base=-0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2594` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2594 (IC base=-0.050)

- **PATRÓN** `volumen_spike_ratio` < `2.3188` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.3188 (IC base=-0.050)

- **PATRÓN** `volumen_spike_ratio` > `1.5058` → IC=+0.155 (n=146)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5058 (IC base=-0.050)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 21.0 (IC base=-0.050)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.173 (n=1639)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0093 (IC base=+0.078)

- **PATRÓN** `ibs_20min` > `0.3043` → IC=+0.148 (n=4900)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.3043 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `1.1973` → IC=+0.298 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1973 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.486` → IC=+0.124 (n=2594)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.486 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `0.6821` → IC=+0.223 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6821 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.251` → IC=+0.252 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.251 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `1.4861` → IC=+0.232 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4861 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `2.8017` → IC=+0.221 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8017 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.294 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.5857` → IC=+0.128 (n=4705)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5857 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.7545` → IC=+0.249 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7545 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.219` → IC=+0.219 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.219 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.7096` → IC=+0.219 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7096 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.241 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2586` → IC=+0.337 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2586 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.4177` → IC=+0.258 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4177 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.257 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.050)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3158` → IC=-0.143 (n=410)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3158
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=837)

- **FILTRO** `sigma_ewma_delta_pct` > `2.454` → IC=-0.163 (n=366)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.454
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=793)

- **PATRÓN** `ibs_20min` > `0.8418` → IC=+0.248 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8418 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.685` → IC=+0.172 (n=230)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.685 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.8775` → IC=+0.244 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8775 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `1.4729` → IC=+0.237 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4729 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.035)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8595` → IC=-0.161 (n=405)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8595
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1217)

- **PATRÓN** `volumen_spike_ratio` < `2.0473` → IC=+0.123 (n=322)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.0473 (IC base=-0.011)

- **PATRÓN** `ballena_activa_n` < `261.0` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 261.0 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1433` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1433 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` < `0.8251` → IC=+0.172 (n=135)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8251 (IC base=-0.022)

- **PATRÓN** `volumen_regimen` > `1.1132` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1132 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2573` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2573 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.7377` → IC=+0.222 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7377 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.4035` → IC=+0.181 (n=158)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4035 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 263.0 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.274 (n=528)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.0852` → IC=+0.233 (n=264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0852 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.254 (n=384)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.7101` → IC=+0.259 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7101 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.371` → IC=+0.296 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.371 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` < `0.1093` → IC=+0.237 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1093 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `2.4282` → IC=+0.230 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4282 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.7205` → IC=+0.235 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7205 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.330 (n=380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.314 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.3563` → IC=+0.308 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3563 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.709` → IC=+0.319 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.709 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `3.4644` → IC=+0.283 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.4644 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.3705` → IC=+0.301 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3705 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.300 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1846.3` → IC=+0.297 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1846.3 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.277 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.293)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.143 (n=250)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=549)

- **FILTRO** `ibs_20min` < `0.5712` → IC=-0.168 (n=399)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5712
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=400)

- **FILTRO** `ibs_20min` > `0.7357` → IC=-0.143 (n=430)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7357
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=837)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `volumen_regimen` < `0.6828` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6828
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.135 (n=83)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1184)

- **PATRÓN** `dist_vwap_pct` > `1.4893` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.4893 (IC base=-0.053)

- **PATRÓN** `volumen_regimen` < `0.8742` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8742 (IC base=-0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.1716` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1716 (IC base=-0.053)

- **PATRÓN** `volumen_spike_ratio` < `2.0972` → IC=+0.234 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0972 (IC base=-0.053)

- **PATRÓN** `volumen_spike_ratio` > `1.3689` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3689 (IC base=-0.053)

- **PATRÓN** `ballena_activa_n` < `187.0` → IC=+0.257 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 187.0 (IC base=-0.053)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.8333` → IC=-0.133 (n=703)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8333
  - _Potencial_: sin este filtro IC_bueno=+0.297 (n=363)

- **FILTRO** `ibs_20min` > `0.7551` → IC=-0.236 (n=301)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7551
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=904)

- **FILTRO** `sigma_ewma_delta_pct` > `4.657` → IC=-0.150 (n=301)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.657
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=904)

- **PATRÓN** `ibs_20min` > `0.8333` → IC=+0.297 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8333 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.2083` → IC=+0.304 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2083 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.8667` → IC=+0.263 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8667 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `1.1564` → IC=+0.283 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1564 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.1127` → IC=+0.263 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1127 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2247` → IC=+0.281 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2247 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.313 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `1.2143` → IC=+0.129 (n=130)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2143 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` > `1.9868` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.9868 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 65.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.338 (n=515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0134 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.265 (n=680)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` > `0.9` → IC=+0.329 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9 (IC base=+0.256)

- **PATRÓN** `dist_vwap_pct` > `0.167` → IC=+0.314 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.167 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.191` → IC=+0.292 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.191 (IC base=+0.256)

- **PATRÓN** `volumen_regimen` > `0.8467` → IC=+0.295 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8467 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.300 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `2.5706` → IC=+0.263 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5706 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `1.8318` → IC=+0.263 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8318 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.259 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `2464.8845` → IC=+0.261 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.8845 (IC base=+0.256)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.280 (n=280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.271)

- **PATRÓN** `sigma_h` > `0.024` → IC=+0.297 (n=279)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.024 (IC base=+0.271)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.278 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.271)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.308 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` > `0.5192` → IC=+0.283 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5192 (IC base=+0.271)

- **PATRÓN** `dist_vwap_pct` < `0.2753` → IC=+0.274 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2753 (IC base=+0.271)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.354` → IC=+0.297 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.354 (IC base=+0.271)

- **PATRÓN** `volumen_regimen` > `1.2604` → IC=+0.304 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2604 (IC base=+0.271)

- **PATRÓN** `volumen_pendiente_norm` > `0.2435` → IC=+0.373 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2435 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` < `2.5859` → IC=+0.259 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5859 (IC base=+0.271)

- **PATRÓN** `volumen_spike_ratio` > `2.1963` → IC=+0.281 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1963 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `2546.9804` → IC=+0.271 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2546.9804 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.265 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.271)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.210 (n=1375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3383` → IC=+0.171 (n=3625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3383 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=4122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.7034` → IC=+0.224 (n=3680)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7034 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.78` → IC=+0.235 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.78 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.121` → IC=+0.253 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.121 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.6316` → IC=+0.162 (n=2776)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6316 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1055` → IC=+0.189 (n=1561)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1055 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.318` → IC=+0.166 (n=3388)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.318 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=3037)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3902.0492` → IC=+0.173 (n=1373)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3902.0492 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.183 (n=3027)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 140.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.180 (n=3377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0083 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.203 (n=1280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=1810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4412` → IC=+0.222 (n=3836)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4412 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.165 (n=2902)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.075` → IC=+0.205 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.075 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.161 (n=2884)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1729 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.154 (n=2884)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6237 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2945` → IC=+0.242 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2945 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5742` → IC=+0.162 (n=1411)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5742 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6579` → IC=+0.192 (n=1069)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6579 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.166 (n=2798)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 155.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.185 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0057 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.216 (n=319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3017` → IC=+0.205 (n=694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3017 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.222 (n=469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.576` → IC=+0.300 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.576 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.267 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.6369` → IC=+0.172 (n=611)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.6369 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4557` → IC=+0.175 (n=611)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4557 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.199 (n=287)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 45.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.260 (n=390)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1666` → IC=+0.303 (n=292)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1666 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.250 (n=442)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.2712` → IC=+0.257 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2712 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.702` → IC=+0.247 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.702 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0683` → IC=+0.227 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0683 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.9129` → IC=+0.222 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9129 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.7651` → IC=+0.252 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7651 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.260 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1704.94` → IC=+0.265 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1704.94 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.228 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.233)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.222 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.4033` → IC=+0.165 (n=607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4033 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.211 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.4793` → IC=+0.206 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4793 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2665` → IC=+0.224 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2665 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.787` → IC=+0.241 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.787 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2719` → IC=+0.167 (n=607)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2719 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.172 (n=275)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.0731 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2304` → IC=+0.195 (n=126)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2304 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.3938` → IC=+0.203 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3938 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `11275.7432` → IC=+0.186 (n=542)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 11275.7432 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.178 (n=699)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0061 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.211 (n=233)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.176 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.4957` → IC=+0.190 (n=699)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.4957 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.3176` → IC=+0.169 (n=751)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.3176 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.232` → IC=+0.241 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.232 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.223 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6986 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.213 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.7274` → IC=+0.162 (n=394)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.7274 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.3973` → IC=+0.163 (n=591)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.3973 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=902)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `14477.4015` → IC=+0.158 (n=317)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 14477.4015 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `241.0` → IC=+0.159 (n=168)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 241.0 (IC base=+0.155)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.212 (n=217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1779` → IC=+0.197 (n=434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1779 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.437` → IC=+0.295 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.437 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1322` → IC=+0.194 (n=246)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1322 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `3.1555` → IC=+0.170 (n=516)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 3.1555 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `3.8668` → IC=+0.177 (n=196)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 3.8668 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.196 (n=133)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 18.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.234 (n=516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.220 (n=344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.211` → IC=+0.228 (n=344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.211 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.374` → IC=+0.255 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.374 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.257 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3693` → IC=+0.279 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3693 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.9277` → IC=+0.204 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9277 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `3.101` → IC=+0.223 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.101 (IC base=+0.220)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.187 (n=544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0071 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1199` → IC=+0.179 (n=272)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1199 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.175 (n=628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.4315` → IC=+0.200 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4315 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.9673` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9673 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.408` → IC=+0.273 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.408 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.8882` → IC=+0.160 (n=413)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8882 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.2168` → IC=+0.188 (n=206)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.2168 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2963` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2963 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4303` → IC=+0.150 (n=201)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4303 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.6221` → IC=+0.185 (n=201)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6221 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=689)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `8738.117` → IC=+0.191 (n=412)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 8738.117 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.146 (n=371)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 135.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.150 (n=684)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0076 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3779` → IC=+0.143 (n=684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3779 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.5432` → IC=+0.176 (n=684)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.5432 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.5927` → IC=+0.139 (n=802)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.5927 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.339` → IC=+0.213 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.339 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.1618` → IC=+0.134 (n=684)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.1618 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6135` → IC=+0.131 (n=684)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6135 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.170 (n=231)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.143 (n=253)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `11649.2275` → IC=+0.143 (n=228)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 11649.2275 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.182 (n=353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0103 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.5294` → IC=+0.194 (n=778)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5294 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1246` → IC=+0.254 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1246 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.280 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `0.6317` → IC=+0.124 (n=778)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6317 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1695` → IC=+0.133 (n=778)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1695 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.144 (n=248)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=587)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3182.8788` → IC=+0.206 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3182.8788 (IC base=+0.115)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.155 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0106 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.097` → IC=+0.147 (n=236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.097 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.169 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 14.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.4722` → IC=+0.215 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4722 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0295` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 1.0295 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1758` → IC=+0.136 (n=641)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1758 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.292` → IC=+0.150 (n=284)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.292 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.18` → IC=+0.138 (n=707)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.18 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.8584` → IC=+0.130 (n=471)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.8584 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5492` → IC=+0.130 (n=252)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5492 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.3851` → IC=+0.184 (n=191)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.3851 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3176.6468` → IC=+0.160 (n=236)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3176.6468 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.220 (n=516)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.1669` → IC=+0.220 (n=341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1669 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=697)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.8846` → IC=+0.274 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8846 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.2588` → IC=+0.232 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2588 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.172` → IC=+0.242 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.172 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `0.8431` → IC=+0.224 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8431 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.0826` → IC=+0.252 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0826 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `2.5479` → IC=+0.213 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5479 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.196 (n=869)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.258 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.220 (n=266)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.208 (n=837)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.4224` → IC=+0.246 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4224 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.2497` → IC=+0.207 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2497 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.959` → IC=+0.245 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.959 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.6917` → IC=+0.225 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6917 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.319 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.6635` → IC=+0.205 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6635 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2511.4806` → IC=+0.207 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2511.4806 (IC base=+0.200)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.172 (n=403)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0079 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0943` → IC=+0.145 (n=297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.0943 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.169 (n=839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.169 (n=888)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.4444 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.9607` → IC=+0.221 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9607 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.607` → IC=+0.176 (n=409)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.607 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8672` → IC=+0.162 (n=477)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8672 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `1.168` → IC=+0.147 (n=239)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.168 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1702` → IC=+0.181 (n=246)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1702 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.2592` → IC=+0.149 (n=734)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.2592 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.8202` → IC=+0.147 (n=556)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8202 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=927)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `9470.7528` → IC=+0.185 (n=296)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 9470.7528 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.3103` → IC=+0.124 (n=604)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.3103 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.081` → IC=+0.131 (n=185)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 8.081 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.1733` → IC=+0.158 (n=226)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1733 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.150 (n=332)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 22.0 (IC base=+0.076)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.126 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` > 0.0034 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.175 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 10.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6078 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.9294` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9294 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.537` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 3.537 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `0.5749` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.5749 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.3468` → IC=+0.146 (n=142)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.3468 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `11253.359` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 11253.359 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 150.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.164 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0029 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.6298` → IC=+0.153 (n=266)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.6298 (IC base=+0.082)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.093` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.093 (IC base=+0.082)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.220 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.167 (n=91)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 146.0 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.276 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.261)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.327 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.261)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.268 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.296 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` > `0.388` → IC=+0.282 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.388 (IC base=+0.261)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.286 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.261)

- **PATRÓN** `dist_vwap_pct` < `0.226` → IC=+0.261 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.226 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.169` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.169 (IC base=+0.261)

- **PATRÓN** `volumen_regimen` < `0.8258` → IC=+0.276 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8258 (IC base=+0.261)

- **PATRÓN** `volumen_regimen` > `1.1544` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1544 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` < `1.3667` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3667 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `2.0363` → IC=+0.333 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0363 (IC base=+0.261)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5789` → IC=-0.182 (n=61)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5789
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=185)

- **FILTRO** `ibs_20min` > `0.4146` → IC=-0.214 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4146
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.2281` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2281
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=139)

- **FILTRO** `volumen_pendiente_norm` > `0.2176` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2176
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=121)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.170 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 14.0 (IC base=+0.028)

- **PATRÓN** `ibs_20min` > `0.8462` → IC=+0.175 (n=124)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8462 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 20.0 (IC base=-0.031)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0226` → IC=+0.146 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0226 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.31` → IC=+0.161 (n=125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.31 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.136 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.162 (n=143)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.4 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.2912` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2912 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.6865` → IC=+0.142 (n=174)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.6865 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.9833` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.9833 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.6571` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6571 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` < `0.2154` → IC=+0.156 (n=123)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.2154 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.899` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.899 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4996` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4996 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.213 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.141 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 10.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.0588` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.0588 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.5 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.9736` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9736 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.507` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.507 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6197` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6197 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.5677` → IC=+0.138 (n=136)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5677 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2567.2585` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2567.2585 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 16.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.201 (n=2267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=5250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.4868` → IC=+0.211 (n=4989)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4868 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `1.0541` → IC=+0.223 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0541 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.46` → IC=+0.228 (n=2504)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.46 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8867` → IC=+0.161 (n=2293)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8867 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.1681` → IC=+0.199 (n=1371)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1681 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8767` → IC=+0.172 (n=3107)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8767 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.166 (n=4685)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3822.0558` → IC=+0.182 (n=1663)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3822.0558 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.211 (n=2414)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.192 (n=4570)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0108 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.4769` → IC=+0.190 (n=4571)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.4769 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=2181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.193 (n=2083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.236 (n=4571)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.4325` → IC=+0.166 (n=3239)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.4325 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.706` → IC=+0.211 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.706 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.707` → IC=+0.185 (n=4259)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.707 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6228` → IC=+0.165 (n=1080)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6228 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `1.1953` → IC=+0.161 (n=1077)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.1953 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2371` → IC=+0.242 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2371 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.305` → IC=+0.196 (n=1749)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.305 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `141.0` → IC=+0.175 (n=3444)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 141.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.197 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0052 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.246 (n=376)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.217 (n=559)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.869` → IC=+0.313 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.869 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.283 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.5829` → IC=+0.198 (n=326)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5829 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.8823` → IC=+0.177 (n=494)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.8823 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.242 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.271 (n=543)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.266 (n=614)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.1899` → IC=+0.296 (n=410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1899 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=555)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.266 (n=627)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.4142` → IC=+0.297 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4142 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.535` → IC=+0.275 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.535 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.5076` → IC=+0.274 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5076 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1730.44` → IC=+0.271 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1730.44 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.259 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.176 (n=273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0029 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.156 (n=271)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0067 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.4595` → IC=+0.207 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4595 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.2199` → IC=+0.211 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2199 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.774` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.774 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.374` → IC=+0.163 (n=711)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 4.374 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.261` → IC=+0.164 (n=813)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.261 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.0941` → IC=+0.158 (n=369)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.0941 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0705` → IC=+0.165 (n=690)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.0705 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1464` → IC=+0.197 (n=219)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1464 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.3899` → IC=+0.171 (n=763)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.3899 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.721` → IC=+0.178 (n=510)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.721 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `10659.1786` → IC=+0.181 (n=726)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 10659.1786 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `470.0` → IC=+0.173 (n=610)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 470.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.177 (n=735)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0062 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.171 (n=658)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0029 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3435` → IC=+0.180 (n=735)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3435 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.171 (n=766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.6191` → IC=+0.208 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6191 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.1406` → IC=+0.186 (n=641)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1406 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.77` → IC=+0.222 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.77 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.225 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.618 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1436` → IC=+0.235 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1436 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.202 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.0527` → IC=+0.191 (n=289)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.0527 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=948)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `289.0` → IC=+0.187 (n=180)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 289.0 (IC base=+0.168)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.224 (n=730)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.246 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.258 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6818 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.358` → IC=+0.318 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.358 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.2205` → IC=+0.212 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2205 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `3.2093` → IC=+0.207 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.2093 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.4526` → IC=+0.208 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4526 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1467.8784` → IC=+0.212 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1467.8784 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.257 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.259 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.249 (n=329)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.238 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.257 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.276 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.51` → IC=+0.267 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.51 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `3.0645` → IC=+0.231 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0645 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.3399` → IC=+0.222 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3399 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.211 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.233)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.157 (n=730)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0069 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.2304` → IC=+0.143 (n=552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2304 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.157 (n=739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.7317` → IC=+0.238 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7317 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3624` → IC=+0.187 (n=321)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.3624 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.313` → IC=+0.173 (n=371)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.313 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8962` → IC=+0.170 (n=552)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8962 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.1991` → IC=+0.140 (n=276)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.1991 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.233 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.5054` → IC=+0.191 (n=263)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5054 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=902)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.240 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.142 (n=574)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0071 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.144 (n=652)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.162 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6809` → IC=+0.173 (n=652)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6809 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.3875` → IC=+0.126 (n=659)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.3875 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.258` → IC=+0.209 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.258 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8324` → IC=+0.125 (n=435)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.8324 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `1.1414` → IC=+0.145 (n=218)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1414 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4526` → IC=+0.142 (n=590)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4526 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `9534.8435` → IC=+0.174 (n=296)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 9534.8435 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `191.0` → IC=+0.138 (n=506)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 191.0 (IC base=+0.125)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.122 (n=873)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0053 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.180 (n=874)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4706 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.866` → IC=+0.182 (n=218)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.866 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.352` → IC=+0.222 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.352 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=603)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2951.497` → IC=+0.254 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2951.497 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.158 (n=217)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 33.0 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.176 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0057 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1259` → IC=+0.177 (n=274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1259 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=389)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5882` → IC=+0.195 (n=821)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5882 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.4871` → IC=+0.138 (n=793)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.4871 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.231` → IC=+0.131 (n=800)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.231 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.145 (n=361)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.7144 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.169 (n=279)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.457` → IC=+0.142 (n=224)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.457 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.1802` → IC=+0.134 (n=304)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.1802 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2650.5037` → IC=+0.155 (n=372)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2650.5037 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0279` → IC=+0.240 (n=310)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0279 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.204 (n=826)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1701` → IC=+0.253 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1701 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.169` → IC=+0.251 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.169 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.862` → IC=+0.220 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.862 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.258 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.8291` → IC=+0.210 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8291 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.271 (n=343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0254` → IC=+0.224 (n=342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0254 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.207 (n=965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.209 (n=1085)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.4984` → IC=+0.257 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4984 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.1769` → IC=+0.210 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1769 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.357` → IC=+0.274 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.357 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.238 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.291 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4567` → IC=+0.193 (n=850)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.4567 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.206 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2530.3534` → IC=+0.204 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2530.3534 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.183 (n=748)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 35.0 (IC base=+0.203)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=1804)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.136 (n=1408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0101 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.2784` → IC=+0.139 (n=1065)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2784 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.9278` → IC=+0.194 (n=533)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.9278 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.464` → IC=+0.146 (n=252)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.464 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.1758` → IC=+0.154 (n=438)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1758 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4605` → IC=+0.143 (n=527)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4605 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.8992` → IC=+0.142 (n=1054)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8992 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `8856.6618` → IC=+0.138 (n=724)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 8856.6618 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.171 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.5006` → IC=+0.148 (n=1365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.5006 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.156 (n=463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 4.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.150 (n=601)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.759` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.759 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.323` → IC=+0.138 (n=1361)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.323 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1015` → IC=+0.139 (n=1145)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1015 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1489` → IC=+0.129 (n=1366)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1489 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.148 (n=645)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.508` → IC=+0.136 (n=1350)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.508 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.8045` → IC=+0.136 (n=900)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8045 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=1804)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7754.4674` → IC=+0.133 (n=1219)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7754.4674 (IC base=+0.127)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `2.554` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.554
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.136 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.75` → IC=+0.121 (n=138)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.75 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.554` → IC=+0.149 (n=183)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.554 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.7903` → IC=+0.126 (n=105)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.7903 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.2086` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.2086 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `12609.7541` → IC=+0.150 (n=141)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12609.7541 (IC base=+0.097)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.172 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0035 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.143 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.1703` → IC=+0.159 (n=274)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1703 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.138 (n=620)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.8683` → IC=+0.147 (n=415)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8683 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.0635` → IC=+0.152 (n=294)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0635 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.143 (n=208)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `11116.1452` → IC=+0.123 (n=622)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 11116.1452 (IC base=+0.113)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.211 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.188 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0104 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4173` → IC=+0.158 (n=331)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4173 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.234 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.295` → IC=+0.229 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.295 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.0981` → IC=+0.173 (n=157)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0981 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `3.5724` → IC=+0.155 (n=375)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 3.5724 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.4202` → IC=+0.163 (n=250)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4202 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2269.1774` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2269.1774 (IC base=+0.148)

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

- **PATRÓN** `libro_liquidez` > `2362.106` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.106 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.147 (n=570)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0089 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.135 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0046 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3924` → IC=+0.140 (n=501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3924 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=194)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.139 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.1834` → IC=+0.146 (n=572)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.1834 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `1.0394` → IC=+0.172 (n=129)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 1.0394 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.4258` → IC=+0.141 (n=538)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.4258 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.953` → IC=+0.145 (n=572)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.953 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.116` → IC=+0.144 (n=501)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.116 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0833` → IC=+0.151 (n=253)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0833 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.426` → IC=+0.167 (n=187)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.426 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.8023` → IC=+0.136 (n=374)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8023 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=495)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `8972.466` → IC=+0.150 (n=509)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8972.466 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.170 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0088 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4064` → IC=+0.209 (n=373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4064 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.162 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 10.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.1084` → IC=+0.164 (n=424)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.1084 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.7192` → IC=+0.159 (n=470)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.7192 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.986` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.986 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.171 (n=424)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2227 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.7364` → IC=+0.151 (n=379)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.7364 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1472` → IC=+0.157 (n=432)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1472 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.0698` → IC=+0.165 (n=186)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0698 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1713` → IC=+0.174 (n=366)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.1713 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.168 (n=416)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `8201.961` → IC=+0.167 (n=424)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8201.961 (IC base=+0.151)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `ibs_20min` < `0.4444` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=81)

- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.008)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.01` → IC=-0.294 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=202)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=187)

- **FILTRO** `dist_vwap_pct` > `0.1539` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1539
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=109)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.190 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0056 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.6481` → IC=+0.216 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6481 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.8416` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8416 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.672` → IC=+0.224 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.672 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.8266` → IC=+0.153 (n=197)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8266 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.5821` → IC=+0.128 (n=294)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.5821 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2695` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2695 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.9919` → IC=+0.171 (n=171)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.9919 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `1.4935` → IC=+0.176 (n=174)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4935 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.161 (n=240)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.02 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `1128.1831` → IC=+0.164 (n=242)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 1128.1831 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.0916` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0916 (IC base=-0.115)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=68)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.233 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.151 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 16.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.7829` → IC=+0.223 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7829 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.3158` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3158 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.35` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.35 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.0983` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0983 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` < `0.0595` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0595 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.1435` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1435 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `2.1124` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1124 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.3814` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.3814 (IC base=-0.033)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.370 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=66)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.227 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=45)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.147 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0071 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.6839` → IC=+0.271 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6839 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.49` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.49 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.1427` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1427 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.185` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.185 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.171 (n=80)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.791 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6214 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` < `0.1419` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.1419 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2254` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2254 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `1.4589` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4589 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.177 (n=125)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `1069.2998` → IC=+0.201 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1069.2998 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=-0.118)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1111` → IC=-0.300 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1111
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.204 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.6842 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.9351` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9351 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `0.9891` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.9891 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.0856` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0856 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` < `2.1825` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.1825 (IC base=+0.056)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.125 (n=54)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.07 (IC base=+0.056)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1312` → IC=-0.368 (n=36)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1312
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=71)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.466 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=82)

- **FILTRO** `volumen_pendiente_norm` < `0.137` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.137
  - _Potencial_: sin este filtro IC_bueno=-0.333 (n=10)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.3745` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.3745
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `volumen_regimen` > `1.0011` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.0011
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6037` → IC=-0.460 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6037
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `dist_vwap_pct` > `0.0802` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0802
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=18)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0086` → IC=-0.231 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0086
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `volumen_regimen` < `1.0152` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0152
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0084` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=8)

- **FILTRO** `dist_vwap_pct` < `0.2118` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2118
  - _Potencial_: sin este filtro IC_bueno=-0.312 (n=14)

- **FILTRO** `volumen_regimen` < `1.1255` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1255
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.6331` → IC=-0.246 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6331
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=174)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.138 (n=150)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.251 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.717` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 5.717 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.0687` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0687 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `2923.7123` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2923.7123 (IC base=+0.053)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `ibs_20min` < `0.3927` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3927
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=60)

- **FILTRO** `volumen_regimen` < `0.7102` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7102
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.258 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1622 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.265` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 10.265 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.5658` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.5658 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.6024` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.6024 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3671.9914` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3671.9914 (IC base=+0.109)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=39)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.057)

- **PATRÓN** `drift_60min` |x|≤ `0.2013` → IC=+0.134 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.2013 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.8029` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.8029 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.1039` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1039 (IC base=+0.057)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `2339.7005` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2339.7005 (IC base=+0.057)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 19.0 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `2418.7992` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2418.7992 (IC base=+0.038)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `dist_vwap_pct` > `0.147` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.147
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=35)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7917 (IC base=+0.068)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2760.3525` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2760.3525 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2262.2744` → IC=+0.136 (n=267)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2262.2744 (IC base=+0.092)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2760.3525` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2760.3525 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2262.2744` → IC=+0.136 (n=267)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2262.2744 (IC base=+0.092)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=64)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=109)

- **FILTRO** `libro_liquidez` < `2306.3177` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 2306.3177
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=94)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=171)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=157)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `libro_liquidez` < `11811.9773` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 11811.9773
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `libro_liquidez` < `14445.5423` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 14445.5423
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1074)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=48)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=80)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35093.65` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `liq_usd_total` < 35093.65
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=78)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `liq_usd_total` > `58893.21` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `liq_usd_total` > 58893.21 (IC base=+0.004)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.004)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9534` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9534
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=72)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=79)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=369)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=405)

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
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=63)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=63)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=162)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=162)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=134)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=124)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=124)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=93)

- **FILTRO** `py_entrada` > `0.525` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.525
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` > `0.55` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=50)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2179.3878` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `libro_liquidez` < 2179.3878
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=127)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=397)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=744)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=810)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=1592)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=4827)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.186 (n=1591)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=5025)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.222 (n=253)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=760)

- **FILTRO** `ibs_20min` < `0.7373` → IC=-0.190 (n=253)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7373
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=760)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.169 (n=285)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=873)

- **FILTRO** `ibs_20min` > `0.724` → IC=-0.153 (n=289)

  - _Acción_: SKIP cuando `ibs_20min` > 0.724
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=869)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.181 (n=255)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=781)

- **FILTRO** `ballena_activa_n` > `58.0` → IC=-0.150 (n=258)

  - _Acción_: SKIP cuando `ballena_activa_n` > 58.0
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=778)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.189 (n=342)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=727)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.220 (n=280)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=852)

- **FILTRO** `ibs_20min` > `0.7111` → IC=-0.201 (n=282)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7111
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=850)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.176 (n=251)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=815)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.171 (n=259)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=789)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.140 (n=287)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=793)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.156 (n=271)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=842)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.194 (n=243)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=757)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=985)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=282)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=847)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.340 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=175)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=194)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=525)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=531)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=52)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.0752` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0752
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `py_entrada` > `0.665` → IC=-0.288 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.665
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=101)

- **FILTRO** `ibs_20min` > `0.9863` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9863
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=100)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **PATRÓN** `libro_liquidez` > `4506.3723` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4506.3723 (IC base=-0.035)

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
- **FILTRO** `py_entrada` < `0.35` → IC=-0.279 (n=3781)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=11713)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.240 (n=3833)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=11661)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.168 (n=5216)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=10278)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.222 (n=4784)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=14787)

- **FILTRO** `ibs_7min` > `0.7143` → IC=-0.173 (n=4883)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=14688)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.309 (n=552)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1737)

- **FILTRO** `ibs_7min` < `0.7043` → IC=-0.253 (n=754)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7043
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1535)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=546)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1743)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.241 (n=844)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2551)

- **FILTRO** `drift_7min_pct` |x|> `0.1135` → IC=-0.133 (n=1154)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1135
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=2241)

- **FILTRO** `ibs_7min` > `0.837` → IC=-0.198 (n=848)

  - _Acción_: SKIP cuando `ibs_7min` > 0.837
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2547)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=2226)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.259 (n=694)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2167)

- **FILTRO** `ibs_7min` < `0.7734` → IC=-0.190 (n=715)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7734
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=2146)

- **FILTRO** `ballena_activa_n` > `167.0` → IC=-0.175 (n=713)

  - _Acción_: SKIP cuando `ballena_activa_n` > 167.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2148)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.243 (n=694)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2186)

- **FILTRO** `ballena_activa_n` > `108.0` → IC=-0.172 (n=972)

  - _Acción_: SKIP cuando `ballena_activa_n` > 108.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1908)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.183 (n=740)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=1545)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.303 (n=725)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=1560)

- **FILTRO** `ibs_7min` < `0.2174` → IC=-0.288 (n=570)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2174
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1715)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.238 (n=544)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=1741)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.224 (n=837)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=2705)

- **FILTRO** `ibs_7min` > `0.2791` → IC=-0.155 (n=1204)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2791
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=2338)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.141 (n=808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=1808)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=629)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=1987)

- **FILTRO** `ibs_7min` < `0.7565` → IC=-0.191 (n=654)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7565
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=1962)

- **FILTRO** `ballena_activa_n` > `37.0` → IC=-0.183 (n=651)

  - _Acción_: SKIP cuando `ballena_activa_n` > 37.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=1965)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.234 (n=864)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1774)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.179 (n=659)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=1979)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.185 (n=656)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=1982)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.243 (n=703)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2197)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.205 (n=720)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2180)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.178 (n=871)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2800)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.126 (n=615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=1928)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.294 (n=620)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1923)

- **FILTRO** `ibs_7min` < `0.7391` → IC=-0.233 (n=634)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7391
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1909)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.226 (n=619)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1924)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.206 (n=839)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=2606)

- **FILTRO** `ibs_7min` > `0.7612` → IC=-0.156 (n=861)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7612
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2584)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=118)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=430)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=38)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=481)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.146 (n=541)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.169 (n=173)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 459.6089 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=255)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3336.2388` → IC=+0.154 (n=212)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3336.2388 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.132 (n=387)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 64.0 (IC base=+0.132)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.268 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.122)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `libro_liquidez` > `2005.686` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2005.686 (IC base=+0.094)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.205 (n=59)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.145 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.113)

- **PATRÓN** `total_vol_5m` < `498.2784` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 498.2784 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `7409.4986` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 7409.4986 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.140 (n=87)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 153.0 (IC base=+0.113)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4084` → IC=+0.207 (n=73)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4084 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.242 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.182)

- **PATRÓN** `total_vol_5m` < `5874.669` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 5874.669 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `3096.9147` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3096.9147 (IC base=+0.182)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.155 (n=85)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.132 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.159 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 14.0 (IC base=+0.133)

- **PATRÓN** `total_vol_5m` < `258575.4` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 258575.4 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `3219.1556` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3219.1556 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 41.0 (IC base=+0.133)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `3.488` → IC=-0.389 (n=61)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.488
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=120)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.363 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=25)

- **FILTRO** `T_h` > `39.9952` → IC=-0.378 (n=39)

  - _Acción_: SKIP cuando `T_h` > 39.9952
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.132)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.214 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `135.9952` → IC=-0.167 (n=49)

  - _Acción_: SKIP cuando `T_h` > 135.9952
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=151)

- **FILTRO** `pct_vs_K` |x|> `5.2323` → IC=-0.245 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.2323
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=151)

- **FILTRO** `T_h` > `145.6762` → IC=-0.360 (n=55)

  - _Acción_: SKIP cuando `T_h` > 145.6762
  - _Potencial_: sin este filtro IC_bueno=-0.307 (n=112)

- **FILTRO** `pct_vs_K` |x|> `4.4208` → IC=-0.448 (n=56)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4208
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=111)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `87.9866` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `T_h` > 87.9866
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **FILTRO** `pct_vs_K` |x|> `3.6199` → IC=-0.444 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.6199
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=59)

- **FILTRO** `T_h` > `144.6172` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=41)

- **FILTRO** `pct_vs_K` |x|> `2.3742` → IC=-0.435 (n=29)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3742
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=31)

- **PATRÓN** `pct_vs_K` |x|≤ `1.2308` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.2308 (IC base=-0.058)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0037` → IC=-0.256 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `T_h` > `111.9956` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 111.9956
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=36)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.357 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=39)

- **FILTRO** `T_h` > `145.5703` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `T_h` > 145.5703
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=31)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.395 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

- **FILTRO** `T_h` > `135.2296` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `T_h` > 135.2296
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2412` → IC=+0.400 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2412 (IC base=+0.385)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.385)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.385)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.385)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.385)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `7.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=67)

- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=74)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=140)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=74)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=77)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=22)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` < `3.0` → IC=-0.144 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=165)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=185)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=187)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=196)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=294)

- **PATRÓN** `streak_estiramiento` < `0.3555` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.3555 (IC base=+0.033)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=579)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=301)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=378)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1657)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=920)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=928)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.167 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0036 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.182 (n=199)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0075 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0605` → IC=+0.144 (n=594)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.0605 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.325` → IC=+0.189 (n=281)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.325 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.143 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 4.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.177 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.5909` → IC=+0.224 (n=595)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5909 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.4267` → IC=+0.157 (n=138)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.4267 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.5539` → IC=+0.140 (n=634)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.5539 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.55` → IC=+0.231 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.55 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=595)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `9700.4747` → IC=+0.175 (n=198)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 9700.4747 (IC base=+0.141)

### UPDOWN_GBM#5min
- **FILTRO** `sigma_ewma_delta_pct` > `7.859` → IC=-0.198 (n=41)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.859
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1165)

### UPDOWN_GBM#60min
- **FILTRO** `ibs_15` < `0.2195` → IC=-0.149 (n=35)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.2195
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=106)

- **FILTRO** `sigma_ewma_delta_pct` > `7.975` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.975
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=78)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=101)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.130 (n=71)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=145)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.190 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0032 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.175 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0045 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.1907` → IC=+0.196 (n=166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1907 (IC base=+0.171)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1443` → IC=+0.221 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1443 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.193 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 4.0 (IC base=+0.171)

- **PATRÓN** `ibs_15` > `0.8766` → IC=+0.295 (n=110)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8766 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.1197` → IC=+0.191 (n=108)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1197 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.367` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.367 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `14792.3098` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14792.3098 (IC base=+0.171)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.190 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=56)

- **FILTRO** `ibs_15` < `0.1742` → IC=-0.227 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1742
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=63)

- **FILTRO** `libro_liquidez` < `12194.7668` → IC=-0.151 (n=41)

  - _Acción_: SKIP cuando `libro_liquidez` < 12194.7668
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=42)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=148)

- **FILTRO** `ibs_15` < `0.675` → IC=-0.181 (n=45)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=136)

- **FILTRO** `sigma_ewma_delta_pct` > `8.068` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.068
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=51)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.029` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 20.029 (IC base=+0.005)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6414` → IC=-0.194 (n=47)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6414
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=143)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.146 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0034 (IC base=+0.099)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2632` → IC=+0.180 (n=48)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.2632 (IC base=+0.099)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1616` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1616 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.124 (n=147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 17.0 (IC base=+0.099)

- **PATRÓN** `ibs_15` > `0.6414` → IC=+0.197 (n=143)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.6414 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.138 (n=114)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1511 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.638` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 14.638 (IC base=+0.099)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=95)

- **FILTRO** `dist_vwap_pct` > `0.215` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.215
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=107)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `libro_spread` > `0.03` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=173)

- **FILTRO** `drift_15min` |x|> `0.3898` → IC=-0.167 (n=19)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3898
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `ibs_15` > `0.2172` → IC=-0.184 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2172
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.5217` → IC=-0.241 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5217
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=76)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.141 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.131)

- **PATRÓN** `delta_ratio_macro` |x|> `0.209` → IC=+0.176 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.209 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.5217` → IC=+0.256 (n=76)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5217 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.0973` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.0973 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.935` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.935 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3020.8724` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3020.8724 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.131)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0251` → IC=-0.207 (n=39)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0251
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=119)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.130 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=106)

- **FILTRO** `ibs_15` < `0.4286` → IC=-0.207 (n=39)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.4286
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=119)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `12.798` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 12.798
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **PATRÓN** `dist_vwap_pct` < `0.3849` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.3849 (IC base=+0.010)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `delta_ratio_macro` |x|> `0.0487` → IC=+0.165 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.0487 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.213 (n=162)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1139` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1139 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.55` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.55 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `2685.6817` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2685.6817 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` < `0.1163` → IC=+0.175 (n=186)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` < 0.1163 (IC base=+0.028)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.323 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.320)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.387 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.320)

- **PATRÓN** `drift_60min` |x|≤ `0.1149` → IC=+0.344 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1149 (IC base=+0.320)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.329 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.320)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.364 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.320)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.337 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.320)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.388 (n=185)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.320)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.320)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.464` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.464 (IC base=+0.320)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.888` → IC=+0.326 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.888 (IC base=+0.320)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.326 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.320)

- **PATRÓN** `libro_liquidez` > `8508.8052` → IC=+0.354 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8508.8052 (IC base=+0.320)

- **PATRÓN** `ballena_activa_n` < `528.0` → IC=+0.361 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 528.0 (IC base=+0.320)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1148` → IC=+0.337 (n=41)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1148 (IC base=+0.310)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.307 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.310)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.337 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.310)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.326 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.310)

- **PATRÓN** `drift_15min` |x|≤ `0.411` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.411 (IC base=+0.310)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.319 (n=81)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.310)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.356 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.310)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.354 (n=121)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.310)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.509` → IC=+0.332 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.509 (IC base=+0.310)

- **PATRÓN** `libro_liquidez` > `8157.6321` → IC=+0.355 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8157.6321 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `626.0` → IC=+0.407 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 626.0 (IC base=+0.310)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.325 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.329)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.381 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.367 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.343 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2105` → IC=+0.333 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2105 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.333 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.329)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.329 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.399 (n=87)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.350 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.144` → IC=+0.357 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.144 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `2809.1248` → IC=+0.325 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2809.1248 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 166.0 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0112` → IC=-0.194 (n=364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0112
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=1093)

- **FILTRO** `ibs_15` < `0.5833` → IC=-0.187 (n=164)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5833
  - _Potencial_: sin este filtro IC_bueno=+0.228 (n=333)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.141 (n=380)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=1077)

- **FILTRO** `sigma_ewma_delta_pct` > `18.709` → IC=-0.153 (n=529)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.709
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4013)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3526` → IC=+0.176 (n=211)

  - _Acción_: Kelly boost +0.88€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3526 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.5833` → IC=+0.228 (n=333)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5833 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.1752` → IC=+0.129 (n=227)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1752 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1246` → IC=+0.222 (n=350)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1246 (IC base=-0.064)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1113` → IC=+0.230 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1113 (IC base=-0.064)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.266 (n=524)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.4226` → IC=+0.210 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4226 (IC base=-0.064)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.214 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=-0.064)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.234 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=709)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.232 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=633)

- **FILTRO** `sigma_ewma_delta_pct` > `19.521` → IC=-0.250 (n=170)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.521
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=774)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.192 (n=24)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.023)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1355` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1355 (IC base=+0.023)

- **PATRÓN** `ibs_15` > `0.6026` → IC=+0.296 (n=52)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6026 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.1742` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1742 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `308.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 308.0 (IC base=+0.023)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6395` → IC=-0.247 (n=77)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6395
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=158)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=218)

- **PATRÓN** `drift_60min` |x|≤ `0.0809` → IC=+0.212 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0809 (IC base=+0.091)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.216 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.091)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.256 (n=158)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` < `0.1779` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1779 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `10832.9607` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 10832.9607 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.244 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.212 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.4379` → IC=+0.216 (n=248)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4379 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0914` → IC=+0.219 (n=222)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0914 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.282 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.272 (n=248)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.2343` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2343 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.4044` → IC=+0.210 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4044 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.609` → IC=+0.228 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.609 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `3638.7885` → IC=+0.212 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3638.7885 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `184.0` → IC=+0.214 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 184.0 (IC base=+0.211)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1609` → IC=-0.188 (n=123)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1609
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=240)

- **FILTRO** `drift_15min` |x|> `0.8398` → IC=-0.261 (n=90)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8398
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=273)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.169 (n=125)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=238)

- **FILTRO** `sigma_ewma_delta_pct` > `16.339` → IC=-0.150 (n=181)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.339
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1413)

- **PATRÓN** `ibs_15` > `0.8214` → IC=+0.262 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8214 (IC base=-0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.124` → IC=+0.175 (n=78)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.124 (IC base=-0.049)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.202` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.202 (IC base=-0.049)

- **PATRÓN** `ibs_15` < `0.3926` → IC=+0.223 (n=117)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3926 (IC base=-0.049)

- **PATRÓN** `dist_vwap_pct` < `0.1449` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1449 (IC base=-0.049)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0178` → IC=-0.232 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0178
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=205)

- **FILTRO** `drift_15min` |x|> `1.1964` → IC=-0.248 (n=101)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1964
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=307)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0953` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0953 (IC base=-0.061)

- **PATRÓN** `ibs_15` < `0.3448` → IC=+0.273 (n=139)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3448 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` > `0.4772` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4772 (IC base=-0.061)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=-0.061)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.206 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.4465` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4465 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.2576` → IC=+0.208 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2576 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `12949.2689` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12949.2689 (IC base=+0.100)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.206 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.4465` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4465 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.2576` → IC=+0.208 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.2576 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.0928` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0928 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `12949.2689` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12949.2689 (IC base=+0.100)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.286 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.291 (n=161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.342 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.303 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.109` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.109 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.834` → IC=+0.315 (n=354)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.834 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.3024` → IC=+0.322 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3024 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.231` → IC=+0.287 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.231 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.289 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13923.122` → IC=+0.325 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13923.122 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.296 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.287 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.279)

- **PATRÓN** `drift_60min` |x|≤ `0.0604` → IC=+0.314 (n=68)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0604 (IC base=+0.279)

- **PATRÓN** `delta_ratio_macro` |x|> `0.128` → IC=+0.318 (n=135)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.128 (IC base=+0.279)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.279)

- **PATRÓN** `ibs_15` > `0.8545` → IC=+0.309 (n=181)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8545 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.3131` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3131 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.806` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.806 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.606` → IC=+0.285 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.606 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `15571.5606` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15571.5606 (IC base=+0.279)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.298 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.290 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0682` → IC=+0.341 (n=67)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0682 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1898` → IC=+0.317 (n=69)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1898 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.350 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.326 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.846` → IC=+0.325 (n=152)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.846 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2966` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2966 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` < `0.4822` → IC=+0.291 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4822 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.319` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.319 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.28` → IC=+0.289 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.28 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.304 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `12232.3596` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12232.3596 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `190.0` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 190.0 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0807` → IC=-0.253 (n=75)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0807
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=146)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1209` → IC=-0.157 (n=106)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1209
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=320)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.174` → IC=-0.129 (n=60)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.174
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=61)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `drift_60min` |x|> `0.1544` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1544
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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
- **FILTRO** `drift_15min` |x|> `0.1405` → IC=-0.342 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1405
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.1352` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1352
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9922` → IC=+0.347 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.115)

- **PATRÓN** `T_h` > `145.965` → IC=+0.419 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.965 (IC base=+0.343)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.343)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.973` → IC=+0.375 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.096)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.282)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9624` → IC=+0.438 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9624 (IC base=+0.163)

- **PATRÓN** `T_h` > `87.996` → IC=+0.329 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.996 (IC base=+0.315)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.330 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.315)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `127.3918` → IC=+0.425 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 127.3918 (IC base=+0.409)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5909 sube el IC de +0.141 a +0.224 en UPDOWN_GBM#15min (n=595). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8766 sube el IC de +0.171 a +0.295 en UPDOWN_GBM#BTC#15min (n=110). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6414 sube el IC de +0.099 a +0.197 en UPDOWN_GBM#ETH#15min (n=143). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5217 sube el IC de +0.131 a +0.256 en UPDOWN_GBM#SOL#15min (n=76). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.131 a +0.213 en UPDOWN_GBM#XRP#15min (n=162). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1163 sube el IC de +0.028 a +0.175 en UPDOWN_GBM#XRP#15min (n=186). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5833 sube el IC de -0.066 a +0.228 en UPDOWN_GBM_15M_TARDIO (n=333). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.064 a +0.266 en UPDOWN_GBM_15M_TARDIO (n=524). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.6026 sube el IC de +0.023 a +0.296 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=52). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6395 sube el IC de +0.091 a +0.256 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=158). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.211 a +0.272 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=248). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8214 sube el IC de -0.130 a +0.262 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3926 sube el IC de -0.049 a +0.223 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=117). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3448 sube el IC de -0.061 a +0.273 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=139). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7 (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.834 sube el IC de +0.284 a +0.315 en UPDOWN_GBM_IBS_ALTO (n=354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8545 sube el IC de +0.279 a +0.309 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=181). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.846 sube el IC de +0.289 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=152). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.320 a +0.388 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=185). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.310 a +0.354 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=121). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.329 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=87). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min` — IC=+0.083 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC` — IC=+0.083 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 862 | +0.088 | +54.76€ | 2 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 862 | +0.088 | +54.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 25 | +0.056 | -0.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 25 | +0.056 | -0.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 573 | +0.103 | +40.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 573 | +0.103 | +40.75€ | 3 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 5 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 42 | +0.159 | +15.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 42 | +0.159 | +15.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 15859 | -0.117 | -2571.29€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 987 | -0.015 | -143.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 14872 | -0.124 | -2427.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 2134 | -0.107 | -471.53€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 2134 | -0.107 | -471.53€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 987 | -0.015 | -143.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 987 | -0.015 | -143.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 2092 | -0.175 | -580.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 2092 | -0.175 | -580.25€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 4216 | -0.057 | -388.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 4216 | -0.057 | -388.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 3530 | -0.129 | -228.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 3530 | -0.129 | -228.29€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2900 | -0.191 | -759.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2900 | -0.191 | -759.17€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 4943 | -0.080 | +1957.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 1415 | -0.013 | +1069.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 3528 | -0.106 | +888.48€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 4943 | -0.080 | +1957.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 1415 | -0.013 | +1069.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 3528 | -0.106 | +888.48€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 106 | -0.028 | -8.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 106 | -0.028 | -8.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 106 | -0.028 | -8.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 106 | -0.028 | -8.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 50923 | +0.114 | -3069.31€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 8468 | +0.182 | -297.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 180 | -0.110 | -57.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 38407 | +0.100 | -2633.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3868 | +0.116 | -81.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 6442 | +0.086 | -795.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 28 | -0.100 | +6.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 6399 | +0.088 | -790.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 10177 | +0.132 | -229.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2495 | +0.197 | -121.26€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 6349 | +0.110 | -130.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1291 | +0.123 | +44.51€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 6463 | +0.086 | -752.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 31 | +0.015 | +3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#240min | 14 | -0.219 | -10.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 6418 | +0.087 | -745.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 11000 | +0.126 | -188.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 3161 | +0.170 | -30.90€ | 1 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 6390 | +0.111 | -108.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1437 | +0.096 | -40.69€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 10398 | +0.122 | -673.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2730 | +0.189 | -156.69€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 88 | -0.022 | -5.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 6440 | +0.095 | -426.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1140 | +0.131 | -84.86€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 6443 | +0.105 | -429.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 23 | -0.020 | +1.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 9 | +0.021 | +0.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 6411 | +0.106 | -432.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 8357 | +0.180 | -623.93€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 8357 | +0.180 | -623.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2133 | +0.168 | -228.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2133 | +0.168 | -228.90€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 149 | -0.136 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 149 | -0.136 | -0.83€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2088 | +0.172 | -213.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2088 | +0.172 | -213.47€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1869 | +0.236 | -46.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1869 | +0.236 | -46.22€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2039 | +0.187 | -148.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2039 | +0.187 | -148.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 417 | +0.443 | +0.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 417 | +0.443 | +0.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 159 | +0.444 | +1.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 159 | +0.444 | +1.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 159 | +0.438 | -0.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 159 | +0.438 | -0.08€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 95 | +0.428 | -1.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 95 | +0.428 | -1.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 27251 | +0.191 | -2462.37€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 27251 | +0.191 | -2462.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 4846 | +0.154 | -727.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 4846 | +0.154 | -727.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 4256 | +0.226 | -145.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 4256 | +0.226 | -145.38€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 4712 | +0.166 | -621.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 4712 | +0.166 | -621.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 4342 | +0.219 | -175.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 4342 | +0.219 | -175.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 4506 | +0.201 | -321.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 4506 | +0.201 | -321.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 4589 | +0.185 | -471.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 4589 | +0.185 | -471.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 9911 | +0.130 | +310.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 9911 | +0.130 | +310.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 4907 | +0.136 | +206.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 4907 | +0.136 | +206.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 5004 | +0.123 | +103.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 5004 | +0.123 | +103.90€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 992 | +0.291 | -12.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 992 | +0.291 | -12.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 429 | +0.277 | -12.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 429 | +0.277 | -12.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 468 | +0.294 | +1.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 468 | +0.294 | +1.58€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 95 | +0.325 | -2.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 95 | +0.325 | -2.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 429 | +0.421 | -13.49€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 429 | +0.421 | -13.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 193 | +0.418 | -7.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 193 | +0.418 | -7.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 199 | +0.425 | -5.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 199 | +0.425 | -5.68€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 37 | +0.372 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 37 | +0.372 | -0.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 518 | +0.094 | -4.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 180 | +0.082 | -7.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 338 | +0.100 | +3.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 34 | +0.083 | +0.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 34 | +0.083 | +0.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 405 | +0.104 | +6.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 67 | +0.123 | +3.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 338 | +0.100 | +3.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 79 | +0.043 | -10.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 79 | +0.043 | -10.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 15387 | +0.096 | -553.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1370 | +0.078 | -20.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 14017 | +0.098 | -533.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 9174 | +0.099 | -196.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1370 | +0.078 | -20.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 7804 | +0.102 | -176.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 2059 | +0.114 | +20.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 2059 | +0.114 | +20.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 4154 | +0.081 | -377.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 4154 | +0.081 | -377.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 587 | +0.259 | -73.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 587 | +0.259 | -73.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 587 | +0.259 | -73.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 587 | +0.259 | -73.31€ | 0 | 4 |
| ✅ GBM_LATE_15M | 12832 | +0.059 | +5498.83€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 12832 | +0.059 | +5498.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 1994 | +0.195 | +1457.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 1994 | +0.195 | +1457.41€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 1918 | +0.178 | +1319.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1918 | +0.178 | +1319.45€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 2039 | +0.195 | +1480.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 2039 | +0.195 | +1480.55€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 1982 | -0.035 | +127.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1982 | -0.035 | +127.55€ | 2 | 10 |
| ✅ GBM_LATE_15M#SOL | 2032 | -0.052 | +472.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2032 | -0.052 | +472.91€ | 5 | 8 |
| ✅ GBM_LATE_15M#XRP | 2867 | -0.067 | +640.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2867 | -0.067 | +640.95€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 13661 | +0.063 | +7054.09€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 13661 | +0.063 | +7054.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 2406 | +0.000 | +1731.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 2406 | +0.000 | +1731.80€ | 2 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2958 | -0.017 | +458.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2958 | -0.017 | +458.10€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1815 | +0.256 | +1780.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1815 | +0.256 | +1780.72€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2066 | -0.046 | +71.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2066 | -0.046 | +71.92€ | 6 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2271 | -0.009 | +829.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2271 | -0.009 | +829.75€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2145 | +0.264 | +2181.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2145 | +0.264 | +2181.80€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 10606 | +0.168 | +7516.92€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 10606 | +0.168 | +7516.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1507 | +0.202 | +1168.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1507 | +0.202 | +1168.04€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1739 | +0.158 | +1258.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1739 | +0.158 | +1258.27€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1553 | +0.197 | +1169.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1553 | +0.197 | +1169.44€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1735 | +0.140 | +1058.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1735 | +0.140 | +1058.36€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 1979 | +0.119 | +1243.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 1979 | +0.119 | +1243.82€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2093 | +0.198 | +1618.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2093 | +0.198 | +1618.98€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 2391 | +0.108 | +805.71€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 2391 | +0.108 | +805.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 91 | +0.113 | +37.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 91 | +0.113 | +37.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 604 | +0.087 | +180.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 604 | +0.087 | +180.30€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 344 | +0.144 | +166.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 344 | +0.144 | +166.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 559 | +0.165 | +240.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 559 | +0.165 | +240.07€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 406 | +0.005 | +29.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 406 | +0.005 | +29.11€ | 4 | 4 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 12743 | +0.174 | +9196.74€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#15min | 12743 | +0.174 | +9196.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1916 | +0.221 | +1619.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1916 | +0.221 | +1619.21€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2062 | +0.161 | +1474.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2062 | +0.161 | +1474.35€ | 0 | 29 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 1935 | +0.222 | +1638.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 1935 | +0.222 | +1638.51€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1971 | +0.134 | +1172.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1971 | +0.134 | +1172.49€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2255 | +0.105 | +1265.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2255 | +0.105 | +1265.93€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2604 | +0.203 | +2026.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2604 | +0.203 | +2026.26€ | 0 | 23 |
| ✅ GBM_LATE_5M | 3948 | +0.124 | +1847.47€ | 1 | 23 |
| ✅ GBM_LATE_5M#5min | 3948 | +0.124 | +1847.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 242 | +0.176 | +159.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 242 | +0.176 | +159.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1038 | +0.110 | +504.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1038 | +0.110 | +504.88€ | 1 | 16 |
| ✅ GBM_LATE_5M#DOGE | 560 | +0.160 | +329.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 560 | +0.160 | +329.63€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 1324 | +0.141 | +657.05€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1324 | +0.141 | +657.05€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 171 | -0.009 | +8.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 171 | -0.009 | +8.37€ | 2 | 1 |
| ✅ GBM_LATE_5M#XRP | 613 | +0.095 | +187.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 613 | +0.095 | +187.99€ | 0 | 0 |
| ✅ GBM_LATE_60M | 782 | +0.024 | +200.56€ | 3 | 13 |
| ✅ GBM_LATE_60M#60min | 782 | +0.024 | +200.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 260 | +0.061 | +57.93€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 260 | +0.061 | +57.93€ | 1 | 11 |
| ✅ GBM_LATE_60M#ETH | 287 | +0.043 | +97.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 287 | +0.043 | +97.03€ | 2 | 14 |
| ✅ GBM_LATE_60M#SOL | 235 | -0.040 | +45.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 235 | -0.040 | +45.59€ | 1 | 8 |
| 🚫 GBM_LATE_60M_FADE | 221 | -0.298 | -34.86€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 221 | -0.298 | -34.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 86 | -0.250 | -8.73€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 86 | -0.250 | -8.73€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 73 | -0.353 | -21.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 73 | -0.353 | -21.66€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 62 | -0.281 | -4.47€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 62 | -0.281 | -4.47€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 457 | +0.040 | +42.25€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 457 | +0.040 | +42.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 187 | +0.045 | +25.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 187 | +0.045 | +25.52€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 122 | +0.048 | -3.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 122 | +0.048 | -3.59€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 148 | +0.027 | +20.33€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 148 | +0.027 | +20.33€ | 1 | 1 |
| ✅ LATE_WINDOW_5MIN | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 655 | +0.095 | +154.14€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 655 | +0.095 | +154.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 655 | +0.095 | +154.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 655 | +0.095 | +154.14€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 317 | -0.099 | -37.91€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 317 | -0.099 | -37.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 73 | -0.113 | -10.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 73 | -0.113 | -10.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 97 | -0.025 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 97 | -0.025 | -3.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 1271 | -0.010 | -19.02€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1271 | -0.010 | -19.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 71 | -0.021 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 71 | -0.021 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 149 | -0.036 | -5.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 149 | -0.036 | -5.37€ | 3 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 99 | -0.054 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 99 | -0.054 | -6.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 415 | +0.020 | +11.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 415 | +0.020 | +11.04€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 445 | -0.006 | -8.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 445 | -0.006 | -8.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 92 | -0.064 | -5.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 92 | -0.064 | -5.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 660 | -0.023 | -5.79€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 660 | -0.023 | -5.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 196 | -0.040 | -10.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 196 | -0.040 | -10.24€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 199 | +0.003 | +3.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 199 | +0.003 | +3.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 265 | -0.028 | +0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 265 | -0.028 | +0.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 7941 | -0.004 | -103.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 7941 | -0.004 | -103.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 555 | -0.008 | +0.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 555 | -0.008 | +0.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 860 | -0.019 | -19.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 860 | -0.019 | -19.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1848 | +0.009 | -14.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1848 | +0.009 | -14.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1585 | +0.001 | +1.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1585 | +0.001 | +1.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 1615 | -0.010 | -40.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 1615 | -0.010 | -40.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1478 | -0.005 | -30.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1478 | -0.005 | -30.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 13035 | -0.030 | +626.25€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 13035 | -0.030 | +626.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 2171 | -0.017 | +318.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 2171 | -0.017 | +318.42€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 2227 | -0.031 | -10.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 2227 | -0.031 | -10.58€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 2201 | -0.028 | +193.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 2201 | -0.028 | +193.81€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 2114 | -0.046 | -47.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 2114 | -0.046 | -47.16€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 2193 | -0.033 | +90.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 2193 | -0.033 | +90.35€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 2129 | -0.025 | +81.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 2129 | -0.025 | +81.41€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 769 | -0.086 | -47.36€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 769 | -0.086 | -47.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 110 | -0.045 | -6.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 110 | -0.045 | -6.25€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 118 | -0.150 | -14.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 118 | -0.150 | -14.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 36 | -0.105 | -4.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 163 | -0.161 | -16.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 163 | -0.161 | -16.98€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 226 | -0.048 | -0.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 226 | -0.048 | -0.24€ | 0 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 116 | -0.017 | -5.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 116 | -0.017 | -5.58€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1386 | +0.006 | -1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1386 | +0.006 | -1.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 35065 | -0.077 | +614.58€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 35065 | -0.077 | +614.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 5684 | -0.088 | +433.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 5684 | -0.088 | +433.08€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 5741 | -0.080 | -144.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 5741 | -0.080 | -144.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 5827 | -0.083 | +199.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 5827 | -0.083 | +199.85€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 5254 | -0.100 | -290.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 5254 | -0.100 | -290.96€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 6571 | -0.052 | +126.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 6571 | -0.052 | +126.00€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 5988 | -0.065 | +290.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 5988 | -0.065 | +290.97€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6289 | -0.015 | -114.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6289 | -0.015 | -114.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 995 | -0.018 | -20.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 995 | -0.018 | -20.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1334 | -0.011 | -15.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1334 | -0.011 | -15.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1366 | -0.005 | -10.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1366 | -0.005 | -10.10€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 856 | -0.021 | -13.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 856 | -0.021 | -13.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 759 | +0.116 | +263.90€ | 1 | 6 |
| ✅ ORDER_FLOW_5M#5min | 623 | +0.129 | +251.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 146 | +0.122 | +62.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 146 | +0.122 | +62.09€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 126 | +0.094 | +27.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 126 | +0.094 | +27.35€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 117 | +0.113 | +44.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 117 | +0.113 | +44.11€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 108 | +0.182 | +68.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 108 | +0.182 | +68.43€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 126 | +0.133 | +49.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 126 | +0.133 | +49.33€ | 0 | 7 |
| ✅ PRICE_TARGET_GBM | 346 | -0.129 | -14.35€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 152 | -0.201 | -37.26€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 122 | -0.258 | -39.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 30 | +0.031 | +1.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 130 | -0.106 | +2.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 93 | -0.132 | -5.01€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 37 | -0.038 | +7.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 64 | +0.000 | +20.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 47 | -0.031 | +13.70€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 17 | +0.067 | +7.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 262 | -0.174 | -30.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 84 | +0.012 | +15.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 367 | -0.213 | -12.47€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 159 | -0.177 | -12.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 135 | -0.164 | -11.63€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 24 | -0.231 | -1.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 133 | -0.263 | -18.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 111 | -0.279 | -22.51€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 22 | -0.167 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 75 | -0.188 | +18.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 62 | -0.188 | +14.99€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 13 | -0.108 | +3.57€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 308 | -0.213 | -19.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 59 | -0.205 | +6.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 108 | +0.364 | +44.60€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#BTC | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 63 | +0.485 | +42.99€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 63 | +0.485 | +42.99€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 108 | +0.364 | +44.60€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 252 | +0.028 | -4.08€ | 3 | 0 |
| ✅ STREAK_FADE_15M#15min | 252 | +0.028 | -4.08€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 112 | +0.053 | +2.33€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 112 | +0.053 | +2.33€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 26 | +0.000 | -2.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 96 | +0.000 | -5.73€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 96 | +0.000 | -5.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1932 | -0.023 | -84.59€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1932 | -0.023 | -84.59€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 801 | -0.018 | -26.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 801 | -0.018 | -26.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 553 | -0.026 | -25.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 553 | -0.026 | -25.13€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 141 | -0.038 | -12.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 141 | -0.038 | -12.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 437 | -0.024 | -20.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 437 | -0.024 | -20.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 4103 | +0.018 | +46.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 4103 | +0.018 | +46.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1334 | +0.019 | +10.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1334 | +0.019 | +10.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 836 | +0.035 | +29.96€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 836 | +0.035 | +29.96€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 1212 | +0.007 | -7.23€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1212 | +0.007 | -7.23€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 721 | +0.016 | +13.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 721 | +0.016 | +13.32€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 4365 | +0.012 | -23.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 4365 | +0.012 | -23.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1676 | +0.013 | -9.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1676 | +0.013 | -9.41€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1737 | +0.021 | +5.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1737 | +0.021 | +5.44€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 952 | -0.005 | -19.60€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 952 | -0.005 | -19.60€ | 2 | 0 |
| ✅ UPDOWN_GBM | 11085 | +0.011 | +372.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3789 | +0.040 | +411.02€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 466 | +0.006 | +5.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 6080 | -0.002 | -34.24€ | 1 | 0 |
| ✅ UPDOWN_GBM#60min | 698 | -0.009 | -9.18€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 532 | +0.071 | +59.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 187 | +0.114 | +44.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 11 | -0.021 | -0.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 334 | +0.051 | +15.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 2039 | +0.014 | +109.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 436 | +0.071 | +87.28€ | 1 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 141 | +0.045 | +8.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1169 | -0.005 | +16.75€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 273 | -0.002 | -4.10€ | 3 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 20 | -0.136 | +1.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 1303 | +0.008 | +10.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 130 | +0.091 | +29.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 10 | +0.042 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 1163 | -0.002 | -19.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 2247 | +0.001 | +21.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1083 | +0.029 | +49.11€ | 1 | 7 |
| ✅ UPDOWN_GBM#ETH#240min | 131 | +0.019 | +6.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 733 | -0.033 | -29.70€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 283 | -0.016 | -4.60€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 17 | -0.157 | +0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 3159 | +0.004 | +22.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 998 | +0.006 | +25.21€ | 1 | 9 |
| ✅ UPDOWN_GBM#SOL#240min | 125 | -0.004 | -2.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1881 | +0.006 | +0.96€ | 3 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 142 | -0.007 | -0.48€ | 1 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 13 | -0.152 | -0.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1803 | +0.020 | +150.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 955 | +0.052 | +175.45€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 48 | -0.120 | -6.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 800 | -0.009 | -18.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 50 | -0.192 | +0.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 276 | +0.320 | +62.06€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 276 | +0.320 | +62.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 161 | +0.310 | +28.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 161 | +0.310 | +28.06€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 115 | +0.329 | +34.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 115 | +0.329 | +34.00€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 5999 | -0.064 | +1312.20€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 5999 | -0.064 | +1312.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 310 | -0.051 | +340.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 310 | -0.051 | +340.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1223 | -0.148 | -57.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1223 | -0.148 | -57.28€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 565 | +0.161 | +278.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 565 | +0.161 | +278.25€ | 2 | 16 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 1957 | -0.064 | +374.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 1957 | -0.064 | +374.19€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1863 | -0.085 | +367.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1863 | -0.085 | +367.84€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 58 | +0.067 | +3.64€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 58 | +0.067 | +3.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 58 | +0.067 | +3.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 58 | +0.067 | +3.64€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 471 | +0.284 | +371.16€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 471 | +0.284 | +371.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 269 | +0.279 | +206.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 269 | +0.279 | +206.91€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 202 | +0.289 | +164.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 202 | +0.289 | +164.25€ | 0 | 14 |
| ✅ UPDOWN_OU_5M | 647 | -0.099 | -71.52€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 647 | -0.099 | -71.52€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 310 | -0.077 | -35.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 310 | -0.077 | -35.00€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 159 | -0.047 | -8.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 159 | -0.047 | -8.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 59 | -0.172 | -8.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 59 | -0.172 | -8.77€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 52 | -0.167 | -5.48€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 52 | -0.167 | -5.48€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1424 | +0.294 | +625.49€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 458 | +0.226 | +22.35€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 472 | +0.276 | +139.65€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 494 | +0.373 | +463.49€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.081) — sin ventaja clara. oversold(IBS<0.3): IC=+0.027 n=3914 | neutral: IC=+0.006 n=4305 | overbought(IBS>0.7): IC=+0.087 n=4315
  - _Datos_: n=13022 IC=+0.042 PNL=+1365.43€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 226 celda(s) pasan gate riguroso completo de 1474 evaluadas (n>=40) y 2536 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.006 < 0.08 — monitorear
  - _Datos_: n=998 IC=+0.006 PNL=+25.21€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=472/15 IC=+0.276 PNL=+139.65€ | BTC: n=458/15 IC=+0.226 PNL=+22.35€ | SOL: n=494/15 IC=+0.373 PNL=+463.49€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 23 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 11023 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.027 n=72/60 | contraria IC=+0.112 n=47 | gap=-0.085 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=159, boost estimado=+0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 108 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=283/40 IC=-0.016 PNL=-4.60€ | BTC#60min: n=273/40 IC=-0.002 PNL=-4.10€ | SOL#60min: n=142/40 IC=-0.007 PNL=-0.48€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.064 n=165352 | tras_1loss IC=+0.053 n=130392 | tras_2loss IC=+0.018 n=58212/40 | gap=+0.046 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.005 n=975 | contrario_BTC IC=-0.007 n=880/40 | gap=-0.002 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.215 > 0.08 con n=121 PNL=+89.35€
  - _Datos_: n=121 IC=+0.215 PNL=+89.35€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=140 PNL=+57.56€
  - _Datos_: n=140 IC=+0.162 PNL=+57.56€

**⏳ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: 25
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: 24/25 ops en el filtro definido (IC actual=+0.269 PNL=+19.70€)
  - _Datos_: n=24 IC=+0.269 PNL=+19.70€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.336 > 0.1 con n=1202 PNL=+626.80€
  - _Datos_: n=1202 IC=+0.336 PNL=+626.80€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=87 IC=+0.039 PNL=+13.95€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=87 IC=+0.039 PNL=+13.95€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=33 IC=+0.186 PNL=+20.93€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=33 IC=+0.186 PNL=+20.93€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=10746 IC=+0.009 PNL=+324.50€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=10746 IC=+0.009 PNL=+324.50€

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
  - _Estado_: n=543 IC=+0.003 PNL=-3.03€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=543 IC=+0.003 PNL=-3.03€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=155 IC=-0.048 PNL=-6.15€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=155 IC=-0.048 PNL=-6.15€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=185 IC=-0.035 PNL=+2.91€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=185 IC=-0.035 PNL=+2.91€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.1 con n=792 PNL=+293.61€
  - _Datos_: n=792 IC=+0.141 PNL=+293.61€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=232 IC=+0.051 PNL=+36.54€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=232 IC=+0.051 PNL=+36.54€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=436 IC=+0.071 PNL=+87.28€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=436 IC=+0.071 PNL=+87.28€

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
  - _Estado_: n=2206 IC=+0.037 PNL=+253.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2206 IC=+0.037 PNL=+253.37€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=54 IC=-0.268 PNL=-10.60€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=54 IC=-0.268 PNL=-10.60€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=113 IC=-0.013 PNL=+8.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=113 IC=-0.013 PNL=+8.43€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=170 IC=+0.029 PNL=+16.61€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=170 IC=+0.029 PNL=+16.61€

**⏳ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: 15
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: 11/15 ops en el filtro definido (IC actual=+0.064 PNL=+1.63€)
  - _Datos_: n=11 IC=+0.064 PNL=+1.63€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2659 IC=-0.016 PNL=-42.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2659 IC=-0.016 PNL=-42.97€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.217 n=44) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=44 IC=+0.217 PNL=+18.24€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=2764 IC=+0.014 PNL=+114.96€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2764 IC=+0.014 PNL=+114.96€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=821 IC=+0.032 PNL=+30.23€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=821 IC=+0.032 PNL=+30.23€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=227 PNL=+68.41€
  - _Datos_: n=227 IC=+0.116 PNL=+68.41€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.08 con n=202 PNL=+22.37€
  - _Datos_: n=202 IC=+0.118 PNL=+22.37€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.137 > 0.08 con n=177 PNL=+68.95€
  - _Datos_: n=177 IC=+0.137 PNL=+68.95€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=27110 IC=+0.102 PNL=+8520.42€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=27110 IC=+0.102 PNL=+8520.42€

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
  - _Estado_: n=1525 IC=+0.034 PNL=+88.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1525 IC=+0.034 PNL=+88.01€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.02 con n=426 PNL=+164.02€
  - _Datos_: n=426 IC=+0.131 PNL=+164.02€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=127 IC=-0.043 PNL=+34.76€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=127 IC=-0.043 PNL=+34.76€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.445 > 0.1 con n=740 PNL=+659.46€
  - _Datos_: n=740 IC=+0.445 PNL=+659.46€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=2858 IC=+0.038 PNL=+276.01€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=2858 IC=+0.038 PNL=+276.01€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.168 > 0.1 con n=1196 PNL=+488.49€
  - _Datos_: n=1196 IC=+0.168 PNL=+488.49€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.194 < -0.1 con n=70 PNL=-0.26€
  - _Datos_: n=70 IC=-0.194 PNL=-0.26€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=740 IC=+0.028 PNL=+75.98€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=740 IC=+0.028 PNL=+75.98€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=32 IC=-0.147 PNL=+4.20€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=32 IC=-0.147 PNL=+4.20€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=140 PNL=+33.32€
  - _Datos_: n=140 IC=+0.113 PNL=+33.32€

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
  - _Estado_: n=8448 IC=-0.139 PNL=+488.46€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8448 IC=-0.139 PNL=+488.46€

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
  - _Estado_: n=1000 IC=+0.145 PNL=+552.23€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1000 IC=+0.145 PNL=+552.23€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.143 > 0.08 con n=754 PNL=+279.24€
  - _Datos_: n=754 IC=+0.143 PNL=+279.24€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=1115 IC=+0.004 PNL=+11.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1115 IC=+0.004 PNL=+11.33€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=1018 PNL=+603.01€
  - _Datos_: n=1018 IC=+0.083 PNL=+603.01€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.170 > 0.08 con n=219 PNL=+87.37€
  - _Datos_: n=219 IC=+0.170 PNL=+87.37€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.234 < -0.1 con n=916 PNL=-100.18€
  - _Datos_: n=916 IC=-0.234 PNL=-100.18€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=2378 IC=+0.142 PNL=+1413.73€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=2378 IC=+0.142 PNL=+1413.73€

**〰️ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: n=50 IC=+0.077 PNL=+10.85€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=50 IC=+0.077 PNL=+10.85€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1002 IC=+0.003 PNL=+122.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1002 IC=+0.003 PNL=+122.40€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.08 con n=918 PNL=+636.52€
  - _Datos_: n=918 IC=+0.187 PNL=+636.52€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1508 IC=-0.058 PNL=+325.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1508 IC=-0.058 PNL=+325.96€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.103 > 0.08 con n=333 PNL=-39.87€
  - _Datos_: n=333 IC=+0.103 PNL=-39.87€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.228 > 0.08 con n=2122 PNL=-217.80€
  - _Datos_: n=2122 IC=+0.228 PNL=-217.80€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 19/40 ops en el filtro definido (IC actual=-0.068 PNL=+3.27€)
  - _Datos_: n=19 IC=-0.068 PNL=+3.27€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.092 n=356) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=356 IC=+0.092 PNL=+84.65€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.312 > 0.08 con n=115 PNL=+57.92€
  - _Datos_: n=115 IC=+0.312 PNL=+57.92€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.422 n=292) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=292 IC=+0.422 PNL=+403.70€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=4846 IC=+0.154 PNL=-727.47€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=4846 IC=+0.154 PNL=-727.47€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.258 > 0.1 con n=64 PNL=+47.91€
  - _Datos_: n=64 IC=+0.258 PNL=+47.91€
