# Hipótesis automáticas — 2026-09-17 00:48 UTC
_Generado por shadow_postmortem.py sobre 474074 resoluciones (PNL=+51004.10€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=439)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=410)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.248 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.213 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.803` → IC=+0.262 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.803 (IC base=+0.122)

- **PATRÓN** `banda_z` > `10.241` → IC=+0.224 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.241 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.139 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=511)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2807.4678` → IC=+0.132 (n=321)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2807.4678 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=339)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.257 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.130)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.217 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.271 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.130)

- **PATRÓN** `banda_z` > `11.377` → IC=+0.250 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.377 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=426)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `2641.4924` → IC=+0.133 (n=336)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2641.4924 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 88.0 (IC base=+0.034)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=86)

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

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.250 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.100)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.100)

- **PATRÓN** `banda_z` > `6.169` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `banda_z` > 6.169 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `1358.622` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1358.622 (IC base=+0.100)

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
- **FILTRO** `restante_s_al_confirmar` < `144.08` → IC=-0.251 (n=5853)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.08
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=17560)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `139.14` → IC=-0.275 (n=805)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.14
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=2415)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `487.24` → IC=-0.161 (n=314)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 487.24
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=942)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `135.32` → IC=-0.283 (n=712)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.32
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2139)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.17` → IC=-0.251 (n=1392)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.17
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4179)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `117.51` → IC=-0.365 (n=1127)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.51
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=3384)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.242 (n=265)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=283)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.143 (n=127)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=404)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.151 (n=127)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=404)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.248 (n=137)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=155)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.156 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=210)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.259 (n=81)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=113)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.196 (n=11865)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.69 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=2956)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5302.2196` → IC=+0.169 (n=1883)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5302.2196 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=9295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=10914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.247 (n=8091)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=5817)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7223.6182` → IC=+0.177 (n=1839)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7223.6182 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.347 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `15038.9938` → IC=+0.214 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15038.9938 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=1388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.264 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `13230.2763` → IC=+0.217 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13230.2763 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.185 (n=277)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.62 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=286)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `4641.025` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4641.025 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.185 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.168 (n=576)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` < 0.425 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=546)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3855.8996` → IC=+0.152 (n=423)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3855.8996 (IC base=+0.131)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=2017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.328 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=1069)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.301 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.245 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `3154.5283` → IC=+0.243 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3154.5283 (IC base=+0.239)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.133 (n=551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 17.0 (IC base=+0.129)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.224 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=465)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `1928.4642` → IC=+0.159 (n=367)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1928.4642 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `5833.0086` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 5833.0086 (IC base=+0.081)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.221 (n=522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.423 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.268 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.180 (n=1126)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.03 (IC base=+0.175)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.172 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 13.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.743` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.743 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.224 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=328)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=9338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=8908)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.221 (n=3300)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=2213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.178 (n=2306)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.310 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.290 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.321 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.279)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=2165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=1948)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=2048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=1733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.320 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.237)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=1893)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.195 (n=1595)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.432 (n=365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `2062.8229` → IC=+0.440 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2062.8229 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.434 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.437 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.455 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `12146.257` → IC=+0.444 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12146.257 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.453 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.413 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.398 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.404)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=27723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.238 (n=10490)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5654)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=5102)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.171)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=4935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=4900)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.272 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.175 (n=4772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=5087)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.169)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=2498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=1865)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=1748)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=4579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.255 (n=2322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=4642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=3684)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.249 (n=1846)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.206 (n=4214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.133 (n=3843)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.07 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.154 (n=3856)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.95 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.137 (n=5670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.29` → IC=+0.154 (n=3842)

  - _Acción_: Kelly boost +0.77€ cuando `lag_apertura_s` < 3.29 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.210 (n=2126)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.129)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.135 (n=1915)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.01 (IC base=+0.129)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.149 (n=2057)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.93 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.146 (n=2803)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.129)

- **PATRÓN** `lag_apertura_s` < `4.03` → IC=+0.153 (n=1906)

  - _Acción_: Kelly boost +0.77€ cuando `lag_apertura_s` < 4.03 (IC base=+0.129)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.202 (n=2088)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.126 (n=2564)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.149 (n=1988)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.96 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.124 (n=2253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.129 (n=2867)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.49` → IC=+0.150 (n=1940)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 2.49 (IC base=+0.120)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.384 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1604.9934` → IC=+0.298 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1604.9934 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.300 (n=293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.272)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.329 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `5065.6943` → IC=+0.294 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5065.6943 (IC base=+0.272)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.329 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1492.929` → IC=+0.315 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1492.929 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.340 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.333)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.359 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.333)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.346 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.370 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.333)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.438 (n=368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.433 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `1860.5823` → IC=+0.438 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.5823 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.434 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.447 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.434 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `2127.0131` → IC=+0.455 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2127.0131 (IC base=+0.434)

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
- **PATRÓN** `ibs_20min` > `0.9778` → IC=+0.230 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9778 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.2156` → IC=+0.245 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2156 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.863` → IC=+0.168 (n=2435)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.863 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.6095` → IC=+0.253 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6095 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.244 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0731 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.308` → IC=+0.205 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.308 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `1.9234` → IC=+0.198 (n=2776)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.9234 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.5687` → IC=+0.130 (n=7725)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.5687 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.5728` → IC=+0.185 (n=459)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5728 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.344` → IC=+0.168 (n=2693)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.344 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `1.2069` → IC=+0.169 (n=2530)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2069 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.8712` → IC=+0.176 (n=1686)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8712 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.225 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `1.4676` → IC=+0.197 (n=4208)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4676 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.210 (n=3975)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 155.0 (IC base=+0.059)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.181 (n=477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0049 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.181 (n=474)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0078 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3249` → IC=+0.164 (n=1422)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3249 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.187 (n=529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.047` → IC=+0.275 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.047 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.204 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.4344` → IC=+0.163 (n=1311)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4344 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.185 (n=1327)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.04 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=945)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.193` → IC=+0.273 (n=703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.193 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.252 (n=724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.290 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.377` → IC=+0.247 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.377 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.232 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.274 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.7136` → IC=+0.262 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7136 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1740.7639` → IC=+0.254 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1740.7639 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.234 (n=480)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.1142` → IC=+0.242 (n=474)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1142 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=1076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.211 (n=1090)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9179` → IC=+0.253 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9179 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.217 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.3728` → IC=+0.214 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3728 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.828` → IC=+0.235 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.828 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.258` → IC=+0.222 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.258 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8723` → IC=+0.212 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8723 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.219 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7478` → IC=+0.217 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7478 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.368` → IC=+0.222 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.368 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `10984.4814` → IC=+0.222 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10984.4814 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.154 (n=1015)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0049 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.158 (n=384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6717` → IC=+0.172 (n=1151)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6717 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1275` → IC=+0.150 (n=1049)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1275 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.49` → IC=+0.170 (n=195)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.49 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.143 (n=1151)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2089 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.615` → IC=+0.138 (n=1151)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.615 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1575` → IC=+0.184 (n=311)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1575 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4311` → IC=+0.151 (n=1042)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4311 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `13509.2539` → IC=+0.149 (n=767)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 13509.2539 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `423.0` → IC=+0.144 (n=959)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 423.0 (IC base=+0.136)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.189 (n=1389)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0058 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=1391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.190 (n=527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.254 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.52` → IC=+0.227 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.52 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.183 (n=1180)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.3768` → IC=+0.191 (n=179)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.3768 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `3.0198` → IC=+0.198 (n=590)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 3.0198 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=1593)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.196 (n=494)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 16.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.222 (n=1194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.215 (n=1068)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.247 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.3796` → IC=+0.231 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3796 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.556` → IC=+0.234 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.556 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.378` → IC=+0.216 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.378 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.263 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.8456` → IC=+0.205 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8456 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.3042` → IC=+0.224 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3042 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.227 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1887.161` → IC=+0.233 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.161 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.220 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1753)

- **PATRÓN** `ibs_20min` > `0.9343` → IC=+0.177 (n=289)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.9343 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.3351` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3351 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.4875` → IC=+0.329 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4875 (IC base=+0.007)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.304` → IC=+0.138 (n=545)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 4.304 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6461` → IC=+0.372 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6461 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.1956` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1956 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.355 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.4862` → IC=+0.338 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4862 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.1278` → IC=+0.343 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1278 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.344 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 165.0 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.1669` → IC=+0.192 (n=196)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1669 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.695 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.151 (n=193)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1643 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2684` → IC=+0.240 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2684 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.5087` → IC=+0.187 (n=471)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.5087 (IC base=+0.004)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=254)

- **FILTRO** `ibs_20min` < `0.375` → IC=-0.170 (n=98)

  - _Acción_: SKIP cuando `ibs_20min` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=206)

- **FILTRO** `ibs_20min` > `0.2692` → IC=-0.127 (n=1777)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=877)

- **FILTRO** `sigma_ewma_delta_pct` > `8.642` → IC=-0.205 (n=290)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.642
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=2364)

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

- **PATRÓN** `dist_vwap_pct` > `0.7533` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7533 (IC base=-0.046)

- **PATRÓN** `volumen_regimen` < `1.1044` → IC=+0.216 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1044 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1972` → IC=+0.219 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1972 (IC base=-0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.1481` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1481 (IC base=-0.046)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.250 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=-0.046)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6615` → IC=-0.195 (n=441)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6615
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1325)

- **FILTRO** `ibs_20min` < `0.7937` → IC=-0.141 (n=1324)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7937
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=442)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.202 (n=380)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=1386)

- **FILTRO** `ibs_20min` > `0.7744` → IC=-0.200 (n=669)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7744
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2008)

- **PATRÓN** `dist_vwap_pct` > `0.9754` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9754 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` < `0.2585` → IC=+0.298 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2585 (IC base=-0.085)

- **PATRÓN** `volumen_regimen` > `0.6119` → IC=+0.285 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6119 (IC base=-0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.1674` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1674 (IC base=-0.085)

- **PATRÓN** `volumen_spike_ratio` < `2.4964` → IC=+0.271 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4964 (IC base=-0.085)

- **PATRÓN** `volumen_spike_ratio` > `1.8274` → IC=+0.288 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8274 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` > `1.0236` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0236 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` < `0.2617` → IC=+0.248 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2617 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` < `0.7337` → IC=+0.243 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7337 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` > `1.0842` → IC=+0.290 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0842 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.1058` → IC=+0.274 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1058 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.224` → IC=+0.261 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.224 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.4747` → IC=+0.245 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4747 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.249 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.175 (n=2632)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0092 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.9813` → IC=+0.289 (n=2632)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9813 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `1.0147` → IC=+0.286 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0147 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.523` → IC=+0.144 (n=3731)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.523 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6753` → IC=+0.237 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6753 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` < `0.1128` → IC=+0.226 (n=4082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1128 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.247` → IC=+0.257 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.247 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `1.4778` → IC=+0.246 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4778 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.771` → IC=+0.236 (n=1428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.771 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.277 (n=3770)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.139 (n=2670)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0085 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.150 (n=7047)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5556 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6847` → IC=+0.242 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6847 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.231` → IC=+0.231 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.231 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.232 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7129 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `1.2024` → IC=+0.248 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2024 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2521` → IC=+0.321 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2521 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.4931` → IC=+0.254 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4931 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `2.3705` → IC=+0.255 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3705 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.256 (n=2731)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2335` → IC=-0.142 (n=543)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2335
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1629)

- **FILTRO** `sigma_ewma_delta_pct` > `4.411` → IC=-0.163 (n=396)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.411
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=1327)

- **PATRÓN** `ibs_20min` > `0.8636` → IC=+0.251 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8636 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.29` → IC=+0.149 (n=733)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.29 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2262` → IC=+0.291 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2262 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.4428` → IC=+0.197 (n=186)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4428 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `2.6525` → IC=+0.195 (n=185)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6525 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.024)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8256` → IC=-0.149 (n=590)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8256
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1771)

- **PATRÓN** `dist_vwap_pct` > `0.299` → IC=+0.137 (n=257)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.299 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1637` → IC=+0.130 (n=596)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1637 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` < `1.0528` → IC=+0.131 (n=611)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0528 (IC base=+0.012)

- **PATRÓN** `volumen_regimen` > `0.6498` → IC=+0.140 (n=620)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6498 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2195` → IC=+0.169 (n=125)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2195 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.178 (n=225)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.189 (n=223)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 230.0 (IC base=+0.012)

- **PATRÓN** `dist_vwap_pct` < `0.1603` → IC=+0.207 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1603 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `0.6836` → IC=+0.201 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6836 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.8117` → IC=+0.207 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8117 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.220 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=-0.000)

- **PATRÓN** `ballena_activa_n` < `243.0` → IC=+0.218 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 243.0 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.266 (n=1124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0983` → IC=+0.248 (n=418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0983 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.241 (n=635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.252 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.534` → IC=+0.275 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.534 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1109` → IC=+0.254 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1109 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8808` → IC=+0.238 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8808 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `3.6431` → IC=+0.252 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6431 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.295 (n=1000)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.316 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.284 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.795` → IC=+0.297 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.795 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.302 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.6329` → IC=+0.283 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6329 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.237` → IC=+0.280 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.237 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `1877.4384` → IC=+0.303 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.4384 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.273 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.278)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2479` → IC=-0.209 (n=362)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2479
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1086)

- **FILTRO** `ibs_20min` > `0.806` → IC=-0.185 (n=471)

  - _Acción_: SKIP cuando `ibs_20min` > 0.806
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1416)

- **PATRÓN** `ibs_20min` > `0.8048` → IC=+0.148 (n=493)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.8048 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.4595` → IC=+0.218 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4595 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` < `0.9683` → IC=+0.214 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9683 (IC base=-0.011)

- **PATRÓN** `volumen_regimen` > `0.6162` → IC=+0.196 (n=304)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.6162 (IC base=-0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.266` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.266 (IC base=-0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4764` → IC=+0.266 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4764 (IC base=-0.011)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.245 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1247 (IC base=-0.018)

- **PATRÓN** `dist_vwap_pct` < `0.2864` → IC=+0.176 (n=254)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2864 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` < `1.1494` → IC=+0.175 (n=244)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.1494 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` > `0.7204` → IC=+0.182 (n=218)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.7204 (IC base=-0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.1505` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1505 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4278` → IC=+0.257 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4278 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.3824` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3824 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.246 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6727` → IC=-0.209 (n=854)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6727
  - _Potencial_: sin este filtro IC_bueno=+0.261 (n=854)

- **FILTRO** `ibs_20min` > `0.7111` → IC=-0.233 (n=451)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7111
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=1356)

- **FILTRO** `sigma_ewma_delta_pct` > `4.677` → IC=-0.176 (n=421)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.677
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=1386)

- **PATRÓN** `ibs_20min` > `0.6727` → IC=+0.261 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6727 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7744` → IC=+0.335 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7744 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.289 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8622 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.7198` → IC=+0.277 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7198 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.279 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.330 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4442` → IC=+0.320 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4442 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.321 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.1071` → IC=+0.197 (n=453)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1071 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` > `0.5893` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.5893 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` < `0.3961` → IC=+0.192 (n=394)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.3961 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.254 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7129 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.187 (n=340)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.207 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.5839` → IC=+0.210 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5839 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.229 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0156` → IC=+0.324 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0156 (IC base=+0.272)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.277 (n=1112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` > `0.9024` → IC=+0.346 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9024 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.315 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.299 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.272)

- **PATRÓN** `volumen_regimen` > `0.6815` → IC=+0.288 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6815 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.305 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` < `1.55` → IC=+0.276 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.55 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` > `2.207` → IC=+0.278 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.207 (IC base=+0.272)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `2588.3532` → IC=+0.280 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2588.3532 (IC base=+0.272)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.269 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.295 (n=780)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.286 (n=586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.3945` → IC=+0.305 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3945 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.5488` → IC=+0.286 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5488 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.44` → IC=+0.292 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.44 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `1.2464` → IC=+0.306 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2464 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.243` → IC=+0.365 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.243 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.5387` → IC=+0.264 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5387 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1688` → IC=+0.271 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1688 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `2346.7872` → IC=+0.274 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2346.7872 (IC base=+0.269)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.176 (n=2077)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0048 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.202 (n=2075)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3373` → IC=+0.174 (n=5477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3373 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=6501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5829` → IC=+0.215 (n=6221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5829 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9483` → IC=+0.220 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9483 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.233` → IC=+0.250 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.233 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2136` → IC=+0.163 (n=4137)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2136 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6196` → IC=+0.159 (n=4137)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6196 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1068` → IC=+0.186 (n=2424)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1068 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5664` → IC=+0.174 (n=2603)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5664 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6666` → IC=+0.168 (n=1971)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.6666 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3825.7125` → IC=+0.171 (n=2074)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3825.7125 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.183 (n=5140)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 122.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.187 (n=4033)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0064 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0798` → IC=+0.203 (n=2015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0798 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=2925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4655` → IC=+0.228 (n=6044)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4655 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2226` → IC=+0.162 (n=4512)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2226 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.238` → IC=+0.197 (n=1043)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.238 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1874` → IC=+0.157 (n=4420)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1874 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6237` → IC=+0.151 (n=4420)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6237 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2926` → IC=+0.230 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2926 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.576` → IC=+0.174 (n=2370)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.576 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.175 (n=2441)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.174 (n=5004)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 123.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.225 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.207 (n=353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.3196` → IC=+0.202 (n=1056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3196 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.212 (n=515)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.049` → IC=+0.308 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.049 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.229` → IC=+0.241 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.229 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `2.5472` → IC=+0.180 (n=961)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.5472 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.427` → IC=+0.180 (n=960)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.427 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.206 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.243 (n=670)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.292 (n=507)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=788)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.242 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.274 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.083` → IC=+0.252 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.083 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.234 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.268 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4356` → IC=+0.259 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4356 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6638` → IC=+0.241 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6638 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1741.1448` → IC=+0.261 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1741.1448 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.249 (n=305)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0759` → IC=+0.186 (n=304)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0759 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4289` → IC=+0.223 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4289 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.208 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.226 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2593` → IC=+0.175 (n=911)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.2593 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2311` → IC=+0.187 (n=199)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2311 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.198 (n=293)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10072.2302` → IC=+0.177 (n=911)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 10072.2302 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=1033)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.197 (n=345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.163 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.54` → IC=+0.189 (n=1033)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.54 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1346` → IC=+0.164 (n=1051)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1346 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.029` → IC=+0.216 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.029 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.215` → IC=+0.160 (n=1033)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.215 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.179 (n=319)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4356` → IC=+0.157 (n=922)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4356 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.160 (n=280)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 228.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.207 (n=688)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.1976` → IC=+0.201 (n=687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1976 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.287 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.672` → IC=+0.270 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.672 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.187 (n=851)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.188 (n=395)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.6708` → IC=+0.191 (n=322)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.6708 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `3.6406` → IC=+0.206 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6406 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.238 (n=864)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.223 (n=865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.245 (n=288)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.270 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.3448` → IC=+0.251 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3448 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.273 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.3597` → IC=+0.270 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3597 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.8388` → IC=+0.215 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8388 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `3.5271` → IC=+0.246 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5271 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `1887.4151` → IC=+0.238 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.4151 (IC base=+0.223)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.222 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.223)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.180 (n=861)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.4227` → IC=+0.168 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4227 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.3996` → IC=+0.204 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3996 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.193 (n=636)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.124` → IC=+0.247 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.124 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.858` → IC=+0.161 (n=653)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.858 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `1.1941` → IC=+0.171 (n=326)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1941 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.1724` → IC=+0.158 (n=841)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1724 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.5111` → IC=+0.182 (n=319)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5111 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7103.5858` → IC=+0.190 (n=652)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7103.5858 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.168 (n=610)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 119.0 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.164 (n=1060)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0072 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.3804` → IC=+0.146 (n=1060)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3804 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.181 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6046` → IC=+0.182 (n=1060)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6046 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.15` → IC=+0.145 (n=1064)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.15 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.972` → IC=+0.191 (n=205)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.972 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.143 (n=707)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8585 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.609` → IC=+0.132 (n=1059)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.609 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.201 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.7931` → IC=+0.139 (n=629)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.7931 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.4786` → IC=+0.143 (n=315)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4786 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.161 (n=481)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.128 (n=875)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 177.0 (IC base=+0.131)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.145 (n=770)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0078 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=1187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.196 (n=1168)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0166` → IC=+0.232 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0166 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.474` → IC=+0.257 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.474 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2208` → IC=+0.121 (n=1156)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2208 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4429` → IC=+0.134 (n=370)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4429 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=1191)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2897.8254` → IC=+0.190 (n=524)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2897.8254 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.132 (n=855)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.148 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0059 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.209 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.55 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.188` → IC=+0.136 (n=1072)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.188 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.385` → IC=+0.163 (n=247)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 7.385 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.125 (n=1160)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.1954 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.185 (n=141)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.573` → IC=+0.137 (n=447)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.573 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.177` → IC=+0.133 (n=461)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.177 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3078.551` → IC=+0.163 (n=387)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3078.551 (IC base=+0.114)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0181` → IC=+0.214 (n=729)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0181 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1686` → IC=+0.210 (n=481)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1686 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.206 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.7267` → IC=+0.253 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7267 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `1.2464` → IC=+0.233 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2464 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.349` → IC=+0.241 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.349 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.206 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2068 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6086` → IC=+0.210 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6086 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.263 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1918` → IC=+0.215 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1918 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.202 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2568.8452` → IC=+0.206 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2568.8452 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.235 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.205)

- **PATRÓN** `sigma_h` > `0.0222` → IC=+0.213 (n=532)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0222 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0917` → IC=+0.212 (n=390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0917 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=531)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.243 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `1.1626` → IC=+0.228 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1626 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2669` → IC=+0.205 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2669 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.349` → IC=+0.242 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.349 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6271` → IC=+0.218 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6271 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.287 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.2519` → IC=+0.198 (n=909)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.2519 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `1.4623` → IC=+0.194 (n=1032)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4623 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2540.0452` → IC=+0.215 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2540.0452 (IC base=+0.205)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.149 (n=505)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0038 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.163 (n=505)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0088 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0977` → IC=+0.150 (n=504)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0977 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.3913` → IC=+0.165 (n=1507)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3913 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.8281` → IC=+0.170 (n=207)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.8281 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.692` → IC=+0.167 (n=692)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.692 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.154 (n=867)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8646 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.168 (n=410)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4313` → IC=+0.150 (n=481)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4313 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.5666` → IC=+0.158 (n=481)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5666 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=1676)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8471.0872` → IC=+0.150 (n=684)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8471.0872 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.157 (n=1285)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 156.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.134 (n=1067)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.129 (n=1408)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=1624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.4882` → IC=+0.156 (n=1409)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4882 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2044` → IC=+0.121 (n=1422)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.2044 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.998` → IC=+0.138 (n=468)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 5.998 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.2231` → IC=+0.121 (n=1419)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2231 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.1668` → IC=+0.142 (n=409)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1668 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `2.2348` → IC=+0.137 (n=1347)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2348 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.128 (n=637)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 25.0 (IC base=+0.115)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.141 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.144 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 10.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.8691` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8691 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.5278` → IC=+0.139 (n=70)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.5278 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.256` → IC=+0.148 (n=160)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.256 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `0.6933` → IC=+0.154 (n=151)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6933 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `10126.7179` → IC=+0.126 (n=343)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 10126.7179 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 151.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.207 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.148 (n=490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.3419` → IC=+0.199 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3419 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.137 (n=199)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.142` → IC=+0.127 (n=555)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 9.142 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.128 (n=490)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2044 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.0616` → IC=+0.167 (n=223)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0616 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.205 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.4163` → IC=+0.150 (n=481)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4163 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 159.0 (IC base=+0.126)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.257 (n=200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.195 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0067 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.221 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.244 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `0.3797` → IC=+0.233 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3797 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.3651` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3651 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.085` → IC=+0.230 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.085 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` < `0.8293` → IC=+0.202 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8293 (IC base=+0.190)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.221 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2472` → IC=+0.321 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2472 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `1.3745` → IC=+0.217 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3745 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.3885` → IC=+0.262 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3885 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `12322.191` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12322.191 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.128 (n=409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0067 (IC base=+0.106)

- **PATRÓN** `drift_60min` |x|≤ `0.0974` → IC=+0.155 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0974 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.136 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.3025` → IC=+0.162 (n=273)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3025 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.5939` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.5939 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.407` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.407 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.6874` → IC=+0.132 (n=180)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6874 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.1661` → IC=+0.173 (n=96)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1661 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.8175` → IC=+0.132 (n=259)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.8175 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.5944` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5944
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=411)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.203 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.7807` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7807 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.173 (n=148)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `3048.5576` → IC=+0.194 (n=109)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3048.5576 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.133 (n=107)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 21.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.4783` → IC=+0.153 (n=321)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.4783 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.278` → IC=+0.145 (n=108)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 5.278 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` < `0.7097` → IC=+0.157 (n=141)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7097 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` < `0.1024` → IC=+0.122 (n=300)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1024 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `2.5969` → IC=+0.136 (n=297)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.5969 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2922.5748` → IC=+0.135 (n=146)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2922.5748 (IC base=+0.087)

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
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.195 (n=3574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0087 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=8247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.4727` → IC=+0.214 (n=7873)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4727 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.9012` → IC=+0.201 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9012 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.589` → IC=+0.223 (n=3856)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.589 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8829` → IC=+0.167 (n=3529)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8829 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.189 (n=1488)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6367` → IC=+0.184 (n=2502)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6367 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3810.3548` → IC=+0.170 (n=2625)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3810.3548 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.194 (n=5728)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 93.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.196 (n=4825)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0067 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.481` → IC=+0.183 (n=7237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.481 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.238 (n=7244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2336` → IC=+0.162 (n=4605)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2336 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.848` → IC=+0.198 (n=1040)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.848 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.695` → IC=+0.182 (n=6994)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.695 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.159 (n=2206)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7031 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.2046` → IC=+0.157 (n=1669)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.2046 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.249 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.3006` → IC=+0.189 (n=2948)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.3006 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.178 (n=6112)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 124.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.209 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.231 (n=603)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.206 (n=888)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.319 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.387` → IC=+0.343 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.387 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.242 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `1.8639` → IC=+0.191 (n=827)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.8639 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.264 (n=694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.265 (n=1035)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.2035` → IC=+0.282 (n=690)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2035 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.3409` → IC=+0.286 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3409 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.438` → IC=+0.264 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.438 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.300 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6807` → IC=+0.295 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6807 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1592.8005` → IC=+0.271 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.8005 (IC base=+0.256)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.194 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1837` → IC=+0.156 (n=835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1837 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3255` → IC=+0.199 (n=1252)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3255 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1264` → IC=+0.186 (n=692)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1264 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.774` → IC=+0.163 (n=292)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.774 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.34` → IC=+0.153 (n=1115)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.34 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6939` → IC=+0.183 (n=551)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6939 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.180 (n=342)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.3949` → IC=+0.157 (n=1198)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.3949 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7544` → IC=+0.157 (n=799)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7544 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `10866.0786` → IC=+0.166 (n=1119)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 10866.0786 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `491.0` → IC=+0.162 (n=1130)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 491.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=1118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.263` → IC=+0.166 (n=984)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.263 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.171 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.6377` → IC=+0.204 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6377 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.6982` → IC=+0.161 (n=169)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6982 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.163 (n=1034)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.22` → IC=+0.165 (n=556)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.22 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.161 (n=1118)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2004 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.208 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.409` → IC=+0.166 (n=1021)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.409 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `370.0` → IC=+0.164 (n=617)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 370.0 (IC base=+0.152)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.226 (n=1251)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=1251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.215 (n=1264)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.6721` → IC=+0.249 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6721 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.59` → IC=+0.299 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.59 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.2176` → IC=+0.216 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2176 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.9939` → IC=+0.235 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9939 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.236 (n=1197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.233 (n=545)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.1545` → IC=+0.232 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1545 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.3648` → IC=+0.266 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3648 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.713` → IC=+0.273 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.713 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3595` → IC=+0.294 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3595 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.7962` → IC=+0.224 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7962 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.2501` → IC=+0.232 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2501 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `1891.5784` → IC=+0.236 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1891.5784 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.258 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.231)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.173 (n=588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0039 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.140 (n=1333)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=1400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.7029` → IC=+0.232 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7029 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.353` → IC=+0.178 (n=492)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.353 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.224` → IC=+0.163 (n=564)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.224 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.160 (n=889)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8799 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.232 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5053` → IC=+0.149 (n=565)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5053 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.4628` → IC=+0.158 (n=428)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4628 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8808.1502` → IC=+0.230 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8808.1502 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.171 (n=408)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 87.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.158 (n=1079)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0076 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4405` → IC=+0.158 (n=1078)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4405 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.151 (n=483)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6884` → IC=+0.193 (n=1078)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6884 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.2051` → IC=+0.144 (n=1015)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2051 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.037` → IC=+0.201 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.037 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6938` → IC=+0.146 (n=475)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6938 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.1867` → IC=+0.146 (n=360)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1867 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.269 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.4649` → IC=+0.169 (n=336)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4649 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `10953.5869` → IC=+0.199 (n=360)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 10953.5869 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `192.0` → IC=+0.145 (n=1003)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 192.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4694` → IC=+0.182 (n=1347)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.4694 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0085` → IC=+0.192 (n=232)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 1.0085 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.403` → IC=+0.222 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.403 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=936)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2917.745` → IC=+0.243 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2917.745 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.127 (n=1006)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 53.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.171 (n=436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0055 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1263` → IC=+0.155 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1263 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.147 (n=619)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.208 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.4694` → IC=+0.130 (n=1290)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.4694 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.449` → IC=+0.126 (n=1260)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.449 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.153 (n=577)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.72 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2215` → IC=+0.170 (n=204)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2215 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4615` → IC=+0.150 (n=384)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4615 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.5681` → IC=+0.122 (n=384)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 2.5681 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2903.4398` → IC=+0.164 (n=436)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2903.4398 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0241` → IC=+0.213 (n=619)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0241 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.5116` → IC=+0.243 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5116 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.1869` → IC=+0.233 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1869 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.35` → IC=+0.247 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.35 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2478` → IC=+0.209 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2478 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.208 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.0802` → IC=+0.229 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0802 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.5793` → IC=+0.240 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5793 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2573.072` → IC=+0.212 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2573.072 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.237 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.227 (n=503)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.254 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.2698` → IC=+0.206 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2698 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.724` → IC=+0.263 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.724 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.238 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.256 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2324` → IC=+0.193 (n=1165)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2324 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4453` → IC=+0.198 (n=1324)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4453 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2546.9804` → IC=+0.202 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2546.9804 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=2583)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.156 (n=2227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0094 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5272` → IC=+0.156 (n=2531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5272 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.161 (n=879)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9387` → IC=+0.215 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9387 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1884` → IC=+0.157 (n=825)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1884 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.736` → IC=+0.169 (n=816)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.736 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.9082` → IC=+0.152 (n=1027)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9082 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1738` → IC=+0.174 (n=692)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1738 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4626` → IC=+0.162 (n=835)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4626 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.9083` → IC=+0.158 (n=1669)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9083 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8205.7154` → IC=+0.154 (n=1148)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8205.7154 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.188 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4875` → IC=+0.154 (n=1949)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4875 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.163 (n=650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 4.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.162 (n=858)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1814 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.7057` → IC=+0.144 (n=346)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.7057 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.306` → IC=+0.144 (n=1932)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.306 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1144` → IC=+0.144 (n=1628)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1144 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.151 (n=919)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.5724` → IC=+0.140 (n=1930)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5724 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.8264` → IC=+0.146 (n=1286)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8264 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=2583)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7675.5901` → IC=+0.151 (n=1741)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7675.5901 (IC base=+0.135)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.171 (n=281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0034 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.0921` → IC=+0.192 (n=105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0921 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.165 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.5413` → IC=+0.198 (n=210)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5413 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.2308` → IC=+0.183 (n=143)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2308 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.25` → IC=+0.167 (n=397)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 8.25 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.2448` → IC=+0.161 (n=314)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2448 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.8276` → IC=+0.197 (n=209)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.8276 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2313` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2313 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.210 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.7581` → IC=+0.201 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7581 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `12617.0993` → IC=+0.207 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12617.0993 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.206 (n=386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.147 (n=870)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1546` → IC=+0.165 (n=383)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1546 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6117` → IC=+0.145 (n=395)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6117 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.723` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.723 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2277` → IC=+0.135 (n=897)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2277 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.265` → IC=+0.158 (n=849)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.265 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.179 (n=580)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8812 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.163 (n=413)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.5735` → IC=+0.143 (n=867)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.5735 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.147 (n=578)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `11358.9394` → IC=+0.150 (n=870)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11358.9394 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `707.0` → IC=+0.138 (n=824)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 707.0 (IC base=+0.135)

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
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.153 (n=750)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0088 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.150 (n=750)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0045 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5046` → IC=+0.156 (n=750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5046 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.153 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.1834` → IC=+0.157 (n=752)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.1834 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.9678` → IC=+0.175 (n=164)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.9678 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.424` → IC=+0.154 (n=714)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.424 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.676` → IC=+0.153 (n=748)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.676 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.116` → IC=+0.148 (n=660)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.116 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `1.2702` → IC=+0.155 (n=250)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2702 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1777` → IC=+0.161 (n=222)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1777 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.169 (n=246)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=712)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8788.5542` → IC=+0.152 (n=670)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8788.5542 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.162 (n=542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0071 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.512` → IC=+0.180 (n=616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.512 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=429)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.160 (n=615)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.1001 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1574` → IC=+0.173 (n=276)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1574 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.4005` → IC=+0.147 (n=633)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.4005 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.921` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 10.921 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6472` → IC=+0.173 (n=206)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6472 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.7274` → IC=+0.154 (n=550)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7274 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.175 (n=263)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.162 (n=533)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.4522` → IC=+0.162 (n=604)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4522 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `8176.6816` → IC=+0.171 (n=615)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8176.6816 (IC base=+0.147)

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

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.135 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0113 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `0.6223` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6223 (IC base=+0.037)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.255 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=289)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=289)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.212 (n=297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.170 (n=231)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.6481` → IC=+0.219 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6481 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1307` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1307 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.09` → IC=+0.219 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.09 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.0933` → IC=+0.127 (n=580)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0933 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.207 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.468` → IC=+0.160 (n=472)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.468 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=470)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.158 (n=252)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.0688` → IC=+0.292 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0688 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` < `0.1599` → IC=+0.123 (n=226)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1599 (IC base=-0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.981` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.981 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.0857` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0857 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.6098` → IC=+0.154 (n=154)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.6098 (IC base=-0.022)

- **PATRÓN** `libro_liquidez` > `2977.6678` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2977.6678 (IC base=-0.022)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5881` → IC=-0.176 (n=66)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5881
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=199)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.177 (n=230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.006 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.5881` → IC=+0.211 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5881 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.535` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 13.535 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `1.0413` → IC=+0.138 (n=175)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0413 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.160 (n=142)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.2582` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2582 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.201 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=204)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2859.3011` → IC=+0.128 (n=186)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2859.3011 (IC base=+0.107)

- **PATRÓN** `drift_60min` |x|≤ `0.0426` → IC=+0.250 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0426 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.5693` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5693 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.87` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 4.87 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.9523` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.9523 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.0764` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0764 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `2.4035` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4035 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `3253.1204` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3253.1204 (IC base=+0.054)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.306 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=90)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.222 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=67)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.177 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.005 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.149 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.649` → IC=+0.249 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.649 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.1208` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1208 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.057` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.057 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.791 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6219 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.3845` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.3845 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=211)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1103.6894` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 1103.6894 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1021` → IC=+0.158 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1021 (IC base=-0.062)

- **PATRÓN** `ibs_20min` < `0.2452` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2452 (IC base=-0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.303` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.303 (IC base=-0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=-0.062)

- **PATRÓN** `volumen_spike_ratio` > `2.7298` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7298 (IC base=-0.062)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=81)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=93)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.080)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.200 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6757 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.8626` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.8626 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.0632` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0632 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `2.5485` → IC=+0.154 (n=160)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5485 (IC base=+0.080)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.143 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.006 (IC base=-0.074)

- **PATRÓN** `ibs_20min` < `0.1154` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1154 (IC base=-0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.012` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.012 (IC base=-0.074)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1406` → IC=-0.354 (n=39)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1406
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=124)

- **FILTRO** `dist_vwap_pct` > `0.2306` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2306
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=143)

- **FILTRO** `volumen_spike_ratio` > `1.4324` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=37)

- **FILTRO** `sigma_ewma_delta_pct` > `2.588` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.588
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=32)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=40)

- **FILTRO** `dist_vwap_pct` > `0.2409` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2409
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=42)

- **FILTRO** `sigma_ewma_delta_pct` > `3.572` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.572
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=35)

- **FILTRO** `volumen_regimen` > `0.8664` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8664
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7738` → IC=-0.447 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7738
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=33)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

- **FILTRO** `dist_vwap_pct` > `0.1871` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.326 (n=21)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.158 (n=77)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=234)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.155 (n=195)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.75 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2345` → IC=+0.130 (n=206)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2345 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.126` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.126 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `3925.9695` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3925.9695 (IC base=+0.043)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=81)

- **FILTRO** `ibs_20min` < `0.5548` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5548
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=73)

- **FILTRO** `volumen_regimen` < `0.7777` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7777
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=73)

- **FILTRO** `volumen_spike_ratio` < `1.4652` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4652
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=52)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.180 (n=95)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1435 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.154 (n=108)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.100)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=59)

- **FILTRO** `ibs_20min` < `0.8327` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8327
  - _Potencial_: sin este filtro IC_bueno=+0.185 (n=52)

- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=75)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.156 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0042 (IC base=+0.070)

- **PATRÓN** `drift_60min` |x|≤ `0.2768` → IC=+0.133 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.2768 (IC base=+0.070)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.8327` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.8327 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.1989` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1989 (IC base=+0.070)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `1558.1749` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1558.1749 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.015)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.55` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=53)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.171 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0063 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.167 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0058 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.159 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 17.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.7273` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.7273 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.7895` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.7895 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.6339` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6339 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.2073` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2073 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.5494` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5494 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.03 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.0984` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0984 (IC base=-0.035)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=487)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2833.8509` → IC=+0.163 (n=170)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2833.8509 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2310.1197` → IC=+0.126 (n=557)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2310.1197 (IC base=+0.100)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=487)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2833.8509` → IC=+0.163 (n=170)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2833.8509 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2310.1197` → IC=+0.126 (n=557)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2310.1197 (IC base=+0.100)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=124)

- **FILTRO** `libro_liquidez` < `2415.4574` → IC=-0.284 (n=35)

  - _Acción_: SKIP cuando `libro_liquidez` < 2415.4574
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=105)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=191)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=177)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1344)

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
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=91)

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

- **PATRÓN** `liq_usd_total` > `59480.98` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `liq_usd_total` > 59480.98 (IC base=+0.025)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.495 (IC base=+0.025)

- **PATRÓN** `libro_liquidez` > `16814.9132` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 16814.9132 (IC base=+0.025)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=584)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=76)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=424)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=264)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=264)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.200 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=231)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=160)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=160)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=97)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=60)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=74)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=163)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=63)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=97)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=1063)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5524)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=6455)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1055)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1385)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.179 (n=2715)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=8244)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.171 (n=2809)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=8621)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.216 (n=463)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1391)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.167 (n=472)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1566)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.120 (n=1102)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.5 (IC base=+0.018)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.203 (n=463)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=1438)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.217 (n=482)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1533)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.165 (n=500)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=1515)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.201 (n=449)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1377)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.193 (n=500)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1514)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2437)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=2478)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2484)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=300)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=188)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=167)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=633)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=7803)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=17902)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.283 (n=6030)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=19675)

- **FILTRO** `ibs_7min` < `0.703` → IC=-0.242 (n=6423)

  - _Acción_: SKIP cuando `ibs_7min` < 0.703
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=19282)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.159 (n=8739)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=16966)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.224 (n=8023)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=24181)

- **FILTRO** `ibs_7min` > `0.2963` → IC=-0.177 (n=8037)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2963
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=24167)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=978)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3169)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.256 (n=1368)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2779)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.195 (n=969)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3178)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.150 (n=3748)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1845)

- **FILTRO** `drift_7min_pct` |x|> `0.137` → IC=-0.134 (n=1396)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.137
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=4197)

- **FILTRO** `ibs_7min` > `0.7992` → IC=-0.206 (n=1398)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7992
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4195)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1028)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=3461)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.257 (n=1051)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3438)

- **FILTRO** `ibs_7min` < `0.7555` → IC=-0.187 (n=1121)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7555
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3368)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.174 (n=1120)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3369)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.256 (n=1074)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3472)

- **FILTRO** `ibs_7min` > `0.2539` → IC=-0.168 (n=1136)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2539
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3410)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=1134)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3412)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.181 (n=940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=2937)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.320 (n=933)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2944)

- **FILTRO** `drift_7min_pct` |x|> `0.181` → IC=-0.132 (n=1317)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.181
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=2560)

- **FILTRO** `ibs_7min` < `0.2031` → IC=-0.275 (n=969)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2031
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=2908)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.221 (n=911)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=2966)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.234 (n=1387)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=4511)

- **FILTRO** `ibs_7min` > `0.2611` → IC=-0.154 (n=2005)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2611
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3893)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=1331)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=2902)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1034)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3199)

- **FILTRO** `ibs_7min` < `0.7433` → IC=-0.191 (n=1058)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7433
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3175)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.183 (n=1045)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3188)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1069)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3257)

- **FILTRO** `ibs_7min` > `0.2739` → IC=-0.175 (n=1080)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2739
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3246)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.182 (n=1068)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3258)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.256 (n=1107)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3516)

- **FILTRO** `ibs_7min` < `0.7187` → IC=-0.220 (n=1155)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7187
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3468)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.170 (n=1472)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=4627)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.283 (n=1058)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3278)

- **FILTRO** `ibs_7min` < `0.7261` → IC=-0.233 (n=1084)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7261
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3252)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.211 (n=1059)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3277)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.207 (n=1357)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=4385)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=964)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=482)

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
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=531)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.136 (n=640)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.140 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.153 (n=214)

  - _Acción_: Kelly boost +0.76€ cuando `total_vol_5m` < 469.512 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.121 (n=291)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3728.089 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.135 (n=272)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 27.0 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.147 (n=49)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.136)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.102)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `total_vol_5m` < `390.3055` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.3055 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 70.0 (IC base=+0.098)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.190 (n=114)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.149)

- **PATRÓN** `total_vol_5m` < `7671.127` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 7671.127 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3218.4716` → IC=+0.164 (n=102)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3218.4716 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 37.0 (IC base=+0.149)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.158 (n=109)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.145 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 13.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `353208.2` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 353208.2 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.230 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.116)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.322 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=147)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.167 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0039 (IC base=-0.125)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.351 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=46)

- **FILTRO** `T_h` > `54.5986` → IC=-0.372 (n=45)

  - _Acción_: SKIP cuando `T_h` > 54.5986
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=46)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.124)

- **PATRÓN** `T_h` < `54.5986` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `T_h` < 54.5986 (IC base=-0.124)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.150 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.236 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=75)

- **FILTRO** `T_h` > `71.8388` → IC=-0.195 (n=224)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=76)

- **FILTRO** `pct_vs_K` |x|> `4.4208` → IC=-0.452 (n=60)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.4208
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=183)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=73)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=65)

- **FILTRO** `pct_vs_K` |x|> `3.0033` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0033
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=59)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.309 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=41)

- **FILTRO** `sigma_h` > `0.01` → IC=-0.262 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=64)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.364 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=63)

- **FILTRO** `T_h` > `63.9668` → IC=-0.328 (n=62)

  - _Acción_: SKIP cuando `T_h` > 63.9668
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0126` → IC=-0.167 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0126
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.271 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

- **FILTRO** `T_h` > `71.8388` → IC=-0.173 (n=50)

  - _Acción_: SKIP cuando `T_h` > 71.8388
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.339 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `T_h` > `87.8036` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `T_h` > 87.8036
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.15` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.15 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.467 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.366)

- **PATRÓN** `T_h` > `0.8774` → IC=+0.467 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8774 (IC base=+0.366)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.468 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.366)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.462 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.366)

- **PATRÓN** `edge` > `0.1015` → IC=+0.452 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1015 (IC base=+0.404)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.465 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.404)

- **PATRÓN** `T_h` > `0.8072` → IC=+0.421 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8072 (IC base=+0.404)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.487 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.436 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.404)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.475)

- **PATRÓN** `edge` > `0.2135` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2135 (IC base=+0.477)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.474 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.477)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.464 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.477)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.477)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.480 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.477)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.463 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.477)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.469 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.477)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=130)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=227)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `streak_estiramiento` < 0.4576 (IC base=+0.024)

- **PATRÓN** `streak_estiramiento` < `0.5597` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.5597 (IC base=+0.036)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

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
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=558)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=564)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=307)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `streak_len` < 4.0 (IC base=+0.029)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=469)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=945)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=558)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=581)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2374)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1220)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1228)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.185 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.004 (IC base=+0.175)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.212 (n=369)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.077` → IC=+0.179 (n=487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.077 (IC base=+0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0587` → IC=+0.177 (n=1105)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0587 (IC base=+0.175)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1354` → IC=+0.227 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1354 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.180 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 11.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.175)

- **PATRÓN** `ibs_15` > `0.6216` → IC=+0.246 (n=1105)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6216 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.1478` → IC=+0.171 (n=542)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1478 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` < `0.1053` → IC=+0.177 (n=735)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1053 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.863` → IC=+0.249 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.863 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2633.3465` → IC=+0.179 (n=987)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2633.3465 (IC base=+0.175)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=378)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.214 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.205 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.271 (n=94)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.195)

- **PATRÓN** `drift_15min` |x|≤ `0.3766` → IC=+0.208 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3766 (IC base=+0.195)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.205 (n=93)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1506` → IC=+0.253 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1506 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `ibs_15` > `0.7112` → IC=+0.251 (n=279)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7112 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.197 (n=196)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.624` → IC=+0.255 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.624 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `14070.628` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14070.628 (IC base=+0.195)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `20.351` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 20.351 (IC base=-0.004)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.174 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.145 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0038 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.145 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.169 (n=179)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2725` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2725 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.161 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.6489` → IC=+0.231 (n=269)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6489 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.4114` → IC=+0.154 (n=284)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4114 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.212 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `11704.6865` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11704.6865 (IC base=+0.142)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `4.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=64)

- **FILTRO** `ibs_15` > `0.1909` → IC=-0.224 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1909
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=53)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.6` → IC=-0.160 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=154)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.204 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.1727` → IC=+0.167 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1727 (IC base=+0.142)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.186 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3347` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3347 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.178 (n=116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.244 (n=154)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.5519` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.5519 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=127)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `3004.2322` → IC=+0.264 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.2322 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 34.0 (IC base=+0.142)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5742` → IC=-0.147 (n=117)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5742
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=609)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.252 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.198 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.183)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0648` → IC=+0.194 (n=279)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.0648 (IC base=+0.183)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.183)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.274 (n=312)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.1729` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1729 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.496` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.496 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.183 (n=339)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.03 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2813.2668` → IC=+0.245 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2813.2668 (IC base=+0.183)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.176 (n=353)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` < 0.1111 (IC base=+0.048)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.336 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.370 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.340 (n=280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.346 (n=212)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2203` → IC=+0.374 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2203 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.375 (n=318)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.4117` → IC=+0.375 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4117 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.335 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.729` → IC=+0.333 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.729 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.340 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3480.6224` → IC=+0.347 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3480.6224 (IC base=+0.333)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1225` → IC=+0.340 (n=79)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1225 (IC base=+0.333)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.330 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.355 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.343 (n=157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.343 (n=119)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.412 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.346 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.367 (n=178)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.341 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `9173.8264` → IC=+0.343 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9173.8264 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `475.0` → IC=+0.399 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 475.0 (IC base=+0.333)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.364 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.330)

- **PATRÓN** `drift_60min` |x|≤ `0.151` → IC=+0.332 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.151 (IC base=+0.330)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.338 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.330)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2352` → IC=+0.357 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2352 (IC base=+0.330)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.330)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.387 (n=140)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` > `0.4241` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4241 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` < `0.0995` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0995 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.328 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.330)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `3566.5529` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3566.5529 (IC base=+0.330)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0125` → IC=-0.203 (n=541)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0125
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1625)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.176 (n=686)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1480)

- **FILTRO** `libro_liquidez` < `3781.8456` → IC=-0.121 (n=1429)

  - _Acción_: SKIP cuando `libro_liquidez` < 3781.8456
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=737)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.244 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.058)

- **PATRÓN** `ibs_15` > `0.6098` → IC=+0.251 (n=544)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6098 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` < `0.2658` → IC=+0.177 (n=431)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2658 (IC base=-0.058)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2098` → IC=+0.238 (n=388)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2098 (IC base=-0.044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1821` → IC=+0.240 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1821 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.356` → IC=+0.280 (n=1164)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.356 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.6604` → IC=+0.268 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6604 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.208 (n=327)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=982)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.228 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=878)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.207 (n=837)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=472)

- **FILTRO** `sigma_ewma_delta_pct` > `19.843` → IC=-0.240 (n=233)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.843
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1076)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.172 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0026 (IC base=+0.071)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1422` → IC=+0.311 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1422 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.332 (n=111)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1073` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1073 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.34` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.34 (IC base=+0.071)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6537` → IC=-0.222 (n=88)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6537
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=265)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=336)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.137 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0065 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.161 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.004 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.214 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.134)

- **PATRÓN** `drift_15min` |x|≤ `0.4625` → IC=+0.147 (n=117)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.4625 (IC base=+0.134)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.236 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.253 (n=265)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.822` → IC=+0.143 (n=284)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 18.822 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=336)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `10544.7398` → IC=+0.191 (n=121)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10544.7398 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.248 (n=491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.4368` → IC=+0.228 (n=491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4368 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.230 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.226)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2` → IC=+0.260 (n=223)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.227 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.226)

- **PATRÓN** `ibs_15` < `0.3657` → IC=+0.269 (n=491)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3657 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.3809` → IC=+0.248 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3809 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.263` → IC=+0.231 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.263 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.221` → IC=+0.230 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.221 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3591.8273` → IC=+0.228 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3591.8273 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.226 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.226)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.8494` → IC=-0.235 (n=130)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8494
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=392)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.211 (n=195)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=327)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.151)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0717` → IC=+0.214 (n=211)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0717 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.249 (n=237)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.207 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0192` → IC=-0.257 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0192
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=325)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=474)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1088` → IC=+0.352 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1088 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3391` → IC=+0.308 (n=341)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3391 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` > `1.111` → IC=+0.421 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.111 (IC base=-0.045)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.136 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0064 (IC base=+0.098)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.239 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.098)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.098)

- **PATRÓN** `ibs_15` > `0.269` → IC=+0.143 (n=40)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.71€ cuando `ibs_15` > 0.269 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1495` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1495 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.309` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.309 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.098)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.136 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0064 (IC base=+0.098)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.239 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.098)

- **PATRÓN** `drift_15min` |x|≤ `0.5874` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `drift_15min` |x|≤ 0.5874 (IC base=+0.098)

- **PATRÓN** `ibs_15` > `0.269` → IC=+0.143 (n=40)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.71€ cuando `ibs_15` > 0.269 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1495` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1495 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.309` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.309 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `13354.4495` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13354.4495 (IC base=+0.098)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.287 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0567` → IC=+0.313 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0567 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1415` → IC=+0.289 (n=358)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1415 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.319 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.324 (n=537)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.326 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.316 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.288 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `12693.7099` → IC=+0.301 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12693.7099 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.293 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.284 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.314 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.276)

- **PATRÓN** `drift_15min` |x|≤ `0.3849` → IC=+0.284 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3849 (IC base=+0.276)

- **PATRÓN** `delta_ratio_macro` |x|> `0.246` → IC=+0.284 (n=100)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.246 (IC base=+0.276)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3724` → IC=+0.291 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3724 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.329 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` > `0.8213` → IC=+0.295 (n=300)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8213 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.340 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.336 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `15613.0471` → IC=+0.314 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15613.0471 (IC base=+0.276)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.312 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.304 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.317 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1458` → IC=+0.307 (n=159)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1458 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.341 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.323 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.342 (n=238)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2755` → IC=+0.307 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2755 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.619` → IC=+0.319 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.619 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `154.0` → IC=+0.298 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 154.0 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.085` → IC=-0.273 (n=64)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.085
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=193)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.253 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=170)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1851` → IC=-0.127 (n=73)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1851
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=73)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2412` → IC=-0.138 (n=67)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2412
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=69)

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
- **PATRÓN** `T_h` > `87.9936` → IC=+0.140 (n=198)

  - _Acción_: Kelly boost +0.70€ cuando `T_h` > 87.9936 (IC base=+0.133)

- **PATRÓN** `ratio` < `0.9771` → IC=+0.464 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9771 (IC base=+0.133)

- **PATRÓN** `T_h` > `145.8408` → IC=+0.408 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8408 (IC base=+0.349)

- **PATRÓN** `ratio` > `1.0115` → IC=+0.381 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0115 (IC base=+0.349)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.091)

- **PATRÓN** `T_h` > `87.996` → IC=+0.309 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.996 (IC base=+0.305)

- **PATRÓN** `ratio` > `1.0413` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0413 (IC base=+0.305)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `145.6143` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.6143 (IC base=+0.190)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.392 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.190)

- **PATRÓN** `T_h` > `88.9194` → IC=+0.348 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 88.9194 (IC base=+0.330)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.378 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.330)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1118` → IC=+0.454 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.405)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6216 sube el IC de +0.175 a +0.246 en UPDOWN_GBM#15min (n=1105). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7112 sube el IC de +0.195 a +0.251 en UPDOWN_GBM#BTC#15min (n=279). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6489 sube el IC de +0.142 a +0.231 en UPDOWN_GBM#ETH#15min (n=269). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.142 a +0.244 en UPDOWN_GBM#SOL#15min (n=154). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.183 a +0.274 en UPDOWN_GBM#XRP#15min (n=312). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.048 a +0.176 en UPDOWN_GBM#XRP#15min (n=353). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6098 sube el IC de -0.058 a +0.251 en UPDOWN_GBM_15M_TARDIO (n=544). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.356 sube el IC de -0.044 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1164). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.071 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=111). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.134 a +0.253 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=265). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3657 sube el IC de +0.226 a +0.269 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=491). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.151 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.042 a +0.249 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=237). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.045 a +0.308 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=341). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.285 a +0.324 en UPDOWN_GBM_IBS_ALTO (n=537). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8213 sube el IC de +0.276 a +0.295 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=300). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.296 a +0.342 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=238). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.333 a +0.375 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=318). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.333 a +0.367 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=178). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.330 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=140). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1163 | +0.084 | +141.54€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1163 | +0.084 | +141.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 842 | +0.091 | +119.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 842 | +0.091 | +119.69€ | 3 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 241 | +0.043 | +3.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 241 | +0.043 | +3.10€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 54 | +0.161 | +20.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 54 | +0.161 | +20.25€ | 0 | 5 |
| ✅ BALLENAS_TARDIAS | 20936 | -0.100 | -3048.22€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1256 | -0.046 | -182.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 19680 | -0.103 | -2865.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3220 | -0.111 | -559.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3220 | -0.111 | -559.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1256 | -0.046 | -182.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1256 | -0.046 | -182.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6004 | -0.043 | -589.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6004 | -0.043 | -589.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5571 | -0.107 | -475.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5571 | -0.107 | -475.44€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4511 | -0.169 | -1079.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4511 | -0.169 | -1079.74€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 12751 | -0.040 | +4226.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3418 | -0.006 | +1844.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 9333 | -0.053 | +2382.32€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 12751 | -0.040 | +4226.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3418 | -0.006 | +1844.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 9333 | -0.053 | +2382.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1079 | -0.107 | -159.60€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 77 | -0.095 | -16.65€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1002 | -0.108 | -142.95€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 617 | -0.088 | -76.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 53 | -0.100 | -11.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 564 | -0.087 | -65.15€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 300 | -0.149 | -65.20€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 276 | -0.155 | -59.97€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 101 | -0.073 | -17.69€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 101 | -0.073 | -17.69€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 75994 | +0.113 | -3911.82€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 11830 | +0.183 | -366.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 294 | -0.115 | -42.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 58654 | +0.100 | -3386.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5216 | +0.115 | -115.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 9773 | +0.097 | -906.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 39 | -0.159 | -2.72€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 9719 | +0.098 | -891.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 15358 | +0.131 | -324.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3628 | +0.201 | -118.58€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 9716 | +0.109 | -193.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1972 | +0.115 | +10.24€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 9812 | +0.089 | -953.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 46 | -0.062 | -2.24€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 9751 | +0.090 | -940.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 16260 | +0.125 | -300.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4566 | +0.172 | -73.33€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 9806 | +0.108 | -173.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1876 | +0.100 | -45.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 15003 | +0.116 | -856.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3511 | +0.186 | -180.62€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 197 | -0.073 | +11.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 9927 | +0.091 | -606.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1368 | +0.137 | -80.22€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 9788 | +0.103 | -570.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 40 | +0.000 | +10.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 9735 | +0.104 | -581.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 12014 | +0.190 | -819.09€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 12014 | +0.190 | -819.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2946 | +0.168 | -318.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2946 | +0.168 | -318.82€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 681 | +0.187 | +7.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 681 | +0.187 | +7.58€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2885 | +0.178 | -264.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2885 | +0.178 | -264.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2594 | +0.237 | -78.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2594 | +0.237 | -78.58€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2829 | +0.191 | -178.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2829 | +0.191 | -178.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 552 | +0.431 | -12.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 552 | +0.431 | -12.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 211 | +0.434 | -3.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 211 | +0.434 | -3.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 210 | +0.439 | -0.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 210 | +0.439 | -0.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 123 | +0.404 | -8.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 123 | +0.404 | -8.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 41080 | +0.195 | -3415.85€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 41080 | +0.195 | -3415.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 7154 | +0.171 | -897.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 7154 | +0.171 | -897.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6523 | +0.224 | -239.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6523 | +0.224 | -239.28€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7116 | +0.169 | -904.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7116 | +0.169 | -904.92€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6618 | +0.217 | -276.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6618 | +0.217 | -276.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6773 | +0.203 | -458.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6773 | +0.203 | -458.72€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6896 | +0.191 | -639.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6896 | +0.191 | -639.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 15365 | +0.124 | +294.34€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 15365 | +0.124 | +294.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7621 | +0.129 | +202.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7621 | +0.129 | +202.95€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7744 | +0.120 | +91.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7744 | +0.120 | +91.39€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1257 | +0.287 | -25.35€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1257 | +0.287 | -25.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 556 | +0.272 | -20.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 556 | +0.272 | -20.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 601 | +0.291 | -3.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 601 | +0.291 | -3.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 100 | +0.333 | -0.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 100 | +0.333 | -0.80€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 551 | +0.431 | -7.21€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 551 | +0.431 | -7.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 258 | +0.431 | -3.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 258 | +0.431 | -3.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 254 | +0.434 | -3.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 254 | +0.434 | -3.14€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 39 | +0.378 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 39 | +0.378 | -0.28€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 878 | +0.068 | -46.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 315 | +0.055 | -27.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 563 | +0.075 | -18.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 683 | +0.077 | -22.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 120 | +0.082 | -3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 563 | +0.075 | -18.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 140 | +0.000 | -28.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 140 | +0.000 | -28.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 27283 | +0.098 | -836.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2292 | +0.093 | +30.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 24991 | +0.099 | -866.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 15533 | +0.102 | -233.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2292 | +0.093 | +30.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 13241 | +0.104 | -263.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4790 | +0.114 | +28.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4790 | +0.114 | +28.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6960 | +0.077 | -631.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6960 | +0.077 | -631.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 729 | +0.247 | -91.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 729 | +0.247 | -91.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 729 | +0.247 | -91.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 729 | +0.247 | -91.87€ | 0 | 4 |
| ✅ GBM_LATE_15M | 20107 | +0.075 | +9026.88€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 20107 | +0.075 | +9026.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3299 | +0.194 | +2403.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3299 | +0.194 | +2403.51€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 2968 | +0.173 | +1969.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2968 | +0.173 | +1969.62€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 3440 | +0.195 | +2514.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3440 | +0.195 | +2514.43€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 2999 | +0.005 | +465.39€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2999 | +0.005 | +465.39€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 2958 | -0.037 | +635.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2958 | -0.037 | +635.66€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 4443 | -0.050 | +1038.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4443 | -0.050 | +1038.26€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 21197 | +0.077 | +10515.71€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 21197 | +0.077 | +10515.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3895 | +0.010 | +1947.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3895 | +0.010 | +1947.54€ | 2 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4473 | +0.006 | +844.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4473 | +0.006 | +844.64€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3003 | +0.255 | +2940.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3003 | +0.255 | +2940.94€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3335 | -0.015 | +428.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3335 | -0.015 | +428.75€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3515 | +0.014 | +1237.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3515 | +0.014 | +1237.84€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2976 | +0.270 | +3116.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2976 | +0.270 | +3116.00€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 16350 | +0.169 | +12016.23€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 16350 | +0.169 | +12016.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2420 | +0.208 | +1930.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2420 | +0.208 | +1930.99€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2590 | +0.154 | +1868.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2590 | +0.154 | +1868.07€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2522 | +0.205 | +1977.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2522 | +0.205 | +1977.60€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2716 | +0.142 | +1853.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2716 | +0.142 | +1853.23€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3086 | +0.113 | +2003.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3086 | +0.113 | +2003.24€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3016 | +0.203 | +2383.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3016 | +0.203 | +2383.11€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4141 | +0.125 | +1661.48€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4141 | +0.125 | +1661.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 150 | +0.118 | +61.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 150 | +0.118 | +61.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1110 | +0.114 | +430.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1110 | +0.114 | +430.61€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1149 | +0.151 | +526.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1149 | +0.151 | +526.72€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 861 | +0.086 | +240.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 861 | +0.086 | +240.91€ | 1 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 20145 | +0.173 | +14568.26€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 20145 | +0.173 | +14568.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3150 | +0.220 | +2646.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3150 | +0.220 | +2646.28€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3159 | +0.151 | +2065.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3159 | +0.151 | +2065.99€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3263 | +0.221 | +2753.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3263 | +0.221 | +2753.73€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3214 | +0.137 | +2085.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3214 | +0.137 | +2085.50€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3539 | +0.107 | +2039.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3539 | +0.107 | +2039.21€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3820 | +0.203 | +2977.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3820 | +0.203 | +2977.55€ | 0 | 23 |
| ✅ GBM_LATE_5M | 5972 | +0.141 | +3249.54€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5972 | +0.141 | +3249.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1577 | +0.141 | +974.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1577 | +0.141 | +974.04€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1819 | +0.146 | +988.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1819 | +0.146 | +988.66€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 320 | +0.031 | +41.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 320 | +0.031 | +41.18€ | 2 | 5 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1279 | +0.067 | +534.80€ | 2 | 16 |
| ✅ GBM_LATE_60M#60min | 1279 | +0.067 | +534.80€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 452 | +0.090 | +176.02€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 452 | +0.090 | +176.02€ | 1 | 18 |
| ✅ GBM_LATE_60M#ETH | 428 | +0.072 | +215.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 428 | +0.072 | +215.72€ | 2 | 17 |
| ✅ GBM_LATE_60M#SOL | 399 | +0.034 | +143.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 399 | +0.034 | +143.06€ | 1 | 11 |
| 🚫 GBM_LATE_60M_FADE | 303 | -0.267 | -23.86€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 303 | -0.267 | -23.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 113 | -0.222 | -7.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 113 | -0.222 | -7.68€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 103 | -0.300 | -13.97€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 103 | -0.300 | -13.97€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 87 | -0.275 | -2.21€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 87 | -0.275 | -2.21€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 601 | +0.056 | +114.51€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 601 | +0.056 | +114.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 240 | +0.045 | +38.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 240 | +0.045 | +38.86€ | 4 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 176 | +0.039 | +6.23€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 176 | +0.039 | +6.23€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 185 | +0.083 | +69.42€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 185 | +0.083 | +69.42€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 70 | +0.264 | +51.39€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1419 | +0.106 | +415.14€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1419 | +0.106 | +415.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1419 | +0.106 | +415.14€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1419 | +0.106 | +415.14€ | 0 | 5 |
| ✅ LIQUIDACIONES_15M | 352 | -0.085 | -34.51€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 352 | -0.085 | -34.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 87 | -0.084 | -7.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 87 | -0.084 | -7.38€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 118 | -0.017 | -3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 118 | -0.017 | -3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1542 | -0.003 | -5.77€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1542 | -0.003 | -5.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 169 | -0.015 | +3.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 169 | -0.015 | +3.90€ | 5 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 631 | +0.023 | +16.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 631 | +0.023 | +16.30€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 460 | -0.006 | -8.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 460 | -0.006 | -8.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 105 | -0.061 | -6.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 105 | -0.061 | -6.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 911 | -0.049 | -29.03€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 911 | -0.049 | -29.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 264 | -0.053 | -14.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 264 | -0.053 | -14.59€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 291 | -0.039 | -5.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 291 | -0.039 | -5.52€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 356 | -0.053 | -8.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 356 | -0.053 | -8.92€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 13283 | -0.012 | -188.72€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 13283 | -0.012 | -188.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2457 | -0.024 | -52.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2457 | -0.024 | -52.13€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2742 | -0.016 | -22.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2742 | -0.016 | -22.66€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3264 | -0.018 | -62.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3264 | -0.018 | -62.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 22389 | -0.012 | +970.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 22389 | -0.012 | +970.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3892 | +0.010 | +498.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3892 | +0.010 | +498.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3613 | -0.026 | -27.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3613 | -0.026 | -27.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3916 | +0.004 | +306.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3916 | +0.004 | +306.62€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3384 | -0.046 | -97.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3384 | -0.046 | -97.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3744 | -0.015 | +154.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3744 | -0.015 | +154.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3840 | -0.002 | +134.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3840 | -0.002 | +134.80€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5016 | -0.041 | -117.45€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5016 | -0.041 | -117.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1091 | -0.049 | -21.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1091 | -0.049 | -21.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 467 | -0.118 | -19.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 467 | -0.118 | -19.16€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1368 | -0.057 | -29.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1368 | -0.057 | -29.11€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 57909 | -0.073 | +1157.90€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 57909 | -0.073 | +1157.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 9740 | -0.082 | +556.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 9740 | -0.082 | +556.10€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 9035 | -0.089 | -340.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 9035 | -0.089 | -340.10€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 9775 | -0.071 | +474.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 9775 | -0.071 | +474.17€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8559 | -0.093 | -232.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8559 | -0.093 | -232.49€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 10722 | -0.048 | +332.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 10722 | -0.048 | +332.15€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 10078 | -0.064 | +368.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 10078 | -0.064 | +368.07€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6739 | -0.021 | -103.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6739 | -0.021 | -103.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1507 | -0.020 | -8.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1507 | -0.020 | -8.36€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1496 | -0.015 | -5.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1496 | -0.015 | -5.58€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1001 | -0.037 | -15.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1001 | -0.037 | -15.24€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 989 | +0.113 | +344.44€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 853 | +0.121 | +331.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 193 | +0.136 | +94.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 193 | +0.136 | +94.29€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 169 | +0.102 | +44.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 169 | +0.102 | +44.38€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 177 | +0.098 | +58.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 177 | +0.098 | +58.34€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#SOL | 152 | +0.149 | +79.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 152 | +0.149 | +79.43€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 162 | +0.116 | +55.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 162 | +0.116 | +55.41€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 469 | -0.077 | -5.10€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 207 | -0.122 | -32.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 165 | -0.159 | -35.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 167 | -0.068 | +8.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 125 | -0.075 | +1.91€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 95 | +0.005 | +19.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 75 | -0.006 | +13.09€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 365 | -0.100 | -20.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 543 | -0.221 | -44.40€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 227 | -0.203 | -33.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 195 | -0.195 | -31.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 191 | -0.241 | -22.27€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 164 | -0.253 | -26.35€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 125 | -0.216 | +11.61€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 111 | -0.217 | +8.55€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 470 | -0.223 | -49.26€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 198 | +0.395 | +144.37€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 48 | +0.360 | +39.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 48 | +0.360 | +39.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 122 | +0.484 | +109.19€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 122 | +0.484 | +109.19€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#sniper | 198 | +0.395 | +144.37€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 395 | +0.032 | +10.90€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 395 | +0.032 | +10.90€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 176 | +0.028 | +1.44€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 176 | +0.028 | +1.44€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 45 | -0.011 | -3.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 45 | -0.011 | -3.64€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 149 | +0.036 | +9.81€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 149 | +0.036 | +9.81€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 2444 | -0.025 | -109.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2444 | -0.025 | -109.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 562 | -0.023 | -23.39€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 562 | -0.023 | -23.39€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 153 | -0.042 | -13.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 153 | -0.042 | -13.91€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 925 | -0.030 | -45.40€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 925 | -0.030 | -45.40€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 58 | -0.033 | -2.61€ | 2 | 1 |
| ✅ STREAK_FADE_60M#60min | 58 | -0.033 | -2.61€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 23 | +0.060 | +1.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 23 | +0.060 | +1.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6549 | +0.021 | +86.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6549 | +0.021 | +86.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2098 | +0.020 | +18.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2098 | +0.020 | +18.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1367 | +0.030 | +34.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1367 | +0.030 | +34.67€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1903 | +0.012 | +2.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1903 | +0.012 | +2.46€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1181 | +0.028 | +30.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1181 | +0.028 | +30.60€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6036 | +0.012 | -37.27€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6036 | +0.012 | -37.27€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2393 | +0.019 | -0.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2393 | +0.019 | -0.79€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2391 | +0.014 | -10.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2391 | +0.014 | -10.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1252 | -0.006 | -26.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1252 | -0.006 | -26.07€ | 2 | 0 |
| ✅ UPDOWN_GBM | 26128 | +0.029 | +1445.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 6997 | +0.059 | +1116.21€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 983 | +0.005 | +8.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 16458 | +0.023 | +325.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1584 | -0.004 | -7.75€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2283 | +0.072 | +220.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 278 | +0.125 | +88.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1986 | +0.065 | +132.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4720 | +0.032 | +311.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 860 | +0.081 | +195.08€ | 0 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 279 | +0.023 | +7.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2841 | +0.028 | +103.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 700 | -0.001 | +4.66€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 40 | -0.119 | +1.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3072 | +0.032 | +99.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 238 | +0.113 | +61.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2818 | +0.025 | +38.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 5377 | +0.016 | +213.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1922 | +0.046 | +214.39€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 266 | +0.007 | +8.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2589 | +0.002 | -4.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 565 | -0.008 | -8.28€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 35 | -0.149 | +3.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6737 | +0.016 | +156.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1876 | +0.024 | +109.84€ | 1 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 260 | -0.008 | -2.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4253 | +0.017 | +53.43€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 319 | -0.002 | -4.14€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 29 | -0.145 | -0.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3937 | +0.042 | +445.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1823 | +0.079 | +447.47€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 143 | -0.010 | -3.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1971 | +0.011 | +1.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 104 | -0.141 | +4.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 423 | +0.333 | +118.82€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 423 | +0.333 | +118.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 237 | +0.333 | +61.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 237 | +0.333 | +61.11€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 186 | +0.330 | +57.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 186 | +0.330 | +57.71€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 9187 | -0.048 | +1954.44€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 9187 | -0.048 | +1954.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 416 | -0.055 | +343.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 416 | -0.055 | +343.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1762 | -0.128 | +34.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1762 | -0.128 | +34.03€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 146 | +0.122 | +60.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 146 | +0.122 | +60.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1007 | +0.194 | +565.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1007 | +0.194 | +565.91€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2938 | -0.062 | +460.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2938 | -0.062 | +460.98€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2918 | -0.075 | +490.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2918 | -0.075 | +490.25€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 102 | +0.067 | +14.80€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 102 | +0.067 | +14.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 102 | +0.067 | +14.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 102 | +0.067 | +14.80€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 716 | +0.285 | +573.99€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 716 | +0.285 | +573.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 399 | +0.276 | +299.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 399 | +0.276 | +299.88€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 317 | +0.296 | +274.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 317 | +0.296 | +274.11€ | 0 | 11 |
| ✅ UPDOWN_OU_5M | 686 | -0.109 | -80.31€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 686 | -0.109 | -80.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 184 | -0.070 | -12.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 184 | -0.070 | -12.11€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 66 | -0.176 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 66 | -0.176 | -10.12€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1949 | +0.304 | +1002.88€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 650 | +0.248 | +104.58€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 700 | +0.293 | +287.86€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 599 | +0.375 | +610.45€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.016 n=372 — no justifica filtro, seguir monitorizando
  - _Datos_: n=372 IC=+0.016 PNL=+18.02€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 462 celda(s) pasan gate riguroso completo de 2053 evaluadas (n>=40) y 3022 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.024 < 0.08 — monitorear
  - _Datos_: n=1874 IC=+0.024 PNL=+109.86€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=700/15 IC=+0.293 PNL=+287.86€ | BTC: n=650/15 IC=+0.248 PNL=+104.58€ | SOL: n=599/15 IC=+0.375 PNL=+610.45€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.097 n=189/60 | contraria IC=+0.135 n=168 | gap=-0.038 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=246, boost estimado=+0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=565/40 IC=-0.008 PNL=-8.28€ | BTC#60min: n=699/40 IC=-0.002 PNL=+4.18€ | SOL#60min: n=319/40 IC=-0.002 PNL=-4.14€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.053 n=265662 | tras_1loss IC=+0.072 n=207640 | tras_2loss IC=+0.040 n=88845/40 | gap=+0.013 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.08 con n=205 PNL=+146.10€
  - _Datos_: n=205 IC=+0.196 PNL=+146.10€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.08 con n=276 PNL=+173.48€
  - _Datos_: n=276 IC=+0.194 PNL=+173.48€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.344 > 0.1 con n=1630 PNL=+995.44€
  - _Datos_: n=1630 IC=+0.344 PNL=+995.44€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=201 IC=+0.076 PNL=+26.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=201 IC=+0.076 PNL=+26.64€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=45 IC=+0.202 PNL=+32.49€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=45 IC=+0.202 PNL=+32.49€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=1151 IC=-0.005 PNL=-14.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1151 IC=-0.005 PNL=-14.84€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=432 IC=-0.002 PNL=+6.61€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=432 IC=-0.002 PNL=+6.61€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.1 con n=1473 PNL=+843.92€
  - _Datos_: n=1473 IC=+0.175 PNL=+843.92€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=859 IC=+0.082 PNL=+195.64€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=859 IC=+0.082 PNL=+195.64€

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
  - _Estado_: n=393 IC=+0.014 PNL=+27.75€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=393 IC=+0.014 PNL=+27.75€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=29 IC=+0.048 PNL=+0.86€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=29 IC=+0.048 PNL=+0.86€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.264 n=70) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=70 IC=+0.264 PNL=+51.39€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.02 con n=567 PNL=+230.73€
  - _Datos_: n=567 IC=+0.129 PNL=+230.73€

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
  - _Estado_: n=8491 IC=+0.049 PNL=+965.23€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=8491 IC=+0.049 PNL=+965.23€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.165 < -0.1 con n=162 PNL=+10.58€
  - _Datos_: n=162 IC=-0.165 PNL=+10.58€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1406 IC=+0.048 PNL=+164.26€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1406 IC=+0.048 PNL=+164.26€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=56 IC=-0.086 PNL=+7.93€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=56 IC=-0.086 PNL=+7.93€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.141 > 0.1 con n=279 PNL=+89.61€
  - _Datos_: n=279 IC=+0.141 PNL=+89.61€

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
  - _Estado_: n=13845 IC=-0.144 PNL=+604.97€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13845 IC=-0.144 PNL=+604.97€

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
  - _Estado_: n=1533 IC=+0.137 PNL=+800.32€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1533 IC=+0.137 PNL=+800.32€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2669 IC=+0.016 PNL=+74.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2669 IC=+0.016 PNL=+74.27€

**〰️ H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: n=1597 IC=+0.079 PNL=+804.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1597 IC=+0.079 PNL=+804.82€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.244 < -0.1 con n=1395 PNL=-205.84€
  - _Datos_: n=1395 IC=-0.244 PNL=-205.84€

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
  - _Estado_: 29/40 ops en el filtro definido (IC actual=-0.016 PNL=+5.59€)
  - _Datos_: n=29 IC=-0.016 PNL=+5.59€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=741) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=741 IC=+0.099 PNL=+195.09€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=389) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=389 IC=+0.413 PNL=+545.43€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=7147 IC=+0.171 PNL=-896.88€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=7147 IC=+0.171 PNL=-896.88€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.1 con n=108 PNL=+72.77€
  - _Datos_: n=108 IC=+0.227 PNL=+72.77€
