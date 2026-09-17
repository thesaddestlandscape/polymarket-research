# Hipótesis automáticas — 2026-09-17 16:10 UTC
_Generado por shadow_postmortem.py sobre 483788 resoluciones (PNL=+52243.79€)_

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
- **FILTRO** `restante_s_al_confirmar` < `144.08` → IC=-0.249 (n=5957)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.08
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=17873)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `141.04` → IC=-0.267 (n=821)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.04
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2466)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `491.58` → IC=-0.159 (n=318)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 491.58
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=954)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `132.07` → IC=-0.291 (n=721)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.07
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=2165)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.47` → IC=-0.243 (n=1416)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.47
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4250)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `117.26` → IC=-0.367 (n=1154)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.26
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=3466)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.249 (n=281)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=307)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.164 (n=135)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=425)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.144 (n=130)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=430)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.252 (n=147)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=162)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.181 (n=67)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=214)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.264 (n=87)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=47)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.154 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=105)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=122)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.197 (n=12034)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.69 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3000)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `11417.6661` → IC=+0.192 (n=957)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11417.6661 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=9296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=11229)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.246 (n=8246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=5907)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7279.5535` → IC=+0.179 (n=1866)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7279.5535 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1408)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.350 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1757)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15201.8178` → IC=+0.222 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15201.8178 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=1292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.210 (n=1424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.274 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1823)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `14982.525` → IC=+0.227 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14982.525 (IC base=+0.203)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.178 (n=281)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.62 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=286)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `4641.025` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4641.025 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.177 (n=298)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.435` → IC=+0.153 (n=678)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.435 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=549)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3855.8996` → IC=+0.149 (n=425)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3855.8996 (IC base=+0.127)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=2060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.328 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=1088)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.302 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.248 (n=1261)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `3159.9604` → IC=+0.245 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3159.9604 (IC base=+0.241)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.136 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.228 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=470)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `1913.3154` → IC=+0.159 (n=373)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1913.3154 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.425 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.269 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.178 (n=1138)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.03 (IC base=+0.174)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.120)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.222 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=335)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.120)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=9492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.198 (n=9117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.222 (n=3337)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.177 (n=2345)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.312 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.270 (n=172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.270)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.353 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.270)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=2320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=1979)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=2072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.322 (n=695)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=1938)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.195 (n=1620)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.440 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `2060.1801` → IC=+0.442 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.1801 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.440 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.456 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `12563.6486` → IC=+0.446 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.6486 (IC base=+0.436)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=28130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.237 (n=10653)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5745)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4875)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=5204)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=5016)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=5020)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=1790)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=2696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=5188)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.170)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=1913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=4650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.255 (n=2365)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.193 (n=4708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4700)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.248 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.205 (n=4296)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.08` → IC=+0.134 (n=3932)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.08 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.153 (n=3962)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` > 4.95 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=5176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.153 (n=3928)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 3.28 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=2161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.129)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.135 (n=1944)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.01 (IC base=+0.129)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.147 (n=2112)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.93 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.144 (n=2885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 8.0 (IC base=+0.129)

- **PATRÓN** `lag_apertura_s` < `3.92` → IC=+0.150 (n=1947)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.92 (IC base=+0.129)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.203 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.126 (n=2611)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.149 (n=2039)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.96 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=2620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.47` → IC=+0.150 (n=1980)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 2.47 (IC base=+0.120)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.383 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1604.9934` → IC=+0.297 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.9934 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.299 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.271)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.336 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.271)

- **PATRÓN** `libro_liquidez` > `4254.7258` → IC=+0.286 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4254.7258 (IC base=+0.271)

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
- **PATRÓN** `ibs_20min` > `0.4989` → IC=+0.155 (n=5756)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.4989 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1442` → IC=+0.245 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1442 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.854` → IC=+0.169 (n=2494)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.854 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.2217` → IC=+0.243 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2217 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `1.0676` → IC=+0.241 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0676 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.175` → IC=+0.191 (n=4433)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.175 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.3071` → IC=+0.203 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3071 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `1.9183` → IC=+0.198 (n=2849)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.9183 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.57` → IC=+0.132 (n=7894)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.57 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.5595` → IC=+0.185 (n=475)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5595 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` < `0.3375` → IC=+0.171 (n=2767)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.3375 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` < `0.7025` → IC=+0.174 (n=1146)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7025 (IC base=+0.061)

- **PATRÓN** `volumen_regimen` > `0.8728` → IC=+0.178 (n=1735)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8728 (IC base=+0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.2439` → IC=+0.226 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2439 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` > `1.5874` → IC=+0.201 (n=3866)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5874 (IC base=+0.061)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.211 (n=4102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.061)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.184 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0049 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.176 (n=486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0079 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.3264` → IC=+0.165 (n=1453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3264 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.185 (n=547)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.034` → IC=+0.276 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.034 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.205 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.4306` → IC=+0.162 (n=1340)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4306 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.182 (n=1367)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.252 (n=964)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0883` → IC=+0.296 (n=361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0883 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.252 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.288 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.362` → IC=+0.248 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.362 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.092` → IC=+0.232 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.092 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.268 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6474` → IC=+0.262 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6474 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1745.82` → IC=+0.257 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1745.82 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.223 (n=969)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1157` → IC=+0.239 (n=485)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1157 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=1155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9149` → IC=+0.255 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9149 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1883` → IC=+0.213 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1883 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.212 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1292 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.828` → IC=+0.231 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.828 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.258` → IC=+0.220 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.258 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.0993` → IC=+0.214 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0993 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4011` → IC=+0.219 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4011 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.3632` → IC=+0.219 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3632 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `11003.4334` → IC=+0.221 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11003.4334 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.165 (n=789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0039 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.162 (n=394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6747` → IC=+0.175 (n=1178)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6747 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.126` → IC=+0.151 (n=1076)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.126 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.6` → IC=+0.162 (n=383)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.6 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2134` → IC=+0.146 (n=1178)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2134 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.853` → IC=+0.142 (n=785)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.853 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.183 (n=317)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.152 (n=1069)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4274` → IC=+0.143 (n=1068)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4274 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `13565.0888` → IC=+0.152 (n=785)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 13565.0888 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.162 (n=332)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 215.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.189 (n=1424)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0058 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=1498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.180 (n=951)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 11.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.253 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.471` → IC=+0.231 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.471 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.183 (n=1209)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.3756` → IC=+0.184 (n=185)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.3756 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `3.0006` → IC=+0.199 (n=605)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 3.0006 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.189 (n=1639)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.226 (n=1220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.217 (n=1091)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3808` → IC=+0.233 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3808 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.693` → IC=+0.233 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.693 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.323` → IC=+0.218 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.323 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.365` → IC=+0.271 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.365 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.8483` → IC=+0.208 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8483 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3057` → IC=+0.223 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3057 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.230 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1894.0152` → IC=+0.236 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.0152 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.224 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=1800)

- **PATRÓN** `ibs_20min` > `0.9343` → IC=+0.178 (n=296)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.9343 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.3284` → IC=+0.344 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3284 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.4828` → IC=+0.326 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4828 (IC base=+0.007)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.136 (n=561)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.5962` → IC=+0.364 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5962 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.1953` → IC=+0.352 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1953 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.4943` → IC=+0.333 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4943 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.8068` → IC=+0.344 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8068 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.350 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.1672` → IC=+0.192 (n=212)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1672 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.697` → IC=+0.159 (n=265)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.697 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2153` → IC=+0.226 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2153 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.5104` → IC=+0.190 (n=492)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.5104 (IC base=+0.007)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=254)

- **FILTRO** `ibs_20min` < `0.375` → IC=-0.170 (n=98)

  - _Acción_: SKIP cuando `ibs_20min` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=206)

- **FILTRO** `ibs_20min` > `0.2692` → IC=-0.128 (n=1809)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=893)

- **FILTRO** `sigma_ewma_delta_pct` > `8.637` → IC=-0.209 (n=297)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.637
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2405)

- **PATRÓN** `ibs_20min` > `0.7586` → IC=+0.207 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7586 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.6239` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6239 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.6528` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6528 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.7776` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7776 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.9536` → IC=+0.293 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9536 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.5081` → IC=+0.269 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5081 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.043)

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
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.196 (n=452)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=1358)

- **FILTRO** `ibs_20min` < `0.6685` → IC=-0.162 (n=1194)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6685
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=616)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.202 (n=380)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1430)

- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.199 (n=682)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2049)

- **PATRÓN** `dist_vwap_pct` > `0.9664` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9664 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.310 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.083)

- **PATRÓN** `volumen_regimen` < `1.0034` → IC=+0.274 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0034 (IC base=-0.083)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.288 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=-0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.1679` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1679 (IC base=-0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.275 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=-0.083)

- **PATRÓN** `volumen_spike_ratio` > `1.8324` → IC=+0.288 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8324 (IC base=-0.083)

- **PATRÓN** `dist_vwap_pct` > `1.0042` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0042 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2603` → IC=+0.248 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2603 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.7351` → IC=+0.247 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7351 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.0829` → IC=+0.297 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0829 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1054` → IC=+0.275 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1054 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.2213` → IC=+0.260 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2213 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.5853` → IC=+0.246 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5853 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.180 (n=2690)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0093 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.457` → IC=+0.178 (n=7194)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.457 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `1.0016` → IC=+0.281 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0016 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.512` → IC=+0.146 (n=3810)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.512 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.678` → IC=+0.238 (n=2455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.678 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.2466` → IC=+0.260 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2466 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.4768` → IC=+0.245 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4768 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` > `2.7557` → IC=+0.238 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7557 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.278 (n=3881)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.143 (n=2725)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0086 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.5547` → IC=+0.152 (n=7190)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5547 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.6733` → IC=+0.248 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6733 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.1628` → IC=+0.234 (n=2114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1628 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.234 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.2001` → IC=+0.251 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2001 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2511` → IC=+0.316 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2511 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4946` → IC=+0.255 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4946 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.3723` → IC=+0.255 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3723 (IC base=+0.070)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.259 (n=2818)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.070)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2379` → IC=-0.144 (n=551)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2379
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1654)

- **FILTRO** `sigma_ewma_delta_pct` > `4.36` → IC=-0.168 (n=411)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.36
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1374)

- **PATRÓN** `ibs_20min` > `0.8687` → IC=+0.256 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8687 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.684` → IC=+0.188 (n=299)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 8.684 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2236` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2236 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.197 (n=193)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8224` → IC=-0.144 (n=600)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8224
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1804)

- **PATRÓN** `dist_vwap_pct` > `0.2885` → IC=+0.139 (n=261)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.2885 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1582` → IC=+0.136 (n=610)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1582 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6556` → IC=+0.142 (n=635)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6556 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2209` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2209 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.178 (n=231)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `229.0` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 229.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1009` → IC=+0.213 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1009 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `1.047` → IC=+0.219 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.047 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.8169` → IC=+0.208 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8169 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1868` → IC=+0.226 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1868 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.214 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.281 (n=856)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.244 (n=428)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.253 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.52` → IC=+0.275 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.52 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.1403` → IC=+0.252 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1403 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.8778` → IC=+0.240 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8778 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `3.6286` → IC=+0.255 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6286 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.298 (n=1020)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.316 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.286 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.808` → IC=+0.297 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.808 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.585` → IC=+0.280 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.585 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.3468` → IC=+0.305 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3468 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `1.6355` → IC=+0.284 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6355 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.2257` → IC=+0.280 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2257 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `1882.4784` → IC=+0.304 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.4784 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.277 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.280)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2479` → IC=-0.210 (n=371)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2479
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=1119)

- **FILTRO** `ibs_20min` > `0.8032` → IC=-0.185 (n=481)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8032
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=1450)

- **PATRÓN** `ibs_20min` > `0.806` → IC=+0.150 (n=507)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.806 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` > `0.4461` → IC=+0.213 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4461 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` < `0.1908` → IC=+0.192 (n=274)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.1908 (IC base=-0.010)

- **PATRÓN** `volumen_regimen` < `0.9674` → IC=+0.213 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9674 (IC base=-0.010)

- **PATRÓN** `volumen_regimen` > `0.6214` → IC=+0.196 (n=317)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.6214 (IC base=-0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2647` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2647 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` < `2.0696` → IC=+0.240 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0696 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` > `1.3739` → IC=+0.219 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3739 (IC base=-0.010)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.242 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=-0.010)

- **PATRÓN** `dist_vwap_pct` > `0.1237` → IC=+0.209 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1237 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` < `1.1418` → IC=+0.182 (n=262)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1418 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` > `0.7266` → IC=+0.186 (n=234)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.7266 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.1505` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1505 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.7947` → IC=+0.252 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7947 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.014)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.252 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 145.0 (IC base=-0.014)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6757` → IC=-0.211 (n=868)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6757
  - _Potencial_: sin este filtro IC_bueno=+0.263 (n=871)

- **FILTRO** `ibs_20min` > `0.7105` → IC=-0.234 (n=456)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7105
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1375)

- **FILTRO** `sigma_ewma_delta_pct` > `4.627` → IC=-0.175 (n=426)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.627
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=1405)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.263 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6757 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1802` → IC=+0.315 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1802 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.484` → IC=+0.142 (n=269)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.484 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `0.8657` → IC=+0.294 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8657 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.7203` → IC=+0.278 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7203 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1055` → IC=+0.279 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1055 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4442` → IC=+0.318 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4442 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.323 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.1053` → IC=+0.200 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1053 (IC base=+0.004)

- **PATRÓN** `dist_vwap_pct` > `0.5846` → IC=+0.190 (n=85)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.5846 (IC base=+0.004)

- **PATRÓN** `dist_vwap_pct` < `0.3939` → IC=+0.196 (n=403)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.3939 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.7148` → IC=+0.244 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7148 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.191 (n=351)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.193 (n=151)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.5876` → IC=+0.208 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5876 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4993` → IC=+0.183 (n=361)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4993 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.222 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.324 (n=718)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.291 (n=506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.347 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `0.2596` → IC=+0.318 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2596 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.301 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `0.6862` → IC=+0.290 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6862 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.303 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `1.5484` → IC=+0.281 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5484 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `2.2067` → IC=+0.281 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2067 (IC base=+0.273)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.277 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `2431.0035` → IC=+0.282 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2431.0035 (IC base=+0.273)

- **PATRÓN** `sigma_h` > `0.0145` → IC=+0.297 (n=792)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0145 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.286 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.395` → IC=+0.306 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.395 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.5366` → IC=+0.288 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5366 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.441` → IC=+0.289 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.441 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.304 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.363 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.5387` → IC=+0.264 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5387 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1688` → IC=+0.273 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1688 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2352.323` → IC=+0.276 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2352.323 (IC base=+0.270)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.177 (n=2120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0048 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.198 (n=2116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0106 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.3377` → IC=+0.174 (n=5586)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3377 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=6621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.5814` → IC=+0.213 (n=6348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5814 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.9321` → IC=+0.217 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9321 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.219` → IC=+0.247 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.219 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.2143` → IC=+0.162 (n=4216)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2143 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `0.623` → IC=+0.158 (n=4216)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.623 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.1064` → IC=+0.184 (n=2489)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1064 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.5656` → IC=+0.173 (n=2658)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5656 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.6612` → IC=+0.169 (n=2013)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.6612 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3831.2799` → IC=+0.168 (n=2116)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3831.2799 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.180 (n=5264)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 121.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.187 (n=4112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0064 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.206 (n=2053)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=2381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4694` → IC=+0.229 (n=6159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4694 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2212` → IC=+0.161 (n=4592)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2212 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.199` → IC=+0.194 (n=1061)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.199 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1821` → IC=+0.155 (n=4501)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1821 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6252` → IC=+0.150 (n=4502)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6252 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.230 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.576` → IC=+0.173 (n=2421)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.576 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.2831` → IC=+0.175 (n=2494)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.2831 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.173 (n=5120)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 122.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.222 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.190 (n=489)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0073 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.3224` → IC=+0.202 (n=1077)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3224 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.206 (n=533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.044` → IC=+0.307 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.044 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.236 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `2.5417` → IC=+0.175 (n=982)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.5417 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `1.4251` → IC=+0.177 (n=981)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4251 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.241 (n=685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.250 (n=695)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.292 (n=518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.241 (n=781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3378` → IC=+0.259 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3378 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.021` → IC=+0.253 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.021 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.234 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.265 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4284` → IC=+0.251 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4284 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.239 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1746.26` → IC=+0.260 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1746.26 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.250 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0765` → IC=+0.187 (n=311)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0765 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.4211` → IC=+0.224 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4211 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2016` → IC=+0.206 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2016 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.216 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2593` → IC=+0.172 (n=930)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2593 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2316` → IC=+0.189 (n=204)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2316 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.194 (n=299)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `10103.8179` → IC=+0.176 (n=930)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 10103.8179 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.166 (n=1054)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.201 (n=352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.162 (n=975)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.5407` → IC=+0.190 (n=1054)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5407 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.165 (n=1075)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.985` → IC=+0.212 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.985 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.161 (n=1054)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2129 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.178 (n=324)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.156 (n=943)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.164 (n=287)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 223.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.197 (n=1057)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0059 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.198` → IC=+0.204 (n=705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.198 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.673` → IC=+0.271 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.673 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.2152` → IC=+0.185 (n=1014)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2152 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.1347` → IC=+0.184 (n=409)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1347 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.6649` → IC=+0.191 (n=331)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.6649 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `3.6123` → IC=+0.205 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6123 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.240 (n=882)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.225 (n=882)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0894` → IC=+0.247 (n=294)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0894 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.270 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.3478` → IC=+0.253 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3478 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.671` → IC=+0.274 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.671 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3607` → IC=+0.271 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3607 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.854` → IC=+0.219 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.854 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `3.5248` → IC=+0.248 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5248 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1893.9584` → IC=+0.240 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1893.9584 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.216 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.224)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.180 (n=882)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0066 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4235` → IC=+0.164 (n=1001)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.4235 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3938` → IC=+0.202 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3938 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1357` → IC=+0.185 (n=655)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1357 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.01` → IC=+0.246 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.01 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.160 (n=669)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8585 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `1.1924` → IC=+0.167 (n=334)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.1924 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.220 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.165 (n=326)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5111` → IC=+0.180 (n=326)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5111 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `7103.48` → IC=+0.185 (n=667)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7103.48 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.153 (n=825)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 149.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.167 (n=1074)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0071 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.147 (n=1074)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6046` → IC=+0.184 (n=1074)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6046 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1486` → IC=+0.148 (n=1076)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1486 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.871` → IC=+0.189 (n=207)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.871 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8548` → IC=+0.145 (n=716)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8548 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `0.609` → IC=+0.133 (n=1074)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.609 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.141 (n=639)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.7994 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.4806` → IC=+0.142 (n=319)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4806 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `10127.4072` → IC=+0.163 (n=487)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10127.4072 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.130 (n=887)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 175.0 (IC base=+0.132)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.155 (n=532)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0098 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.196 (n=1185)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0154` → IC=+0.224 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0154 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.474` → IC=+0.258 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.474 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.122 (n=1175)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2233 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.8146` → IC=+0.127 (n=752)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8146 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=1213)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2898.8632` → IC=+0.189 (n=532)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2898.8632 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.132 (n=869)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.147 (n=522)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.006 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1005` → IC=+0.146 (n=396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1005 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.204 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5556 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.9375` → IC=+0.131 (n=139)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.9375 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.1823` → IC=+0.134 (n=1088)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1823 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.391` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.391 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.0388` → IC=+0.121 (n=1044)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0388 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.185 (n=141)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4638` → IC=+0.140 (n=348)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4638 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.179` → IC=+0.129 (n=472)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.179 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `3086.3351` → IC=+0.163 (n=396)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3086.3351 (IC base=+0.111)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0182` → IC=+0.211 (n=742)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0182 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1678` → IC=+0.215 (n=490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1678 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.7255` → IC=+0.253 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7255 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `1.2278` → IC=+0.228 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2278 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.371` → IC=+0.239 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.371 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.207 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.209 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6141 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2413` → IC=+0.265 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2413 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1918` → IC=+0.214 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1918 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4272` → IC=+0.206 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4272 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.202 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.234 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.213 (n=539)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.217 (n=397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.212 (n=546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.244 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1437` → IC=+0.227 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1437 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.265` → IC=+0.204 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.265 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.319` → IC=+0.234 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.319 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6282` → IC=+0.217 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6282 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.279 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2444` → IC=+0.196 (n=926)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2444 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4604` → IC=+0.195 (n=1052)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4604 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2546.1622` → IC=+0.214 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2546.1622 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.156 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.163 (n=515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0089 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3432` → IC=+0.141 (n=1359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3432 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.388` → IC=+0.168 (n=1546)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.388 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.805` → IC=+0.171 (n=214)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.805 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.691` → IC=+0.170 (n=712)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.691 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8692` → IC=+0.155 (n=889)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8692 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.167 (n=424)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4335` → IC=+0.153 (n=494)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4335 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.5517` → IC=+0.163 (n=493)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5517 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=1725)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8599.8756` → IC=+0.149 (n=701)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 8599.8756 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.158 (n=1324)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 160.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.152 (n=550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0038 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.132 (n=1448)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=1662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.4872` → IC=+0.158 (n=1448)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4872 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.1448` → IC=+0.122 (n=1399)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1448 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.009` → IC=+0.134 (n=476)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 6.009 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.123 (n=1459)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2216 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.142 (n=417)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.2373` → IC=+0.136 (n=1387)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2373 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `3609.2507` → IC=+0.124 (n=1097)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3609.2507 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.126 (n=658)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 25.0 (IC base=+0.117)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.140 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.142 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 10.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.2815` → IC=+0.133 (n=360)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.2815 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.5024` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.5024 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.328` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.328 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `0.9116` → IC=+0.130 (n=241)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.9116 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `10160.5257` → IC=+0.127 (n=360)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 10160.5257 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.155 (n=111)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 151.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.211 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.156 (n=509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.3422` → IC=+0.208 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3422 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.437` → IC=+0.149 (n=203)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 4.437 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.159` → IC=+0.137 (n=579)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 9.159 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.138 (n=509)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.218 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.063` → IC=+0.178 (n=231)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.063 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.217 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.1106` → IC=+0.160 (n=439)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1106 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4209` → IC=+0.143 (n=499)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4209 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 155.0 (IC base=+0.135)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.260 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.197 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0067 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.223 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.244 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.388` → IC=+0.237 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.388 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.223 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.116` → IC=+0.235 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.116 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.201 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.193)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.131 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.8906` → IC=+0.210 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8906 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.7744` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.7744 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.234` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.234 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `2.2151` → IC=+0.128 (n=146)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.2151 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.213 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 21.0 (IC base=+0.092)

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
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.192 (n=3656)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0087 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=8413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.213 (n=8063)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8871` → IC=+0.196 (n=1039)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.8871 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.762` → IC=+0.231 (n=3017)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.762 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8829` → IC=+0.167 (n=3609)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8829 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.190 (n=1521)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.6338` → IC=+0.182 (n=2561)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6338 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3810.3548` → IC=+0.168 (n=2685)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3810.3548 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.193 (n=5884)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 92.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.195 (n=4930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0068 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.4818` → IC=+0.185 (n=7388)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4818 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5602` → IC=+0.240 (n=7388)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5602 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.231` → IC=+0.163 (n=4691)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.231 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.846` → IC=+0.196 (n=1059)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.846 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.683` → IC=+0.184 (n=7141)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.683 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.159 (n=2249)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7049 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.204` → IC=+0.159 (n=1704)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.204 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.247 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.2985` → IC=+0.191 (n=3016)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.2985 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.193 (n=2113)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 25.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.210 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.217 (n=617)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.198 (n=654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.320 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.368` → IC=+0.346 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.368 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2241` → IC=+0.239 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2241 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.5474` → IC=+0.183 (n=559)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5474 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.5623` → IC=+0.197 (n=423)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5623 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1266)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.260 (n=705)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.265 (n=1059)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.2039` → IC=+0.284 (n=706)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2039 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=958)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.3469` → IC=+0.288 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3469 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.422` → IC=+0.265 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.422 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.304 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `1.8812` → IC=+0.279 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8812 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1746.26` → IC=+0.278 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1746.26 (IC base=+0.256)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.194 (n=433)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3568` → IC=+0.151 (n=1283)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3568 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.3159` → IC=+0.198 (n=1281)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3159 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.1238` → IC=+0.186 (n=704)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1238 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.939` → IC=+0.154 (n=434)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.939 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.316` → IC=+0.153 (n=1138)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.316 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.182 (n=564)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6973 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.154` → IC=+0.176 (n=350)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.154 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.156 (n=1080)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7574` → IC=+0.157 (n=818)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7574 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `10923.8518` → IC=+0.165 (n=1145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 10923.8518 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `488.0` → IC=+0.160 (n=1160)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 488.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.170 (n=1141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0057 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2618` → IC=+0.168 (n=1004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2618 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` < `0.6376` → IC=+0.206 (n=1141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6376 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6891` → IC=+0.165 (n=171)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.6891 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.1283` → IC=+0.165 (n=1057)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1283 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.209` → IC=+0.166 (n=567)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.209 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `1.2029` → IC=+0.161 (n=1141)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2029 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.1513` → IC=+0.211 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1513 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.4156` → IC=+0.167 (n=1044)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.4156 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.7562` → IC=+0.159 (n=696)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7562 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `12529.5931` → IC=+0.155 (n=761)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12529.5931 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `368.0` → IC=+0.168 (n=634)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 368.0 (IC base=+0.154)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.226 (n=1284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=1348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.213 (n=1308)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.6709` → IC=+0.249 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6709 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.548` → IC=+0.302 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.548 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.2161` → IC=+0.215 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2161 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.9918` → IC=+0.231 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9918 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.239 (n=1222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.237 (n=815)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=580)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3642` → IC=+0.269 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3642 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.713` → IC=+0.274 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.713 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.359` → IC=+0.297 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.359 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7987` → IC=+0.228 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7987 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2483` → IC=+0.233 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2483 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.247 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1896.6084` → IC=+0.241 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1896.6084 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.261 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.180 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0034 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.436` → IC=+0.138 (n=1367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.436 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.7002` → IC=+0.230 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7002 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.5569` → IC=+0.173 (n=365)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.5569 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.195` → IC=+0.162 (n=577)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.195 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8782` → IC=+0.160 (n=912)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8782 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.227 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.409` → IC=+0.149 (n=1316)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.409 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8750.1763` → IC=+0.228 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8750.1763 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.168 (n=420)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 86.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.162 (n=1109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0076 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.445` → IC=+0.161 (n=1107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.445 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=500)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6874` → IC=+0.196 (n=1107)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6874 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.2043` → IC=+0.145 (n=1035)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2043 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.012` → IC=+0.191 (n=166)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.012 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.192` → IC=+0.144 (n=1034)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.192 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.6962` → IC=+0.150 (n=487)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6962 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.1778` → IC=+0.152 (n=369)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1778 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.472` → IC=+0.172 (n=346)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.472 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `11036.6607` → IC=+0.203 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11036.6607 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.144 (n=909)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 166.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.182 (n=1377)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.4706 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `1.0026` → IC=+0.187 (n=241)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 1.0026 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.408` → IC=+0.226 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.408 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.122 (n=955)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2920.0962` → IC=+0.240 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2920.0962 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.125 (n=1033)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 53.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.175 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1279` → IC=+0.155 (n=445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1279 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.209 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.4668` → IC=+0.129 (n=1310)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.4668 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.437` → IC=+0.127 (n=1281)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.437 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.149 (n=588)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.72 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2225` → IC=+0.168 (n=206)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2225 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4637` → IC=+0.152 (n=392)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4637 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.2313` → IC=+0.122 (n=533)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 2.2313 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2900.0851` → IC=+0.162 (n=445)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2900.0851 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0184` → IC=+0.214 (n=928)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0184 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.5111` → IC=+0.244 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5111 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.183` → IC=+0.231 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.183 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.372` → IC=+0.248 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.372 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2478` → IC=+0.210 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2478 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6303` → IC=+0.210 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6303 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.232 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.5676` → IC=+0.238 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5676 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2584.5792` → IC=+0.210 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2584.5792 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.234 (n=512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.225 (n=510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5122` → IC=+0.253 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5122 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.2665` → IC=+0.206 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2665 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.738` → IC=+0.261 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.738 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.234 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2859` → IC=+0.255 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2859 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2267` → IC=+0.195 (n=1189)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2267 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.198 (n=1350)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=2590)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.156 (n=2232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0094 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5272` → IC=+0.156 (n=2536)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5272 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.160 (n=883)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9392` → IC=+0.213 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9392 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1884` → IC=+0.156 (n=829)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1884 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.736` → IC=+0.168 (n=818)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.736 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.9096` → IC=+0.151 (n=1030)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9096 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1738` → IC=+0.175 (n=694)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1738 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4626` → IC=+0.162 (n=837)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4626 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.9066` → IC=+0.158 (n=1672)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9066 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8216.4561` → IC=+0.154 (n=1150)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8216.4561 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.188 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4875` → IC=+0.153 (n=1954)
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

- **PATRÓN** `dist_vwap_pct` > `0.7054` → IC=+0.142 (n=347)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.7054 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.306` → IC=+0.142 (n=1937)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.306 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.1151` → IC=+0.143 (n=1633)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1151 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.151 (n=920)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.5706` → IC=+0.138 (n=1935)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5706 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8237` → IC=+0.145 (n=1290)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8237 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=2590)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `7675.4145` → IC=+0.150 (n=1746)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7675.4145 (IC base=+0.134)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.171 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.174 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0035 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.185 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.195 (n=211)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5413 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2289` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2289 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.25` → IC=+0.166 (n=399)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 8.25 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.2448` → IC=+0.160 (n=316)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2448 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.8282` → IC=+0.195 (n=211)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.8282 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.3073` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3073 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.213 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.7022` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7022 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `12617.0993` → IC=+0.205 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12617.0993 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.206 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.3662` → IC=+0.145 (n=874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3662 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.157` → IC=+0.162 (n=385)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.157 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.6153` → IC=+0.138 (n=396)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.6153 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.7103` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.7103 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.2277` → IC=+0.133 (n=901)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2277 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.052` → IC=+0.149 (n=955)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 9.052 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8847` → IC=+0.177 (n=583)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8847 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.163 (n=413)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.5707` → IC=+0.140 (n=871)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5707 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.8153` → IC=+0.146 (n=580)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8153 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `11358.9394` → IC=+0.149 (n=873)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11358.9394 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `708.0` → IC=+0.137 (n=828)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 708.0 (IC base=+0.133)

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

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.215 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.170 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 18.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.6407` → IC=+0.218 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6407 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.1307` → IC=+0.168 (n=311)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1307 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.09` → IC=+0.220 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.09 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.0933` → IC=+0.128 (n=597)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0933 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `0.977` → IC=+0.126 (n=271)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.977 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.212 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.116` → IC=+0.169 (n=430)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.116 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=484)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.157 (n=260)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0688` → IC=+0.278 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0688 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.6098` → IC=+0.138 (n=161)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.6098 (IC base=-0.025)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.181 (n=236)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.006 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.5857` → IC=+0.210 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5857 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.4088` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4088 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.739` → IC=+0.126 (n=129)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 3.739 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `1.0529` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0529 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.158 (n=147)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.2602` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2602 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.198 (n=147)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=212)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2868.0323` → IC=+0.129 (n=192)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2868.0323 (IC base=+0.108)

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

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.177 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.005 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.6407` → IC=+0.251 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6407 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.1205` → IC=+0.185 (n=109)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1205 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.0679` → IC=+0.152 (n=208)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0679 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6313` → IC=+0.152 (n=185)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6313 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.7354` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.7354 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.3845` → IC=+0.160 (n=157)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.3845 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=217)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1103.6894` → IC=+0.194 (n=181)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 1103.6894 (IC base=+0.124)

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

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.170 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.083)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.135 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 13.0 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.201 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6757 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.8626` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.8626 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` > `1.0632` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.0632 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.1854` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.1854 (IC base=+0.083)

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
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=210)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.158 (n=197)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.75 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.2345` → IC=+0.127 (n=210)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.2345 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `3805.194` → IC=+0.158 (n=109)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3805.194 (IC base=+0.037)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

- **FILTRO** `volumen_regimen` < `1.0255` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0255
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=36)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0047 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.172 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0058 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.3956` → IC=+0.156 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3956 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.177 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.163 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 17.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.7143` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.7143 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.167 (n=79)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.7692 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.1961` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1961 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4486` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4486 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.0808` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0808 (IC base=-0.034)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.128 (n=501)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` > 0.5 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2842.677` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2842.677 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2318.1516` → IC=+0.122 (n=577)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2318.1516 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.156 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.128 (n=501)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` > 0.5 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2842.677` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2842.677 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2318.1516` → IC=+0.122 (n=577)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1366)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=604)

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
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6632)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.180 (n=2770)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=8451)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.172 (n=2861)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=8837)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.215 (n=475)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=1428)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.167 (n=485)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1605)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.205 (n=472)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1476)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.221 (n=489)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1575)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.168 (n=504)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=1560)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.200 (n=454)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1422)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.194 (n=507)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=1556)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=2460)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=2526)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=2532)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=302)

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
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=645)

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
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=18137)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.283 (n=6185)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=19988)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.245 (n=6481)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=19692)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.160 (n=8893)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=17280)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.224 (n=8219)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=24719)

- **FILTRO** `ibs_7min` > `0.2957` → IC=-0.177 (n=8234)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2957
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=24704)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=1302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=2927)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=1003)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3226)

- **FILTRO** `ibs_7min` < `0.7068` → IC=-0.262 (n=1395)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7068
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2834)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.197 (n=976)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3253)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.150 (n=3829)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=1890)

- **FILTRO** `drift_7min_pct` |x|> `0.1107` → IC=-0.122 (n=1944)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1107
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=3775)

- **FILTRO** `ibs_7min` > `0.7979` → IC=-0.207 (n=1429)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7979
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=4290)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1056)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3510)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.259 (n=1079)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3487)

- **FILTRO** `ibs_7min` < `0.7548` → IC=-0.189 (n=1141)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7548
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3425)

- **FILTRO** `ballena_activa_n` > `162.0` → IC=-0.179 (n=1137)

  - _Acción_: SKIP cuando `ballena_activa_n` > 162.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3429)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.257 (n=1104)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3547)

- **FILTRO** `ibs_7min` > `0.2539` → IC=-0.170 (n=1162)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2539
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3489)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.184 (n=1156)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3495)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.181 (n=970)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=2980)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.317 (n=953)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2997)

- **FILTRO** `drift_7min_pct` |x|> `0.1802` → IC=-0.132 (n=1342)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1802
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=2608)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.273 (n=977)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=2973)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.221 (n=919)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=3031)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.235 (n=1416)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=4618)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.155 (n=2050)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3984)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=1374)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=2942)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.253 (n=1058)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3258)

- **FILTRO** `ibs_7min` < `0.7429` → IC=-0.192 (n=1079)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=3237)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.186 (n=1066)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3250)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1091)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3336)

- **FILTRO** `ibs_7min` > `0.2743` → IC=-0.175 (n=1106)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2743
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3321)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.183 (n=1083)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3344)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.257 (n=1128)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3562)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.232 (n=1143)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3547)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.169 (n=1519)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4720)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=1346)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=3076)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.282 (n=1093)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3329)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.235 (n=1100)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=3322)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.211 (n=1079)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3343)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.206 (n=1391)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=4477)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=972)

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
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.137 (n=654)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.132 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `456.268` → IC=+0.159 (n=218)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 456.268 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.128 (n=296)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3728.089 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.126 (n=549)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 61.0 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.160 (n=51)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.137 (n=133)

  - _Acción_: Kelly boost +0.69€ cuando `total_vol_5m` < 422.506 (IC base=+0.136)

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

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.309 (n=82)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=168)

- **FILTRO** `pct_vs_K` |x|> `3.8394` → IC=-0.429 (n=82)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8394
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=168)

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

- **FILTRO** `sigma_h` < `0.0129` → IC=-0.339 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `T_h` > `86.0998` → IC=-0.357 (n=33)

  - _Acción_: SKIP cuando `T_h` > 86.0998
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
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=230)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.016)

- **PATRÓN** `streak_estiramiento` < `0.5545` → IC=+0.149 (n=95)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.5545 (IC base=+0.037)

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
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=593)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=599)

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

  - _Acción_: Kelly boost +0.66€ cuando `streak_len` < 4.0 (IC base=+0.028)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=482)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=976)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=576)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=597)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2423)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1250)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1258)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.191 (n=383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0041 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.218 (n=520)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1643` → IC=+0.179 (n=1010)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.1643 (IC base=+0.177)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0582` → IC=+0.180 (n=1147)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.0582 (IC base=+0.177)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.232 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.185 (n=805)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 11.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_15` > `0.62` → IC=+0.252 (n=1147)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.62 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.4191` → IC=+0.172 (n=269)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.4191 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.1023` → IC=+0.179 (n=750)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1023 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.836` → IC=+0.242 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.836 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `4949.0692` → IC=+0.180 (n=520)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4949.0692 (IC base=+0.177)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=390)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.213 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.263 (n=95)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.192)

- **PATRÓN** `drift_15min` |x|≤ `0.3775` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3775 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2245` → IC=+0.239 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2245 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.210 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.248 (n=284)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.3789` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3789 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.099` → IC=+0.195 (n=198)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.099 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.624` → IC=+0.244 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.624 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `15203.8562` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15203.8562 (IC base=+0.192)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.174 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.148 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0057 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.174 (n=93)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2725` → IC=+0.165 (n=183)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2725 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.151 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.6485` → IC=+0.231 (n=277)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6485 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1433` → IC=+0.164 (n=218)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1433 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `10004.8873` → IC=+0.141 (n=126)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 10004.8873 (IC base=+0.139)

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
  - _Potencial_: sin este filtro IC_bueno=+0.247 (n=156)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.212 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1757` → IC=+0.171 (n=156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1757 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0669` → IC=+0.195 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.0669 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2704` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2704 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.183 (n=118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.247 (n=156)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.5591` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.5591 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.164 (n=129)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3004.2322` → IC=+0.267 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.2322 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.146)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5695` → IC=-0.142 (n=118)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5695
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=620)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.259 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.201 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0442` → IC=+0.200 (n=321)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0442 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0933` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0933 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.241 (n=160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.280 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.55 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1139` → IC=+0.202 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1139 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.55` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.55 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.189 (n=352)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `2841.1464` → IC=+0.262 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2841.1464 (IC base=+0.188)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.171 (n=366)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` < 0.1111 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.372 (n=147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.339 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.343 (n=215)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.371 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.374 (n=323)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.4105` → IC=+0.379 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4105 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.085` → IC=+0.342 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.085 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.332 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.340 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3895.4216` → IC=+0.352 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3895.4216 (IC base=+0.333)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1225` → IC=+0.340 (n=79)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1225 (IC base=+0.334)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.355 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.334)

- **PATRÓN** `drift_60min` |x|≤ `0.1497` → IC=+0.344 (n=158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1497 (IC base=+0.334)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.344 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.334)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.412 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.334)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.347 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.334)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.332 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.334)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.368 (n=180)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.334)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.339 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.334)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.341 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.334)

- **PATRÓN** `libro_liquidez` > `9210.2084` → IC=+0.344 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9210.2084 (IC base=+0.334)

- **PATRÓN** `ballena_activa_n` < `474.0` → IC=+0.400 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 474.0 (IC base=+0.334)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.357 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.330 (n=127)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.336 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.346 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.348 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.384 (n=144)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.344 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.367 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `3525.4286` → IC=+0.357 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3525.4286 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.329 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.204 (n=549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1649)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.178 (n=701)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1497)

- **FILTRO** `libro_liquidez` < `3781.8456` → IC=-0.123 (n=1450)

  - _Acción_: SKIP cuando `libro_liquidez` < 3781.8456
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=748)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2964` → IC=+0.228 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2964 (IC base=-0.059)

- **PATRÓN** `ibs_15` > `0.6098` → IC=+0.253 (n=548)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6098 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.2658` → IC=+0.176 (n=433)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2658 (IC base=-0.059)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1175` → IC=+0.236 (n=809)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1175 (IC base=-0.042)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1825` → IC=+0.243 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1825 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3571` → IC=+0.282 (n=1215)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3571 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.6504` → IC=+0.262 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6504 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.210 (n=332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=999)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.226 (n=439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=892)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.206 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=485)

- **FILTRO** `sigma_ewma_delta_pct` > `19.843` → IC=-0.241 (n=237)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.843
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1094)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.170 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0026 (IC base=+0.070)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1145` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1145 (IC base=+0.070)

- **PATRÓN** `ibs_15` > `0.8021` → IC=+0.333 (n=112)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8021 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.256 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.34` → IC=+0.258 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.34 (IC base=+0.070)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6537` → IC=-0.222 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6537
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=268)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=339)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.141 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0066 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.168 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.004 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0771` → IC=+0.217 (n=118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0771 (IC base=+0.137)

- **PATRÓN** `drift_15min` |x|≤ `0.4253` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.4253 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3062` → IC=+0.239 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3062 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.140 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.256 (n=268)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.177 (n=193)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.838` → IC=+0.147 (n=287)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 18.838 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=339)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `10544.7398` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 10544.7398 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.249 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.4379` → IC=+0.230 (n=509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4379 (IC base=+0.229)

- **PATRÓN** `drift_15min` |x|≤ `0.7761` → IC=+0.238 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7761 (IC base=+0.229)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1994` → IC=+0.260 (n=231)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1994 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.241 (n=345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.229)

- **PATRÓN** `ibs_15` < `0.2758` → IC=+0.287 (n=448)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2758 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.3755` → IC=+0.256 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3755 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.82` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.82 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.033` → IC=+0.237 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.033 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `3591.8273` → IC=+0.232 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3591.8273 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.230 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.229)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.8773` → IC=-0.254 (n=132)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8773
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=399)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.218 (n=200)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=331)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.157)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.157)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0726` → IC=+0.214 (n=218)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0726 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.253 (n=245)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1586` → IC=+0.210 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1586 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0194` → IC=-0.261 (n=329)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0194
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=330)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=485)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1088` → IC=+0.345 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1088 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3437` → IC=+0.311 (n=353)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3437 (IC base=-0.044)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.287 (n=247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.310 (n=182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.289 (n=363)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.221` → IC=+0.319 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.221 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8374` → IC=+0.322 (n=544)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8374 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.322 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.322 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.287 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `12706.4331` → IC=+0.299 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12706.4331 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.289 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.280 (n=139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.316 (n=101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.4172` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4172 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.246` → IC=+0.277 (n=101)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.246 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3724` → IC=+0.293 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3724 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.329 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.8239` → IC=+0.297 (n=303)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8239 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.335 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15699.4792` → IC=+0.316 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15699.4792 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.307 (n=242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.303 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.307 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1881` → IC=+0.312 (n=110)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1881 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.338 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.341 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.340 (n=242)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.311 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.295 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.682` → IC=+0.322 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.682 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.305 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.297 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.296)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.62 sube el IC de +0.177 a +0.252 en UPDOWN_GBM#15min (n=1147). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.192 a +0.248 en UPDOWN_GBM#BTC#15min (n=284). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6485 sube el IC de +0.139 a +0.231 en UPDOWN_GBM#ETH#15min (n=277). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.146 a +0.247 en UPDOWN_GBM#SOL#15min (n=156). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.188 a +0.280 en UPDOWN_GBM#XRP#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.046 a +0.171 en UPDOWN_GBM#XRP#15min (n=366). Ya aplicado como kelly_boost=+0.86€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6098 sube el IC de -0.059 a +0.253 en UPDOWN_GBM_15M_TARDIO (n=548). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3571 sube el IC de -0.042 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=1215). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8021 sube el IC de +0.070 a +0.333 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=112). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.137 a +0.256 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=268). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2758 sube el IC de +0.229 a +0.287 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=448). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.157 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.042 a +0.253 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3437 sube el IC de -0.044 a +0.311 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=353). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8374 sube el IC de +0.285 a +0.322 en UPDOWN_GBM_IBS_ALTO (n=544). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8239 sube el IC de +0.275 a +0.297 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=303). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.296 a +0.340 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=242). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.333 a +0.374 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=323). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.334 a +0.368 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.329 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=144). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
| ✅ BALLENAS_TARDIAS | 21318 | -0.097 | -3136.74€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1272 | -0.050 | -194.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 20046 | -0.100 | -2942.11€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3287 | -0.103 | -560.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3287 | -0.103 | -560.94€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1272 | -0.050 | -194.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1272 | -0.050 | -194.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6099 | -0.040 | -606.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6099 | -0.040 | -606.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5666 | -0.101 | -480.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5666 | -0.101 | -480.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4620 | -0.172 | -1133.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4620 | -0.172 | -1133.29€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 13201 | -0.039 | +4206.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3528 | -0.006 | +1836.52€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 9673 | -0.051 | +2370.26€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 13201 | -0.039 | +4206.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3528 | -0.006 | +1836.52€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 9673 | -0.051 | +2370.26€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1148 | -0.104 | -167.70€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 92 | -0.043 | -9.07€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1056 | -0.110 | -158.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 658 | -0.086 | -79.46€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 68 | -0.029 | -3.84€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 590 | -0.093 | -75.62€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 316 | -0.154 | -74.29€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 292 | -0.160 | -69.07€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 113 | -0.048 | -13.80€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 113 | -0.048 | -13.80€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 77369 | +0.114 | -3915.50€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 12007 | +0.183 | -357.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 298 | -0.120 | -46.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 59777 | +0.101 | -3368.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5287 | +0.114 | -143.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 9957 | +0.097 | -909.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 39 | -0.159 | -2.72€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 9903 | +0.099 | -895.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 15642 | +0.132 | -304.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3694 | +0.203 | -108.29€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 9903 | +0.110 | -176.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2003 | +0.114 | +2.68€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 9997 | +0.089 | -969.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 47 | -0.051 | -1.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 9935 | +0.090 | -956.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 16550 | +0.125 | -288.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4637 | +0.173 | -69.02€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 9998 | +0.108 | -160.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1903 | +0.098 | -50.81€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 15249 | +0.115 | -877.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3550 | +0.185 | -186.69€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 201 | -0.081 | +7.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 10117 | +0.092 | -603.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1381 | +0.134 | -95.03€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 9974 | +0.103 | -567.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 40 | +0.000 | +10.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 9921 | +0.104 | -577.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 12223 | +0.189 | -849.59€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 12223 | +0.189 | -849.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2992 | +0.167 | -329.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2992 | +0.167 | -329.06€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 722 | +0.184 | +1.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 722 | +0.184 | +1.77€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2928 | +0.178 | -268.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2928 | +0.178 | -268.36€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2628 | +0.236 | -84.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2628 | +0.236 | -84.86€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2874 | +0.191 | -182.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2874 | +0.191 | -182.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 569 | +0.433 | -11.03€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 569 | +0.433 | -11.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 218 | +0.436 | -2.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 218 | +0.436 | -2.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 216 | +0.440 | +0.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 216 | +0.440 | +0.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 127 | +0.407 | -7.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 127 | +0.407 | -7.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 41824 | +0.195 | -3470.79€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 41824 | +0.195 | -3470.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 7277 | +0.171 | -911.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 7277 | +0.171 | -911.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6643 | +0.224 | -241.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6643 | +0.224 | -241.06€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7244 | +0.170 | -914.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7244 | +0.170 | -914.45€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6740 | +0.217 | -285.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6740 | +0.217 | -285.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6900 | +0.203 | -467.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6900 | +0.203 | -467.56€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 7020 | +0.191 | -650.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 7020 | +0.191 | -650.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 15672 | +0.124 | +304.72€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 15672 | +0.124 | +304.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7774 | +0.129 | +204.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7774 | +0.129 | +204.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7898 | +0.120 | +100.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7898 | +0.120 | +100.51€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1277 | +0.287 | -24.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1277 | +0.287 | -24.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 566 | +0.271 | -23.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 566 | +0.271 | -23.07€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 893 | +0.072 | -40.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 316 | +0.057 | -27.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 577 | +0.080 | -13.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 697 | +0.081 | -16.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 120 | +0.082 | -3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 577 | +0.080 | -13.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 141 | +0.004 | -28.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 141 | +0.004 | -28.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 27938 | +0.099 | -817.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2348 | +0.095 | +36.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 25590 | +0.099 | -853.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 15884 | +0.103 | -221.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2348 | +0.095 | +36.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 13536 | +0.104 | -257.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4942 | +0.115 | +40.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4942 | +0.115 | +40.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 7112 | +0.078 | -636.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 7112 | +0.078 | -636.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 735 | +0.242 | -93.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 735 | +0.242 | -93.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 735 | +0.242 | -93.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 735 | +0.242 | -93.40€ | 0 | 4 |
| ✅ GBM_LATE_15M | 20546 | +0.076 | +9254.49€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 20546 | +0.076 | +9254.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3371 | +0.193 | +2448.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3371 | +0.193 | +2448.45€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 3038 | +0.174 | +2036.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3038 | +0.174 | +2036.95€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 3521 | +0.195 | +2577.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3521 | +0.195 | +2577.01€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 3069 | +0.007 | +486.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3069 | +0.007 | +486.33€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 3006 | -0.037 | +642.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3006 | -0.037 | +642.16€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 4541 | -0.049 | +1063.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4541 | -0.049 | +1063.59€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 21630 | +0.079 | +10765.78€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 21630 | +0.079 | +10765.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3990 | +0.013 | +1970.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3990 | +0.013 | +1970.92€ | 2 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4565 | +0.007 | +874.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4565 | +0.007 | +874.51€ | 1 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3064 | +0.257 | +3020.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3064 | +0.257 | +3020.35€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3421 | -0.012 | +456.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3421 | -0.012 | +456.07€ | 2 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3570 | +0.015 | +1265.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3570 | +0.015 | +1265.97€ | 3 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3020 | +0.272 | +3177.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3020 | +0.272 | +3177.96€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 16674 | +0.168 | +12207.12€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 16674 | +0.168 | +12207.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2470 | +0.206 | +1953.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2470 | +0.206 | +1953.11€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2643 | +0.153 | +1900.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2643 | +0.153 | +1900.03€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2582 | +0.204 | +2015.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2582 | +0.204 | +2015.32€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2765 | +0.141 | +1895.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2765 | +0.141 | +1895.14€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3145 | +0.111 | +2028.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3145 | +0.111 | +2028.71€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3069 | +0.202 | +2414.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3069 | +0.202 | +2414.80€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4252 | +0.126 | +1744.52€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4252 | +0.126 | +1744.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 163 | +0.112 | +63.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 163 | +0.112 | +63.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1158 | +0.121 | +479.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1158 | +0.121 | +479.75€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1160 | +0.151 | +540.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1160 | +0.151 | +540.43€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 900 | +0.089 | +259.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 900 | +0.089 | +259.47€ | 1 | 11 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 20590 | +0.173 | +14926.13€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 20590 | +0.173 | +14926.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3220 | +0.219 | +2695.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3220 | +0.219 | +2695.29€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3229 | +0.151 | +2126.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3229 | +0.151 | +2126.14€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3340 | +0.221 | +2824.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3340 | +0.221 | +2824.46€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3297 | +0.138 | +2165.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3297 | +0.138 | +2165.84€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3613 | +0.106 | +2082.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3613 | +0.106 | +2082.03€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3891 | +0.203 | +3032.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3891 | +0.203 | +3032.36€ | 0 | 22 |
| ✅ GBM_LATE_5M | 5985 | +0.140 | +3237.99€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5985 | +0.140 | +3237.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1585 | +0.140 | +969.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1585 | +0.140 | +969.76€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1823 | +0.145 | +982.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1823 | +0.145 | +982.89€ | 0 | 30 |
| ✅ GBM_LATE_5M#SOL | 321 | +0.029 | +39.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 321 | +0.029 | +39.66€ | 2 | 4 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1311 | +0.067 | +582.00€ | 2 | 14 |
| ✅ GBM_LATE_60M#60min | 1311 | +0.067 | +582.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 467 | +0.088 | +202.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 467 | +0.088 | +202.78€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 437 | +0.072 | +222.53€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 437 | +0.072 | +222.53€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 407 | +0.035 | +156.68€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 407 | +0.035 | +156.68€ | 1 | 11 |
| 🚫 GBM_LATE_60M_FADE | 310 | -0.266 | -23.39€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 310 | -0.266 | -23.39€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 115 | -0.227 | -8.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 115 | -0.227 | -8.70€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 105 | -0.285 | -10.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 105 | -0.285 | -10.96€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 90 | -0.283 | -3.74€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 90 | -0.283 | -3.74€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 612 | +0.055 | +119.30€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 612 | +0.055 | +119.30€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 243 | +0.047 | +38.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 243 | +0.047 | +38.41€ | 3 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 181 | +0.035 | +3.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 181 | +0.035 | +3.29€ | 3 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 188 | +0.084 | +77.60€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 188 | +0.084 | +77.60€ | 2 | 15 |
| ✅ LATE_WINDOW_5MIN | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1461 | +0.106 | +430.47€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1461 | +0.106 | +430.47€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1461 | +0.106 | +430.47€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1461 | +0.106 | +430.47€ | 0 | 4 |
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
| ✅ LIQUIDACIONES_5M | 1564 | -0.002 | -2.82€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1564 | -0.002 | -2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 170 | -0.012 | +5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 170 | -0.012 | +5.32€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 651 | +0.024 | +17.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 651 | +0.024 | +17.32€ | 5 | 0 |
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
| ✅ MOMENTUM_IBS_15M | 13496 | -0.011 | -178.68€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 13496 | -0.011 | -178.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2518 | -0.021 | -48.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2518 | -0.021 | -48.02€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2831 | -0.014 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2831 | -0.014 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3327 | -0.016 | -60.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3327 | -0.016 | -60.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 22919 | -0.011 | +1001.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 22919 | -0.011 | +1001.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3993 | +0.010 | +509.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3993 | +0.010 | +509.93€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3682 | -0.025 | -22.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3682 | -0.025 | -22.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4012 | +0.004 | +306.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4012 | +0.004 | +306.65€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3457 | -0.047 | -95.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3457 | -0.047 | -95.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3836 | -0.014 | +158.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3836 | -0.014 | +158.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3939 | -0.000 | +144.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3939 | -0.000 | +144.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5087 | -0.043 | -127.27€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5087 | -0.043 | -127.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1120 | -0.053 | -23.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1120 | -0.053 | -23.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 483 | -0.127 | -25.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 483 | -0.127 | -25.05€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1394 | -0.059 | -30.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1394 | -0.059 | -30.93€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 59111 | -0.073 | +1177.59€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 59111 | -0.073 | +1177.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 9948 | -0.081 | +573.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 9948 | -0.081 | +573.11€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 9217 | -0.090 | -368.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 9217 | -0.090 | -368.25€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 9984 | -0.070 | +508.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 9984 | -0.070 | +508.82€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8743 | -0.094 | -258.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8743 | -0.094 | -258.66€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 10929 | -0.048 | +344.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 10929 | -0.048 | +344.92€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 10290 | -0.064 | +377.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 10290 | -0.064 | +377.65€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6758 | -0.021 | -96.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6758 | -0.021 | -96.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1519 | -0.019 | -3.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1519 | -0.019 | -3.37€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1501 | -0.014 | -2.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1501 | -0.014 | -2.33€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1003 | -0.038 | -16.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1003 | -0.038 | -16.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1006 | +0.113 | +353.28€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 870 | +0.122 | +340.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 201 | +0.136 | +98.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 201 | +0.136 | +98.05€ | 0 | 3 |
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
| 🚫 PRICE_TARGET_GBM_FADE | 560 | -0.221 | -47.50€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 233 | -0.202 | -34.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 201 | -0.195 | -32.31€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 198 | -0.240 | -23.51€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 171 | -0.251 | -27.60€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 129 | -0.218 | +10.61€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 115 | -0.218 | +7.55€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 487 | -0.222 | -52.36€ | 0 | 0 |
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
| ✅ STREAK_FADE_15M | 406 | +0.029 | +11.58€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 406 | +0.029 | +11.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 180 | +0.028 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 180 | +0.028 | +2.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 47 | -0.031 | -4.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 47 | -0.031 | -4.66€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 153 | +0.035 | +9.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 153 | +0.035 | +9.68€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 2490 | -0.027 | -116.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2490 | -0.027 | -116.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 563 | -0.024 | -23.90€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 563 | -0.024 | -23.90€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 153 | -0.042 | -13.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 153 | -0.042 | -13.91€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 970 | -0.034 | -51.46€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 970 | -0.034 | -51.46€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 60 | -0.032 | -2.60€ | 2 | 1 |
| ✅ STREAK_FADE_60M#60min | 60 | -0.032 | -2.60€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 23 | +0.060 | +1.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 23 | +0.060 | +1.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6694 | +0.024 | +104.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6694 | +0.024 | +104.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2117 | +0.021 | +19.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2117 | +0.021 | +19.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1404 | +0.031 | +36.73€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1404 | +0.031 | +36.73€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1958 | +0.016 | +9.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1958 | +0.016 | +9.60€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1215 | +0.034 | +38.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1215 | +0.034 | +38.18€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6161 | +0.014 | -25.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6161 | +0.014 | -25.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2442 | +0.020 | +2.82€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2442 | +0.020 | +2.82€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2437 | +0.016 | -5.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2437 | +0.016 | -5.31€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1282 | -0.002 | -22.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1282 | -0.002 | -22.55€ | 2 | 0 |
| ✅ UPDOWN_GBM | 26940 | +0.030 | +1524.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 7249 | +0.060 | +1172.34€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1014 | +0.005 | +8.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 16928 | +0.023 | +341.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1639 | +0.001 | +0.68€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2389 | +0.071 | +238.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 313 | +0.132 | +104.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2057 | +0.063 | +134.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4887 | +0.033 | +321.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 884 | +0.082 | +199.38€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 287 | +0.022 | +7.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2949 | +0.029 | +108.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 725 | -0.001 | +6.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 42 | -0.114 | +0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3172 | +0.033 | +119.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 264 | +0.124 | +80.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2892 | +0.025 | +39.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 5596 | +0.017 | +216.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1978 | +0.047 | +213.71€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 274 | +0.007 | +7.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2726 | +0.002 | -3.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 582 | -0.002 | -4.74€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 36 | -0.158 | +3.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6861 | +0.017 | +166.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1926 | +0.023 | +111.57€ | 1 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 268 | -0.007 | -2.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4305 | +0.018 | +59.55€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 332 | +0.009 | -0.65€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 30 | -0.156 | -1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4033 | +0.042 | +463.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1884 | +0.079 | +462.96€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 150 | -0.007 | -2.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1999 | +0.012 | +2.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 108 | -0.145 | +3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 430 | +0.333 | +120.54€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 430 | +0.333 | +120.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 239 | +0.334 | +62.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 239 | +0.334 | +62.45€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 191 | +0.329 | +58.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 191 | +0.329 | +58.09€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 9415 | -0.046 | +2003.25€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 9415 | -0.046 | +2003.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 455 | -0.049 | +342.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 455 | -0.049 | +342.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1792 | -0.128 | +34.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1792 | -0.128 | +34.87€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 162 | +0.128 | +71.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 162 | +0.128 | +71.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1034 | +0.198 | +592.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1034 | +0.198 | +592.70€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2993 | -0.063 | +457.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2993 | -0.063 | +457.32€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2979 | -0.075 | +504.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2979 | -0.075 | +504.39€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 108 | +0.073 | +17.16€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 108 | +0.073 | +17.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 108 | +0.073 | +17.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 108 | +0.073 | +17.16€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 725 | +0.285 | +577.94€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 725 | +0.285 | +577.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 403 | +0.275 | +302.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 403 | +0.275 | +302.23€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 322 | +0.296 | +275.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 322 | +0.296 | +275.71€ | 0 | 12 |
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