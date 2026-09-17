# Hipótesis automáticas — 2026-09-17 18:19 UTC
_Generado por shadow_postmortem.py sobre 485094 resoluciones (PNL=+52377.23€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.247 (n=441)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=411)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.247 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.213 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.803` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.803 (IC base=+0.122)

- **PATRÓN** `banda_z` > `10.241` → IC=+0.224 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.241 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.139 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=512)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.254 (n=340)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.254 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.129)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.217 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.129)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.268 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.129)

- **PATRÓN** `banda_z` > `11.377` → IC=+0.250 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.377 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=427)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2641.4924` → IC=+0.131 (n=337)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2641.4924 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 88.0 (IC base=+0.034)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=87)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.253 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.103)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.103)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 6.043 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `1185.8848` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1185.8848 (IC base=+0.103)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.181)

- **PATRÓN** `n_total_lado` > `39.0` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 39.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.300 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `2707.1913` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2707.1913 (IC base=+0.181)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `144.17` → IC=-0.249 (n=5973)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.17
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=17921)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `141.04` → IC=-0.266 (n=824)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.04
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2474)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `491.58` → IC=-0.159 (n=318)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 491.58
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=954)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `132.71` → IC=-0.292 (n=723)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.71
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2169)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.71` → IC=-0.242 (n=1419)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.71
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4258)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `117.43` → IC=-0.366 (n=1158)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.43
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=3477)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.247 (n=283)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=310)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.162 (n=137)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=426)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.144 (n=130)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=433)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.252 (n=147)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=163)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.181 (n=67)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=214)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.258 (n=89)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=48)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.154 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=110)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=124)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.197 (n=12054)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.69 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3004)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `11420.5455` → IC=+0.193 (n=959)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 11420.5455 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=9335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=11229)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.247 (n=8265)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=5922)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7282.8247` → IC=+0.178 (n=1870)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7282.8247 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1412)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15207.8402` → IC=+0.220 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15207.8402 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=1299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.210 (n=1431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.273 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `13358.8621` → IC=+0.225 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13358.8621 (IC base=+0.203)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.176 (n=282)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=286)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `4641.025` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4641.025 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.177 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.435` → IC=+0.154 (n=680)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.435 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=549)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `3855.8996` → IC=+0.149 (n=425)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3855.8996 (IC base=+0.128)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.329 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=1094)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.330 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `3166.6464` → IC=+0.245 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3166.6464 (IC base=+0.241)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.135 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=507)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.130)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.228 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=470)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `1911.75` → IC=+0.160 (n=374)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1911.75 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=1110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 12.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.423 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.173)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.269 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.177 (n=1139)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.03 (IC base=+0.173)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.172 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 13.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.359 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.137 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.119)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.222 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=336)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.119)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=9517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=9142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.222 (n=3341)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.176 (n=2350)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.167)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.307 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.270 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.268)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.358 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.268)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=2200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=1980)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=2077)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.322 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=1938)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.196 (n=1622)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.440 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `2060.1801` → IC=+0.442 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.1801 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.440 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.457 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `12563.6486` → IC=+0.446 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.6486 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.453 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.465 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.438 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.411 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.407 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.407)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.402 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.407)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.415 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.407)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=28229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.237 (n=10672)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4875)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=5218)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=5035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=5037)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=2711)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=5200)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.170)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=1913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=1777)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=4666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.255 (n=2369)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.193 (n=4722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.248 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.205 (n=4309)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.125)

- **PATRÓN** `restante_min` < `4.08` → IC=+0.134 (n=3940)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.08 (IC base=+0.125)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.153 (n=3975)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.95 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.137 (n=5839)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.125)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.153 (n=3941)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 3.28 (IC base=+0.125)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.129)

- **PATRÓN** `restante_min` < `4.02` → IC=+0.136 (n=1966)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.02 (IC base=+0.129)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.146 (n=2119)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.93 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.144 (n=2885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 8.0 (IC base=+0.129)

- **PATRÓN** `lag_apertura_s` < `3.91` → IC=+0.151 (n=1950)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.91 (IC base=+0.129)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=2137)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.126 (n=2617)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.150 (n=2045)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.96 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.125 (n=2266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=2620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `2.47` → IC=+0.150 (n=1986)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 2.47 (IC base=+0.121)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=1018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.383 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1604.9934` → IC=+0.296 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.9934 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.296 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.270)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.336 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `5052.0555` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5052.0555 (IC base=+0.270)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.327 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1495.8208` → IC=+0.318 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1495.8208 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.342 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.335)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.361 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.335)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.335)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.346 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.371 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.335)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.442 (n=447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.435 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.434 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `1860.5823` → IC=+0.439 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.5823 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.440 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.435 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.448 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.432 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.436 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `2089.6231` → IC=+0.456 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2089.6231 (IC base=+0.435)

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
- **PATRÓN** `ibs_20min` > `0.4986` → IC=+0.155 (n=5776)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.4986 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.1442` → IC=+0.246 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1442 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.846` → IC=+0.168 (n=2503)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.846 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.2223` → IC=+0.243 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2223 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.0678` → IC=+0.242 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0678 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1746` → IC=+0.191 (n=4448)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1746 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.3072` → IC=+0.202 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3072 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.9174` → IC=+0.199 (n=2858)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.9174 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.57` → IC=+0.133 (n=7912)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.57 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.5584` → IC=+0.185 (n=480)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5584 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` < `0.337` → IC=+0.171 (n=2774)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.337 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.174 (n=1150)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7016 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` > `0.8724` → IC=+0.178 (n=1742)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8724 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.2439` → IC=+0.226 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2439 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` > `1.5873` → IC=+0.201 (n=3881)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5873 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.212 (n=4117)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.061)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.184 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0049 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.172 (n=486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0079 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3264` → IC=+0.164 (n=1458)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3264 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.185 (n=547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.032` → IC=+0.275 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.032 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.205 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.4306` → IC=+0.161 (n=1344)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4306 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.181 (n=1373)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.250 (n=967)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.293 (n=360)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.251 (n=740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.288 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.34` → IC=+0.247 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.34 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.092` → IC=+0.231 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.092 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.268 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6473` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6473 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1745.82` → IC=+0.255 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1745.82 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.222 (n=973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1152` → IC=+0.240 (n=486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1152 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=1159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9149` → IC=+0.256 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9149 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.214 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.213 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1292 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.822` → IC=+0.231 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.822 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2593` → IC=+0.220 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2593 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.8755` → IC=+0.211 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8755 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2276` → IC=+0.213 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2276 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.220 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.368` → IC=+0.223 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.368 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `11003.4334` → IC=+0.221 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11003.4334 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.157 (n=1040)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0049 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.159 (n=394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6747` → IC=+0.176 (n=1182)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6747 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1254` → IC=+0.152 (n=1078)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1254 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.596` → IC=+0.164 (n=385)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.596 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2134` → IC=+0.147 (n=1182)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2134 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.141 (n=1182)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6201 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.181 (n=318)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.153 (n=1072)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `13570.903` → IC=+0.153 (n=788)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 13570.903 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.163 (n=330)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 214.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.189 (n=1426)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0058 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.188 (n=546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.254 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.502` → IC=+0.231 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.502 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.183 (n=1212)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.3753` → IC=+0.184 (n=185)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.3753 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.9989` → IC=+0.200 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9989 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.189 (n=1644)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.226 (n=1224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.217 (n=1093)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3808` → IC=+0.234 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3808 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.693` → IC=+0.234 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.693 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.323` → IC=+0.218 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.323 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.269 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3042` → IC=+0.224 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3042 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.231 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1895.6572` → IC=+0.234 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1895.6572 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.224 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1806)

- **PATRÓN** `ibs_20min` > `0.9343` → IC=+0.178 (n=296)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9343 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.3284` → IC=+0.344 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3284 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` < `0.4828` → IC=+0.326 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4828 (IC base=+0.006)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.396` → IC=+0.136 (n=561)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 4.396 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.5962` → IC=+0.364 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5962 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.1953` → IC=+0.352 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1953 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.4943` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4943 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.8068` → IC=+0.344 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8068 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.350 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.17` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.17 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.162 (n=267)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6955 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2689` → IC=+0.247 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2689 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.5104` → IC=+0.191 (n=496)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.5104 (IC base=+0.007)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.154 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=257)

- **FILTRO** `ibs_20min` < `0.375` → IC=-0.180 (n=101)

  - _Acción_: SKIP cuando `ibs_20min` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=209)

- **FILTRO** `ibs_20min` > `0.2692` → IC=-0.128 (n=1812)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=893)

- **FILTRO** `sigma_ewma_delta_pct` > `8.635` → IC=-0.207 (n=298)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.635
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2407)

- **PATRÓN** `ibs_20min` > `0.7576` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7576 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` < `0.6239` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6239 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.6528` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6528 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `0.7836` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7836 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.2252` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2252 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `1.5176` → IC=+0.272 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5176 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.326 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.038)

- **PATRÓN** `ibs_20min` < `0.2692` → IC=+0.121 (n=893)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.2692 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `0.7042` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7042 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` < `1.1044` → IC=+0.212 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1044 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1972` → IC=+0.221 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1972 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.0844` → IC=+0.230 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0844 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.4353` → IC=+0.253 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4353 (IC base=-0.046)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.195 (n=453)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=1361)

- **FILTRO** `ibs_20min` < `0.6685` → IC=-0.162 (n=1197)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6685
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=617)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.202 (n=380)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1434)

- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.200 (n=684)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2054)

- **PATRÓN** `dist_vwap_pct` > `0.9664` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9664 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.310 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.083)

- **PATRÓN** `volumen_regimen` < `0.9997` → IC=+0.274 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9997 (IC base=-0.083)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.288 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.1679` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1679 (IC base=-0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.276 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=-0.083)

- **PATRÓN** `volumen_spike_ratio` > `1.8324` → IC=+0.288 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8324 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` > `1.0024` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0024 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2575` → IC=+0.249 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2575 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.7351` → IC=+0.248 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7351 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.0828` → IC=+0.294 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0828 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1054` → IC=+0.277 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1054 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.2213` → IC=+0.259 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2213 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.5853` → IC=+0.245 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5853 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.181 (n=2699)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0093 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.457` → IC=+0.178 (n=7212)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.457 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.695` → IC=+0.278 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.695 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.509` → IC=+0.146 (n=3823)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.509 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.6782` → IC=+0.238 (n=2462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6782 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.261 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.4763` → IC=+0.245 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4763 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.7567` → IC=+0.237 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7567 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.278 (n=3896)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.142 (n=2737)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0086 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.5551` → IC=+0.152 (n=7209)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5551 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.6702` → IC=+0.247 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6702 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.163` → IC=+0.234 (n=2119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.163 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.7151` → IC=+0.234 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7151 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.1993` → IC=+0.252 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1993 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2507` → IC=+0.316 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2507 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4935` → IC=+0.254 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4935 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.3705` → IC=+0.256 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3705 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.258 (n=2829)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.070)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2381` → IC=-0.144 (n=552)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2381
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1658)

- **FILTRO** `sigma_ewma_delta_pct` > `4.322` → IC=-0.168 (n=414)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.322
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1379)

- **PATRÓN** `ibs_20min` > `0.8702` → IC=+0.255 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8702 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.285` → IC=+0.152 (n=751)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.285 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.300 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.209 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.5947` → IC=+0.194 (n=194)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5947 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8216` → IC=-0.146 (n=602)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8216
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1807)

- **PATRÓN** `dist_vwap_pct` > `0.289` → IC=+0.141 (n=263)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.289 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1582` → IC=+0.135 (n=611)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1582 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6566` → IC=+0.142 (n=637)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6566 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.178 (n=231)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.191 (n=228)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 229.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1515` → IC=+0.212 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1515 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.5983` → IC=+0.207 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5983 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.8169` → IC=+0.209 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8169 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1868` → IC=+0.227 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1868 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `490.0` → IC=+0.215 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 490.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.281 (n=860)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.244 (n=428)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.253 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.52` → IC=+0.276 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.52 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.1395` → IC=+0.252 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1395 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8762` → IC=+0.241 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8762 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `3.625` → IC=+0.256 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.625 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.299 (n=1022)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.316 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.286 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.883` → IC=+0.298 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.883 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.585` → IC=+0.281 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.585 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.3468` → IC=+0.306 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3468 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `1.6378` → IC=+0.285 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6378 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.2257` → IC=+0.280 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2257 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.290 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `1883.1265` → IC=+0.305 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1883.1265 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.278 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.281)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2479` → IC=-0.211 (n=372)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2479
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=1123)

- **FILTRO** `ibs_20min` > `0.8032` → IC=-0.186 (n=482)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8032
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1454)

- **PATRÓN** `ibs_20min` > `0.8055` → IC=+0.152 (n=509)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.8055 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` > `0.4471` → IC=+0.217 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4471 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` < `0.2001` → IC=+0.193 (n=275)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2001 (IC base=-0.010)

- **PATRÓN** `volumen_regimen` < `0.9592` → IC=+0.216 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9592 (IC base=-0.010)

- **PATRÓN** `volumen_regimen` > `0.6225` → IC=+0.195 (n=319)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.6225 (IC base=-0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2647` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2647 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` < `2.0676` → IC=+0.241 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0676 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` > `1.3739` → IC=+0.220 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3739 (IC base=-0.010)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.260 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 110.0 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` > `0.1237` → IC=+0.214 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1237 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` < `1.1339` → IC=+0.183 (n=263)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.1339 (IC base=-0.013)

- **PATRÓN** `volumen_regimen` > `0.7255` → IC=+0.188 (n=235)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.7255 (IC base=-0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.7898` → IC=+0.253 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7898 (IC base=-0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.013)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.255 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 145.0 (IC base=-0.013)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6757` → IC=-0.212 (n=871)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6757
  - _Potencial_: sin este filtro IC_bueno=+0.263 (n=874)

- **FILTRO** `ibs_20min` > `0.7105` → IC=-0.232 (n=457)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7105
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=1377)

- **FILTRO** `sigma_ewma_delta_pct` > `4.635` → IC=-0.174 (n=427)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.635
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=1407)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.263 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6757 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1802` → IC=+0.314 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1802 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.469` → IC=+0.145 (n=271)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 9.469 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8657` → IC=+0.294 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8657 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.7204` → IC=+0.277 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7204 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.278 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.335 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4442` → IC=+0.319 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4442 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.321 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.1071` → IC=+0.199 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1071 (IC base=+0.004)

- **PATRÓN** `dist_vwap_pct` > `0.7726` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7726 (IC base=+0.004)

- **PATRÓN** `dist_vwap_pct` < `0.3939` → IC=+0.196 (n=403)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.3939 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.7148` → IC=+0.244 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7148 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.189 (n=352)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.195 (n=152)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.5876` → IC=+0.206 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5876 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4968` → IC=+0.181 (n=362)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4968 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.220 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.324 (n=719)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.274)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.291 (n=506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.274)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.347 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.274)

- **PATRÓN** `dist_vwap_pct` > `0.2632` → IC=+0.319 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2632 (IC base=+0.274)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.302 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.274)

- **PATRÓN** `volumen_regimen` > `0.6862` → IC=+0.290 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6862 (IC base=+0.274)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.303 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` < `1.5484` → IC=+0.281 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5484 (IC base=+0.274)

- **PATRÓN** `volumen_spike_ratio` > `2.2067` → IC=+0.281 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2067 (IC base=+0.274)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.278 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `2431.1711` → IC=+0.283 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2431.1711 (IC base=+0.274)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.270 (n=398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0073 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0145` → IC=+0.297 (n=796)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0145 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.284 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.395` → IC=+0.306 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.395 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.5341` → IC=+0.288 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5341 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.441` → IC=+0.290 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.441 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `1.2434` → IC=+0.305 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2434 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.243` → IC=+0.364 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.243 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.5387` → IC=+0.263 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5387 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1674` → IC=+0.272 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1674 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `2354.6422` → IC=+0.276 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2354.6422 (IC base=+0.269)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.175 (n=2132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0048 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.197 (n=2126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0106 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.3377` → IC=+0.173 (n=5606)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3377 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=6650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.5808` → IC=+0.213 (n=6370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5808 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.9321` → IC=+0.216 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9321 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.218` → IC=+0.247 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.218 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.2136` → IC=+0.161 (n=4230)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2136 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.157 (n=4230)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6232 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.1066` → IC=+0.183 (n=2496)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1066 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4521` → IC=+0.173 (n=2020)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4521 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.6612` → IC=+0.170 (n=2020)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.6612 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3832.0952` → IC=+0.168 (n=2123)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3832.0952 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.180 (n=5288)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 121.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.187 (n=4115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0064 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.205 (n=2058)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=2388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4698` → IC=+0.229 (n=6172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4698 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2207` → IC=+0.161 (n=4597)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2207 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.187` → IC=+0.195 (n=1063)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.187 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1819` → IC=+0.155 (n=4510)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1819 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6254` → IC=+0.150 (n=4511)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6254 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2924` → IC=+0.230 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2924 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5762` → IC=+0.173 (n=2427)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5762 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.2831` → IC=+0.175 (n=2500)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.2831 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.172 (n=5133)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 122.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.222 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.189 (n=361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0081 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3224` → IC=+0.200 (n=1082)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3224 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.206 (n=533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.034` → IC=+0.306 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.034 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.229` → IC=+0.236 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.229 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.5274` → IC=+0.173 (n=986)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.5274 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4242` → IC=+0.177 (n=987)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4242 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.241 (n=685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.248 (n=697)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1816` → IC=+0.289 (n=519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1816 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.239 (n=783)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.3384` → IC=+0.259 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3384 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.016` → IC=+0.251 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.016 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.233 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4302` → IC=+0.252 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4302 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.239 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1604.36` → IC=+0.256 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.36 (IC base=+0.236)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.252 (n=313)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.188 (n=312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.4211` → IC=+0.225 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4211 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2011` → IC=+0.208 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2011 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.216 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2628` → IC=+0.170 (n=934)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2628 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.0779` → IC=+0.159 (n=775)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0779 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2326` → IC=+0.189 (n=204)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2326 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.4154` → IC=+0.195 (n=300)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4154 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.4599` → IC=+0.159 (n=300)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4599 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `10126.7179` → IC=+0.176 (n=933)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 10126.7179 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.167 (n=1057)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.201 (n=353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.162 (n=979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.5415` → IC=+0.190 (n=1057)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5415 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.165 (n=1077)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.985` → IC=+0.212 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.985 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.161 (n=1057)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2129 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.176 (n=325)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.156 (n=946)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.166 (n=288)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 223.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.197 (n=1061)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0059 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.198` → IC=+0.205 (n=706)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.198 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.673` → IC=+0.271 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.673 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.2145` → IC=+0.185 (n=1017)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2145 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.1346` → IC=+0.185 (n=411)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1346 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.6619` → IC=+0.188 (n=331)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.6619 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `3.6109` → IC=+0.206 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6109 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.239 (n=884)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.225 (n=884)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.244 (n=295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.270 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.3478` → IC=+0.254 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3478 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.677` → IC=+0.275 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.677 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3607` → IC=+0.273 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3607 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.8509` → IC=+0.217 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8509 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `3.5248` → IC=+0.249 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5248 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1894.26` → IC=+0.241 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.26 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.214 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.224)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.179 (n=884)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0066 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4277` → IC=+0.165 (n=1004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4277 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.190 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3925` → IC=+0.203 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3925 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.185 (n=659)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.003` → IC=+0.246 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.003 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.159 (n=670)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8577 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `1.1917` → IC=+0.165 (n=335)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1917 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.222 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.5337` → IC=+0.164 (n=432)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5337 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5111` → IC=+0.181 (n=327)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5111 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `7103.5858` → IC=+0.185 (n=669)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7103.5858 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.151 (n=940)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 173.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.168 (n=1075)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0071 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3804` → IC=+0.146 (n=1075)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3804 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6028` → IC=+0.183 (n=1075)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6028 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1489` → IC=+0.148 (n=1077)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1489 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.871` → IC=+0.191 (n=208)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.871 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8541` → IC=+0.144 (n=717)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8541 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `0.6094` → IC=+0.132 (n=1075)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6094 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.205 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.142 (n=640)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7994 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.4786` → IC=+0.143 (n=320)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4786 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `10117.3478` → IC=+0.161 (n=488)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10117.3478 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.130 (n=889)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 175.0 (IC base=+0.132)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.145 (n=786)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0079 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.196 (n=1190)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0166` → IC=+0.221 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0166 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.474` → IC=+0.258 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.474 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2208` → IC=+0.121 (n=1178)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2208 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.134 (n=378)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=1217)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2901.0267` → IC=+0.188 (n=534)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2901.0267 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.130 (n=874)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.152 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0053 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.203 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5588 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.6834` → IC=+0.130 (n=217)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.6834 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.1825` → IC=+0.134 (n=1088)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1825 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.391` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.391 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.0407` → IC=+0.121 (n=1046)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0407 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.185 (n=141)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4623` → IC=+0.140 (n=348)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4623 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.179` → IC=+0.130 (n=473)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.179 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `3086.3351` → IC=+0.163 (n=396)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3086.3351 (IC base=+0.111)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0182` → IC=+0.212 (n=744)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0182 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1678` → IC=+0.215 (n=492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1678 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.725` → IC=+0.254 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.725 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `1.2244` → IC=+0.228 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2244 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.371` → IC=+0.240 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.371 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.207 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2075 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6122` → IC=+0.208 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6122 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.266 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1881` → IC=+0.215 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1881 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4271` → IC=+0.207 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4271 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.202 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.235 (n=398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.214 (n=540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.218 (n=399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.244 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1437` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1437 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2629` → IC=+0.204 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2629 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.312` → IC=+0.235 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.312 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6282` → IC=+0.217 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6282 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2444` → IC=+0.196 (n=928)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2444 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4604` → IC=+0.195 (n=1054)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4604 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2546.9804` → IC=+0.215 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2546.9804 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.154 (n=518)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0039 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.163 (n=517)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0089 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3431` → IC=+0.142 (n=1365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3431 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.3929` → IC=+0.168 (n=1551)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3929 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.8162` → IC=+0.170 (n=216)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.8162 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.678` → IC=+0.168 (n=715)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.678 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8703` → IC=+0.155 (n=894)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8703 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.169 (n=427)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.153 (n=496)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.5517` → IC=+0.163 (n=496)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5517 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=1732)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `11932.15` → IC=+0.151 (n=517)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11932.15 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.157 (n=1329)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 159.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.151 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0038 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.133 (n=1449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=1664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.158 (n=1449)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4872 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.1445` → IC=+0.122 (n=1399)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1445 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.998` → IC=+0.135 (n=477)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 5.998 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.124 (n=1461)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2216 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.1674` → IC=+0.143 (n=418)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1674 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.2373` → IC=+0.136 (n=1388)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2373 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2625.3161` → IC=+0.122 (n=1471)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2625.3161 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.126 (n=658)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 25.0 (IC base=+0.117)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.120 (n=364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.143 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 10.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.2815` → IC=+0.136 (n=363)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.2815 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.6466` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.6466 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.31` → IC=+0.143 (n=169)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.31 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `0.6135` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6135 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `10387.6961` → IC=+0.127 (n=363)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 10387.6961 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 151.0 (IC base=+0.101)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.213 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.157 (n=511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.153 (n=459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.3422` → IC=+0.208 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3422 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.149 (n=203)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.142` → IC=+0.138 (n=580)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 9.142 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.139 (n=511)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.218 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.7202` → IC=+0.157 (n=456)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7202 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.217 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1115` → IC=+0.161 (n=441)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1115 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4209` → IC=+0.144 (n=501)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4209 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.179 (n=160)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 154.0 (IC base=+0.136)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.260 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.203 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.223 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.246 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.388` → IC=+0.238 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.388 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.224 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.085` → IC=+0.235 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.085 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.204 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.223 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.247` → IC=+0.324 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.247 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.3759` → IC=+0.219 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3759 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.3885` → IC=+0.265 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3885 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `12317.9636` → IC=+0.210 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12317.9636 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.127 (n=413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0066 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.157 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.131 (n=280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 11.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.3044` → IC=+0.155 (n=276)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.3044 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.459` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 6.459 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `0.6874` → IC=+0.130 (n=182)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.6874 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` > `1.8165` → IC=+0.133 (n=262)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.8165 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3309` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3309
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=415)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.130 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.207 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.7807` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7807 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.234` → IC=+0.177 (n=156)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.234 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `1.0509` → IC=+0.121 (n=299)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0509 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `3074.7539` → IC=+0.215 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3074.7539 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 21.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.4783` → IC=+0.152 (n=337)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.4783 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.7121` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.7121 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.604` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.604 (IC base=+0.085)

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
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.192 (n=3665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0088 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=8446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.212 (n=8085)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8872` → IC=+0.195 (n=1044)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8872 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.75` → IC=+0.231 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.75 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8827` → IC=+0.166 (n=3620)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8827 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.189 (n=1523)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.6338` → IC=+0.181 (n=2569)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6338 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3811.2917` → IC=+0.168 (n=2694)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3811.2917 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.192 (n=5911)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 92.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.196 (n=4949)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0068 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.4819` → IC=+0.185 (n=7411)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4819 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=2804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5606` → IC=+0.240 (n=7410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5606 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2311` → IC=+0.164 (n=4698)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2311 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.844` → IC=+0.196 (n=1063)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.844 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.683` → IC=+0.183 (n=7165)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.683 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.159 (n=2256)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7049 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.2035` → IC=+0.160 (n=1710)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.2035 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.248 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.2995` → IC=+0.191 (n=3026)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.2995 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.193 (n=2123)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 25.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.210 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.208 (n=910)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.195 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.366` → IC=+0.290 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.366 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.239 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.5474` → IC=+0.180 (n=561)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5474 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.2375` → IC=+0.193 (n=577)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.2375 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.257 (n=1060)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.264 (n=1059)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.2039` → IC=+0.283 (n=707)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2039 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.3469` → IC=+0.287 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3469 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.416` → IC=+0.263 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.416 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.224` → IC=+0.305 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.224 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `1.88` → IC=+0.279 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.88 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1747.06` → IC=+0.275 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1747.06 (IC base=+0.255)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.194 (n=433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3567` → IC=+0.151 (n=1285)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3567 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3159` → IC=+0.199 (n=1285)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3159 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.3247` → IC=+0.195 (n=489)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3247 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.921` → IC=+0.152 (n=435)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 6.921 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.296` → IC=+0.153 (n=1143)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.296 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6976` → IC=+0.180 (n=566)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6976 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.265` → IC=+0.179 (n=185)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.265 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1166` → IC=+0.156 (n=1084)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1166 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7596` → IC=+0.157 (n=821)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7596 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `10925.7104` → IC=+0.164 (n=1148)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 10925.7104 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `488.0` → IC=+0.160 (n=1165)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 488.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.171 (n=1146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.263` → IC=+0.168 (n=1008)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.263 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.6377` → IC=+0.206 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6377 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6888` → IC=+0.165 (n=171)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.6888 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.1271` → IC=+0.165 (n=1059)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1271 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.197` → IC=+0.166 (n=567)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.197 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2029` → IC=+0.163 (n=1145)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2029 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1513` → IC=+0.209 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1513 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.4236` → IC=+0.169 (n=1048)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.4236 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `12561.7266` → IC=+0.156 (n=763)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12561.7266 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `366.0` → IC=+0.168 (n=633)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 366.0 (IC base=+0.154)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.227 (n=1289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.213 (n=1313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.6711` → IC=+0.248 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6711 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.548` → IC=+0.302 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.548 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.2161` → IC=+0.215 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2161 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.9896` → IC=+0.232 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9896 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.239 (n=1225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.236 (n=817)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.257 (n=459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3636` → IC=+0.269 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3636 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.708` → IC=+0.275 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.708 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.298 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7962` → IC=+0.226 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7962 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2488` → IC=+0.235 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2488 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.247 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1898.5935` → IC=+0.242 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1898.5935 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.261 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.177 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0034 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4371` → IC=+0.139 (n=1372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4371 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6988` → IC=+0.230 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6988 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.5582` → IC=+0.176 (n=368)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5582 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.195` → IC=+0.160 (n=578)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.195 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8773` → IC=+0.161 (n=915)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8773 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.227 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.5114` → IC=+0.145 (n=581)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5114 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.409` → IC=+0.149 (n=1319)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.409 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8736.9866` → IC=+0.228 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8736.9866 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.167 (n=415)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 85.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.163 (n=1113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0076 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.445` → IC=+0.161 (n=1111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.445 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=500)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6856` → IC=+0.196 (n=1111)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6856 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.2048` → IC=+0.145 (n=1036)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2048 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.009` → IC=+0.192 (n=167)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.009 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.194` → IC=+0.143 (n=1038)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.194 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.150 (n=489)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6958 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `1.1764` → IC=+0.154 (n=371)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1764 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.274 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.4741` → IC=+0.173 (n=347)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.4741 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `11048.3545` → IC=+0.205 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11048.3545 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4694` → IC=+0.182 (n=1383)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.4694 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0059` → IC=+0.183 (n=244)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 1.0059 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.395` → IC=+0.225 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.395 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=958)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2920.0962` → IC=+0.239 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2920.0962 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.124 (n=1038)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 53.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.175 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1279` → IC=+0.154 (n=446)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1279 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.6371` → IC=+0.208 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6371 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.4678` → IC=+0.129 (n=1312)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4678 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.446` → IC=+0.127 (n=1286)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.446 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.7204` → IC=+0.150 (n=589)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.7204 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2225` → IC=+0.168 (n=206)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2225 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4645` → IC=+0.151 (n=394)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4645 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.2313` → IC=+0.122 (n=535)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 2.2313 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2899.8099` → IC=+0.163 (n=446)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2899.8099 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0184` → IC=+0.215 (n=930)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0184 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.5111` → IC=+0.245 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5111 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1818` → IC=+0.232 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1818 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.372` → IC=+0.248 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.372 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2457` → IC=+0.209 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2457 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6303` → IC=+0.209 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6303 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.230 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.5673` → IC=+0.237 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5673 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2586.8192` → IC=+0.210 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2586.8192 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.234 (n=512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.226 (n=512)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5122` → IC=+0.253 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5122 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.2661` → IC=+0.206 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2661 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.724` → IC=+0.262 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.724 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.234 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.257 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2259` → IC=+0.194 (n=1192)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2259 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4438` → IC=+0.198 (n=1354)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4438 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1007)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=2591)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.155 (n=2233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0094 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5263` → IC=+0.156 (n=2536)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5263 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.160 (n=883)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9389` → IC=+0.213 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9389 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1877` → IC=+0.156 (n=829)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1877 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.736` → IC=+0.168 (n=819)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.736 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.9082` → IC=+0.151 (n=1031)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9082 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1737` → IC=+0.175 (n=694)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1737 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4626` → IC=+0.162 (n=837)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4626 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.9066` → IC=+0.157 (n=1673)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9066 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8243.4336` → IC=+0.154 (n=1150)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8243.4336 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.188 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4875` → IC=+0.153 (n=1955)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4875 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.159 (n=655)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.1823` → IC=+0.161 (n=860)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1823 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.7051` → IC=+0.142 (n=347)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.7051 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.306` → IC=+0.142 (n=1938)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.306 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.1144` → IC=+0.142 (n=1633)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1144 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.151 (n=920)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.5707` → IC=+0.138 (n=1936)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5707 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.145 (n=1290)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=2591)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `7675.4145` → IC=+0.150 (n=1747)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7675.4145 (IC base=+0.134)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.171 (n=284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0035 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.185 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.192 (n=212)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5413 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2289` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2289 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.25` → IC=+0.164 (n=400)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 8.25 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.2448` → IC=+0.158 (n=317)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2448 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.832` → IC=+0.190 (n=211)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.832 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.3073` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3073 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.213 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.7581` → IC=+0.194 (n=106)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.7581 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `12617.0993` → IC=+0.205 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12617.0993 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.206 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.145 (n=874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.157` → IC=+0.162 (n=385)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.157 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.6152` → IC=+0.139 (n=397)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.6152 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.7085` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.7085 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.2266` → IC=+0.133 (n=902)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2266 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.273` → IC=+0.155 (n=854)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.273 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.177 (n=583)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8847 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.163 (n=413)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.5707` → IC=+0.140 (n=871)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5707 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.8153` → IC=+0.145 (n=581)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8153 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `11358.9394` → IC=+0.148 (n=874)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11358.9394 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `712.0` → IC=+0.138 (n=829)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 712.0 (IC base=+0.132)

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
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.152 (n=752)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0088 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.150 (n=752)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0045 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.5046` → IC=+0.154 (n=752)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.5046 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.151 (n=273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 4.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.185` → IC=+0.155 (n=752)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.185 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.9629` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.9629 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.4235` → IC=+0.152 (n=716)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4235 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.153 (n=751)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.9097` → IC=+0.149 (n=502)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.9097 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `1.2651` → IC=+0.152 (n=251)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.2651 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1758` → IC=+0.162 (n=223)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1758 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.167 (n=247)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=714)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `8191.84` → IC=+0.150 (n=752)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8191.84 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.160 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0071 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.5119` → IC=+0.178 (n=616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.5119 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.7429` → IC=+0.147 (n=616)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.7429 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.159 (n=616)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.1001 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1574` → IC=+0.170 (n=277)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1574 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.4003` → IC=+0.146 (n=634)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.4003 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.802` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 10.802 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.6472` → IC=+0.173 (n=206)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6472 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` > `0.7262` → IC=+0.153 (n=551)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7262 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.177 (n=264)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.162 (n=533)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.4522` → IC=+0.161 (n=605)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4522 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `8169.7182` → IC=+0.170 (n=616)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8169.7182 (IC base=+0.146)

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

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.034)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.250 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=296)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=298)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.215 (n=307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.170 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 18.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.6355` → IC=+0.214 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6355 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.1307` → IC=+0.171 (n=314)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1307 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.072` → IC=+0.222 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.072 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.7974` → IC=+0.134 (n=400)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.7974 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` > `0.977` → IC=+0.128 (n=272)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.977 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.212 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `2.4899` → IC=+0.162 (n=492)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4899 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=486)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.154 (n=261)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0688` → IC=+0.278 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0688 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.6098` → IC=+0.138 (n=161)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.6098 (IC base=-0.025)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5781` → IC=-0.186 (n=68)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5781
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=206)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.178 (n=237)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0061 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.5781` → IC=+0.211 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5781 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.4026` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4026 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.734` → IC=+0.129 (n=130)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 3.734 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.0527` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0527 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.0198` → IC=+0.200 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0198 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2974.9985` → IC=+0.126 (n=172)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2974.9985 (IC base=+0.106)

- **PATRÓN** `drift_60min` |x|≤ `0.0426` → IC=+0.224 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0426 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5693` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5693 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.9523` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.9523 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.0849` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0849 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.1644` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1644 (IC base=+0.048)

- **PATRÓN** `libro_liquidez` > `3267.3803` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3267.3803 (IC base=+0.048)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.306 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=91)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.222 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=68)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.175 (n=161)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.005 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.248 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.1205` → IC=+0.188 (n=110)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1205 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.0654` → IC=+0.152 (n=208)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0654 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6313` → IC=+0.154 (n=186)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6313 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.185 (n=106)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.3845` → IC=+0.163 (n=158)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.3845 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=218)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `1103.6894` → IC=+0.196 (n=182)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1103.6894 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.2452` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2452 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `2.4519` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4519 (IC base=-0.066)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.163 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.006 (IC base=+0.086)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.197 (n=186)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.6744 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.8682` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.8682 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `1.0643` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.0643 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.179 (n=79)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `2.1825` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1825 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.5314` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5314 (IC base=+0.086)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.143 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.006 (IC base=-0.077)

- **PATRÓN** `ibs_20min` < `0.1154` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1154 (IC base=-0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.966` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.966 (IC base=-0.077)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1376` → IC=-0.333 (n=40)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1376
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=121)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.429 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=123)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.343 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=98)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=127)

- **FILTRO** `sigma_ewma_delta_pct` > `8.432` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.432
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=118)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=45)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=38)

- **FILTRO** `sigma_ewma_delta_pct` > `2.588` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.588
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=33)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=41)

- **FILTRO** `dist_vwap_pct` > `0.2409` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2409
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=43)

- **FILTRO** `sigma_ewma_delta_pct` > `3.354` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.354
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=36)

- **FILTRO** `volumen_regimen` > `0.8664` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8664
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=40)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8218` → IC=-0.450 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8218
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **FILTRO** `dist_vwap_pct` > `0.0599` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0599
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=34)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.309 (n=19)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2345` → IC=-0.136 (n=108)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2345
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=211)

- **FILTRO** `dist_vwap_pct` > `0.6344` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6344
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=294)

- **PATRÓN** `ibs_20min` > `0.6592` → IC=+0.161 (n=222)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6592 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.2345` → IC=+0.124 (n=211)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2345 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `3805.194` → IC=+0.158 (n=109)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3805.194 (IC base=+0.036)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

- **FILTRO** `ibs_20min` < `0.5548` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5548
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=74)

- **FILTRO** `volumen_regimen` < `0.7777` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7777
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=74)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1435 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.9499` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.9499 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.158 (n=109)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.099)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.8361` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8361
  - _Potencial_: sin este filtro IC_bueno=+0.209 (n=53)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=77)

- **FILTRO** `ibs_20min` > `0.3236` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3236
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=77)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.167 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0042 (IC base=+0.080)

- **PATRÓN** `drift_60min` |x|≤ `0.2791` → IC=+0.129 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.2791 (IC base=+0.080)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.080)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8361 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.0869` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.0869 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.1989` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1989 (IC base=+0.080)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `1558.1749` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1558.1749 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.000)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.55` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=56)

- **FILTRO** `volumen_regimen` < `1.0339` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0339
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=36)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.172 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0058 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.167 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 17.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.7143` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7143 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.7143 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.1961` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1961 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.5494` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5494 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.0808` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0808 (IC base=-0.041)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.160 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 16.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.130 (n=503)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.5 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2842.803` → IC=+0.182 (n=174)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2842.803 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2318.1516` → IC=+0.121 (n=579)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2318.1516 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.160 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 16.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.130 (n=503)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.5 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2842.803` → IC=+0.182 (n=174)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2842.803 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2318.1516` → IC=+0.121 (n=579)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2318.1516 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=108)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=125)

- **FILTRO** `libro_liquidez` < `2415.4574` → IC=-0.284 (n=35)

  - _Acción_: SKIP cuando `libro_liquidez` < 2415.4574
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=106)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=194)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=180)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `libro_liquidez` < `15120.4031` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 15120.4031
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1370)

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
- **FILTRO** `liq_usd_total` < `33209.41` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `liq_usd_total` < 33209.41
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

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

- **PATRÓN** `liq_usd_total` > `61042.02` → IC=+0.186 (n=68)

  - _Acción_: Kelly boost +0.93€ cuando `liq_usd_total` > 61042.02 (IC base=+0.029)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.495 (IC base=+0.029)

- **PATRÓN** `libro_liquidez` > `15568.3857` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 15568.3857 (IC base=+0.029)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=608)

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
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=420)

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
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=77)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=427)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=269)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=269)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.200 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=236)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=161)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=161)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=98)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.151 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=165)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9998` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9998
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=60)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=64)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=98)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6654)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1058)

- **FILTRO** `libro_liquidez` < `15906.9303` → IC=-0.152 (n=268)

  - _Acción_: SKIP cuando `libro_liquidez` < 15906.9303
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=805)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.181 (n=2778)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=8481)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.172 (n=2870)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=8862)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.215 (n=475)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=1436)

- **FILTRO** `ibs_20min` < `0.748` → IC=-0.179 (n=475)

  - _Acción_: SKIP cuando `ibs_20min` < 0.748
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=1436)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.169 (n=487)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=1608)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.206 (n=474)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=1481)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.221 (n=489)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1582)

- **FILTRO** `ibs_20min` > `0.2846` → IC=-0.161 (n=517)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2846
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=1554)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.202 (n=457)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1427)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.194 (n=508)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1561)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=2465)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=2532)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=2538)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=306)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=195)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=174)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=646)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.038)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=8036)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=18205)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.283 (n=6206)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=20035)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.245 (n=6504)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=19737)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.161 (n=8916)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=17325)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.225 (n=8244)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=24794)

- **FILTRO** `ibs_7min` > `0.2955` → IC=-0.176 (n=8258)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2955
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=24780)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=1302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=2940)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1005)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3237)

- **FILTRO** `ibs_7min` < `0.7069` → IC=-0.261 (n=1399)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7069
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2843)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.197 (n=976)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3266)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.150 (n=3842)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1895)

- **FILTRO** `drift_7min_pct` |x|> `0.1108` → IC=-0.123 (n=1947)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1108
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3790)

- **FILTRO** `ibs_7min` > `0.7976` → IC=-0.205 (n=1433)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7976
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=4304)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1056)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3520)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.259 (n=1083)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3493)

- **FILTRO** `ibs_7min` < `0.7548` → IC=-0.189 (n=1144)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7548
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3432)

- **FILTRO** `ballena_activa_n` > `162.0` → IC=-0.179 (n=1140)

  - _Acción_: SKIP cuando `ballena_activa_n` > 162.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3436)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.257 (n=1111)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3556)

- **FILTRO** `ibs_7min` > `0.2546` → IC=-0.170 (n=1166)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2546
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3501)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.184 (n=1161)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3506)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.181 (n=970)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=2994)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.317 (n=955)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3009)

- **FILTRO** `drift_7min_pct` |x|> `0.1797` → IC=-0.133 (n=1347)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1797
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=2617)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.273 (n=982)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=2982)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.221 (n=920)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=3044)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.235 (n=1417)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=4634)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.155 (n=2053)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3998)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=1374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=2952)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.253 (n=1061)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3265)

- **FILTRO** `ibs_7min` < `0.7427` → IC=-0.190 (n=1080)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7427
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3246)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.186 (n=1068)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=3258)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1096)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3347)

- **FILTRO** `ibs_7min` > `0.2743` → IC=-0.175 (n=1110)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2743
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3333)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.183 (n=1088)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3355)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.258 (n=1133)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3566)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.233 (n=1147)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3552)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.169 (n=1526)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4730)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=1346)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=3088)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.282 (n=1100)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=3334)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.236 (n=1106)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3328)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1083)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3351)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.206 (n=1393)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=4491)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=973)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=486)

- **FILTRO** `libro_liquidez` < `10509.8872` → IC=-0.152 (n=133)

  - _Acción_: SKIP cuando `libro_liquidez` < 10509.8872
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=399)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=313)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=533)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.136 (n=655)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.159 (n=218)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 453.526 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3725.3423` → IC=+0.125 (n=297)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 3725.3423 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.130 (n=544)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 60.0 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.160 (n=51)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `311.907` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 311.907 (IC base=+0.132)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.185 (n=90)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.102)

- **PATRÓN** `total_vol_5m` < `672.2721` → IC=+0.169 (n=119)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 672.2721 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 70.0 (IC base=+0.102)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.399` → IC=+0.198 (n=117)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio` |x|> 0.399 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.217 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `7671.127` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 7671.127 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 37.0 (IC base=+0.150)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.161 (n=110)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.152 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 13.0 (IC base=+0.120)

- **PATRÓN** `total_vol_5m` < `425122.3` → IC=+0.135 (n=124)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 425122.3 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.237 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.120)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.327 (n=102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=199)

- **FILTRO** `T_h` > `52.6662` → IC=-0.204 (n=201)

  - _Acción_: SKIP cuando `T_h` > 52.6662
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=100)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.179 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0039 (IC base=-0.120)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.357 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=48)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.119)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.234 (n=231)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **FILTRO** `T_h` > `71.1632` → IC=-0.200 (n=231)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=79)

- **FILTRO** `pct_vs_K` |x|> `2.84` → IC=-0.421 (n=125)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.84
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=126)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.194 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

- **FILTRO** `T_h` > `63.9918` → IC=-0.209 (n=84)

  - _Acción_: SKIP cuando `T_h` > 63.9918
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=68)

- **FILTRO** `pct_vs_K` |x|> `3.0033` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0033
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=62)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` < `87.9808` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `T_h` < 87.9808
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=59)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.283 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=65)

- **FILTRO** `sigma_h` < `0.004` → IC=-0.370 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=65)

- **FILTRO** `T_h` > `61.3303` → IC=-0.318 (n=64)

  - _Acción_: SKIP cuando `T_h` > 61.3303
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0126` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0126
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=47)

- **FILTRO** `sigma_h` < `0.01` → IC=-0.230 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=35)

- **FILTRO** `T_h` > `135.927` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `T_h` > 135.927
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=53)

- **FILTRO** `sigma_h` < `0.0129` → IC=-0.344 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `T_h` > `84.9421` → IC=-0.361 (n=34)

  - _Acción_: SKIP cuando `T_h` > 84.9421
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=12)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.15` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.15 (IC base=+0.371)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.468 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.371)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.468 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.371)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.469 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.371)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.371)

- **PATRÓN** `edge` > `0.1023` → IC=+0.454 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.406)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.466 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.406)

- **PATRÓN** `T_h` > `0.8072` → IC=+0.423 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8072 (IC base=+0.406)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.487 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.406)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.477)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.460 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.477)

- **PATRÓN** `edge` > `0.2335` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2335 (IC base=+0.477)

- **PATRÓN** `sigma_h` < `0.0144` → IC=+0.483 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0144 (IC base=+0.477)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.466 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.477)

- **PATRÓN** `T_h` > `0.8977` → IC=+0.466 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8977 (IC base=+0.477)

- **PATRÓN** `dist_50` > `0.4421` → IC=+0.483 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4421 (IC base=+0.477)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.465 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.477)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.470 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.477)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=138)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=231)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.016)

- **PATRÓN** `streak_estiramiento` < `0.5577` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `streak_estiramiento` < 0.5577 (IC base=+0.039)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `991078.0` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 991078.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=25)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_racha` < 991078.0 (IC base=+0.010)

- **PATRÓN** `streak_estiramiento` < `0.3893` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.3893 (IC base=+0.010)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=75)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=85)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=598)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=604)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=317)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `streak_len` < 4.0 (IC base=+0.013)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=483)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=979)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=577)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=599)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2431)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1253)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1261)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.193 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0041 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.221 (n=524)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.0771` → IC=+0.182 (n=508)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0771 (IC base=+0.178)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.179 (n=1155)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.178)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1355` → IC=+0.232 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1355 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.187 (n=815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 11.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_15` > `0.619` → IC=+0.251 (n=1156)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.619 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.4191` → IC=+0.172 (n=272)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.4191 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.179 (n=751)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.817` → IC=+0.242 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.817 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `4928.6279` → IC=+0.182 (n=524)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4928.6279 (IC base=+0.178)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=392)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.213 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.263 (n=95)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.193)

- **PATRÓN** `drift_15min` |x|≤ `0.3775` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3775 (IC base=+0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2245` → IC=+0.241 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2245 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.211 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.193)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.249 (n=285)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.3789` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3789 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.099` → IC=+0.195 (n=198)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.099 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.624` → IC=+0.245 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.624 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `11757.2155` → IC=+0.219 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11757.2155 (IC base=+0.193)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.174 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0034 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.151 (n=127)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0057 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.174 (n=93)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2712` → IC=+0.167 (n=184)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2712 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.159 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.151 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.6467` → IC=+0.230 (n=279)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6467 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1439` → IC=+0.164 (n=218)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1439 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `10004.8873` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 10004.8873 (IC base=+0.141)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=62)

- **FILTRO** `ibs_15` > `0.1909` → IC=-0.224 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1909
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=55)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.160 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=157)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.199 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0078 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.169 (n=158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.190 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2704` → IC=+0.190 (n=98)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2704 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.178 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.242 (n=157)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.5654` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.5654 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=129)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3004.732` → IC=+0.253 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.732 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.143)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5695` → IC=-0.142 (n=118)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5695
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=620)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0155` → IC=+0.257 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0155 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0859` → IC=+0.203 (n=143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0859 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0439` → IC=+0.199 (n=324)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0439 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0933` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0933 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.241 (n=160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.5488` → IC=+0.282 (n=324)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5488 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1137` → IC=+0.206 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1137 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.928` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.928 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.189 (n=355)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2841.8146` → IC=+0.264 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2841.8146 (IC base=+0.188)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.171 (n=366)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` < 0.1111 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.372 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.334)

- **PATRÓN** `drift_60min` |x|≤ `0.1544` → IC=+0.340 (n=286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1544 (IC base=+0.334)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.344 (n=216)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.334)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2192` → IC=+0.372 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2192 (IC base=+0.334)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.351 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.334)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.374 (n=324)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.334)

- **PATRÓN** `dist_vwap_pct` > `0.4117` → IC=+0.379 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4117 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.085` → IC=+0.342 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.085 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.333 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.334)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.341 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.334)

- **PATRÓN** `libro_liquidez` > `3397.72` → IC=+0.350 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3397.72 (IC base=+0.334)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1228` → IC=+0.342 (n=80)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1228 (IC base=+0.335)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.332 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.371 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.345 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.335)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.344 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.335)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.414 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.348 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.335)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.333 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.335)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.368 (n=180)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.343 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `9300.6023` → IC=+0.352 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9300.6023 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `472.0` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 472.0 (IC base=+0.335)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.367 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.330)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.330 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.330)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.336 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.330)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.348 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.330)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.349 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.330)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.384 (n=144)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.348 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` < `0.1061` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1061 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.367 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.330)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.346 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `3553.0968` → IC=+0.357 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3553.0968 (IC base=+0.330)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.331 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.330)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.205 (n=551)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1654)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.180 (n=704)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1501)

- **FILTRO** `libro_liquidez` < `3796.054` → IC=-0.123 (n=1455)

  - _Acción_: SKIP cuando `libro_liquidez` < 3796.054
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=750)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.248 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.059)

- **PATRÓN** `ibs_15` > `0.6187` → IC=+0.255 (n=550)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6187 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.176 (n=433)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.266 (IC base=-0.059)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1174` → IC=+0.235 (n=816)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1174 (IC base=-0.042)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1825` → IC=+0.243 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1825 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.282 (n=1225)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.6509` → IC=+0.262 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6509 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.210 (n=332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1002)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.226 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=894)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.205 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=485)

- **FILTRO** `sigma_ewma_delta_pct` > `19.873` → IC=-0.241 (n=237)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.873
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1097)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.170 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0026 (IC base=+0.071)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1156` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1156 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.333 (n=112)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.259 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.3434` → IC=+0.260 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3434 (IC base=+0.071)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6537` → IC=-0.222 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6537
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=270)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=341)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.142 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0066 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.169 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.004 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.211 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.139)

- **PATRÓN** `drift_15min` |x|≤ `0.4631` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.4631 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.240 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.257 (n=270)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.177 (n=193)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.775` → IC=+0.148 (n=211)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.775 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=341)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.252 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.230)

- **PATRÓN** `drift_60min` |x|≤ `0.4382` → IC=+0.232 (n=513)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4382 (IC base=+0.230)

- **PATRÓN** `drift_15min` |x|≤ `0.7762` → IC=+0.239 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7762 (IC base=+0.230)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2412` → IC=+0.257 (n=171)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2412 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.241 (n=345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `ibs_15` < `0.2758` → IC=+0.288 (n=451)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2758 (IC base=+0.230)

- **PATRÓN** `dist_vwap_pct` > `0.7529` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7529 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.004` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.004 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.033` → IC=+0.238 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.033 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `3591.8273` → IC=+0.232 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3591.8273 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.232 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.230)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.8825` → IC=-0.248 (n=133)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8825
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=400)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.219 (n=201)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=332)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.156)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.156)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0717` → IC=+0.207 (n=220)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0717 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.254 (n=246)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1586` → IC=+0.210 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1586 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0194` → IC=-0.265 (n=330)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0194
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=331)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=487)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0826` → IC=+0.347 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0826 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3443` → IC=+0.312 (n=355)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3443 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `1.0781` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0781 (IC base=-0.044)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.138 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0064 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.4393` → IC=+0.167 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4393 (IC base=+0.105)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.105)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.138 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0064 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.4393` → IC=+0.167 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4393 (IC base=+0.105)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.105)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.289 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.288 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.310 (n=182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.290 (n=364)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.320 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8374` → IC=+0.323 (n=546)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8374 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2686` → IC=+0.324 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2686 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.322 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.288 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `12722.4964` → IC=+0.300 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12722.4964 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.290 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.286 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0588` → IC=+0.317 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0588 (IC base=+0.276)

- **PATRÓN** `drift_15min` |x|≤ `0.3883` → IC=+0.279 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3883 (IC base=+0.276)

- **PATRÓN** `delta_ratio_macro` |x|> `0.246` → IC=+0.277 (n=101)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.246 (IC base=+0.276)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3684` → IC=+0.293 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3684 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.330 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` > `0.8242` → IC=+0.297 (n=303)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8242 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2601` → IC=+0.335 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2601 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `15745.2501` → IC=+0.316 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15745.2501 (IC base=+0.276)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.304 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.304 (n=243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.307 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1881` → IC=+0.312 (n=110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1881 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.339 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.342 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.341 (n=243)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.312 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` < `0.4471` → IC=+0.300 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4471 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.322 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `11789.5205` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11789.5205 (IC base=+0.297)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.297 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.297)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.085` → IC=-0.273 (n=64)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.085
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=194)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.253 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=171)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.161 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=322)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1792` → IC=-0.140 (n=73)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1792
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=74)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2395` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2395
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=69)

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
- **PATRÓN** `T_h` > `73.926` → IC=+0.140 (n=231)

  - _Acción_: Kelly boost +0.70€ cuando `T_h` > 73.926 (IC base=+0.138)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.319 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.138)

- **PATRÓN** `T_h` > `145.8408` → IC=+0.407 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8408 (IC base=+0.350)

- **PATRÓN** `ratio` > `1.01` → IC=+0.386 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.350)

### WEEKLY_PRICE#BTC
- **FILTRO** `ratio` > `0.9933` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `ratio` > 0.9933
  - _Potencial_: sin este filtro IC_bueno=+0.282 (n=76)

- **PATRÓN** `T_h` > `144.522` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `T_h` > 144.522 (IC base=+0.096)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.096)

- **PATRÓN** `T_h` > `87.9969` → IC=+0.314 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9969 (IC base=+0.307)

- **PATRÓN** `ratio` > `1.0413` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0413 (IC base=+0.307)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9882` → IC=+0.216 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9882 (IC base=+0.193)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.193)

- **PATRÓN** `T_h` > `93.2998` → IC=+0.350 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 93.2998 (IC base=+0.331)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.382 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.331)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.405)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.619 sube el IC de +0.178 a +0.251 en UPDOWN_GBM#15min (n=1156). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.193 a +0.249 en UPDOWN_GBM#BTC#15min (n=285). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6467 sube el IC de +0.141 a +0.230 en UPDOWN_GBM#ETH#15min (n=279). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.143 a +0.242 en UPDOWN_GBM#SOL#15min (n=157). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5488 sube el IC de +0.188 a +0.282 en UPDOWN_GBM#XRP#15min (n=324). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.045 a +0.171 en UPDOWN_GBM#XRP#15min (n=366). Ya aplicado como kelly_boost=+0.86€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6187 sube el IC de -0.059 a +0.255 en UPDOWN_GBM_15M_TARDIO (n=550). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3605 sube el IC de -0.042 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=1225). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.071 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=112). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.139 a +0.257 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=270). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2758 sube el IC de +0.230 a +0.288 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=451). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.156 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.042 a +0.254 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3443 sube el IC de -0.044 a +0.312 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=355). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8374 sube el IC de +0.286 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=546). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8242 sube el IC de +0.276 a +0.297 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=303). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.297 a +0.341 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=243). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.334 a +0.374 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=324). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.335 a +0.368 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.330 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=144). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1166 | +0.084 | +143.02€ | 2 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1166 | +0.084 | +143.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 843 | +0.090 | +117.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 843 | +0.090 | +117.65€ | 3 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 242 | +0.045 | +4.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 242 | +0.045 | +4.70€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 55 | +0.167 | +22.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 55 | +0.167 | +22.18€ | 0 | 5 |
| ✅ BALLENAS_TARDIAS | 21376 | -0.097 | -3136.11€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1272 | -0.050 | -194.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 20104 | -0.100 | -2941.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3298 | -0.103 | -565.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3298 | -0.103 | -565.99€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1272 | -0.050 | -194.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1272 | -0.050 | -194.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6120 | -0.040 | -601.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6120 | -0.040 | -601.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5677 | -0.100 | -480.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5677 | -0.100 | -480.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4635 | -0.172 | -1132.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4635 | -0.172 | -1132.58€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 13266 | -0.039 | +4195.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3542 | -0.005 | +1834.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 9724 | -0.051 | +2361.00€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 13266 | -0.039 | +4195.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3542 | -0.005 | +1834.85€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 9724 | -0.051 | +2361.00€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1156 | -0.104 | -167.69€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 94 | -0.052 | -11.21€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1062 | -0.109 | -156.48€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 661 | -0.087 | -80.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 70 | -0.042 | -5.99€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 591 | -0.092 | -74.59€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 321 | -0.153 | -73.17€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 297 | -0.159 | -67.95€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 113 | -0.048 | -13.80€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 113 | -0.048 | -13.80€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 77560 | +0.113 | -3936.69€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 12035 | +0.183 | -363.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 298 | -0.120 | -46.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 59932 | +0.101 | -3378.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5295 | +0.113 | -149.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 9982 | +0.097 | -913.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 39 | -0.159 | -2.72€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 9928 | +0.099 | -898.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 15682 | +0.132 | -303.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3705 | +0.203 | -108.34€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 9929 | +0.110 | -176.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2006 | +0.114 | +3.06€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 10022 | +0.089 | -976.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 47 | -0.051 | -1.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 9960 | +0.090 | -963.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 16592 | +0.125 | -295.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4649 | +0.173 | -71.96€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 10025 | +0.108 | -161.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1906 | +0.098 | -53.07€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 15283 | +0.115 | -881.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3555 | +0.185 | -189.65€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 201 | -0.081 | +7.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 10144 | +0.092 | -600.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1383 | +0.133 | -99.02€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 9999 | +0.103 | -567.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 40 | +0.000 | +10.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 9946 | +0.104 | -578.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 12248 | +0.189 | -848.84€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 12248 | +0.189 | -848.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2998 | +0.167 | -329.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2998 | +0.167 | -329.78€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 727 | +0.183 | +0.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 727 | +0.183 | +0.85€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2933 | +0.178 | -267.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2933 | +0.178 | -267.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2633 | +0.236 | -84.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2633 | +0.236 | -84.67€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2878 | +0.191 | -181.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2878 | +0.191 | -181.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 570 | +0.434 | -10.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 570 | +0.434 | -10.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 219 | +0.437 | -2.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 219 | +0.437 | -2.22€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 216 | +0.440 | +0.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 216 | +0.440 | +0.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 127 | +0.407 | -7.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 127 | +0.407 | -7.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 41923 | +0.195 | -3476.35€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 41923 | +0.195 | -3476.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 7296 | +0.171 | -916.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 7296 | +0.171 | -916.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6662 | +0.224 | -240.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6662 | +0.224 | -240.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7259 | +0.170 | -914.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7259 | +0.170 | -914.87€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6756 | +0.217 | -287.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6756 | +0.217 | -287.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6916 | +0.203 | -467.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6916 | +0.203 | -467.22€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 7034 | +0.191 | -650.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 7034 | +0.191 | -650.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 15717 | +0.125 | +307.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 15717 | +0.125 | +307.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7797 | +0.129 | +203.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7797 | +0.129 | +203.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7920 | +0.121 | +104.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7920 | +0.121 | +104.24€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1278 | +0.287 | -26.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1278 | +0.287 | -26.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 567 | +0.270 | -25.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 567 | +0.270 | -25.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 610 | +0.292 | -1.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 610 | +0.292 | -1.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 101 | +0.335 | -0.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 101 | +0.335 | -0.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 560 | +0.432 | -6.01€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 560 | +0.432 | -6.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 262 | +0.432 | -3.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 262 | +0.432 | -3.29€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 259 | +0.435 | -2.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 259 | +0.435 | -2.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 39 | +0.378 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 39 | +0.378 | -0.28€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 895 | +0.072 | -41.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 316 | +0.057 | -27.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 579 | +0.080 | -13.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 699 | +0.081 | -16.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 120 | +0.082 | -3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 579 | +0.080 | -13.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 141 | +0.004 | -28.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 141 | +0.004 | -28.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 28028 | +0.099 | -816.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2355 | +0.095 | +37.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 25673 | +0.099 | -854.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 15933 | +0.103 | -222.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2355 | +0.095 | +37.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 13578 | +0.104 | -260.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4964 | +0.115 | +43.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4964 | +0.115 | +43.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 7131 | +0.078 | -636.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 7131 | +0.078 | -636.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 736 | +0.242 | -91.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 736 | +0.242 | -91.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 736 | +0.242 | -91.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 736 | +0.242 | -91.58€ | 0 | 4 |
| ✅ GBM_LATE_15M | 20603 | +0.076 | +9278.74€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 20603 | +0.076 | +9278.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3381 | +0.193 | +2444.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3381 | +0.193 | +2444.26€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 3047 | +0.174 | +2047.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3047 | +0.174 | +2047.48€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 3531 | +0.195 | +2588.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3531 | +0.195 | +2588.57€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 3077 | +0.007 | +486.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3077 | +0.007 | +486.78€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 3015 | -0.037 | +647.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3015 | -0.037 | +647.52€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 4552 | -0.049 | +1064.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4552 | -0.049 | +1064.15€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 21685 | +0.079 | +10792.63€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 21685 | +0.079 | +10792.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4003 | +0.013 | +1972.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4003 | +0.013 | +1972.96€ | 2 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4575 | +0.007 | +878.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4575 | +0.007 | +878.92€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3071 | +0.257 | +3030.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3071 | +0.257 | +3030.03€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3431 | -0.012 | +463.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3431 | -0.012 | +463.12€ | 2 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3579 | +0.014 | +1265.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3579 | +0.014 | +1265.92€ | 3 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3026 | +0.272 | +3181.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3026 | +0.272 | +3181.68€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 16720 | +0.168 | +12234.97€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 16720 | +0.168 | +12234.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2479 | +0.205 | +1946.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2479 | +0.205 | +1946.97€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2652 | +0.153 | +1904.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2652 | +0.153 | +1904.39€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2589 | +0.204 | +2021.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2589 | +0.204 | +2021.00€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2771 | +0.141 | +1899.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2771 | +0.141 | +1899.48€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3154 | +0.111 | +2044.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3154 | +0.111 | +2044.58€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3075 | +0.202 | +2418.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3075 | +0.202 | +2418.56€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4263 | +0.127 | +1756.15€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4263 | +0.127 | +1756.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 165 | +0.111 | +63.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 165 | +0.111 | +63.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1164 | +0.122 | +491.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1164 | +0.122 | +491.08€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1161 | +0.151 | +541.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1161 | +0.151 | +541.00€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 902 | +0.088 | +259.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 902 | +0.088 | +259.06€ | 1 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 20652 | +0.173 | +14964.35€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 20652 | +0.173 | +14964.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3229 | +0.218 | +2689.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3229 | +0.218 | +2689.14€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3239 | +0.151 | +2133.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3239 | +0.151 | +2133.11€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3350 | +0.222 | +2836.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3350 | +0.222 | +2836.02€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3309 | +0.139 | +2173.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3309 | +0.139 | +2173.87€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3625 | +0.105 | +2094.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3625 | +0.105 | +2094.21€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3900 | +0.203 | +3038.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3900 | +0.203 | +3038.00€ | 0 | 22 |
| ✅ GBM_LATE_5M | 5987 | +0.140 | +3233.91€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5987 | +0.140 | +3233.91€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1587 | +0.139 | +965.68€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1587 | +0.139 | +965.68€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1823 | +0.145 | +982.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1823 | +0.145 | +982.89€ | 0 | 30 |
| ✅ GBM_LATE_5M#SOL | 321 | +0.029 | +39.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 321 | +0.029 | +39.66€ | 2 | 4 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1315 | +0.067 | +594.83€ | 2 | 14 |
| ✅ GBM_LATE_60M#60min | 1315 | +0.067 | +594.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 468 | +0.087 | +200.89€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 468 | +0.087 | +200.89€ | 1 | 15 |
| ✅ GBM_LATE_60M#ETH | 438 | +0.073 | +230.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 438 | +0.073 | +230.02€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 409 | +0.038 | +163.92€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 409 | +0.038 | +163.92€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 310 | -0.266 | -23.39€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 310 | -0.266 | -23.39€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 115 | -0.227 | -8.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 115 | -0.227 | -8.70€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 105 | -0.285 | -10.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 105 | -0.285 | -10.96€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 90 | -0.283 | -3.74€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 90 | -0.283 | -3.74€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 614 | +0.055 | +118.63€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 614 | +0.055 | +118.63€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 243 | +0.047 | +38.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 243 | +0.047 | +38.41€ | 3 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 181 | +0.035 | +3.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 181 | +0.035 | +3.29€ | 3 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 190 | +0.083 | +76.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 190 | +0.083 | +76.93€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1465 | +0.107 | +434.31€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1465 | +0.107 | +434.31€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1465 | +0.107 | +434.31€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1465 | +0.107 | +434.31€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M | 356 | -0.084 | -34.42€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 356 | -0.084 | -34.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 88 | -0.078 | -6.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 88 | -0.078 | -6.79€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 120 | -0.016 | -3.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 120 | -0.016 | -3.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1568 | -0.002 | -2.88€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1568 | -0.002 | -2.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 170 | -0.012 | +5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 170 | -0.012 | +5.32€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 655 | +0.024 | +17.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 655 | +0.024 | +17.26€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 460 | -0.006 | -8.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 460 | -0.006 | -8.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 106 | -0.056 | -6.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 106 | -0.056 | -6.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 919 | -0.048 | -28.81€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 919 | -0.048 | -28.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 268 | -0.052 | -14.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 268 | -0.052 | -14.50€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 294 | -0.037 | -4.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 294 | -0.037 | -4.88€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 357 | -0.054 | -9.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 357 | -0.054 | -9.43€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 13518 | -0.011 | -177.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 13518 | -0.011 | -177.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2526 | -0.021 | -47.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2526 | -0.021 | -47.09€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2838 | -0.014 | -19.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2838 | -0.014 | -19.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3334 | -0.016 | -60.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3334 | -0.016 | -60.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 22991 | -0.011 | +1003.30€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 22991 | -0.011 | +1003.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4006 | +0.011 | +511.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4006 | +0.011 | +511.83€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3691 | -0.025 | -22.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3691 | -0.025 | -22.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4026 | +0.005 | +305.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4026 | +0.005 | +305.62€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3465 | -0.047 | -91.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3465 | -0.047 | -91.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3850 | -0.014 | +158.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3850 | -0.014 | +158.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3953 | -0.000 | +141.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3953 | -0.000 | +141.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5098 | -0.044 | -127.75€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5098 | -0.044 | -127.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1127 | -0.054 | -24.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1127 | -0.054 | -24.66€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 483 | -0.127 | -25.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 483 | -0.127 | -25.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1398 | -0.060 | -30.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1398 | -0.060 | -30.46€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3339 | +0.004 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3339 | +0.004 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 186 | +0.011 | -0.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 186 | +0.011 | -0.87€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1314 | +0.007 | +7.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1314 | +0.007 | +7.09€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 59279 | -0.074 | +1160.93€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 59279 | -0.074 | +1160.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 9979 | -0.081 | +580.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 9979 | -0.081 | +580.46€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 9243 | -0.090 | -381.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 9243 | -0.090 | -381.69€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 10015 | -0.071 | +502.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 10015 | -0.071 | +502.72€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8769 | -0.093 | -254.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8769 | -0.093 | -254.64€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 10955 | -0.048 | +342.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 10955 | -0.048 | +342.07€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 10318 | -0.064 | +372.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 10318 | -0.064 | +372.02€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6760 | -0.021 | -94.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6760 | -0.021 | -94.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1520 | -0.018 | -0.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1520 | -0.018 | -0.65€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1502 | -0.015 | -2.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1502 | -0.015 | -2.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1003 | -0.038 | -16.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1003 | -0.038 | -16.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1007 | +0.113 | +351.24€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 871 | +0.121 | +338.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 202 | +0.132 | +96.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 202 | +0.132 | +96.01€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 171 | +0.095 | +40.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 171 | +0.095 | +40.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 179 | +0.102 | +61.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 179 | +0.102 | +61.63€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 155 | +0.150 | +81.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 155 | +0.150 | +81.31€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 164 | +0.120 | +59.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 164 | +0.120 | +59.09€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 479 | -0.076 | -5.11€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 211 | -0.120 | -32.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 169 | -0.155 | -35.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 171 | -0.067 | +8.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 129 | -0.072 | +1.92€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 97 | +0.005 | +18.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 77 | -0.006 | +12.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 375 | -0.097 | -20.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 561 | -0.221 | -48.01€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 233 | -0.202 | -34.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 201 | -0.195 | -32.31€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 198 | -0.240 | -23.51€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 171 | -0.251 | -27.60€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 130 | -0.220 | +10.10€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 116 | -0.220 | +7.04€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 488 | -0.222 | -52.87€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 205 | +0.399 | +153.07€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 49 | +0.363 | +40.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 49 | +0.363 | +40.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 128 | +0.485 | +116.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 128 | +0.485 | +116.86€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#sniper | 205 | +0.399 | +153.07€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 407 | +0.031 | +12.07€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 407 | +0.031 | +12.07€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 181 | +0.030 | +2.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 181 | +0.030 | +2.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 47 | -0.031 | -4.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 47 | -0.031 | -4.66€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 153 | +0.035 | +9.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 153 | +0.035 | +9.68€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 2495 | -0.028 | -117.77€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2495 | -0.028 | -117.77€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 563 | -0.024 | -23.90€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 563 | -0.024 | -23.90€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 153 | -0.042 | -13.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 153 | -0.042 | -13.91€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 975 | -0.035 | -53.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 975 | -0.035 | -53.02€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 61 | -0.040 | -3.88€ | 2 | 1 |
| ✅ STREAK_FADE_60M#60min | 61 | -0.040 | -3.88€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 24 | +0.038 | +0.06€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 24 | +0.038 | +0.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6706 | +0.024 | +103.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6706 | +0.024 | +103.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2117 | +0.021 | +19.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2117 | +0.021 | +19.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1406 | +0.030 | +36.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1406 | +0.030 | +36.72€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1965 | +0.015 | +8.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1965 | +0.015 | +8.05€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1218 | +0.034 | +38.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1218 | +0.034 | +38.65€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6180 | +0.014 | -24.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6180 | +0.014 | -24.85€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2450 | +0.020 | +3.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2450 | +0.020 | +3.69€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2445 | +0.016 | -5.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2445 | +0.016 | -5.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1285 | -0.003 | -23.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1285 | -0.003 | -23.09€ | 2 | 0 |
| ✅ UPDOWN_GBM | 27047 | +0.030 | +1539.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 7288 | +0.060 | +1189.48€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1014 | +0.005 | +8.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 16988 | +0.023 | +337.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1647 | +0.002 | +2.94€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2394 | +0.071 | +239.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 315 | +0.131 | +105.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2060 | +0.063 | +134.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4914 | +0.033 | +326.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 888 | +0.083 | +201.98€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 287 | +0.022 | +7.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2968 | +0.029 | +108.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 729 | -0.001 | +7.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 42 | -0.114 | +0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3188 | +0.033 | +123.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 270 | +0.129 | +85.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2902 | +0.024 | +37.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 5626 | +0.017 | +224.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1986 | +0.048 | +221.16€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 274 | +0.007 | +7.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2746 | +0.002 | -3.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 584 | -0.002 | -4.75€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 36 | -0.158 | +3.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6877 | +0.017 | +166.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1935 | +0.024 | +110.52€ | 1 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 268 | -0.007 | -2.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4310 | +0.017 | +58.97€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 334 | +0.012 | +0.36€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 30 | -0.156 | -1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4046 | +0.042 | +462.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1894 | +0.078 | +464.26€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 150 | -0.007 | -2.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2002 | +0.011 | +1.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 108 | -0.145 | +3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 432 | +0.334 | +121.59€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 432 | +0.334 | +121.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 240 | +0.335 | +62.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 240 | +0.335 | +62.92€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 192 | +0.330 | +58.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 192 | +0.330 | +58.66€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 9456 | -0.046 | +2023.47€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 9456 | -0.046 | +2023.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 462 | -0.050 | +342.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 462 | -0.050 | +342.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1796 | -0.127 | +37.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1796 | -0.127 | +37.48€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 166 | +0.131 | +75.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 166 | +0.131 | +75.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1041 | +0.199 | +603.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1041 | +0.199 | +603.29€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3003 | -0.062 | +464.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3003 | -0.062 | +464.25€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2988 | -0.075 | +500.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2988 | -0.075 | +500.23€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 108 | +0.073 | +17.16€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 108 | +0.073 | +17.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 108 | +0.073 | +17.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 108 | +0.073 | +17.16€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 727 | +0.286 | +581.94€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 727 | +0.286 | +581.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 404 | +0.276 | +304.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 404 | +0.276 | +304.23€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 323 | +0.297 | +277.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 323 | +0.297 | +277.71€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 687 | -0.110 | -80.82€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 687 | -0.110 | -80.82€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 185 | -0.072 | -12.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 185 | -0.072 | -12.62€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 66 | -0.176 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 66 | -0.176 | -10.12€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1998 | +0.305 | +1042.24€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 668 | +0.251 | +109.91€ | 1 | 4 |
| ✅ WEEKLY_PRICE#ETH | 723 | +0.294 | +310.36€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 607 | +0.375 | +621.96€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.054) — sin ventaja clara. oversold(IBS<0.3): IC=+0.048 n=9511 | neutral: IC=+0.030 n=10242 | overbought(IBS>0.7): IC=+0.084 n=9712
  - _Datos_: n=30550 IC=+0.054 PNL=+3603.82€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 470 celda(s) pasan gate riguroso completo de 2068 evaluadas (n>=40) y 3040 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.023 < 0.08 — monitorear
  - _Datos_: n=1930 IC=+0.023 PNL=+111.52€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=723/15 IC=+0.294 PNL=+310.36€ | BTC: n=668/15 IC=+0.251 PNL=+109.91€ | SOL: n=607/15 IC=+0.375 PNL=+621.96€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 29 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 26932 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.102 n=199/60 | contraria IC=+0.148 n=180 | gap=-0.046 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=250, boost estimado=+0.005. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 155 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=583/40 IC=-0.001 PNL=-4.24€ | BTC#60min: n=727/40 IC=-0.001 PNL=+6.02€ | SOL#60min: n=333/40 IC=+0.010 PNL=-0.13€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.053 n=271901 | tras_1loss IC=+0.073 n=212265 | tras_2loss IC=+0.041 n=90676/40 | gap=+0.012 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.013 n=2918 | contrario_BTC IC=+0.018 n=2581/40 | gap=+0.005 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=221 PNL=+148.90€
  - _Datos_: n=221 IC=+0.191 PNL=+148.90€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.08 con n=278 PNL=+177.40€
  - _Datos_: n=278 IC=+0.196 PNL=+177.40€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.235 > 0.08 con n=32 PNL=+22.88€
  - _Datos_: n=32 IC=+0.235 PNL=+22.88€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.344 > 0.1 con n=1667 PNL=+1030.23€
  - _Datos_: n=1667 IC=+0.344 PNL=+1030.23€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=203 IC=+0.076 PNL=+26.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=203 IC=+0.076 PNL=+26.59€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=45 IC=+0.202 PNL=+32.49€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=45 IC=+0.202 PNL=+32.49€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=25820 IC=+0.029 PNL=+1426.64€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=25820 IC=+0.029 PNL=+1426.64€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

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
  - _Estado_: n=1198 IC=+0.004 PNL=-5.17€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1198 IC=+0.004 PNL=-5.17€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=445 IC=-0.006 PNL=+6.82€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=445 IC=-0.006 PNL=+6.82€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=372 IC=+0.016 PNL=+18.02€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=372 IC=+0.016 PNL=+18.02€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.1 con n=1530 PNL=+888.15€
  - _Datos_: n=1530 IC=+0.177 PNL=+888.15€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=857 IC=+0.050 PNL=+69.29€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=857 IC=+0.050 PNL=+69.29€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=885 IC=+0.083 PNL=+200.05€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=885 IC=+0.083 PNL=+200.05€

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
  - _Estado_: n=4163 IC=+0.065 PNL=+802.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4163 IC=+0.065 PNL=+802.60€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=114 IC=-0.215 PNL=-0.14€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=114 IC=-0.215 PNL=-0.14€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=201 IC=-0.012 PNL=+13.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=201 IC=-0.012 PNL=+13.87€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=410 IC=+0.019 PNL=+34.16€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=410 IC=+0.019 PNL=+34.16€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=32 IC=+0.000 PNL=-0.67€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=32 IC=+0.000 PNL=-0.67€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=3352 IC=-0.002 PNL=-1.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3352 IC=-0.002 PNL=-1.82€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=66 PNL=+18.24€
  - _Datos_: n=66 IC=+0.176 PNL=+18.24€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.264 n=70) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=70 IC=+0.264 PNL=+51.39€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=5197 IC=+0.030 PNL=+274.74€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=5197 IC=+0.030 PNL=+274.74€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=1715 IC=+0.049 PNL=+189.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1715 IC=+0.049 PNL=+189.40€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.08 con n=300 PNL=+95.92€
  - _Datos_: n=300 IC=+0.116 PNL=+95.92€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.142 > 0.08 con n=440 PNL=+103.73€
  - _Datos_: n=440 IC=+0.142 PNL=+103.73€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.08 con n=345 PNL=+160.30€
  - _Datos_: n=345 IC=+0.117 PNL=+160.30€

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
  - _Estado_: n=3829 IC=+0.037 PNL=+265.68€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3829 IC=+0.037 PNL=+265.68€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.02 con n=575 PNL=+238.12€
  - _Datos_: n=575 IC=+0.131 PNL=+238.12€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=140 IC=-0.056 PNL=+31.39€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=140 IC=-0.056 PNL=+31.39€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.454 > 0.1 con n=994 PNL=+1013.79€
  - _Datos_: n=994 IC=+0.454 PNL=+1013.79€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=8918 IC=+0.050 PNL=+1022.09€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=8918 IC=+0.050 PNL=+1022.09€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.1 con n=2420 PNL=+1263.08€
  - _Datos_: n=2420 IC=+0.196 PNL=+1263.08€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.157 < -0.1 con n=167 PNL=+14.68€
  - _Datos_: n=167 IC=-0.157 PNL=+14.68€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1460 IC=+0.046 PNL=+162.33€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1460 IC=+0.046 PNL=+162.33€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=59 IC=-0.107 PNL=+6.34€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=59 IC=-0.107 PNL=+6.34€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.143 > 0.1 con n=281 PNL=+90.63€
  - _Datos_: n=281 IC=+0.143 PNL=+90.63€

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
  - _Estado_: n=14159 IC=-0.144 PNL=+615.63€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=14159 IC=-0.144 PNL=+615.63€

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
  - _Estado_: n=1572 IC=+0.139 PNL=+843.63€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1572 IC=+0.139 PNL=+843.63€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=1491 PNL=+875.52€
  - _Datos_: n=1491 IC=+0.180 PNL=+875.52€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2800 IC=+0.016 PNL=+72.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2800 IC=+0.016 PNL=+72.88€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=1650 PNL=+847.26€
  - _Datos_: n=1650 IC=+0.083 PNL=+847.26€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=377 PNL=+175.78€
  - _Datos_: n=377 IC=+0.191 PNL=+175.78€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.244 < -0.1 con n=1427 PNL=-207.50€
  - _Datos_: n=1427 IC=-0.244 PNL=-207.50€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=4109 IC=+0.147 PNL=+2475.43€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=4109 IC=+0.147 PNL=+2475.43€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.134 > 0.08 con n=69 PNL=+33.24€
  - _Datos_: n=69 IC=+0.134 PNL=+33.24€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1616 IC=+0.048 PNL=+354.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1616 IC=+0.048 PNL=+354.12€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.178 > 0.08 con n=1467 PNL=+978.36€
  - _Datos_: n=1467 IC=+0.178 PNL=+978.36€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=2404 IC=-0.038 PNL=+562.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2404 IC=-0.038 PNL=+562.49€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.092 > 0.08 con n=479 PNL=-45.83€
  - _Datos_: n=479 IC=+0.092 PNL=-45.83€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.230 > 0.08 con n=2821 PNL=-274.53€
  - _Datos_: n=2821 IC=+0.230 PNL=-274.53€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 29/40 ops en el filtro definido (IC actual=-0.016 PNL=+5.59€)
  - _Datos_: n=29 IC=-0.016 PNL=+5.59€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=769) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=769 IC=+0.099 PNL=+203.01€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.346 > 0.08 con n=200 PNL=+82.37€
  - _Datos_: n=200 IC=+0.346 PNL=+82.37€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=397) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=397 IC=+0.412 PNL=+556.95€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=7286 IC=+0.171 PNL=-912.93€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=7286 IC=+0.171 PNL=-912.93€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.1 con n=108 PNL=+72.77€
  - _Datos_: n=108 IC=+0.227 PNL=+72.77€
