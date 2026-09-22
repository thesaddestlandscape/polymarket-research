# Hipótesis automáticas — 2026-09-22 12:13 UTC
_Generado por shadow_postmortem.py sobre 556989 resoluciones (PNL=+62022.52€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=498)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=453)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.250 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `76.0` → IC=+0.208 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 76.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.804` → IC=+0.250 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.804 (IC base=+0.134)

- **PATRÓN** `banda_z` > `9.867` → IC=+0.223 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.867 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.142 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.134 (n=364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 11.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=562)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4759.1448` → IC=+0.144 (n=175)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4759.1448 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.256 (n=396)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=326)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.256 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.143)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.215 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.143)

- **PATRÓN** `banda_hit_calibrado` > `0.802` → IC=+0.262 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.802 (IC base=+0.143)

- **PATRÓN** `banda_z` > `10.841` → IC=+0.227 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.841 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=476)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 96.0 (IC base=+0.042)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
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

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.256 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.106)

- **PATRÓN** `banda_hit_calibrado` > `0.6274` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6274 (IC base=+0.106)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 6.043 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `1185.8848` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1185.8848 (IC base=+0.106)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.154)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.705` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballenas_wallet_edge_medio` > 0.705 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.154)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `146.06` → IC=-0.232 (n=6708)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.06
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=20124)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `140.57` → IC=-0.237 (n=891)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.57
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2674)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `495.95` → IC=-0.149 (n=354)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 495.95
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1062)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `134.5` → IC=-0.281 (n=823)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.5
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2471)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `162.9` → IC=-0.228 (n=1588)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 162.9
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4767)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `123.96` → IC=-0.362 (n=1333)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 123.96
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=4006)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.234 (n=348)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=402)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.178 (n=228)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=470)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=548)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.259 (n=164)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.218 (n=69)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=234)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.338 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=183)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.179 (n=76)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=152)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=158)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.201 (n=13316)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3338)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5535.0003` → IC=+0.174 (n=2127)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5535.0003 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.140 (n=10668)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=13109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.233 (n=10311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=5440)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7654.5864` → IC=+0.172 (n=2045)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7654.5864 (IC base=+0.128)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1603)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `15752.6972` → IC=+0.231 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15752.6972 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.264 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2044)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `13892.572` → IC=+0.208 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13892.572 (IC base=+0.199)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.183 (n=307)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.62 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `4624.034` → IC=+0.144 (n=234)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4624.034 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.143 (n=494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 11.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.148 (n=794)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.44 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=556)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `5871.1399` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5871.1399 (IC base=+0.111)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=2678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.144 (n=2294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.332 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.356 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.240 (n=1424)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.234)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.151 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.141 (n=566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.230 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=514)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `1302.4168` → IC=+0.151 (n=625)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1302.4168 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.431 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.171 (n=1042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 7.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.313 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.176 (n=709)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.166)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.165 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 13.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.743` → IC=+0.353 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.743 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=186)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `1271.2794` → IC=+0.156 (n=222)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1271.2794 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.201 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.116)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=10814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=10372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.224 (n=3675)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.184 (n=1835)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.71 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.270 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.253 (n=723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.253)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.358 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.253)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=2593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.189 (n=1125)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.73 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=2311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.318 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=2516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=2427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=1840)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=472)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.431 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.470 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `2062.8229` → IC=+0.437 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2062.8229 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.434 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.434 (n=194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.452 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.471 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.437 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `3355.2252` → IC=+0.444 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3355.2252 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.406 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.417 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.405 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `libro_liquidez` < `6836.9618` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 6836.9618
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=32011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.232 (n=17475)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=6525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=5538)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=5974)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=5740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=5743)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.277 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=5832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=5872)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=2869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.264 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=5297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.254 (n=2174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.205)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=2297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=5364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.251 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4930)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.14` → IC=+0.128 (n=4521)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.14 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.141 (n=4799)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.132 (n=5993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `3.11` → IC=+0.143 (n=4496)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 3.11 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=2487)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.09` → IC=+0.132 (n=2242)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` < 4.09 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.140 (n=2373)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=2957)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.47` → IC=+0.146 (n=2231)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.47 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=2443)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.18` → IC=+0.126 (n=2275)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.18 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=2427)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.33` → IC=+0.141 (n=2270)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1569.8406` → IC=+0.297 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1569.8406 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.299 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.340 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `4200.4566` → IC=+0.297 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4200.4566 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.336 (n=357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.298)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.386 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `1466.4356` → IC=+0.315 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1466.4356 (IC base=+0.298)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.347 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.340)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.363 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.340)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.340)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.445 (n=416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `1834.428` → IC=+0.440 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1834.428 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.447 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.446 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `2031.364` → IC=+0.460 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2031.364 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.381)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `4.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=46)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

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
- **FILTRO** `hora_utc` < `4.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=46)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4733` → IC=+0.120 (n=7537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.4733 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.9825` → IC=+0.242 (n=2512)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9825 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.8271` → IC=+0.248 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8271 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.2185` → IC=+0.247 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2185 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.927` → IC=+0.178 (n=2910)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.927 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` > `1.0513` → IC=+0.254 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0513 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.3055` → IC=+0.213 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3055 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` > `1.911` → IC=+0.206 (n=3421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.911 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.5706` → IC=+0.132 (n=9098)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5706 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.5913` → IC=+0.191 (n=683)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.5913 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.1466` → IC=+0.172 (n=2832)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1466 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` < `0.6976` → IC=+0.175 (n=1382)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6976 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` > `0.8683` → IC=+0.174 (n=2093)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.8683 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.1678` → IC=+0.220 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1678 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` > `1.5772` → IC=+0.200 (n=4680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5772 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.210 (n=5020)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=+0.063)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.179 (n=571)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0051 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.172 (n=571)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0082 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3452` → IC=+0.165 (n=1710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3452 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=824)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1154)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.116` → IC=+0.272 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.116 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.209 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.165 (n=1595)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.255 (n=573)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.290 (n=421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.062` → IC=+0.297 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.062 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.381` → IC=+0.250 (n=1318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.381 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0914` → IC=+0.233 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0914 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.263 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.247 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1784.3481` → IC=+0.243 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1784.3481 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.236 (n=574)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.086` → IC=+0.248 (n=435)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.086 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=1368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9918` → IC=+0.266 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9918 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.220 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1948 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.5771` → IC=+0.216 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5771 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.856` → IC=+0.252 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.856 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.217 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.0825` → IC=+0.223 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0825 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.229 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.4005` → IC=+0.221 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4005 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.3672` → IC=+0.221 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3672 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `16510.6932` → IC=+0.225 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16510.6932 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.175 (n=453)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.156 (n=451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=613)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6846` → IC=+0.168 (n=1352)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6846 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1267` → IC=+0.158 (n=1205)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1267 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.209` → IC=+0.161 (n=219)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.209 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.206` → IC=+0.140 (n=1229)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 4.206 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.148 (n=1352)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2046 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8501` → IC=+0.138 (n=901)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8501 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.178 (n=364)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.149 (n=1242)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.147 (n=828)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `411.0` → IC=+0.147 (n=1159)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 411.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.217 (n=557)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=1751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1493)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.107` → IC=+0.254 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.107 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.2114` → IC=+0.191 (n=1653)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.2114 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.3632` → IC=+0.197 (n=219)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3632 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.8852` → IC=+0.205 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8852 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.197 (n=1150)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.224 (n=1420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.217 (n=673)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.0636` → IC=+0.242 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0636 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.693` → IC=+0.238 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.693 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.267 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.8783` → IC=+0.228 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8783 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `1863.0764` → IC=+0.228 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1863.0764 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.218 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.216)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.153 (n=93)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2093)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.207 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.3625` → IC=+0.320 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3625 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.7769` → IC=+0.326 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7769 (IC base=+0.021)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.666` → IC=+0.152 (n=668)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 4.666 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.6681` → IC=+0.330 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6681 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.335 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1961 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.1771` → IC=+0.316 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1771 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4007` → IC=+0.330 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4007 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.321 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.329 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6662` → IC=+0.195 (n=139)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6662 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.157 (n=511)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8509 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.220 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `1.5133` → IC=+0.176 (n=637)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5133 (IC base=+0.013)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.155 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=301)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.192 (n=89)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=268)

- **FILTRO** `ibs_20min` > `0.2581` → IC=-0.125 (n=2072)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2581
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=1022)

- **FILTRO** `sigma_ewma_delta_pct` > `8.654` → IC=-0.204 (n=333)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.654
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2761)

- **PATRÓN** `ibs_20min` > `0.7647` → IC=+0.226 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7647 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.357 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.5682` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5682 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` > `0.7744` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7744 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` < `0.0747` → IC=+0.309 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0747 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `2.2264` → IC=+0.289 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2264 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.292 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.2581` → IC=+0.123 (n=1022)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2581 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` > `0.684` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.684 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` < `0.4425` → IC=+0.205 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4425 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` < `1.096` → IC=+0.220 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.096 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` > `0.9027` → IC=+0.207 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9027 (IC base=-0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1038` → IC=+0.222 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1038 (IC base=-0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.250 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.456` → IC=+0.257 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.456 (IC base=-0.043)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6434` → IC=-0.182 (n=524)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6434
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1580)

- **FILTRO** `ibs_20min` < `0.6993` → IC=-0.156 (n=1388)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6993
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=716)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.198 (n=398)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1706)

- **FILTRO** `ibs_20min` > `0.7736` → IC=-0.204 (n=781)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7736
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2346)

- **PATRÓN** `dist_vwap_pct` > `0.7356` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7356 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2585` → IC=+0.319 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2585 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.304 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.302 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.5359` → IC=+0.300 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5359 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `2.1203` → IC=+0.291 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1203 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `1.0599` → IC=+0.274 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0599 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.7389` → IC=+0.243 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7389 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.0811` → IC=+0.291 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0811 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1035` → IC=+0.275 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1035 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.248 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.4511` → IC=+0.246 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4511 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.197 (n=3149)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0097 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.187 (n=8426)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4706 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.7447` → IC=+0.288 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7447 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.662` → IC=+0.152 (n=4931)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.662 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6849` → IC=+0.244 (n=2973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6849 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2972` → IC=+0.264 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2972 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4704` → IC=+0.238 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4704 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6893` → IC=+0.235 (n=1805)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6893 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.267 (n=4926)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.147 (n=3157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.009 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.5502` → IC=+0.151 (n=8332)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5502 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.2431` → IC=+0.239 (n=2592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2431 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.238 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7129 (IC base=+0.071)

- **PATRÓN** `volumen_regimen` > `1.2028` → IC=+0.246 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2028 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2466` → IC=+0.303 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2466 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.6127` → IC=+0.255 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6127 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` > `2.3312` → IC=+0.258 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3312 (IC base=+0.071)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.262 (n=3465)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.071)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2593` → IC=-0.143 (n=648)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2593
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1946)

- **FILTRO** `sigma_ewma_delta_pct` > `4.494` → IC=-0.168 (n=501)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.494
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1689)

- **PATRÓN** `ibs_20min` > `0.8916` → IC=+0.263 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8916 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.299` → IC=+0.164 (n=891)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.299 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2239` → IC=+0.270 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2239 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4401` → IC=+0.175 (n=275)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4401 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.188 (n=373)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.173 (n=362)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 15.0 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8136` → IC=-0.149 (n=682)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8136
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=2048)

- **PATRÓN** `ibs_20min` > `0.862` → IC=+0.158 (n=633)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.862 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.3003` → IC=+0.169 (n=354)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.3003 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6622` → IC=+0.157 (n=773)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6622 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.214 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.197 (n=282)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `249.0` → IC=+0.188 (n=367)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 249.0 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.155` → IC=+0.217 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.155 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6059` → IC=+0.211 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6059 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.0728` → IC=+0.209 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0728 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.300 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.4573` → IC=+0.225 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4573 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.228 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=+0.002)

- **PATRÓN** `ballena_activa_n` < `481.0` → IC=+0.215 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 481.0 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.286 (n=677)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.251 (n=994)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.678` → IC=+0.284 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.678 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1382` → IC=+0.257 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1382 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `3.4725` → IC=+0.262 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4725 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.256 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1930.62` → IC=+0.252 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.62 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.318 (n=537)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1657` → IC=+0.284 (n=521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1657 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.327 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.2248` → IC=+0.289 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2248 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.816` → IC=+0.300 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.816 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.3431` → IC=+0.310 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3431 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.6052` → IC=+0.288 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6052 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.7879` → IC=+0.287 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7879 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.291 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1857.5432` → IC=+0.303 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1857.5432 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.290 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2789` → IC=-0.191 (n=457)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2789
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=1372)

- **FILTRO** `ibs_20min` > `0.7785` → IC=-0.181 (n=559)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7785
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1679)

- **PATRÓN** `ibs_20min` > `0.8076` → IC=+0.155 (n=622)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.8076 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.4602` → IC=+0.222 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4602 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.9865` → IC=+0.231 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9865 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `0.5819` → IC=+0.204 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5819 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.0791` → IC=+0.255 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0791 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.4982` → IC=+0.251 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4982 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.253 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.1547` → IC=+0.197 (n=196)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1547 (IC base=-0.007)

- **PATRÓN** `dist_vwap_pct` < `0.6607` → IC=+0.188 (n=424)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.6607 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.1607` → IC=+0.201 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1607 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8269` → IC=+0.247 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8269 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.1389` → IC=+0.247 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1389 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.237 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7143` → IC=-0.203 (n=998)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=+0.275 (n=1000)

- **FILTRO** `ibs_20min` > `0.6901` → IC=-0.229 (n=525)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6901
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1577)

- **FILTRO** `sigma_ewma_delta_pct` > `4.677` → IC=-0.178 (n=461)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.677
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=1641)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.275 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7143 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` > `0.8456` → IC=+0.341 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8456 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.526` → IC=+0.160 (n=316)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.526 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.8648` → IC=+0.297 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8648 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` > `0.639` → IC=+0.288 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.639 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1034` → IC=+0.291 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1034 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.294 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.319 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.310 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.1` → IC=+0.209 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.224 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.263 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.211 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.069` → IC=+0.207 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.069 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.5012` → IC=+0.222 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5012 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.241 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.318 (n=818)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.294 (n=577)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` > `0.7398` → IC=+0.323 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7398 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.1979` → IC=+0.319 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1979 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.487` → IC=+0.303 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.487 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` > `0.8624` → IC=+0.304 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8624 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.320 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.5155` → IC=+0.289 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5155 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.283 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2612.836` → IC=+0.289 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2612.836 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.296 (n=894)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.276 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.272 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.3966` → IC=+0.303 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3966 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.288` → IC=+0.277 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.288 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.9274` → IC=+0.270 (n=1508)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9274 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.981` → IC=+0.292 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.981 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `1.241` → IC=+0.313 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.241 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.336 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.543` → IC=+0.265 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.543 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.167` → IC=+0.274 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.167 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `2601.8214` → IC=+0.275 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2601.8214 (IC base=+0.269)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.169 (n=2482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.206 (n=2472)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0899` → IC=+0.183 (n=2474)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0899 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=7741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.5785` → IC=+0.217 (n=7413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5785 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1732` → IC=+0.195 (n=3258)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1732 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.257` → IC=+0.259 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.257 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.160 (n=4909)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2177 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.160 (n=4909)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6279 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.246` → IC=+0.195 (n=1493)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.246 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5625` → IC=+0.171 (n=3122)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5625 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6293` → IC=+0.175 (n=2365)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6293 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2393.5592` → IC=+0.169 (n=4942)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2393.5592 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.182 (n=6321)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 117.0 (IC base=+0.168)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.181 (n=4701)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.205 (n=2350)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=2733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.4773` → IC=+0.226 (n=7047)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4773 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.228` → IC=+0.159 (n=5111)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.228 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.239` → IC=+0.193 (n=1195)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.239 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.150 (n=5125)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.174 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.221 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5695` → IC=+0.164 (n=2804)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5695 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.2639` → IC=+0.170 (n=2889)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2639 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `118.0` → IC=+0.172 (n=6007)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 118.0 (IC base=+0.167)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.218 (n=423)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.187 (n=423)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0083 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3413` → IC=+0.205 (n=1267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3413 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=850)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.107` → IC=+0.313 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.107 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.235 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4355` → IC=+0.181 (n=1168)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4355 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.239 (n=795)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.245 (n=602)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1842` → IC=+0.295 (n=603)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1842 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=451)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3427` → IC=+0.266 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3427 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.095` → IC=+0.253 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.095 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.239 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.254 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `2.2616` → IC=+0.247 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2616 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1946.84` → IC=+0.256 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1946.84 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.244 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.201 (n=369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=1164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.4088` → IC=+0.226 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4088 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.2067` → IC=+0.215 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2067 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.523` → IC=+0.238 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.523 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.163 (n=1105)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2653 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `0.879` → IC=+0.165 (n=736)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.879 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2325` → IC=+0.201 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2325 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4125` → IC=+0.194 (n=357)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4125 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `15821.8878` → IC=+0.170 (n=501)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 15821.8878 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.195 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0025 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.29` → IC=+0.156 (n=1199)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.29 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.5583` → IC=+0.183 (n=1200)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5583 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.133` → IC=+0.163 (n=1190)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.133 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.828` → IC=+0.213 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.828 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.153 (n=1199)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2116 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1573` → IC=+0.160 (n=368)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1573 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.143 (n=1088)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.165 (n=335)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 217.0 (IC base=+0.136)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.234 (n=563)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.2221` → IC=+0.217 (n=825)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2221 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.325` → IC=+0.290 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.325 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.2101` → IC=+0.200 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2101 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.201 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.8935` → IC=+0.209 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8935 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=852)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `1931.801` → IC=+0.208 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.801 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.236 (n=1018)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0942` → IC=+0.257 (n=339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0942 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.2462` → IC=+0.258 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2462 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.703` → IC=+0.271 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.703 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3589` → IC=+0.269 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3589 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.6112` → IC=+0.221 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6112 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.2259` → IC=+0.227 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2259 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1866.4384` → IC=+0.224 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1866.4384 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.224 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.174 (n=1043)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0067 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.160 (n=1185)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3868` → IC=+0.198 (n=1185)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3868 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1571` → IC=+0.180 (n=797)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1571 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.233 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0471` → IC=+0.149 (n=1043)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0471 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6318` → IC=+0.150 (n=1185)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6318 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2921` → IC=+0.208 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2921 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5364` → IC=+0.148 (n=510)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5364 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5292` → IC=+0.173 (n=387)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.5292 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `6960.2205` → IC=+0.186 (n=790)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 6960.2205 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.147 (n=1123)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 166.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.155 (n=1242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.141 (n=1242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.181 (n=415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 18.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.622` → IC=+0.169 (n=1242)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.622 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.1585` → IC=+0.142 (n=1197)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1585 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.869` → IC=+0.174 (n=437)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 6.869 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8475` → IC=+0.145 (n=828)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8475 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.200 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7891` → IC=+0.130 (n=749)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.7891 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `9988.1936` → IC=+0.160 (n=563)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 9988.1936 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **FILTRO** `ibs_20min` > `0.5676` → IC=-0.183 (n=452)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5676
  - _Potencial_: sin este filtro IC_bueno=+0.207 (n=1358)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.157 (n=608)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5172` → IC=+0.201 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5172 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.8396` → IC=+0.215 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8396 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.609` → IC=+0.254 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.609 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.2249` → IC=+0.130 (n=1342)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2249 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4817` → IC=+0.128 (n=1294)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.4817 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1398)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2895.2022` → IC=+0.197 (n=608)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2895.2022 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.136 (n=1022)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 50.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.148 (n=601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0061 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.1033` → IC=+0.146 (n=453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1033 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.5676` → IC=+0.207 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5676 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.9777` → IC=+0.139 (n=189)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.9777 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.196` → IC=+0.135 (n=1239)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.196 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.445` → IC=+0.144 (n=282)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 7.445 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `1.0382` → IC=+0.122 (n=1195)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0382 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `3081.0348` → IC=+0.155 (n=453)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3081.0348 (IC base=+0.110)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0187` → IC=+0.215 (n=853)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0187 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.203 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7367` → IC=+0.260 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7367 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.2847` → IC=+0.237 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2847 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.496` → IC=+0.248 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.496 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2103` → IC=+0.205 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2103 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6195` → IC=+0.213 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6195 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.234` → IC=+0.269 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.234 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1554` → IC=+0.214 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1554 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.8029` → IC=+0.209 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8029 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2785.0379` → IC=+0.207 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2785.0379 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.235 (n=443)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.212 (n=602)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.220 (n=444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.247 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.1311` → IC=+0.225 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1311 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.2677` → IC=+0.203 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2677 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.247 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6303` → IC=+0.216 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6303 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.286 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4476` → IC=+0.198 (n=1188)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4476 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2571.095` → IC=+0.207 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2571.095 (IC base=+0.203)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.156 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0044 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.176 (n=576)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0089 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.152 (n=762)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.5514` → IC=+0.188 (n=1544)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5514 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.3876` → IC=+0.187 (n=528)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3876 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.703` → IC=+0.176 (n=803)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.703 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8743` → IC=+0.162 (n=1003)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8743 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.701` → IC=+0.149 (n=1344)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.701 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.176 (n=477)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.164 (n=554)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5517` → IC=+0.164 (n=554)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5517 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=1947)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.145 (n=1544)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.167 (n=515)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 21.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.128 (n=1208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0057 (IC base=+0.100)

- **PATRÓN** `ibs_20min` < `0.6569` → IC=+0.132 (n=1808)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6569 (IC base=+0.100)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3382` → IC=+0.121 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.3382 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.146 (n=411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 8.0 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.6665` → IC=+0.181 (n=290)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.6665 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.5024` → IC=+0.161 (n=107)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.5024 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.291` → IC=+0.126 (n=196)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 3.291 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `0.6135` → IC=+0.142 (n=146)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6135 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `12391.64` → IC=+0.132 (n=389)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 12391.64 (IC base=+0.101)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.206 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3387` → IC=+0.145 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3387 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.142 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.129 (n=594)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6012` → IC=+0.176 (n=507)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6012 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.2947` → IC=+0.151 (n=612)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.2947 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.149 (n=223)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0712` → IC=+0.162 (n=261)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0712 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.1609` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1609 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.1165` → IC=+0.148 (n=498)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1165 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.137 (n=566)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `390.0` → IC=+0.137 (n=544)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 390.0 (IC base=+0.128)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.264 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.213 (n=172)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.224 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.7017` → IC=+0.257 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7017 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.3897` → IC=+0.233 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3897 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.015` → IC=+0.236 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.015 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.8422` → IC=+0.210 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8422 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.1544` → IC=+0.218 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1544 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2555` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2555 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.3845` → IC=+0.243 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3845 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.4105` → IC=+0.248 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4105 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.0789` → IC=+0.165 (n=159)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.0789 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.4188` → IC=-0.129 (n=165)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4188
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=321)

- **FILTRO** `dist_vwap_pct` > `0.3337` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3337
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=451)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.167 (n=172)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0089 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.156 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 8.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.228 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.210 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.202 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.136 (n=333)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.0699 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.7268` → IC=+0.141 (n=338)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7268 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.2097` → IC=+0.161 (n=163)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.2097 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=412)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3064.7088` → IC=+0.203 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3064.7088 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 18.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.4188` → IC=+0.159 (n=321)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.4188 (IC base=+0.061)

- **PATRÓN** `volumen_spike_ratio` < `1.5976` → IC=+0.158 (n=150)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5976 (IC base=+0.061)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.182 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0068 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.189 (n=178)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6778` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6778 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.2547` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2547 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.155 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0091 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.178` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.178 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.576` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.576 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8853` → IC=+0.128 (n=135)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8853 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.136 (n=201)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6515 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.130 (n=179)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.6848` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.6848 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.122)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.206 (n=3147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=9847)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.4715` → IC=+0.215 (n=9432)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4715 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9501` → IC=+0.207 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9501 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.228 (n=4586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.882` → IC=+0.165 (n=4207)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.882 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.202 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.188 (n=3017)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2338.0825` → IC=+0.170 (n=6288)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2338.0825 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.194 (n=7090)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 88.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.187 (n=7521)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0092 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.4895` → IC=+0.183 (n=8539)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4895 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=3239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5644` → IC=+0.237 (n=8539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5644 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.2424` → IC=+0.161 (n=5285)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2424 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.923` → IC=+0.198 (n=1199)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.923 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.714` → IC=+0.182 (n=8282)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.714 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.7039` → IC=+0.159 (n=2596)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7039 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.2031` → IC=+0.154 (n=1967)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2031 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.240 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6379` → IC=+0.192 (n=2599)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6379 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.190 (n=4943)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 48.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.207 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.217 (n=539)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.188 (n=1606)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.198 (n=1093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.319 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.992` → IC=+0.310 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.992 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.252 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.5831` → IC=+0.204 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5831 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.259 (n=1232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.261 (n=559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1277` → IC=+0.289 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1277 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=1126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.290 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.456` → IC=+0.266 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.456 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.290 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `1.8682` → IC=+0.275 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8682 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.259 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1782.98` → IC=+0.270 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1782.98 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.194 (n=507)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0028 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0845` → IC=+0.161 (n=505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0845 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=1583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.3136` → IC=+0.200 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3136 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1284` → IC=+0.182 (n=867)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1284 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.74` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.74 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.234` → IC=+0.150 (n=1358)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.234 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.175 (n=505)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6267 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.2686` → IC=+0.203 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2686 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.1148` → IC=+0.159 (n=1285)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1148 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7583` → IC=+0.153 (n=973)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7583 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `478.0` → IC=+0.154 (n=1390)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 478.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3218` → IC=+0.160 (n=1305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3218 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.171 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.267` → IC=+0.234 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.267 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.168 (n=1179)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.186` → IC=+0.157 (n=628)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.186 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.161 (n=1305)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1894 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.199 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.159 (n=1207)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.1039` → IC=+0.161 (n=547)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1039 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `428.0` → IC=+0.157 (n=979)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 428.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.246 (n=506)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=1590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.6723` → IC=+0.258 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6723 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.783` → IC=+0.295 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.783 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2118` → IC=+0.223 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2118 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8789` → IC=+0.242 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8789 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.230 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1934.9386` → IC=+0.221 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1934.9386 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.233 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.241 (n=1410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.237 (n=944)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1619` → IC=+0.243 (n=621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1619 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.237 (n=675)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.196` → IC=+0.282 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.196 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.746` → IC=+0.280 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.746 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3456` → IC=+0.287 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3456 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7668` → IC=+0.236 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7668 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2018` → IC=+0.238 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2018 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1865.0432` → IC=+0.249 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1865.0432 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.251 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.235)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.183 (n=538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.143 (n=1609)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=1684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.8784` → IC=+0.261 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8784 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3695` → IC=+0.168 (n=648)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.3695 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.201` → IC=+0.163 (n=669)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.201 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8781` → IC=+0.158 (n=1073)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8781 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.224 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5155` → IC=+0.147 (n=684)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5155 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.138` → IC=+0.153 (n=705)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.138 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8147.128` → IC=+0.229 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8147.128 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.155 (n=494)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 80.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.156 (n=1309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4454` → IC=+0.154 (n=1308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4454 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.142 (n=599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.693` → IC=+0.185 (n=1308)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.693 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.8089` → IC=+0.141 (n=1508)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.8089 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.14` → IC=+0.177 (n=193)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.14 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8589` → IC=+0.145 (n=872)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8589 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1774` → IC=+0.148 (n=436)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1774 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4421` → IC=+0.151 (n=1236)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4421 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `10997.1346` → IC=+0.210 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10997.1346 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `181.0` → IC=+0.142 (n=1232)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 181.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.135 (n=1064)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0081 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=597)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.188 (n=1598)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4706 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `1.0762` → IC=+0.200 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0762 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.442` → IC=+0.236 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.442 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.8926` → IC=+0.134 (n=1063)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8926 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=1603)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2909.4755` → IC=+0.247 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2909.4755 (IC base=+0.108)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.127 (n=1396)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 62.0 (IC base=+0.108)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.174 (n=525)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0057 (IC base=+0.111)

- **PATRÓN** `drift_60min` |x|≤ `0.1303` → IC=+0.157 (n=523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1303 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.146 (n=724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 15.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.204 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.129 (n=1267)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.451` → IC=+0.125 (n=1516)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.451 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.72` → IC=+0.153 (n=690)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.72 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.169 (n=240)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.4547` → IC=+0.140 (n=470)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4547 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` > `2.5274` → IC=+0.129 (n=470)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5274 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2859.0238` → IC=+0.167 (n=523)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2859.0238 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0192` → IC=+0.218 (n=1063)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0192 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.209 (n=1430)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.5143` → IC=+0.249 (n=1595)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5143 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.8711` → IC=+0.244 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8711 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.504` → IC=+0.253 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.504 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.6356` → IC=+0.216 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6356 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.247 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.517` → IC=+0.239 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.517 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2607.8846` → IC=+0.217 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2607.8846 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.223 (n=575)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.217 (n=575)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.206 (n=1209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.5207` → IC=+0.253 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5207 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.8705` → IC=+0.202 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8705 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.724` → IC=+0.263 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.724 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.2318` → IC=+0.238 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2318 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.261 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.2118` → IC=+0.191 (n=1354)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2118 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4369` → IC=+0.197 (n=1538)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4369 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.137 (n=2868)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.157 (n=2428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0093 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.150 (n=2468)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0056 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.5252` → IC=+0.159 (n=2758)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.5252 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.210 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1908` → IC=+0.157 (n=991)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1908 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `1.1467` → IC=+0.140 (n=1952)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 1.1467 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.14` → IC=+0.181 (n=450)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.14 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.902` → IC=+0.161 (n=1165)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.902 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1727` → IC=+0.183 (n=755)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1727 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4575` → IC=+0.156 (n=909)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4575 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.8888` → IC=+0.161 (n=1817)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8888 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3665.3765` → IC=+0.152 (n=1839)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3665.3765 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.193 (n=725)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4865` → IC=+0.154 (n=2163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4865 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.164 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 4.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.184` → IC=+0.164 (n=952)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.184 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.9213` → IC=+0.148 (n=339)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.9213 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2469` → IC=+0.129 (n=1928)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.2469 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.212` → IC=+0.143 (n=2152)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.212 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.9014` → IC=+0.151 (n=1374)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.9014 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.145 (n=1006)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4285` → IC=+0.145 (n=713)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4285 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.8136` → IC=+0.141 (n=1425)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8136 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=2868)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7059.7056` → IC=+0.150 (n=1932)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 7059.7056 (IC base=+0.135)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.163 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0056 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.162 (n=323)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0033 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0919` → IC=+0.183 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0919 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.5204` → IC=+0.187 (n=241)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5204 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2197` → IC=+0.163 (n=170)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.2197 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.4014` → IC=+0.156 (n=353)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.4014 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.337` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.337 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.39` → IC=+0.162 (n=391)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 2.39 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2719` → IC=+0.150 (n=361)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2719 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.8476` → IC=+0.187 (n=241)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.8476 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.3073` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3073 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4501` → IC=+0.175 (n=121)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4501 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.6819` → IC=+0.199 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6819 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `12465.6116` → IC=+0.192 (n=323)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 12465.6116 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.212 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1108` → IC=+0.172 (n=400)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1108 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.172 (n=401)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1409 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6091` → IC=+0.142 (n=412)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6091 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.7048` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7048 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.158 (n=886)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8811` → IC=+0.183 (n=606)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8811 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.163 (n=428)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4209` → IC=+0.141 (n=302)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4209 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.143 (n=603)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `11328.3365` → IC=+0.147 (n=908)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11328.3365 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `712.0` → IC=+0.142 (n=862)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 712.0 (IC base=+0.135)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.5715` → IC=+0.174 (n=623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5715 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.3499` → IC=+0.170 (n=749)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3499 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.167 (n=622)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.165)

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
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.157 (n=843)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0087 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.160 (n=843)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0044 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1253` → IC=+0.154 (n=281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1253 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.162 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.172 (n=297)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 4.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.5529` → IC=+0.156 (n=562)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5529 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.8892` → IC=+0.168 (n=281)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8892 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.9899` → IC=+0.163 (n=197)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.9899 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.4235` → IC=+0.162 (n=777)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4235 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.126` → IC=+0.152 (n=139)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.126 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.678` → IC=+0.160 (n=844)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.678 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.7182` → IC=+0.154 (n=753)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7182 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.153 (n=776)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1724` → IC=+0.164 (n=248)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1724 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.2097` → IC=+0.157 (n=727)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.2097 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.5194` → IC=+0.152 (n=737)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5194 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=822)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.155 (n=708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0084 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.3946` → IC=+0.172 (n=622)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3946 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.153 (n=246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 4.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.1015` → IC=+0.153 (n=707)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.1015 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.6221` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6221 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.3863` → IC=+0.144 (n=709)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.3863 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.98` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.98 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.142 (n=641)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.0948` → IC=+0.152 (n=622)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0948 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.7218` → IC=+0.143 (n=632)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.7218 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.173 (n=301)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.155 (n=610)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.7743` → IC=+0.157 (n=462)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7743 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `7600.4466` → IC=+0.166 (n=707)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 7600.4466 (IC base=+0.141)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 1.0 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.097` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.097 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.1567` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1567 (IC base=+0.076)

- **PATRÓN** `libro_liquidez` > `3398.8602` → IC=+0.128 (n=170)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3398.8602 (IC base=+0.076)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.224 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.094)

- **PATRÓN** `drift_60min` |x|≤ `0.5393` → IC=+0.129 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5393 (IC base=+0.094)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.144 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 10.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.1538` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1538 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.699` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 2.699 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` < `0.0881` → IC=+0.151 (n=144)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0881 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `3218.3001` → IC=+0.135 (n=187)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3218.3001 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 56.0 (IC base=+0.094)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.210 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=343)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.196 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=345)

- **FILTRO** `dist_vwap_pct` > `0.1781` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1781
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=286)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.213 (n=371)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.128 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.5536` → IC=+0.183 (n=746)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5536 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1475` → IC=+0.155 (n=413)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1475 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.216 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.216 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `2.0983` → IC=+0.142 (n=559)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.0983 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=603)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2432.8034` → IC=+0.148 (n=328)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2432.8034 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.256 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.0685` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0685 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.132 (n=207)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.5975 (IC base=-0.005)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.277 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.5656` → IC=+0.194 (n=256)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.5656 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `1.0669` → IC=+0.123 (n=226)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0669 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` < `0.0651` → IC=+0.132 (n=191)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.0651 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.2692` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2692 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.189 (n=191)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=261)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `3986.8232` → IC=+0.134 (n=110)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3986.8232 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.0889` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0889 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.5944` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.5944 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.0664` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0664 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.045)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.257 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=106)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=106)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.200 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.136 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.5536` → IC=+0.204 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5536 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.1269` → IC=+0.160 (n=142)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1269 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.815` → IC=+0.295 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.815 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.126 (n=228)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6396 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `2.456` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.456 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=268)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `1606.9963` → IC=+0.181 (n=114)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1606.9963 (IC base=+0.106)

- **PATRÓN** `drift_60min` |x|≤ `0.1272` → IC=+0.160 (n=48)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1272 (IC base=-0.025)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1269` → IC=+0.128 (n=84)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1269 (IC base=-0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.791` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 2.791 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.1373` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1373 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.637` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.637 (IC base=-0.025)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=-0.025)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.2381` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=59)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.069)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.130 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 13.0 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.176 (n=211)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6842 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1957` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1957 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.244` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.244 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0847` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0847 (IC base=+0.069)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=-0.057)

- **PATRÓN** `ibs_20min` < `0.0882` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0882 (IC base=-0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.174` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 2.174 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1012` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1012 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `1.4069` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4069 (IC base=-0.057)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `9.0` → IC=-0.396 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=147)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=178)

- **FILTRO** `volumen_regimen` < `0.7431` → IC=-0.361 (n=63)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7431
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=130)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=139)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=130)

- **FILTRO** `volumen_pendiente_norm` > `0.0765` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0765
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=59)

- **FILTRO** `volumen_spike_ratio` > `2.0323` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.0323
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=58)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=53)

- **FILTRO** `ibs_20min` < `0.0329` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` < 0.0329
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=46)

- **FILTRO** `volumen_spike_ratio` > `3.5274` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.5274
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=30)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.292 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.305 (n=39)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=28)

- **FILTRO** `volumen_regimen` > `0.807` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.807
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33)

- **FILTRO** `volumen_regimen` > `0.8808` → IC=-0.235 (n=32)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8808
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=33)

- **FILTRO** `volumen_regimen` > `0.5614` → IC=-0.361 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.5614
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=44)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

- **FILTRO** `volumen_regimen` < `1.0683` → IC=-0.431 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0683
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2059` → IC=-0.129 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2059
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=222)

- **FILTRO** `dist_vwap_pct` > `0.6296` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6296
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=310)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.127 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.082)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.161 (n=237)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.6522 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.4724` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.4724 (IC base=+0.082)

- **PATRÓN** `ibs_20min` < `0.2059` → IC=+0.120 (n=222)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.2059 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `3761.0521` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3761.0521 (IC base=+0.035)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.557` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.557
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=77)

- **FILTRO** `volumen_regimen` < `0.7797` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7797
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=77)

- **PATRÓN** `volumen_spike_ratio` > `1.4652` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4652 (IC base=-0.019)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1361 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.1782` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1782 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.8706` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.8706 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `3566.36` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3566.36 (IC base=+0.097)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.8361` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8361
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=55)

- **FILTRO** `ibs_20min` > `0.3115` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3115
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=81)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0042 (IC base=+0.059)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.125 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.059)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.239 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.059)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.8361 (IC base=+0.059)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.005)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=40)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.214 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.186 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0081 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.176 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.7619` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7619 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.7975` → IC=+0.265 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7975 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.06 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.044)

### LATE_WINDOW_5MIN
- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.300)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.8446` → IC=+0.382 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8446 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `1767.0` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1767.0 (IC base=+0.300)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.300)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.8446` → IC=+0.382 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8446 (IC base=+0.300)

- **PATRÓN** `ballena_activa_n` < `1767.0` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1767.0 (IC base=+0.300)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.134 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 16.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=643)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2874.277` → IC=+0.164 (n=218)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2874.277 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.134 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 16.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=643)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2874.277` → IC=+0.164 (n=218)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2874.277 (IC base=+0.107)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=77)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=111)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=130)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=203)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=189)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1629)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=76)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=81)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.167 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=62)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `29085.84` → IC=-0.151 (n=41)

  - _Acción_: SKIP cuando `liq_usd_total` < 29085.84
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=123)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `ballena_activa_n` > `569.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 569.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_n` > `18.0` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.036)

- **PATRÓN** `liq_usd_total` > `80505.33` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `liq_usd_total` > 80505.33 (IC base=+0.036)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.036)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9778` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9778
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=99)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=725)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=426)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=131)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9109` → IC=-0.140 (n=48)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9109
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=99)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.122 (n=72)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=75)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=480)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=324)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=324)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=170)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=170)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.138 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=140)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.123 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=58)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=192)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=83)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=76)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=231)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=231)

- **FILTRO** `libro_liquidez` < `730.7333` → IC=-0.121 (n=130)

  - _Acción_: SKIP cuando `libro_liquidez` < 730.7333
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=131)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7319)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.175 (n=3156)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=10019)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.172 (n=3405)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=10232)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.216 (n=561)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1711)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.174 (n=559)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1878)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.203 (n=577)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=1739)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.207 (n=598)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=1834)

- **FILTRO** `ibs_20min` > `0.2842` → IC=-0.163 (n=607)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2842
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1825)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.177 (n=550)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1706)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.182 (n=602)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1826)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=2668)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=2816)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=2822)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.173 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=354)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.125 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=340)

- **FILTRO** `libro_liquidez` < `16874.9653` → IC=-0.142 (n=213)

  - _Acción_: SKIP cuando `libro_liquidez` < 16874.9653
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=642)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=231)

- **FILTRO** `ibs_20min` < `0.1008` → IC=-0.250 (n=74)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1008
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=225)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=214)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=745)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=9434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=20951)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=7357)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=23028)

- **FILTRO** `ibs_7min` < `0.2903` → IC=-0.235 (n=7589)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2903
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=22796)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=10301)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=20084)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.229 (n=9407)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=28530)

- **FILTRO** `ibs_7min` > `0.2941` → IC=-0.180 (n=9438)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=28499)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=1544)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=3445)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.306 (n=1189)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3800)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.251 (n=1645)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3344)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.184 (n=1163)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3826)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.260 (n=1625)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=4906)

- **FILTRO** `drift_7min_pct` |x|> `0.1121` → IC=-0.125 (n=2217)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1121
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4314)

- **FILTRO** `ibs_7min` > `0.7925` → IC=-0.205 (n=1632)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7925
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=4899)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=4034)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1262)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4009)

- **FILTRO** `ibs_7min` < `0.7501` → IC=-0.191 (n=1317)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7501
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3954)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.172 (n=1313)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3958)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.256 (n=1309)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3992)

- **FILTRO** `ibs_7min` > `0.2588` → IC=-0.176 (n=1325)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2588
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3976)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.187 (n=1324)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3977)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.169 (n=1352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=3375)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.309 (n=1155)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=3572)

- **FILTRO** `ibs_7min` < `0.1961` → IC=-0.261 (n=1180)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1961
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3547)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.214 (n=1116)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3611)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.238 (n=1615)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=5354)

- **FILTRO** `ibs_7min` > `0.7539` → IC=-0.179 (n=1742)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7539
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5227)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.240 (n=1228)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3779)

- **FILTRO** `ibs_7min` < `0.7428` → IC=-0.180 (n=1251)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7428
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3756)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.170 (n=1226)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3781)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.264 (n=1129)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=3965)

- **FILTRO** `ibs_7min` > `0.2745` → IC=-0.173 (n=1273)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2745
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3821)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.191 (n=1245)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3849)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.262 (n=1264)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=4066)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.240 (n=1307)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4023)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.179 (n=1728)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=5479)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=1195)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3866)

- **FILTRO** `ibs_7min` < `0.7037` → IC=-0.228 (n=1264)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7037
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=3797)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.212 (n=1215)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3846)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.203 (n=1669)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=5166)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1046)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=520)

- **FILTRO** `libro_liquidez` < `10575.5071` → IC=-0.143 (n=141)

  - _Acción_: SKIP cuando `libro_liquidez` < 10575.5071
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=425)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=635)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=323)

- **FILTRO** `ballena_activa_n` > `2.0` → IC=-0.138 (n=139)

  - _Acción_: SKIP cuando `ballena_activa_n` > 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=286)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=544)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.145 (n=477)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `464.449` → IC=+0.150 (n=238)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 464.449 (IC base=+0.115)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.138 (n=56)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.142 (n=146)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 445.688 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 13.0 (IC base=+0.132)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.121 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.096)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.173 (n=96)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.093)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 69.0 (IC base=+0.093)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.175 (n=124)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.205 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `6272.013` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 6272.013 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 34.0 (IC base=+0.141)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.151 (n=127)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.143 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 13.0 (IC base=+0.108)

- **PATRÓN** `total_vol_5m` < `258575.4` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 258575.4 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `3729.2002` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3729.2002 (IC base=+0.108)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.309 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=172)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.352 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=53)

- **FILTRO** `T_h` > `87.9936` → IC=-0.429 (n=26)

  - _Acción_: SKIP cuando `T_h` > 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=79)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.203 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.145)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0142` → IC=-0.206 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=49)

- **FILTRO** `T_h` < `39.9942` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` < 39.9942
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=48)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.8381` → IC=-0.243 (n=177)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8381
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=178)

- **FILTRO** `pct_vs_K` |x|> `3.3729` → IC=-0.442 (n=101)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3729
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=197)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `0.8662` → IC=-0.244 (n=80)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 0.8662
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=45)

- **FILTRO** `T_h` > `144.5878` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `T_h` > 144.5878
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=81)

- **FILTRO** `T_h` < `96.6729` → IC=-0.361 (n=34)

  - _Acción_: SKIP cuando `T_h` < 96.6729
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=72)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `71.1632` → IC=-0.210 (n=74)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=25)

- **FILTRO** `pct_vs_K` |x|> `2.4552` → IC=-0.360 (n=48)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4552
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=51)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.308 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=74)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.385 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=74)

- **FILTRO** `T_h` > `53.9898` → IC=-0.313 (n=73)

  - _Acción_: SKIP cuando `T_h` > 53.9898
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0144` → IC=-0.182 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0144
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=62)

- **FILTRO** `T_h` > `135.1308` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `T_h` > 135.1308
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=55)

- **FILTRO** `pct_vs_K` |x|> `5.0222` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.0222
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=62)

- **FILTRO** `sigma_h` < `0.015` → IC=-0.367 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.015
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `T_h` > `63.9197` → IC=-0.389 (n=43)

  - _Acción_: SKIP cuando `T_h` > 63.9197
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=15)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.131` → IC=+0.463 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.131 (IC base=+0.389)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.473 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.389)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.446 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.389)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.389)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.466 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.389)

- **PATRÓN** `edge` > `0.1011` → IC=+0.460 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1011 (IC base=+0.425)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.464 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.425)

- **PATRÓN** `T_h` > `1.0863` → IC=+0.440 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.0863 (IC base=+0.425)

- **PATRÓN** `dist_50` > `0.4077` → IC=+0.484 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4077 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.451 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.425)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.2492` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2492 (IC base=+0.439)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.458 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.439)

- **PATRÓN** `T_h` < `0.7452` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7452 (IC base=+0.439)

- **PATRÓN** `T_h` > `0.7452` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7452 (IC base=+0.439)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.417 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.439)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.480)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.471 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.480)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.471 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.480)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.480)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.480)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.480)

- **PATRÓN** `edge` > `0.1` → IC=+0.476 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.475)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.476 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.475)

- **PATRÓN** `T_h` > `0.9332` → IC=+0.473 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9332 (IC base=+0.475)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.487 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.475)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.464 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.475)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.466 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.475)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=157)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=277)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.023)

- **PATRÓN** `streak_estiramiento` < `0.4095` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4095 (IC base=+0.036)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4152` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4152
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=24)

- **FILTRO** `ballena_activa_n` > `52.0` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 52.0
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=33)

- **PATRÓN** `volumen_racha` < `990711.2` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_racha` < 990711.2 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 52.0 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 34.0 (IC base=+0.054)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=77)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=87)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=700)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=706)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=376)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `libro_liquidez` < `3086.3665` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 3086.3665
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=557)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1108)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=689)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=680)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2766)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1416)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1424)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.228 (n=663)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.1615` → IC=+0.194 (n=1287)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1615 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2162` → IC=+0.191 (n=487)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2162 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3318` → IC=+0.215 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3318 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=1357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.186 (n=1484)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 16.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6087` → IC=+0.261 (n=1462)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6087 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.4551` → IC=+0.192 (n=355)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.4551 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.881` → IC=+0.269 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.881 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `2985.1852` → IC=+0.190 (n=975)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2985.1852 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=518)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.210 (n=343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.286 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.197)

- **PATRÓN** `drift_15min` |x|≤ `0.3806` → IC=+0.209 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3806 (IC base=+0.197)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2571` → IC=+0.241 (n=114)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2571 (IC base=+0.197)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1462` → IC=+0.250 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1462 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.229 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.197)

- **PATRÓN** `ibs_15` > `0.7031` → IC=+0.262 (n=342)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7031 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.503` → IC=+0.251 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.503 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `15928.6386` → IC=+0.233 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15928.6386 (IC base=+0.197)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `25.169` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 25.169
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=330)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.144 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0035 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.167 (n=232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0051 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.069` → IC=+0.158 (n=153)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.069 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.178 (n=116)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.141)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2561` → IC=+0.171 (n=244)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2561 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` > `0.6675` → IC=+0.238 (n=311)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6675 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.5575` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.5575 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.159 (n=271)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.389` → IC=+0.203 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.389 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3459.7073` → IC=+0.152 (n=311)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3459.7073 (IC base=+0.141)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=75)

- **PATRÓN** `drift_60min` |x|≤ `0.1422` → IC=+0.122 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.1422 (IC base=-0.019)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.258 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.204 (n=157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.165)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0662` → IC=+0.196 (n=159)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.0662 (IC base=+0.165)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2836` → IC=+0.223 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2836 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.205 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.165)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.250 (n=178)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.1219` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1219 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=138)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `3004.732` → IC=+0.271 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.732 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.165)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.7049` → IC=-0.146 (n=97)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.7049
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=801)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `16.21` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.21 (IC base=+0.019)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0176` → IC=+0.238 (n=265)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0176 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.206 (n=175)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.187)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0626` → IC=+0.200 (n=355)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0626 (IC base=+0.187)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0898` → IC=+0.257 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0898 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.235 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.187)

- **PATRÓN** `ibs_15` > `0.55` → IC=+0.282 (n=397)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.55 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.1272` → IC=+0.206 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1272 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.916` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.916 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.408` → IC=+0.189 (n=355)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 7.408 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `2889.776` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2889.776 (IC base=+0.187)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.162 (n=439)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` < 0.1176 (IC base=+0.045)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.333 (n=261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.371 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1089` → IC=+0.340 (n=261)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1089 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1462` → IC=+0.359 (n=260)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1462 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.369 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.356 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7856` → IC=+0.378 (n=390)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7856 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.4267` → IC=+0.377 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4267 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.334 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.085` → IC=+0.343 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.085 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.334 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.340 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3532.3524` → IC=+0.349 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3532.3524 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `475.0` → IC=+0.356 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 475.0 (IC base=+0.333)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.346 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.367 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.353 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.336)

- **PATRÓN** `drift_15min` |x|≤ `0.4288` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4288 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.346 (n=219)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1231` → IC=+0.378 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1231 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.363 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.373 (n=219)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.408 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.381` → IC=+0.346 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.381 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.338 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `15613.0471` → IC=+0.340 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15613.0471 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `582.0` → IC=+0.384 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 582.0 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.377 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.327)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.338 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.327)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.346 (n=154)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.327)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.353 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.327)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.389 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.327)

- **PATRÓN** `ibs_15` > `0.7403` → IC=+0.385 (n=172)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7403 (IC base=+0.327)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.362 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.327)

- **PATRÓN** `dist_vwap_pct` < `0.1227` → IC=+0.338 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1227 (IC base=+0.327)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.717` → IC=+0.339 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.717 (IC base=+0.327)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.331 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.327)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.342 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.327)

- **PATRÓN** `libro_liquidez` > `3546.8859` → IC=+0.355 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3546.8859 (IC base=+0.327)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0131` → IC=-0.215 (n=619)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0131
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1861)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.190 (n=817)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1663)

- **FILTRO** `libro_liquidez` < `3921.5421` → IC=-0.135 (n=1636)

  - _Acción_: SKIP cuando `libro_liquidez` < 3921.5421
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=844)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.249 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.061)

- **PATRÓN** `ibs_15` > `0.6326` → IC=+0.266 (n=605)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6326 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` > `0.5693` → IC=+0.175 (n=115)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.5693 (IC base=-0.061)

- **PATRÓN** `dist_vwap_pct` < `0.2727` → IC=+0.177 (n=475)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.2727 (IC base=-0.061)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1175` → IC=+0.236 (n=1034)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1175 (IC base=-0.038)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1784` → IC=+0.240 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1784 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.280 (n=1549)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.6644` → IC=+0.289 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6644 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.218 (n=377)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1134)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.226 (n=498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1013)

- **FILTRO** `sigma_ewma_delta_pct` > `19.79` → IC=-0.252 (n=268)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.79
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1243)

- **FILTRO** `libro_liquidez` < `16225.701` → IC=-0.203 (n=997)

  - _Acción_: SKIP cuando `libro_liquidez` < 16225.701
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=514)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.171 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0028 (IC base=+0.074)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.273 (n=73)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.074)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.074)

- **PATRÓN** `ibs_15` > `0.7374` → IC=+0.315 (n=160)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7374 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.284 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.536` → IC=+0.270 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.536 (IC base=+0.074)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6647` → IC=-0.194 (n=96)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6647
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=368)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.187 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0051 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.215 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.4253` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.4253 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1329` → IC=+0.162 (n=193)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.1329 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.239 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.260 (n=289)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6422` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6422 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1187` → IC=+0.179 (n=207)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1187 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.951` → IC=+0.156 (n=245)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 8.951 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=368)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.192 (n=131)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.240 (n=626)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.227)

- **PATRÓN** `drift_15min` |x|≤ `0.778` → IC=+0.236 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.778 (IC base=+0.227)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.245 (n=284)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.227 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.246 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.227)

- **PATRÓN** `ibs_15` < `0.2705` → IC=+0.283 (n=551)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2705 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.7574` → IC=+0.304 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7574 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.01` → IC=+0.250 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.01 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.254` → IC=+0.232 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.254 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `3546.5572` → IC=+0.229 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3546.5572 (IC base=+0.227)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.228 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=436)

- **FILTRO** `drift_60min` |x|> `0.1671` → IC=-0.224 (n=197)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1671
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=384)

- **FILTRO** `drift_15min` |x|> `0.8849` → IC=-0.255 (n=145)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8849
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=436)

- **FILTRO** `sigma_ewma_delta_pct` > `18.011` → IC=-0.131 (n=310)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.011
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2505)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.162)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.162)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0761` → IC=+0.218 (n=257)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0761 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3542` → IC=+0.259 (n=288)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3542 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` > `0.4766` → IC=+0.200 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4766 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.215 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0198` → IC=-0.256 (n=371)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=373)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.263 (n=184)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=560)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1531` → IC=+0.271 (n=142)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1531 (IC base=-0.047)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.356 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.047)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.308 (n=426)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` > `1.111` → IC=+0.373 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.111 (IC base=-0.047)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.190 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `13168.0076` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 13168.0076 (IC base=+0.061)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.190 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `13168.0076` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 13168.0076 (IC base=+0.061)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.294 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.288 (n=286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.311 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.302 (n=210)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1084` → IC=+0.340 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1084 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8404` → IC=+0.323 (n=630)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8404 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4435` → IC=+0.331 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4435 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.326 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.290 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `12879.5491` → IC=+0.302 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12879.5491 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.314 (n=116)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.281 (n=158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.339 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `0.3889` → IC=+0.280 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3889 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.297 (n=116)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3724` → IC=+0.296 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3724 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.311 (n=348)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.4264` → IC=+0.360 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4264 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `15946.6772` → IC=+0.331 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15946.6772 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.300 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.113` → IC=+0.296 (n=189)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.113 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.310 (n=188)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.332 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.328 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8475` → IC=+0.335 (n=282)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8475 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` < `0.456` → IC=+0.293 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.456 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.167` → IC=+0.313 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.167 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.042` → IC=+0.292 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.042 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2669` → IC=-0.181 (n=67)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2669
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=205)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1131` → IC=-0.171 (n=68)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1131
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=204)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.121` → IC=-0.164 (n=105)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.121
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=327)

- **FILTRO** `drift_15min` |x|> `0.4386` → IC=-0.135 (n=146)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4386
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=286)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1445` → IC=-0.148 (n=52)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1445
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=106)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.262 (n=19)
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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `74.1058` → IC=+0.187 (n=266)

  - _Acción_: Kelly boost +0.93€ cuando `T_h` > 74.1058 (IC base=+0.180)

- **PATRÓN** `ratio` < `0.9766` → IC=+0.464 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9766 (IC base=+0.180)

- **PATRÓN** `T_h` > `145.7998` → IC=+0.399 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7998 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0449` → IC=+0.394 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0449 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.2203` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 144.2203 (IC base=+0.148)

- **PATRÓN** `ratio` < `0.9922` → IC=+0.328 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.148)

- **PATRÓN** `T_h` < `111.9936` → IC=+0.293 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9936 (IC base=+0.289)

- **PATRÓN** `T_h` > `98.1369` → IC=+0.295 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 98.1369 (IC base=+0.289)

- **PATRÓN** `ratio` > `1.0449` → IC=+0.417 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0449 (IC base=+0.289)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9957` → IC=+0.246 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.230)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.404 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.230)

- **PATRÓN** `T_h` > `102.672` → IC=+0.333 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.672 (IC base=+0.312)

- **PATRÓN** `ratio` > `1.0088` → IC=+0.321 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0088 (IC base=+0.312)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1402` → IC=+0.455 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1402 (IC base=+0.404)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6087 sube el IC de +0.186 a +0.261 en UPDOWN_GBM#15min (n=1462). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7031 sube el IC de +0.197 a +0.262 en UPDOWN_GBM#BTC#15min (n=342). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6675 sube el IC de +0.141 a +0.238 en UPDOWN_GBM#ETH#15min (n=311). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.165 a +0.250 en UPDOWN_GBM#SOL#15min (n=178). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.55 sube el IC de +0.187 a +0.282 en UPDOWN_GBM#XRP#15min (n=397). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.045 a +0.162 en UPDOWN_GBM#XRP#15min (n=439). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6326 sube el IC de -0.061 a +0.266 en UPDOWN_GBM_15M_TARDIO (n=605). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.038 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1549). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7374 sube el IC de +0.074 a +0.315 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=160). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.146 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=289). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2705 sube el IC de +0.227 a +0.283 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=551). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.162 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3542 sube el IC de -0.044 a +0.259 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=288). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.047 a +0.308 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=426). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8404 sube el IC de +0.287 a +0.323 en UPDOWN_GBM_IBS_ALTO (n=630). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.281 a +0.311 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=348). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8475 sube el IC de +0.294 a +0.335 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=282). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7856 sube el IC de +0.333 a +0.378 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.336 a +0.373 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=219). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7403 sube el IC de +0.327 a +0.385 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=172). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1265 | +0.093 | +165.01€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1265 | +0.093 | +165.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 936 | +0.102 | +139.82€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 936 | +0.102 | +139.82€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 243 | +0.047 | +6.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 243 | +0.047 | +6.54€ | 3 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 6 |
| ✅ BALLENAS_TARDIAS | 23912 | -0.091 | -3088.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1416 | -0.046 | -216.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 22496 | -0.094 | -2872.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3565 | -0.084 | -573.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3565 | -0.084 | -573.90€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1416 | -0.046 | -216.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1416 | -0.046 | -216.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6863 | -0.026 | -603.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6863 | -0.026 | -603.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6355 | -0.095 | -421.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6355 | -0.095 | -421.52€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5339 | -0.183 | -1112.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5339 | -0.183 | -1112.43€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 16502 | -0.030 | +4118.24€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4330 | -0.000 | +1832.38€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 12172 | -0.041 | +2285.86€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 16502 | -0.030 | +4118.24€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4330 | -0.000 | +1832.38€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 12172 | -0.041 | +2285.86€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1448 | -0.103 | -190.09€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1280 | -0.109 | -168.73€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 470 | -0.129 | -78.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 446 | -0.132 | -73.35€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 57 | -0.161 | -4.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 87681 | +0.113 | -4468.51€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 13390 | +0.184 | -435.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 348 | -0.094 | -48.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 68161 | +0.100 | -3792.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5782 | +0.110 | -191.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 11342 | +0.098 | -987.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 44 | -0.174 | -3.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 11283 | +0.099 | -972.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 17734 | +0.132 | -376.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4185 | +0.202 | -147.15€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 11298 | +0.111 | -185.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2209 | +0.107 | -22.12€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 11382 | +0.089 | -1078.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 51 | -0.085 | -5.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 11316 | +0.090 | -1061.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 18689 | +0.123 | -383.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5176 | +0.175 | -82.59€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 11412 | +0.105 | -240.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2089 | +0.098 | -51.57€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 17175 | +0.115 | -978.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3890 | +0.188 | -205.60€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 251 | -0.053 | +5.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 11550 | +0.092 | -660.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1484 | +0.129 | -118.05€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 11359 | +0.102 | -663.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 44 | -0.022 | +8.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 11302 | +0.102 | -672.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 13905 | +0.192 | -900.86€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 13905 | +0.192 | -900.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3339 | +0.168 | -352.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3339 | +0.168 | -352.83€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1061 | +0.196 | -2.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1061 | +0.196 | -2.96€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3274 | +0.182 | -273.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3274 | +0.182 | -273.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2935 | +0.238 | -96.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2935 | +0.238 | -96.45€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3217 | +0.194 | -189.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3217 | +0.194 | -189.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 656 | +0.429 | -19.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 656 | +0.429 | -19.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 250 | +0.432 | -4.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 250 | +0.432 | -4.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 247 | +0.436 | -2.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 247 | +0.436 | -2.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 151 | +0.402 | -11.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 151 | +0.402 | -11.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 47728 | +0.198 | -3707.47€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 47728 | +0.198 | -3707.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8271 | +0.176 | -965.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8271 | +0.176 | -965.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 7617 | +0.225 | -264.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 7617 | +0.225 | -264.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8238 | +0.175 | -970.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8238 | +0.175 | -970.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7710 | +0.220 | -292.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7710 | +0.220 | -292.11€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 7880 | +0.204 | -511.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 7880 | +0.204 | -511.83€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8012 | +0.193 | -703.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8012 | +0.193 | -703.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 17983 | +0.118 | +142.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 17983 | +0.118 | +142.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 8923 | +0.122 | +123.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 8923 | +0.122 | +123.27€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9060 | +0.114 | +18.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9060 | +0.114 | +18.87€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1406 | +0.293 | -3.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1406 | +0.293 | -3.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 627 | +0.277 | -15.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 627 | +0.277 | -15.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 675 | +0.298 | +10.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 675 | +0.298 | +10.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 104 | +0.340 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 104 | +0.340 | +1.79€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 617 | +0.439 | +0.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 617 | +0.439 | +0.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 292 | +0.439 | +0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 292 | +0.439 | +0.19€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 285 | +0.441 | +0.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 285 | +0.441 | +0.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 40 | +0.381 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 40 | +0.381 | -0.11€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1044 | +0.075 | -41.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 364 | +0.063 | -27.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 680 | +0.082 | -13.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 821 | +0.083 | -14.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 141 | +0.087 | -1.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 680 | +0.082 | -13.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 162 | +0.018 | -29.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 162 | +0.018 | -29.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 32917 | +0.097 | -1033.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2728 | +0.090 | +20.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 30189 | +0.098 | -1054.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 18548 | +0.102 | -302.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2728 | +0.090 | +20.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 15820 | +0.104 | -323.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6084 | +0.106 | -48.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6084 | +0.106 | -48.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 8285 | +0.081 | -682.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 8285 | +0.081 | -682.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 774 | +0.219 | -94.91€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 774 | +0.219 | -94.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 774 | +0.219 | -94.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 774 | +0.219 | -94.91€ | 2 | 4 |
| ✅ GBM_LATE_15M | 23830 | +0.081 | +11167.93€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 23830 | +0.081 | +11167.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3959 | +0.193 | +2865.98€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3959 | +0.193 | +2865.98€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 3538 | +0.175 | +2412.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3538 | +0.175 | +2412.99€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 4109 | +0.201 | +3101.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4109 | +0.201 | +3101.03€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 3542 | +0.016 | +693.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3542 | +0.016 | +693.19€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3451 | -0.033 | +788.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3451 | -0.033 | +788.48€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 5231 | -0.044 | +1306.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5231 | -0.044 | +1306.26€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 25198 | +0.084 | +13125.91€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 25198 | +0.084 | +13125.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4784 | +0.014 | +2584.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4784 | +0.014 | +2584.87€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5261 | +0.012 | +1048.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5261 | +0.012 | +1048.04€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3563 | +0.262 | +3589.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3563 | +0.262 | +3589.93€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4067 | -0.001 | +743.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4067 | -0.001 | +743.13€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4100 | +0.025 | +1533.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4100 | +0.025 | +1533.43€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3423 | +0.274 | +3626.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3423 | +0.274 | +3626.52€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 19275 | +0.168 | +14223.04€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 19275 | +0.168 | +14223.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2893 | +0.206 | +2291.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2893 | +0.206 | +2291.19€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3070 | +0.147 | +2180.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3070 | +0.147 | +2180.88€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3004 | +0.211 | +2425.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3004 | +0.211 | +2425.27€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3234 | +0.134 | +2185.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3234 | +0.134 | +2185.04€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3598 | +0.113 | +2402.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3598 | +0.113 | +2402.50€ | 1 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3476 | +0.203 | +2738.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3476 | +0.203 | +2738.15€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4713 | +0.122 | +1889.85€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4713 | +0.122 | +1889.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 184 | +0.118 | +76.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1347 | +0.117 | +565.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1347 | +0.117 | +565.72€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 369 | +0.147 | +180.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1319 | +0.139 | +565.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1319 | +0.139 | +565.16€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 990 | +0.092 | +285.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 990 | +0.092 | +285.27€ | 2 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 504 | +0.134 | +216.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 504 | +0.134 | +216.54€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 23960 | +0.174 | +17587.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 23960 | +0.174 | +17587.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3781 | +0.218 | +3157.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3781 | +0.218 | +3157.66€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3758 | +0.148 | +2422.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3758 | +0.148 | +2422.41€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3901 | +0.227 | +3378.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3901 | +0.227 | +3378.81€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3887 | +0.136 | +2592.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3887 | +0.136 | +2592.75€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4215 | +0.110 | +2591.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4215 | +0.110 | +2591.10€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4418 | +0.203 | +3444.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4418 | +0.203 | +3444.29€ | 0 | 22 |
| ✅ GBM_LATE_5M | 6560 | +0.143 | +3629.35€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 6560 | +0.143 | +3629.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1691 | +0.139 | +1068.26€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1691 | +0.139 | +1068.26€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2065 | +0.147 | +1127.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2065 | +0.147 | +1127.13€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 502 | +0.085 | +136.57€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 502 | +0.085 | +136.57€ | 0 | 13 |
| ✅ GBM_LATE_5M#XRP | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 819 | +0.115 | +316.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1571 | +0.066 | +669.62€ | 3 | 12 |
| ✅ GBM_LATE_60M#60min | 1571 | +0.066 | +669.62€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 567 | +0.087 | +234.63€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 567 | +0.087 | +234.63€ | 0 | 14 |
| ✅ GBM_LATE_60M#ETH | 522 | +0.071 | +260.34€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 522 | +0.071 | +260.34€ | 2 | 18 |
| ✅ GBM_LATE_60M#SOL | 482 | +0.035 | +174.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 482 | +0.035 | +174.66€ | 1 | 11 |
| 🚫 GBM_LATE_60M_FADE | 353 | -0.258 | -25.21€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 353 | -0.258 | -25.21€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 135 | -0.223 | -10.82€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 135 | -0.223 | -10.82€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 116 | -0.263 | -9.13€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 116 | -0.263 | -9.13€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 102 | -0.288 | -5.26€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 102 | -0.288 | -5.26€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 650 | +0.058 | +124.28€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 650 | +0.058 | +124.28€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 254 | +0.051 | +45.16€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 254 | +0.051 | +45.16€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 189 | +0.029 | -3.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 189 | +0.029 | -3.13€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 207 | +0.093 | +82.24€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 207 | +0.093 | +82.24€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 90 | +0.250 | +68.82€ | 0 | 4 |
| ✅ LATE_WINDOW_5MIN#5min | 90 | +0.250 | +68.82€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 90 | +0.250 | +68.82€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 90 | +0.250 | +68.82€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M | 1784 | +0.097 | +480.88€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1784 | +0.097 | +480.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1784 | +0.097 | +480.88€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1784 | +0.097 | +480.88€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 370 | -0.083 | -35.15€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 370 | -0.083 | -35.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 94 | -0.062 | -5.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 94 | -0.062 | -5.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 128 | -0.031 | -5.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 128 | -0.031 | -5.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1827 | +0.005 | +13.69€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1827 | +0.005 | +13.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 96 | +0.000 | -2.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 96 | +0.000 | -2.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 198 | +0.000 | +13.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 198 | +0.000 | +13.72€ | 3 | 3 |
| ✅ LIQUIDACIONES_5M#DOGE | 135 | -0.047 | -7.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 135 | -0.047 | -7.81€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 772 | +0.031 | +25.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 772 | +0.031 | +25.36€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 466 | -0.002 | -5.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 466 | -0.002 | -5.97€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 160 | -0.049 | -8.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 160 | -0.049 | -8.66€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M | 1027 | -0.045 | -27.59€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1027 | -0.045 | -27.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 294 | -0.041 | -12.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 294 | -0.041 | -12.15€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 340 | -0.035 | -4.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 340 | -0.035 | -4.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 393 | -0.057 | -11.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 393 | -0.057 | -11.12€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 62 | -0.047 | -3.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 27 | -0.017 | +0.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 35 | -0.068 | -3.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 20 | -0.091 | -5.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 9 | -0.021 | -1.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 11 | -0.064 | -3.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 6 | +0.000 | +0.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 11 | -0.064 | -1.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 5 | -0.018 | -0.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 6 | -0.037 | -0.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 9 | +0.021 | +0.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 5 | -0.018 | -1.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 13 | -0.022 | +0.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 9 | +0.021 | +1.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 14183 | -0.012 | -208.25€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14183 | -0.012 | -208.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2900 | -0.022 | -61.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2900 | -0.022 | -61.43€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 26812 | -0.009 | +1140.12€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 26812 | -0.009 | +1140.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4709 | +0.015 | +573.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4709 | +0.015 | +573.98€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4201 | -0.028 | -53.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4201 | -0.028 | -53.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4748 | +0.013 | +406.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4748 | +0.013 | +406.66€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3980 | -0.053 | -144.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3980 | -0.053 | -144.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4490 | -0.013 | +166.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4490 | -0.013 | +166.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4684 | +0.005 | +191.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4684 | +0.005 | +191.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5585 | -0.055 | -135.85€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5585 | -0.055 | -135.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1203 | +0.000 | -15.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1305 | -0.072 | -32.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1305 | -0.072 | -32.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 577 | -0.123 | -24.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 577 | -0.123 | -24.12€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1610 | -0.076 | -32.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1610 | -0.076 | -32.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 847 | -0.016 | -25.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 847 | -0.016 | -25.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3343 | +0.005 | -1.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 68322 | -0.073 | +1595.41€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 68322 | -0.073 | +1595.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 11520 | -0.079 | +665.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 11520 | -0.079 | +665.53€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 10572 | -0.093 | -480.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 10572 | -0.093 | -480.72€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 11696 | -0.069 | +613.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 11696 | -0.069 | +613.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 10101 | -0.093 | -133.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 10101 | -0.093 | -133.33€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 12537 | -0.049 | +360.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 12537 | -0.049 | +360.63€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 11896 | -0.062 | +569.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 11896 | -0.062 | +569.77€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6993 | -0.023 | -102.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6993 | -0.023 | -102.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1627 | -0.025 | -3.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1627 | -0.025 | -3.87€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1605 | -0.018 | -8.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1605 | -0.018 | -8.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1024 | -0.039 | -16.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1024 | -0.039 | -16.08€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1087 | +0.108 | +364.63€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 951 | +0.115 | +352.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 221 | +0.132 | +106.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 221 | +0.132 | +106.04€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 186 | +0.096 | +44.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 186 | +0.096 | +44.24€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 192 | +0.093 | +61.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 192 | +0.093 | +61.03€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 165 | +0.141 | +80.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 165 | +0.141 | +80.87€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 187 | +0.108 | +59.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 187 | +0.108 | +59.86€ | 0 | 5 |
| ✅ ORDER_FLOW_5M_REACTIVO | 404 | -0.052 | -39.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 404 | -0.052 | -39.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 87 | +0.017 | +7.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 87 | +0.017 | +7.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 52 | -0.130 | -16.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 52 | -0.130 | -16.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 117 | -0.080 | -23.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 117 | -0.080 | -23.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 76 | +0.013 | +4.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 76 | +0.013 | +4.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 72 | -0.095 | -12.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 72 | -0.095 | -12.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 528 | -0.094 | -27.18€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 241 | -0.138 | -47.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 193 | -0.182 | -50.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 183 | -0.084 | +1.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 139 | -0.096 | -6.48€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 104 | -0.009 | +18.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 82 | -0.024 | +12.23€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 414 | -0.123 | -44.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 653 | -0.210 | -35.95€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 268 | -0.200 | -30.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 231 | -0.195 | -30.34€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 229 | -0.227 | -23.00€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 197 | -0.239 | -27.66€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 156 | -0.196 | +17.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 140 | -0.197 | +13.11€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 568 | -0.212 | -44.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 265 | +0.418 | +211.36€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 69 | +0.401 | +61.26€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 69 | +0.401 | +61.26€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 168 | +0.482 | +154.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 168 | +0.482 | +154.85€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#sniper | 265 | +0.418 | +211.36€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 472 | +0.032 | +13.90€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 472 | +0.032 | +13.90€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 222 | +0.036 | +5.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 222 | +0.036 | +5.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 30 | +0.062 | +0.07€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 30 | +0.062 | +0.07€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 49 | -0.029 | -4.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 49 | -0.029 | -4.03€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 171 | +0.038 | +11.98€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 171 | +0.038 | +11.98€ | 2 | 4 |
| ✅ STREAK_FADE_5M | 2660 | -0.023 | -111.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2660 | -0.023 | -111.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 565 | -0.022 | -22.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 565 | -0.022 | -22.81€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1136 | -0.023 | -46.76€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1136 | -0.023 | -46.76€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 68 | -0.057 | -6.84€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 68 | -0.057 | -6.84€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 31 | -0.015 | -2.91€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 31 | -0.015 | -2.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7436 | +0.022 | +102.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7436 | +0.022 | +102.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1636 | +0.035 | +50.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1636 | +0.035 | +50.32€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2268 | +0.010 | -1.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2268 | +0.010 | -1.00€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1411 | +0.026 | +32.13€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1411 | +0.026 | +32.13€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6954 | +0.010 | -53.12€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6954 | +0.010 | -53.12€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2785 | +0.014 | -13.35€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2785 | +0.014 | -13.35€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2721 | +0.012 | -17.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2721 | +0.012 | -17.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1448 | +0.000 | -22.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1448 | +0.000 | -22.07€ | 2 | 0 |
| ✅ UPDOWN_GBM | 33710 | +0.031 | +1994.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 9063 | +0.064 | +1586.79€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1256 | +0.006 | +7.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 21221 | +0.021 | +377.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2043 | +0.009 | +24.06€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3265 | +0.067 | +337.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 507 | +0.148 | +196.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 28 | +0.000 | -0.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2730 | +0.052 | +141.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 6262 | +0.034 | +403.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1144 | +0.079 | +242.26€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 344 | +0.020 | +7.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3808 | +0.030 | +137.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 917 | +0.005 | +16.24€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 49 | -0.108 | +0.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3933 | +0.041 | +233.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 474 | +0.147 | +183.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 24 | +0.000 | -1.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3435 | +0.026 | +51.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 7168 | +0.019 | +289.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2385 | +0.045 | +267.27€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 332 | +0.006 | +7.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3712 | +0.007 | +11.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 698 | +0.007 | +0.70€ | 1 | 1 |
| ✅ UPDOWN_GBM#ETH#daily | 41 | -0.151 | +3.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8159 | +0.016 | +208.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2276 | +0.024 | +145.06€ | 0 | 11 |
| ✅ UPDOWN_GBM#SOL#240min | 325 | -0.005 | -2.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5095 | +0.015 | +61.87€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 428 | +0.019 | +7.12€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 35 | -0.176 | -2.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4921 | +0.036 | +522.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2277 | +0.078 | +551.78€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 203 | -0.002 | -2.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2441 | -0.001 | -26.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 125 | -0.146 | +0.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 520 | +0.333 | +145.77€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 520 | +0.333 | +145.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 291 | +0.336 | +77.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 291 | +0.336 | +77.61€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 229 | +0.327 | +68.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 229 | +0.327 | +68.16€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 11039 | -0.043 | +2274.01€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 11039 | -0.043 | +2274.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 646 | -0.048 | +326.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 646 | -0.048 | +326.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2072 | -0.124 | +23.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2072 | -0.124 | +23.80€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 293 | +0.171 | +184.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 293 | +0.171 | +184.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1219 | +0.202 | +704.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1219 | +0.202 | +704.70€ | 2 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3396 | -0.064 | +520.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3396 | -0.064 | +520.20€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3413 | -0.079 | +514.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3413 | -0.079 | +514.47€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 132 | +0.045 | +9.79€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 132 | +0.045 | +9.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 132 | +0.045 | +9.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 132 | +0.045 | +9.79€ | 2 | 3 |
| ✅ UPDOWN_GBM_IBS_ALTO | 839 | +0.287 | +667.87€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 839 | +0.287 | +667.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 463 | +0.281 | +344.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 463 | +0.281 | +344.01€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 376 | +0.294 | +323.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 376 | +0.294 | +323.85€ | 0 | 11 |
| ✅ UPDOWN_OU_5M | 704 | -0.106 | -79.18€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 704 | -0.106 | -79.18€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 197 | -0.063 | -11.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 197 | -0.063 | -11.26€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 69 | -0.162 | -8.81€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 69 | -0.162 | -8.81€ | 3 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 60 | -0.210 | -9.56€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 60 | -0.210 | -9.56€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2223 | +0.300 | +1106.87€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 761 | +0.248 | +106.26€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 820 | +0.288 | +332.38€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 642 | +0.376 | +668.23€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.020 n=444 — no justifica filtro, seguir monitorizando
  - _Datos_: n=444 IC=+0.020 PNL=+22.57€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 512 celda(s) pasan gate riguroso completo de 2165 evaluadas (n>=40) y 3175 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.024 < 0.08 — monitorear
  - _Datos_: n=2276 IC=+0.024 PNL=+145.06€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=820/15 IC=+0.288 PNL=+332.38€ | BTC: n=761/15 IC=+0.248 PNL=+106.26€ | SOL: n=642/15 IC=+0.376 PNL=+668.23€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.091 n=257/60 | contraria IC=+0.144 n=251 | gap=-0.054 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=270, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=697/40 IC=+0.006 PNL=+0.20€ | BTC#60min: n=916/40 IC=+0.004 PNL=+15.71€ | SOL#60min: n=428/40 IC=+0.019 PNL=+7.12€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.051 n=312927 | tras_1loss IC=+0.076 n=243600 | tras_2loss IC=+0.045 n=103129/40 | gap=+0.006 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=306 PNL=+195.93€
  - _Datos_: n=306 IC=+0.179 PNL=+195.93€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.08 con n=348 PNL=+249.00€
  - _Datos_: n=348 IC=+0.217 PNL=+249.00€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.269 > 0.08 con n=37 PNL=+31.71€
  - _Datos_: n=37 IC=+0.269 PNL=+31.71€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.331 > 0.1 con n=1845 PNL=+1054.70€
  - _Datos_: n=1845 IC=+0.331 PNL=+1054.70€

**🟡 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=257 PNL=+33.36€
  - _Datos_: n=257 IC=+0.087 PNL=+33.36€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=49 IC=+0.186 PNL=+32.29€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=49 IC=+0.186 PNL=+32.29€

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
  - _Estado_: n=1469 IC=+0.015 PNL=+11.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1469 IC=+0.015 PNL=+11.39€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=572 IC=-0.011 PNL=+11.64€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=572 IC=-0.011 PNL=+11.64€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=444 IC=+0.020 PNL=+22.57€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=444 IC=+0.020 PNL=+22.57€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.1 con n=1948 PNL=+1213.23€
  - _Datos_: n=1948 IC=+0.186 PNL=+1213.23€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1144 IC=+0.079 PNL=+242.26€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1144 IC=+0.079 PNL=+242.26€

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
  - _Estado_: n=495 IC=+0.007 PNL=+31.14€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=495 IC=+0.007 PNL=+31.14€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=46 IC=+0.062 PNL=+2.91€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=46 IC=+0.062 PNL=+2.91€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.250 n=90) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=90 IC=+0.250 PNL=+68.82€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.02 con n=622 PNL=+244.64€
  - _Datos_: n=622 IC=+0.125 PNL=+244.64€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: n=11644 IC=+0.056 PNL=+1447.28€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=11644 IC=+0.056 PNL=+1447.28€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.168 < -0.1 con n=212 PNL=+17.12€
  - _Datos_: n=212 IC=-0.168 PNL=+17.12€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1747 IC=+0.044 PNL=+180.05€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1747 IC=+0.044 PNL=+180.05€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=68 IC=-0.143 PNL=+2.20€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=68 IC=-0.143 PNL=+2.20€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.1 con n=362 PNL=+103.14€
  - _Datos_: n=362 IC=+0.126 PNL=+103.14€

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
  - _Estado_: n=16577 IC=-0.137 PNL=+1143.95€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=16577 IC=-0.137 PNL=+1143.95€

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
  - _Estado_: n=1802 IC=+0.138 PNL=+967.80€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1802 IC=+0.138 PNL=+967.80€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=3575 IC=+0.019 PNL=+111.02€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3575 IC=+0.019 PNL=+111.02€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=1944 PNL=+1013.10€
  - _Datos_: n=1944 IC=+0.086 PNL=+1013.10€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.237 < -0.1 con n=1632 PNL=-172.87€
  - _Datos_: n=1632 IC=-0.237 PNL=-172.87€

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
  - _Estado_: 34/40 ops en el filtro definido (IC actual=-0.028 PNL=+4.25€)
  - _Datos_: n=34 IC=-0.028 PNL=+4.25€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.088 n=915) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=915 IC=+0.088 PNL=+207.91€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=426) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=426 IC=+0.411 PNL=+599.27€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=8269 IC=+0.176 PNL=-964.34€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8269 IC=+0.176 PNL=-964.34€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=129 PNL=+76.64€
  - _Datos_: n=129 IC=+0.202 PNL=+76.64€
