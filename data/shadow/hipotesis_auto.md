# Hipótesis automáticas — 2026-09-16 17:04 UTC
_Generado por shadow_postmortem.py sobre 469294 resoluciones (PNL=+50323.66€)_

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
- **FILTRO** `restante_s_al_confirmar` < `144.5` → IC=-0.252 (n=5807)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.5
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=17424)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `139.1` → IC=-0.280 (n=797)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.1
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2393)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `486.3` → IC=-0.164 (n=313)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 486.3
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=939)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `136.09` → IC=-0.280 (n=710)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.09
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2132)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `157.73` → IC=-0.252 (n=1381)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.73
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=4146)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `122.05` → IC=-0.359 (n=1115)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.05
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=3345)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.243 (n=251)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=270)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.142 (n=118)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=391)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.156 (n=123)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=386)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.262 (n=128)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=153)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.142 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=196)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.256 (n=80)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=44)

- **FILTRO** `py_entrada` < `0.42` → IC=-0.194 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=97)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.196 (n=11761)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.69 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=2936)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `5280.0735` → IC=+0.169 (n=1869)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 5280.0735 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=9030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=10886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.246 (n=8021)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=5779)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7220.7864` → IC=+0.176 (n=1828)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7220.7864 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1373)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.347 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `14970.8921` → IC=+0.205 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14970.8921 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=1385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.37` → IC=+0.273 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `13178.3279` → IC=+0.214 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13178.3279 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.182 (n=275)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.62 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=286)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `4641.025` → IC=+0.148 (n=231)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4641.025 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.185 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.167 (n=571)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.425 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=543)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3846.6396` → IC=+0.157 (n=421)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3846.6396 (IC base=+0.132)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.138 (n=2015)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.327 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=1059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.302 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.245 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `3743.7277` → IC=+0.244 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3743.7277 (IC base=+0.239)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.134 (n=550)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.221 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=640)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `1933.4748` → IC=+0.156 (n=364)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1933.4748 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.081)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=1088)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.424 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=1111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.268 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.181 (n=1122)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.03 (IC base=+0.176)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.172 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 13.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.338 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.178 (n=181)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.225 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=327)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.124)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=9232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=8883)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.221 (n=3275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.178 (n=2286)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.316 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.287 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.333 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.279)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=2267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2172)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=1929)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=2027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.321 (n=672)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=1891)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.194 (n=1580)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.439 (n=374)
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
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.412 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.403)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.403)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=20)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=27358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.238 (n=10397)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=5591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4747)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=5038)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.170)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=4875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=4882)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.272 (n=1747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=2623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=5033)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.169)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=1859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.269 (n=1736)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=4521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.255 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.193 (n=4586)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=3678)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.250 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.191)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.204 (n=4173)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.07` → IC=+0.132 (n=3804)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.07 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.153 (n=3808)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 4.95 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.137 (n=5654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.3` → IC=+0.153 (n=3812)

  - _Acción_: Kelly boost +0.77€ cuando `lag_apertura_s` < 3.3 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.208 (n=2105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.129)

- **PATRÓN** `restante_min` < `4.01` → IC=+0.135 (n=1895)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.01 (IC base=+0.129)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.148 (n=2033)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.93 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.146 (n=2795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.129)

- **PATRÓN** `lag_apertura_s` < `4.07` → IC=+0.152 (n=1886)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 4.07 (IC base=+0.129)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.126 (n=2533)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.48 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.147 (n=1962)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.128 (n=2537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.5` → IC=+0.148 (n=1918)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 2.5 (IC base=+0.119)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.384 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1613.1588` → IC=+0.297 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1613.1588 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.273)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.338 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `3358.5917` → IC=+0.279 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3358.5917 (IC base=+0.273)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.329 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.390 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1493.0973` → IC=+0.313 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1493.0973 (IC base=+0.291)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.438 (n=368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.433 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `1864.6918` → IC=+0.438 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1864.6918 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.438 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=197)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.434 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.447 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.434 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `2127.0131` → IC=+0.455 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2127.0131 (IC base=+0.433)

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
- **PATRÓN** `ibs_20min` > `0.9779` → IC=+0.229 (n=2076)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9779 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.2132` → IC=+0.243 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2132 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.856` → IC=+0.166 (n=2402)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.856 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6105` → IC=+0.252 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6105 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.0676` → IC=+0.240 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0676 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1746` → IC=+0.191 (n=4265)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1746 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.308` → IC=+0.200 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.308 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.4716` → IC=+0.193 (n=4104)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4716 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.5676` → IC=+0.131 (n=7653)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5676 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.5758` → IC=+0.183 (n=453)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5758 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.3459` → IC=+0.167 (n=2660)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3459 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.6996` → IC=+0.168 (n=1100)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6996 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` > `0.8714` → IC=+0.177 (n=1666)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8714 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.223 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` > `1.4676` → IC=+0.197 (n=4159)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4676 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.209 (n=3931)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.060)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.182 (n=470)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0049 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.180 (n=470)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0077 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.183 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 8.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.057` → IC=+0.274 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.057 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.197 (n=183)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.163 (n=1294)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.184 (n=1302)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.04 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.251 (n=935)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.194` → IC=+0.271 (n=698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.194 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.252 (n=715)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0542` → IC=+0.288 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0542 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.377` → IC=+0.246 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.377 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0688` → IC=+0.232 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0688 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2841` → IC=+0.276 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2841 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.7186` → IC=+0.263 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7186 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1739.2496` → IC=+0.251 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1739.2496 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.223 (n=936)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.239 (n=469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=1115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9179` → IC=+0.252 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9179 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1987` → IC=+0.220 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1987 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.858` → IC=+0.233 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.858 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2628` → IC=+0.221 (n=1063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2628 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.0989` → IC=+0.218 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0989 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4957` → IC=+0.218 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4957 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.221 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `10979.8664` → IC=+0.221 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10979.8664 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.156 (n=1004)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0049 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.155 (n=381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.168 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6705` → IC=+0.173 (n=1140)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6705 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1275` → IC=+0.149 (n=1039)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1275 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.172 (n=193)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.144 (n=1140)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2046 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.8472` → IC=+0.141 (n=761)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8472 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.182 (n=309)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4267` → IC=+0.153 (n=1031)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4267 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `13456.9562` → IC=+0.151 (n=760)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 13456.9562 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `216.0` → IC=+0.158 (n=320)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 216.0 (IC base=+0.137)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.176 (n=1209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0089 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.187 (n=1374)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0058 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.176 (n=1373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.563` → IC=+0.211 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.563 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.181 (n=1168)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.3763` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.3763 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.666` → IC=+0.180 (n=1285)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.666 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.188 (n=1573)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.04 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.190 (n=479)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 16.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.221 (n=1185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.215 (n=1061)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0602` → IC=+0.248 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0602 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.554` → IC=+0.233 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.554 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.364` → IC=+0.216 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.364 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.264 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.8483` → IC=+0.204 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8483 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.3042` → IC=+0.223 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3042 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `1883.1265` → IC=+0.231 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1883.1265 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.225 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1732)

- **PATRÓN** `ibs_20min` > `0.9309` → IC=+0.168 (n=287)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.9309 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.3351` → IC=+0.335 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3351 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` < `0.4875` → IC=+0.329 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4875 (IC base=+0.006)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.258` → IC=+0.135 (n=538)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 4.258 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6461` → IC=+0.380 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6461 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1929 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2833` → IC=+0.350 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2833 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.4916` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4916 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1278` → IC=+0.338 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1278 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.345 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 165.0 (IC base=+0.006)

- **PATRÓN** `dist_vwap_pct` > `0.1655` → IC=+0.192 (n=193)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1655 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.147 (n=250)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6963 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `1.1669` → IC=+0.151 (n=190)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1669 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2684` → IC=+0.233 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2684 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.5087` → IC=+0.183 (n=462)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.5087 (IC base=+0.003)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.154 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=243)

- **FILTRO** `ibs_20min` < `0.3714` → IC=-0.173 (n=96)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3714
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=197)

- **FILTRO** `ibs_20min` > `0.2692` → IC=-0.125 (n=1762)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=869)

- **FILTRO** `sigma_ewma_delta_pct` > `8.613` → IC=-0.200 (n=288)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.613
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2343)

- **PATRÓN** `ibs_20min` > `0.7547` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7547 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `1.3203` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.3203 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.5788` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5788 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.323 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `3.0245` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0245 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.278 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.323 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.7533` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7533 (IC base=-0.045)

- **PATRÓN** `volumen_regimen` < `1.1047` → IC=+0.212 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1047 (IC base=-0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=-0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.4773` → IC=+0.246 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4773 (IC base=-0.045)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6568` → IC=-0.194 (n=436)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1312)

- **FILTRO** `ibs_20min` < `0.7882` → IC=-0.141 (n=1311)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7882
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=437)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.200 (n=378)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1370)

- **FILTRO** `ibs_20min` > `0.7751` → IC=-0.200 (n=662)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7751
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1988)

- **PATRÓN** `dist_vwap_pct` > `0.9726` → IC=+0.324 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9726 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` < `0.2555` → IC=+0.299 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2555 (IC base=-0.085)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.290 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6141 (IC base=-0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.0746` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0746 (IC base=-0.085)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.276 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=-0.085)

- **PATRÓN** `volumen_spike_ratio` > `1.8242` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8242 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` > `1.0227` → IC=+0.267 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0227 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` < `0.2666` → IC=+0.244 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2666 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` > `1.0842` → IC=+0.292 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0842 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.1065` → IC=+0.275 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1065 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.224` → IC=+0.260 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.224 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.4752` → IC=+0.241 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4752 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.247 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.173 (n=2600)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0091 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.9821` → IC=+0.288 (n=2600)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9821 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `1.0155` → IC=+0.285 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0155 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.523` → IC=+0.141 (n=3683)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.523 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `0.6761` → IC=+0.235 (n=2364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6761 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.225 (n=4015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2482` → IC=+0.255 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2482 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.478` → IC=+0.240 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.478 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.7761` → IC=+0.234 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7761 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.276 (n=3693)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.086)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.141 (n=2646)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0085 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.151 (n=6983)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5556 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6852` → IC=+0.245 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6852 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2319` → IC=+0.230 (n=2116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2319 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.7147` → IC=+0.232 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7147 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `1.2011` → IC=+0.253 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2011 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2514` → IC=+0.317 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2514 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.4922` → IC=+0.255 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4922 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `2.37` → IC=+0.254 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.37 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.256 (n=2696)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.068)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2293` → IC=-0.139 (n=536)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2293
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=1608)

- **FILTRO** `sigma_ewma_delta_pct` > `4.412` → IC=-0.164 (n=391)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.412
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1309)

- **PATRÓN** `ibs_20min` > `0.8632` → IC=+0.249 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8632 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.293` → IC=+0.145 (n=722)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.293 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.288 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.8402` → IC=+0.188 (n=360)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.8402 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.6489` → IC=+0.192 (n=180)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6489 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8266` → IC=-0.148 (n=584)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8266
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1756)

- **PATRÓN** `dist_vwap_pct` > `0.2998` → IC=+0.140 (n=251)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.2998 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.0507` → IC=+0.130 (n=600)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0507 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6498` → IC=+0.136 (n=611)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6498 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2205` → IC=+0.172 (n=123)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2205 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.173 (n=221)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.185 (n=217)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 231.0 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1592` → IC=+0.206 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1592 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `1.1403` → IC=+0.221 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1403 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.0714` → IC=+0.203 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0714 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2834` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2834 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.8012` → IC=+0.218 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8012 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.220 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `243.0` → IC=+0.219 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 243.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.265 (n=1109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0966` → IC=+0.248 (n=414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0966 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.237 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.253 (n=463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.269 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.1111` → IC=+0.253 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1111 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.8816` → IC=+0.237 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8816 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `3.6393` → IC=+0.249 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6393 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.252 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.295 (n=990)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.317 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.3321` → IC=+0.284 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3321 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.795` → IC=+0.298 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.795 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.3494` → IC=+0.300 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3494 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.6329` → IC=+0.284 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6329 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.2419` → IC=+0.278 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2419 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.283 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `1875.32` → IC=+0.301 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.32 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.271 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.278)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2448` → IC=-0.211 (n=355)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2448
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1072)

- **FILTRO** `ibs_20min` > `0.8089` → IC=-0.182 (n=467)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8089
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1402)

- **PATRÓN** `ibs_20min` > `0.806` → IC=+0.143 (n=486)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.806 (IC base=-0.014)

- **PATRÓN** `dist_vwap_pct` > `0.466` → IC=+0.213 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.466 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` < `0.9565` → IC=+0.216 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9565 (IC base=-0.014)

- **PATRÓN** `volumen_regimen` > `0.5518` → IC=+0.190 (n=330)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 0.5518 (IC base=-0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.2672` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2672 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.4909` → IC=+0.259 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4909 (IC base=-0.014)

- **PATRÓN** `volumen_spike_ratio` > `1.7422` → IC=+0.218 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7422 (IC base=-0.014)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.243 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=-0.014)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1247 (IC base=-0.018)

- **PATRÓN** `dist_vwap_pct` < `0.2864` → IC=+0.172 (n=248)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2864 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` < `1.1494` → IC=+0.168 (n=239)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1494 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` > `0.7204` → IC=+0.181 (n=214)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.7204 (IC base=-0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.4157` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4157 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.244 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.210 (n=835)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.254 (n=854)

- **FILTRO** `ibs_20min` > `0.7115` → IC=-0.233 (n=447)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7115
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1344)

- **FILTRO** `sigma_ewma_delta_pct` > `4.677` → IC=-0.172 (n=416)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.677
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=1375)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.254 (n=854)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7586` → IC=+0.334 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7586 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.293 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.7198` → IC=+0.276 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7198 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.280 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.326 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.317 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.321 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.1053` → IC=+0.196 (n=448)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1053 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` > `0.5842` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5842 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` < `0.1823` → IC=+0.196 (n=337)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1823 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.256 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7154 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.188 (n=334)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2178` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2178 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.5839` → IC=+0.212 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5839 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4942` → IC=+0.186 (n=345)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4942 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.228 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0155` → IC=+0.322 (n=702)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0155 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.287 (n=495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` > `0.9043` → IC=+0.347 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9043 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.2672` → IC=+0.317 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2672 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.299 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.6824` → IC=+0.286 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6824 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2364` → IC=+0.301 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2364 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `1.5484` → IC=+0.275 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5484 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.207` → IC=+0.276 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.207 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.274 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2587.3393` → IC=+0.278 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.3393 (IC base=+0.270)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.324 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0143` → IC=+0.294 (n=774)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0143 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.284 (n=576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.3939` → IC=+0.306 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3939 (IC base=+0.268)

- **PATRÓN** `dist_vwap_pct` > `0.5491` → IC=+0.285 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5491 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.43` → IC=+0.291 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.43 (IC base=+0.268)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.310 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2426` → IC=+0.359 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2426 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `2.5387` → IC=+0.265 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5387 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.1671` → IC=+0.268 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1671 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `2350.7328` → IC=+0.274 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2350.7328 (IC base=+0.268)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.177 (n=2053)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0048 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.200 (n=2049)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3341` → IC=+0.171 (n=5406)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3341 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=6406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.6942` → IC=+0.228 (n=5486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6942 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.9466` → IC=+0.221 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9466 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.218` → IC=+0.246 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.218 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.2135` → IC=+0.161 (n=4087)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2135 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.158 (n=4087)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6211 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.1068` → IC=+0.185 (n=2401)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1068 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.5664` → IC=+0.172 (n=2570)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5664 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6656` → IC=+0.167 (n=1947)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.6656 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3822.0558` → IC=+0.169 (n=2047)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 3822.0558 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.182 (n=5053)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 122.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.188 (n=3995)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0064 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.203 (n=1998)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=1997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.461` → IC=+0.227 (n=5989)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.461 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.2225` → IC=+0.161 (n=4476)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2225 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.234` → IC=+0.196 (n=1032)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.234 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1891` → IC=+0.156 (n=4378)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1891 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6256` → IC=+0.151 (n=4378)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6256 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.228 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.5751` → IC=+0.174 (n=2346)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5751 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.651` → IC=+0.176 (n=1777)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.651 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.172 (n=4948)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 123.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.224 (n=349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.205 (n=347)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.3156` → IC=+0.202 (n=1039)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3156 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.211 (n=513)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.049` → IC=+0.305 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.049 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.239 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `2.5428` → IC=+0.178 (n=946)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.5428 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.427` → IC=+0.180 (n=946)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.427 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.206 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.242 (n=669)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.251 (n=676)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1823` → IC=+0.292 (n=504)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1823 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=688)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.242 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.258 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.083` → IC=+0.252 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.083 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0955` → IC=+0.235 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0955 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.273 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4302` → IC=+0.261 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4302 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.243 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1741.1448` → IC=+0.261 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1741.1448 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.246 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.185 (n=300)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=949)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.4292` → IC=+0.221 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4292 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2099` → IC=+0.212 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2099 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.551` → IC=+0.223 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.551 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.173 (n=898)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.2629 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2311` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2311 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.197 (n=288)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `10070.4177` → IC=+0.176 (n=897)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 10070.4177 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.174 (n=898)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0049 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.196 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.164 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.5312` → IC=+0.191 (n=1020)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5312 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1346` → IC=+0.166 (n=1039)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1346 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.043` → IC=+0.217 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.043 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.161 (n=1020)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2145 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.176 (n=316)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.159 (n=910)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.152 (n=277)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 230.0 (IC base=+0.147)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.197 (n=1016)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0059 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1947` → IC=+0.199 (n=678)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1947 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.285 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.625` → IC=+0.267 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.625 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.2175` → IC=+0.184 (n=974)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2175 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.1358` → IC=+0.184 (n=391)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1358 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.6798` → IC=+0.186 (n=317)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.6798 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `3.6406` → IC=+0.202 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6406 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.226 (n=377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.221 (n=856)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.243 (n=286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.269 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.3448` → IC=+0.251 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3448 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.271 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.272 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.8456` → IC=+0.213 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8456 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `3.5269` → IC=+0.248 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5269 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1884.62` → IC=+0.236 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1884.62 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.217 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.180 (n=851)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4217` → IC=+0.167 (n=967)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4217 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.163 (n=970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3996` → IC=+0.203 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3996 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1355` → IC=+0.193 (n=627)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1355 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.124` → IC=+0.246 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.124 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.858` → IC=+0.160 (n=645)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.858 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `1.1941` → IC=+0.170 (n=322)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1941 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2389` → IC=+0.203 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2389 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1718` → IC=+0.156 (n=830)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1718 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.178 (n=315)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `7148.6032` → IC=+0.187 (n=644)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7148.6032 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.164 (n=605)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 120.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.164 (n=1051)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0071 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3789` → IC=+0.146 (n=1050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3789 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6008` → IC=+0.179 (n=1050)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6008 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1494` → IC=+0.143 (n=1055)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1494 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.972` → IC=+0.188 (n=203)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.972 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8596` → IC=+0.140 (n=700)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8596 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.6106` → IC=+0.133 (n=1050)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.6106 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.193 (n=151)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.138 (n=623)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.7982 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.4806` → IC=+0.142 (n=311)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4806 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.157 (n=476)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.126 (n=862)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 177.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.146 (n=764)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0077 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=1171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.194 (n=1153)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `1.0121` → IC=+0.233 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0121 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.447` → IC=+0.249 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.447 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.121 (n=1142)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2203 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.8007` → IC=+0.125 (n=732)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8007 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=1175)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2897.5388` → IC=+0.190 (n=518)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2897.5388 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.136 (n=831)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 48.0 (IC base=+0.110)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.153 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0053 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.5492` → IC=+0.208 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5492 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.6893` → IC=+0.145 (n=201)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.6893 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.135 (n=1068)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.375` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 7.375 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.1973` → IC=+0.124 (n=1151)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.1973 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.181 (n=139)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4638` → IC=+0.136 (n=336)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4638 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.1766` → IC=+0.133 (n=456)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.1766 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3082.2041` → IC=+0.162 (n=383)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3082.2041 (IC base=+0.113)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` < `0.0272` → IC=+0.202 (n=1083)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0272 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0181` → IC=+0.210 (n=722)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0181 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1671` → IC=+0.212 (n=477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1671 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=490)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.7277` → IC=+0.254 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7277 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `1.2464` → IC=+0.236 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2464 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.243 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.206 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2068 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6101` → IC=+0.210 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6101 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.260 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1845` → IC=+0.216 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1845 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.202 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2566.7167` → IC=+0.202 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2566.7167 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.233 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0222` → IC=+0.214 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0222 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.0904` → IC=+0.212 (n=387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0904 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=530)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.027` → IC=+0.309 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.027 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `1.1573` → IC=+0.228 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1573 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.2686` → IC=+0.205 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2686 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.244 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6291` → IC=+0.218 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6291 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.285 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.2458` → IC=+0.198 (n=901)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.2458 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4614` → IC=+0.194 (n=1023)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4614 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2541.3638` → IC=+0.215 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2541.3638 (IC base=+0.204)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.149 (n=497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.155 (n=497)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0088 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0966` → IC=+0.148 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0966 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.177 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.388` → IC=+0.165 (n=1485)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.388 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.8281` → IC=+0.167 (n=202)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.8281 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.027` → IC=+0.170 (n=516)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 6.027 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8649` → IC=+0.154 (n=853)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8649 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1644` → IC=+0.166 (n=408)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1644 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.4332` → IC=+0.145 (n=474)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4332 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.5716` → IC=+0.158 (n=474)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5716 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=1647)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `8454.7872` → IC=+0.150 (n=673)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8454.7872 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.156 (n=1265)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 156.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.135 (n=1055)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.3392` → IC=+0.128 (n=1390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3392 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=1598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.4848` → IC=+0.157 (n=1390)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4848 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2044` → IC=+0.122 (n=1408)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2044 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.836` → IC=+0.135 (n=619)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 3.836 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.2231` → IC=+0.120 (n=1400)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2231 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.1666` → IC=+0.142 (n=403)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1666 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `2.2286` → IC=+0.136 (n=1329)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2286 (IC base=+0.115)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.151 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.146 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 10.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.2836` → IC=+0.131 (n=334)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.2836 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.138 (n=103)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.256` → IC=+0.154 (n=157)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.256 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.6949` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6949 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `9834.2432` → IC=+0.128 (n=334)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 9834.2432 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 151.0 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.205 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.147 (n=486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.3419` → IC=+0.203 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3419 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.138 (n=197)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.2002` → IC=+0.127 (n=486)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2002 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.0616` → IC=+0.171 (n=220)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.0616 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.207 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.4163` → IC=+0.148 (n=476)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4163 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.132 (n=476)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.150 (n=155)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 159.0 (IC base=+0.126)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.260 (n=202)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.199 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.219 (n=151)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.2587` → IC=+0.226 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2587 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.367` → IC=+0.223 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.367 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.116` → IC=+0.228 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.116 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.8293` → IC=+0.200 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8293 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.212 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2472` → IC=+0.318 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2472 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.374` → IC=+0.215 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.374 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.3827` → IC=+0.253 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3827 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `12351.8233` → IC=+0.212 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12351.8233 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.133 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0066 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.0962` → IC=+0.157 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0962 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.140 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 11.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.3025` → IC=+0.165 (n=270)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.3025 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.1474` → IC=+0.120 (n=156)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` > 0.1474 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.432` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 6.432 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.2294` → IC=+0.121 (n=404)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2294 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.170 (n=95)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `1.5498` → IC=+0.126 (n=343)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.5498 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.9` → IC=+0.201 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.169 (n=143)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `3029.7873` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3029.7873 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.131 (n=101)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 21.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.475` → IC=+0.158 (n=311)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.475 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.126` → IC=+0.120 (n=106)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` > 5.126 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.7177` → IC=+0.147 (n=137)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.7177 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `2.5598` → IC=+0.133 (n=287)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5598 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `2922.181` → IC=+0.136 (n=141)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2922.181 (IC base=+0.086)

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
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.192 (n=3535)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0086 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=8138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.213 (n=7783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4717 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.9009` → IC=+0.202 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9009 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.222 (n=3814)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8833` → IC=+0.167 (n=3491)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8833 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2395` → IC=+0.186 (n=1471)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2395 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.6366` → IC=+0.183 (n=2472)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6366 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3796.8122` → IC=+0.169 (n=2594)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3796.8122 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.193 (n=5638)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 93.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.196 (n=4795)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0067 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4789` → IC=+0.183 (n=7173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.4789 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=2714)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5584` → IC=+0.239 (n=7173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5584 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2337` → IC=+0.162 (n=4566)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2337 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.836` → IC=+0.199 (n=1030)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.836 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.695` → IC=+0.182 (n=6929)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.695 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.6286` → IC=+0.160 (n=1655)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6286 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.2044` → IC=+0.160 (n=1653)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.2044 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.247 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.2996` → IC=+0.189 (n=2919)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.2996 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.178 (n=6054)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 125.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.212 (n=439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.228 (n=597)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=886)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.317 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.876` → IC=+0.312 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.876 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2266` → IC=+0.237 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2266 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `1.5568` → IC=+0.181 (n=538)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5568 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.5691` → IC=+0.198 (n=408)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.5691 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.263 (n=687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.265 (n=1030)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.2026` → IC=+0.280 (n=685)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2026 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=933)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.3409` → IC=+0.286 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3409 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.61` → IC=+0.264 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.61 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.298 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6838` → IC=+0.297 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6838 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1592.66` → IC=+0.270 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.66 (IC base=+0.256)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.193 (n=415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0028 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1834` → IC=+0.153 (n=825)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1834 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6873` → IC=+0.244 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6873 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.34` → IC=+0.199 (n=473)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.34 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.774` → IC=+0.161 (n=290)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.774 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.396` → IC=+0.152 (n=1100)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.396 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6942` → IC=+0.186 (n=545)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6942 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.177 (n=339)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.1158` → IC=+0.157 (n=1042)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1158 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7544` → IC=+0.156 (n=789)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7544 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `10840.8065` → IC=+0.166 (n=1105)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 10840.8065 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `492.0` → IC=+0.159 (n=1115)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 492.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.168 (n=1107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0057 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.3247` → IC=+0.164 (n=1107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3247 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.178 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 18.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6372` → IC=+0.205 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6372 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.7006` → IC=+0.161 (n=169)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.7006 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1297` → IC=+0.162 (n=1022)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1297 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.534` → IC=+0.173 (n=197)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.534 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.161 (n=1107)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1954 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1509` → IC=+0.206 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1509 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4003` → IC=+0.167 (n=1009)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.4003 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `371.0` → IC=+0.163 (n=609)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 371.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.224 (n=1237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.215 (n=1260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.6721` → IC=+0.247 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6721 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.548` → IC=+0.296 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.548 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.2176` → IC=+0.214 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2176 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `3.0042` → IC=+0.231 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0042 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.236 (n=1188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.3642` → IC=+0.267 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3642 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.713` → IC=+0.274 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.713 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3595` → IC=+0.298 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3595 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.8015` → IC=+0.223 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8015 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.2501` → IC=+0.231 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2501 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `1887.4151` → IC=+0.236 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1887.4151 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.254 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.231)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.172 (n=584)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0039 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4293` → IC=+0.139 (n=1318)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4293 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=1382)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.7032` → IC=+0.233 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7032 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3525` → IC=+0.182 (n=485)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.3525 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.258` → IC=+0.162 (n=560)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.258 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8805` → IC=+0.160 (n=879)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8805 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2746` → IC=+0.221 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2746 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5068` → IC=+0.147 (n=559)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5068 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.4575` → IC=+0.159 (n=423)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4575 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8761.5886` → IC=+0.230 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8761.5886 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.168 (n=402)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 88.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.159 (n=1066)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0075 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4386` → IC=+0.155 (n=1066)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4386 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.153 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6884` → IC=+0.193 (n=1066)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6884 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.2048` → IC=+0.144 (n=1003)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2048 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.009` → IC=+0.200 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.009 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.143 (n=469)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.695 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.1877` → IC=+0.151 (n=356)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.1877 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.266 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5573` → IC=+0.148 (n=438)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5573 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.4663` → IC=+0.168 (n=332)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4663 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `10929.1174` → IC=+0.193 (n=356)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 10929.1174 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `192.0` → IC=+0.144 (n=988)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 192.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.180 (n=1337)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4667 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `1.0029` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 1.0029 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.373` → IC=+0.218 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.373 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=928)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2912.6118` → IC=+0.243 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2912.6118 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.127 (n=995)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 53.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.169 (n=572)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0062 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.155 (n=433)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.150 (n=606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.208 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.2689` → IC=+0.130 (n=1127)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.2689 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.449` → IC=+0.128 (n=1249)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.449 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.7205` → IC=+0.154 (n=571)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7205 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2215` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2215 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4615` → IC=+0.150 (n=381)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4615 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.225` → IC=+0.122 (n=517)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 2.225 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2904.3214` → IC=+0.164 (n=433)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2904.3214 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0183` → IC=+0.212 (n=898)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0183 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.205 (n=1203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.5124` → IC=+0.243 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5124 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.1865` → IC=+0.235 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1865 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.087` → IC=+0.261 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.087 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2457` → IC=+0.209 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2457 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.627` → IC=+0.209 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.627 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2371` → IC=+0.234 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2371 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.5793` → IC=+0.239 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5793 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2573.072` → IC=+0.210 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2573.072 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.236 (n=498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.226 (n=497)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.214 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.254 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.2715` → IC=+0.205 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2715 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.723` → IC=+0.265 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.723 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.239 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2868` → IC=+0.258 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2868 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2322` → IC=+0.194 (n=1154)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2322 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4428` → IC=+0.196 (n=1311)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4428 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2549.3704` → IC=+0.202 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2549.3704 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=2576)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.156 (n=2225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0094 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5274` → IC=+0.156 (n=2528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.5274 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.159 (n=843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.161 (n=879)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.9386` → IC=+0.215 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9386 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1884` → IC=+0.156 (n=824)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1884 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.736` → IC=+0.168 (n=814)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 5.736 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.9068` → IC=+0.152 (n=1025)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9068 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1738` → IC=+0.173 (n=690)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1738 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4629` → IC=+0.162 (n=834)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4629 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.9083` → IC=+0.158 (n=1667)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9083 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `8197.4544` → IC=+0.153 (n=1146)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8197.4544 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.189 (n=650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0037 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4871` → IC=+0.154 (n=1944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4871 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.163 (n=650)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.1809` → IC=+0.162 (n=856)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1809 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.7057` → IC=+0.147 (n=344)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7057 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.273` → IC=+0.145 (n=1928)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.273 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1133` → IC=+0.144 (n=1623)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1133 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.152 (n=917)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.5724` → IC=+0.140 (n=1924)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5724 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.8251` → IC=+0.147 (n=1283)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8251 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=2576)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7741.6466` → IC=+0.150 (n=1736)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7741.6466 (IC base=+0.136)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.168 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.171 (n=278)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0034 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.0919` → IC=+0.189 (n=104)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0919 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.539` → IC=+0.195 (n=208)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.539 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2354` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2354 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.256` → IC=+0.167 (n=394)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 8.256 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.2372` → IC=+0.161 (n=311)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2372 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.8262` → IC=+0.199 (n=207)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.8262 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2313` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2313 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.217 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.7022` → IC=+0.198 (n=104)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.7022 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `12609.7541` → IC=+0.207 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12609.7541 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.205 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.146 (n=869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.1529` → IC=+0.164 (n=382)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1529 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6109` → IC=+0.144 (n=394)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6109 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.6011` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6011 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.2277` → IC=+0.135 (n=896)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2277 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.265` → IC=+0.158 (n=848)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.265 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.178 (n=579)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8812 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.162 (n=412)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.5735` → IC=+0.142 (n=865)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5735 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.148 (n=577)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `11358.9394` → IC=+0.149 (n=868)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11358.9394 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `707.0` → IC=+0.138 (n=823)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 707.0 (IC base=+0.134)

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

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.162 (n=540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0071 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.5119` → IC=+0.180 (n=613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.5119 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.154 (n=429)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.162 (n=613)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.1001 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.176 (n=273)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.4008` → IC=+0.149 (n=630)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.4008 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.985` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 8.985 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.176 (n=205)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6473 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.7288` → IC=+0.154 (n=548)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7288 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.1527` → IC=+0.152 (n=631)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1527 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.175 (n=263)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.162 (n=531)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.4508` → IC=+0.162 (n=602)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4508 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `8189.1573` → IC=+0.172 (n=613)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8189.1573 (IC base=+0.148)

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

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.147 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0113 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.6189` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6189 (IC base=+0.045)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.255 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=289)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=289)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.210 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` > `0.649` → IC=+0.218 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.649 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.1307` → IC=+0.173 (n=292)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1307 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.09` → IC=+0.220 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.09 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `1.0933` → IC=+0.125 (n=571)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.0933 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.207 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.156 (n=463)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.456 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.138 (n=462)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.160 (n=248)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.103)

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
- **FILTRO** `ibs_20min` < `0.5881` → IC=-0.172 (n=65)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5881
  - _Potencial_: sin este filtro IC_bueno=+0.212 (n=196)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.181 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.006 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` > `0.5881` → IC=+0.212 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5881 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.535` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 13.535 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `1.0504` → IC=+0.140 (n=173)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0504 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` < `0.0677` → IC=+0.160 (n=139)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.0677 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2541` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2541 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `2.0118` → IC=+0.195 (n=139)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.0118 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=201)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2848.0904` → IC=+0.132 (n=183)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2848.0904 (IC base=+0.109)

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

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.147 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 8.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.6494` → IC=+0.245 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6494 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.5243` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5243 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.057` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.057 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.791` → IC=+0.167 (n=133)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.791 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6236` → IC=+0.142 (n=177)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6236 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2987` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2987 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.183 (n=99)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.3908 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=207)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `1103.6894` → IC=+0.191 (n=173)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 1103.6894 (IC base=+0.122)

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
- **FILTRO** `ibs_20min` < `0.6757` → IC=-0.212 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6757
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=178)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=81)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.167 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0059 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.194 (n=178)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.6757 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.8626` → IC=+0.156 (n=30)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.8626 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `0.9509` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.9509 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.0865` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0865 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `2.5513` → IC=+0.150 (n=158)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.5513 (IC base=+0.074)

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

- **FILTRO** `drift_60min` |x|> `0.2175` → IC=-0.333 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2175
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=104)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=125)

- **FILTRO** `volumen_spike_ratio` > `1.8521` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.8521
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=41)

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

- **FILTRO** `hora_utc` > `8.0` → IC=-0.244 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=22)

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
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=232)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.151 (n=193)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.75 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.234` → IC=+0.131 (n=204)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.234 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.12` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.12 (IC base=+0.043)

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

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.207 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.1435` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1435 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.1776` → IC=+0.128 (n=76)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1776 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.097)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=58)

- **FILTRO** `ibs_20min` < `0.8327` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8327
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=51)

- **FILTRO** `ibs_20min` > `0.3277` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3277
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=74)

- **PATRÓN** `sigma_h` < `0.0015` → IC=+0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0015 (IC base=+0.064)

- **PATRÓN** `drift_60min` |x|≤ `0.111` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.111 (IC base=+0.064)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.8327` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.8327 (IC base=+0.064)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `1571.5815` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1571.5815 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.020)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.55` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=53)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=47)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.167 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3956` → IC=+0.152 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3956 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.167 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 12.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.156 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 18.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.7692 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.5856` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5856 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1961` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1961 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.5494` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5494 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0984` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0984 (IC base=-0.035)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=483)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2833.8623` → IC=+0.159 (n=168)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2833.8623 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2309.0554` → IC=+0.130 (n=550)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2309.0554 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=509)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=483)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2833.8623` → IC=+0.159 (n=168)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2833.8623 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=523)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2309.0554` → IC=+0.130 (n=550)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2309.0554 (IC base=+0.101)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1336)

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
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=90)

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

- **PATRÓN** `liq_usd_total` > `59480.98` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `liq_usd_total` > 59480.98 (IC base=+0.022)

- **PATRÓN** `libro_liquidez` > `16811.4722` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 16811.4722 (IC base=+0.022)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=577)

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
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=260)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=260)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.200 (n=48)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=227)

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

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9998` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9998
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=62)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=214)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=94)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.124 (n=1047)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5498)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=6366)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=1050)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1355)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.179 (n=2683)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=8137)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.171 (n=2770)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=8524)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.221 (n=438)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=1387)

- **FILTRO** `ibs_20min` < `0.748` → IC=-0.180 (n=454)

  - _Acción_: SKIP cuando `ibs_20min` < 0.748
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=1371)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.164 (n=468)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=1546)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.201 (n=460)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1414)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.216 (n=474)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1513)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.164 (n=495)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1492)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.200 (n=445)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1357)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.192 (n=495)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1494)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2411)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2454)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2460)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=287)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.7493` → IC=-0.202 (n=122)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7493
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=122)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=162)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=627)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=7781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=17663)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.284 (n=5950)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=19494)

- **FILTRO** `ibs_7min` < `0.7033` → IC=-0.242 (n=6360)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7033
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=19084)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.161 (n=8412)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=17032)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.225 (n=7924)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=23928)

- **FILTRO** `ibs_7min` > `0.2963` → IC=-0.177 (n=7956)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2963
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=23896)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=965)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3124)

- **FILTRO** `ibs_7min` < `0.7089` → IC=-0.259 (n=1348)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7089
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2741)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.196 (n=964)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3125)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.150 (n=3709)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1829)

- **FILTRO** `drift_7min_pct` |x|> `0.136` → IC=-0.132 (n=1384)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.136
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=4154)

- **FILTRO** `ibs_7min` > `0.7992` → IC=-0.206 (n=1383)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7992
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4155)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=3425)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.258 (n=1038)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3411)

- **FILTRO** `ibs_7min` < `0.7558` → IC=-0.188 (n=1111)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7558
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3338)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.174 (n=1109)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3340)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.257 (n=1057)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3438)

- **FILTRO** `ibs_7min` > `0.2534` → IC=-0.168 (n=1123)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2534
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3372)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=1118)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3377)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.182 (n=937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=2897)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.323 (n=923)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2911)

- **FILTRO** `drift_7min_pct` |x|> `0.181` → IC=-0.131 (n=1302)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.181
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=2532)

- **FILTRO** `ibs_7min` < `0.2021` → IC=-0.274 (n=958)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2021
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2876)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.221 (n=906)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=2928)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.236 (n=1371)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=4459)

- **FILTRO** `ibs_7min` > `0.2629` → IC=-0.156 (n=1982)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2629
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3848)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1324)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=2863)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1018)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3169)

- **FILTRO** `ibs_7min` < `0.7429` → IC=-0.192 (n=1046)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3141)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.183 (n=1035)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3152)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1053)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3225)

- **FILTRO** `ibs_7min` > `0.2743` → IC=-0.174 (n=1069)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2743
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3209)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.180 (n=1060)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3218)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.255 (n=1089)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3500)

- **FILTRO** `ibs_7min` < `0.72` → IC=-0.220 (n=1146)

  - _Acción_: SKIP cuando `ibs_7min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3443)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.171 (n=1451)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4583)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.281 (n=1046)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3250)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.231 (n=1073)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3223)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.210 (n=1052)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3244)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.206 (n=1347)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=4330)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=959)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.130 (n=44)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=482)

- **FILTRO** `libro_liquidez` < `10506.0977` → IC=-0.154 (n=131)

  - _Acción_: SKIP cuando `libro_liquidez` < 10506.0977
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=395)

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
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=529)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.135 (n=637)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.142 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.156 (n=213)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 469.512 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.135 (n=269)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 27.0 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4386` → IC=+0.140 (n=48)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4386 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.139)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.178 (n=88)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.101)

- **PATRÓN** `total_vol_5m` < `672.2721` → IC=+0.172 (n=117)

  - _Acción_: Kelly boost +0.86€ cuando `total_vol_5m` < 672.2721 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 80.0 (IC base=+0.101)

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
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.154 (n=108)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.142 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 13.0 (IC base=+0.114)

- **PATRÓN** `total_vol_5m` < `353208.2` → IC=+0.142 (n=107)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 353208.2 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.114)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.322 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=147)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.167 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0039 (IC base=-0.125)

### PRICE_TARGET_GBM#ETH#atexpiry
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
- **FILTRO** `sigma_h` < `0.0078` → IC=-0.191 (n=82)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=28)

- **FILTRO** `T_h` > `63.9918` → IC=-0.202 (n=82)

  - _Acción_: SKIP cuando `T_h` > 63.9918
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=65)

- **FILTRO** `pct_vs_K` |x|> `3.0033` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0033
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=59)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` < `87.9808` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `T_h` < 87.9808
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

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
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=224)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `streak_estiramiento` < 0.4576 (IC base=+0.024)

- **PATRÓN** `streak_estiramiento` < `0.5545` → IC=+0.149 (n=92)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.5545 (IC base=+0.030)

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
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=545)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=551)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=303)

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
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=464)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=939)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=552)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=576)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2354)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=1207)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1215)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.184 (n=365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.004 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.199 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0072 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.0529` → IC=+0.178 (n=365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0529 (IC base=+0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0587` → IC=+0.174 (n=1092)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.0587 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1332` → IC=+0.222 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1332 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.177 (n=447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 16.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.62` → IC=+0.244 (n=1092)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.62 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.176 (n=729)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.798` → IC=+0.240 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.798 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2633.3465` → IC=+0.176 (n=976)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2633.3465 (IC base=+0.172)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=367)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.213 (n=186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.192 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0049 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.258 (n=93)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.192)

- **PATRÓN** `drift_15min` |x|≤ `0.3762` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3762 (IC base=+0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.252` → IC=+0.202 (n=92)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.252 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1492` → IC=+0.247 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1492 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.206 (n=287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.7746` → IC=+0.263 (n=247)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7746 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.3848` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3848 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.1` → IC=+0.192 (n=193)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.1 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.472` → IC=+0.255 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.472 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `15082.5609` → IC=+0.223 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15082.5609 (IC base=+0.192)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `20.029` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 20.029 (IC base=-0.004)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.181 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0033 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.138 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.139 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.138)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.165 (n=177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.138)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2725` → IC=+0.169 (n=173)

  - _Acción_: Kelly boost +0.84€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2725 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.161 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_15` > `0.6485` → IC=+0.224 (n=266)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6485 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1433` → IC=+0.164 (n=212)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1433 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.212 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.138)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=53)

- **FILTRO** `ibs_15` > `0.1983` → IC=-0.250 (n=26)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1983
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=51)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `ibs_15` < `0.5926` → IC=-0.173 (n=50)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5926
  - _Potencial_: sin este filtro IC_bueno=+0.240 (n=152)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.190 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0077 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.1757` → IC=+0.162 (n=152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1757 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0657` → IC=+0.174 (n=136)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.0657 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.204 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.170 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.5926` → IC=+0.240 (n=152)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5926 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.213` → IC=+0.153 (n=148)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.213 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.532` → IC=+0.371 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.532 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=125)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3002.1997` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3002.1997 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 34.0 (IC base=+0.137)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5758` → IC=-0.147 (n=117)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5758
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=605)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `13.183` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.183 (IC base=+0.027)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.251 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.198 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.183)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0648` → IC=+0.193 (n=278)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0648 (IC base=+0.183)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.183)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.273 (n=311)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.1729` → IC=+0.205 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1729 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.55` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.55 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.182 (n=338)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.03 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2726.373` → IC=+0.234 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2726.373 (IC base=+0.183)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.178 (n=349)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` < 0.1111 (IC base=+0.050)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.336 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.332)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.376 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.339 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.332)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1435` → IC=+0.344 (n=210)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1435 (IC base=+0.332)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2203` → IC=+0.373 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2203 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.348 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.332)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.374 (n=315)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` > `0.4129` → IC=+0.374 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4129 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.333 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.332 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.332)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `3480.6224` → IC=+0.345 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3480.6224 (IC base=+0.332)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1211` → IC=+0.338 (n=78)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1211 (IC base=+0.331)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.329 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.331)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.369 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.342 (n=156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1476` → IC=+0.342 (n=118)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1476 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.411 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.344 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.366 (n=177)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` > `0.242` → IC=+0.389 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.242 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.597` → IC=+0.345 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.597 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `9173.8264` → IC=+0.342 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9173.8264 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `478.0` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 478.0 (IC base=+0.331)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.361 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.333 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.337 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3017` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3017 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.349 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.387 (n=139)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.337 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` < `0.0995` → IC=+0.347 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0995 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.588` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.588 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.327 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.329)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.346 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `3558.8831` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3558.8831 (IC base=+0.329)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0125` → IC=-0.202 (n=538)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0125
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1616)

- **FILTRO** `ibs_15` < `0.6078` → IC=-0.170 (n=180)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6078
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=542)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.174 (n=680)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1474)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2875` → IC=+0.224 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2875 (IC base=-0.058)

- **PATRÓN** `ibs_15` > `0.6078` → IC=+0.250 (n=542)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6078 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` < `0.2658` → IC=+0.175 (n=429)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.2658 (IC base=-0.058)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2103` → IC=+0.240 (n=382)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2103 (IC base=-0.044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1819` → IC=+0.238 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1819 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3571` → IC=+0.279 (n=1145)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3571 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.6579` → IC=+0.269 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6579 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.208 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=972)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.227 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=868)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.207 (n=825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=470)

- **FILTRO** `sigma_ewma_delta_pct` > `19.873` → IC=-0.244 (n=232)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.873
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1063)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.170 (n=113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0026 (IC base=+0.071)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1156` → IC=+0.305 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1156 (IC base=+0.071)

- **PATRÓN** `ibs_15` > `0.8098` → IC=+0.330 (n=110)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8098 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.3434` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3434 (IC base=+0.071)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6526` → IC=-0.230 (n=87)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6526
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=264)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=334)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.135 (n=264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0065 (IC base=+0.132)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.160 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.004 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.212 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `0.4193` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `drift_15min` |x|≤ 0.4193 (IC base=+0.132)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.234 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.175 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.6526` → IC=+0.252 (n=264)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6526 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.179 (n=191)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.857` → IC=+0.139 (n=206)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 6.857 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=334)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.132)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.247 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.3563` → IC=+0.227 (n=427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3563 (IC base=+0.224)

- **PATRÓN** `drift_15min` |x|≤ `0.7675` → IC=+0.227 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7675 (IC base=+0.224)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2028` → IC=+0.257 (n=220)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2028 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.237 (n=325)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_15` < `0.3657` → IC=+0.268 (n=485)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3657 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.3791` → IC=+0.248 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3791 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.004` → IC=+0.236 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.004 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.182` → IC=+0.229 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.182 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3576.5439` → IC=+0.225 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3576.5439 (IC base=+0.224)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.185 (n=389)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=130)

- **FILTRO** `drift_60min` |x|> `0.1616` → IC=-0.208 (n=176)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1616
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=343)

- **FILTRO** `drift_15min` |x|> `0.8398` → IC=-0.233 (n=129)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8398
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=390)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0711` → IC=+0.209 (n=208)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0711 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.245 (n=233)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1738` → IC=+0.204 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1738 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0192` → IC=-0.257 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0192
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=324)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=174)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=473)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1081` → IC=+0.351 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1081 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.305 (n=337)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` > `1.1104` → IC=+0.419 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1104 (IC base=-0.045)

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
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.287 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.0567` → IC=+0.311 (n=178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0567 (IC base=+0.283)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1415` → IC=+0.286 (n=354)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1415 (IC base=+0.283)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2199` → IC=+0.317 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2199 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.299 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.283)

- **PATRÓN** `ibs_15` > `0.8348` → IC=+0.320 (n=531)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8348 (IC base=+0.283)

- **PATRÓN** `dist_vwap_pct` > `0.2686` → IC=+0.325 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2686 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.316 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `12684.1483` → IC=+0.294 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12684.1483 (IC base=+0.283)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.289 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.273)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.281 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.273)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.312 (n=99)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.273)

- **PATRÓN** `drift_15min` |x|≤ `0.3845` → IC=+0.282 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3845 (IC base=+0.273)

- **PATRÓN** `delta_ratio_macro` |x|> `0.246` → IC=+0.282 (n=99)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.246 (IC base=+0.273)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3796` → IC=+0.288 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3796 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.332 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.273)

- **PATRÓN** `ibs_15` > `0.965` → IC=+0.325 (n=135)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.965 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `0.2601` → IC=+0.337 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2601 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.336 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `12139.6` → IC=+0.290 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12139.6 (IC base=+0.273)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.310 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.302 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0035 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0504` → IC=+0.315 (n=79)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0504 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1458` → IC=+0.305 (n=157)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1458 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.338 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.320 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.335 (n=235)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.313 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.292 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.317 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.303 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.296 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.294)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.62 sube el IC de +0.172 a +0.244 en UPDOWN_GBM#15min (n=1092). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7746 sube el IC de +0.192 a +0.263 en UPDOWN_GBM#BTC#15min (n=247). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6485 sube el IC de +0.138 a +0.224 en UPDOWN_GBM#ETH#15min (n=266). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5926 sube el IC de +0.137 a +0.240 en UPDOWN_GBM#SOL#15min (n=152). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.183 a +0.273 en UPDOWN_GBM#XRP#15min (n=311). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.050 a +0.178 en UPDOWN_GBM#XRP#15min (n=349). Ya aplicado como kelly_boost=+0.89€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6078 sube el IC de -0.058 a +0.250 en UPDOWN_GBM_15M_TARDIO (n=542). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3571 sube el IC de -0.044 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1145). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.8098 sube el IC de +0.071 a +0.330 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=110). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6526 sube el IC de +0.132 a +0.252 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=264). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3657 sube el IC de +0.224 a +0.268 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=485). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.149 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.042 a +0.245 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=233). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.045 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=337). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8348 sube el IC de +0.283 a +0.320 en UPDOWN_GBM_IBS_ALTO (n=531). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.965 sube el IC de +0.273 a +0.325 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=135). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.294 a +0.335 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=235). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.332 a +0.374 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=315). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.331 a +0.366 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=177). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.329 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=139). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
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
| ✅ BALLENAS_TARDIAS | 20763 | -0.101 | -3000.18€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1252 | -0.045 | -180.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 19511 | -0.104 | -2819.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3190 | -0.115 | -556.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3190 | -0.115 | -556.31€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1252 | -0.045 | -180.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1252 | -0.045 | -180.96€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5960 | -0.045 | -586.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5960 | -0.045 | -586.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5527 | -0.110 | -473.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5527 | -0.110 | -473.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4460 | -0.166 | -1041.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4460 | -0.166 | -1041.56€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 12529 | -0.041 | +4225.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3362 | -0.007 | +1851.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 9167 | -0.054 | +2373.60€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 12529 | -0.041 | +4225.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3362 | -0.007 | +1851.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 9167 | -0.054 | +2373.60€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1030 | -0.108 | -156.34€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 72 | -0.095 | -15.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 958 | -0.108 | -140.71€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 590 | -0.088 | -78.52€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 48 | -0.100 | -10.40€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 542 | -0.086 | -68.12€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 292 | -0.150 | -62.57€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 268 | -0.156 | -57.34€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 87 | -0.073 | -15.11€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 87 | -0.073 | -15.11€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 39 | -0.159 | -4.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 75299 | +0.113 | -3869.30€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 11745 | +0.183 | -361.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 290 | -0.116 | -45.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 58082 | +0.100 | -3352.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5182 | +0.115 | -110.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 9678 | +0.097 | -891.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 38 | -0.150 | -1.48€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 9625 | +0.099 | -878.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 15220 | +0.132 | -308.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3598 | +0.201 | -115.13€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 9622 | +0.110 | -185.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1958 | +0.115 | +14.78€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 9717 | +0.089 | -942.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 45 | -0.053 | -1.73€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 9657 | +0.091 | -929.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 16117 | +0.125 | -298.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4533 | +0.172 | -75.47€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 9709 | +0.108 | -169.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1863 | +0.100 | -45.57€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 14875 | +0.115 | -854.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3493 | +0.186 | -178.15€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 193 | -0.074 | +8.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 9828 | +0.091 | -605.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1361 | +0.137 | -79.49€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 9692 | +0.103 | -573.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 38 | +0.000 | +10.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 9641 | +0.103 | -584.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 11899 | +0.189 | -823.09€ | 3 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 11899 | +0.189 | -823.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2920 | +0.167 | -318.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2920 | +0.167 | -318.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 658 | +0.183 | +5.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 658 | +0.183 | +5.40€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2863 | +0.177 | -267.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2863 | +0.177 | -267.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2571 | +0.237 | -76.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2571 | +0.237 | -76.81€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2808 | +0.191 | -179.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2808 | +0.191 | -179.62€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 551 | +0.431 | -13.06€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 551 | +0.431 | -13.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 211 | +0.434 | -3.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 211 | +0.434 | -3.04€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 210 | +0.439 | -0.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 210 | +0.439 | -0.43€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 122 | +0.403 | -8.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 122 | +0.403 | -8.55€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 40680 | +0.195 | -3389.38€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 40680 | +0.195 | -3389.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 7085 | +0.170 | -895.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 7085 | +0.170 | -895.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6456 | +0.223 | -239.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6456 | +0.223 | -239.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7046 | +0.169 | -895.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7046 | +0.169 | -895.00€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6549 | +0.218 | -272.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6549 | +0.218 | -272.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6710 | +0.203 | -455.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6710 | +0.203 | -455.15€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6834 | +0.191 | -631.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6834 | +0.191 | -631.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 15208 | +0.124 | +292.34€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 15208 | +0.124 | +292.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7543 | +0.129 | +206.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7543 | +0.129 | +206.10€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7665 | +0.119 | +86.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7665 | +0.119 | +86.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1247 | +0.287 | -26.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1247 | +0.287 | -26.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 552 | +0.273 | -20.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 552 | +0.273 | -20.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 596 | +0.291 | -4.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 596 | +0.291 | -4.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 99 | +0.332 | -1.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 99 | +0.332 | -1.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 550 | +0.431 | -7.39€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 550 | +0.431 | -7.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 258 | +0.431 | -3.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 258 | +0.431 | -3.78€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 253 | +0.433 | -3.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 253 | +0.433 | -3.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 39 | +0.378 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 39 | +0.378 | -0.28€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 866 | +0.066 | -49.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 310 | +0.048 | -31.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 556 | +0.075 | -18.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 54 | +0.125 | +3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 54 | +0.125 | +3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 674 | +0.075 | -22.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 118 | +0.075 | -4.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 556 | +0.075 | -18.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 138 | -0.007 | -30.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 138 | -0.007 | -30.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 26947 | +0.098 | -817.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2267 | +0.094 | +32.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 24680 | +0.099 | -850.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 15354 | +0.103 | -228.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2267 | +0.094 | +32.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 13087 | +0.104 | -261.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4712 | +0.115 | +33.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4712 | +0.115 | +33.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6881 | +0.077 | -622.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6881 | +0.077 | -622.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 724 | +0.251 | -92.55€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 724 | +0.251 | -92.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 724 | +0.251 | -92.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 724 | +0.251 | -92.55€ | 0 | 4 |
| ✅ GBM_LATE_15M | 19895 | +0.075 | +8925.33€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 19895 | +0.075 | +8925.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3264 | +0.194 | +2375.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3264 | +0.194 | +2375.21€ | 0 | 19 |
| ✅ GBM_LATE_15M#BTC | 2935 | +0.173 | +1945.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2935 | +0.173 | +1945.96€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 3407 | +0.194 | +2473.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3407 | +0.194 | +2473.75€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 2967 | +0.004 | +454.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2967 | +0.004 | +454.00€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 2924 | -0.037 | +638.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2924 | -0.037 | +638.40€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 4398 | -0.050 | +1038.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4398 | -0.050 | +1038.00€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 20968 | +0.077 | +10390.98€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 20968 | +0.077 | +10390.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3844 | +0.010 | +1940.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3844 | +0.010 | +1940.42€ | 2 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4425 | +0.005 | +833.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4425 | +0.005 | +833.36€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2972 | +0.255 | +2900.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2972 | +0.255 | +2900.18€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3296 | -0.017 | +405.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3296 | -0.017 | +405.61€ | 2 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3480 | +0.015 | +1235.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3480 | +0.015 | +1235.92€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2951 | +0.269 | +3075.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2951 | +0.269 | +3075.48€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 16173 | +0.169 | +11822.61€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 16173 | +0.169 | +11822.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2392 | +0.208 | +1908.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2392 | +0.208 | +1908.37€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2555 | +0.154 | +1836.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2555 | +0.154 | +1836.04€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2495 | +0.204 | +1940.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2495 | +0.204 | +1940.67€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2687 | +0.140 | +1807.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2687 | +0.140 | +1807.06€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3054 | +0.112 | +1970.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3054 | +0.112 | +1970.39€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2990 | +0.203 | +2360.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2990 | +0.203 | +2360.07€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4084 | +0.124 | +1624.26€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4084 | +0.124 | +1624.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 145 | +0.112 | +56.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 145 | +0.112 | +56.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1092 | +0.113 | +416.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1092 | +0.113 | +416.74€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1139 | +0.151 | +522.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1139 | +0.151 | +522.75€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 837 | +0.084 | +226.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 837 | +0.084 | +226.98€ | 0 | 10 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 19939 | +0.173 | +14367.29€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 19939 | +0.173 | +14367.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3117 | +0.220 | +2613.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3117 | +0.220 | +2613.90€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3124 | +0.151 | +2036.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3124 | +0.151 | +2036.70€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3230 | +0.220 | +2713.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3230 | +0.220 | +2713.05€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3178 | +0.137 | +2050.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3178 | +0.137 | +2050.24€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3508 | +0.106 | +2009.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3508 | +0.106 | +2009.77€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3782 | +0.203 | +2943.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3782 | +0.203 | +2943.64€ | 0 | 24 |
| ✅ GBM_LATE_5M | 5961 | +0.141 | +3243.90€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5961 | +0.141 | +3243.90€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 563 | +0.181 | +383.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1571 | +0.140 | +966.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1571 | +0.140 | +966.23€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1816 | +0.147 | +987.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1816 | +0.147 | +987.76€ | 0 | 30 |
| ✅ GBM_LATE_5M#SOL | 318 | +0.034 | +44.24€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 318 | +0.034 | +44.24€ | 2 | 5 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1267 | +0.065 | +502.94€ | 2 | 16 |
| ✅ GBM_LATE_60M#60min | 1267 | +0.065 | +502.94€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 448 | +0.091 | +173.92€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 448 | +0.091 | +173.92€ | 1 | 18 |
| ✅ GBM_LATE_60M#ETH | 424 | +0.070 | +201.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 424 | +0.070 | +201.16€ | 2 | 17 |
| ✅ GBM_LATE_60M#SOL | 395 | +0.029 | +127.86€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 395 | +0.029 | +127.86€ | 2 | 10 |
| 🚫 GBM_LATE_60M_FADE | 303 | -0.267 | -23.86€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 303 | -0.267 | -23.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 113 | -0.222 | -7.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 113 | -0.222 | -7.68€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 103 | -0.300 | -13.97€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 103 | -0.300 | -13.97€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 87 | -0.275 | -2.21€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 87 | -0.275 | -2.21€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 597 | +0.054 | +111.23€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 597 | +0.054 | +111.23€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 239 | +0.044 | +34.99€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 239 | +0.044 | +34.99€ | 4 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 174 | +0.040 | +7.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 174 | +0.040 | +7.11€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 184 | +0.081 | +69.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 184 | +0.081 | +69.13€ | 2 | 13 |
| ✅ LATE_WINDOW_5MIN | 66 | +0.250 | +42.94€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 66 | +0.250 | +42.94€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 66 | +0.250 | +42.94€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 66 | +0.250 | +42.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1405 | +0.105 | +408.94€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1405 | +0.105 | +408.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1405 | +0.105 | +408.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1405 | +0.105 | +408.94€ | 0 | 5 |
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
| ✅ LIQUIDACIONES_5M | 1534 | -0.005 | -8.91€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1534 | -0.005 | -8.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 168 | -0.018 | +2.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 168 | -0.018 | +2.40€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 624 | +0.021 | +14.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 624 | +0.021 | +14.67€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 460 | -0.006 | -8.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 460 | -0.006 | -8.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 105 | -0.061 | -6.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 105 | -0.061 | -6.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 907 | -0.048 | -27.98€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 907 | -0.048 | -27.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 264 | -0.053 | -14.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 264 | -0.053 | -14.59€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 290 | -0.038 | -5.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 290 | -0.038 | -5.01€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 353 | -0.052 | -8.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 353 | -0.052 | -8.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 13152 | -0.011 | -182.43€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 13152 | -0.011 | -182.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2423 | -0.023 | -49.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2423 | -0.023 | -49.26€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2561 | +0.008 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2681 | -0.016 | -21.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2681 | -0.016 | -21.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3230 | -0.017 | -60.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3230 | -0.017 | -60.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 22114 | -0.011 | +990.04€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 22114 | -0.011 | +990.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3839 | +0.010 | +500.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3839 | +0.010 | +500.08€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3575 | -0.025 | -21.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3575 | -0.025 | -21.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3861 | +0.004 | +312.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3861 | +0.004 | +312.19€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3350 | -0.045 | -94.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3350 | -0.045 | -94.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3698 | -0.015 | +157.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3698 | -0.015 | +157.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3791 | -0.001 | +136.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3791 | -0.001 | +136.63€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4966 | -0.039 | -112.81€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4966 | -0.039 | -112.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1201 | +0.000 | -16.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1065 | -0.046 | -21.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1065 | -0.046 | -21.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 42 | -0.114 | -4.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 456 | -0.118 | -18.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 456 | -0.118 | -18.35€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1356 | -0.054 | -25.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1356 | -0.054 | -25.45€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 57296 | -0.073 | +1079.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 57296 | -0.073 | +1079.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 9627 | -0.082 | +538.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 9627 | -0.082 | +538.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 8944 | -0.088 | -340.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 8944 | -0.088 | -340.17€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 9664 | -0.072 | +442.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 9664 | -0.072 | +442.55€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 8465 | -0.092 | -224.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 8465 | -0.092 | -224.68€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 10623 | -0.048 | +329.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 10623 | -0.048 | +329.00€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 9973 | -0.064 | +334.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 9973 | -0.064 | +334.30€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6727 | -0.021 | -104.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6727 | -0.021 | -104.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1500 | -0.021 | -9.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1500 | -0.021 | -9.30€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1493 | -0.015 | -5.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1493 | -0.015 | -5.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 999 | -0.036 | -14.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 999 | -0.036 | -14.22€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 984 | +0.113 | +343.25€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 848 | +0.121 | +330.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 192 | +0.139 | +96.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 192 | +0.139 | +96.33€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 167 | +0.098 | +41.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 167 | +0.098 | +41.05€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 176 | +0.101 | +60.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 176 | +0.101 | +60.28€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 152 | +0.149 | +79.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 152 | +0.149 | +79.43€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 161 | +0.114 | +53.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 161 | +0.114 | +53.58€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 469 | -0.077 | -5.10€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 207 | -0.122 | -32.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 165 | -0.159 | -35.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 167 | -0.068 | +8.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 125 | -0.075 | +1.91€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 95 | +0.005 | +19.19€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 75 | -0.006 | +13.09€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 365 | -0.100 | -20.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 543 | -0.221 | -44.40€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 227 | -0.203 | -33.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 195 | -0.195 | -31.45€ | 4 | 0 |
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
| ✅ STREAK_FADE_15M | 392 | +0.028 | +9.43€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 392 | +0.028 | +9.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 174 | +0.023 | +0.46€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 174 | +0.023 | +0.46€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 25 | +0.093 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 45 | -0.011 | -3.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 45 | -0.011 | -3.64€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 148 | +0.033 | +9.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 148 | +0.033 | +9.32€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 2426 | -0.025 | -109.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2426 | -0.025 | -109.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 562 | -0.023 | -23.39€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 562 | -0.023 | -23.39€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 152 | -0.045 | -14.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 152 | -0.045 | -14.43€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 908 | -0.030 | -44.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 908 | -0.030 | -44.65€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 58 | -0.033 | -2.61€ | 2 | 1 |
| ✅ STREAK_FADE_60M#60min | 58 | -0.033 | -2.61€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 23 | +0.060 | +1.33€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 23 | +0.060 | +1.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6491 | +0.021 | +80.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6491 | +0.021 | +80.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2076 | +0.020 | +18.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2076 | +0.020 | +18.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1356 | +0.028 | +32.26€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1356 | +0.028 | +32.26€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1889 | +0.011 | +0.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1889 | +0.011 | +0.55€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1170 | +0.027 | +29.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1170 | +0.027 | +29.22€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5983 | +0.012 | -32.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5983 | +0.012 | -32.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2373 | +0.020 | +1.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2373 | +0.020 | +1.53€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2371 | +0.014 | -10.04€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2371 | +0.014 | -10.04€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1239 | -0.004 | -24.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1239 | -0.004 | -24.39€ | 2 | 0 |
| ✅ UPDOWN_GBM | 25795 | +0.029 | +1417.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 6896 | +0.058 | +1090.09€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 969 | +0.005 | +8.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 16273 | +0.023 | +320.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1551 | -0.003 | -4.97€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2254 | +0.070 | +213.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 273 | +0.122 | +84.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1962 | +0.064 | +129.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4640 | +0.031 | +303.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 843 | +0.080 | +189.22€ | 0 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 275 | +0.024 | +7.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2796 | +0.027 | +99.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 686 | +0.000 | +5.80€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 40 | -0.119 | +1.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3036 | +0.032 | +94.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 229 | +0.106 | +55.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2791 | +0.026 | +39.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 5289 | +0.015 | +205.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1900 | +0.045 | +206.63€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 262 | +0.008 | +8.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2537 | +0.001 | -4.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 555 | -0.008 | -8.21€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 35 | -0.149 | +3.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6677 | +0.017 | +158.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1849 | +0.024 | +107.49€ | 1 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 256 | -0.008 | -2.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4233 | +0.018 | +56.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 310 | +0.000 | -2.56€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 29 | -0.145 | -0.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3897 | +0.042 | +444.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1802 | +0.080 | +447.03€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 141 | -0.011 | -3.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1954 | +0.011 | +0.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 104 | -0.141 | +4.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 420 | +0.332 | +116.37€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 420 | +0.332 | +116.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 235 | +0.331 | +59.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 235 | +0.331 | +59.31€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 185 | +0.329 | +57.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 185 | +0.329 | +57.06€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 9092 | -0.048 | +1953.29€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 9092 | -0.048 | +1953.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 403 | -0.053 | +344.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 403 | -0.053 | +344.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1745 | -0.128 | +38.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1745 | -0.128 | +38.94€ | 4 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 997 | +0.192 | +555.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 997 | +0.192 | +555.25€ | 2 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2912 | -0.061 | +466.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2912 | -0.061 | +466.52€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2896 | -0.075 | +493.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2896 | -0.075 | +493.26€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 102 | +0.067 | +14.80€ | 0 | 7 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 102 | +0.067 | +14.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 102 | +0.067 | +14.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 102 | +0.067 | +14.80€ | 0 | 7 |
| ✅ UPDOWN_GBM_IBS_ALTO | 708 | +0.283 | +561.69€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 708 | +0.283 | +561.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 395 | +0.273 | +294.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 395 | +0.273 | +294.45€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 313 | +0.294 | +267.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 313 | +0.294 | +267.24€ | 0 | 12 |
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
  - _Estado_: IC=+0.028 n=360 — no justifica filtro, seguir monitorizando
  - _Datos_: n=360 IC=+0.028 PNL=+22.59€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 455 celda(s) pasan gate riguroso completo de 2050 evaluadas (n>=40) y 3015 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.024 < 0.08 — monitorear
  - _Datos_: n=1845 IC=+0.024 PNL=+106.48€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=697/15 IC=+0.295 PNL=+289.41€ | BTC: n=649/15 IC=+0.248 PNL=+102.66€ | SOL: n=599/15 IC=+0.375 PNL=+610.45€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.086 n=184/60 | contraria IC=+0.127 n=164 | gap=-0.041 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=245, boost estimado=+0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=555/40 IC=-0.008 PNL=-8.21€ | BTC#60min: n=686/40 IC=+0.000 PNL=+5.80€ | SOL#60min: n=310/40 IC=+0.000 PNL=-2.56€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.053 n=262908 | tras_1loss IC=+0.071 n=205558 | tras_2loss IC=+0.040 n=88018/40 | gap=+0.014 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.190 > 0.08 con n=266 PNL=+164.11€
  - _Datos_: n=266 IC=+0.190 PNL=+164.11€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.344 > 0.1 con n=1627 PNL=+993.03€
  - _Datos_: n=1627 IC=+0.344 PNL=+993.03€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=189 IC=+0.076 PNL=+25.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=189 IC=+0.076 PNL=+25.67€

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
  - _Estado_: n=1130 IC=-0.004 PNL=-14.10€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1130 IC=-0.004 PNL=-14.10€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=421 IC=+0.001 PNL=+9.12€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=421 IC=+0.001 PNL=+9.12€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=360 IC=+0.028 PNL=+22.59€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=360 IC=+0.028 PNL=+22.59€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.1 con n=1451 PNL=+819.83€
  - _Datos_: n=1451 IC=+0.172 PNL=+819.83€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=838 IC=+0.080 PNL=+189.19€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=838 IC=+0.080 PNL=+189.19€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.250 n=66) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=66 IC=+0.250 PNL=+42.94€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.02 con n=566 PNL=+229.08€
  - _Datos_: n=566 IC=+0.129 PNL=+229.08€

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
  - _Estado_: n=8365 IC=+0.049 PNL=+943.44€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=8365 IC=+0.049 PNL=+943.44€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.163 < -0.1 con n=158 PNL=+11.45€
  - _Datos_: n=158 IC=-0.163 PNL=+11.45€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1385 IC=+0.049 PNL=+164.24€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1385 IC=+0.049 PNL=+164.24€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.139 > 0.1 con n=258 PNL=+83.16€
  - _Datos_: n=258 IC=+0.139 PNL=+83.16€

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
  - _Estado_: n=13718 IC=-0.144 PNL=+599.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=13718 IC=-0.144 PNL=+599.79€

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
  - _Estado_: n=1516 IC=+0.138 PNL=+798.94€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1516 IC=+0.138 PNL=+798.94€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.243 < -0.1 con n=1382 PNL=-195.30€
  - _Datos_: n=1382 IC=-0.243 PNL=-195.30€

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
  - _Estado_: 27/40 ops en el filtro definido (IC actual=+0.017 PNL=+6.66€)
  - _Datos_: n=27 IC=+0.017 PNL=+6.66€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=733) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=733 IC=+0.101 PNL=+198.73€

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
  - _Estado_: n=7076 IC=+0.170 PNL=-893.25€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=7076 IC=+0.170 PNL=-893.25€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.220 > 0.1 con n=105 PNL=+68.10€
  - _Datos_: n=105 IC=+0.220 PNL=+68.10€
