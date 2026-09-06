# Hipótesis automáticas — 2026-09-06 04:09 UTC
_Generado por shadow_postmortem.py sobre 305012 resoluciones (PNL=+29750.03€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.705` → IC=-0.133 (n=148)

  - _Acción_: SKIP cuando `py_entrada` < 0.705
  - _Potencial_: sin este filtro IC_bueno=+0.268 (n=325)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.392 (n=81)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=335)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.268 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.142)

- **PATRÓN** `n_ballena_banda` > `20.0` → IC=+0.142 (n=319)

  - _Acción_: Kelly boost +0.71€ cuando `n_ballena_banda` > 20.0 (IC base=+0.142)

- **PATRÓN** `n_total_lado` > `72.0` → IC=+0.248 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 72.0 (IC base=+0.142)

- **PATRÓN** `banda_hit_calibrado` > `0.6166` → IC=+0.234 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6166 (IC base=+0.142)

- **PATRÓN** `banda_z` > `11.542` → IC=+0.277 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.542 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=369)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3120.8362` → IC=+0.175 (n=161)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3120.8362 (IC base=+0.142)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.129 (n=335)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.5 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 92.0 (IC base=+0.026)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=205)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=230)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.265 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.167)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.243 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.167)

- **PATRÓN** `banda_hit_calibrado` > `0.6176` → IC=+0.258 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6176 (IC base=+0.167)

- **PATRÓN** `banda_z` > `11.552` → IC=+0.273 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.552 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.203 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=289)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2945.0699` → IC=+0.172 (n=172)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2945.0699 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.465` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.465 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 92.0 (IC base=+0.017)

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
- **FILTRO** `restante_s_al_confirmar` < `147.73` → IC=-0.299 (n=4059)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 147.73
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=12179)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `133.8` → IC=-0.325 (n=552)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.8
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1657)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` > `629.69` → IC=-0.165 (n=341)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` > 629.69
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=662)

- **FILTRO** `restante_s_al_confirmar` < `466.2` → IC=-0.167 (n=250)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 466.2
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=753)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `119.1` → IC=-0.397 (n=534)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 119.1
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=1602)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `157.1` → IC=-0.159 (n=1073)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.1
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3230)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `145.71` → IC=-0.312 (n=910)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.71
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=2730)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `160.67` → IC=-0.370 (n=972)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 160.67
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=1975)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.192 (n=8459)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.7 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=2178)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2361.0666` → IC=+0.162 (n=2091)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2361.0666 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=6120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=7238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.253 (n=5367)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=4172)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1936.8072` → IC=+0.172 (n=3575)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1936.8072 (IC base=+0.138)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=957)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.373 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `12941.1293` → IC=+0.219 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12941.1293 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=988)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.288 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=1264)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `12407.3262` → IC=+0.204 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12407.3262 (IC base=+0.192)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.177 (n=224)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `4800.0243` → IC=+0.151 (n=216)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4800.0243 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=225)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.179 (n=350)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.41 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4037.3082` → IC=+0.158 (n=334)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4037.3082 (IC base=+0.131)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=1488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.69` → IC=+0.311 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.260 (n=686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.251 (n=788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` < `0.205` → IC=+0.393 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.205 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.255 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1921.0402` → IC=+0.266 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1921.0402 (IC base=+0.251)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=366)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.66` → IC=+0.261 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.66 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=489)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1752.2689` → IC=+0.153 (n=364)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1752.2689 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4449.086 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.213 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.84` → IC=+0.425 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.84 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.198 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 7.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.340 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1987.7285` → IC=+0.198 (n=379)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1987.7285 (IC base=+0.194)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.332 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=175)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3435.4625` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3435.4625 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=560)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.227 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=300)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **FILTRO** `libro_liquidez` < `11360.7096` → IC=-0.266 (n=143)

  - _Acción_: SKIP cuando `libro_liquidez` < 11360.7096
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=48)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=6656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=5643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.205 (n=3213)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.313 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `6228.1216` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6228.1216 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=1450)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=1708)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.74 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.421 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.338 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `5642.183` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5642.183 (IC base=+0.307)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=1686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=1420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.176 (n=1706)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.173)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.186 (n=1143)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.72 (IC base=+0.173)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.246 (n=1507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.238 (n=1282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.315 (n=543)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=1390)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.190 (n=843)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.7 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.187 (n=704)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.73 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.448 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.444 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.481 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.439 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `8027.017` → IC=+0.454 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8027.017 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.440 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.450 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `10987.7492` → IC=+0.464 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10987.7492 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.450 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.452 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `2350.8723` → IC=+0.446 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2350.8723 (IC base=+0.439)

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
- **FILTRO** `py_entrada` > `0.775` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `libro_liquidez` < `6196.1698` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 6196.1698
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.194 (n=18902)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=8073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.210 (n=19301)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=3915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.157 (n=2671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 12.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.178 (n=3363)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.71 (IC base=+0.154)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=1657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.228 (n=1246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.277 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.181 (n=1219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 18.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.168 (n=2570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 12.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3356)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.167)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=1701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.230 (n=1267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=1210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.215 (n=1159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.241 (n=1634)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.187 (n=3174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=2508)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.233 (n=1623)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=2742)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.129)

- **PATRÓN** `restante_min` < `4.0` → IC=+0.138 (n=2549)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 4.0 (IC base=+0.129)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.156 (n=2571)

  - _Acción_: Kelly boost +0.78€ cuando `restante_min` > 4.94 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.143 (n=3758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 8.0 (IC base=+0.129)

- **PATRÓN** `lag_apertura_s` < `3.81` → IC=+0.156 (n=2549)

  - _Acción_: Kelly boost +0.78€ cuando `lag_apertura_s` < 3.81 (IC base=+0.129)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.213 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.135)

- **PATRÓN** `restante_min` < `3.95` → IC=+0.143 (n=1266)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` < 3.95 (IC base=+0.135)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.150 (n=1759)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.88 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.151 (n=2676)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 12.0 (IC base=+0.135)

- **PATRÓN** `lag_apertura_s` < `6.86` → IC=+0.149 (n=1663)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 6.86 (IC base=+0.135)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.123)

- **PATRÓN** `restante_min` < `4.44` → IC=+0.127 (n=1703)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.44 (IC base=+0.123)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.165 (n=1301)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` > 4.95 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.126 (n=1488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=1703)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.165 (n=1290)

  - _Acción_: Kelly boost +0.82€ cuando `lag_apertura_s` < 3.28 (IC base=+0.123)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1729.4046` → IC=+0.296 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1729.4046 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.285 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.347 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5464.0706` → IC=+0.293 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5464.0706 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.340 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.375 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `1704.9114` → IC=+0.319 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1704.9114 (IC base=+0.297)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.429 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.429 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.434 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.425 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `1957.89` → IC=+0.432 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1957.89 (IC base=+0.423)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.434 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.419)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.419)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.425 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.419)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.429 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.419)

- **PATRÓN** `libro_liquidez` > `5433.9622` → IC=+0.461 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5433.9622 (IC base=+0.419)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.436 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.430 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.429 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `1934.5002` → IC=+0.452 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.5002 (IC base=+0.427)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.372)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.372)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.408 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.273 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `958.8537` → IC=+0.268 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 958.8537 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.865` → IC=+0.408 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.865 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.273 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `958.8537` → IC=+0.268 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 958.8537 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9516` → IC=+0.211 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9516 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.4477` → IC=+0.227 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4477 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.714` → IC=+0.155 (n=1564)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 5.714 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.231 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.242 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2521` → IC=+0.194 (n=501)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2521 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.8733` → IC=+0.182 (n=2502)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.8733 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `1.4722` → IC=+0.180 (n=2502)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4722 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.4025` → IC=+0.126 (n=3879)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.4025 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1307` → IC=+0.144 (n=1275)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1307 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.6867` → IC=+0.146 (n=617)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6867 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.0473` → IC=+0.143 (n=636)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.0473 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.3022` → IC=+0.234 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3022 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.9336` → IC=+0.195 (n=1474)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.9336 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.214 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.040)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.197 (n=308)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0076 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2961` → IC=+0.167 (n=917)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2961 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.204 (n=440)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.666` → IC=+0.284 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.666 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.242 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `2.6736` → IC=+0.151 (n=820)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.6736 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.442` → IC=+0.154 (n=819)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.442 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=778)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.191 (n=499)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 57.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.245 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.253 (n=568)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1827` → IC=+0.286 (n=424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1827 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.246 (n=635)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.4091` → IC=+0.274 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4091 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.548` → IC=+0.241 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.548 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.37` → IC=+0.258 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.37 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0697` → IC=+0.236 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0697 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.8655` → IC=+0.291 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8655 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.261 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1718.2348` → IC=+0.258 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1718.2348 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.238 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 66.0 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.249 (n=237)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.223 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.1996` → IC=+0.234 (n=472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1996 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=711)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.3717` → IC=+0.225 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3717 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.8223` → IC=+0.221 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8223 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.444` → IC=+0.216 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.444 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.217` → IC=+0.225 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.217 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2518` → IC=+0.218 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2518 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `1.0855` → IC=+0.228 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0855 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0971` → IC=+0.216 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0971 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4797` → IC=+0.246 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4797 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `11817.8916` → IC=+0.243 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11817.8916 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.152 (n=765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.006 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.150 (n=683)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0029 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.078` → IC=+0.162 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.078 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.146 (n=544)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 12.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6614` → IC=+0.171 (n=764)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6614 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1336` → IC=+0.169 (n=651)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1336 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.553` → IC=+0.222 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.553 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.6788` → IC=+0.163 (n=336)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6788 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1504` → IC=+0.218 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1504 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.7252` → IC=+0.166 (n=438)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.7252 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4046` → IC=+0.160 (n=656)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4046 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `12569.7182` → IC=+0.152 (n=509)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12569.7182 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.174 (n=191)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 213.0 (IC base=+0.144)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.196 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0097 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.205 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.248 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.351` → IC=+0.267 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.351 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` < `0.1042` → IC=+0.164 (n=721)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.1042 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.3831` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.3831 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `3.7458` → IC=+0.162 (n=787)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 3.7458 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.8863` → IC=+0.181 (n=703)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8863 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=929)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.193 (n=558)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 48.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.229 (n=725)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.220 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.238 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.228 (n=336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.0268` → IC=+0.279 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0268 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.986` → IC=+0.237 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.986 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.22` → IC=+0.222 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.22 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3726` → IC=+0.306 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3726 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.6975` → IC=+0.200 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6975 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3963` → IC=+0.212 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3963 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.234 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.206 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.220)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `ibs_20min` > `0.816` → IC=-0.182 (n=309)

  - _Acción_: SKIP cuando `ibs_20min` > 0.816
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=935)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.149 (n=72)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1172)

- **PATRÓN** `dist_vwap_pct` < `0.5765` → IC=+0.320 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5765 (IC base=-0.024)

- **PATRÓN** `volumen_regimen` < `0.5993` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5993 (IC base=-0.024)

- **PATRÓN** `volumen_regimen` > `1.1956` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1956 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.114` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.114 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4292` → IC=+0.379 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4292 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.9064` → IC=+0.297 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9064 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1427` → IC=+0.148 (n=89)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1427 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.8136` → IC=+0.135 (n=157)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8136 (IC base=-0.040)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=161)

- **FILTRO** `ibs_20min` < `0.3111` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3111
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=135)

- **FILTRO** `sigma_ewma_delta_pct` > `8.412` → IC=-0.187 (n=215)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.412
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=1666)

- **FILTRO** `volumen_pendiente_norm` < `0.1129` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.1129
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=29)

- **FILTRO** `volumen_spike_ratio` > `1.524` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.524
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=27)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.179 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0056 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.3111` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.3111 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.6887` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6887 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` < `0.9699` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9699 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `0.7836` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7836 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.8428` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8428 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.5596` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5596 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1129` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1129 (IC base=-0.062)

- **PATRÓN** `volumen_spike_ratio` < `1.524` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.524 (IC base=-0.062)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.5031` → IC=-0.160 (n=386)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5031
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=750)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.179 (n=166)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=970)

- **FILTRO** `ibs_20min` > `0.7902` → IC=-0.193 (n=450)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7902
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1351)

- **FILTRO** `sigma_ewma_delta_pct` > `8.935` → IC=-0.135 (n=206)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.935
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1595)

- **PATRÓN** `dist_vwap_pct` > `0.6657` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6657 (IC base=-0.094)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.229 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2288 (IC base=-0.094)

- **PATRÓN** `volumen_regimen` > `0.6895` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6895 (IC base=-0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.0665` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0665 (IC base=-0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.5219` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5219 (IC base=-0.094)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1546` → IC=+0.201 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1546 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` < `0.231` → IC=+0.209 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.231 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` > `1.0971` → IC=+0.283 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0971 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2549` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2549 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.3135` → IC=+0.207 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3135 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` > `1.5056` → IC=+0.177 (n=156)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.5056 (IC base=-0.046)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.198 (n=104)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 22.0 (IC base=-0.046)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.164 (n=2297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0078 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.4476` → IC=+0.169 (n=4520)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.4476 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `1.1688` → IC=+0.293 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1688 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.48` → IC=+0.123 (n=2683)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.48 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `0.68` → IC=+0.224 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.68 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.251` → IC=+0.251 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.251 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `1.4899` → IC=+0.234 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4899 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `2.8083` → IC=+0.225 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8083 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.293 (n=2033)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.5853` → IC=+0.128 (n=4830)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5853 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.7601` → IC=+0.247 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7601 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.2212` → IC=+0.220 (n=1176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2212 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.7061` → IC=+0.221 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7061 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` > `1.2196` → IC=+0.241 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2196 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2573` → IC=+0.334 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2573 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` > `2.8406` → IC=+0.259 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8406 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.253 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.051)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3333` → IC=-0.140 (n=423)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3333
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=866)

- **FILTRO** `sigma_ewma_delta_pct` > `2.485` → IC=-0.162 (n=380)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.485
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=837)

- **PATRÓN** `ibs_20min` > `0.8469` → IC=+0.251 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8469 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.771` → IC=+0.161 (n=343)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.771 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2213` → IC=+0.303 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2213 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.8884` → IC=+0.246 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8884 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `1.4729` → IC=+0.220 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4729 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.318 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.038)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8608` → IC=-0.156 (n=411)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8608
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1241)

- **PATRÓN** `volumen_spike_ratio` < `1.7086` → IC=+0.136 (n=256)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.7086 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `290.0` → IC=+0.142 (n=163)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 290.0 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.188 (n=206)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1366 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` < `0.5828` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.5828 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` > `1.1253` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1253 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2511` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2511 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.0293` → IC=+0.205 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0293 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.185 (n=163)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4236 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `263.0` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 263.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.276 (n=546)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.235 (n=274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.258 (n=395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.259 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.365` → IC=+0.296 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.365 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.239 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `2.3907` → IC=+0.237 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3907 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `1.7204` → IC=+0.236 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7204 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.311 (n=537)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.316 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.287)

- **PATRÓN** `ibs_20min` < `0.3558` → IC=+0.302 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3558 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.516` → IC=+0.319 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.516 (IC base=+0.287)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` < `3.4433` → IC=+0.282 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.4433 (IC base=+0.287)

- **PATRÓN** `volumen_spike_ratio` > `2.3329` → IC=+0.294 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3329 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.301 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1846.3` → IC=+0.287 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1846.3 (IC base=+0.287)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.144 (n=254)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=577)

- **FILTRO** `ibs_20min` < `0.5835` → IC=-0.162 (n=415)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5835
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=416)

- **FILTRO** `ibs_20min` > `0.8648` → IC=-0.159 (n=321)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8648
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=964)

- **FILTRO** `volumen_regimen` > `0.8624` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8624
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=51)

- **FILTRO** `volumen_regimen` < `0.6983` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.6983
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=51)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=84)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=1201)

- **PATRÓN** `dist_vwap_pct` > `1.3501` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3501 (IC base=-0.049)

- **PATRÓN** `volumen_regimen` < `0.8912` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8912 (IC base=-0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=-0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.2544` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2544 (IC base=-0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.3713` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3713 (IC base=-0.049)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.262 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=-0.049)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6` → IC=-0.198 (n=550)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.229 (n=552)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.233 (n=305)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=929)

- **FILTRO** `sigma_ewma_delta_pct` > `4.678` → IC=-0.145 (n=308)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.678
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=926)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.229 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.2099` → IC=+0.305 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2099 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` < `0.8684` → IC=+0.270 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8684 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` > `1.1763` → IC=+0.292 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1763 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` < `0.116` → IC=+0.261 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.116 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.2247` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2247 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.302 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.3531` → IC=+0.276 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3531 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.313 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` < `1.0698` → IC=+0.141 (n=126)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0698 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2394` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2394 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.6907` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.6907 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 61.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.336 (n=528)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.265 (n=377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` > `0.898` → IC=+0.328 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.898 (IC base=+0.257)

- **PATRÓN** `dist_vwap_pct` > `0.1699` → IC=+0.315 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1699 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.201` → IC=+0.289 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.201 (IC base=+0.257)

- **PATRÓN** `volumen_regimen` > `0.839` → IC=+0.296 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.839 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.292 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `2.5673` → IC=+0.264 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5673 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `1.8308` → IC=+0.261 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8308 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.260 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `2448.2154` → IC=+0.257 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2448.2154 (IC base=+0.257)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.282 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.273)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.296 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.273)

- **PATRÓN** `drift_60min` |x|≤ `0.3085` → IC=+0.273 (n=566)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3085 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.281 (n=806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.311 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `0.5366` → IC=+0.289 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5366 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.2763` → IC=+0.273 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2763 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.402` → IC=+0.295 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.402 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `1.2589` → IC=+0.307 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2589 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.371 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `1.4345` → IC=+0.264 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4345 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `2.1862` → IC=+0.285 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1862 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `2543.9918` → IC=+0.273 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2543.9918 (IC base=+0.273)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.268 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.273)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.205 (n=1417)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3392` → IC=+0.171 (n=3741)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3392 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=4472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.224 (n=3800)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `1.0939` → IC=+0.232 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0939 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.14` → IC=+0.251 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.14 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.226` → IC=+0.156 (n=2866)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.226 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.6308` → IC=+0.161 (n=2867)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6308 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1053` → IC=+0.189 (n=1612)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1053 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `2.311` → IC=+0.165 (n=3502)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.311 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3887.2465` → IC=+0.173 (n=1417)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3887.2465 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.182 (n=3162)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 139.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.178 (n=3465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0083 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0783` → IC=+0.201 (n=1312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0783 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=1900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4426` → IC=+0.221 (n=3935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4426 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.163 (n=2923)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.102` → IC=+0.203 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.102 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1727` → IC=+0.160 (n=2941)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1727 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.153 (n=2941)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6226 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.243 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6561` → IC=+0.188 (n=1102)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6561 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.164 (n=2895)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 149.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.191 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0057 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.211 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3045` → IC=+0.206 (n=712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3045 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.222 (n=515)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.602` → IC=+0.299 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.602 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.267 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.6388` → IC=+0.175 (n=629)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.6388 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4556` → IC=+0.173 (n=629)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.4556 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.200 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.254 (n=412)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1701` → IC=+0.306 (n=307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1701 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.246 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.2702` → IC=+0.259 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2702 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.002` → IC=+0.237 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.002 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.0683` → IC=+0.218 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0683 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.4356` → IC=+0.229 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4356 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.791` → IC=+0.242 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.791 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.255 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1701.1448` → IC=+0.257 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1701.1448 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.217 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 75.0 (IC base=+0.226)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.229 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.2857` → IC=+0.169 (n=547)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2857 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.212 (n=432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4666` → IC=+0.208 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4666 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2601` → IC=+0.225 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2601 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.787` → IC=+0.236 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.787 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6419` → IC=+0.176 (n=208)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6419 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0799` → IC=+0.176 (n=282)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0799 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.1644` → IC=+0.189 (n=194)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1644 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.3944` → IC=+0.205 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3944 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `11188.0133` → IC=+0.191 (n=555)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11188.0133 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.180 (n=707)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.006 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.059` → IC=+0.210 (n=236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.059 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.4911` → IC=+0.193 (n=707)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.4911 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.3171` → IC=+0.169 (n=756)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3171 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.321` → IC=+0.235 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.321 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.6918` → IC=+0.216 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6918 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.211 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.7277` → IC=+0.157 (n=400)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.7277 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.3973` → IC=+0.164 (n=599)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.3973 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=913)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `15612.642` → IC=+0.160 (n=236)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 15612.642 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `241.0` → IC=+0.159 (n=171)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 241.0 (IC base=+0.156)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.209 (n=225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.1811` → IC=+0.196 (n=449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1811 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.189 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.193 (n=311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.569` → IC=+0.304 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.569 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.1328` → IC=+0.194 (n=256)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1328 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.896` → IC=+0.178 (n=545)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.896 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.232 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.218 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.2226` → IC=+0.230 (n=357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2226 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.242 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3647` → IC=+0.251 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3647 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.704` → IC=+0.258 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.704 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3671` → IC=+0.282 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3671 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.9009` → IC=+0.211 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.9009 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3473` → IC=+0.211 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3473 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1858.5555` → IC=+0.218 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1858.5555 (IC base=+0.217)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.193 (n=568)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.179 (n=216)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.4315` → IC=+0.199 (n=645)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4315 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1493` → IC=+0.180 (n=455)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1493 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.408` → IC=+0.264 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.408 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8895` → IC=+0.156 (n=431)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8895 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.2177` → IC=+0.191 (n=215)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 1.2177 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.225 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.435` → IC=+0.151 (n=210)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.435 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6185` → IC=+0.184 (n=210)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6185 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=721)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `8688.9164` → IC=+0.194 (n=430)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 8688.9164 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.148 (n=390)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 135.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.147 (n=697)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0075 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3745` → IC=+0.138 (n=697)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3745 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.174 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.3954` → IC=+0.191 (n=613)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.3954 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.6073` → IC=+0.134 (n=810)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.6073 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.385` → IC=+0.217 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.385 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1618` → IC=+0.131 (n=697)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1618 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.129 (n=696)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6129 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.1018` → IC=+0.175 (n=238)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1018 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.5407` → IC=+0.141 (n=260)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5407 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `5188.5595` → IC=+0.133 (n=464)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 5188.5595 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.189 (n=268)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0118 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.5294` → IC=+0.191 (n=804)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5294 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.1246` → IC=+0.238 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1246 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.264 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.6339` → IC=+0.120 (n=804)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` > 0.6339 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2465.0939` → IC=+0.175 (n=536)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2465.0939 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.139 (n=541)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 51.0 (IC base=+0.113)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.149 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0105 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.0982` → IC=+0.144 (n=245)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.0982 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.4744` → IC=+0.209 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4744 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0295` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 1.0295 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.1817` → IC=+0.135 (n=644)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1817 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.296` → IC=+0.149 (n=297)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.296 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.135 (n=730)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.1954 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2724` → IC=+0.202 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2724 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.127 (n=199)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.3913` → IC=+0.175 (n=198)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.3913 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3156.1484` → IC=+0.165 (n=243)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3156.1484 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.217 (n=531)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1669` → IC=+0.220 (n=351)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1669 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.7277` → IC=+0.247 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7277 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.2613` → IC=+0.227 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2613 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.182` → IC=+0.242 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.182 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.2022` → IC=+0.193 (n=796)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2022 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `0.8431` → IC=+0.221 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8431 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.0832` → IC=+0.251 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0832 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `2.5276` → IC=+0.211 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5276 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.196 (n=874)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.02 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.262 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0901` → IC=+0.221 (n=270)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0901 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.213 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.425` → IC=+0.245 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.425 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.2521` → IC=+0.206 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2521 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.893` → IC=+0.239 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.893 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.6912` → IC=+0.228 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6912 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.321 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.658` → IC=+0.202 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.658 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2502.0176` → IC=+0.208 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2502.0176 (IC base=+0.202)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.171 (n=308)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0092 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.166 (n=872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.4315` → IC=+0.167 (n=923)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.4315 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.9406` → IC=+0.214 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9406 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.673` → IC=+0.169 (n=427)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.673 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.155 (n=499)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8709 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.1833` → IC=+0.161 (n=249)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1833 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1708` → IC=+0.179 (n=257)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1708 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4513` → IC=+0.148 (n=291)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4513 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5563` → IC=+0.143 (n=776)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.5563 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=970)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `9633.393` → IC=+0.174 (n=308)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 9633.393 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.170 (n=237)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.3158` → IC=+0.123 (n=621)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.3158 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.144` → IC=+0.129 (n=192)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 8.144 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.1733` → IC=+0.155 (n=233)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1733 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.149 (n=263)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 16.0 (IC base=+0.075)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.004` → IC=+0.137 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.004 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.150 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 9.0 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.5605` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.5605 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.8205` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8205 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.537` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.537 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.6919` → IC=+0.153 (n=73)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6919 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `8533.3968` → IC=+0.149 (n=166)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 8533.3968 (IC base=+0.087)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.154 (n=105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0028 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.6346` → IC=+0.158 (n=276)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.6346 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.213` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.213 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.194 (n=83)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 146.0 (IC base=+0.083)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.263 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.309 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` > `0.7468` → IC=+0.295 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7468 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` > `0.154` → IC=+0.275 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.154 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` < `0.2332` → IC=+0.260 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2332 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.681` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.681 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` < `0.8266` → IC=+0.267 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8266 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.352 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.4732` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4732 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.261 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.259)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` < `0.5806` → IC=-0.172 (n=62)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5806
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=186)

- **FILTRO** `ibs_20min` > `0.4146` → IC=-0.214 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4146
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.2281` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2281
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=139)

- **FILTRO** `volumen_pendiente_norm` > `0.2176` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.2176
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=121)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.156 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 14.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` > `0.8462` → IC=+0.175 (n=124)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8462 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.024)

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
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.200 (n=2340)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=5407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4839` → IC=+0.211 (n=5157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4839 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `1.0375` → IC=+0.220 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0375 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.463` → IC=+0.226 (n=2579)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.463 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.887` → IC=+0.159 (n=2367)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.887 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.1681` → IC=+0.196 (n=1414)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1681 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `1.8757` → IC=+0.172 (n=3216)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8757 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.165 (n=4810)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3787.3248` → IC=+0.181 (n=1719)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3787.3248 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.209 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.190 (n=4691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0109 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.4769` → IC=+0.189 (n=4692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.4769 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=2283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=2126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.235 (n=4692)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2337` → IC=+0.168 (n=2902)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.2337 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.723` → IC=+0.209 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.723 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.716` → IC=+0.184 (n=4357)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.716 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6225` → IC=+0.166 (n=1101)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6225 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `1.193` → IC=+0.162 (n=1099)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.193 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.237` → IC=+0.244 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.237 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.305` → IC=+0.194 (n=1805)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.305 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `138.0` → IC=+0.175 (n=3564)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 138.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.197 (n=285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0052 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.240 (n=387)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=568)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.905` → IC=+0.313 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.905 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2282` → IC=+0.274 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2282 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.469` → IC=+0.202 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.469 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.3008` → IC=+0.183 (n=348)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.3008 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.245 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.263 (n=564)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.261 (n=641)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.192` → IC=+0.290 (n=427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.192 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.263 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.4158` → IC=+0.296 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4158 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.577` → IC=+0.271 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.577 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2987` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2987 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.4258` → IC=+0.309 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4258 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1506.64` → IC=+0.265 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1506.64 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.268 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.256)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.190 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0029 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.156 (n=280)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0067 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.4508` → IC=+0.208 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4508 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.213` → IC=+0.201 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.213 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.757` → IC=+0.180 (n=201)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.757 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.322` → IC=+0.163 (n=731)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 4.322 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2659` → IC=+0.162 (n=836)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2659 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1002` → IC=+0.156 (n=379)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1002 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.166 (n=708)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1485` → IC=+0.191 (n=228)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1485 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.3936` → IC=+0.169 (n=786)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.3936 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.7292` → IC=+0.173 (n=524)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.7292 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `10405.5061` → IC=+0.182 (n=747)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 10405.5061 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `511.0` → IC=+0.168 (n=712)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 511.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.178 (n=749)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0061 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.170 (n=671)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0029 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.2635` → IC=+0.183 (n=658)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.2635 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.171 (n=778)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 18.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.6253` → IC=+0.208 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6253 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.135` → IC=+0.186 (n=651)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.135 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.892` → IC=+0.215 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.892 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.6156` → IC=+0.218 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6156 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.086` → IC=+0.225 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.086 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.3241` → IC=+0.184 (n=651)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.3241 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.0527` → IC=+0.190 (n=295)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.0527 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=965)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `289.0` → IC=+0.190 (n=185)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 289.0 (IC base=+0.167)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.232 (n=505)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.249 (n=364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.6809` → IC=+0.257 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6809 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.609` → IC=+0.331 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.609 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.219` → IC=+0.212 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.219 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `2.4267` → IC=+0.207 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4267 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.7115` → IC=+0.207 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7115 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1462.3784` → IC=+0.214 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1462.3784 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.249 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.264 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.238 (n=342)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.251 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.3973` → IC=+0.275 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3973 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.556` → IC=+0.280 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.556 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3568` → IC=+0.294 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3568 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `3.0442` → IC=+0.229 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0442 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `1.9003` → IC=+0.217 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9003 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.205 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.156 (n=757)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0069 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.156 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.7314` → IC=+0.238 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7314 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3633` → IC=+0.186 (n=342)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3633 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.313` → IC=+0.168 (n=381)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.313 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8969` → IC=+0.167 (n=571)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8969 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.2062` → IC=+0.146 (n=286)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.2062 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.233 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1479` → IC=+0.183 (n=370)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.1479 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=933)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `9500.4052` → IC=+0.236 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9500.4052 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.165 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0032 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.4348` → IC=+0.138 (n=667)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4348 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=297)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6809` → IC=+0.170 (n=667)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6809 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.6744` → IC=+0.134 (n=741)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.6744 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.341` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.341 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.0179` → IC=+0.123 (n=587)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.0179 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `1.1432` → IC=+0.136 (n=223)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.1432 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.8208` → IC=+0.142 (n=403)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8208 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `9441.0647` → IC=+0.169 (n=303)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 9441.0647 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `190.0` → IC=+0.133 (n=518)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 190.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.140 (n=603)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0078 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.142 (n=454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.179 (n=906)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4706 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `1.0924` → IC=+0.182 (n=174)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 1.0924 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.414` → IC=+0.220 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.414 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=632)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2933.8625` → IC=+0.260 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2933.8625 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.135 (n=681)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 63.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.180 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1269` → IC=+0.184 (n=280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1269 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.148 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5862` → IC=+0.194 (n=841)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5862 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.5012` → IC=+0.136 (n=805)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.5012 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.263` → IC=+0.125 (n=814)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.263 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.148 (n=370)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.7144 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.175 (n=290)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.144 (n=304)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.1793` → IC=+0.129 (n=313)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.1793 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2624.9762` → IC=+0.147 (n=381)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2624.9762 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0278` → IC=+0.235 (n=319)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0278 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.204 (n=844)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1701` → IC=+0.249 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1701 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.827` → IC=+0.264 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.827 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.6932` → IC=+0.211 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6932 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.248 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.828` → IC=+0.212 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.828 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.209 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.276 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.227 (n=349)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.6467` → IC=+0.206 (n=1045)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6467 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=986)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.211 (n=1098)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.258 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.1792` → IC=+0.210 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1792 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.357` → IC=+0.270 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.357 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.221 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.282 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4555` → IC=+0.197 (n=869)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4555 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.186 (n=763)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 35.0 (IC base=+0.206)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=1821)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.135 (n=1487)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0103 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.556` → IC=+0.131 (n=1687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.556 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.169 (n=578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.193 (n=564)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.9286 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.379` → IC=+0.147 (n=267)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.379 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.1729` → IC=+0.155 (n=471)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1729 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4629` → IC=+0.140 (n=557)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4629 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.8953` → IC=+0.143 (n=1114)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8953 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `8548.2725` → IC=+0.132 (n=765)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 8548.2725 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.175 (n=460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0039 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4997` → IC=+0.147 (n=1378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4997 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.155 (n=467)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.1963` → IC=+0.150 (n=606)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1963 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.9977` → IC=+0.132 (n=180)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.9977 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.342` → IC=+0.137 (n=1368)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 6.342 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.0954` → IC=+0.140 (n=1154)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0954 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1496` → IC=+0.128 (n=1378)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1496 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.149 (n=651)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `2.4942` → IC=+0.136 (n=1363)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.4942 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.8045` → IC=+0.136 (n=908)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.8045 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=1821)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7727.9509` → IC=+0.134 (n=1231)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7727.9509 (IC base=+0.127)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `3.294` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.294
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=199)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.156 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 19.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.7517` → IC=+0.122 (n=146)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.7517 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.294` → IC=+0.132 (n=199)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.294 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `0.9417` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.9417 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.3696` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.3696 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `12574.1361` → IC=+0.147 (n=148)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 12574.1361 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.183 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.143 (n=211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.1703` → IC=+0.157 (n=278)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1703 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.6417` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6417 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.379` → IC=+0.138 (n=625)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 6.379 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.1896` → IC=+0.129 (n=631)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1896 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.0641` → IC=+0.155 (n=297)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0641 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4049` → IC=+0.141 (n=210)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4049 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `11132.7025` → IC=+0.123 (n=630)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 11132.7025 (IC base=+0.113)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.210 (n=143)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.180 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0106 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.2953` → IC=+0.166 (n=285)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2953 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.988` → IC=+0.231 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.988 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.26` → IC=+0.223 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.26 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2112` → IC=+0.186 (n=119)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2112 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `3.4971` → IC=+0.166 (n=426)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.4971 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.8333` → IC=+0.160 (n=380)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8333 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `2303.4734` → IC=+0.190 (n=143)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2303.4734 (IC base=+0.155)

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
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.148 (n=572)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0089 (IC base=+0.132)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.132 (n=572)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0046 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.4724` → IC=+0.146 (n=572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4724 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.195 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.185` → IC=+0.145 (n=572)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.185 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `1.036` → IC=+0.172 (n=129)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 1.036 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.4258` → IC=+0.138 (n=540)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.4258 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.989` → IC=+0.141 (n=575)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.989 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.1165` → IC=+0.145 (n=503)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1165 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.0834` → IC=+0.146 (n=255)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0834 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.168 (n=188)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=496)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8958.3045` → IC=+0.147 (n=511)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 8958.3045 (IC base=+0.132)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.169 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0088 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.5171` → IC=+0.194 (n=426)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.5171 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.162 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 10.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.1076` → IC=+0.164 (n=426)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.1076 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.7273` → IC=+0.158 (n=472)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.7273 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.986` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.986 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.171 (n=426)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2227 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.7338` → IC=+0.152 (n=380)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7338 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.1472` → IC=+0.155 (n=433)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.1472 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0698` → IC=+0.167 (n=187)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0698 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1713` → IC=+0.172 (n=367)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1713 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.168 (n=417)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `8169.7182` → IC=+0.164 (n=426)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 8169.7182 (IC base=+0.150)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `ibs_20min` < `0.4545` → IC=-0.177 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4545
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=88)

- **FILTRO** `dist_vwap_pct` < `0.7269` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.7269
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=28)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.247` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.247 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.008)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `0.6404` → IC=-0.164 (n=102)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6404
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=309)

- **FILTRO** `sigma_h` > `0.0099` → IC=-0.286 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=206)

- **FILTRO** `ibs_20min` > `0.0952` → IC=-0.123 (n=128)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0952
  - _Potencial_: sin este filtro IC_bueno=+0.217 (n=44)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.185 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0054 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.154 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.211 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.8416` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.8416 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` < `0.212` → IC=+0.123 (n=245)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.212 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.236 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `0.8192` → IC=+0.144 (n=206)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8192 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2766` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2766 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` < `2.0004` → IC=+0.161 (n=184)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.0004 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` > `1.4935` → IC=+0.151 (n=187)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4935 (IC base=+0.091)

- **PATRÓN** `libro_spread` < `0.023` → IC=+0.152 (n=251)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.023 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `1064.9876` → IC=+0.156 (n=254)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1064.9876 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.0952` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0952 (IC base=-0.112)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.225 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.160 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.7892` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7892 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.414` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.414 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.8665` → IC=+0.162 (n=69)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8665 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.1478` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1478 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `2.2665` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2665 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `1.4853` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4853 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.0945` → IC=+0.136 (n=31)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.0945 (IC base=-0.032)

- **PATRÓN** `ibs_20min` < `0.1923` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1923 (IC base=-0.032)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6789` → IC=-0.143 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6789
  - _Potencial_: sin este filtro IC_bueno=+0.263 (n=112)

- **FILTRO** `sigma_h` > `0.0071` → IC=-0.370 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=67)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.227 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=46)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.164 (n=105)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.005 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.139 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 15.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.6789` → IC=+0.263 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6789 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4909` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4909 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.1621` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1621 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.55` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.55 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.791 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.2901` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2901 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `1.4589` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4589 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=130)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `1230.6413` → IC=+0.209 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1230.6413 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.1005` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1005 (IC base=-0.111)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` < `0.6744` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6744
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=81)

- **FILTRO** `sigma_h` > `0.0156` → IC=-0.333 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0156
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=72)

- **FILTRO** `ibs_20min` > `0.1111` → IC=-0.300 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1111
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.6744 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.9891` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.9891 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.0856` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0856 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.3495` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.3495 (IC base=+0.047)

- **PATRÓN** `libro_liquidez` > `376.737` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 376.737 (IC base=+0.047)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1905` → IC=-0.362 (n=27)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1905
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=83)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.466 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=85)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=96)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=97)

- **FILTRO** `sigma_ewma_delta_pct` > `3.662` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.662
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=63)

- **FILTRO** `volumen_spike_ratio` > `1.721` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.721
  - _Potencial_: sin este filtro IC_bueno=-0.333 (n=16)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0036` → IC=-0.250 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `ibs_20min` < `0.5407` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5407
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

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
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.463 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
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

- **FILTRO** `sigma_h` < `0.0065` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `volumen_regimen` < `1.1715` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1715
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` < `0.6331` → IC=-0.246 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6331
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=174)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.25 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.672` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 5.672 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.0687` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.0687 (IC base=+0.050)

- **PATRÓN** `libro_liquidez` > `2868.4937` → IC=+0.129 (n=114)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2868.4937 (IC base=+0.050)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=36)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7917 (IC base=+0.068)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.149 (n=186)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2605.1459` → IC=+0.156 (n=161)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2605.1459 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2229.0754` → IC=+0.129 (n=278)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2229.0754 (IC base=+0.097)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.149 (n=186)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2605.1459` → IC=+0.156 (n=161)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2605.1459 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2229.0754` → IC=+0.129 (n=278)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2229.0754 (IC base=+0.097)

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
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1101)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=48)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=91)

- **FILTRO** `libro_liquidez` < `10665.27` → IC=-0.233 (n=84)

  - _Acción_: SKIP cuando `libro_liquidez` < 10665.27
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=28)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=49)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35151.71` → IC=-0.200 (n=38)

  - _Acción_: SKIP cuando `liq_usd_total` < 35151.71
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=80)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `liq_usd_total` > `59480.98` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `liq_usd_total` > 59480.98 (IC base=+0.008)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.008)

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
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=383)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=410)

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
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=64)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=64)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=169)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=169)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=141)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=125)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=125)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=94)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=31)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=30)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=53)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=1637)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=5019)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.184 (n=1639)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=5219)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.221 (n=260)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=798)

- **FILTRO** `ibs_20min` < `0.7378` → IC=-0.188 (n=264)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7378
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=794)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.159 (n=294)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=915)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.56` → IC=-0.186 (n=262)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=806)

- **FILTRO** `ballena_activa_n` > `58.0` → IC=-0.157 (n=266)

  - _Acción_: SKIP cuando `ballena_activa_n` > 58.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=802)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.182 (n=360)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=752)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.218 (n=289)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=890)

- **FILTRO** `ibs_20min` > `0.7059` → IC=-0.196 (n=294)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7059
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=885)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.170 (n=316)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=793)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.173 (n=264)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=809)

- **FILTRO** `ibs_20min` > `0.214` → IC=-0.148 (n=268)

  - _Acción_: SKIP cuando `ibs_20min` > 0.214
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=805)

### MOMENTUM_IBS_15M_BALLENA#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.142 (n=294)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=827)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.150 (n=281)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=873)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.188 (n=254)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=774)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1013)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=292)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=883)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `hora_utc` < `16.0` → IC=-0.340 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=235)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=239)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=558)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=564)

### MOMENTUM_IBS_15M_FADE#BNB#15min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=20)

- **FILTRO** `libro_liquidez` < `2024.7167` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 2024.7167
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.012)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

- **FILTRO** `ibs_20min` < `0.0156` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0156
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=65)

- **FILTRO** `drift_20min_pct` |x|> `0.2103` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2103
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=65)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.1064` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1064
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=19)

- **FILTRO** `py_entrada` > `0.645` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.645
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=106)

- **FILTRO** `ibs_20min` > `0.9803` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9803
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=106)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=43)

- **PATRÓN** `libro_liquidez` > `4444.4944` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 4444.4944 (IC base=-0.065)

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

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 16.0 (IC base=+0.033)

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
- **FILTRO** `py_entrada` < `0.35` → IC=-0.279 (n=3878)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=12120)

- **FILTRO** `ibs_7min` < `0.7172` → IC=-0.234 (n=3999)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7172
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=11999)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.168 (n=5382)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=10616)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.221 (n=4915)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=15351)

- **FILTRO** `ibs_7min` > `0.7134` → IC=-0.172 (n=5066)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7134
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15200)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=566)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1805)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.251 (n=782)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1589)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=563)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1808)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.243 (n=865)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2655)

- **FILTRO** `drift_7min_pct` |x|> `0.1143` → IC=-0.133 (n=1194)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=2326)

- **FILTRO** `ibs_7min` > `0.8349` → IC=-0.198 (n=879)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8349
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2641)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=2287)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.262 (n=712)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2234)

- **FILTRO** `ibs_7min` < `0.7722` → IC=-0.192 (n=736)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7722
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=2210)

- **FILTRO** `ballena_activa_n` > `164.0` → IC=-0.177 (n=734)

  - _Acción_: SKIP cuando `ballena_activa_n` > 164.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=2212)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.242 (n=723)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2246)

- **FILTRO** `ballena_activa_n` > `107.0` → IC=-0.169 (n=1005)

  - _Acción_: SKIP cuando `ballena_activa_n` > 107.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1964)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.180 (n=760)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=1587)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.303 (n=746)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=1601)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.288 (n=583)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1764)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.241 (n=554)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=1793)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.224 (n=866)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=2811)

- **FILTRO** `ibs_7min` > `0.7964` → IC=-0.172 (n=919)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7964
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2758)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.261 (n=647)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=2056)

- **FILTRO** `ibs_7min` < `0.7586` → IC=-0.187 (n=675)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7586
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=2028)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.170 (n=905)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=1798)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.255 (n=680)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=2047)

- **FILTRO** `ibs_7min` > `0.2766` → IC=-0.176 (n=681)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2766
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=2046)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.186 (n=674)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=2053)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.236 (n=725)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2267)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.203 (n=740)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2252)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.167 (n=948)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=2853)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.296 (n=635)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2004)

- **FILTRO** `ibs_7min` < `0.74` → IC=-0.231 (n=653)

  - _Acción_: SKIP cuando `ibs_7min` < 0.74
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=1986)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.226 (n=636)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2003)

- **FILTRO** `py_entrada` > `0.69` → IC=-0.204 (n=857)

  - _Acción_: SKIP cuando `py_entrada` > 0.69
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=2715)

- **FILTRO** `ibs_7min` > `0.76` → IC=-0.154 (n=888)

  - _Acción_: SKIP cuando `ibs_7min` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2684)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=855)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=437)

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
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=484)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.145 (n=548)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.140 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `456.268` → IC=+0.161 (n=175)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 456.268 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3336.2388` → IC=+0.150 (n=215)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3336.2388 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.130 (n=387)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 63.0 (IC base=+0.130)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.276 (n=56)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.127)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `libro_liquidez` > `2005.686` → IC=+0.121 (n=85)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2005.686 (IC base=+0.094)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.194 (n=60)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.107)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.129 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 10.0 (IC base=+0.107)

- **PATRÓN** `total_vol_5m` < `655.7948` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `total_vol_5m` < 655.7948 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `7354.4583` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7354.4583 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 152.0 (IC base=+0.107)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4038` → IC=+0.202 (n=82)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4038 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.174 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.196 (n=90)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 18.0 (IC base=+0.176)

- **PATRÓN** `total_vol_5m` < `5831.176` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 5831.176 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `3762.2112` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3762.2112 (IC base=+0.176)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.152 (n=87)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.156 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 14.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `257344.8` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 257344.8 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3381.2566` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3381.2566 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 54.0 (IC base=+0.126)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `3.488` → IC=-0.381 (n=65)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.488
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=127)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `39.9942` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `T_h` > 39.9942
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.125)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=19)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `135.9956` → IC=-0.167 (n=49)

  - _Acción_: SKIP cuando `T_h` > 135.9956
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=161)

- **FILTRO** `pct_vs_K` |x|> `5.2098` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.2098
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=158)

- **FILTRO** `sigma_h` < `0.008` → IC=-0.347 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=60)

- **FILTRO** `T_h` > `145.7058` → IC=-0.367 (n=43)

  - _Acción_: SKIP cuando `T_h` > 145.7058
  - _Potencial_: sin este filtro IC_bueno=-0.307 (n=133)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `87.9918` → IC=-0.179 (n=51)

  - _Acción_: SKIP cuando `T_h` > 87.9918
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **FILTRO** `pct_vs_K` |x|> `3.6199` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.6199
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=62)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=44)

- **FILTRO** `pct_vs_K` |x|> `4.2908` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2908
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=49)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8662` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 0.8662 (IC base=-0.068)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` < `87.9808` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `T_h` < 87.9808
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

- **FILTRO** `sigma_h` > `0.0085` → IC=-0.382 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=46)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.364 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=41)

- **FILTRO** `T_h` > `111.9668` → IC=-0.308 (n=45)

  - _Acción_: SKIP cuando `T_h` > 111.9668
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0142` → IC=-0.450 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `T_h` > `119.1632` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `T_h` > 119.1632
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2367` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2367 (IC base=+0.388)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.450 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.388)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.425 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.388)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.388)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.420 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.388)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.452 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.480)

### STREAK_FADE_15M
- **FILTRO** `hora_utc` < `7.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=68)

- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=75)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.127 (n=65)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.043)

- **PATRÓN** `streak_estiramiento` < `0.4159` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.4159 (IC base=+0.024)

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
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=173)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=193)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=195)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=208)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=298)

- **PATRÓN** `streak_estiramiento` < `0.3671` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.3671 (IC base=+0.026)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=583)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=309)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=388)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=1701)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=943)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=951)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.173 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0035 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.197 (n=209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0076 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.191` → IC=+0.145 (n=285)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.191 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3329` → IC=+0.191 (n=312)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3329 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.5957` → IC=+0.221 (n=626)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5957 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.2685` → IC=+0.150 (n=241)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.2685 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.547` → IC=+0.144 (n=667)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.547 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.709` → IC=+0.229 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.709 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=620)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `9601.804` → IC=+0.168 (n=209)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 9601.804 (IC base=+0.143)

### UPDOWN_GBM#5min
- **FILTRO** `sigma_ewma_delta_pct` > `7.816` → IC=-0.189 (n=43)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.816
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1325)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_ewma_delta_pct` > `15.082` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 15.082
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=108)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=114)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.130 (n=71)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=145)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.206 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.179 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0044 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.201 (n=175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.179)

- **PATRÓN** `drift_15min` |x|≤ `0.391` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.391 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.200 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.8714` → IC=+0.297 (n=116)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8714 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1553` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1553 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1189` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1189 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `6996.6608` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6996.6608 (IC base=+0.179)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.200 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `ibs_15` < `0.1827` → IC=-0.239 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.1827
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64)

- **FILTRO** `libro_liquidez` < `13612.3448` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 13612.3448
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.132 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=157)

- **FILTRO** `ibs_15` < `0.6789` → IC=-0.180 (n=48)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6789
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=145)

- **FILTRO** `sigma_ewma_delta_pct` > `7.134` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.134
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=62)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.351` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 20.351 (IC base=+0.009)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6467` → IC=-0.206 (n=49)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6467
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2632` → IC=+0.192 (n=50)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2632 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2314` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2314 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.123 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 17.0 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.6467` → IC=+0.195 (n=149)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.6467 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.1542` → IC=+0.147 (n=117)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1542 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.878` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.878 (IC base=+0.095)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=118)

- **FILTRO** `dist_vwap_pct` > `0.2547` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2547
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=129)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `libro_spread` > `0.03` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=180)

- **FILTRO** `hora_utc` < `16.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.5217` → IC=-0.214 (n=26)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5217
  - _Potencial_: sin este filtro IC_bueno=+0.235 (n=81)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.259 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1604` → IC=+0.139 (n=81)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1604 (IC base=+0.124)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1276` → IC=+0.161 (n=54)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1276 (IC base=+0.124)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2717` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2717 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.210 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.124)

- **PATRÓN** `ibs_15` > `0.5217` → IC=+0.235 (n=81)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5217 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.0906` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.0906 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.477` → IC=+0.312 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.477 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2951.056` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2951.056 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.124)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0241` → IC=-0.223 (n=45)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0241
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=137)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=142)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `12.798` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 12.798
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.007 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3805` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3805 (IC base=+0.029)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0202` → IC=+0.217 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0202 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0451` → IC=+0.163 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.0451 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3131` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3131 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.4821` → IC=+0.220 (n=173)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4821 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1207` → IC=+0.213 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1207 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.5574` → IC=+0.142 (n=199)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.5574 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.916` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.916 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2734.4955` → IC=+0.200 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2734.4955 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.179 (n=191)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` < 0.1154 (IC base=+0.032)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.326 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.324)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.390 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.324)

- **PATRÓN** `drift_60min` |x|≤ `0.1149` → IC=+0.347 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1149 (IC base=+0.324)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.339 (n=141)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.324)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.369 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.324)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.350 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.324)

- **PATRÓN** `ibs_15` > `0.8365` → IC=+0.390 (n=189)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8365 (IC base=+0.324)

- **PATRÓN** `dist_vwap_pct` > `0.156` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.156 (IC base=+0.324)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.39` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.39 (IC base=+0.324)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.888` → IC=+0.327 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.888 (IC base=+0.324)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.330 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.324)

- **PATRÓN** `libro_liquidez` > `8557.9163` → IC=+0.357 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8557.9163 (IC base=+0.324)

- **PATRÓN** `ballena_activa_n` < `528.0` → IC=+0.365 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 528.0 (IC base=+0.324)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.112` → IC=+0.364 (n=42)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.112 (IC base=+0.316)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.321 (n=110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.341 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.316)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.330 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.316)

- **PATRÓN** `drift_15min` |x|≤ `0.376` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.376 (IC base=+0.316)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0919` → IC=+0.325 (n=112)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0919 (IC base=+0.316)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.358 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.316)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.358 (n=125)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.459` → IC=+0.335 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.459 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `8157.6321` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8157.6321 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `625.0` → IC=+0.410 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 625.0 (IC base=+0.316)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.329 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.331)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.381 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.369 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.343 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2567` → IC=+0.336 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2567 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.335 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.331)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.327 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.399 (n=87)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` < `0.3157` → IC=+0.352 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3157 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.378 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.331)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `2812.5928` → IC=+0.338 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2812.5928 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.344 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 166.0 (IC base=+0.331)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0112` → IC=-0.192 (n=375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0112
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1129)

- **FILTRO** `ibs_15` < `0.5879` → IC=-0.188 (n=168)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5879
  - _Potencial_: sin este filtro IC_bueno=+0.240 (n=344)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.150 (n=398)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1106)

- **FILTRO** `sigma_ewma_delta_pct` > `18.83` → IC=-0.158 (n=539)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.83
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4107)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3577` → IC=+0.192 (n=222)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3577 (IC base=-0.064)

- **PATRÓN** `ibs_15` > `0.5879` → IC=+0.240 (n=344)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5879 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.1742` → IC=+0.138 (n=233)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1742 (IC base=-0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1261` → IC=+0.223 (n=359)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1261 (IC base=-0.065)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1115` → IC=+0.234 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1115 (IC base=-0.065)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.265 (n=538)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.1477` → IC=+0.212 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1477 (IC base=-0.065)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.214 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=-0.065)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0074` → IC=-0.227 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=722)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.234 (n=317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=645)

- **FILTRO** `sigma_ewma_delta_pct` > `19.521` → IC=-0.257 (n=175)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.521
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=787)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1186` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1186 (IC base=+0.035)

- **PATRÓN** `ibs_15` > `0.6819` → IC=+0.320 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6819 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` < `0.156` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.156 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `320.0` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 320.0 (IC base=+0.035)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6515` → IC=-0.228 (n=79)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6515
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=161)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=223)

- **PATRÓN** `drift_60min` |x|≤ `0.0806` → IC=+0.207 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0806 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.6515` → IC=+0.255 (n=161)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6515 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.1823` → IC=+0.130 (n=136)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1823 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `12132.5552` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12132.5552 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.248 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.212)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.213 (n=252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.221 (n=252)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0945` → IC=+0.223 (n=225)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0945 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.213 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.278 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.276 (n=252)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1698` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1698 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.337` → IC=+0.230 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.337 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `3621.1646` → IC=+0.213 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3621.1646 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.220 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 128.0 (IC base=+0.212)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1609` → IC=-0.198 (n=127)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1609
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=248)

- **FILTRO** `drift_15min` |x|> `0.8118` → IC=-0.268 (n=93)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8118
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=282)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=130)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=245)

- **FILTRO** `sigma_ewma_delta_pct` > `16.585` → IC=-0.135 (n=187)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.585
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=1447)

- **PATRÓN** `ibs_15` > `0.8214` → IC=+0.262 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8214 (IC base=-0.134)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0761` → IC=+0.164 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.0761 (IC base=-0.053)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2087` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2087 (IC base=-0.053)

- **PATRÓN** `ibs_15` < `0.3814` → IC=+0.207 (n=121)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3814 (IC base=-0.053)

- **PATRÓN** `dist_vwap_pct` < `0.2528` → IC=+0.187 (n=113)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.2528 (IC base=-0.053)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1295` → IC=-0.176 (n=143)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1295
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=279)

- **FILTRO** `drift_15min` |x|> `1.1952` → IC=-0.248 (n=105)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.1952
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=317)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=346)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0953` → IC=+0.344 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0953 (IC base=-0.062)

- **PATRÓN** `ibs_15` < `0.1346` → IC=+0.280 (n=98)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1346 (IC base=-0.062)

- **PATRÓN** `dist_vwap_pct` > `0.4952` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4952 (IC base=-0.062)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=-0.062)

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
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.285 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.284 (n=327)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.331 (n=122)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1322` → IC=+0.305 (n=244)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1322 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.320 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8311` → IC=+0.315 (n=366)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8311 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2982` → IC=+0.322 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2982 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.832` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.832 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.28` → IC=+0.286 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.28 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `13914.1536` → IC=+0.323 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13914.1536 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.296 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.283 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.1141` → IC=+0.296 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1141 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1252` → IC=+0.324 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1252 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8545` → IC=+0.315 (n=187)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8545 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.3029` → IC=+0.330 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3029 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.592` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.592 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.915` → IC=+0.288 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.915 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `15468.9258` → IC=+0.347 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15468.9258 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.280 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.283 (n=141)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0041 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.047` → IC=+0.336 (n=53)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.047 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1898` → IC=+0.324 (n=72)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1898 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1463` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1463 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.317 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8444` → IC=+0.318 (n=157)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8444 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` < `0.4777` → IC=+0.284 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4777 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.547` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.547 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.304 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `12186.1594` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12186.1594 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `183.0` → IC=+0.277 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 183.0 (IC base=+0.282)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0807` → IC=-0.253 (n=75)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0807
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=148)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1209` → IC=-0.157 (n=106)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1209
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=320)

- **FILTRO** `drift_15min` |x|> `0.5291` → IC=-0.130 (n=106)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5291
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=320)

- **FILTRO** `ballena_activa_n` > `20.0` → IC=-0.179 (n=82)

  - _Acción_: SKIP cuando `ballena_activa_n` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=83)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.143 (n=40)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=82)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1979` → IC=-0.382 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1979
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

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
- **PATRÓN** `T_h` < `63.9918` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `T_h` < 63.9918 (IC base=+0.121)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.322 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.121)

- **PATRÓN** `T_h` > `145.9626` → IC=+0.417 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.9626 (IC base=+0.344)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.344)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.096)

- **PATRÓN** `ratio` > `1.0126` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0126 (IC base=+0.285)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `79.3918` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 79.3918 (IC base=+0.174)

- **PATRÓN** `ratio` < `0.9911` → IC=+0.411 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9911 (IC base=+0.174)

- **PATRÓN** `T_h` > `87.9969` → IC=+0.328 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9969 (IC base=+0.316)

- **PATRÓN** `ratio` > `1.012` → IC=+0.320 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.316)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9824` → IC=+0.428 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9824 (IC base=+0.409)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-SIGMA-SOL-60MIN**: `UPDOWN_GBM#SOL#60min` gana cuando sigma_h < 0.007 (IC=+0.167 n=34). Implementar como filtro pre-predicción en shadow_predict.py.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5957 sube el IC de +0.143 a +0.221 en UPDOWN_GBM#15min (n=626). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8714 sube el IC de +0.179 a +0.297 en UPDOWN_GBM#BTC#15min (n=116). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6467 sube el IC de +0.095 a +0.195 en UPDOWN_GBM#ETH#15min (n=149). Ya aplicado como kelly_boost=+0.98€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5217 sube el IC de +0.124 a +0.235 en UPDOWN_GBM#SOL#15min (n=81). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4821 sube el IC de +0.142 a +0.220 en UPDOWN_GBM#XRP#15min (n=173). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1154 sube el IC de +0.032 a +0.179 en UPDOWN_GBM#XRP#15min (n=191). Ya aplicado como kelly_boost=+0.89€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5879 sube el IC de -0.064 a +0.240 en UPDOWN_GBM_15M_TARDIO (n=344). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.065 a +0.265 en UPDOWN_GBM_15M_TARDIO (n=538). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.6819 sube el IC de +0.035 a +0.320 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6515 sube el IC de +0.095 a +0.255 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=161). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.212 a +0.276 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=252). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8214 sube el IC de -0.134 a +0.262 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3814 sube el IC de -0.053 a +0.207 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=121). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1346 sube el IC de -0.062 a +0.280 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=98). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7 (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_NO, IBS > 0.2576 sube el IC de +0.100 a +0.208 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=22). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8311 sube el IC de +0.283 a +0.315 en UPDOWN_GBM_IBS_ALTO (n=366). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8545 sube el IC de +0.282 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=187). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8444 sube el IC de +0.282 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=157). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8365 sube el IC de +0.324 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=189). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.316 a +0.358 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=125). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.331 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=87). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 889 | +0.088 | +66.21€ | 2 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 889 | +0.088 | +66.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 25 | +0.056 | -0.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 25 | +0.056 | -0.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 600 | +0.103 | +52.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 600 | +0.103 | +52.19€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 222 | +0.036 | -0.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 222 | +0.036 | -0.81€ | 5 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 42 | +0.159 | +15.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 42 | +0.159 | +15.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 16238 | -0.118 | -2600.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1003 | -0.019 | -153.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 15235 | -0.124 | -2447.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 2209 | -0.108 | -484.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 2209 | -0.108 | -484.73€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1003 | -0.019 | -153.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1003 | -0.019 | -153.07€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 2136 | -0.169 | -580.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 2136 | -0.169 | -580.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 4303 | -0.062 | -397.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 4303 | -0.062 | -397.56€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 3640 | -0.131 | -235.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 3640 | -0.131 | -235.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 2947 | -0.187 | -749.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 2947 | -0.187 | -749.87€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 5322 | -0.079 | +1940.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 1518 | -0.013 | +1059.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 3804 | -0.105 | +881.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 5322 | -0.079 | +1940.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 1518 | -0.013 | +1059.04€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 3804 | -0.105 | +881.47€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 115 | -0.038 | -11.48€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 115 | -0.038 | -11.48€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 115 | -0.038 | -11.48€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 115 | -0.038 | -11.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 52234 | +0.114 | -3117.72€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 8647 | +0.182 | -297.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 188 | -0.116 | -60.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 39481 | +0.099 | -2680.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 3918 | +0.116 | -80.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 6620 | +0.086 | -820.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 29 | -0.113 | +4.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 6576 | +0.088 | -813.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 10428 | +0.132 | -226.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2554 | +0.198 | -115.59€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 6528 | +0.109 | -132.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1304 | +0.123 | +43.62€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 6641 | +0.087 | -760.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 32 | +0.000 | +1.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 6594 | +0.088 | -751.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 11281 | +0.126 | -185.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 3239 | +0.170 | -30.92€ | 1 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 6571 | +0.112 | -106.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1459 | +0.097 | -39.34€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 10642 | +0.121 | -690.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2769 | +0.188 | -161.60€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 93 | -0.037 | -7.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 6625 | +0.094 | -436.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1155 | +0.130 | -84.50€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 6622 | +0.105 | -435.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 24 | +0.000 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 11 | +0.021 | +1.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 6587 | +0.105 | -440.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 8535 | +0.180 | -643.43€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 8535 | +0.180 | -643.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2179 | +0.168 | -235.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2179 | +0.168 | -235.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 149 | -0.136 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 149 | -0.136 | -0.83€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2130 | +0.173 | -217.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2130 | +0.173 | -217.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 1914 | +0.236 | -47.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 1914 | +0.236 | -47.26€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2084 | +0.186 | -156.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2084 | +0.186 | -156.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 422 | +0.441 | -0.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 422 | +0.441 | -0.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 162 | +0.439 | -0.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 162 | +0.439 | -0.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 161 | +0.439 | +0.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 161 | +0.439 | +0.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 95 | +0.428 | -1.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 95 | +0.428 | -1.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 28055 | +0.191 | -2521.52€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 28055 | +0.191 | -2521.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 4983 | +0.154 | -745.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 4983 | +0.154 | -745.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 4384 | +0.225 | -155.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 4384 | +0.225 | -155.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 4848 | +0.167 | -628.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 4848 | +0.167 | -628.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 4474 | +0.221 | -173.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 4474 | +0.221 | -173.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 4640 | +0.201 | -331.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 4640 | +0.201 | -331.38€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 4726 | +0.185 | -486.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 4726 | +0.185 | -486.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 10178 | +0.129 | +297.50€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 10178 | +0.129 | +297.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 5035 | +0.135 | +200.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 5035 | +0.135 | +200.51€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 5143 | +0.123 | +96.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 5143 | +0.123 | +96.99€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1005 | +0.292 | -8.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1005 | +0.292 | -8.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 435 | +0.278 | -11.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 435 | +0.278 | -11.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 475 | +0.297 | +5.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 475 | +0.297 | +5.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 95 | +0.325 | -2.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 95 | +0.325 | -2.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 438 | +0.423 | -12.40€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 438 | +0.423 | -12.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 196 | +0.419 | -6.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 196 | +0.419 | -6.94€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 205 | +0.427 | -5.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 205 | +0.427 | -5.01€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 37 | +0.372 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 37 | +0.372 | -0.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 538 | +0.098 | -0.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 190 | +0.094 | -4.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 348 | +0.100 | +3.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 37 | +0.090 | +0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 37 | +0.090 | +0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 418 | +0.107 | +9.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 70 | +0.139 | +5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 348 | +0.100 | +3.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 83 | +0.053 | -9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 83 | +0.053 | -9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 16019 | +0.096 | -588.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 1418 | +0.077 | -23.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 14601 | +0.097 | -565.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 9515 | +0.098 | -213.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 1418 | +0.077 | -23.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 8097 | +0.102 | -190.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 2193 | +0.111 | +9.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 2193 | +0.111 | +9.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 4311 | +0.082 | -384.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 4311 | +0.082 | -384.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 594 | +0.257 | -78.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 594 | +0.257 | -78.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 594 | +0.257 | -78.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 594 | +0.257 | -78.05€ | 0 | 4 |
| ✅ GBM_LATE_15M | 13204 | +0.060 | +5657.27€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 13204 | +0.060 | +5657.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 2068 | +0.194 | +1503.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 2068 | +0.194 | +1503.18€ | 0 | 24 |
| ✅ GBM_LATE_15M#BTC | 1961 | +0.177 | +1339.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1961 | +0.177 | +1339.87€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 2128 | +0.192 | +1521.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 2128 | +0.192 | +1521.58€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 2028 | -0.034 | +132.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2028 | -0.034 | +132.84€ | 2 | 11 |
| ✅ GBM_LATE_15M#SOL | 2082 | -0.052 | +493.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2082 | -0.052 | +493.88€ | 5 | 10 |
| ✅ GBM_LATE_15M#XRP | 2937 | -0.065 | +665.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2937 | -0.065 | +665.91€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 14062 | +0.065 | +7265.12€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 14062 | +0.065 | +7265.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 2506 | +0.002 | +1758.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 2506 | +0.002 | +1758.13€ | 2 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 3032 | -0.014 | +486.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 3032 | -0.014 | +486.02€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 1886 | +0.255 | +1842.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 1886 | +0.255 | +1842.51€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2116 | -0.046 | +80.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2116 | -0.046 | +80.63€ | 6 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2336 | -0.006 | +859.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2336 | -0.006 | +859.16€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2186 | +0.266 | +2238.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2186 | +0.266 | +2238.67€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 10913 | +0.167 | +7716.73€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 10913 | +0.167 | +7716.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 1561 | +0.200 | +1198.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 1561 | +0.200 | +1198.76€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 1770 | +0.159 | +1284.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 1770 | +0.159 | +1284.85€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 1610 | +0.196 | +1209.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 1610 | +0.196 | +1209.06€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 1788 | +0.138 | +1102.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 1788 | +0.138 | +1102.90€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2044 | +0.116 | +1265.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2044 | +0.116 | +1265.46€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2140 | +0.198 | +1655.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2140 | +0.198 | +1655.69€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 2469 | +0.107 | +816.79€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 2469 | +0.107 | +816.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 92 | +0.106 | +36.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 92 | +0.106 | +36.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 639 | +0.085 | +182.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 639 | +0.085 | +182.47€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 353 | +0.145 | +171.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 353 | +0.145 | +171.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 590 | +0.162 | +248.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 590 | +0.162 | +248.92€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 408 | +0.002 | +26.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 408 | +0.002 | +26.19€ | 4 | 4 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 13130 | +0.174 | +9444.34€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#15min | 13130 | +0.174 | +9444.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 1986 | +0.220 | +1673.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 1986 | +0.220 | +1673.14€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2110 | +0.161 | +1492.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2110 | +0.161 | +1492.33€ | 0 | 29 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 2015 | +0.221 | +1697.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 2015 | +0.221 | +1697.90€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 2030 | +0.132 | +1213.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 2030 | +0.132 | +1213.92€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2324 | +0.105 | +1284.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2324 | +0.105 | +1284.83€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2665 | +0.204 | +2082.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2665 | +0.204 | +2082.21€ | 0 | 23 |
| ✅ GBM_LATE_5M | 4085 | +0.124 | +1911.20€ | 1 | 23 |
| ✅ GBM_LATE_5M#5min | 4085 | +0.124 | +1911.20€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 255 | +0.165 | +157.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 255 | +0.165 | +157.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1060 | +0.109 | +511.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1060 | +0.109 | +511.17€ | 1 | 16 |
| ✅ GBM_LATE_5M#DOGE | 628 | +0.165 | +382.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 628 | +0.165 | +382.64€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 1329 | +0.140 | +656.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1329 | +0.140 | +656.69€ | 0 | 28 |
| ✅ GBM_LATE_5M#SOL | 180 | -0.017 | +4.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 180 | -0.017 | +4.93€ | 2 | 2 |
| ✅ GBM_LATE_5M#XRP | 633 | +0.097 | +198.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 633 | +0.097 | +198.14€ | 0 | 0 |
| ✅ GBM_LATE_60M | 807 | +0.022 | +193.77€ | 3 | 13 |
| ✅ GBM_LATE_60M#60min | 807 | +0.022 | +193.77€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 270 | +0.062 | +57.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 270 | +0.062 | +57.83€ | 0 | 12 |
| ✅ GBM_LATE_60M#ETH | 295 | +0.039 | +89.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 295 | +0.039 | +89.13€ | 3 | 12 |
| ✅ GBM_LATE_60M#SOL | 242 | -0.045 | +46.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 242 | -0.045 | +46.80€ | 3 | 7 |
| 🚫 GBM_LATE_60M_FADE | 225 | -0.302 | -36.90€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 225 | -0.302 | -36.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 87 | -0.253 | -9.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 87 | -0.253 | -9.24€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 75 | -0.357 | -22.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 75 | -0.357 | -22.68€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 63 | -0.285 | -4.98€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 63 | -0.285 | -4.98€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 458 | +0.039 | +40.97€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 458 | +0.039 | +40.97€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 187 | +0.045 | +25.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 187 | +0.045 | +25.52€ | 3 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 122 | +0.048 | -3.59€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 122 | +0.048 | -3.59€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 149 | +0.023 | +19.04€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 149 | +0.023 | +19.04€ | 1 | 1 |
| ✅ LATE_WINDOW_5MIN | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 44 | +0.217 | +18.24€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 691 | +0.103 | +172.48€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 691 | +0.103 | +172.48€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 691 | +0.103 | +172.48€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 691 | +0.103 | +172.48€ | 0 | 4 |
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
| ✅ LIQUIDACIONES_5M | 1298 | -0.010 | -18.41€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1298 | -0.010 | -18.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 152 | -0.033 | -3.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 152 | -0.033 | -3.83€ | 3 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 99 | -0.054 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 99 | -0.054 | -6.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 429 | +0.022 | +12.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 429 | +0.022 | +12.18€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 450 | -0.009 | -9.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 450 | -0.009 | -9.60€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 93 | -0.058 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 93 | -0.058 | -5.46€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 677 | -0.026 | -7.90€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 677 | -0.026 | -7.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 199 | -0.042 | -10.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 199 | -0.042 | -10.70€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 205 | -0.002 | +2.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 205 | -0.002 | +2.99€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 273 | -0.031 | -0.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 273 | -0.031 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 8210 | -0.003 | -103.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 8210 | -0.003 | -103.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 561 | -0.008 | +0.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 561 | -0.008 | +0.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 894 | -0.020 | -21.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 894 | -0.020 | -21.28€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 1958 | +0.010 | -12.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 1958 | +0.010 | -12.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 1585 | +0.001 | +1.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 1585 | +0.001 | +1.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 1733 | -0.009 | -42.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 1733 | -0.009 | -42.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1479 | -0.005 | -30.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1479 | -0.005 | -30.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 13514 | -0.029 | +636.61€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 13514 | -0.029 | +636.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 2267 | -0.015 | +328.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 2267 | -0.015 | +328.65€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 2296 | -0.032 | -20.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 2296 | -0.032 | -20.48€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 2291 | -0.025 | +195.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 2291 | -0.025 | +195.06€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 2182 | -0.047 | -50.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 2182 | -0.047 | -50.64€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 2275 | -0.032 | +100.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 2275 | -0.032 | +100.85€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 2203 | -0.025 | +83.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 2203 | -0.025 | +83.16€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 862 | -0.090 | -50.53€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 862 | -0.090 | -50.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 121 | -0.020 | -3.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 121 | -0.020 | -3.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 132 | -0.142 | -14.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 132 | -0.142 | -14.20€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 37 | -0.115 | -4.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 37 | -0.115 | -4.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 177 | -0.170 | -16.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 177 | -0.170 | -16.47€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 245 | -0.067 | -2.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 245 | -0.067 | -2.10€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 150 | -0.033 | -9.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 150 | -0.033 | -9.24€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3185 | +0.004 | -4.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1386 | +0.006 | -1.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1386 | +0.006 | -1.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 36264 | -0.078 | +578.25€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 36264 | -0.078 | +578.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 5891 | -0.088 | +426.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 5891 | -0.088 | +426.23€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 5915 | -0.083 | -168.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 5915 | -0.083 | -168.38€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 6024 | -0.084 | +197.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 6024 | -0.084 | +197.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 5430 | -0.101 | -316.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 5430 | -0.101 | -316.17€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 6793 | -0.053 | +146.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 6793 | -0.053 | +146.75€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 6211 | -0.066 | +292.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 6211 | -0.066 | +292.05€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6324 | -0.015 | -109.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6324 | -0.015 | -109.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1350 | -0.010 | -12.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1350 | -0.010 | -12.96€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1374 | -0.006 | -9.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1374 | -0.006 | -9.77€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 866 | -0.021 | -12.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 866 | -0.021 | -12.20€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 736 | -0.020 | -23.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 768 | +0.114 | +261.42€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 632 | +0.126 | +248.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 148 | +0.127 | +65.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 148 | +0.127 | +65.89€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 126 | +0.094 | +27.35€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 126 | +0.094 | +27.35€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 120 | +0.107 | +41.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 120 | +0.107 | +41.99€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 109 | +0.176 | +66.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 109 | +0.176 | +66.39€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 129 | +0.126 | +47.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 129 | +0.126 | +47.21€ | 0 | 6 |
| ✅ PRICE_TARGET_GBM | 357 | -0.130 | -16.07€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 157 | -0.198 | -37.75€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 127 | -0.252 | -39.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 30 | +0.031 | +1.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 134 | -0.103 | +1.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 97 | -0.126 | -5.22€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 37 | -0.038 | +7.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 66 | -0.015 | +19.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 49 | -0.049 | +12.68€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 17 | +0.067 | +7.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 273 | -0.173 | -32.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 84 | +0.012 | +15.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 386 | -0.214 | -17.25€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 167 | -0.180 | -16.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 143 | -0.169 | -14.88€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 24 | -0.231 | -1.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 139 | -0.259 | -18.00€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 117 | -0.273 | -22.39€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 22 | -0.167 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 80 | -0.195 | +16.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 67 | -0.196 | +13.35€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 13 | -0.108 | +3.57€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 327 | -0.214 | -23.93€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 59 | -0.205 | +6.68€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 111 | +0.367 | +46.74€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#BTC | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 19 | -0.023 | -4.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 26 | +0.321 | +5.89€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 66 | +0.485 | +45.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 66 | +0.485 | +45.13€ | 0 | 1 |
| ✅ RESOLUTION_SNIPER#sniper | 111 | +0.367 | +46.74€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 258 | +0.031 | -3.04€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 258 | +0.031 | -3.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 114 | +0.060 | +3.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 114 | +0.060 | +3.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 18 | +0.045 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 28 | -0.033 | -3.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 28 | -0.033 | -3.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 98 | +0.010 | -4.75€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 98 | +0.010 | -4.75€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 1952 | -0.022 | -82.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 1952 | -0.022 | -82.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 801 | -0.018 | -26.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 801 | -0.018 | -26.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 553 | -0.026 | -25.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 553 | -0.026 | -25.13€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 141 | -0.038 | -12.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 141 | -0.038 | -12.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 457 | -0.018 | -18.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 457 | -0.018 | -18.43€ | 4 | 0 |
| ✅ STREAK_FADE_60M | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 45 | +0.011 | -0.05€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 28 | -0.067 | -2.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 17 | +0.112 | +2.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 4196 | +0.015 | +35.73€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 4196 | +0.015 | +35.73€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1364 | +0.018 | +7.80€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1364 | +0.018 | +7.80€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 860 | +0.028 | +24.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 860 | +0.028 | +24.72€ | 1 | 1 |
| ✅ STREAK_MOM_5M#SOL | 1233 | +0.007 | -6.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1233 | +0.007 | -6.94€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 739 | +0.011 | +10.15€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 739 | +0.011 | +10.15€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 4481 | +0.011 | -31.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 4481 | +0.011 | -31.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 1720 | +0.012 | -11.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 1720 | +0.012 | -11.20€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 1786 | +0.018 | +1.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 1786 | +0.018 | +1.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 975 | -0.007 | -21.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 975 | -0.007 | -21.43€ | 2 | 0 |
| ✅ UPDOWN_GBM | 11652 | +0.013 | +419.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3907 | +0.041 | +441.61€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 491 | +0.007 | +8.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 6460 | -0.000 | -22.52€ | 1 | 0 |
| ✅ UPDOWN_GBM#60min | 738 | -0.004 | -5.53€ | 2 | 0 |
| ✅ UPDOWN_GBM#BNB | 593 | +0.063 | +55.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 188 | +0.111 | +41.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 11 | -0.021 | -0.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 394 | +0.043 | +14.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 2105 | +0.015 | +124.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 448 | +0.078 | +99.23€ | 1 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 149 | +0.043 | +8.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 1189 | -0.004 | +21.25€ | 3 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 298 | -0.003 | -5.55€ | 3 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 21 | -0.152 | +0.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 1398 | +0.011 | +15.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 130 | +0.091 | +29.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 10 | +0.042 | +0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 1258 | +0.002 | -14.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 2374 | +0.002 | +22.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1115 | +0.027 | +45.58€ | 1 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 139 | +0.018 | +7.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 811 | -0.028 | -28.20€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 290 | -0.010 | -2.99€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 19 | -0.158 | +0.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 3288 | +0.003 | +26.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1033 | +0.004 | +26.36€ | 1 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 133 | -0.004 | -2.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 1958 | +0.005 | +0.68€ | 2 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 150 | +0.007 | +3.00€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 14 | -0.175 | -1.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 1892 | +0.025 | +177.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 993 | +0.058 | +198.51€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 49 | -0.108 | -6.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 850 | -0.005 | -15.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 54 | -0.196 | +0.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 282 | +0.324 | +66.94€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 282 | +0.324 | +66.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 166 | +0.316 | +31.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 166 | +0.316 | +31.87€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 116 | +0.331 | +35.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 116 | +0.331 | +35.06€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 6150 | -0.065 | +1328.75€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 6150 | -0.065 | +1328.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 311 | -0.050 | +343.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 311 | -0.050 | +343.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1257 | -0.145 | -56.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1257 | -0.145 | -56.45€ | 3 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 81 | +0.042 | +8.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 575 | +0.164 | +288.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 575 | +0.164 | +288.38€ | 2 | 16 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2009 | -0.068 | +371.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2009 | -0.068 | +371.34€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1917 | -0.085 | +374.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1917 | -0.085 | +374.08€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 58 | +0.067 | +3.64€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 58 | +0.067 | +3.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 58 | +0.067 | +3.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 58 | +0.067 | +3.64€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 487 | +0.283 | +382.83€ | 0 | 12 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 487 | +0.283 | +382.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 278 | +0.282 | +217.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 278 | +0.282 | +217.95€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 209 | +0.282 | +164.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 209 | +0.282 | +164.89€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 649 | -0.101 | -72.54€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 649 | -0.101 | -72.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 310 | -0.077 | -35.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 310 | -0.077 | -35.00€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 160 | -0.049 | -8.74€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 160 | -0.049 | -8.74€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 60 | -0.177 | -9.28€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 60 | -0.177 | -9.28€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 52 | -0.167 | -5.48€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 52 | -0.167 | -5.48€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1471 | +0.296 | +656.89€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 477 | +0.229 | +25.18€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 491 | +0.279 | +154.58€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 503 | +0.373 | +477.13€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.077) — sin ventaja clara. oversold(IBS<0.3): IC=+0.025 n=4050 | neutral: IC=+0.010 n=4545 | overbought(IBS>0.7): IC=+0.088 n=4552
  - _Datos_: n=13646 IC=+0.042 PNL=+1455.35€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 239 celda(s) pasan gate riguroso completo de 1504 evaluadas (n>=40) y 2554 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.004 < 0.08 — monitorear
  - _Datos_: n=1033 IC=+0.004 PNL=+26.36€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=491/15 IC=+0.279 PNL=+154.58€ | BTC: n=477/15 IC=+0.229 PNL=+25.18€ | SOL: n=503/15 IC=+0.373 PNL=+477.13€

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
  - _Estado_: 11590 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.012 n=80/60 | contraria IC=+0.138 n=56 | gap=-0.126 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=163, boost estimado=-0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 109 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=290/40 IC=-0.010 PNL=-2.99€ | BTC#60min: n=298/40 IC=-0.003 PNL=-5.55€ | SOL#60min: n=150/40 IC=+0.007 PNL=+3.00€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.062 n=170286 | tras_1loss IC=+0.054 n=134464 | tras_2loss IC=+0.019 n=59888/40 | gap=+0.044 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.003 n=1006 | contrario_BTC IC=-0.005 n=903/40 | gap=-0.002 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.145 > 0.08 con n=153 PNL=+52.49€
  - _Datos_: n=153 IC=+0.145 PNL=+52.49€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.278 > 0.08 con n=25 PNL=+21.66€
  - _Datos_: n=25 IC=+0.278 PNL=+21.66€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.336 > 0.1 con n=1238 PNL=+657.09€
  - _Datos_: n=1238 IC=+0.336 PNL=+657.09€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=88 IC=+0.033 PNL=+13.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=88 IC=+0.033 PNL=+13.44€

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
  - _Estado_: n=11272 IC=+0.011 PNL=+363.88€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=11272 IC=+0.011 PNL=+363.88€

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
  - _Estado_: n=570 IC=+0.011 PNL=+2.30€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=570 IC=+0.011 PNL=+2.30€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=168 IC=-0.053 PNL=-7.83€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=168 IC=-0.053 PNL=-7.83€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=196 IC=-0.020 PNL=+4.24€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=196 IC=-0.020 PNL=+4.24€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.143 > 0.1 con n=834 PNL=+318.61€
  - _Datos_: n=834 IC=+0.143 PNL=+318.61€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=250 IC=+0.048 PNL=+40.54€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=250 IC=+0.048 PNL=+40.54€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=448 IC=+0.078 PNL=+99.23€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=448 IC=+0.078 PNL=+99.23€

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
  - _Estado_: n=2283 IC=+0.038 PNL=+271.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2283 IC=+0.038 PNL=+271.87€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=55 IC=-0.254 PNL=-6.56€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=55 IC=-0.254 PNL=-6.56€

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
  - _Estado_: n=2665 IC=-0.016 PNL=-43.20€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2665 IC=-0.016 PNL=-43.20€

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
  - _Estado_: n=2826 IC=+0.015 PNL=+123.17€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2826 IC=+0.015 PNL=+123.17€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=891 IC=+0.035 PNL=+48.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=891 IC=+0.035 PNL=+48.62€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=229 PNL=+68.33€
  - _Datos_: n=229 IC=+0.115 PNL=+68.33€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.08 con n=211 PNL=+31.18€
  - _Datos_: n=211 IC=+0.124 PNL=+31.18€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.136 > 0.08 con n=185 PNL=+67.52€
  - _Datos_: n=185 IC=+0.136 PNL=+67.52€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=27153 IC=+0.103 PNL=+8552.65€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=27153 IC=+0.103 PNL=+8552.65€

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
  - _Estado_: n=1638 IC=+0.034 PNL=+93.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1638 IC=+0.034 PNL=+93.12€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.02 con n=432 PNL=+163.78€
  - _Datos_: n=432 IC=+0.129 PNL=+163.78€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.446 > 0.1 con n=761 PNL=+690.83€
  - _Datos_: n=761 IC=+0.446 PNL=+690.83€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=3102 IC=+0.044 PNL=+320.37€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=3102 IC=+0.044 PNL=+320.37€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.1 con n=1258 PNL=+526.40€
  - _Datos_: n=1258 IC=+0.171 PNL=+526.40€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.193 < -0.1 con n=73 PNL=+2.76€
  - _Datos_: n=73 IC=-0.193 PNL=+2.76€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=763 IC=+0.032 PNL=+82.01€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=763 IC=+0.032 PNL=+82.01€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=35 IC=-0.176 PNL=+2.62€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=35 IC=-0.176 PNL=+2.62€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=145 PNL=+37.82€
  - _Datos_: n=145 IC=+0.119 PNL=+37.82€

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
  - _Estado_: n=8740 IC=-0.140 PNL=+450.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8740 IC=-0.140 PNL=+450.44€

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
  - _Estado_: n=1018 IC=+0.144 PNL=+553.96€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1018 IC=+0.144 PNL=+553.96€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.145 > 0.08 con n=796 PNL=+304.24€
  - _Datos_: n=796 IC=+0.145 PNL=+304.24€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=1125 IC=+0.005 PNL=+12.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1125 IC=+0.005 PNL=+12.76€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=1021 PNL=+605.53€
  - _Datos_: n=1021 IC=+0.084 PNL=+605.53€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.178 > 0.08 con n=231 PNL=+99.32€
  - _Datos_: n=231 IC=+0.178 PNL=+99.32€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.236 < -0.1 con n=942 PNL=-111.02€
  - _Datos_: n=942 IC=-0.236 PNL=-111.02€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=2449 IC=+0.144 PNL=+1460.92€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=2449 IC=+0.144 PNL=+1460.92€

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
  - _Estado_: n=1033 IC=+0.003 PNL=+128.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1033 IC=+0.003 PNL=+128.55€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.08 con n=943 PNL=+649.37€
  - _Datos_: n=943 IC=+0.187 PNL=+649.37€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=1547 IC=-0.055 PNL=+342.10€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1547 IC=-0.055 PNL=+342.10€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.104 > 0.08 con n=336 PNL=-38.83€
  - _Datos_: n=336 IC=+0.104 PNL=-38.83€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=2162 PNL=-223.04€
  - _Datos_: n=2162 IC=+0.227 PNL=-223.04€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=370) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=370 IC=+0.097 PNL=+91.21€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.320 > 0.08 con n=120 PNL=+59.77€
  - _Datos_: n=120 IC=+0.320 PNL=+59.77€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.421 n=301) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=301 IC=+0.421 PNL=+417.34€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=4983 IC=+0.154 PNL=-745.55€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=4983 IC=+0.154 PNL=-745.55€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.1 con n=68 PNL=+47.66€
  - _Datos_: n=68 IC=+0.243 PNL=+47.66€
